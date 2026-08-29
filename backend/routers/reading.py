from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from backend.database.database import get_db
from backend.database.models import User
from backend.services.ai_engine import ai_engine
from backend.routers.auth import get_current_user

reading_router   = APIRouter(prefix="/api/reading", tags=["Reading"])

class SummarizeRequest(BaseModel):
    text: str
    language: str = "vi"

class ReadingQuestionsRequest(BaseModel):
    text: str
    count: int = 5

@reading_router.get("/articles")
async def get_articles(level: Optional[str] = None, topic: Optional[str] = None,
                        db: AsyncSession = Depends(get_db),
                        current_user: User = Depends(get_current_user)):
    from backend.database.models import ReadingArticle
    q = select(ReadingArticle)
    if level: q = q.where(ReadingArticle.level == level)
    if topic: q = q.where(ReadingArticle.topic == topic)
    r = await db.execute(q.limit(100))
    articles = r.scalars().all()
    return [{"id": a.id, "title": a.title, "summary": a.summary,
             "level": a.level, "topic": a.topic, "word_count": a.word_count,
             "article_type": a.article_type, "content": a.content, "questions": a.questions} for a in articles]

@reading_router.post("/summarize")
async def summarize_article(data: SummarizeRequest, current_user: User = Depends(get_current_user)):
    summary = await ai_engine.summarize(data.text, data.language)
    return {"summary": summary}

@reading_router.post("/questions")
async def generate_questions(data: ReadingQuestionsRequest,
                              current_user: User = Depends(get_current_user)):
    questions = await ai_engine.generate_reading_questions(data.text, data.count)
    return {"questions": questions}


@reading_router.get("/articles/{article_id}")
async def get_article_detail(
    article_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    from backend.database.models import ReadingArticle
    result = await db.execute(
        select(ReadingArticle).where(ReadingArticle.id == article_id)
    )
    article = result.scalar_one_or_none()
    if not article:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Article not found")
    
    return {
        "id": article.id,
        "title": article.title,
        "content": article.content,
        "summary": article.summary,
        "level": article.level,
        "topic": article.topic,
        "word_count": article.word_count,
        "questions": article.questions
    }
