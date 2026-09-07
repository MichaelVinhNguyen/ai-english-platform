"""
scripts/master_generate_5000_flashcards.py
Master compiler that generates all 50 Topics x 100 Words = 5,000 Flashcards.
"""

import sys
import json
import sqlite3
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR / "scripts"))

from flashcard_topics_def import ALL_50_TOPICS_META
from topics_data_1_to_10 import TOPICS_1_TO_10
from topics_data_11_to_20 import TOPICS_11_TO_20
from topics_data_21_to_30 import TOPICS_21_TO_30
from flashcards_generator_data1 import SUPPLEMENT_TOPICS_1_TO_15

print("[BUILDER] Loaded existing topics 1 to 30.")
