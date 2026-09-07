"""
scripts/build_reserve_lexicon.py
Generates scripts/data/master_lexicon_gap_filler.py
Contains authentic professional vocabulary for all remaining slots across 50 topics.
"""

import sys
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
OUT_FILE = BASE_DIR / "scripts" / "data" / "master_lexicon_gap_filler.py"

print("Building reserve lexicon gap filler...")
