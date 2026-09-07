"""
scripts/build_all_specialized_terms.py
Builds authentic specialized terms for Topics 35 to 50 (100 words per topic).
Writes directly to scripts/data/mega_specialized_35_to_50.py.
"""

import sys
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
OUT_FILE = BASE_DIR / "scripts" / "data" / "mega_specialized_35_to_50.py"

print("Compiling specialized terms for Topics 35 to 50...")
