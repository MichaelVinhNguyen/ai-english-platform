"""
scripts/seed_5000_flashcards.py
Builds and seeds the complete 50 Topics x 100 Words = 5,000 Flashcards dataset.
"""

import os
import sys
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR / "scripts"))

from flashcard_topics_def import ALL_50_TOPICS_META

print("[SEEDER] Setting up full 5000 flashcards seeder...")
