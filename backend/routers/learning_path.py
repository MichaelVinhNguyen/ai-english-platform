from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from backend.database.database import get_db
from backend.database.models import User, LearningPath
from backend.routers.auth import get_current_user
from backend.services.ai_engine import ai_engine

router = APIRouter(prefix="/api/learning-path", tags=["Learning Path"])

class GeneratePathRequest(BaseModel):
    current_level: str
    target_level: str
    purpose: str
    daily_minutes: int
    strengths: Optional[str] = None
    weaknesses: Optional[str] = None

class PathResponse(BaseModel):
    id: int
    current_level: str
    target_level: str
    purpose: str
    daily_minutes: int
    weeks_total: int
    current_week: int
    path_data: Dict[str, Any]
    progress_data: Dict[str, Any]

@router.post("/generate")
async def generate_learning_path(
    req: GeneratePathRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """AI tạo lộ trình cá nhân hóa dựa trên CEFR."""
    # Deactivate old paths
    await db.execute(
        select(LearningPath).where(LearningPath.user_id == current_user.id)
    )
    # Simple direct update for brevity in SQLite, or just insert new and mark others inactive
    # Actually, let's just fetch all and mark them inactive
    old_paths_result = await db.execute(
        select(LearningPath).where(LearningPath.user_id == current_user.id, LearningPath.is_active == True)
    )
    for old_path in old_paths_result.scalars():
        old_path.is_active = False

    # Call AI Engine to generate path
    user_data = {
        "level": req.current_level,
        "target_level": req.target_level,
        "purpose": req.purpose,
        "daily_minutes": req.daily_minutes,
        "strengths": req.strengths,
        "weaknesses": req.weaknesses
    }
    
    # We will use the existing recommend_learning_path or a new one, let's assume recommend_learning_path returns the structured data we need
    ai_response = await ai_engine.recommend_learning_path(user_data)
    
    weeks_total = ai_response.get("estimated_weeks", 12)
    path_data = ai_response
    progress_data = {"completed_weeks": []}

    new_path = LearningPath(
        user_id=current_user.id,
        current_level=req.current_level,
        target_level=req.target_level,
        purpose=req.purpose,
        daily_minutes=req.daily_minutes,
        strengths=req.strengths,
        weaknesses=req.weaknesses,
        path_data=path_data,
        progress_data=progress_data,
        weeks_total=weeks_total,
        current_week=1,
        is_active=True
    )
    db.add(new_path)
    
    # Update user's target level in User model
    current_user.target_level = req.target_level
    current_user.level = int(req.current_level[-1]) if req.current_level[-1].isdigit() else 1 # basic approximation
    
    await db.commit()
    await db.refresh(new_path)

    return new_path


@router.get("/my-path", response_model=Optional[PathResponse])
async def get_my_path(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Lấy lộ trình học hiện tại của user."""
    result = await db.execute(
        select(LearningPath)
        .where(LearningPath.user_id == current_user.id, LearningPath.is_active == True)
        .order_by(desc(LearningPath.created_at))
        .limit(1)
    )
    path = result.scalar_one_or_none()
    if not path:
        return None
    return path


@router.post("/update-progress")
async def update_progress(
    week_completed: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Cập nhật tiến độ học."""
    result = await db.execute(
        select(LearningPath)
        .where(LearningPath.user_id == current_user.id, LearningPath.is_active == True)
    )
    path = result.scalar_one_or_none()
    if not path:
        raise HTTPException(status_code=404, detail="No active learning path found.")

    progress = path.progress_data or {"completed_weeks": []}
    completed_weeks = progress.get("completed_weeks", [])
    
    if week_completed not in completed_weeks:
        completed_weeks.append(week_completed)
        progress["completed_weeks"] = completed_weeks
        path.progress_data = progress
        
        # Move to next week if possible
        if path.current_week == week_completed and path.current_week < path.weeks_total:
            path.current_week += 1

        await db.commit()
    
    return {"status": "success", "current_week": path.current_week, "progress": path.progress_data}


@router.get("/cefr-info")
async def get_cefr_info():
    """Lấy thông tin chi tiết các cấp CEFR."""
    return {
        "A1": "Beginner - Có thể hiểu và sử dụng các biểu thức cơ bản hàng ngày.",
        "A2": "Elementary - Có thể giao tiếp trong các tình huống đơn giản, thường xuyên.",
        "B1": "Intermediate - Có thể xử lý hầu hết các tình huống khi đi du lịch, viết văn bản đơn giản.",
        "B2": "Upper Intermediate - Có thể hiểu ý chính của văn bản phức tạp, giao tiếp trôi chảy.",
        "C1": "Advanced - Có thể hiểu nhiều loại văn bản dài và yêu cầu cao, giao tiếp linh hoạt.",
        "C2": "Proficient - Có thể hiểu hầu như mọi thứ nghe hoặc đọc được, tóm tắt và trình bày lại trôi chảy."
    }
