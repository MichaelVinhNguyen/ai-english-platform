"""
scripts/build_lexicon_modules.py
Generates modular term bank files for all remaining topics and top-ups.
Ensures authentic, academic, and professional terms with real IPA, POS, levels, and Vietnamese translations.
"""

import os
import sys
from pathlib import Path

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "scripts" / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

print("Writing comprehensive lexicon bank modules...")

# We will write scripts/data/lexicon_topics_33_to_41.py
# scripts/data/lexicon_topics_42_to_50.py
# scripts/data/lexicon_topups_13_to_32.py
