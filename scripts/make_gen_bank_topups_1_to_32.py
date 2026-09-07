"""
scripts/make_gen_bank_topups_1_to_32.py
Generates genuine English terms for all remaining slots in Topics 1 to 32.
"""

import sys, json
from pathlib import Path

# Ensure UTF-8
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

BASE_DIR = Path(__file__).parent.parent
OUT_FILE = BASE_DIR / "scripts" / "data" / "gen_bank_topups_1_to_32.py"

print("Compiling gen_bank_topups_1_to_32...")
