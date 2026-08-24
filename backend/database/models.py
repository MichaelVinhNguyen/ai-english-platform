"""
models.py – SQLAlchemy ORM models for the entire platform
"""

import json
from datetime import datetime, timezone
from sqlalchemy import (
    Boolean, Column, DateTime, Float, ForeignKey,
    Integer, String, Text, JSON, Enum as SAEnum
)
from sqlalchemy.orm import relationship
from backend.database.database import Base


def now_utc():
    return datetime.now(timezone.utc)


# ═══════════════════════════════════════════════════════════════
#  USER & AUTH
# ═══════════════════════════════════════════════════════════════
class User(Base):
    __tablename__ = "users"

    id            = Column(Integer, primary_key=True, index=True)
    email         = Column(String(255), unique=True, nullable=False, index=True)
    username      = Column(String(100), unique=True, nullable=False, index=True)
    full_name     = Column(String(200))
    password_hash = Column(String(255), nullable=False)
    role          = Column(String(20), default="student")   # student | teacher | admin | parent
    avatar_url    = Column(String(500))

    # Learning stats
    level         = Column(Integer, default=1)
    xp            = Column(Integer, default=0)
    coins         = Column(Integer, default=0)
    streak        = Column(Integer, default=0)
    longest_streak = Column(Integer, default=0)
    last_study_date = Column(DateTime)

    # Settings
    native_language = Column(String(10), default="vi")
    target_level    = Column(String(5), default="B1")
    daily_goal_xp   = Column(Integer, default=50)
    is_active       = Column(Boolean, default=True)
    is_verified     = Column(Boolean, default=False)

    created_at    = Column(DateTime, default=now_utc)
    updated_at    = Column(DateTime, default=now_utc, onupdate=now_utc)

    # Relationships
    chat_histories     = relationship("ChatHistory", back_populates="user", cascade="all, delete-orphan")
    user_vocabularies  = relationship("UserVocabulary", back_populates="user", cascade="all, delete-orphan")
    user_courses       = relationship("UserCourse", back_populates="user", cascade="all, delete-orphan")
    quiz_attempts      = relationship("UserQuizAttempt", back_populates="user", cascade="all, delete-orphan")
    user_badges        = relationship("UserBadge", back_populates="user", cascade="all, delete-orphan")
    writing_submissions = relationship("WritingSubmission", back_populates="user", cascade="all, delete-orphan")
    study_sessions     = relationship("StudySession", back_populates="user", cascade="all, delete-orphan")
    notifications      = relationship("Notification", back_populates="user", cascade="all, delete-orphan")


# ═══════════════════════════════════════════════════════════════
#  COURSES & LESSONS
# ═══════════════════════════════════════════════════════════════
class Course(Base):
    __tablename__ = "courses"

    id           = Column(Integer, primary_key=True, index=True)
    title        = Column(String(300), nullable=False)
    description  = Column(Text)
    level        = Column(String(5))          # A1 | A2 | B1 | B2 | C1 | C2
    category     = Column(String(50))         # general | toeic | ielts | business | ...
    thumbnail_url = Column(String(500))
    total_lessons = Column(Integer, default=0)
    duration_hours = Column(Float, default=0)
    is_premium   = Column(Boolean, default=False)
    is_published = Column(Boolean, default=True)
    order_index  = Column(Integer, default=0)
    created_at   = Column(DateTime, default=now_utc)

    lessons      = relationship("Lesson", back_populates="course", cascade="all, delete-orphan",
                                order_by="Lesson.order_index")
    user_courses = relationship("UserCourse", back_populates="course", cascade="all, delete-orphan")


class Lesson(Base):
    __tablename__ = "lessons"

    id           = Column(Integer, primary_key=True, index=True)
    course_id    = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    title        = Column(String(300), nullable=False)
    description  = Column(Text)
    lesson_type  = Column(String(30))         # vocabulary | grammar | listening | speaking | reading | writing
    content      = Column(Text)               # JSON or markdown content
    audio_url    = Column(String(500))
    video_url    = Column(String(500))
    thumbnail_url = Column(String(500))
    duration_minutes = Column(Integer, default=15)
    order_index  = Column(Integer, default=0)
    xp_reward    = Column(Integer, default=50)
    is_published = Column(Boolean, default=True)
    created_at   = Column(DateTime, default=now_utc)

    course       = relationship("Course", back_populates="lessons")


class UserCourse(Base):
    __tablename__ = "user_courses"

    id               = Column(Integer, primary_key=True, index=True)
    user_id          = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    course_id        = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    progress_percent = Column(Float, default=0.0)
    completed_lessons = Column(Integer, default=0)
    started_at       = Column(DateTime, default=now_utc)
    completed_at     = Column(DateTime)
    certificate_url  = Column(String(500))

    user   = relationship("User", back_populates="user_courses")
    course = relationship("Course", back_populates="user_courses")


# ═══════════════════════════════════════════════════════════════
#  VOCABULARY
# ═══════════════════════════════════════════════════════════════
class Vocabulary(Base):
    __tablename__ = "vocabularies"

    id             = Column(Integer, primary_key=True, index=True)
    word           = Column(String(200), nullable=False, index=True)
    ipa            = Column(String(200))
    word_type      = Column(String(30))        # noun | verb | adjective | adverb | phrase | idiom
    definition_en  = Column(Text)
    definition_vi  = Column(Text)
    examples       = Column(JSON)              # list of example sentences
    synonyms       = Column(JSON)              # list of synonyms
    antonyms       = Column(JSON)
    collocations   = Column(JSON)
    audio_url      = Column(String(500))
    image_url      = Column(String(500))
    level          = Column(String(5))         # A1 | A2 | B1 | B2 | C1 | C2
    topic          = Column(String(100))       # business | travel | daily | academic | ...
    created_at     = Column(DateTime, default=now_utc)

    user_vocabularies = relationship("UserVocabulary", back_populates="vocabulary", cascade="all, delete-orphan")


class UserVocabulary(Base):
    __tablename__ = "user_vocabularies"

    id            = Column(Integer, primary_key=True, index=True)
    user_id       = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    vocab_id      = Column(Integer, ForeignKey("vocabularies.id", ondelete="CASCADE"), nullable=False)

    # Anki SRS fields
    ease_factor   = Column(Float, default=2.5)
    interval_days = Column(Integer, default=1)
    repetitions   = Column(Integer, default=0)
    due_date      = Column(DateTime, default=now_utc)
    review_count  = Column(Integer, default=0)
    correct_count = Column(Integer, default=0)
    is_learned    = Column(Boolean, default=False)
    added_at      = Column(DateTime, default=now_utc)
    last_reviewed = Column(DateTime)

    user       = relationship("User", back_populates="user_vocabularies")
    vocabulary = relationship("Vocabulary", back_populates="user_vocabularies")


# ═══════════════════════════════════════════════════════════════
#  GRAMMAR
# ═══════════════════════════════════════════════════════════════
class GrammarRule(Base):
    __tablename__ = "grammar_rules"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String(300), nullable=False)
    category    = Column(String(100))       # tenses | articles | prepositions | ...
    level       = Column(String(5))
    explanation = Column(Text)
    examples    = Column(JSON)
    tips        = Column(JSON)
    common_mistakes = Column(JSON)
    created_at  = Column(DateTime, default=now_utc)


# ═══════════════════════════════════════════════════════════════
#  QUIZ & EXERCISES
# ═══════════════════════════════════════════════════════════════
class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    id             = Column(Integer, primary_key=True, index=True)
    question_text  = Column(Text, nullable=False)
    question_type  = Column(String(30))     # multiple_choice | fill_blank | matching | true_false | ordering
    options        = Column(JSON)           # list of options
    correct_answer = Column(Text)
    explanation    = Column(Text)
    skill          = Column(String(30))     # vocabulary | grammar | listening | reading | writing
    level          = Column(String(5))
    topic          = Column(String(100))
    lesson_id      = Column(Integer, ForeignKey("lessons.id"), nullable=True)
    is_ai_generated = Column(Boolean, default=False)
    created_at     = Column(DateTime, default=now_utc)

    attempts = relationship("UserQuizAttempt", back_populates="question", cascade="all, delete-orphan")


class UserQuizAttempt(Base):
    __tablename__ = "user_quiz_attempts"

    id             = Column(Integer, primary_key=True, index=True)
    user_id        = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    question_id    = Column(Integer, ForeignKey("quiz_questions.id", ondelete="CASCADE"), nullable=False)
    user_answer    = Column(Text)
    is_correct     = Column(Boolean)
    time_taken_sec = Column(Float)
    xp_earned      = Column(Integer, default=0)
    attempted_at   = Column(DateTime, default=now_utc)

    user     = relationship("User", back_populates="quiz_attempts")
    question = relationship("QuizQuestion", back_populates="attempts")


# ═══════════════════════════════════════════════════════════════
#  CHAT HISTORY (AI Teacher)
# ═══════════════════════════════════════════════════════════════
class ChatHistory(Base):
    __tablename__ = "chat_histories"

    id         = Column(Integer, primary_key=True, index=True)
    user_id    = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    session_id = Column(String(100), index=True)
    role       = Column(String(20))         # user | assistant | system
    content    = Column(Text)
    mode       = Column(String(30))         # chat | voice | roleplay | lesson
    metadata_  = Column(JSON, name="metadata")
    created_at = Column(DateTime, default=now_utc)

    user = relationship("User", back_populates="chat_histories")


# ═══════════════════════════════════════════════════════════════
#  WRITING SUBMISSIONS
# ═══════════════════════════════════════════════════════════════
class WritingSubmission(Base):
    __tablename__ = "writing_submissions"

    id             = Column(Integer, primary_key=True, index=True)
    user_id        = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    writing_type   = Column(String(30))     # essay | email | cv | report | story
    prompt         = Column(Text)
    content        = Column(Text)
    word_count     = Column(Integer, default=0)
    score          = Column(Float)          # 0.0 → 10.0
    grammar_score  = Column(Float)
    vocabulary_score = Column(Float)
    coherence_score  = Column(Float)
    feedback       = Column(Text)           # AI feedback JSON
    grammar_errors = Column(JSON)
    suggestions    = Column(JSON)
    submitted_at   = Column(DateTime, default=now_utc)

    user = relationship("User", back_populates="writing_submissions")


# ═══════════════════════════════════════════════════════════════
#  STUDY SESSIONS
# ═══════════════════════════════════════════════════════════════
class StudySession(Base):
    __tablename__ = "study_sessions"

    id           = Column(Integer, primary_key=True, index=True)
    user_id      = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    session_type = Column(String(30))       # lesson | quiz | flashcard | speaking | reading | writing
    skill        = Column(String(30))
    duration_sec = Column(Integer, default=0)
    score        = Column(Float)
    xp_earned    = Column(Integer, default=0)
    coins_earned = Column(Integer, default=0)
    details      = Column(JSON)
    started_at   = Column(DateTime, default=now_utc)
    ended_at     = Column(DateTime)

    user = relationship("User", back_populates="study_sessions")


# ═══════════════════════════════════════════════════════════════
#  GAMIFICATION
# ═══════════════════════════════════════════════════════════════
class Badge(Base):
    __tablename__ = "badges"

    id              = Column(Integer, primary_key=True, index=True)
    name            = Column(String(200), nullable=False)
    description     = Column(Text)
    icon            = Column(String(200))   # emoji or url
    category        = Column(String(50))    # streak | vocab | grammar | level | ...
    condition_type  = Column(String(50))    # streak_days | vocab_count | level | quiz_score | ...
    condition_value = Column(Integer)
    xp_reward       = Column(Integer, default=0)
    coin_reward     = Column(Integer, default=0)

    user_badges = relationship("UserBadge", back_populates="badge", cascade="all, delete-orphan")


class UserBadge(Base):
    __tablename__ = "user_badges"

    id        = Column(Integer, primary_key=True, index=True)
    user_id   = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    badge_id  = Column(Integer, ForeignKey("badges.id", ondelete="CASCADE"), nullable=False)
    earned_at = Column(DateTime, default=now_utc)

    user  = relationship("User", back_populates="user_badges")
    badge = relationship("Badge", back_populates="user_badges")


class Mission(Base):
    __tablename__ = "missions"

    id             = Column(Integer, primary_key=True, index=True)
    title          = Column(String(300), nullable=False)
    description    = Column(Text)
    mission_type   = Column(String(30))     # daily | weekly | monthly | special
    condition_type = Column(String(50))     # study_minutes | vocab_reviewed | quiz_correct | streak_days
    condition_value = Column(Integer)
    xp_reward      = Column(Integer, default=0)
    coin_reward    = Column(Integer, default=0)
    is_active      = Column(Boolean, default=True)
    expires_at     = Column(DateTime)


class UserMission(Base):
    __tablename__ = "user_missions"

    id           = Column(Integer, primary_key=True, index=True)
    user_id      = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    mission_id   = Column(Integer, ForeignKey("missions.id", ondelete="CASCADE"), nullable=False)
    progress     = Column(Integer, default=0)
    is_completed = Column(Boolean, default=False)
    completed_at = Column(DateTime)
    assigned_at  = Column(DateTime, default=now_utc)


# ═══════════════════════════════════════════════════════════════
#  COMMUNITY
# ═══════════════════════════════════════════════════════════════
class Post(Base):
    __tablename__ = "posts"

    id         = Column(Integer, primary_key=True, index=True)
    user_id    = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title      = Column(String(500))
    content    = Column(Text)
    category   = Column(String(50))         # question | share | challenge | event
    likes      = Column(Integer, default=0)
    is_pinned  = Column(Boolean, default=False)
    created_at = Column(DateTime, default=now_utc)
    updated_at = Column(DateTime, default=now_utc, onupdate=now_utc)


class Comment(Base):
    __tablename__ = "comments"

    id         = Column(Integer, primary_key=True, index=True)
    post_id    = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    user_id    = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    content    = Column(Text)
    likes      = Column(Integer, default=0)
    created_at = Column(DateTime, default=now_utc)


# ═══════════════════════════════════════════════════════════════
#  NOTIFICATIONS
# ═══════════════════════════════════════════════════════════════
class Notification(Base):
    __tablename__ = "notifications"

    id         = Column(Integer, primary_key=True, index=True)
    user_id    = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title      = Column(String(300))
    message    = Column(Text)
    notif_type = Column(String(30))         # streak | achievement | reminder | system
    is_read    = Column(Boolean, default=False)
    action_url = Column(String(500))
    created_at = Column(DateTime, default=now_utc)

    user = relationship("User", back_populates="notifications")


# ═══════════════════════════════════════════════════════════════
#  READING ARTICLES
# ═══════════════════════════════════════════════════════════════
class ReadingArticle(Base):
    __tablename__ = "reading_articles"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String(500), nullable=False)
    content     = Column(Text)
    summary     = Column(Text)
    source      = Column(String(200))
    article_type = Column(String(30))       # news | blog | story | academic
    level       = Column(String(5))
    topic       = Column(String(100))
    word_count  = Column(Integer, default=0)
    audio_url   = Column(String(500))
    questions   = Column(JSON)
    created_at  = Column(DateTime, default=now_utc)


# ═══════════════════════════════════════════════════════════════
#  LISTENING EXERCISES
# ═══════════════════════════════════════════════════════════════
class ListeningExercise(Base):
    __tablename__ = "listening_exercises"

    id             = Column(Integer, primary_key=True, index=True)
    title          = Column(String(500), nullable=False)
    description    = Column(Text)
    audio_url      = Column(String(500))
    transcript     = Column(Text)
    exercise_type  = Column(String(30))     # shadowing | dictation | fill_blank | comprehension
    level          = Column(String(5))
    topic          = Column(String(100))
    duration_sec   = Column(Integer, default=0)
    questions      = Column(JSON)
    created_at     = Column(DateTime, default=now_utc)


# ═══════════════════════════════════════════════════════════════
#  STUDY SCHEDULE
# ═══════════════════════════════════════════════════════════════
class StudySchedule(Base):
    __tablename__ = "study_schedules"

    id           = Column(Integer, primary_key=True, index=True)
    user_id      = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    day_of_week  = Column(Integer)          # 0=Mon, 6=Sun
    study_time   = Column(String(5))        # "HH:MM"
    duration_min = Column(Integer, default=30)
    skill_focus  = Column(String(30))
    is_active    = Column(Boolean, default=True)


# ═══════════════════════════════════════════════════════════════
#  LEARNING PATH (Lộ trình học CEFR)
# ═══════════════════════════════════════════════════════════════
class LearningPath(Base):
    __tablename__ = "learning_paths"

    id              = Column(Integer, primary_key=True, index=True)
    user_id         = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    current_level   = Column(String(5), default="A1")    # A1 → C2
    target_level    = Column(String(5), default="B2")
    purpose         = Column(String(200))                 # thi IELTS, giao tiếp, du học, công việc...
    daily_minutes   = Column(Integer, default=30)
    strengths       = Column(String(500))                 # kỹ năng mạnh
    weaknesses      = Column(String(500))                 # kỹ năng yếu
    path_data       = Column(JSON)                        # lộ trình chi tiết từ AI
    progress_data   = Column(JSON)                        # tiến độ từng tuần
    weeks_total     = Column(Integer, default=12)
    current_week    = Column(Integer, default=1)
    is_active       = Column(Boolean, default=True)
    created_at      = Column(DateTime, default=now_utc)
    updated_at      = Column(DateTime, default=now_utc, onupdate=now_utc)

# ═══════════════════════════════════════════════════════════════
#  ARCHITECTURE DIAGRAM UPGRADES
# ═══════════════════════════════════════════════════════════════
class LessonSession(Base):
    __tablename__ = "lesson_sessions"
    id          = Column(Integer, primary_key=True, index=True)
    session_id  = Column(String(100), unique=True, index=True)
    user_id     = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    lesson_id   = Column(Integer, ForeignKey("lessons.id", ondelete="CASCADE"), nullable=False)
    start_time  = Column(DateTime, default=now_utc)
    end_time    = Column(DateTime)
    status      = Column(String(20), default="active") # active, completed
    score       = Column(Float, default=0.0)

class LessonQuestion(Base):
    __tablename__ = "lesson_questions"
    id          = Column(Integer, primary_key=True, index=True)
    session_id  = Column(String(100), ForeignKey("lesson_sessions.session_id", ondelete="CASCADE"), nullable=False)
    content     = Column(Text)
    question_type = Column(String(30))
    order_no    = Column(Integer)

class LessonAnswer(Base):
    __tablename__ = "lesson_answers"
    id          = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("lesson_questions.id", ondelete="CASCADE"), nullable=False)
    user_id     = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    answer_text = Column(Text)
    is_correct  = Column(Boolean)
    score       = Column(Float)
    feedback    = Column(Text) # AI suggestions

class UserMistake(Base):
    __tablename__ = "user_mistakes"
    id          = Column(Integer, primary_key=True, index=True)
    user_id     = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    lesson_id   = Column(Integer, ForeignKey("lessons.id", ondelete="CASCADE"))
    mistake_type= Column(String(50)) # grammar, vocab, pronunciation
    original_text = Column(Text)
    correction  = Column(Text)
    explanation = Column(Text)
    created_at  = Column(DateTime, default=now_utc)

class MockTest(Base):
    __tablename__ = "mock_tests"
    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String(300))
    test_type   = Column(String(50)) # TOEIC, IELTS
    total_score = Column(Float)
    duration_min= Column(Integer)
    sections    = Column(JSON) # e.g. [{name: 'Listening', questions: [...]}]

class MockTestAttempt(Base):
    __tablename__ = "mock_test_attempts"
    id          = Column(Integer, primary_key=True, index=True)
    test_id     = Column(Integer, ForeignKey("mock_tests.id", ondelete="CASCADE"), nullable=False)
    user_id     = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    score       = Column(Float)
    details     = Column(JSON) # Detailed scoring per section
    started_at  = Column(DateTime, default=now_utc)
    completed_at= Column(DateTime)
