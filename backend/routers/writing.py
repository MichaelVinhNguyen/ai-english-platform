from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.database import get_db
from backend.database.models import User, WritingSubmission, StudySession
from backend.database.schemas import WritingSubmit
from backend.services.ai_engine import ai_engine
from backend.services.gamification_service import gamification_service
from backend.routers.auth import get_current_user

writing_router = APIRouter(prefix="/api/writing", tags=["Writing"])

@writing_router.post("/submit")
async def submit_writing(
    data: WritingSubmit, current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    feedback = await ai_engine.evaluate_writing(data.content, data.writing_type, data.prompt)
    score = feedback.get("score", 6.5)
    xp = gamification_service.calculate_xp_reward("writing", score / 10)

    sub = WritingSubmission(
        user_id=current_user.id, writing_type=data.writing_type,
        prompt=data.prompt, content=data.content,
        word_count=len(data.content.split()),
        score=score,
        grammar_score=feedback.get("grammar_score", score),
        vocabulary_score=feedback.get("vocabulary_score", score),
        coherence_score=feedback.get("coherence_score", score),
        feedback=feedback.get("feedback", ""),
        grammar_errors=feedback.get("grammar_errors", []),
        suggestions=feedback.get("suggestions", []),
    )
    db.add(sub)
    session = StudySession(user_id=current_user.id, session_type="writing",
                            skill="writing", score=score, xp_earned=xp)
    db.add(session)
    current_user.xp += xp
    await db.commit()
    return {**feedback, "xp_earned": xp, "submission_id": sub.id}

@writing_router.get("/history")
async def writing_history(
    limit: int = 10, current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    r = await db.execute(
        select(WritingSubmission)
        .where(WritingSubmission.user_id == current_user.id)
        .order_by(desc(WritingSubmission.submitted_at)).limit(limit)
    )
    subs = r.scalars().all()
    return [{"id": s.id, "writing_type": s.writing_type, "word_count": s.word_count,
             "score": s.score, "submitted_at": s.submitted_at} for s in subs]

@writing_router.get("/prompts")
async def writing_prompts(writing_type: str = "essay",
                           current_user: User = Depends(get_current_user)):
    prompts_map = {
        "essay": ["Describe the advantages and disadvantages of social media.",
                  "Is technology making us more or less social?",
                  "The importance of learning English in today's world."],
        "email": ["Write a formal email to apply for a job.",
                  "Write an email to your professor asking for extension.",
                  "Write a complaint email to a company."],
        "cv": ["Write a professional summary for a software engineer.",
               "Write a CV objective for a marketing position."],
        "story": ["Write a short story about a surprising discovery.",
                  "Describe your most memorable travel experience."],
    }
    return {"prompts": prompts_map.get(writing_type, prompts_map["essay"])}
