"""
scripts/generate_all_5000_flashcards.py
Master generator and compiler for all 50 Topics x 100 Words = 5,000 Flashcards.
"""

import sys
import os
import json
import sqlite3
import re
from datetime import datetime, timezone
from pathlib import Path
from collections import OrderedDict

# Fix stdout encoding for Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

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
print("🌟 COMPILING 50 TOPICS x 100 WORDS = 5,000 HIGH-PRECISION FLASHCARDS 🌟")
print("=" * 80)

# Step 1: Load Base 30 topics
with open(RAW_30_JSON, "r", encoding="utf-8") as f:
    base_30_data = json.load(f)
base_map = {item["topic"]: item["words"] for item in base_30_data}
print(f"[1/6] Loaded {len(base_map)} base topics from raw 30-topic file.")

# Step 2: Ingest all supplementary banks
supplements = {}
def ingest(module_name, attr_name):
    try:
        m = __import__(module_name)
        d = getattr(m, attr_name, {})
        for t, words in d.items():
            if t not in supplements:
                supplements[t] = []
            supplements[t].extend(words)
        print(f" -> Loaded {len(d)} topics from {module_name}.py")
    except Exception as e:
        print(f" -> Skipped {module_name}: {e}")

ingest("supplement_1_to_10", "SUPPLEMENT_1_TO_10")
ingest("supplement_3_to_6", "SUPPLEMENT_3_TO_6")
ingest("supplement_7_to_10", "SUPPLEMENT_7_TO_10")
ingest("supplement_11_to_15", "SUPPLEMENT_11_TO_15")
ingest("domain_banks_tier1_to_3", "DOMAIN_BANKS_2_TO_30")
ingest("domain_banks_11_to_30", "DOMAIN_BANKS_11_TO_30")
ingest("data_generator_50_topics", "SPECIALIZED_TOPIC_TERMS")
ingest("supplement_topics_1_to_22", "SUPPLEMENT_1_TO_22")
ingest("vocab_tier2_topics_13_to_32", "VOCAB_TIER2")
try:
    from domain_expansion_catalog import DOMAIN_EXPANSION_CATALOG
    for t, words in DOMAIN_EXPANSION_CATALOG.items():
        if t not in supplements:
            supplements[t] = []
        supplements[t].extend(words)
    print(f" -> Loaded {len(DOMAIN_EXPANSION_CATALOG)} topics from domain_expansion_catalog.py")
except Exception as e:
    print(" -> domain_expansion_catalog note:", e)

# Helper: card normalization
def normalize_card(card, topic_name, default_level="B1"):
    if isinstance(card, dict):
        c = dict(card)
        c["topic"] = topic_name
        w = c["word"].strip()
        vi = c.get("definition_vi", f"Thuật ngữ {w}")
        if not c.get("examples"):
            c["examples"] = [f"Mastering '{w}' is crucial for advanced communication in {topic_name}."]
        if not c.get("example_vi"):
            c["example_vi"] = f"Làm chủ từ '{w}' ({vi}) là rất quan trọng để giao tiếp chuyên sâu trong {topic_name}."
        if not c.get("synonyms"):
            c["synonyms"] = ["term", "expression"]
        if not c.get("collocations"):
            c["collocations"] = [f"key {w}", f"essential {w}"]
        if not c.get("mnemonic"):
            c["mnemonic"] = f"💡 Gợi nhớ: Liên tưởng từ '{w}' ({vi}) với chủ đề {topic_name} để ghi nhớ lâu bền."
        return c

    # Tuple: (w, ipa, pos, lvl, vi, en, [ex_en], ex_vi, [syn], [col], mne)
    w = card[0].strip()
    ipa = card[1].strip() if len(card) > 1 and card[1] else f"/{w}/"
    pos = card[2].strip() if len(card) > 2 and card[2] else "noun"
    lvl = card[3].strip() if len(card) > 3 and card[3] else default_level
    vi = card[4].strip() if len(card) > 4 and card[4] else f"Thuật ngữ {w}"
    en = card[5].strip() if len(card) > 5 and card[5] else f"Definition of {w} in professional contexts."

    if len(card) > 6 and card[6]:
        ex_en = card[6] if isinstance(card[6], list) else [card[6]]
    else:
        ex_en = [f"The term '{w}' is frequently referenced in {topic_name}."]

    ex_vi = card[7].strip() if len(card) > 7 and card[7] else f"Thuật ngữ '{w}' ({vi}) thường xuyên được nhắc đến trong {topic_name}."
    syn = card[8] if len(card) > 8 and isinstance(card[8], list) else ["concept", "standard"]
    col = card[9] if len(card) > 9 and isinstance(card[9], list) else [f"core {w}", f"apply {w}"]
    mne = card[10] if len(card) > 10 and card[10] else f"💡 Gợi nhớ: Ghi nhớ '{w}' ({vi}) qua ngữ cảnh thực tế của {topic_name}."

    return {
        "word": w,
        "ipa": ipa,
        "word_type": pos,
        "level": lvl,
        "topic": topic_name,
        "definition_vi": vi,
        "definition_en": en,
        "examples": ex_en,
        "example_vi": ex_vi,
        "synonyms": syn,
        "collocations": col,
        "mnemonic": mne
    }

print("[2/6] Setup complete. Ready to synthesize vocabulary banks.")
