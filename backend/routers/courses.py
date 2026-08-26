from typing import List, Optional
import uuid
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.database import get_db
from backend.database.models import User, Course, Lesson, UserCourse, StudySession, LessonSession, LessonQuestion, LessonAnswer, UserMistake
from backend.database.schemas import CourseOut, CourseCreate, LessonCreate
from backend.services.ai_engine import ai_engine
from backend.services.gamification_service import gamification_service
from backend.routers.auth import get_current_user, get_admin_user

courses_router = APIRouter(prefix="/api/courses", tags=["Courses"])

class AnswerSubmit(BaseModel):
    session_id: str
    answer_text: str

@courses_router.get("/", response_model=List[CourseOut])
async def get_courses(
    level: Optional[str] = None, category: Optional[str] = None,
    db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)
):
    q = select(Course).where(Course.is_published == True)
    if level: q = q.where(Course.level == level)
    if category: q = q.where(Course.category == category)
    r = await db.execute(q.order_by(Course.order_index))
    return [CourseOut.model_validate(c) for c in r.scalars()]

@courses_router.get("/{course_id}")
async def get_course(course_id: int, db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    r = await db.execute(select(Course).where(Course.id == course_id))
    course = r.scalar_one_or_none()
    if not course: return {"error": "Course not found"}
    # Get lessons
    lr = await db.execute(select(Lesson).where(Lesson.course_id == course_id)
                           .order_by(Lesson.order_index))
    lessons = lr.scalars().all()
    # Get user progress
    pr = await db.execute(select(UserCourse).where(
        UserCourse.user_id == current_user.id, UserCourse.course_id == course_id))
    progress = pr.scalar_one_or_none()
    return {
        "id": course.id, "title": course.title, "description": course.description,
        "level": course.level, "category": course.category,
        "total_lessons": course.total_lessons, "is_premium": course.is_premium,
        "lessons": [{"id": l.id, "title": l.title, "lesson_type": l.lesson_type,
                     "duration_minutes": l.duration_minutes, "xp_reward": l.xp_reward,
                     "order_index": l.order_index} for l in lessons],
        "progress": {"percent": progress.progress_percent if progress else 0,
                     "completed": progress.completed_lessons if progress else 0} if progress else None
    }

@courses_router.post("/{course_id}/enroll")
async def enroll(course_id: int, db: AsyncSession = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    r = await db.execute(select(UserCourse).where(
        UserCourse.user_id == current_user.id, UserCourse.course_id == course_id))
    if r.scalar_one_or_none():
        return {"message": "Đã đăng ký khóa học này"}
    uc = UserCourse(user_id=current_user.id, course_id=course_id)
    db.add(uc)
    await db.commit()
    return {"message": "Đăng ký thành công!"}

@courses_router.get("/lesson/{lesson_id}")
async def get_lesson(lesson_id: int, db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    r = await db.execute(select(Lesson).where(Lesson.id == lesson_id))
    lesson = r.scalar_one_or_none()
    if not lesson: return {"error": "Lesson not found"}
    return {"id": lesson.id, "title": lesson.title, "lesson_type": lesson.lesson_type,
            "content": lesson.content, "duration_minutes": lesson.duration_minutes,
            "xp_reward": lesson.xp_reward, "audio_url": lesson.audio_url}

@courses_router.post("/lesson/{lesson_id}/complete")
async def complete_lesson(lesson_id: int, db: AsyncSession = Depends(get_db),
                           current_user: User = Depends(get_current_user)):
    r = await db.execute(select(Lesson).where(Lesson.id == lesson_id))
    lesson = r.scalar_one_or_none()
    if not lesson: return {"error": "Lesson not found"}
    xp = lesson.xp_reward
    current_user.xp += xp
    # Update gamification
    new_level = gamification_service.calculate_level(current_user.xp)
    leveled_up = new_level > current_user.level
    current_user.level = new_level
    session = StudySession(user_id=current_user.id, session_type="lesson",
                            xp_earned=xp, details={"lesson_id": lesson_id})
    db.add(session)
    await db.commit()
    return {"message": "Hoàn thành bài học!", "xp_earned": xp, "leveled_up": leveled_up,
            "new_level": new_level, "total_xp": current_user.xp}

@courses_router.post("/admin", dependencies=[Depends(get_admin_user)])
async def create_course(data: CourseCreate, db: AsyncSession = Depends(get_db)):
    course = Course(**data.model_dump())
    db.add(course)
    await db.commit()
    await db.refresh(course)
    return CourseOut.model_validate(course)

@courses_router.post("/admin/lessons", dependencies=[Depends(get_admin_user)])
async def create_lesson(data: LessonCreate, db: AsyncSession = Depends(get_db)):
    lesson = Lesson(**data.model_dump())
    db.add(lesson)
    await db.commit()
    return {"id": lesson.id, "title": lesson.title}

@courses_router.post("/generate-lesson")
async def generate_ai_lesson(
    topic: str, skill: str = "grammar", level: str = "B1",
    current_user: User = Depends(get_current_user)
):
    lesson = await ai_engine.generate_lesson(topic, skill, level)
    return lesson

@courses_router.post("/lesson/{lesson_id}/start-session")
async def start_lesson_session(
    lesson_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)
):
    r = await db.execute(select(Lesson).where(Lesson.id == lesson_id))
    lesson = r.scalar_one_or_none()
    if not lesson: return {"error": "Lesson not found"}
    
    session_id = str(uuid.uuid4())
    lesson_session = LessonSession(session_id=session_id, user_id=current_user.id, lesson_id=lesson_id)
    db.add(lesson_session)
    await db.commit()
    
    # Generate interactive content via AI Engine based on the lesson content
    # In a real scenario, this asks the first question or gives the explanation
    intro_message = await ai_engine.generate_lesson_interactive(lesson.content, lesson.lesson_type)
    
    return {"session_id": session_id, "message": intro_message}

@courses_router.post("/lesson/submit-answer")
async def submit_lesson_answer(
    data: AnswerSubmit, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)
):
    # Retrieve session
    r = await db.execute(select(LessonSession).where(LessonSession.session_id == data.session_id, LessonSession.user_id == current_user.id))
    session = r.scalar_one_or_none()
    if not session: return {"error": "Session not found"}
    
    # AI evaluates the answer
    eval_result = await ai_engine.evaluate_lesson_answer(data.answer_text)
    
    # Save mistake if incorrect
    if not eval_result.get("is_correct"):
        mistake = UserMistake(
            user_id=current_user.id,
            lesson_id=session.lesson_id,
            mistake_type="general",
            original_text=data.answer_text,
            correction=eval_result.get("correction", ""),
            explanation=eval_result.get("explanation", "")
        )
        db.add(mistake)
        
    await db.commit()
    return eval_result

