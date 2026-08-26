from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.database import get_db
from backend.database.models import User, Badge, UserBadge, Mission
from backend.routers.auth import get_current_user

gamification_router = APIRouter(prefix="/api/gamification", tags=["Gamification"])

@gamification_router.get("/badges")
async def get_badges(db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    r = await db.execute(select(Badge))
    all_badges = r.scalars().all()
    r2 = await db.execute(
        select(UserBadge.badge_id).where(UserBadge.user_id == current_user.id)
    )
    earned_ids = {row[0] for row in r2.all()}
    return [{
        "id": b.id, "name": b.name, "description": b.description,
        "icon": b.icon, "category": b.category, "xp_reward": b.xp_reward,
        "coin_reward": b.coin_reward, "earned": b.id in earned_ids,
    } for b in all_badges]

@gamification_router.get("/my-badges")
async def my_badges(current_user: User = Depends(get_current_user),
                     db: AsyncSession = Depends(get_db)):
    r = await db.execute(
        select(UserBadge, Badge).join(Badge)
        .where(UserBadge.user_id == current_user.id)
    )
    rows = r.all()
    return [{"badge_id": b.id, "name": b.name, "icon": b.icon,
             "description": b.description, "earned_at": ub.earned_at} for ub, b in rows]

@gamification_router.get("/missions")
async def get_missions(current_user: User = Depends(get_current_user),
                        db: AsyncSession = Depends(get_db)):
    r = await db.execute(select(Mission).where(Mission.is_active == True))
    missions = r.scalars().all()
    return [{"id": m.id, "title": m.title, "description": m.description,
             "mission_type": m.mission_type, "xp_reward": m.xp_reward,
             "coin_reward": m.coin_reward} for m in missions]
