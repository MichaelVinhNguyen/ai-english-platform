"""
scripts/generate_all_5000_flashcards_master.py
Generates 50 Topics x 100 Words = 5,000 Flashcards and updates Database & Standalone Data.
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
from topics_data_1_to_10 import TOPICS_1_TO_10
from topics_data_11_to_20 import TOPICS_11_TO_20
from topics_data_21_to_30 import TOPICS_21_TO_30
from vocab_supplement_1_to_10 import SUPPLEMENT_1_TO_10

print("[BUILDER] Master compiler initialized.")
