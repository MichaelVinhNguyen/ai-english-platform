from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from backend.database.database import get_db
from backend.database.models import User, StudySession
from backend.services.ai_engine import ai_engine
from backend.services.gamification_service import gamification_service
from backend.routers.auth import get_current_user

speaking_router  = APIRouter(prefix="/api/speaking", tags=["Speaking"])

class SpeakingEval(BaseModel):
    transcript: str
    target_text: Optional[str] = None
    topic: Optional[str] = None

@speaking_router.post("/evaluate")
async def evaluate_speaking(data: SpeakingEval, current_user: User = Depends(get_current_user),
                             db: AsyncSession = Depends(get_db)):
    result = await ai_engine.evaluate_pronunciation(data.transcript, data.target_text)
    xp = gamification_service.calculate_xp_reward("speaking", result.get("overall_score", 70) / 100)
    current_user.xp += xp
    session = StudySession(user_id=current_user.id, session_type="speaking", skill="speaking",
                            score=result.get("overall_score", 70), xp_earned=xp)
    db.add(session)
    await db.commit()
    return {**result, "xp_earned": xp}

@speaking_router.get("/topics")
async def speaking_topics(level: str = "B1", current_user: User = Depends(get_current_user)):
    topics = {
        "A1": ["Giới thiệu bản thân", "Gia đình", "Màu sắc và số đếm"],
        "A2": ["Sở thích", "Du lịch", "Mô tả hình ảnh"],
        "B1": ["Công việc và nghề nghiệp", "Vấn đề môi trường", "Công nghệ"],
        "B2": ["Tranh luận xã hội", "Kinh doanh", "Văn hóa toàn cầu"],
        "C1": ["Triết học", "Chính sách kinh tế", "Đạo đức AI"],
        "C2": ["Academic debate", "Global politics", "Scientific discovery"],
    }
    return {"level": level, "topics": topics.get(level, topics["B1"])}


@speaking_router.get("/scenarios")
async def speaking_scenarios(current_user: User = Depends(get_current_user)):
    """Trả về danh sách 10 kịch bản Speaking Room chuẩn thương mại."""
    scenarios = [
        {"id": "daily", "title": "Daily Conversation", "icon": "💬", "ai_role": "Friend", "user_role": "Learner", "prompt": "How was your day? Tell me about your recent activities!"},
        {"id": "restaurant", "title": "Restaurant Ordering", "icon": "🍽️", "ai_role": "Waiter", "user_role": "Customer", "prompt": "Welcome to Bistro AI! Are you ready to order?"},
        {"id": "hotel", "title": "Hotel Reception", "icon": "🏨", "ai_role": "Receptionist", "user_role": "Guest", "prompt": "Good afternoon! Welcome to Grand Palace Hotel. How may I assist you?"},
        {"id": "airport", "title": "Airport Check-in", "icon": "✈️", "ai_role": "Airport Staff", "user_role": "Passenger", "prompt": "Passport and ticket, please! Where are you flying today?"},
        {"id": "interview", "title": "Job Interview", "icon": "💼", "ai_role": "Interviewer", "user_role": "Candidate", "prompt": "Thank you for joining us today. Please introduce yourself and your background."},
        {"id": "business", "title": "Business Meeting", "icon": "🏢", "ai_role": "Manager", "user_role": "Employee", "prompt": "Let's review our quarterly goals. What are your main accomplishments?"},
        {"id": "doctor", "title": "Medical Consultation", "icon": "🩺", "ai_role": "Doctor", "user_role": "Patient", "prompt": "Hello! How have you been feeling lately? What symptoms are you experiencing?"},
        {"id": "dating", "title": "Dating & Social", "icon": "💑", "ai_role": "Conversation Partner", "user_role": "Friend", "prompt": "It's so nice meeting you! What do you like to do in your free time?"},
        {"id": "presentation", "title": "Presentation Stage", "icon": "🎤", "ai_role": "Audience Lead", "user_role": "Presenter", "prompt": "The stage is yours! Please begin your presentation on your selected topic."},
        {"id": "debate", "title": "AI Debate Room", "icon": "⚔️", "ai_role": "Debate Opponent", "user_role": "Debater", "prompt": "I believe artificial intelligence will replace human jobs. What is your stance?"}
    ]
    return {"scenarios": scenarios}


class RealtimeTurnRequest(BaseModel):
    transcript: str
    scenario_id: Optional[str] = "daily"
    user_level: Optional[str] = "B1"


@speaking_router.post("/realtime-turn")
async def realtime_speaking_turn(
    data: RealtimeTurnRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Xử lý lượt nói realtime trong AI Speaking Room, trả về điểm, biểu cảm 3D Avatar, và phản hồi AI."""
    eval_res = await ai_engine.evaluate_pronunciation(data.transcript)
    
    # Generate conversational AI reply
    system_prompt = f"You are a friendly English teacher avatar in scenario '{data.scenario_id}' for level {data.user_level}. Respond naturally in English, provide a short Vietnamese translation and brief grammar correction if needed, then ask a follow-up question."
    ai_reply = await ai_engine.chat(
        message=f"Learner said: \"{data.transcript}\"",
        mode="roleplay",
        user_level=data.user_level
    )

    # Determine 3D Avatar emotion/gesture based on performance & tone
    pron_score = eval_res.get("pronunciation_score", 85)
    gram_score = eval_res.get("grammar_score", 80)
    
    if pron_score >= 85 and gram_score >= 80:
        emotion = "smile"
        gesture = "nod"
    elif gram_score < 70:
        emotion = "thinking"
        gesture = "head_tilt"
    else:
        emotion = "nod"
        gesture = "open_hands"

    xp = gamification_service.calculate_xp_reward("speaking", (pron_score + gram_score) / 200)
    current_user.xp += xp
    await db.commit()

    reply_text = ai_reply.get("content") or ai_reply.get("response") or ai_reply.get("text") or "That's wonderful! Keep practicing everyday."

    return {
        "user_transcript": data.transcript,
        "ai_response": reply_text,
        "response_en": reply_text,
        "emotion": emotion,
        "gesture": gesture,
        "scores": {
            "pronunciation": pron_score,
            "grammar": gram_score,
            "fluency": eval_res.get("fluency_score", 82),
            "vocabulary": eval_res.get("vocabulary_score", 85),
            "overall": eval_res.get("overall_score", 84)
        },
        "corrections": eval_res.get("corrections", []),

        "xp_earned": xp
    }


@speaking_router.post("/generate-practice")
async def generate_speaking_practice(
    topic: str,
    level: str = "B1",
    current_user: User = Depends(get_current_user)
):
    """Tạo kịch bản luyện nói AI (Roleplay)."""
    return await ai_engine.generate_speaking_practice(topic, level)

