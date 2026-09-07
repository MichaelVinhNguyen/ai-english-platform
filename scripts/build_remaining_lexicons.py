"""
scripts/build_remaining_lexicons.py
Generates the remaining domain catalogs for Topics 24 to 50.
"""

import sys
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "scripts" / "data"

print("Compiling remaining domain catalogs...")
