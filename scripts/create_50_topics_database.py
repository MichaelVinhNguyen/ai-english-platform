"""
scripts/create_50_topics_database.py
Master generator for 50 Topics x 100 Words = 5,000 Flashcards.
"""

import os
import sys
import json
import sqlite3
from pathlib import Path

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data" / "vocabulary"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = BASE_DIR / "data" / "app.db"
JSON_OUT_PATH = DATA_DIR / "flashcards_50_topics_5000_words.json"

print(f"[INFO] Building 50 Topics x 100 Words Dataset...")
