"""
scripts/full_50_topics_builder.py
Comprehensive builder that generates all 50 Topics x 100 Words = 5,000 Flashcards.
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
from vocab_supplement_1_to_10 import SUPPLEMENT_1_TO_10

# Load existing 30 topics
RAW_30_JSON = BASE_DIR / "data" / "vocabulary" / "flashcards_30_topics_1500_words.json"
with open(RAW_30_JSON, "r", encoding="utf-8") as f:
    existing_30_topics = json.load(f)

print(f"[INIT] Loaded {len(existing_30_topics)} existing topics from 1500 words JSON.")
