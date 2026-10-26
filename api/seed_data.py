from datetime import datetime, timedelta
from api.database import get_db

CROPS_DATA = [
    {"name": "Wheat", "hindi_name": "गेहूं", "category": "Cereal", "msp_price": 2275.0, "unit": "Quintal"},
    {"name": "Paddy (Basmati)", "hindi_name": "धान (बासमती)", "category": "Cereal", "msp_price": 2183.0, "unit": "Quintal"},
    {"name": "Mustard", "hindi_name": "सरसों", "category": "Oilseed", "msp_price": 5650.0, "unit": "Quintal"},
    {"name": "Cotton", "hindi_name": "कपास", "category": "Cash Crop", "msp_price": 7121.0, "unit": "Quintal"},
    {"name": "Maize", "hindi_name": "मक्का", "category": "Cereal", "msp_price": 2090.0, "unit": "Quintal"},
    {"name": "Soybean", "hindi_name": "सोयाबीन", "category": "Oilseed", "msp_price": 4600.0, "unit": "Quintal"},
    {"name": "Potato", "hindi_name": "आलू", "category": "Vegetable", "msp_price": 1250.0, "unit": "Quintal"},
    {"name": "Onion", "hindi_name": "प्याज़", "category": "Vegetable", "msp_price": 1600.0, "unit": "Quintal"},
    {"name": "Gram (Chana)", "hindi_name": "चना", "category": "Pulse", "msp_price": 5440.0, "unit": "Quintal"},
]

# Mandis list with realistic district associations and logistics parameters
MANDIS_DATA = [
    # Punjab - Patiala & surrounds
    {
        "name": "Patiala Grain Market (APMC)",
        "district": "Patiala",
        "state": "Punjab",
        "distance_km": 6.5,
        "transport_rate_per_km_qtl": 3.2,
        "handling_charge_per_qtl": 18.0,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Principal Yard",
        "contact_phone": "+91-175-2214589"
    },
    {
        "name": "Nabha Anaj Mandi",
        "district": "Patiala",
        "state": "Punjab",
        "distance_km": 28.0,
        "transport_rate_per_km_qtl": 3.4,
        "handling_charge_per_qtl": 16.0,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Sub-Yard",
        "contact_phone": "+91-176-5221045"
    },
    {
        "name": "Samana Grain Market",
        "district": "Patiala",
        "state": "Punjab",
        "distance_km": 36.0,
        "transport_rate_per_km_qtl": 3.5,
        "handling_charge_per_qtl": 17.0,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Principal Yard",
        "contact_phone": "+91-176-4220311"
    },
    {
        "name": "Rajpura e-NAM Mandi",
        "district": "Patiala",
        "state": "Punjab",
        "distance_km": 29.5,
        "transport_rate_per_km_qtl": 3.3,
        "handling_charge_per_qtl": 15.0,
        "mandi_cess_percent": 1.2,
        "market_type": "e-NAM Integrated Yard",
        "contact_phone": "+91-176-2245890"
    },
    {
        "name": "Khanna Grain Market (Asia's Largest)",
        "district": "Patiala", # Accessible to Patiala farmers
        "state": "Punjab",
        "distance_km": 52.0,
        "transport_rate_per_km_qtl": 3.6,
        "handling_charge_per_qtl": 22.0,
        "mandi_cess_percent": 1.5,
        "market_type": "Mega APMC Yard",
        "contact_phone": "+91-162-8220014"
    },
    {
        "name": "Sirhind Anaj Mandi",
        "district": "Patiala",
        "state": "Punjab",
        "distance_km": 35.0,
        "transport_rate_per_km_qtl": 3.3,
        "handling_charge_per_qtl": 16.5,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Yard",
        "contact_phone": "+91-176-3232145"
    },

    # Punjab - Ludhiana
    {
        "name": "Ludhiana APMC New Grain Market",
        "district": "Ludhiana",
        "state": "Punjab",
        "distance_km": 8.0,
        "transport_rate_per_km_qtl": 3.2,
        "handling_charge_per_qtl": 19.0,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Principal Yard",
        "contact_phone": "+91-161-2401290"
    },
    {
        "name": "Khanna Grain Market",
        "district": "Ludhiana",
        "state": "Punjab",
        "distance_km": 42.0,
        "transport_rate_per_km_qtl": 3.5,
        "handling_charge_per_qtl": 20.0,
        "mandi_cess_percent": 1.5,
        "market_type": "Mega APMC Yard",
        "contact_phone": "+91-162-8220014"
    },
    {
        "name": "Jagraon Grain Mandi",
        "district": "Ludhiana",
        "state": "Punjab",
        "distance_km": 45.0,
        "transport_rate_per_km_qtl": 3.6,
        "handling_charge_per_qtl": 17.0,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Sub-Yard",
        "contact_phone": "+91-162-4223101"
    },

    # Haryana - Karnal
    {
        "name": "Karnal APMC Yard",
        "district": "Karnal",
        "state": "Haryana",
        "distance_km": 7.0,
        "transport_rate_per_km_qtl": 3.2,
        "handling_charge_per_qtl": 18.0,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Principal Yard",
        "contact_phone": "+91-184-2254300"
    },
    {
        "name": "Taraori Rice & Grain Mandi",
        "district": "Karnal",
        "state": "Haryana",
        "distance_km": 19.0,
        "transport_rate_per_km_qtl": 3.4,
        "handling_charge_per_qtl": 16.0,
        "mandi_cess_percent": 1.5,
        "market_type": "Specialized Basmati Yard",
        "contact_phone": "+91-184-2388210"
    },
    {
        "name": "Gharaunda Sub-Mandi",
        "district": "Karnal",
        "state": "Haryana",
        "distance_km": 22.0,
        "transport_rate_per_km_qtl": 3.3,
        "handling_charge_per_qtl": 17.5,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Sub-Yard",
        "contact_phone": "+91-184-2512400"
    },

    # Madhya Pradesh - Indore
    {
        "name": "Indore Devi Ahilya Bai Holkar APMC (Choithram)",
        "district": "Indore",
        "state": "Madhya Pradesh",
        "distance_km": 9.0,
        "transport_rate_per_km_qtl": 3.4,
        "handling_charge_per_qtl": 18.0,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Principal Yard",
        "contact_phone": "+91-731-2481020"
    },
    {
        "name": "Sanwer Krishi Upaj Mandi",
        "district": "Indore",
        "state": "Madhya Pradesh",
        "distance_km": 32.0,
        "transport_rate_per_km_qtl": 3.5,
        "handling_charge_per_qtl": 15.0,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Sub-Yard",
        "contact_phone": "+91-731-2895101"
    },
    {
        "name": "Mhow (Dr. Ambedkar Nagar) Mandi",
        "district": "Indore",
        "state": "Madhya Pradesh",
        "distance_km": 26.0,
        "transport_rate_per_km_qtl": 3.3,
        "handling_charge_per_qtl": 16.0,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Yard",
        "contact_phone": "+91-732-4272300"
    },

    # Maharashtra - Nashik
    {
        "name": "Nashik APMC (Panchavati)",
        "district": "Nashik",
        "state": "Maharashtra",
        "distance_km": 6.0,
        "transport_rate_per_km_qtl": 3.5,
        "handling_charge_per_qtl": 20.0,
        "mandi_cess_percent": 1.25,
        "market_type": "APMC Principal Yard",
        "contact_phone": "+91-253-2512800"
    },
    {
        "name": "Lasalgaon Onion & Grain Market",
        "district": "Nashik",
        "state": "Maharashtra",
        "distance_km": 58.0,
        "transport_rate_per_km_qtl": 3.8,
        "handling_charge_per_qtl": 24.0,
        "mandi_cess_percent": 1.25,
        "market_type": "Asia's Premier Onion Hub",
        "contact_phone": "+91-255-0266025"
    },
    {
        "name": "Pimpalgaon Baswant APMC",
        "district": "Nashik",
        "state": "Maharashtra",
        "distance_km": 31.0,
        "transport_rate_per_km_qtl": 3.4,
        "handling_charge_per_qtl": 19.0,
        "mandi_cess_percent": 1.25,
        "market_type": "APMC Sub-Yard",
        "contact_phone": "+91-255-4232145"
    },

    # Uttar Pradesh - Agra
    {
        "name": "Agra APMC (Khandari)",
        "district": "Agra",
        "state": "Uttar Pradesh",
        "distance_km": 7.5,
        "transport_rate_per_km_qtl": 3.2,
        "handling_charge_per_qtl": 18.0,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Principal Yard",
        "contact_phone": "+91-562-2521190"
    },
    {
        "name": "Fatehabad Mandi",
        "district": "Agra",
        "state": "Uttar Pradesh",
        "distance_km": 35.0,
        "transport_rate_per_km_qtl": 3.5,
        "handling_charge_per_qtl": 16.0,
        "mandi_cess_percent": 1.5,
        "market_type": "APMC Yard",
        "contact_phone": "+91-562-2731040"
    },
    {
        "name": "Shamsabad Potato Market",
        "district": "Agra",
        "state": "Uttar Pradesh",
        "distance_km": 28.0,
        "transport_rate_per_km_qtl": 3.3,
        "handling_charge_per_qtl": 17.0,
        "mandi_cess_percent": 1.5,
        "market_type": "Vegetable Specialist Mandi",
        "contact_phone": "+91-562-2841020"
    }
]

def seed_database(force: bool = False):
    """
    Populates the database with initial crops, mandis, price quotes, and trends.
    """
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Check if already seeded
        cursor.execute("SELECT COUNT(*) as cnt FROM crops;")
        crops_count = cursor.fetchone()["cnt"]
        if crops_count > 0 and not force:
            return  # Already seeded
        
        # Clear existing tables if forcing
        if force:
            cursor.execute("DELETE FROM price_trends;")
            cursor.execute("DELETE FROM crop_prices;")
            cursor.execute("DELETE FROM mandis;")
            cursor.execute("DELETE FROM crops;")

        # Insert crops
        for c in CROPS_DATA:
            cursor.execute("""
            INSERT INTO crops (name, hindi_name, category, msp_price, unit)
            VALUES (?, ?, ?, ?, ?)
            """, (c["name"], c["hindi_name"], c["category"], c["msp_price"], c["unit"]))
            
        # Insert mandis
        for m in MANDIS_DATA:
            cursor.execute("""
            INSERT INTO mandis (name, district, state, distance_km, transport_rate_per_km_qtl,
                                handling_charge_per_qtl, mandi_cess_percent, market_type, contact_phone)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                m["name"], m["district"], m["state"], m["distance_km"],
                m["transport_rate_per_km_qtl"], m["handling_charge_per_qtl"],
                m["mandi_cess_percent"], m["market_type"], m["contact_phone"]
            ))

        # Retrieve inserted mandis map: name -> id
        cursor.execute("SELECT id, name, district FROM mandis;")
        mandi_rows = cursor.fetchall()
        mandi_map = {row["name"]: row["id"] for row in mandi_rows}

        today_str = datetime.now().strftime("%Y-%m-%d")
        yesterday_str = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        three_days_ago_str = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")

        # Specific realistic price matrix designed to demonstrate real decision trade-offs
        # Format: (mandi_name, crop_name, min_p, modal_p, max_p, arrivals, date, source)
        price_specs = [
            # Patiala district - Wheat (classic gross vs net comparison case study!)
            # Patiala: modal 2360, dist 6.5 km -> low transport
            # Khanna: modal 2490, dist 52 km -> high transport (+187 transport), net might be close!
            # Rajpura: modal 2390, dist 29.5 km
            # Nabha: modal 2320, dist 28 km
            # Samana: modal 2345, dist 36 km
            # Sirhind: modal 2410, dist 35 km (stale date: 3 days ago, to trigger freshness alert!)
            ("Patiala Grain Market (APMC)", "Wheat", 2310.0, 2360.0, 2395.0, 420.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Khanna Grain Market (Asia's Largest)", "Wheat", 2440.0, 2490.0, 2530.0, 1150.0, today_str, "e-NAM Market Feed (Simulated Demo)"),
            ("Rajpura e-NAM Mandi", "Wheat", 2350.0, 2390.0, 2420.0, 310.0, today_str, "e-NAM Market Feed (Simulated Demo)"),
            ("Nabha Anaj Mandi", "Wheat", 2280.0, 2320.0, 2350.0, 180.0, yesterday_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Samana Grain Market", "Wheat", 2300.0, 2345.0, 2370.0, 250.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Sirhind Anaj Mandi", "Wheat", 2370.0, 2410.0, 2440.0, 290.0, three_days_ago_str, "Agmarknet Daily Bulletin (Simulated Demo)"),

            # Patiala district - Paddy (Basmati)
            ("Patiala Grain Market (APMC)", "Paddy (Basmati)", 3350.0, 3420.0, 3490.0, 350.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Khanna Grain Market (Asia's Largest)", "Paddy (Basmati)", 3580.0, 3680.0, 3750.0, 890.0, today_str, "e-NAM Market Feed (Simulated Demo)"),
            ("Rajpura e-NAM Mandi", "Paddy (Basmati)", 3400.0, 3470.0, 3520.0, 210.0, today_str, "e-NAM Market Feed (Simulated Demo)"),
            ("Nabha Anaj Mandi", "Paddy (Basmati)", 3300.0, 3380.0, 3440.0, 140.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),

            # Patiala district - Mustard
            ("Patiala Grain Market (APMC)", "Mustard", 5450.0, 5550.0, 5650.0, 120.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Rajpura e-NAM Mandi", "Mustard", 5520.0, 5620.0, 5700.0, 95.0, today_str, "e-NAM Market Feed (Simulated Demo)"),
            ("Khanna Grain Market (Asia's Largest)", "Mustard", 5600.0, 5710.0, 5800.0, 260.0, today_str, "e-NAM Market Feed (Simulated Demo)"),

            # Ludhiana District
            ("Ludhiana APMC New Grain Market", "Wheat", 2330.0, 2380.0, 2415.0, 620.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Khanna Grain Market", "Wheat", 2440.0, 2490.0, 2530.0, 1150.0, today_str, "e-NAM Market Feed (Simulated Demo)"),
            ("Jagraon Grain Mandi", "Wheat", 2310.0, 2360.0, 2390.0, 340.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Ludhiana APMC New Grain Market", "Paddy (Basmati)", 3450.0, 3540.0, 3600.0, 480.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Khanna Grain Market", "Paddy (Basmati)", 3580.0, 3680.0, 3750.0, 890.0, today_str, "e-NAM Market Feed (Simulated Demo)"),

            # Karnal District (Basmati Heartland)
            ("Karnal APMC Yard", "Paddy (Basmati)", 3600.0, 3720.0, 3810.0, 750.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Taraori Rice & Grain Mandi", "Paddy (Basmati)", 3750.0, 3890.0, 3980.0, 920.0, today_str, "e-NAM Market Feed (Simulated Demo)"),
            ("Gharaunda Sub-Mandi", "Paddy (Basmati)", 3580.0, 3670.0, 3740.0, 310.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Karnal APMC Yard", "Wheat", 2340.0, 2385.0, 2420.0, 510.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Taraori Rice & Grain Mandi", "Wheat", 2360.0, 2405.0, 2440.0, 390.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),

            # Indore District (Soybean & Wheat)
            ("Indore Devi Ahilya Bai Holkar APMC (Choithram)", "Soybean", 4650.0, 4780.0, 4890.0, 890.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Sanwer Krishi Upaj Mandi", "Soybean", 4580.0, 4700.0, 4790.0, 420.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Mhow (Dr. Ambedkar Nagar) Mandi", "Soybean", 4520.0, 4640.0, 4720.0, 310.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Indore Devi Ahilya Bai Holkar APMC (Choithram)", "Wheat", 2420.0, 2490.0, 2550.0, 710.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Sanwer Krishi Upaj Mandi", "Wheat", 2380.0, 2440.0, 2490.0, 380.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Indore Devi Ahilya Bai Holkar APMC (Choithram)", "Gram (Chana)", 5600.0, 5740.0, 5850.0, 360.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),

            # Nashik District (Onion Capital)
            ("Nashik APMC (Panchavati)", "Onion", 1750.0, 1920.0, 2150.0, 680.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Lasalgaon Onion & Grain Market", "Onion", 1950.0, 2180.0, 2420.0, 1850.0, today_str, "e-NAM Market Feed (Simulated Demo)"),
            ("Pimpalgaon Baswant APMC", "Onion", 1850.0, 2040.0, 2260.0, 890.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),

            # Agra District (Potato)
            ("Agra APMC (Khandari)", "Potato", 1320.0, 1420.0, 1530.0, 1200.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Fatehabad Mandi", "Potato", 1280.0, 1370.0, 1460.0, 620.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
            ("Shamsabad Potato Market", "Potato", 1360.0, 1480.0, 1590.0, 840.0, today_str, "e-NAM Market Feed (Simulated Demo)"),
            ("Agra APMC (Khandari)", "Mustard", 5400.0, 5520.0, 5610.0, 240.0, today_str, "Agmarknet Daily Bulletin (Simulated Demo)"),
        ]

        for m_name, c_name, min_p, mod_p, max_p, arr_ton, p_date, src in price_specs:
            if m_name in mandi_map:
                m_id = mandi_map[m_name]
                cursor.execute("""
                INSERT INTO crop_prices (mandi_id, crop_name, min_price, modal_price, max_price,
                                         arrival_tonnes, price_date, source, is_sample_data)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1)
                """, (m_id, c_name, min_p, mod_p, max_p, arr_ton, p_date, src))

        # Insert 30-day realistic historical price trends for major crops
        # This powers the GET /prices/trends endpoint and the Chart.js visual
        trends_base = {
            "Wheat": (2290.0, 4.2),      # base price, slight daily rise
            "Paddy (Basmati)": (3420.0, 7.5),
            "Mustard": (5420.0, 6.0),
            "Soybean": (4620.0, 4.8),
            "Onion": (1650.0, 12.0),
            "Potato": (1310.0, 3.2),
            "Cotton": (6980.0, 9.5),
            "Maize": (2050.0, 2.5),
            "Gram (Chana)": (5580.0, 5.0)
        }

        for crop, (base_p, slope) in trends_base.items():
            for i in range(30, -1, -1):
                day = datetime.now() - timedelta(days=i)
                date_str = day.strftime("%Y-%m-%d")
                # Add slight realistic cyclic variation
                day_offset = (30 - i) * slope
                variation = ((i % 5) - 2) * 12.0
                modal = round(base_p + day_offset + variation, 1)
                min_p = round(modal * 0.96, 1)
                max_p = round(modal * 1.04, 1)
                volume = round(400 + (i % 7) * 45 + (30 - i) * 6, 1)
                
                cursor.execute("""
                INSERT INTO price_trends (crop_name, trend_date, modal_price, min_price, max_price, volume_tonnes, source)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (crop, date_str, modal, min_p, max_p, volume, "Agmarknet Historical Feed (Simulated)"))

if __name__ == "__main__":
    from api.database import init_db
    init_db()
    seed_database(force=True)
    print("Database initialized and seeded successfully.")
