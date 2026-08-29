from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from backend.database.database import get_db
from backend.database.models import User
from backend.routers.auth import get_current_user

listening_router = APIRouter(prefix="/api/listening", tags=["Listening"])

class DictationCheckRequest(BaseModel):
    original: str
    user_input: str

@listening_router.get("/exercises")
async def get_exercises(level: Optional[str] = None, db: AsyncSession = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    from backend.database.models import ListeningExercise
    q = select(ListeningExercise)
    if level: q = q.where(ListeningExercise.level == level)
    r = await db.execute(q.limit(100))
    exercises = r.scalars().all()
    return [{"id": e.id, "title": e.title, "description": e.description,
             "exercise_type": e.exercise_type, "level": e.level,
             "audio_url": e.audio_url, "duration_sec": e.duration_sec,
             "transcript": e.transcript, "questions": e.questions} for e in exercises]

@listening_router.post("/check-dictation")
async def check_dictation(data: DictationCheckRequest,
                            current_user: User = Depends(get_current_user)):
    """Check dictation exercise."""
    orig_words = data.original.lower().split()
    user_words = data.user_input.lower().split()
    correct = sum(1 for o, u in zip(orig_words, user_words) if o == u)
    total = max(len(orig_words), len(user_words))
    score = correct / total * 10 if total > 0 else 0
    return {"score": round(score, 1), "correct_words": correct, "total_words": total,
            "original": data.original, "user_input": data.user_input,
            "feedback": "Xuất sắc!" if score >= 9 else "Tốt lắm!" if score >= 7 else "Cần luyện thêm!"}


@listening_router.post("/generate-exercise")
async def generate_listening_exercise(
    topic: str,
    level: str = "B1",
    current_user: User = Depends(get_current_user)
):
    """AI tạo bài luyện nghe."""
    from backend.services.ai_engine import ai_engine
    return await ai_engine.generate_listening_exercise(topic, level)
