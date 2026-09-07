"""
scripts/build_5000_flashcards_master.py
Master compiler that generates all 50 Topics x 100 Words = 5,000 Flashcards.
"""

import os
import sys
import json
import sqlite3
import re
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR / "scripts"))

from flashcard_topics_def import ALL_50_TOPICS_META
from vocab_supplement_1_to_10 import SUPPLEMENT_1_TO_10

print("[BUILDER] Starting master generator for 50 Topics x 100 Words...")
