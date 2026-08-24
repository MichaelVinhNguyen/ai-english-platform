"""
gamification_service.py – XP, Level, Streak, Badge, Coin logic
"""
from datetime import datetime, date, timezone
from typing import Dict, List, Optional
from backend.config import settings, LEVEL_THRESHOLDS, LEVEL_NAMES


class GamificationService:

    # ── XP & LEVEL ────────────────────────────────────────────────────────────
    def calculate_level(self, total_xp: int) -> int:
        level = 1
        for lvl, threshold in sorted(LEVEL_THRESHOLDS.items(), reverse=True):
            if total_xp >= threshold:
                level = lvl
                break
        return level

    def get_level_name(self, level: int) -> str:
        return LEVEL_NAMES.get(level, "Học Viên")

    def xp_to_next_level(self, total_xp: int, current_level: int) -> int:
        next_level = current_level + 1
        if next_level not in LEVEL_THRESHOLDS:
            return 0
        return LEVEL_THRESHOLDS[next_level] - total_xp

    def xp_progress_percent(self, total_xp: int, current_level: int) -> float:
        curr_threshold = LEVEL_THRESHOLDS.get(current_level, 0)
        next_threshold = LEVEL_THRESHOLDS.get(current_level + 1, curr_threshold + 1000)
        progress = (total_xp - curr_threshold) / (next_threshold - curr_threshold)
        return round(min(100.0, max(0.0, progress * 100)), 1)

    def calculate_xp_reward(self, activity_type: str, score: float = 1.0) -> int:
        base = {
            "lesson_complete": settings.XP_PER_LESSON,
            "quiz_correct":    settings.XP_PER_QUIZ_CORRECT,
            "vocab_review":    settings.XP_PER_VOCAB,
            "streak_bonus":    settings.XP_PER_STREAK_DAY,
            "writing":         30,
            "speaking":        25,
            "reading":         20,
        }.get(activity_type, 5)
        return int(base * max(0.5, score))

    # ── STREAK ────────────────────────────────────────────────────────────────
    def update_streak(self, last_study_date: Optional[datetime], current_streak: int) -> Dict:
        today = date.today()
        if last_study_date is None:
            return {"streak": 1, "bonus_xp": 0, "streak_maintained": True}

        last = last_study_date.date() if isinstance(last_study_date, datetime) else last_study_date
        diff = (today - last).days

        if diff == 0:
            return {"streak": current_streak, "bonus_xp": 0, "streak_maintained": True}
        elif diff == 1:
            new_streak = current_streak + 1
            bonus_xp = settings.XP_PER_STREAK_DAY if new_streak % 7 == 0 else 0
            return {"streak": new_streak, "bonus_xp": bonus_xp, "streak_maintained": True}
        else:
            return {"streak": 1, "bonus_xp": 0, "streak_maintained": False}

    # ── BADGE CHECK ───────────────────────────────────────────────────────────
    def check_badge_conditions(self, user_stats: Dict) -> List[str]:
        """Returns list of badge names the user has just earned."""
        earned = []
        streak = user_stats.get("streak", 0)
        vocab_count = user_stats.get("total_vocab_learned", 0)
        level = user_stats.get("level", 1)

        if streak >= 7:   earned.append("Streak 7 ngày")
        if streak >= 30:  earned.append("Streak 30 ngày")
        if vocab_count >= 100: earned.append("100 từ vựng")
        if vocab_count >= 500: earned.append("500 từ vựng")
        if level >= 5:    earned.append("Level 5")
        if level >= 10:   earned.append("Master")

        return earned

    # ── COINS ─────────────────────────────────────────────────────────────────
    def calculate_coin_reward(self, activity_type: str, level_up: bool = False) -> int:
        base = {"lesson_complete": 10, "quiz_perfect": 20, "writing": 15}.get(activity_type, 5)
        if level_up:
            base += settings.COIN_PER_LEVEL_UP
        return base


gamification_service = GamificationService()
