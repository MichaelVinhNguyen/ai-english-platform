import sys, json
from pathlib import Path

# Ensure UTF-8
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR / "scripts"))
sys.path.append(str(BASE_DIR / "scripts" / "data"))

from flashcard_topics_def import ALL_50_TOPICS_META

RAW_30_JSON = BASE_DIR / "data" / "vocabulary" / "flashcards_30_topics_1500_words.json"
with open(RAW_30_JSON, "r", encoding="utf-8") as f:
    base_data = json.load(f)
base_map = {item["topic"]: item["words"] for item in base_data}

supps = {}
def load_s(mod, attr):
    try:
        m = __import__(mod)
        d = getattr(m, attr, {})
        for t, words in d.items():
            supps.setdefault(t, []).extend(words)
    except Exception as e:
        pass

load_s("supplement_1_to_10", "SUPPLEMENT_1_TO_10")
load_s("supplement_3_to_6", "SUPPLEMENT_3_TO_6")
load_s("supplement_7_to_10", "SUPPLEMENT_7_TO_10")
load_s("supplement_11_to_15", "SUPPLEMENT_11_TO_15")
load_s("domain_banks_tier1_to_3", "DOMAIN_BANKS_2_TO_30")
load_s("domain_banks_11_to_30", "DOMAIN_BANKS_11_TO_30")
load_s("data_generator_50_topics", "SPECIALIZED_TOPIC_TERMS")
load_s("supplement_topics_1_to_22", "SUPPLEMENT_1_TO_22")
load_s("data_tier_lexicon", "ADDITIONAL_TERMS_13_TO_32")

total_words = 0
for meta in ALL_50_TOPICS_META:
    t = meta["topic"]
    seen = set()
    if t in base_map:
        for w in base_map[t]: seen.add(w["word"].strip().lower())
    if t in supps:
        for w in supps[t]:
            w_val = w["word"] if isinstance(w, dict) else w[0]
            seen.add(w_val.strip().lower())
    total_words += len(seen)
    print(f"{meta['id']:02d}. {t[:42]:<42}: {len(seen)} words")

print(f"\nTotal authentic words collected: {total_words}")
