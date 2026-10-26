import sys
import os
from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager

# Ensure both project root and api/ are importable in Vercel Serverless
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
for p in [current_dir, parent_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

from api.database import get_db, init_db
from api.seed_data import seed_database
from api.models import (
    CropItem,
    CompareRequest,
    CompareResponse,
    TrendsResponse,
    TrendPoint,
    DataStatusResponse
)
from api.calculations import (
    calculate_market_proceeds,
    rank_and_analyze_markets,
    is_record_stale
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        init_db()
        seed_database()
    except Exception as e:
        print(f"Database initialization error on startup: {e}")
    yield

app = FastAPI(
    title="MandiSell AgriTech API",
    description=(
        "MandiSell helps farmers compare agricultural market prices, account for real logistics "
        "and handling deductions, and identify the market with the highest net estimated proceeds.\n\n"
        "Tagline: **Know your market. Calculate your returns. Make informed decisions.**"
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS — allow everything for demo/hackathon
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Helper: ensure DB is ready on every request (idempotent) ──────────────────
def ensure_db():
    init_db()
    seed_database()

# ── 1. GET /health ────────────────────────────────────────────────────────────
@app.get("/health", tags=["System"])
def get_health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "MandiSell API",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "database": "sqlite",
        "mode": "Hackathon Demo (Sample Benchmark Feed)"
    }

# ── 2. GET /crops ─────────────────────────────────────────────────────────────
@app.get("/crops", response_model=List[CropItem], tags=["Master Data"])
def get_crops():
    """Returns all supported agricultural commodities with Hindi names and MSP benchmark."""
    ensure_db()
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, hindi_name, category, msp_price, unit FROM crops ORDER BY name ASC;"
        )
        return [dict(row) for row in cursor.fetchall()]

# ── 3. GET /districts ─────────────────────────────────────────────────────────
@app.get("/districts", tags=["Master Data"])
def get_districts(
    crop: Optional[str] = Query(default=None, description="Filter districts by crop availability")
):
    """Returns available districts, optionally filtered by crop."""
    ensure_db()
    with get_db() as conn:
        cursor = conn.cursor()
        if crop:
            # Extract raw string value if FastAPI wraps it
            crop_val = str(crop).strip()
            cursor.execute(
                """
                SELECT DISTINCT m.district, m.state
                FROM mandis m
                JOIN crop_prices cp ON m.id = cp.mandi_id
                WHERE LOWER(cp.crop_name) = LOWER(?)
                ORDER BY m.district ASC;
                """,
                (crop_val,)
            )
        else:
            cursor.execute(
                "SELECT DISTINCT district, state FROM mandis ORDER BY district ASC;"
            )
        return [{"district": r["district"], "state": r["state"]} for r in cursor.fetchall()]

# ── 4. GET /markets ───────────────────────────────────────────────────────────
@app.get("/markets", tags=["Markets & Prices"])
def get_markets(
    crop: str = Query(..., description="Crop name, e.g. Wheat"),
    district: str = Query(..., description="Farmer's base district, e.g. Patiala")
):
    """Retrieves market price quotes for the specified crop and district."""
    ensure_db()
    crop_val = str(crop).strip()
    district_val = str(district).strip()

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT
                m.id, m.name, m.district, m.state, m.distance_km,
                m.transport_rate_per_km_qtl, m.handling_charge_per_qtl, m.mandi_cess_percent,
                m.market_type, m.contact_phone, m.operating_hours,
                cp.crop_name, cp.min_price, cp.modal_price, cp.max_price,
                cp.arrival_tonnes, cp.price_date, cp.source, cp.is_sample_data
            FROM mandis m
            JOIN crop_prices cp ON m.id = cp.mandi_id
            WHERE LOWER(cp.crop_name) = LOWER(?) AND LOWER(m.district) = LOWER(?)
            ORDER BY cp.modal_price DESC;
            """,
            (crop_val, district_val)
        )
        rows = cursor.fetchall()

        if not rows:
            cursor.execute(
                "SELECT name FROM crops WHERE LOWER(name) = LOWER(?);", (crop_val,)
            )
            if not cursor.fetchone():
                raise HTTPException(
                    status_code=404,
                    detail=f"Crop '{crop}' is not currently indexed. Use GET /crops for supported crops."
                )
            cursor.execute(
                "SELECT district FROM mandis WHERE LOWER(district) = LOWER(?);", (district_val,)
            )
            if not cursor.fetchone():
                raise HTTPException(
                    status_code=404,
                    detail=f"No mandis registered in district '{district}'. Try 'Patiala', 'Ludhiana', 'Karnal', 'Indore', 'Nashik', or 'Agra'."
                )
            return {"message": f"No quotes for {crop} in {district}.", "crop": crop, "district": district, "markets": []}

        results = []
        for r in rows:
            rd = dict(r)
            rd["is_stale"] = is_record_stale(rd["price_date"])
            rd["is_sample_data"] = bool(rd["is_sample_data"])
            results.append(rd)

        return {"crop": crop, "district": district, "count": len(results), "markets": results}

# ── 5. POST /compare ──────────────────────────────────────────────────────────
@app.post("/compare", response_model=CompareResponse, tags=["Calculations & Rankings"])
def compare_markets(payload: CompareRequest):
    """Core comparison and ranking engine."""
    ensure_db()

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT
                m.id, m.name, m.district, m.state, m.distance_km,
                m.transport_rate_per_km_qtl, m.handling_charge_per_qtl, m.mandi_cess_percent,
                m.market_type, m.contact_phone,
                cp.min_price, cp.modal_price, cp.max_price,
                cp.arrival_tonnes, cp.price_date, cp.source, cp.is_sample_data
            FROM mandis m
            JOIN crop_prices cp ON m.id = cp.mandi_id
            WHERE LOWER(cp.crop_name) = LOWER(?) AND LOWER(m.district) = LOWER(?)
            """,
            (payload.crop.strip(), payload.district.strip())
        )
        rows = cursor.fetchall()

    if not rows:
        raise HTTPException(
            status_code=404,
            detail=f"No price records found for crop '{payload.crop}' in district '{payload.district}'."
        )

    evaluated_markets = [
        calculate_market_proceeds(
            raw_mandi_data=dict(row),
            quantity_quintals=payload.quantity_quintals,
            custom_transport_rates=payload.custom_transport_rates,
            custom_other_costs=payload.custom_other_costs_per_qtl
        )
        for row in rows
    ]

    ranked_markets, best_mandi, runner_up, diff_proceeds, diff_pct, explanation = rank_and_analyze_markets(
        evaluated_markets, payload.quantity_quintals
    )

    return CompareResponse(
        crop=payload.crop,
        district=payload.district,
        quantity_quintals=payload.quantity_quintals,
        markets_evaluated_count=len(ranked_markets),
        best_mandi=best_mandi,
        runner_up_mandi=runner_up,
        proceeds_advantage=diff_proceeds,
        proceeds_advantage_percentage=diff_pct,
        why_best_explanation=explanation,
        ranked_markets=ranked_markets,
        calculated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        data_notice="Simulated Benchmark Data for Hackathon Evaluation (Agmarknet/e-NAM model)."
    )

# ── 6. GET /prices/trends ─────────────────────────────────────────────────────
@app.get("/prices/trends", response_model=TrendsResponse, tags=["Historical Trends"])
def get_price_trends(crop: str = Query(..., description="Crop name, e.g. Wheat")):
    """Returns 30-day historical price trend data."""
    ensure_db()
    crop_val = str(crop).strip()

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT trend_date, modal_price, min_price, max_price, volume_tonnes
            FROM price_trends
            WHERE LOWER(crop_name) = LOWER(?)
            ORDER BY trend_date ASC;
            """,
            (crop_val,)
        )
        rows = cursor.fetchall()

    if not rows:
        raise HTTPException(status_code=404, detail=f"No trend records found for crop '{crop}'.")

    points = [
        TrendPoint(
            date=r["trend_date"],
            modal_price=r["modal_price"],
            min_price=r["min_price"],
            max_price=r["max_price"],
            volume_tonnes=r["volume_tonnes"]
        ) for r in rows
    ]

    prices = [p.modal_price for p in points]
    current_p = prices[-1]
    first_p = prices[0]
    avg_p = round(sum(prices) / len(prices), 2)
    change_pct = round(((current_p - first_p) / first_p) * 100, 2)
    direction = "upward" if change_pct > 1.5 else ("downward" if change_pct < -1.5 else "stable")

    return TrendsResponse(
        crop=crop,
        point_count=len(points),
        current_price=current_p,
        average_price=avg_p,
        min_price=min(prices),
        max_price=max(prices),
        trend_direction=direction,
        trend_change_pct=change_pct,
        trends=points
    )

# ── 7. GET /data-status ───────────────────────────────────────────────────────
@app.get("/data-status", response_model=DataStatusResponse, tags=["Data Integrity"])
def get_data_status():
    """Data integrity and transparency report."""
    ensure_db()
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) as cnt FROM crops;")
        total_crops = cursor.fetchone()["cnt"]
        cursor.execute("SELECT COUNT(*) as cnt FROM mandis;")
        total_mandis = cursor.fetchone()["cnt"]
        cursor.execute("SELECT COUNT(*) as cnt FROM crop_prices;")
        total_prices = cursor.fetchone()["cnt"]
        cursor.execute("SELECT MAX(price_date) as latest FROM crop_prices;")
        latest_date = cursor.fetchone()["latest"] or "N/A"

    return DataStatusResponse(
        status="Operational",
        database_type="SQLite (Local persistent / Vercel Serverless /tmp compatible)",
        total_crops=total_crops,
        total_mandis=total_mandis,
        total_price_records=total_prices,
        data_mode="Sample Benchmark Data (Agmarknet Simulation)",
        last_data_update=latest_date,
        government_source_integration="Simulated API Schema ready for Data.gov.in / Agmarknet API key integration",
        transparency_note=(
            "MandiSell strictly labels all current demo data as synthetic/sample benchmark data. "
            "No live government API keys are hardcoded in public repositories for security. "
            "Production deployment can bind directly to OGD (Open Government Data) API feeds."
        )
    )

# ── Static Frontend Serving ───────────────────────────────────────────────────
@app.get("/", tags=["Frontend"])
def serve_index():
    index_file = os.path.join(parent_dir, "public", "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"project": "MandiSell", "docs": "/docs", "health": "/health"}

@app.get("/styles.css", include_in_schema=False)
def serve_css():
    f = os.path.join(parent_dir, "public", "styles.css")
    if os.path.exists(f):
        return FileResponse(f, media_type="text/css")
    raise HTTPException(status_code=404, detail="styles.css not found")

@app.get("/app.js", include_in_schema=False)
def serve_js():
    f = os.path.join(parent_dir, "public", "app.js")
    if os.path.exists(f):
        return FileResponse(f, media_type="application/javascript")
    raise HTTPException(status_code=404, detail="app.js not found")
