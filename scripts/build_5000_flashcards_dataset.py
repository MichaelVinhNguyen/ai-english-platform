"""
scripts/build_5000_flashcards_dataset.py
Master builder for 50 Topics x 100 Words = 5,000 Flashcards.
"""

import sys
import json
import sqlite3
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR / "scripts"))

from flashcard_topics_def import ALL_50_TOPICS_META

print(f"[BUILDER] Starting generation of 50 Topics x 100 Words...")
