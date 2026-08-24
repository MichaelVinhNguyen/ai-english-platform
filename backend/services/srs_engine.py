"""
srs_engine.py – Anki SM-2 Spaced Repetition System
Thuật toán lặp lại ngắt quãng cho flashcard
"""
from datetime import datetime, timedelta, timezone
from typing import Dict


class SRSEngine:
    """
    SM-2 algorithm implementation (same as Anki).
    Quality: 0=Fail/forgot, 1=Fail hint, 2=Pass hard, 3=Pass ok, 4=Pass good, 5=Perfect
    """

    INITIAL_EASE_FACTOR = 2.5
    MIN_EASE_FACTOR     = 1.3
    MAX_EASE_FACTOR     = 4.0

    def calculate_next_review(
        self,
        ease_factor: float,
        interval_days: int,
        repetitions: int,
        quality: int,
    ) -> Dict:
        """
        Returns updated SRS params after a review with given quality.
        """
        if quality < 3:
            # Failed: reset
            new_repetitions = 0
            new_interval = 1
            new_ef = max(
                self.MIN_EASE_FACTOR,
                ease_factor - 0.2 * (5 - quality) * (0.08 + (5 - quality) * 0.02)
            )
        else:
            # Passed
            if repetitions == 0:
                new_interval = 1
            elif repetitions == 1:
                new_interval = 6
            else:
                new_interval = round(interval_days * ease_factor)

            new_repetitions = repetitions + 1
            new_ef = ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
            new_ef = max(self.MIN_EASE_FACTOR, min(self.MAX_EASE_FACTOR, new_ef))

        due_date = datetime.now(timezone.utc) + timedelta(days=new_interval)
        return {
            "ease_factor":   round(new_ef, 2),
            "interval_days": new_interval,
            "repetitions":   new_repetitions,
            "due_date":      due_date,
        }

    def is_due(self, due_date: datetime) -> bool:
        now = datetime.now(timezone.utc)
        if due_date.tzinfo is None:
            due_date = due_date.replace(tzinfo=timezone.utc)
        return now >= due_date

    def get_retention_rate(self, review_count: int, correct_count: int) -> float:
        if review_count == 0:
            return 0.0
        return round(correct_count / review_count * 100, 1)

    def estimate_daily_reviews(self, total_cards: int, ease_factor: float = 2.5) -> int:
        """Estimate daily reviews needed."""
        return max(10, round(total_cards / ease_factor))


srs_engine = SRSEngine()
