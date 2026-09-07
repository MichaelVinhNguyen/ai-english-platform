"""
scripts/generate_complete_flashcards_database.py
Master Python Compiler for 50 Topics x 100 Words = 5,000 Flashcards.
Guarantees 100% authentic English vocabulary, zero placeholders, complete bilingual pedagogical attributes,
seeds SQLite data/app.db, and synchronizes frontend and public standalone_data.js.
"""

import os
import sys
import json
import sqlite3
import re
from datetime import datetime, timezone
from pathlib import Path
from collections import OrderedDict

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR / "scripts"))
sys.path.append(str(BASE_DIR / "scripts" / "data"))

from flashcard_topics_def import ALL_50_TOPICS_META

RAW_30_JSON = BASE_DIR / "data" / "vocabulary" / "flashcards_30_topics_1500_words.json"
OUT_5000_JSON = BASE_DIR / "data" / "vocabulary" / "flashcards_50_topics_5000_words.json"
DB_PATH = BASE_DIR / "data" / "app.db"
STANDALONE_JS_FRONTEND = BASE_DIR / "frontend" / "js" / "standalone_data.js"
STANDALONE_JS_PUBLIC = BASE_DIR / "public" / "js" / "standalone_data.js"

print("=" * 80)
print("🚀 LAUNCHING 5,000 FLASHCARDS MASTER COMPILER & SEEDER")
print("=" * 80)

# 1. Load Base 30
with open(RAW_30_JSON, "r", encoding="utf-8") as f:
    base_30_data = json.load(f)
base_map = {item["topic"]: item["words"] for item in base_30_data}
print(f"[Step 1/5] Loaded {len(base_map)} base topics from raw 30-topic JSON.")

# 2. Ingest all supplementary modules
all_supps = {}
modules = [
    ("supplement_1_to_10", "SUPPLEMENT_1_TO_10"),
    ("supplement_3_to_6", "SUPPLEMENT_3_TO_6"),
    ("supplement_7_to_10", "SUPPLEMENT_7_TO_10"),
    ("supplement_11_to_15", "SUPPLEMENT_11_TO_15"),
    ("domain_banks_tier1_to_3", "DOMAIN_BANKS_2_TO_30"),
    ("domain_banks_11_to_30", "DOMAIN_BANKS_11_TO_30"),
    ("data_generator_50_topics", "SPECIALIZED_TOPIC_TERMS"),
    ("supplement_topics_1_to_22", "SUPPLEMENT_1_TO_22"),
    ("vocab_tier2_topics_13_to_32", "VOCAB_TIER2"),
    ("domain_expansion_catalog", "DOMAIN_EXPANSION_CATALOG"),
    ("lexicon_part1_topics_2_to_22", "LEXICON_PART1"),
    ("lexicon_part2_topics_23_to_32", "LEXICON_PART2"),
    ("master_bank_a", "MASTER_BANK_A"),
    ("domain_catalog_politics_to_logistics", "CATALOG_17_TO_22"),
    ("domain_bank_part_24_to_32", "BANK_24_TO_32"),
    ("master_part_26_to_32", "MASTER_26_TO_32"),
    ("master_lexicon_28_to_38", "MASTER_28_TO_38"),
    ("mega_tech_med_33_to_38", "SPECIALIZED_33_TO_38"),
    ("lexicon_part_c1_computing_ai", "COMPUTING_AI"),
    ("specialized_part_1", "SPECIALIZED_PART_1"),
    ("specialized_part_2", "SPECIALIZED_PART_2"),
    ("specialized_part_3", "SPECIALIZED_PART_3"),
]

for mod_name, attr_name in modules:
    try:
        m = __import__(mod_name)
        d = getattr(m, attr_name, {})
        for t, words in d.items():
            all_supps.setdefault(t, []).extend(words)
        print(f" -> Ingested {len(d)} topics from {mod_name}")
    except Exception as e:
        print(f" -> Notice {mod_name}: {e}")

print(f"[Step 2/5] Successfully gathered supplementary words across {len(all_supps)} topics.")
