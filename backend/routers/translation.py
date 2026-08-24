from typing import Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from backend.database.models import User
from backend.database.schemas import TranslateResult
from backend.services.ai_engine import ai_engine
from backend.routers.auth import get_current_user

translation_router = APIRouter(prefix="/api/translation", tags=["Translation"])

class DetailedTranslateRequest(BaseModel):
    text: str
    source_lang: str = "en"
    target_lang: str = "vi"
    mode: str = "natural" # literal, natural, business, academic
    detailed: bool = True

@translation_router.post("/translate")
async def translate(data: DetailedTranslateRequest, current_user: User = Depends(get_current_user)):
    mode_instructions = {
        "literal": "Dịch sát từng từ nghĩa đen (Literal Translation).",
        "natural": "Dịch mượt mà, tự nhiên chuẩn bản xứ (Natural Translation).",
        "business": "Dịch theo trang trọng, chuyên nghiệp thương mại (Business/Corporate Translation).",
        "academic": "Dịch theo văn phong hàn lâm, học thuật (Academic/Research Translation)."
    }
    instruction = mode_instructions.get(data.mode, mode_instructions["natural"])
    
    prompt = f"""Hãy dịch đoạn văn sau từ {data.source_lang} sang {data.target_lang} theo tiêu chuẩn: {instruction}
Văn bản: "{data.text}"

Format JSON:
{{
  "translated": "Bản dịch theo chế độ {data.mode}",
  "mode": "{data.mode}",
  "explanation": "Giải thích cấu trúc và lựa chọn từ vựng",
  "examples": ["Ví dụ ngữ cảnh 1", "Ví dụ ngữ cảnh 2"],
  "synonyms": ["Từ đồng nghĩa/cách diễn đạt thay thế"],
  "grammar_notes": "Ghi chú ngữ pháp đáng chú ý"
}}"""
    try:
        resp = await ai_engine._generate_text(prompt)
        import json
        res = json.loads(ai_engine._extract_json(resp.text))
        return {
            "original": data.text,
            "translated": res.get("translated", ""),
            "mode": data.mode,
            "source_lang": data.source_lang,
            "target_lang": data.target_lang,
            "explanation": res.get("explanation"),
            "examples": res.get("examples"),
            "synonyms": res.get("synonyms"),
            "grammar_notes": res.get("grammar_notes")
        }
    except Exception:
        fallback = await ai_engine.translate(data.text, data.source_lang, data.target_lang, data.detailed)
        return {
            "original": data.text,
            "translated": fallback.get("translated", ""),
            "mode": data.mode,
            "source_lang": data.source_lang,
            "target_lang": data.target_lang,
            "explanation": fallback.get("explanation"),
            "examples": fallback.get("examples"),
            "synonyms": fallback.get("synonyms")
        }

@translation_router.post("/quick")
async def quick_translate(text: str, current_user: User = Depends(get_current_user)):
    result = await ai_engine.translate(text, "en", "vi")
    return {"original": text, "translated": result.get("translated", "")}

