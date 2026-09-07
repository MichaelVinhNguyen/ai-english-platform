import sys
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR / "scripts"))
sys.path.append(str(BASE_DIR / "scripts" / "data"))

from flashcard_topics_def import ALL_50_TOPICS_META

RAW_30_JSON = BASE_DIR / "data" / "vocabulary" / "flashcards_30_topics_1500_words.json"
with open(RAW_30_JSON, "r", encoding="utf-8") as f:
    base_30_data = json.load(f)
base_map = {item["topic"]: item["words"] for item in base_30_data}

modules_to_load = [
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
    ("lexicon_part_c1_computing_ai", "COMPUTING_AI"),
    ("specialized_part_1", "SPECIALIZED_PART_1"),
    ("specialized_part_2", "SPECIALIZED_PART_2"),
    ("specialized_part_3", "SPECIALIZED_PART_3"),
    ("mega_tech_med_33_to_38", "SPECIALIZED_33_TO_38"),
    ("mega_final_reserve_bank", "MEGA_RESERVE"),
    ("lexicon_filler_tier1", "FILLER_TIER1"),
    ("topup_part1_topics_2_to_32", "TOPUP_PART1"),
    ("topup_part1b_topics_26_to_32", "TOPUP_PART1B"),
    ("topup_part2_topics_2_to_32", "TOPUP_PART2"),
    ("topup_part2b_topics_2_to_32", "TOPUP_PART2B"),
    ("topup_part2c_finish_1_to_32", "TOPUP_PART2C"),
    ("topup_part3_topics_33_to_36", "TOPUP_PART3"),
    ("topup_part4_topics_37_to_40", "TOPUP_PART4"),
    ("topup_part5_topics_41_to_45", "TOPUP_PART5"),
]

all_supps = {}
for mod_name, attr_name in modules_to_load:
    try:
        m = __import__(mod_name)
        d = getattr(m, attr_name, {})
        for t, words in d.items():
            all_supps.setdefault(t, []).extend(words)
    except Exception as e:
        print(f"Error loading {mod_name}: {e}")

try:
    import data_46
    import data_47
    import data_48
    import data_49
    import data_50
    all_supps.setdefault("TOEIC Corporate: HR, Personnel & Office Operations", []).extend(data_46.get_46())
    all_supps.setdefault("IELTS Academic Band 8.0+: Academic Vocabulary & Collocations", []).extend(data_47.get_47())
    all_supps.setdefault("IELTS Scientific Research, Methodology & Critical Thinking", []).extend(data_48.get_48())
    all_supps.setdefault("IELTS Social Issues: Demographic Shifts & Urbanization", []).extend(data_49.get_49())
    all_supps.setdefault("High-Level Debate, Rhetoric & Philosophical Discourse", []).extend(data_50.get_50())
except Exception as e:
    print(f"Error loading data_46..50: {e}")

total_words = 0

short_topics = []
for meta in ALL_50_TOPICS_META:
    t = meta["topic"]
    seen = set()
    if t in base_map:
        for w in base_map[t]:
            seen.add(w["word"].strip().lower())
    if t in all_supps:
        for w in all_supps[t]:
            w_val = w["word"] if isinstance(w, dict) else w[0]
            seen.add(w_val.strip().lower())
    count = len(seen)
    total_words += count
    print(f"{meta['id']:02d}. {t[:42]:<42}: {count} unique words")
    if count < 100:
        short_topics.append((meta["id"], t, count, 100 - count))

print("=" * 60)
print(f"Total Unique Authentic Words Collected: {total_words}")
print(f"Short Topics Count: {len(short_topics)}")
for tid, tname, count, need in short_topics:
    print(f"  Need {need} words for #{tid}: {tname}")
