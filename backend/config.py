"""
config.py – Cấu hình hệ thống AI English Learning Platform
"""

import os
from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent
IS_VERCEL = bool(os.getenv("VERCEL"))

if IS_VERCEL:
    DATA_DIR = Path("/tmp/data")
    tmp_db = Path("/tmp/app.db")
    bundled_db = BASE_DIR / "data" / "app.db"
    if not tmp_db.exists() and bundled_db.exists():
        try:
            import shutil
            shutil.copy2(bundled_db, tmp_db)
            print("[VERCEL] Pre-seeded database copied to /tmp/app.db successfully.")
        except Exception as e:
            print(f"[VERCEL] Could not copy bundled DB: {e}")
else:
    DATA_DIR = BASE_DIR / "data"

MEDIA_DIR = DATA_DIR / "media"
VOCAB_DIR = DATA_DIR / "vocabulary"
AUDIO_DIR = MEDIA_DIR / "audio"
IMAGE_DIR = MEDIA_DIR / "images"

# Ensure directories exist
for d in [DATA_DIR, MEDIA_DIR, VOCAB_DIR, AUDIO_DIR, IMAGE_DIR]:
    try:
        d.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass


class Settings(BaseSettings):
    # ── App ────────────────────────────────────────────────────
    APP_NAME: str = "AI English Learning Platform"
    APP_VERSION: str = "1.0.0"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DEBUG: bool = True

    # ── Database ───────────────────────────────────────────────
    DATABASE_URL: str = "sqlite+aiosqlite:////tmp/app.db" if IS_VERCEL else f"sqlite+aiosqlite:///{DATA_DIR}/app.db"

    # ── JWT Auth ───────────────────────────────────────────────
    SECRET_KEY: str = "vihtech-ai-english-learning-secret-key-2024-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 hours

    # ── Gemini API ─────────────────────────────────────────────
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "AIzaSyAmw1VHga-G0fp6tOaoQPcmFUsVP6N-8vQ")
    GEMINI_MODEL: str = "gemini-2.5-flash"
    GEMINI_TEMPERATURE: float = 0.7


    # ── AI Engine Settings ─────────────────────────────────────
    WHISPER_MODEL: str = "base"          # tiny | base | small | medium | large
    WHISPER_LANGUAGE: str = "en"

    # ── LibreTranslate ─────────────────────────────────────────
    LIBRETRANSLATE_URL: str = "http://localhost:5000"
    LIBRETRANSLATE_API_KEY: str = ""

    # ── LanguageTool ───────────────────────────────────────────
    LANGUAGETOOL_URL: str = "http://localhost:8081"

    # ── Qdrant Vector DB ───────────────────────────────────────
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "ai_english_memory"

    # ── Gamification ───────────────────────────────────────────
    XP_PER_LESSON: int = 50
    XP_PER_QUIZ_CORRECT: int = 10
    XP_PER_VOCAB: int = 5
    XP_PER_STREAK_DAY: int = 20
    COIN_PER_LEVEL_UP: int = 100

    # ── CORS ───────────────────────────────────────────────────
    CORS_ORIGINS: list = ["*"]

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

# ── Level System ──────────────────────────────────────────────────────────────
LEVEL_THRESHOLDS = {
    1: 0,
    2: 100,
    3: 300,
    4: 600,
    5: 1000,
    6: 1500,
    7: 2200,
    8: 3000,
    9: 4000,
    10: 5500,
}

LEVEL_NAMES = {
    1: "Người Mới Bắt Đầu",
    2: "Học Viên Cơ Bản",
    3: "Học Viên Trung Cấp",
    4: "Người Học Chăm Chỉ",
    5: "Học Viên Nâng Cao",
    6: "Chuyên Gia Tiếng Anh",
    7: "Cao Thủ Ngôn Ngữ",
    8: "Bậc Thầy Tiếng Anh",
    9: "Siêu Sao Học Thuật",
    10: "Huyền Thoại Ngôn Ngữ",
}

# ── CEFR Levels ───────────────────────────────────────────────────────────────
CEFR_LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]

# ── Skill Types ───────────────────────────────────────────────────────────────
SKILL_TYPES = ["vocabulary", "grammar", "listening", "speaking", "reading", "writing", "translation"]

# ── Course Categories ─────────────────────────────────────────────────────────
COURSE_CATEGORIES = ["general", "toeic", "ielts", "toefl", "business", "travel", "kids", "conversation"]
