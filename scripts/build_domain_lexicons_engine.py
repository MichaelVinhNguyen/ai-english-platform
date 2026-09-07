"""
scripts/build_domain_lexicons_engine.py
Writes scripts/data/master_domain_lexicon.py containing complete curated catalogs
for all remaining topics (Topics 26 to 50).
"""

import sys
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
OUT_FILE = BASE_DIR / "scripts" / "data" / "master_domain_lexicon.py"

print("Starting build of master_domain_lexicon.py...")
