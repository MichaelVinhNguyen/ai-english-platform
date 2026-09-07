"""
scripts/generate_all_50_topics_curated.py
Generates the complete 50 Topics x 100 Words = 5,000 Flashcards dataset.
Every single topic has exactly 100 authentic, high-quality words.
"""

import os
import sys
import json
import sqlite3
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR / "scripts"))

from flashcard_topics_def import ALL_50_TOPICS_META
from topics_data_1_to_10 import TOPICS_1_TO_10
from topics_data_11_to_20 import TOPICS_11_TO_20
from topics_data_21_to_30 import TOPICS_21_TO_30

# Output paths
DATA_DIR = BASE_DIR / "data" / "vocabulary"
DATA_DIR.mkdir(parents=True, exist_ok=True)
JSON_OUT_PATH = DATA_DIR / "flashcards_50_topics_5000_words.json"
DB_PATH = BASE_DIR / "data" / "app.db"
STANDALONE_JS_FRONTEND = BASE_DIR / "frontend" / "js" / "standalone_data.js"
STANDALONE_JS_PUBLIC = BASE_DIR / "public" / "js" / "standalone_data.js"

print("[STEP 1] Generating 50 Topics x 100 Words = 5,000 Flashcards...")
