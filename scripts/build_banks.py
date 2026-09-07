"""
scripts/build_banks.py
Generates authentic vocabulary banks for Topics 33-50 and remaining topics.
Each word has genuine IPA, part of speech, CEFR level, Vietnamese translation, and English definition.
"""

import sys
import json
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

print("Starting vocabulary bank generation...")
