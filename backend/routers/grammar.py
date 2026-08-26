from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.database import get_db
from backend.database.models import User, GrammarRule
from backend.database.schemas import GrammarCheck, GrammarRuleOut
from backend.services.ai_engine import ai_engine
from backend.routers.auth import get_current_user

grammar_router = APIRouter(prefix="/api/grammar", tags=["Grammar"])

@grammar_router.post("/check")
async def check_grammar(data: GrammarCheck, current_user: User = Depends(get_current_user)):
    result = await ai_engine.check_grammar(data.text)
    return result

@grammar_router.post("/explain")
async def explain_grammar(
    topic: str = Query(...),
    level: str = Query("B1"),
    current_user: User = Depends(get_current_user)
):
    return await ai_engine.explain_grammar(topic, level)

@grammar_router.post("/explain-beginner")
async def explain_grammar_beginner(
    topic: str = Query(...),
    current_user: User = Depends(get_current_user)
):
    """Giải thích quy tắc ngữ pháp cho người mới bắt đầu / trình độ mầm non đơn giản nhất."""
    prompt = f"""Giải thích khái niệm ngữ pháp tiếng Anh: "{topic}" theo phong cách "Giải thích cho người mới bắt đầu hoàn toàn / em bé 10 tuổi" bằng Tiếng Việt cực kỳ hóm hỉnh, ngắn gọn, dùng các ví dụ so sánh ẩn dụ siêu đời sống.

Format JSON:
{{
  "title": "{topic}",
  "simple_explanation": "Giải thích siêu siêu đơn giản 2-3 câu",
  "analogy": "Hình ảnh so sánh đời sống",
  "golden_rule": "Quy tắc vàng nằm lòng",
  "easy_examples": [{{"en": "Ví dụ siêu ngắn", "vi": "Dịch siêu mượt"}}],
  "quick_tip": "Mẹo nhớ trong 3 giây"
}}"""
    try:
        resp = await ai_engine._generate_text(prompt)
        import json
        return json.loads(ai_engine._extract_json(resp.text))
    except Exception:
        return {
            "title": topic,
            "simple_explanation": f"Hãy nghĩ về {topic} như một chiếc công tắc đèn: bật lên khi diễn tả hành động đang xảy ra!",
            "analogy": "Giống như bạn đeo đồng hồ đếm ngược.",
            "golden_rule": "Nhớ thêm đuôi -ing hoặc dùng trợ động từ phù hợp.",
            "easy_examples": [{"en": "I am studying.", "vi": "Tôi đang học bài."}],
            "quick_tip": "Nhìn từ chìa khóa là biết chọn ngay!"
        }

@grammar_router.get("/rules", response_model=List[GrammarRuleOut])
async def get_grammar_rules(
    level: Optional[str] = None, category: Optional[str] = None,
    db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)
):
    q = select(GrammarRule)
    if level: q = q.where(GrammarRule.level == level)
    if category: q = q.where(GrammarRule.category == category)
    r = await db.execute(q.limit(50))
    return [GrammarRuleOut.model_validate(g) for g in r.scalars()]

@grammar_router.post("/generate-exercise")
async def generate_grammar_exercise(
    topic: str, level: str = "B1", count: int = 5,
    current_user: User = Depends(get_current_user)
):
    questions = await ai_engine.generate_quiz(
        skill="grammar",
        level=level,
        topic=topic,
        count=count,
        types=["multiple_choice", "fill_blank"]
    )
    return {"questions": questions}

