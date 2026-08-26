"""
ai_teacher.py – AI Teacher: Chat, Voice, Roleplay, Pronunciation
"""
import uuid
from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.database import get_db
from backend.database.models import User, ChatHistory, StudySession
from backend.database.schemas import ChatMessage, ChatResponse
from backend.services.ai_engine import ai_engine
from backend.services.voice_engine import voice_engine
from backend.routers.auth import get_current_user
from backend.services.gamification_service import gamification_service
from datetime import datetime, timezone
from pydantic import BaseModel

router = APIRouter(prefix="/api/teacher", tags=["AI Teacher"])


class VoiceMessage(BaseModel):
    audio_base64: str
    mode: str = "speaking"
    session_id: Optional[str] = None
    target_text: Optional[str] = None

class TTSRequest(BaseModel):
    text: str
    language: str = "en"

class RoleplayStart(BaseModel):
    scenario: str
    difficulty: str = "intermediate"


@router.post("/chat", response_model=ChatResponse)
async def chat_with_teacher(
    msg: ChatMessage,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Chat với AI Teacher."""
    session_id = msg.session_id or str(uuid.uuid4())

    # Load chat history
    r = await db.execute(
        select(ChatHistory)
        .where(ChatHistory.user_id == current_user.id,
               ChatHistory.session_id == session_id)
        .order_by(ChatHistory.created_at)
        .limit(20)
    )
    history = [{"role": h.role, "content": h.content} for h in r.scalars()]

    # AI response
    result = await ai_engine.chat(
        message=msg.content,
        session_id=session_id,
        mode=msg.mode,
        user_level=current_user.target_level or "B1",
        history=history,
    )

    # Save to DB
    db.add(ChatHistory(user_id=current_user.id, session_id=session_id,
                        role="user", content=msg.content, mode=msg.mode))
    db.add(ChatHistory(user_id=current_user.id, session_id=session_id,
                        role="assistant", content=result["content"], mode=msg.mode))
    await db.commit()

    return ChatResponse(**result)


@router.post("/voice")
async def voice_chat(
    msg: VoiceMessage,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Voice input → STT → AI response → TTS."""
    # STT
    stt_result = await voice_engine.transcribe_base64(msg.audio_base64)
    transcript = stt_result.get("text", "")
    if not transcript:
        return {"error": "Không nhận được giọng nói", "transcript": ""}

    # Pronunciation evaluation if in speaking mode
    eval_result = None
    if msg.mode == "speaking":
        eval_result = await ai_engine.evaluate_pronunciation(transcript, msg.target_text)

    # AI response
    ai_result = await ai_engine.chat(
        message=transcript, mode=msg.mode,
        user_level=current_user.target_level or "B1",
    )

    # TTS for AI response
    audio_b64 = await voice_engine.synthesize_to_base64(ai_result["content"][:500])

    # Save session
    db.add(StudySession(user_id=current_user.id, session_type="speaking",
                         skill="speaking", xp_earned=15))
    await db.commit()

    return {
        "transcript": transcript,
        "ai_response": ai_result["content"],
        "audio_base64": audio_b64,
        "evaluation": eval_result,
        "session_id": ai_result.get("session_id"),
    }


@router.post("/tts")
async def text_to_speech(req: TTSRequest, current_user: User = Depends(get_current_user)):
    """Convert text to speech."""
    audio_b64 = await voice_engine.synthesize_to_base64(req.text, req.language)
    if not audio_b64:
        raise HTTPException(status_code=500, detail="Không thể tạo audio")
    return {"audio_base64": audio_b64, "text": req.text}


@router.get("/history")
async def get_chat_history(
    session_id: Optional[str] = None,
    limit: int = 50,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get chat history."""
    query = select(ChatHistory).where(ChatHistory.user_id == current_user.id)
    if session_id:
        query = query.where(ChatHistory.session_id == session_id)
    query = query.order_by(desc(ChatHistory.created_at)).limit(limit)
    r = await db.execute(query)
    messages = r.scalars().all()
    return [{"role": m.role, "content": m.content, "mode": m.mode,
             "created_at": m.created_at, "session_id": m.session_id}
            for m in reversed(messages)]


@router.get("/sessions")
async def get_sessions(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get unique chat sessions."""
    from sqlalchemy import distinct, func
    r = await db.execute(
        select(
            ChatHistory.session_id,
            func.max(ChatHistory.created_at).label("last_message"),
            func.count(ChatHistory.id).label("message_count"),
        )
        .where(ChatHistory.user_id == current_user.id)
        .group_by(ChatHistory.session_id)
        .order_by(desc("last_message"))
        .limit(20)
    )
    return [{"session_id": r.session_id, "last_message": r.last_message,
             "message_count": r.message_count} for r in r.all()]


@router.post("/roleplay")
async def start_roleplay(
    req: RoleplayStart,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Bắt đầu tình huống roleplay."""
    session_id = str(uuid.uuid4())
    scenarios = {
        "restaurant": "Hãy đóng vai nhân viên nhà hàng người nước ngoài. Khách hàng sẽ đặt bàn, gọi món.",
        "interview": "Hãy đóng vai người phỏng vấn. Đây là buổi phỏng vấn công việc tiếng Anh.",
        "travel": "Hãy đóng vai nhân viên sân bay. Hành khách cần hỗ trợ.",
        "shopping": "Hãy đóng vai người bán hàng ở cửa hàng thời trang.",
        "doctor": "Hãy đóng vai bác sĩ. Bệnh nhân sẽ mô tả triệu chứng.",
    }
    prompt = scenarios.get(req.scenario, f"Tình huống: {req.scenario}")
    result = await ai_engine.chat(
        message=f"Bắt đầu roleplay. {prompt}",
        session_id=session_id, mode="roleplay",
        user_level=current_user.target_level or "B1",
    )
    return {"session_id": session_id, "scenario": req.scenario,
            "opening": result["content"]}
