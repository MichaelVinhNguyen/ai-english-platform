"""
vocabulary.py – Vocabulary module: search, learn, AI explain
"""
from typing import Optional, List
from fastapi import APIRouter, Depends, Query
from sqlalchemy import select, func, or_
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from backend.database.database import get_db
from backend.database.models import User, Vocabulary, UserVocabulary
from backend.database.schemas import VocabOut, FlashcardReview
from backend.services.ai_engine import ai_engine
from backend.services.srs_engine import srs_engine
from backend.services.voice_engine import voice_engine
from backend.routers.auth import get_current_user
from pydantic import BaseModel

router = APIRouter(prefix="/api/vocabulary", tags=["Vocabulary"])


class VocabExplain(BaseModel):
    word: str
    context: Optional[str] = None


@router.get("/", response_model=List[VocabOut])
async def get_vocabulary(
    level: Optional[str] = Query(None),
    topic: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    letter: Optional[str] = Query(None),
    limit: int = Query(1000, le=2000),
    offset: int = 0,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Lấy danh sách từ vựng (hỗ trợ lọc A-Z và CEFR)."""
    q = select(Vocabulary)
    if level:   q = q.where(Vocabulary.level == level)
    if topic:   q = q.where(Vocabulary.topic == topic)
    if letter:  q = q.where(Vocabulary.word.ilike(f"{letter}%"))
    if search:  q = q.where(or_(
        Vocabulary.word.ilike(f"%{search}%"),
        Vocabulary.definition_vi.ilike(f"%{search}%")
    ))
    q = q.order_by(Vocabulary.word.asc()).offset(offset).limit(limit)
    r = await db.execute(q)
    return [VocabOut.model_validate(v) for v in r.scalars()]


@router.post("/explain")
async def explain_word(req: VocabExplain, current_user: User = Depends(get_current_user)):
    """AI giải thích từ vựng chi tiết."""
    result = await ai_engine.explain_vocabulary(req.word, req.context)
    return result


@router.post("/add-to-my-list/{vocab_id}")
async def add_to_my_list(
    vocab_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Thêm từ vào danh sách học cá nhân."""
    # Check exists
    r = await db.execute(
        select(UserVocabulary).where(
            UserVocabulary.user_id == current_user.id,
            UserVocabulary.vocab_id == vocab_id
        )
    )
    if r.scalar_one_or_none():
        return {"message": "Từ đã có trong danh sách"}

    uv = UserVocabulary(user_id=current_user.id, vocab_id=vocab_id)
    db.add(uv)
    await db.commit()
    return {"message": "Đã thêm vào danh sách học", "vocab_id": vocab_id}


@router.get("/my-list")
async def my_vocabulary_list(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Danh sách từ vựng của tôi."""
    r = await db.execute(
        select(UserVocabulary, Vocabulary)
        .join(Vocabulary)
        .where(UserVocabulary.user_id == current_user.id)
        .order_by(UserVocabulary.added_at.desc())
    )
    rows = r.all()
    return [{
        "vocab_id": uv.id, "word": v.word, "ipa": v.ipa,
        "definition_vi": v.definition_vi, "definition_en": v.definition_en,
        "level": v.level, "ease_factor": uv.ease_factor,
        "interval_days": uv.interval_days, "due_date": uv.due_date,
        "is_learned": uv.is_learned, "review_count": uv.review_count,
    } for uv, v in rows]


@router.get("/flashcards/due")
async def get_due_flashcards(
    limit: int = 20,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Lấy flashcards cần ôn tập hôm nay."""
    now = datetime.now(timezone.utc)
    r = await db.execute(
        select(UserVocabulary, Vocabulary)
        .join(Vocabulary)
        .where(
            UserVocabulary.user_id == current_user.id,
            UserVocabulary.due_date <= now
        )
        .order_by(UserVocabulary.due_date)
        .limit(limit)
    )
    rows = r.all()
    return [{
        "vocab_id": v.id, "user_vocab_id": uv.id,
        "word": v.word, "ipa": v.ipa,
        "definition_vi": v.definition_vi, "definition_en": v.definition_en,
        "examples": v.examples, "synonyms": v.synonyms,
        "ease_factor": uv.ease_factor, "interval_days": uv.interval_days,
    } for uv, v in rows]


@router.get("/flashcards/deck")
async def get_flashcard_deck(
    letter: Optional[str] = Query(None),
    level: Optional[str] = Query(None),
    topic: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    limit: int = Query(50, le=200),
    shuffle: bool = Query(True),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Lấy bộ flashcards thông minh trực tiếp từ kho 25,215 từ vựng (hỗ trợ lọc A-Z, CEFR, Topic)."""
    q = select(Vocabulary)
    if letter:
        q = q.where(Vocabulary.word.ilike(f"{letter}%"))
    if level:
        q = q.where(Vocabulary.level == level)
    if topic:
        q = q.where(Vocabulary.topic == topic)
    if search:
        q = q.where(or_(
            Vocabulary.word.ilike(f"%{search}%"),
            Vocabulary.definition_vi.ilike(f"%{search}%")
        ))
    if shuffle:
        from sqlalchemy.sql.expression import func
        q = q.order_by(func.random())
    else:
        q = q.order_by(Vocabulary.word.asc())
    
    r = await db.execute(q.limit(limit))
    vocab_items = r.scalars().all()
    
    # Get user study stats for these words
    vocab_ids = [v.id for v in vocab_items]
    user_map = {}
    if vocab_ids:
        ur = await db.execute(
            select(UserVocabulary).where(
                UserVocabulary.user_id == current_user.id,
                UserVocabulary.vocab_id.in_(vocab_ids)
            )
        )
        for uv in ur.scalars():
            user_map[uv.vocab_id] = uv
            
    cards = []
    for v in vocab_items:
        uv = user_map.get(v.id)
        cards.append({
            "vocab_id": v.id,
            "word": v.word,
            "ipa": v.ipa,
            "word_type": v.word_type,
            "level": v.level,
            "topic": v.topic,
            "definition_vi": v.definition_vi,
            "definition_en": v.definition_en,
            "examples": v.examples or [],
            "synonyms": v.synonyms or [],
            "antonyms": v.antonyms or [],
            "collocations": v.collocations or [],
            "image_url": v.image_url,
            "audio_url": v.audio_url,
            "ease_factor": uv.ease_factor if uv else 2.5,
            "interval_days": uv.interval_days if uv else 1,
            "review_count": uv.review_count if uv else 0,
            "is_learned": uv.is_learned if uv else False,
            "due_date": uv.due_date.isoformat() if uv and uv.due_date else None
        })
    return {"cards": cards, "total": len(cards)}


@router.post("/flashcards/review")
async def review_flashcard(
    data: FlashcardReview,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Đánh giá flashcard (Anki SRS SuperMemo-2)."""
    r = await db.execute(
        select(UserVocabulary).where(
            UserVocabulary.user_id == current_user.id,
            UserVocabulary.vocab_id == data.vocab_id
        )
    )
    uv = r.scalar_one_or_none()
    if not uv:
        # Create UserVocabulary if not exists
        uv = UserVocabulary(
            user_id=current_user.id,
            vocab_id=data.vocab_id,
            ease_factor=2.5,
            interval_days=1,
            repetitions=0,
            due_date=datetime.now(timezone.utc),
            created_at=datetime.now(timezone.utc)
        )
        db.add(uv)
        await db.flush()

    # Apply SM-2
    result = srs_engine.calculate_next_review(
        uv.ease_factor, uv.interval_days, uv.repetitions, data.quality
    )
    uv.ease_factor   = result["ease_factor"]
    uv.interval_days = result["interval_days"]
    uv.repetitions   = result["repetitions"]
    uv.due_date      = result["due_date"]
    uv.review_count  += 1
    if data.quality >= 3:
        uv.correct_count += 1
    if uv.review_count >= 5 and uv.correct_count / uv.review_count >= 0.8:
        uv.is_learned = True
    uv.last_reviewed = datetime.now(timezone.utc)

    # XP reward
    xp = 5 if data.quality >= 3 else 0
    current_user.xp += xp

    await db.commit()
    return {
        "message": "Đã cập nhật tiến độ",
        "next_review": result["due_date"],
        "interval_days": result["interval_days"],
        "xp_earned": xp,
        "is_learned": uv.is_learned,
    }


TOPICS_METADATA_MAP = {
    "Daily Life & Routines": {"icon": "☕", "color": "#f59e0b", "category": "General Life", "desc": "Thói quen hàng ngày, sinh hoạt và nhịp sống đô thị"},
    "Food, Cooking & Dining": {"icon": "🍳", "color": "#ef4444", "category": "Lifestyle", "desc": "Nghệ thuật ẩm thực, kỹ thuật nấu ăn và trải nghiệm nhà hàng"},
    "Travel, Tourism & Transportation": {"icon": "✈️", "color": "#3b82f6", "category": "Travel", "desc": "Hành trình khám phá, thủ tục bay và các loại hình giao thông"},
    "Technology & Artificial Intelligence": {"icon": "🤖", "color": "#8b5cf6", "category": "Technology", "desc": "Công nghệ số, AI, an ninh mạng và kỷ nguyên thông minh"},
    "Business, Management & Workplace": {"icon": "💼", "color": "#0ea5e9", "category": "Business", "desc": "Kinh doanh, văn hóa công sở, quản trị và đàm phán"},
    "Finance, Banking & Investment": {"icon": "💳", "color": "#10b981", "category": "Finance", "desc": "Tài chính, ngân hàng, thị trường chứng khoán và đầu tư"},
    "Health, Medicine & Wellness": {"icon": "🩺", "color": "#ec4899", "category": "Health", "desc": "Y tế, sức khỏe thể chất, chế độ dinh dưỡng và phòng bệnh"},
    "Education & Academic Life": {"icon": "🎓", "color": "#6366f1", "category": "Academic", "desc": "Trường học, nghiên cứu học thuật, phương pháp học tập"},
    "Environment, Nature & Climate": {"icon": "🌱", "color": "#14b8a6", "category": "Science", "desc": "Hệ sinh thái, biến đổi khí hậu và phát triển bền vững"},
    "Shopping, Fashion & Retail": {"icon": "🛍️", "color": "#f43f5e", "category": "Lifestyle", "desc": "Thời trang, mua sắm bán lẻ, phong cách và xu hướng"},
    "Entertainment, Cinema & Arts": {"icon": "🎬", "color": "#a855f7", "category": "Entertainment", "desc": "Điện ảnh, âm nhạc, nghệ thuật thị giác và giải trí"},
    "Sports, Fitness & Outdoor Activities": {"icon": "⚽", "color": "#eab308", "category": "Sports", "desc": "Thể thao, rèn luyện thể lực và các hoạt động dã ngoại"},
    "Emotions, Personality & Character": {"icon": "🎭", "color": "#d946ef", "category": "Psychology", "desc": "Cảm xúc con người, phẩm chất tính cách và tâm lý"},
    "Family, Relationships & Society": {"icon": "👨‍👩‍👧‍👦", "color": "#f97316", "category": "Social", "desc": "Gia đình, tình bạn, quan hệ xã hội và cộng đồng"},
    "Media, News & Communication": {"icon": "📡", "color": "#06b6d4", "category": "Media", "desc": "Báo chí truyền thông, mạng xã hội và kênh thông tin"},
    "Law, Crime & Justice": {"icon": "⚖️", "color": "#64748b", "category": "Society", "desc": "Hệ thống luật pháp, tư pháp, quyền công dân và tội phạm"},
    "Politics, Diplomacy & Global Affairs": {"icon": "🏛️", "color": "#475569", "category": "Politics", "desc": "Chính trị, ngoại giao quốc tế và các hiệp ước toàn cầu"},
    "Science, Space & Astronomy": {"icon": "🔭", "color": "#4f46e5", "category": "Science", "desc": "Khoa học vũ trụ, thiên văn học và khám phá dải ngân hà"},
    "Architecture, Housing & Real Estate": {"icon": "🏢", "color": "#78716c", "category": "Industry", "desc": "Kiến trúc công trình, thị trường nhà ở và bất động sản"},
    "Job Interview & Career Development": {"icon": "🎯", "color": "#0284c7", "category": "Career", "desc": "Phỏng vấn xin việc, phát triển kỹ năng nghề và thăng tiến"},
    "Marketing, Advertising & Branding": {"icon": "📢", "color": "#f59e0b", "category": "Marketing", "desc": "Tiếp thị số, quảng cáo sáng tạo và định vị thương hiệu"},
    "Logistics, Supply Chain & E-commerce": {"icon": "📦", "color": "#ea580c", "category": "Business", "desc": "Chuỗi cung ứng, kho vận và sàn thương mại điện tử"},
    "Hospitality, Hotel & Customer Service": {"icon": "🛎️", "color": "#e11d48", "category": "Service", "desc": "Dịch vụ khách hàng, quản trị khách sạn và du lịch lưu trú"},
    "Culture, Traditions & Festivals": {"icon": "🏮", "color": "#b91c1c", "category": "Culture", "desc": "Di sản văn hóa, phong tục tập quán và lễ hội truyền thống"},
    "Hobbies, Leisure & Creative Skills": {"icon": "🎨", "color": "#9333ea", "category": "Leisure", "desc": "Sở thích cá nhân, sáng tạo nghệ thuật và kỹ năng thủ công"},
    "Weather, Seasons & Natural Disasters": {"icon": "⛈️", "color": "#0284c7", "category": "Nature", "desc": "Khí tượng thủy văn, bốn mùa và các hiện tượng thiên nhiên"},
    "Philosophy, Psychology & Mindfulness": {"icon": "🧘", "color": "#059669", "category": "Mind", "desc": "Triết học nhân sinh, sức khỏe tinh thần và chánh niệm"},
    "Animals, Wildlife & Marine Biology": {"icon": "🐬", "color": "#0284c7", "category": "Nature", "desc": "Động vật hoang dã, sinh vật biển và bảo tồn tự nhiên"},
    "Innovation, Startups & Entrepreneurship": {"icon": "🚀", "color": "#7c3aed", "category": "Business", "desc": "Tinh thần khởi nghiệp, gọi vốn và đổi mới đột phá"},
    "Idioms, Phrasal Verbs & Slang for Speaking": {"icon": "💬", "color": "#db2777", "category": "Communication", "desc": "Thành ngữ, cụm động từ tự nhiên và tiếng lóng bản xứ"}
}


@router.get("/topics")
async def get_topics(db: AsyncSession = Depends(get_db),
                     current_user: User = Depends(get_current_user)):
    """Lấy danh sách chủ đề từ vựng."""
    r = await db.execute(select(Vocabulary.topic).distinct().where(Vocabulary.topic != None))
    return {"topics": [row[0] for row in r.all() if row[0]]}


@router.get("/flashcard-topics-meta")
async def get_flashcard_topics_meta(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Lấy 30 chủ đề Flashcards kèm icon, tiến độ học, tổng từ và mô tả."""
    # Count words per topic
    topic_counts_q = await db.execute(
        select(Vocabulary.topic, func.count(Vocabulary.id))
        .where(Vocabulary.topic.isnot(None))
        .group_by(Vocabulary.topic)
    )
    topic_counts = dict(topic_counts_q.all())

    # Count learned words by user per topic
    learned_q = await db.execute(
        select(Vocabulary.topic, func.count(UserVocabulary.id))
        .join(Vocabulary, UserVocabulary.vocab_id == Vocabulary.id)
        .where(UserVocabulary.user_id == current_user.id, UserVocabulary.is_learned == True)
        .group_by(Vocabulary.topic)
    )
    learned_map = dict(learned_q.all())

    result = []
    # Loop over predefined 30 topics
    for topic_name, meta in TOPICS_METADATA_MAP.items():
        total_w = topic_counts.get(topic_name, 50)
        learned_w = learned_map.get(topic_name, 0)
        progress = round((learned_w / total_w * 100) if total_w > 0 else 0, 1)
        result.append({
            "name": topic_name,
            "icon": meta["icon"],
            "color": meta["color"],
            "category": meta["category"],
            "description": meta["desc"],
            "total_words": total_w,
            "learned_words": learned_w,
            "progress_percent": progress
        })

    return {"topics": result, "total_topics": len(result)}


@router.get("/stats")
async def vocab_stats(current_user: User = Depends(get_current_user),
                      db: AsyncSession = Depends(get_db)):
    now = datetime.now(timezone.utc)
    total = await db.execute(
        select(func.count()).where(UserVocabulary.user_id == current_user.id)
    )
    learned = await db.execute(
        select(func.count()).where(UserVocabulary.user_id == current_user.id,
                                   UserVocabulary.is_learned == True)
    )
    due = await db.execute(
        select(func.count()).where(UserVocabulary.user_id == current_user.id,
                                   UserVocabulary.due_date <= now)
    )
    return {
        "total": total.scalar(), "learned": learned.scalar(), "due_today": due.scalar()
    }
