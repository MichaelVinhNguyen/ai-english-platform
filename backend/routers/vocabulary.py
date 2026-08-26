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


@router.get("", response_model=List[VocabOut])
@router.get("/", response_model=List[VocabOut])
async def get_vocabulary(
    level: Optional[str] = Query(None),
    topic: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    letter: Optional[str] = Query(None),
    limit: int = Query(300, le=500),
    offset: int = 0,
    db: AsyncSession = Depends(get_db)
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
    results = [VocabOut.model_validate(v) for v in r.scalars()]
    return results


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


@router.post("/flashcards/review")
async def review_flashcard(
    data: FlashcardReview,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Đánh giá flashcard (Anki SRS)."""
    r = await db.execute(
        select(UserVocabulary).where(
            UserVocabulary.user_id == current_user.id,
            UserVocabulary.vocab_id == data.vocab_id
        )
    )
    uv = r.scalar_one_or_none()
    if not uv:
        return {"error": "Từ không có trong danh sách"}

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


@router.get("/topics")
async def get_topics(db: AsyncSession = Depends(get_db)):
    """Lấy danh sách chủ đề từ vựng."""
    try:
        r = await db.execute(select(Vocabulary.topic).distinct().where(Vocabulary.topic != None))
        topics = [row[0] for row in r.all() if row[0]]
        if not topics:
            topics = ["Daily Life", "Travel", "Business", "Technology", "Food & Drink", "Education", "Health", "Environment"]
        return {"topics": topics}
    except Exception:
        return {"topics": ["Daily Life", "Travel", "Business", "Technology", "Food & Drink", "Education", "Health", "Environment"]}


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
