# MandiSell 🌾
> **Know your market. Calculate your returns. Make informed decisions.**
> Built for the **Srijan Setu Hackathon** &bull; AgriTech Decision Support Track

---

## 📌 Executive Summary & The Problem

In agricultural trading across India, farmers typically evaluate where to sell their harvest by checking headline modal prices quoted at various Agricultural Produce Market Committee (APMC) mandis or on WhatsApp groups.

### The "Headline Price Trap"
A farmer in **Patiala** with 50 quintals of wheat observes:
* **Khanna Grain Market:** Quotes **₹2,490 / quintal** *(Headline looks ₹130 higher!)*
* **Patiala Local Mandi:** Quotes **₹2,360 / quintal**

Most farmers assume Khanna will yield higher profits. However:
* Khanna is **52 km** away. Commercial freight costs ₹3.60/km/quintal = **₹9,360** in roundtrip transport deductions, plus higher labor and mandi cess.
* Patiala is only **6.5 km** away, incurring just **₹1,040** in freight.

**The Reality:** After accounting for freight, loading/unloading labor, and statutory APMC cess:
* **Patiala Local Net Proceeds:** **₹1,14,290** (Net ₹2,285.80 / qtl)
* **Khanna Mandi Net Proceeds:** **₹1,11,432** (Net ₹2,228.64 / qtl)

The farmer who chose Khanna purely based on headline price actually **lost ₹2,858 in cold cash**!

**MandiSell solves this trap.** It is an intuitive, farmer-tailored web application that calculates **estimated take-home proceeds after actual delivery deductions**, recommending the market that puts the most cash into the farmer's pocket.

---

## 🛠️ Technology Stack

| Layer | Technologies Used | Description |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript (ES6+), Chart.js | Tactile, high-contrast, rural-friendly UI with bilingual Hindi hints. Zero bulky frameworks. |
| **Backend** | Python 3.12, FastAPI, Pydantic v2 | High-performance asynchronous REST API with strict request validation and dynamic calculation engine. |
| **Database** | SQLite3 | Zero-configuration SQL database. Uses local persistent file locally and `/tmp` in serverless Vercel environments. |
| **Testing** | Pytest, HTTPX | 16 comprehensive unit & regression tests covering calculations, edge cases, negative values, and stale data. |
| **Deployment** | Vercel | Unified Vercel serverless deployment (`@vercel/python` + `@vercel/static`). |

---

## ✨ Key Features

1. **True Net Proceeds Calculator**: Computes `Gross Value - Transport Freight - Handling Labor - Mandi Cess`.
2. **Dynamic Ranking Engine**: Ranks all nearby mandis by net in-hand proceeds, not merely the displayed crop price.
3. **Actionable Decision Insight ("Why this Mandi?")**: Plain-language explanation showing whether the winning market won due to price premium, logistics proximity, or both.
4. **Interactive Custom Cost Overrides**: Farmers can click **"Adjust Costs"** on any mandi row to enter custom transport freight or labor rates (e.g. if using own tractor) and immediately recalculate.
5. **Data Freshness & Transparency**:
   - Green badge for fresh quotes (< 24h).
   - Amber warning for stale quotes (> 48h).
   - Transparent disclaimer labeling sample benchmark data (Agmarknet simulation model).
6. **30-Day Historical Price Trends**: Visual Chart.js trendline showing daily modal prices, 30-day average, and price momentum.
7. **Farmer-Centered UI (No AI Clichés)**:
   - High-contrast natural palette (forest green, warm amber, linen eggshell).
   - Large touch targets (48px+) optimized for field smartphones under bright sunlight.
   - Quick load preset chips (25 qtl Pickup, 50 qtl Tractor, 100 qtl Double Trolley, 250 qtl Truck).

---

## 📐 Business Logic & Mathematical Formulas

$$\text{Gross Market Value} = \text{Modal Price (₹/qtl)} \times \text{Quantity (qtl)}$$

$$\text{Transport Freight} = \text{Distance (km)} \times \text{Transport Rate (₹/km/qtl)} \times \text{Quantity (qtl)}$$

$$\text{Handling Labor} = \text{Handling Charge (₹/qtl)} \times \text{Quantity (qtl)}$$

$$\text{Mandi Cess} = \text{Gross Value} \times \left(\frac{\text{Cess Rate \%}}{100}\right)$$

$$\text{Total Deductions} = \text{Transport Freight} + \text{Handling Labor} + \text{Mandi Cess}$$

$$\mathbf{\text{Estimated Proceeds}} = \mathbf{\text{Gross Market Value}} - \mathbf{\text{Total Deductions}}$$

$$\text{Net Rate per Quintal} = \frac{\text{Estimated Proceeds}}{\text{Quantity (qtl)}}$$

$$\text{Proceeds Advantage} = \text{Proceeds}_{\text{Rank \#1}} - \text{Proceeds}_{\text{Rank \#2}}$$

---

## 🔌 API Endpoints Reference

All endpoints are documented interactively via FastAPI Swagger UI at `http://localhost:8000/docs`.

### 1. `GET /health`
System health check and deployment status.
```json
{
  "status": "healthy",
  "service": "MandiSell API",
  "version": "1.0.0",
  "timestamp": "2026-10-26T23:07:59",
  "database": "sqlite",
  "mode": "Hackathon Demo (Sample Benchmark Feed)"
}
```

### 2. `GET /crops`
Returns all supported commodities with Hindi names, category, and MSP benchmark.

### 3. `GET /districts?crop=Wheat`
Returns all registered districts, optionally filtered by crop.

### 4. `GET /markets?crop=Wheat&district=Patiala`
Retrieves market price quotes for a specific crop and district with freshness flags.

### 5. `POST /compare`
The core comparison and ranking engine.
* **Request Body:**
```json
{
  "crop": "Wheat",
  "district": "Patiala",
  "quantity_quintals": 50.0,
  "custom_transport_rates": { "1": 3.2 },
  "custom_other_costs_per_qtl": { "1": 18.0 }
}
```
* **Response:**
Returns ranked markets list, top market (`best_mandi`), runner up (`runner_up_mandi`), `proceeds_advantage`, and `why_best_explanation`.

### 6. `GET /prices/trends?crop=Wheat`
Returns 30-day historical modal prices, current price, 30-day average, and momentum direction (`upward`, `downward`, `stable`).

### 7. `GET /data-status`
Transparency and data integrity report detailing database record counts, data timestamp, and government API integration status.

---

## 🚀 Quickstart & Local Installation

### Prerequisites
* Python 3.10+ installed
* Git installed

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/mandisell.git
cd mandisell
```

### 2. Create and activate virtual environment
* **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
* **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run automated test suite
```bash
pytest -v tests
```
*(All 16 tests should pass in ~1 second)*

### 5. Start the local server
```bash
python run.py
```

### 6. Open in your browser
* **Web Application:** [http://localhost:8000](http://localhost:8000)
* **Interactive Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Redoc Documentation:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Testing Verification

The project includes 16 automated tests covering the entire workflow:
1. `test_health_endpoint`: Uptime check and version validation.
2. `test_get_crops`: Master data retrieval and MSP prices.
3. `test_get_markets_success`: District market retrieval.
4. `test_get_markets_unsupported_crop`: 404 response for unindexed crops.
5. `test_get_markets_unknown_district`: 404 response with helpful district suggestions.
6. `test_compare_markets_standard`: Complete arithmetic, deduction calculation, and descending rank order.
7. `test_compare_negative_quantity`: Pydantic 422 validation on negative harvest.
8. `test_compare_zero_quantity`: Pydantic 422 validation on zero harvest.
9. `test_compare_excessive_quantity`: Pydantic 422 validation on quantities > 20,000 qtl.
10. `test_compare_empty_fields`: Validation against blank/whitespace crop or district names.
11. `test_compare_custom_transport_override`: Verifies that custom transport rates dynamically recalculate deductions and update market ranks.
12. `test_compare_custom_handling_override`: Verifies that custom labor rates update total deductions.
13. `test_price_trends_success`: Trend points retrieval and momentum calculation.
14. `test_price_trends_not_found`: 404 response on non-existent crop trends.
15. `test_data_status`: System metrics and transparency disclaimer.
16. `test_stale_record_detection`: Correctly flags quotes older than 48 hours as `is_stale=True`.

---

## 🌐 Vercel Deployment Instructions

MandiSell is pre-configured for instant zero-configuration deployment to **Vercel**.

### Option A: Deploy via GitHub (Recommended)
1. Push your code to GitHub:
   ```bash
   git add .
   git commit -m "feat: complete MandiSell AgriTech MVP"
   git branch -M main
   git remote add origin https://github.com/<your-username>/mandisell.git
   git push -u origin main
   ```
2. Log in to [Vercel](https://vercel.com) and click **"Add New Project"**.
3. Import your `mandisell` GitHub repository.
4. Keep the default settings (Vercel will detect `vercel.json`).
5. Click **Deploy**. Your app will be live with a free `https://<project-name>.vercel.app` URL in under 60 seconds!

### Option B: Deploy via Vercel CLI
```bash
npm i -g vercel
vercel
```

---

## 🎤 Hackathon Pitch & Judge Demonstration Guide

### 3-Minute Demo Walkthrough
1. **The Hook (30 sec):** 
   Show the tagline: *"Know your market. Calculate your returns. Make informed decisions."* Ask judges: *"If Mandi A offers ₹2,490 and Mandi B offers ₹2,360, which one should a farmer choose? Most farmers pick Mandi A and lose money. Let me show you why."*
2. **The Calculation (60 sec):**
   * Select **Wheat** and **Patiala**.
   * Select **50 Quintals (Tractor Trolley)**.
   * Click **Calculate & Compare Mandis**.
   * Point out the **Recommendation Card**: Patiala APMC wins with **₹1,14,290** in net proceeds, even though Khanna APMC advertises ₹2,490! Show the Advantage Pill: `+₹2,858 MORE in hand`.
3. **Interactive Overrides (45 sec):**
   * Click **"Adjust Costs"** next to Khanna Mandi.
   * Change freight rate to ₹2.00/km/qtl (simulating a farmer who has their own commercial truck).
   * Click **Apply & Recalculate**.
   * Show judges how the backend dynamically re-ranks Khanna to #1 with the custom rate!
4. **Historical Trends & Data Integrity (45 sec):**
   * Scroll to the **30-Day Modal Price Trend chart**.
   * Click the **"Sample Benchmark Feed"** badge in the header to demonstrate total transparency regarding government data integration.

---

## 🛡️ Data Integrity Statement

MandiSell is committed to data transparency:
* Current hackathon prices are benchmark quotes modeled on real Agmarknet seasonal distributions and are explicitly tagged with `is_sample_data = True`.
* MandiSell does not claim live API quotes until a verified API key is bound to the official Open Government Data (data.gov.in) Agmarknet endpoint.
* Prices older than 48 hours trigger an amber `⚠️ Stale` warning on the UI.

---

## 📄 License
MIT License &bull; Developed for Srijan Setu Hackathon 2026.
