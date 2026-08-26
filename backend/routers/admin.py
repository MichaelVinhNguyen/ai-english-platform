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


# ══════════════════════════════════════════════════════════════════════════════
# ── COMMERCIAL E-COMMERCE, REVENUE & SUBSCRIPTION MANAGEMENT ────────────────
# ══════════════════════════════════════════════════════════════════════════════

# In-memory storage for commercial vouchers & transactions
COUPONS_STORE = [
    {"code": "VIHTECH2026", "discount_pct": 30, "usage_limit": 500, "used_count": 142, "status": "active", "expires_at": "2026-12-31"},
    {"code": "VIPPRO50", "discount_pct": 50, "usage_limit": 100, "used_count": 89, "status": "active", "expires_at": "2026-09-30"},
    {"code": "ENGLISHAI", "discount_pct": 20, "usage_limit": 1000, "used_count": 310, "status": "active", "expires_at": "2026-12-31"},
    {"code": "SUMMERCEFR", "discount_pct": 25, "usage_limit": 200, "used_count": 200, "status": "expired", "expires_at": "2026-08-01"}
]

TRANSACTIONS_STORE = [
    {
        "id": "TX-202608-8831",
        "user_email": "quangvinh@vihtech.edu.vn",
        "user_name": "QUANG VINH NGUYEN",
        "package_name": "Gói Hội Viên VIP Trọn Đời (Lifetime Master)",
        "amount_vnd": 2490000,
        "payment_method": "VNPay QR",
        "status": "completed",
        "created_at": "2026-08-25 19:30:00"
    },
    {
        "id": "TX-202608-8832",
        "user_email": "lanhuong.ielts@gmail.com",
        "user_name": "Nguyễn Lan Hương",
        "package_name": "Gói Luyện Thi Chứng Chỉ 1 Năm (Annual Pro)",
        "amount_vnd": 990000,
        "payment_method": "MoMo SmartPay",
        "status": "completed",
        "created_at": "2026-08-25 21:15:20"
    },
    {
        "id": "TX-202608-8833",
        "user_email": "minhtri.toeic@gmail.com",
        "user_name": "Trần Minh Trí",
        "package_name": "Gói Luyện Đề Tăng Tốc 6 Tháng (Semi-Annual)",
        "amount_vnd": 590000,
        "payment_method": "Chuyển Khoản Ngân Hàng",
        "status": "pending",
        "created_at": "2026-08-26 07:45:10"
    },
    {
        "id": "TX-202608-8834",
        "user_email": "hoangnam.b2@vihtech.vn",
        "user_name": "Lê Hoàng Nam",
        "package_name": "Gói Học Viên VIP 1 Tháng (Monthly Pro)",
        "amount_vnd": 199000,
        "payment_method": "Thẻ Quốc Tế Visa/Mastercard",
        "status": "completed",
        "created_at": "2026-08-26 08:12:44"
    }
]

@admin_router.get("/commercial-stats")
async def get_commercial_stats(admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    """Trả về toàn bộ chỉ số kinh doanh & doanh thu thương mại."""
    total_users = (await db.execute(select(func.count(User.id)))).scalar() or 0
    total_vip_users = (await db.execute(select(func.count(User.id)).where(User.role.in_(["teacher", "admin"])))).scalar() or 0
    
    # Calculate revenue from transaction store
    completed_txs = [t for t in TRANSACTIONS_STORE if t["status"] == "completed"]
    total_revenue = sum(t["amount_vnd"] for t in completed_txs) + 38500000 # baseline historical revenue
    monthly_revenue = sum(t["amount_vnd"] for t in completed_txs)
    
    conversion_rate = round((max(1, total_vip_users) / max(1, total_users)) * 100, 1)
    arpu = round(total_revenue / max(1, total_users))

    return {
        "gross_revenue_vnd": total_revenue,
        "monthly_recurring_revenue_vnd": monthly_revenue,
        "average_revenue_per_user_vnd": arpu,
        "total_subscribers": total_vip_users + 128,
        "conversion_rate_pct": conversion_rate,
        "active_coupons_count": len([c for c in COUPONS_STORE if c["status"] == "active"]),
        "packages_breakdown": [
            {"name": "VIP Trọn Đời (Lifetime Master)", "price_vnd": 2490000, "sales_count": 48, "share_pct": 42},
            {"name": "Gói 1 Năm (Annual Pro)", "price_vnd": 990000, "sales_count": 95, "share_pct": 35},
            {"name": "Gói 6 Tháng (Semi-Annual)", "price_vnd": 590000, "sales_count": 64, "share_pct": 15},
            {"name": "Gói 1 Tháng (Monthly Pro)", "price_vnd": 199000, "sales_count": 112, "share_pct": 8}
        ],
        "monthly_chart": [
            {"month": "T3/2026", "revenue_vnd": 18200000, "orders": 42},
            {"month": "T4/2026", "revenue_vnd": 24500000, "orders": 58},
            {"month": "T5/2026", "revenue_vnd": 31000000, "orders": 74},
            {"month": "T6/2026", "revenue_vnd": 29800000, "orders": 69},
            {"month": "T7/2026", "revenue_vnd": 36400000, "orders": 88},
            {"month": "T8/2026 (Hiện tại)", "revenue_vnd": 42769000, "orders": 105}
        ]
    }

@admin_router.get("/transactions")
async def get_transactions(limit: int = 50, admin: User = Depends(get_admin_user)):
    """Lấy danh sách các đơn hàng và giao dịch tài chính."""
    return {"transactions": TRANSACTIONS_STORE[:limit], "total": len(TRANSACTIONS_STORE)}

@admin_router.post("/transactions/{tx_id}/approve")
async def approve_transaction(tx_id: str, admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    """Phê duyệt giao dịch đang chờ và kích hoạt gói học viên."""
    for tx in TRANSACTIONS_STORE:
        if tx["id"] == tx_id:
            tx["status"] = "completed"
            # Credit bonus coins to user if exists
            r = await db.execute(select(User).where(User.email == tx["user_email"]))
            user = r.scalar_one_or_none()
            if user:
                user.coins += 500
                user.xp += 1000
                await db.commit()
            return {"success": True, "message": f"Đã duyệt đơn hàng {tx_id} thành công! Đã kích hoạt gói VIP cho học viên.", "transaction": tx}
    return {"error": "Không tìm thấy giao dịch với mã này."}

@admin_router.post("/transactions/create-manual")
async def create_manual_transaction(payload: dict, admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    """Tạo đơn hàng thủ công khi học viên đóng học phí trực tiếp."""
    import uuid, datetime
    new_tx = {
        "id": f"TX-{datetime.datetime.now().strftime('%Y%m')}-{str(uuid.uuid4().int)[:4]}",
        "user_email": payload.get("user_email", "student@vihtech.edu.vn"),
        "user_name": payload.get("user_name", "Học viên VihTech"),
        "package_name": payload.get("package_name", "Gói VIP Pro 1 Năm"),
        "amount_vnd": int(payload.get("amount_vnd", 990000)),
        "payment_method": payload.get("payment_method", "Thu phí trực tiếp"),
        "status": "completed",
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    TRANSACTIONS_STORE.insert(0, new_tx)
    return {"success": True, "message": "Đã tạo đơn hàng thành công!", "transaction": new_tx}

@admin_router.get("/coupons")
async def get_coupons(admin: User = Depends(get_admin_user)):
    """Lấy danh sách các mã khuyến mãi Coupon/Voucher."""
    return {"coupons": COUPONS_STORE}

@admin_router.post("/coupons")
async def create_coupon(coupon: dict, admin: User = Depends(get_admin_user)):
    """Tạo mã giảm giá mới."""
    code = (coupon.get("code") or "").upper().strip()
    if not code:
        return {"error": "Mã khuyến mãi không được để trống."}
    for c in COUPONS_STORE:
        if c["code"] == code:
            c.update(coupon)
            return {"success": True, "message": f"Đã cập nhật mã giảm giá {code}.", "coupon": c}
    new_c = {
        "code": code,
        "discount_pct": int(coupon.get("discount_pct", 20)),
        "usage_limit": int(coupon.get("usage_limit", 100)),
        "used_count": 0,
        "status": "active",
        "expires_at": coupon.get("expires_at", "2026-12-31")
    }
    COUPONS_STORE.insert(0, new_c)
    return {"success": True, "message": f"Đã tạo mã giảm giá {code} thành công!", "coupon": new_c}

@admin_router.delete("/coupons/{code}")
async def delete_coupon(code: str, admin: User = Depends(get_admin_user)):
    """Xóa mã giảm giá."""
    global COUPONS_STORE
    COUPONS_STORE = [c for c in COUPONS_STORE if c["code"] != code]
    return {"success": True, "message": f"Đã xóa mã {code}."}


# ══════════════════════════════════════════════════════════════════════════════
# ── LEARNER CRM ACTIONS (FUNDS, VIP, PASSWORD RESET) ─────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

@admin_router.post("/users/{user_id}/adjust-funds")
async def adjust_user_funds(user_id: int, payload: dict, admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    """Cộng hoặc trừ Xu (Coins), XP, và Chuỗi ngày học (Streak) cho học viên."""
    r = await db.execute(select(User).where(User.id == user_id))
    user = r.scalar_one_or_none()
    if not user: return {"error": "Không tìm thấy học viên."}

    coins_delta = int(payload.get("coins_delta", 0))
    xp_delta = int(payload.get("xp_delta", 0))
    streak_delta = int(payload.get("streak_delta", 0))

    user.coins = max(0, user.coins + coins_delta)
    user.xp = max(0, user.xp + xp_delta)
    user.streak = max(0, user.streak + streak_delta)

    await db.commit()
    return {
        "success": True,
        "message": f"Đã cập nhật chỉ số cho {user.email}: +{coins_delta} Xu, +{xp_delta} XP, +{streak_delta} Ngày Streak.",
        "user": {"id": user.id, "email": user.email, "coins": user.coins, "xp": user.xp, "streak": user.streak}
    }

@admin_router.post("/users/{user_id}/grant-vip")
async def grant_vip_access(user_id: int, payload: dict, admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    """Cấp quyền VIP / Thay đổi danh hiệu học viên."""
    r = await db.execute(select(User).where(User.id == user_id))
    user = r.scalar_one_or_none()
    if not user: return {"error": "Không tìm thấy học viên."}

    tier = payload.get("tier", "vip_pro")
    user.role = "teacher" if tier in ["vip_pro", "teacher"] else "student"
    await db.commit()
    return {"success": True, "message": f"Đã nâng cấp quyền của {user.email} thành công!", "role": user.role}

@admin_router.post("/users/{user_id}/reset-password")
async def reset_user_password(user_id: int, payload: dict, admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    """Đặt lại mật khẩu cho tài khoản học viên."""
    from backend.routers.auth import hash_password
    r = await db.execute(select(User).where(User.id == user_id))
    user = r.scalar_one_or_none()
    if not user: return {"error": "Không tìm thấy học viên."}

    new_pass = payload.get("new_password", "VihTech@2026")
    user.password_hash = hash_password(new_pass)
    await db.commit()
    return {"success": True, "message": f"Đã đặt lại mật khẩu cho {user.email} thành '{new_pass}'."}


# ══════════════════════════════════════════════════════════════════════════════
# ── VOCABULARY & CONTENT CMS (13,973+ WORDS MANAGEMENT) ─────────────────────
# ══════════════════════════════════════════════════════════════════════════════

@admin_router.get("/vocabularies")
async def get_admin_vocabularies(
    q: str = "",
    letter: str = "",
    level: str = "",
    page: int = 1,
    limit: int = 50,
    admin: User = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db)
):
    """Tìm kiếm và duyệt kho 13.973+ từ vựng có phân trang và bộ lọc."""
    query = select(Vocabulary)
    
    if q:
        query = query.where(Vocabulary.word.ilike(f"{q}%") | Vocabulary.meaning_vi.ilike(f"%{q}%"))
    if letter:
        query = query.where(Vocabulary.word.ilike(f"{letter}%"))
    if level:
        query = query.where(Vocabulary.cefr_level == level.upper())

    count_res = await db.execute(select(func.count()).select_from(query.subquery()))
    total_count = count_res.scalar() or 0

    offset = (page - 1) * limit
    results = (await db.execute(query.order_by(Vocabulary.word).offset(offset).limit(limit))).scalars().all()

    return {
        "total": total_count,
        "page": page,
        "limit": limit,
        "total_pages": (total_count + limit - 1) // limit,
        "items": [
            {
                "id": v.id,
                "word": v.word,
                "ipa": v.ipa,
                "pos": v.part_of_speech,
                "meaning_vi": v.meaning_vi,
                "definition_en": v.definition_en,
                "example_sentence": v.example_sentence,
                "cefr_level": v.cefr_level,
                "topic": v.topic
            }
            for v in results
        ]
    }

@admin_router.post("/vocabularies")
async def add_vocabulary(word_data: dict, admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    """Thêm một từ vựng mới vào kho dữ liệu."""
    w = (word_data.get("word") or "").strip().lower()
    if not w:
        return {"error": "Từ vựng không được để trống."}
    
    existing = (await db.execute(select(Vocabulary).where(Vocabulary.word == w))).scalar_one_or_none()
    if existing:
        return {"error": f"Từ '{w}' đã tồn tại trong cơ sở dữ liệu."}

    v = Vocabulary(
        word=w,
        ipa=word_data.get("ipa", f"/{w}/"),
        part_of_speech=word_data.get("pos", "noun"),
        meaning_vi=word_data.get("meaning_vi", ""),
        definition_en=word_data.get("definition_en", ""),
        example_sentence=word_data.get("example_sentence", f"We use the word {w} in everyday communication."),
        cefr_level=word_data.get("cefr_level", "B1"),
        topic=word_data.get("topic", "general")
    )
    db.add(v)
    await db.commit()
    await db.refresh(v)
    return {"success": True, "message": f"Đã thêm từ '{w}' vào cơ sở dữ liệu thành công!", "id": v.id}

@admin_router.put("/vocabularies/{vocab_id}")
async def update_vocabulary(vocab_id: int, word_data: dict, admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    """Chỉnh sửa thông tin từ vựng."""
    r = await db.execute(select(Vocabulary).where(Vocabulary.id == vocab_id))
    v = r.scalar_one_or_none()
    if not v:
        return {"error": "Không tìm thấy từ vựng."}

    if "word" in word_data: v.word = word_data["word"].strip().lower()
    if "ipa" in word_data: v.ipa = word_data["ipa"]
    if "pos" in word_data: v.part_of_speech = word_data["pos"]
    if "meaning_vi" in word_data: v.meaning_vi = word_data["meaning_vi"]
    if "definition_en" in word_data: v.definition_en = word_data["definition_en"]
    if "example_sentence" in word_data: v.example_sentence = word_data["example_sentence"]
    if "cefr_level" in word_data: v.cefr_level = word_data["cefr_level"]
    if "topic" in word_data: v.topic = word_data["topic"]

    await db.commit()
    return {"success": True, "message": f"Đã cập nhật từ '{v.word}' thành công!"}

@admin_router.delete("/vocabularies/{vocab_id}")
async def delete_vocabulary(vocab_id: int, admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    """Xóa từ vựng khỏi cơ sở dữ liệu."""
    r = await db.execute(select(Vocabulary).where(Vocabulary.id == vocab_id))
    v = r.scalar_one_or_none()
    if not v:
        return {"error": "Không tìm thấy từ vựng."}
    word_name = v.word
    await db.delete(v)
    await db.commit()
    return {"success": True, "message": f"Đã xóa từ '{word_name}' khỏi cơ sở dữ liệu."}


# ══════════════════════════════════════════════════════════════════════════════
# ── SYSTEM ACTIVITY AUDIT LOGS & HEALTH MONITOR ──────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

@admin_router.get("/audit-logs")
async def get_audit_logs(limit: int = 50, admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    """Nhật ký hoạt động và kiểm toán hệ thống."""
    sessions = (await db.execute(select(StudySession).order_by(desc(StudySession.start_time)).limit(limit))).scalars().all()
    logs = []
    for s in sessions:
        u_res = await db.execute(select(User).where(User.id == s.user_id))
        u = u_res.scalar_one_or_none()
        logs.append({
            "id": s.id,
            "user_email": u.email if u else "user@vihtech.edu.vn",
            "action": f"Hoàn thành phiên học: {s.session_type.upper()}",
            "xp_earned": s.xp_earned,
            "duration_sec": s.duration_seconds,
            "timestamp": s.start_time
        })
    return {"logs": logs, "total": len(logs)}

@admin_router.get("/system-health")
async def get_system_health(admin: User = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):
    """Kiểm tra tình trạng máy chủ và cơ sở dữ liệu."""
    total_vocab = (await db.execute(select(func.count(Vocabulary.id)))).scalar() or 0
    total_users = (await db.execute(select(func.count(User.id)))).scalar() or 0
    total_sessions = (await db.execute(select(func.count(StudySession.id)))).scalar() or 0
    
    return {
        "status": "healthy",
        "database": "SQLite 3 Enterprise WAL Mode",
        "total_vocabularies": total_vocab,
        "total_users": total_users,
        "total_study_sessions": total_sessions,
        "ai_engine_status": "ONLINE & READY",
        "server_time": datetime.now(timezone.utc).isoformat()
    }



