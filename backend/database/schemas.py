"""
schemas.py – Pydantic schemas for request/response validation
"""
from datetime import datetime
from typing import Any, Optional, List
from pydantic import BaseModel, EmailStr, Field


# ── AUTH ─────────────────────────────────────────────────────────────────────
class UserRegister(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str = Field(..., min_length=2, max_length=200)
    password: str = Field(..., min_length=6)
    native_language: str = "vi"

class UserLogin(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    username: str
    full_name: Optional[str] = None
    role: Optional[str] = "student"
    level: Optional[int] = 1
    xp: Optional[int] = 0
    coins: Optional[int] = 0
    streak: Optional[int] = 0
    longest_streak: Optional[int] = 0
    target_level: Optional[str] = "B1"
    daily_goal_xp: Optional[int] = 50
    avatar_url: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str; token_type: str = "bearer"; user: UserOut

class UserUpdate(BaseModel):
    full_name: Optional[str] = None; target_level: Optional[str] = None
    daily_goal_xp: Optional[int] = None; native_language: Optional[str] = None


# ── CHAT / AI TEACHER ─────────────────────────────────────────────────────────
class ChatMessage(BaseModel):
    content: str; mode: str = "chat"
    session_id: Optional[str] = None; context: Optional[dict] = None

class ChatResponse(BaseModel):
    content: str; session_id: str
    feedback: Optional[dict] = None
    suggestions: Optional[List[str]] = None
    vocabulary: Optional[List[dict]] = None

class SpeakingEvaluation(BaseModel):
    transcript: str; pronunciation_score: float; fluency_score: float
    grammar_score: float; vocabulary_score: float; overall_score: float
    feedback: str; corrections: List[dict]; suggestions: List[str]


# ── VOCABULARY ────────────────────────────────────────────────────────────────
class VocabOut(BaseModel):
    id: int; word: str; ipa: Optional[str]; word_type: Optional[str]
    definition_en: Optional[str]; definition_vi: Optional[str]
    examples: Optional[List] = None; synonyms: Optional[List] = None
    level: Optional[str]; topic: Optional[str]; audio_url: Optional[str]
    class Config: from_attributes = True

class FlashcardReview(BaseModel):
    vocab_id: int; quality: int = Field(..., ge=0, le=5)


# ── GRAMMAR ───────────────────────────────────────────────────────────────────
class GrammarCheck(BaseModel):
    text: str; language: str = "en-US"

class GrammarCheckResult(BaseModel):
    original_text: str; corrected_text: str
    errors: List[dict]; error_count: int; score: float
    explanation: Optional[str] = None

class GrammarRuleOut(BaseModel):
    id: int; title: str; category: Optional[str]; level: Optional[str]
    explanation: Optional[str]; examples: Optional[List] = None
    tips: Optional[List] = None; common_mistakes: Optional[List] = None
    class Config: from_attributes = True


# ── QUIZ ──────────────────────────────────────────────────────────────────────
class QuizGenRequest(BaseModel):
    skill: str = "vocabulary"; level: str = "B1"
    topic: Optional[str] = None; count: int = Field(10, ge=1, le=30)
    question_types: Optional[List[str]] = None

class QuizSubmit(BaseModel):
    question_id: int; user_answer: str; time_taken_sec: Optional[float] = None

class QuizResult(BaseModel):
    question_id: int; is_correct: bool; correct_answer: str
    explanation: Optional[str]; xp_earned: int

class QuizQuestionOut(BaseModel):
    id: int; question_text: str; question_type: str
    options: Optional[List] = None; skill: Optional[str]; level: Optional[str]
    class Config: from_attributes = True


# ── WRITING ───────────────────────────────────────────────────────────────────
class WritingSubmit(BaseModel):
    writing_type: str = "essay"; prompt: Optional[str] = None; content: str

class WritingFeedback(BaseModel):
    score: float; grammar_score: float; vocabulary_score: float
    coherence_score: float; feedback: str; grammar_errors: List[dict]
    suggestions: List[str]; corrected_version: Optional[str] = None


# ── TRANSLATION ───────────────────────────────────────────────────────────────
class TranslateRequest(BaseModel):
    text: str; source_lang: str = "en"; target_lang: str = "vi"; detailed: bool = False

class TranslateResult(BaseModel):
    original: str; translated: str; source_lang: str; target_lang: str
    explanation: Optional[str] = None; examples: Optional[List[str]] = None
    synonyms: Optional[List[str]] = None


# ── COURSES ───────────────────────────────────────────────────────────────────
class CourseOut(BaseModel):
    id: int; title: str; description: Optional[str]; level: Optional[str]
    category: Optional[str]; total_lessons: int; duration_hours: float
    is_premium: bool; thumbnail_url: Optional[str]
    class Config: from_attributes = True

class LessonOut(BaseModel):
    id: int; course_id: int; title: str; lesson_type: Optional[str]
    duration_minutes: int; xp_reward: int; order_index: int
    class Config: from_attributes = True

class CourseCreate(BaseModel):
    title: str; description: Optional[str] = None
    level: str = "A1"; category: str = "general"; is_premium: bool = False

class LessonCreate(BaseModel):
    course_id: int; title: str; description: Optional[str] = None
    lesson_type: str; content: Optional[str] = None
    duration_minutes: int = 15; xp_reward: int = 50; order_index: int = 0


# ── GAMIFICATION ──────────────────────────────────────────────────────────────
class BadgeOut(BaseModel):
    id: int; name: str; description: Optional[str]; icon: Optional[str]
    category: Optional[str]; xp_reward: int; coin_reward: int
    class Config: from_attributes = True

class LeaderboardEntry(BaseModel):
    rank: int; user_id: int; username: str; full_name: Optional[str]
    avatar_url: Optional[str]; level: int; xp: int; streak: int

class DashboardStats(BaseModel):
    xp: int; level: int; level_name: str; coins: int; streak: int
    xp_to_next_level: int; xp_progress_percent: float
    today_xp: int; daily_goal_xp: int
    total_vocab_learned: int; total_lessons_completed: int
    total_study_time_min: int; skill_scores: dict
    next_recommended_action: Optional[dict] = None
    recent_activity: List[dict]; due_flashcards: int


# ── COMMUNITY ─────────────────────────────────────────────────────────────────
class PostCreate(BaseModel):
    title: str; content: str; category: str = "question"

class PostOut(BaseModel):
    id: int; user_id: int; title: Optional[str]; content: Optional[str]
    category: Optional[str]; likes: int; created_at: datetime
    class Config: from_attributes = True

class CommentCreate(BaseModel):
    content: str

class AdminStats(BaseModel):
    total_users: int; active_users_today: int; total_courses: int
    total_lessons: int; total_vocabulary: int; total_study_sessions: int
