"""
scripts/build_dataset_5000.py
Builds the complete 50 Topics x 100 Words = 5,000 Flashcards dataset.
"""

import os
import sys
import json
import sqlite3
import re
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR / "scripts"))

from flashcard_topics_def import ALL_50_TOPICS_META

RAW_30_JSON = BASE_DIR / "data" / "vocabulary" / "flashcards_30_topics_1500_words.json"
OUT_5000_JSON = BASE_DIR / "data" / "vocabulary" / "flashcards_50_topics_5000_words.json"
DB_PATH = BASE_DIR / "data" / "app.db"
STANDALONE_JS_FRONTEND = BASE_DIR / "frontend" / "js" / "standalone_data.js"
STANDALONE_JS_PUBLIC = BASE_DIR / "public" / "js" / "standalone_data.js"

print("[BUILDER] Master dataset compiler initialized.")
