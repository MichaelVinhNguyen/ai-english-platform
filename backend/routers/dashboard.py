from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy import select, func, desc
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from backend.database.database import get_db
from backend.database.models import User, StudySession
from backend.database.schemas import DashboardStats
from backend.services.ai_engine import ai_engine
from backend.services.gamification_service import gamification_service
from backend.routers.auth import get_current_user

dashboard_router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])

@dashboard_router.get("/stats", response_model=DashboardStats)
async def get_dashboard(current_user: User = Depends(get_current_user),
                         db: AsyncSession = Depends(get_db)):
    today_start = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0)

    # Today XP from sessions
    r = await db.execute(
        select(func.sum(StudySession.xp_earned))
        .where(StudySession.user_id == current_user.id,
               StudySession.started_at >= today_start)
    )
    today_xp = r.scalar() or 0

    # Total study time
    r2 = await db.execute(
        select(func.sum(StudySession.duration_sec))
        .where(StudySession.user_id == current_user.id)
    )
    total_sec = r2.scalar() or 0

    # Vocabulary stats
    from backend.database.models import UserVocabulary
    r3 = await db.execute(
        select(func.count()).where(UserVocabulary.user_id == current_user.id,
                                   UserVocabulary.is_learned == True)
    )
    vocab_learned = r3.scalar() or 0

    # Due flashcards
    now = datetime.now(timezone.utc)
    r4 = await db.execute(
        select(func.count()).where(UserVocabulary.user_id == current_user.id,
                                   UserVocabulary.due_date <= now)
    )
    due_flashcards = r4.scalar() or 0

    # Lessons completed
    r5 = await db.execute(
        select(func.count()).where(StudySession.user_id == current_user.id,
                                   StudySession.session_type == "lesson")
    )
    lessons_done = r5.scalar() or 0

    # Recent activity
    r6 = await db.execute(
        select(StudySession).where(StudySession.user_id == current_user.id)
        .order_by(desc(StudySession.started_at)).limit(5)
    )
    recent = [{"type": s.session_type, "skill": s.skill, "xp": s.xp_earned,
               "score": s.score, "at": s.started_at} for s in r6.scalars()]

    level = gamification_service.calculate_level(current_user.xp)
    xp_next = gamification_service.xp_to_next_level(current_user.xp, level)
    xp_pct  = gamification_service.xp_progress_percent(current_user.xp, level)

    # Dynamic skill scores based on lessons completed & level
    base_score = min(95, 50 + (level * 4))
    skill_scores = {
        "vocabulary": min(100, base_score + (min(vocab_learned, 50) // 5)),
        "grammar": base_score,
        "listening": max(40, base_score - 5),
        "speaking": max(40, base_score - 10),
        "reading": min(100, base_score + 5),
        "writing": base_score
    }

    # Intelligent Next Best Action
    if due_flashcards > 0:
        next_action = {
            "type": "flashcards",
            "title": f"Ôn tập {due_flashcards} từ vựng Flashcard đến hạn",
            "action_url": "flashcards",
            "reason": "Duy trì chuỗi nhớ từ vựng hôm nay (+20 XP)"
        }
    else:
        next_action = {
            "type": "teacher",
            "title": f"Học giao tiếp AI Teacher (Level {current_user.target_level or 'B1'})",
            "action_url": "teacher",
            "reason": "Thực hành hội thoại thực tế cùng AI Teacher (+15 XP)"
        }

    return {
        "xp": current_user.xp, "level": level,
        "level_name": gamification_service.get_level_name(level),
        "coins": current_user.coins, "streak": current_user.streak,
        "xp_to_next_level": xp_next, "xp_progress_percent": xp_pct,
        "today_xp": today_xp, "daily_goal_xp": current_user.daily_goal_xp,
        "total_vocab_learned": vocab_learned, "total_lessons_completed": lessons_done,
        "total_study_time_min": total_sec // 60,
        "skill_scores": skill_scores,
        "next_recommended_action": next_action,
        "recent_activity": recent, "due_flashcards": due_flashcards,
    }

@dashboard_router.get("/leaderboard")
async def leaderboard(limit: int = 10, db: AsyncSession = Depends(get_db),
                       current_user: User = Depends(get_current_user)):
    r = await db.execute(
        select(User).where(User.is_active == True)
        .order_by(desc(User.xp)).limit(limit)
    )
    users = r.scalars().all()
    return [{"rank": i+1, "user_id": u.id, "username": u.username,
             "full_name": u.full_name, "level": u.level, "xp": u.xp,
             "streak": u.streak, "avatar_url": u.avatar_url}
            for i, u in enumerate(users)]

@dashboard_router.get("/recommend")
async def get_recommendations(current_user: User = Depends(get_current_user)):
    user_data = {
        "level": current_user.target_level or "B1",
        "target": "Giao tiếp tốt",
        "daily_minutes": 30,
    }
    result = await ai_engine.recommend_learning_path(user_data)
    return result
