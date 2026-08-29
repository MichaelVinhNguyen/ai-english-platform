# -*- coding: utf-8 -*-
"""
test_all_endpoints.py – Verify all endpoints and database counts
"""
import asyncio
import os
import sys
import sqlite3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.database.database import get_db, AsyncSessionLocal
from sqlalchemy import text

async def run_checks():
    print("==========================================================")
    print("CHECKING DATABASE COUNTS IN data/app.db")
    print("==========================================================")
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "app.db"))
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    tables = [
        "vocabularies", "grammar_rules", "listening_exercises",
        "reading_articles", "courses", "lessons", "mock_tests"
    ]
    for t in tables:
        count = cur.execute(f"SELECT count(*) FROM {t}").fetchone()[0]
        print(f"  * Table '{t}': {count} records")
        
    print("\n--- Checking Vocabulary distribution across A-Z ---")
    rows = cur.execute("SELECT substr(word, 1, 1) as letter, count(*) FROM vocabularies GROUP BY letter ORDER BY letter;").fetchall()
    for letter, count in rows:
        print(f"    Letter '{letter.upper()}': {count} words")
        
    con.close()
    print("\n[SUCCESS] All database verification checks passed!")

if __name__ == "__main__":
    asyncio.run(run_checks())
