"""
common_phrases.py – API Router for Common Phrases & Situational Dialogues (Câu nói thường gặp)
50 Comprehensive Topics x 50 Bilingual Q&A Conversation Pairs (2,500 pairs total)
"""
import sqlite3
import json
import re
from pathlib import Path
from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Query, HTTPException

from backend.config import BASE_DIR

router = APIRouter(prefix="/api/common-phrases", tags=["Common Phrases (Câu nói thường gặp)"])

DB_PATH = BASE_DIR / "data" / "app.db"

def get_db_connection():
    """Create a connection to SQLite database."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def clean_bracket_prefix(text: str) -> str:
    """Remove leading [Topic Name] prefix if present."""
    if not text:
        return ""
    return re.sub(r"^\[.*?\]\s*", "", text).strip()

def normalize_topic_row(r) -> dict:
    """Normalize topic row to standard schema."""
    d = dict(r)
    return {
        "id": d.get("id"),
        "code": d.get("code", ""),
        "title": d.get("name") or d.get("title") or "",
        "title_vi": d.get("name_vi") or d.get("title_vi") or "",
        "category": d.get("category", ""),
        "category_vi": d.get("category_vi", ""),
        "icon": d.get("icon", "💬"),
        "cartoon": d.get("avatar_a") or d.get("icon") or "💬",
        "avatar_a": d.get("avatar_a", "🙋‍♀️"),
        "avatar_b": d.get("avatar_b", "🙋‍♂️"),
        "color": d.get("color", "#10b981"),
        "description": d.get("desc") or d.get("description") or "",
        "description_vi": d.get("desc") or d.get("description_vi") or "",
        "phrase_count": d.get("total_phrases") or d.get("phrase_count") or 50
    }

def normalize_phrase_row(r) -> dict:
    """Normalize phrase row to standard schema."""
    d = dict(r)
    q_raw = d.get("question_en") or d.get("q_text") or ""
    q_vi_raw = d.get("question_vi") or d.get("q_vi") or ""
    a_raw = d.get("answer_en") or d.get("a_text") or ""
    a_vi_raw = d.get("answer_vi") or d.get("a_vi") or ""

    kw = d.get("keywords") or d.get("key_vocab") or ""
    if isinstance(kw, str) and kw.startswith("[") and kw.endswith("]"):
        try:
            kw_list = json.loads(kw)
            kw = ", ".join(kw_list)
        except Exception:
            pass

    return {
        "id": d.get("id"),
        "topic_id": d.get("topic_id"),
        "order_index": d.get("order_index", 1),
        "situation": d.get("situation", ""),
        "situation_type": d.get("situation_type", ""),
        "q_text": clean_bracket_prefix(q_raw),
        "q_vi": clean_bracket_prefix(q_vi_raw),
        "q_ipa": d.get("question_ipa") or d.get("q_ipa") or "",
        "q_speaker": d.get("speaker_a_role") or d.get("q_speaker") or "Speaker A",
        "q_avatar": d.get("speaker_a_avatar") or d.get("q_avatar") or "🙋‍♀️",
        "a_text": clean_bracket_prefix(a_raw),
        "a_vi": clean_bracket_prefix(a_vi_raw),
        "a_ipa": d.get("answer_ipa") or d.get("a_ipa") or "",
        "a_speaker": d.get("speaker_b_role") or d.get("a_speaker") or "Speaker B",
        "a_avatar": d.get("speaker_b_avatar") or d.get("a_avatar") or "🙋‍♂️",
        "tips": d.get("tip") or d.get("tips") or "",
        "key_vocab": kw,
        "difficulty": d.get("difficulty", "Intermediate")
    }

@router.get("/categories")
async def get_categories():
    """Get list of topic categories with counts."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT category, category_vi, COUNT(*) as topic_count, SUM(total_phrases) as phrase_count
            FROM common_phrases_topics
            GROUP BY category
            ORDER BY MIN(id)
        """)
        rows = cur.fetchall()
        conn.close()
        
        categories = []
        for r in rows:
            categories.append({
                "category": r["category"],
                "category_vi": r["category_vi"],
                "topic_count": r["topic_count"],
                "phrase_count": r["phrase_count"] or (r["topic_count"] * 50)
            })
        return {"categories": categories, "total_categories": len(categories)}
    except Exception as e:
        return {"categories": [], "error": str(e)}

@router.get("/topics")
async def get_topics(category: Optional[str] = None):
    """Get list of 50 topics with phrase count and metadata."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        if category and isinstance(category, str) and category.lower() != "all":
            cur.execute("""
                SELECT * FROM common_phrases_topics
                WHERE category = ? OR category_vi = ?
                ORDER BY id ASC
            """, (category, category))
        else:
            cur.execute("SELECT * FROM common_phrases_topics ORDER BY id ASC")
        rows = cur.fetchall()
        conn.close()
        
        topics = [normalize_topic_row(r) for r in rows]
        return {"topics": topics, "total": len(topics)}
    except Exception as e:
        return {"topics": [], "error": str(e)}

@router.get("/topic/{topic_id}")
async def get_topic_phrases(topic_id: int):
    """Get a specific topic along with all 50 bilingual Q&A conversation phrases."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM common_phrases_topics WHERE id = ?", (topic_id,))
        topic_row = cur.fetchone()
        if not topic_row:
            conn.close()
            raise HTTPException(status_code=404, detail=f"Topic {topic_id} not found")
        
        topic = normalize_topic_row(topic_row)
        
        cur.execute("""
            SELECT * FROM common_phrases
            WHERE topic_id = ?
            ORDER BY order_index ASC
        """, (topic_id,))
        phrase_rows = cur.fetchall()
        conn.close()
        
        phrases = [normalize_phrase_row(r) for r in phrase_rows]
        return {
            "topic": topic,
            "phrases": phrases,
            "total_phrases": len(phrases)
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search")
async def search_phrases(q: str = Query(..., min_length=1, description="Search keyword in English or Vietnamese")):
    """Search phrases across all 50 topics by keyword."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        pattern = f"%{q}%"
        cur.execute("""
            SELECT p.*, t.name as topic_title, t.name_vi as topic_title_vi, t.icon as topic_icon, t.avatar_a as topic_cartoon
            FROM common_phrases p
            JOIN common_phrases_topics t ON p.topic_id = t.id
            WHERE p.question_en LIKE ? OR p.question_vi LIKE ? OR p.answer_en LIKE ? OR p.answer_vi LIKE ? OR p.keywords LIKE ?
            ORDER BY p.topic_id ASC, p.order_index ASC
            LIMIT 100
        """, (pattern, pattern, pattern, pattern, pattern))
        rows = cur.fetchall()
        conn.close()
        
        results = []
        for r in rows:
            p = normalize_phrase_row(r)
            p["topic_title"] = r["topic_title"]
            p["topic_title_vi"] = r["topic_title_vi"]
            p["topic_icon"] = r["topic_icon"]
            p["topic_cartoon"] = r["topic_cartoon"]
            results.append(p)

        return {"query": q, "results": results, "total": len(results)}
    except Exception as e:
        return {"query": q, "results": [], "error": str(e)}
