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
        "A1": [
            "Giới thiệu bản thân & Nghề nghiệp", "Gia đình & Người thân", "Màu sắc, Trang phục & Số đếm",
            "Món ăn & Đồ uống yêu thích", "Hoạt động sinh hoạt buổi sáng", "Thời tiết & Các mùa trong năm"
        ],
        "A2": [
            "Sở thích & Hoạt động giải trí cuối tuần", "Kỳ nghỉ du lịch đáng nhớ", "Miêu tả hình ảnh & Không gian sống",
            "Hỏi và chỉ đường trong thành phố", "Mua sắm quần áo tại trung tâm thương mại", "Đặt phòng khách sạn & Gọi món ăn"
        ],
        "B1": [
            "Phỏng vấn xin việc: Điểm mạnh & Điểm yếu", "Vấn đề bảo vệ môi trường & Rác thải nhựa", "Ảnh hưởng của mạng xã hội đối với giới trẻ",
            "Thuyết trình dự án công việc trước đồng nghiệp", "Kế hoạch phát triển sự nghiệp 5 năm tới", "Lợi ích của việc đọc sách mỗi ngày"
        ],
        "B2": [
            "Tranh luận: Trí tuệ nhân tạo (AI) có thay thế con người?", "Văn hóa làm việc từ xa (Remote Work) vs Trực tiếp", "Toàn cầu hóa kinh tế và giữ gìn bản sắc dân tộc",
            "Đạo đức trong công nghệ sinh học và chỉnh sửa gen", "Chiến lược marketing & Thu hút khách hàng Gen Z", "Khủng hoảng năng lượng & Chuyển đổi xanh"
        ],
        "C1": [
            "Triết học nhận thức luận & Trực giác con người", "Chính sách tiền tệ vĩ mô & Lạm phát toàn cầu", "Đạo đức thuật toán & Trách nhiệm xã hội của Big Tech",
            "Kiến trúc đô thị bền vững & Thành phố thông minh", "Nghiên cứu khoa học thần kinh & Tính dẻo não bộ", "Địa chính trị chuỗi cung ứng khoáng sản đất hiếm"
        ],
        "C2": [
            "Academic Oxford Debate: Universal Basic Income", "Theoretical Limits of Artificial General Intelligence", "Epistemological Synthesis in Modern Critical Theory",
            "Quantum Information Theory & Cyber Warfare", "International Maritime Sovereignty Under UNCLOS", "Astrobiology & Extraterrestrial Biosignatures"
        ],
    }
    return {"level": level, "topics": topics.get(level, topics["B1"])}


@speaking_router.get("/scenarios")
async def speaking_scenarios(current_user: User = Depends(get_current_user)):
    """Trả về danh sách 30+ kịch bản Speaking Room chuẩn thương mại quốc tế."""
    scenarios = [
        {"id": "daily", "title": "1. Daily Conversation", "icon": "💬", "ai_role": "Friend", "user_role": "Learner", "prompt": "How was your day? Tell me about your recent activities!"},
        {"id": "restaurant", "title": "2. Restaurant Ordering", "icon": "🍽️", "ai_role": "Waiter", "user_role": "Customer", "prompt": "Welcome to Bistro AI! Are you ready to order?"},
        {"id": "hotel", "title": "3. Hotel Reception", "icon": "🏨", "ai_role": "Receptionist", "user_role": "Guest", "prompt": "Good afternoon! Welcome to Grand Palace Hotel. How may I assist you?"},
        {"id": "airport", "title": "4. Airport Check-in", "icon": "✈️", "ai_role": "Airport Staff", "user_role": "Passenger", "prompt": "Passport and ticket, please! Where are you flying today?"},
        {"id": "interview", "title": "5. Job Interview", "icon": "💼", "ai_role": "Interviewer", "user_role": "Candidate", "prompt": "Thank you for joining us today. Please introduce yourself and your background."},
        {"id": "business", "title": "6. Business Meeting", "icon": "🏢", "ai_role": "Manager", "user_role": "Employee", "prompt": "Let's review our quarterly goals. What are your main accomplishments?"},
        {"id": "doctor", "title": "7. Medical Consultation", "icon": "🩺", "ai_role": "Doctor", "user_role": "Patient", "prompt": "Hello! How have you been feeling lately? What symptoms are you experiencing?"},
        {"id": "shopping", "title": "8. Fashion Boutique Shopping", "icon": "🛍️", "ai_role": "Shop Assistant", "user_role": "Customer", "prompt": "Hello! Are you looking for any specific outfit or style today?"},
        {"id": "bank", "title": "9. Bank Account & Finance", "icon": "🏦", "ai_role": "Bank Teller", "user_role": "Customer", "prompt": "Welcome to Global Trust Bank. How can I help with your account today?"},
        {"id": "tech_support", "title": "10. Tech Support Hotline", "icon": "💻", "ai_role": "IT Support Specialist", "user_role": "Client", "prompt": "Tech Support here! What technical issue are you facing on your laptop?"},
        {"id": "dating", "title": "11. Dating & Social Rendezvous", "icon": "💑", "ai_role": "Conversation Partner", "user_role": "Friend", "prompt": "It's so nice meeting you! What do you like to do in your free time?"},
        {"id": "presentation", "title": "12. Presentation Stage", "icon": "🎤", "ai_role": "Audience Lead", "user_role": "Presenter", "prompt": "The stage is yours! Please begin your presentation on your selected topic."},
        {"id": "debate", "title": "13. AI Debate Room", "icon": "⚔️", "ai_role": "Debate Opponent", "user_role": "Debater", "prompt": "I believe artificial intelligence will replace human jobs. What is your stance?"},
        {"id": "ielts_part1", "title": "14. IELTS Speaking Part 1", "icon": "🎯", "ai_role": "IELTS Examiner", "user_role": "Candidate", "prompt": "Good morning. Can you tell me about your hometown and what you like about it?"},
        {"id": "ielts_part2", "title": "15. IELTS Speaking Part 2 Cue Card", "icon": "📋", "ai_role": "IELTS Examiner", "user_role": "Candidate", "prompt": "Describe an unforgettable journey you made. You have 1 minute to prepare and 2 minutes to speak."},
        {"id": "ielts_part3", "title": "16. IELTS Speaking Part 3 Discussion", "icon": "🧠", "ai_role": "IELTS Examiner", "user_role": "Candidate", "prompt": "How has modern tourism affected local cultures and the environment?"},
        {"id": "apartment_rental", "title": "17. Apartment Rental Inquiry", "icon": "🔑", "ai_role": "Real Estate Agent", "user_role": "Tenant", "prompt": "Hello! Are you interested in the two-bedroom apartment near downtown?"},
        {"id": "car_rental", "title": "18. Car Rental Service", "icon": "🚗", "ai_role": "Rental Agent", "user_role": "Driver", "prompt": "Welcome to DriveFast Rentals! What type of vehicle would you like to hire?"},
        {"id": "gym_trainer", "title": "19. Fitness Coaching Session", "icon": "🏋️", "ai_role": "Personal Trainer", "user_role": "Gym Member", "prompt": "Ready for your workout? Let's discuss your fitness goals and current diet plan."},
        {"id": "university_admissions", "title": "20. University Admissions Interview", "icon": "🎓", "ai_role": "Admissions Officer", "user_role": "Applicant", "prompt": "Welcome! Why did you choose our university and this specific major?"},
        {"id": "coffee_chat", "title": "21. Coffee Shop Networking", "icon": "☕", "ai_role": "Tech Founder", "user_role": "Developer", "prompt": "Hi! Great to meet you at the tech meetup. What projects are you working on?"},
        {"id": "negotiation", "title": "22. Business Contract Negotiation", "icon": "🤝", "ai_role": "Supplier Representative", "user_role": "Procurement Manager", "prompt": "Let's discuss the unit pricing and delivery terms for the annual contract."},
        {"id": "customer_complaint", "title": "23. Customer Complaint Handling", "icon": "⚠️", "ai_role": "Customer Service Manager", "user_role": "Unhappy Customer", "prompt": "I understand you had a problem with our delivery. Please tell me what happened."},
        {"id": "travel_guide", "title": "24. Museum Tour Guide", "icon": "🏛️", "ai_role": "Tour Guide", "user_role": "Tourist", "prompt": "Welcome to the National Art Gallery! Which historical period would you like to explore first?"},
        {"id": "startup_pitch", "title": "25. Startup Pitch to Investors", "icon": "🚀", "ai_role": "Venture Capitalist", "user_role": "Founder", "prompt": "You have 3 minutes to pitch your AI startup idea. What problem are you solving?"},
        {"id": "pharmacy", "title": "26. Pharmacy Medication Advice", "icon": "💊", "ai_role": "Pharmacist", "user_role": "Customer", "prompt": "Hello! How can I help you with your prescription or symptoms today?"},
        {"id": "police_report", "title": "27. Reporting Lost Item to Police", "icon": "👮", "ai_role": "Police Officer", "user_role": "Citizen", "prompt": "Good day. Please describe the item you lost and where you last saw it."},
        {"id": "library", "title": "28. University Library Research", "icon": "📚", "ai_role": "Librarian", "user_role": "Student", "prompt": "Can I help you locate any academic journals or reference books today?"},
        {"id": "customs_border", "title": "29. Border Customs Control", "icon": "🛂", "ai_role": "Customs Officer", "user_role": "Traveler", "prompt": "What is the purpose of your visit to our country, and how long do you intend to stay?"},
        {"id": "podcast_interview", "title": "30. Live Podcast Guest Interview", "icon": "🎙️", "ai_role": "Podcast Host", "user_role": "Guest Expert", "prompt": "Welcome to the show! Tell our global audience about your journey into English mastery."}
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

