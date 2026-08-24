from fastapi import APIRouter, Depends
from sqlalchemy import select, func, desc
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from backend.database.database import get_db
from backend.database.models import User, Course, Lesson, StudySession, UserQuizAttempt, Vocabulary
from backend.database.schemas import AdminStats
from backend.routers.auth import get_admin_user

admin_router = APIRouter(prefix="/api/admin", tags=["Admin"])

@admin_router.get("/stats")
async def admin_stats(admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    today_start = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0)
    total_users = (await db.execute(select(func.count(User.id)))).scalar()
    active_today = (await db.execute(
        select(func.count(User.id)).where(User.last_study_date >= today_start)
    )).scalar()
    total_courses = (await db.execute(select(func.count(Course.id)))).scalar()
    total_lessons = (await db.execute(select(func.count(Lesson.id)))).scalar()
    total_vocab = (await db.execute(select(func.count(Vocabulary.id)))).scalar()
    total_sessions = (await db.execute(select(func.count(StudySession.id)))).scalar()
    total_quiz = (await db.execute(select(func.count(UserQuizAttempt.id)))).scalar()
    return AdminStats(
        total_users=total_users, active_users_today=active_today,
        total_courses=total_courses, total_lessons=total_lessons,
        total_vocabulary=total_vocab, total_study_sessions=total_sessions,
        total_quiz_attempts=total_quiz,
    )

@admin_router.get("/users")
async def list_users(limit: int = 100, admin: User = Depends(get_admin_user),
                      db: AsyncSession = Depends(get_db)):
    r = await db.execute(select(User).order_by(desc(User.created_at)).limit(limit))
    users = r.scalars().all()
    return [{
        "id": u.id,
        "email": u.email,
        "username": u.username,
        "full_name": u.full_name or u.username,
        "role": u.role,
        "level": u.level,
        "xp": u.xp,
        "coins": u.coins,
        "streak": u.streak,
        "last_study_date": u.last_study_date,
        "is_active": u.is_active,
        "created_at": u.created_at
    } for u in users]

@admin_router.get("/study-activity")
async def get_study_activity(limit: int = 30, admin: User = Depends(get_admin_user),
                              db: AsyncSession = Depends(get_db)):
    r = await db.execute(select(StudySession).order_by(desc(StudySession.start_time)).limit(limit))
    sessions = r.scalars().all()
    result = []
    for s in sessions:
        user_res = await db.execute(select(User).where(User.id == s.user_id))
        user = user_res.scalar_one_or_none()
        result.append({
            "id": s.id,
            "user_id": s.user_id,
            "email": user.email if user else "Unknown",
            "username": user.username if user else "Unknown",
            "session_type": s.session_type,
            "duration_seconds": s.duration_seconds,
            "xp_earned": s.xp_earned,
            "start_time": s.start_time
        })
    return result

@admin_router.post("/users/{user_id}/toggle-active")
async def toggle_user(user_id: int, admin: User = Depends(get_admin_user),
                       db: AsyncSession = Depends(get_db)):
    r = await db.execute(select(User).where(User.id == user_id))
    user = r.scalar_one_or_none()
    if not user: return {"error": "User not found"}
    user.is_active = not user.is_active
    await db.commit()
    return {"is_active": user.is_active, "message": f"Tài khoản đã được {'kích hoạt' if user.is_active else 'khóa'}."}

@admin_router.post("/users/{user_id}/change-role")
async def change_role(user_id: int, role: str, admin: User = Depends(get_admin_user),
                       db: AsyncSession = Depends(get_db)):
    r = await db.execute(select(User).where(User.id == user_id))
    user = r.scalar_one_or_none()
    if not user: return {"error": "User not found"}
    if role not in ["user", "teacher", "admin"]:
        return {"error": "Role không hợp lệ"}
    user.role = role
    await db.commit()
    return {"id": user.id, "role": user.role, "message": f"Đã chuyển quyền của {user.email} thành {role.upper()}."}

@admin_router.delete("/users/{user_id}")
async def delete_user(user_id: int, admin: User = Depends(get_admin_user),
                       db: AsyncSession = Depends(get_db)):
    if user_id == admin.id:
        return {"error": "Không thể xóa tài khoản của chính bạn"}
    r = await db.execute(select(User).where(User.id == user_id))
    user = r.scalar_one_or_none()
    if not user: return {"error": "User not found"}
    await db.delete(user)
    await db.commit()
    return {"success": True, "message": f"Đã xóa tài khoản {user.email}."}

@admin_router.post("/seed-data")
async def seed_data(admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    """Seed demo data."""
    from backend.database.models import Badge, Mission, GrammarRule
    # Seed Badges
    badges_data = [
        Badge(name="🔥 Streak 7 ngày", description="Học 7 ngày liên tục", icon="🔥",
               category="streak", condition_type="streak_days", condition_value=7, xp_reward=100),
        Badge(name="📚 100 từ vựng", description="Học được 100 từ vựng", icon="📚",
               category="vocabulary", condition_type="vocab_count", condition_value=100, xp_reward=150),
        Badge(name="⭐ Cấp 5", description="Đạt cấp độ 5", icon="⭐",
               category="level", condition_type="level", condition_value=5, xp_reward=200),
        Badge(name="🏆 Bậc thầy ngữ pháp", description="Quiz ngữ pháp 10 điểm", icon="🏆",
               category="grammar", condition_type="quiz_score", condition_value=10, xp_reward=100),
    ]
    for b in badges_data:
        db.add(b)

    # Seed Missions
    missions_data = [
        Mission(title="Ôn tập 10 flashcard", description="Ôn tập 10 từ vựng hôm nay",
                 mission_type="daily", condition_type="vocab_reviewed", condition_value=10,
                 xp_reward=30, coin_reward=5),
        Mission(title="Làm 1 quiz", description="Hoàn thành ít nhất 1 bài quiz",
                 mission_type="daily", condition_type="quiz_correct", condition_value=1,
                 xp_reward=20, coin_reward=3),
        Mission(title="Chat với AI Teacher", description="Chat ít nhất 5 tin nhắn với AI Teacher",
                 mission_type="daily", condition_type="chat_messages", condition_value=5,
                 xp_reward=25, coin_reward=5),
    ]
    for m in missions_data:
        db.add(m)

    # Seed Grammar Rules
    grammar_data = [
        GrammarRule(title="Present Simple", category="tenses", level="A1",
                     explanation="Diễn đạt thói quen, sự thật hiển nhiên",
                     examples=[{"en": "She works every day.", "vi": "Cô ấy làm việc mỗi ngày."}]),
        GrammarRule(title="Present Continuous", category="tenses", level="A1",
                     explanation="Diễn đạt hành động đang xảy ra",
                     examples=[{"en": "He is reading now.", "vi": "Anh ấy đang đọc sách."}]),
        GrammarRule(title="Past Simple", category="tenses", level="A2",
                     explanation="Diễn đạt hành động đã hoàn thành trong quá khứ",
                     examples=[{"en": "I visited London last year.", "vi": "Tôi đã thăm London năm ngoái."}]),
    ]
    for g in grammar_data:
        db.add(g)

    await db.commit()
    return {"message": "Đã tạo dữ liệu mẫu thành công!"}

@admin_router.get("/ai-config")
async def get_admin_ai_config(admin: User = Depends(get_admin_user)):
    from backend.ai_config_manager import get_ai_config
    return get_ai_config()

@admin_router.post("/ai-config")
async def update_admin_ai_config(payload: dict, admin: User = Depends(get_admin_user)):
    from backend.ai_config_manager import save_ai_config
    updated = save_ai_config(payload)
    from backend.services.ai_engine import ai_engine
    try:
        ai_engine.reload_config()
    except Exception as err:
        print("Error reloading AI config in-memory:", err)
    return {"success": True, "message": "Đã lưu cấu hình AI Engine & API mới thành công!", "config": updated}

@admin_router.get("/ai-profiles")
async def get_ai_profiles(admin: User = Depends(get_admin_user)):
    from backend.ai_config_manager import get_ai_config
    cfg = get_ai_config()
    return {
        "profiles": cfg.get("profiles", []),
        "active_profile_id": cfg.get("active_profile_id"),
        "current_model": cfg.get("model"),
        "current_provider": cfg.get("provider")
    }

@admin_router.post("/ai-profiles")
async def save_or_add_ai_profile(profile: dict, admin: User = Depends(get_admin_user)):
    import uuid
    from datetime import datetime, timezone
    from backend.ai_config_manager import get_ai_config, save_ai_config

    cfg = get_ai_config()
    profiles = cfg.get("profiles", [])

    p_id = profile.get("id") or str(uuid.uuid4())[:8]
    profile["id"] = p_id
    profile["created_at"] = profile.get("created_at") or datetime.now(timezone.utc).isoformat()

    existing_idx = next((i for i, p in enumerate(profiles) if p.get("id") == p_id), None)
    if existing_idx is not None:
        profiles[existing_idx].update(profile)
    else:
        profiles.append(profile)

    cfg["profiles"] = profiles
    if profile.get("is_active"):
        cfg["active_profile_id"] = p_id

    updated = save_ai_config(cfg)
    from backend.services.ai_engine import ai_engine
    try:
        ai_engine.reload_config()
    except Exception as err:
        print("Error reloading AI config:", err)

    return {"success": True, "message": f"Đã lưu cấu hình AI '{profile.get('name')}' thành công!", "profile": profile, "config": updated}

@admin_router.delete("/ai-profiles/{profile_id}")
async def delete_ai_profile(profile_id: str, admin: User = Depends(get_admin_user)):
    from backend.ai_config_manager import get_ai_config, save_ai_config
    cfg = get_ai_config()
    profiles = cfg.get("profiles", [])
    if len(profiles) <= 1:
        return {"error": "Phải giữ lại ít nhất một cấu hình API mặc định trong hệ thống."}

    new_profiles = [p for p in profiles if p.get("id") != profile_id]
    cfg["profiles"] = new_profiles
    if cfg.get("active_profile_id") == profile_id and len(new_profiles) > 0:
        cfg["active_profile_id"] = new_profiles[0]["id"]

    updated = save_ai_config(cfg)
    from backend.services.ai_engine import ai_engine
    try:
        ai_engine.reload_config()
    except Exception as err:
        print("Error reloading AI config:", err)

    return {"success": True, "message": f"Đã xóa cấu hình API thành công!", "config": updated}

@admin_router.post("/ai-profiles/{profile_id}/activate")
async def activate_ai_profile(profile_id: str, admin: User = Depends(get_admin_user)):
    from backend.ai_config_manager import get_ai_config, save_ai_config
    cfg = get_ai_config()
    cfg["active_profile_id"] = profile_id
    updated = save_ai_config(cfg)

    from backend.services.ai_engine import ai_engine
    try:
        ai_engine.reload_config()
    except Exception as err:
        print("Error reloading AI config:", err)

    return {
        "success": True,
        "message": f"Đã kích hoạt AI Profile '{profile_id}' làm API chính thức!",
        "active_profile_id": profile_id,
        "provider": updated.get("provider"),
        "model": updated.get("model")
    }

@admin_router.post("/test-ai-connection")
async def test_ai_connection(payload: dict, admin: User = Depends(get_admin_user)):
    from backend.services.ai_engine import ai_engine
    result = await ai_engine.test_connection(payload)
    return result


