import sys
import os
import sqlite3
from typing import Generator
from contextlib import contextmanager

# Ensure proper path resolution for Vercel Serverless
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
for p in [current_dir, parent_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

def get_db_path() -> str:
    """
    Returns the SQLite database path.
    On Vercel serverless environments, writes are restricted to /tmp.
    Locally, it uses the project directory.
    """
    if os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME"):
        return "/tmp/mandisell.db"
    
    # Check if local directory is writable, fallback to /tmp if read-only
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    local_path = os.path.join(base_dir, "mandisell.db")
    try:
        if not os.path.exists(local_path):
            with open(local_path, "a") as f:
                pass
        return local_path
    except Exception:
        return "/tmp/mandisell.db"

def get_db_connection() -> sqlite3.Connection:
    """Create and return a configured SQLite connection with dict-like row access."""
    db_path = get_db_path()
    try:
        conn = sqlite3.connect(db_path, check_same_thread=False)
    except Exception:
        # Fallback to in-memory if disk is completely restricted
        conn = sqlite3.connect(":memory:", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

@contextmanager
def get_db() -> Generator[sqlite3.Connection, None, None]:
    """Context manager for database connections."""
    conn = get_db_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db():
    """Initializes schema and tables if they don't exist."""
    with get_db() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS crops (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            hindi_name TEXT NOT NULL,
            category TEXT NOT NULL,
            msp_price REAL,
            unit TEXT DEFAULT 'Quintal'
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS mandis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            district TEXT NOT NULL,
            state TEXT NOT NULL,
            distance_km REAL NOT NULL,
            transport_rate_per_km_qtl REAL NOT NULL DEFAULT 3.5,
            handling_charge_per_qtl REAL NOT NULL DEFAULT 18.0,
            mandi_cess_percent REAL NOT NULL DEFAULT 1.5,
            market_type TEXT NOT NULL DEFAULT 'APMC Principal Yard',
            contact_phone TEXT,
            operating_hours TEXT DEFAULT '06:00 AM - 04:00 PM'
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS crop_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mandi_id INTEGER NOT NULL,
            crop_name TEXT NOT NULL,
            min_price REAL NOT NULL,
            modal_price REAL NOT NULL,
            max_price REAL NOT NULL,
            arrival_tonnes REAL NOT NULL,
            price_date TEXT NOT NULL,
            source TEXT NOT NULL,
            is_sample_data INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (mandi_id) REFERENCES mandis (id) ON DELETE CASCADE,
            FOREIGN KEY (crop_name) REFERENCES crops (name) ON DELETE CASCADE
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_trends (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crop_name TEXT NOT NULL,
            trend_date TEXT NOT NULL,
            modal_price REAL NOT NULL,
            min_price REAL NOT NULL,
            max_price REAL NOT NULL,
            volume_tonnes REAL NOT NULL,
            source TEXT NOT NULL
        );
        """)
        
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_crop_prices_crop_mandi ON crop_prices(crop_name, mandi_id);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_mandis_district ON mandis(district);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_price_trends_crop ON price_trends(crop_name, trend_date);")
