"""
main.py – FastAPI Application Entry Point
Khởi động toàn bộ hệ thống AI English Learning Platform
"""
import os
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession

from backend.config import settings, BASE_DIR
from backend.database.database import init_db, get_db

# Import routers
from backend.routers.auth import router as auth_router
from backend.routers.ai_teacher import router as teacher_router
from backend.routers.vocabulary import router as vocab_router
from backend.routers.quiz import router as quiz_router
from backend.routers.grammar import grammar_router
from backend.routers.writing import writing_router
from backend.routers.translation import translation_router
from backend.routers.courses import courses_router
from backend.routers.dashboard import dashboard_router
from backend.routers.gamification import gamification_router
from backend.routers.community import community_router
from backend.routers.admin import admin_router
from backend.routers.listening import listening_router
from backend.routers.speaking import speaking_router
from backend.routers.reading import reading_router
from backend.routers.learning_path import router as learning_path_router
from backend.routers.level_curriculum import router as level_curriculum_router
from backend.routers.common_phrases import router as common_phrases_router

FRONTEND_DIR = BASE_DIR / "frontend"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup & shutdown events."""
    print("[START] Khoi dong AI English Learning Platform...")
    try:
        await init_db()
        print("[OK] Database initialized")
    except Exception as e:
        print(f"[WARN] Database init: {e}")
    print("[WEB] Frontend Ready")
    print(f"[AI] Gemini Model: {settings.GEMINI_MODEL}")
    yield
    print("[STOP] Dung he thong...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="🎓 Nền tảng học tiếng Anh thông minh với AI",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    lifespan=lifespan,
)

@app.get("/api/health")
@app.get("/health")
async def health_check():
    return {"status": "ok", "app": "AI English Learning Platform", "cloud": "ready"}

# ── CORS ─────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── API Routers ───────────────────────────────────────────────────────────────
app.include_router(auth_router, prefix="/api")
app.include_router(auth_router, prefix="")
app.include_router(teacher_router)
app.include_router(vocab_router)
app.include_router(quiz_router)
app.include_router(grammar_router)
app.include_router(writing_router)
app.include_router(translation_router)
app.include_router(courses_router)
app.include_router(dashboard_router)
app.include_router(gamification_router)
app.include_router(community_router)
app.include_router(admin_router)
app.include_router(listening_router)
app.include_router(speaking_router)
app.include_router(reading_router)
app.include_router(learning_path_router)
app.include_router(level_curriculum_router)
app.include_router(common_phrases_router)

# ── Admin Seed Endpoint ────────────────────────────────────────────────────────
@app.post("/api/admin/seed-rich-data", tags=["admin"])
async def seed_rich_data_endpoint(db: AsyncSession = Depends(get_db)):
    from backend.seed_rich_data import seed_data
    await seed_data(db)
    return {"message": "Rich data seeded successfully!"}

# ── Static Files (Frontend) ───────────────────────────────────────────────────
if FRONTEND_DIR.exists():
    # Serve static assets
    for sub in ["css", "js", "assets"]:
        sub_path = FRONTEND_DIR / sub
        if sub_path.exists():
            app.mount(f"/{sub}", StaticFiles(directory=str(sub_path), html=False), name=sub)

# ── Health Check ──────────────────────────────────────────────────────────────
@app.get("/api/health", tags=["system"])
async def health():
    return {"status": "ok", "version": settings.APP_VERSION, "app": settings.APP_NAME}

# ── SPA Catch-all ─────────────────────────────────────────────────────────────
@app.get("/", include_in_schema=False)
@app.get("/{full_path:path}", include_in_schema=False)
async def serve_frontend(full_path: str = ""):
    """Serve frontend SPA for all non-API routes with no-cache headers."""
    if full_path.startswith("api/"):
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="API endpoint not found")
    index_file = FRONTEND_DIR / "index.html"
    if index_file.exists():
        response = FileResponse(str(index_file))
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    return {"message": "AI English Learning Platform API", "docs": "/api/docs",
            "version": settings.APP_VERSION}

