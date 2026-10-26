"""
MandiSell — One-Click Local Development Server Runner
Run: python run.py
"""

import sys
import os
import uvicorn
from api.database import init_db
from api.seed_data import seed_database

def main():
    print("=" * 65)
    print(" 🌾 MandiSell — Agricultural Returns & Market Comparison App")
    print(" Tagline: Know your market. Calculate your returns. Make informed decisions.")
    print("=" * 65)
    
    print("\n[1/2] Initializing SQLite database schema and seed data...")
    init_db()
    seed_database()
    print("      ✓ Database ready (mandisell.db)")

    print("\n[2/2] Starting local FastAPI & static frontend server...")
    print("      • Web App URL:      http://localhost:8000")
    print("      • Swagger API Docs: http://localhost:8000/docs")
    print("      • Alternative Docs: http://localhost:8000/redoc")
    print("      • Health Check:     http://localhost:8000/health")
    print("\nPress Ctrl+C to stop the server.\n" + "-" * 65)

    uvicorn.run(
        "api.index:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()
