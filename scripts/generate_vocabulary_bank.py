"""
scripts/generate_vocabulary_bank.py
High-quality curated terminology bank for 50 Flashcard Topics.
"""

import re
import json

# Helper to format clean flashcard dictionary item
def make_fc(word, ipa, pos, level, topic, vi, en, ex_en, ex_vi=None, syn=None, col=None, mne=None):
    if not ex_vi:
        ex_vi = f"Ví dụ cho từ '{word}': {ex_en}"
    if not syn:
        syn = []
    if not col:
        col = [f"{word} usage", f"apply {word}"]
    if not mne:
        mne = f"💡 Mẹo nhớ: Ghi nhớ từ '{word}' ({pos}) qua ngữ cảnh: {vi}."
    return {
        "word": word,
        "ipa": ipa,
        "word_type": pos,
        "level": level,
        "topic": topic,
        "definition_vi": vi,
        "definition_en": en,
        "examples": [ex_en],
        "example_vi": ex_vi,
        "synonyms": syn,
        "collocations": col,
        "mnemonic": mne
    }

print("[HELPER] make_fc ready.")
