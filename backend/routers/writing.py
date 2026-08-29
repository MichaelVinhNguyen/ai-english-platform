from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.database import get_db
from backend.database.models import User, WritingSubmission, StudySession
from backend.database.schemas import WritingSubmit
from backend.services.ai_engine import ai_engine
from backend.services.gamification_service import gamification_service
from backend.routers.auth import get_current_user

writing_router = APIRouter(prefix="/api/writing", tags=["Writing"])

@writing_router.post("/submit")
async def submit_writing(
    data: WritingSubmit, current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    feedback = await ai_engine.evaluate_writing(data.content, data.writing_type, data.prompt)
    score = feedback.get("score", 6.5)
    xp = gamification_service.calculate_xp_reward("writing", score / 10)

    sub = WritingSubmission(
        user_id=current_user.id, writing_type=data.writing_type,
        prompt=data.prompt, content=data.content,
        word_count=len(data.content.split()),
        score=score,
        grammar_score=feedback.get("grammar_score", score),
        vocabulary_score=feedback.get("vocabulary_score", score),
        coherence_score=feedback.get("coherence_score", score),
        feedback=feedback.get("feedback", ""),
        grammar_errors=feedback.get("grammar_errors", []),
        suggestions=feedback.get("suggestions", []),
    )
    db.add(sub)
    session = StudySession(user_id=current_user.id, session_type="writing",
                            skill="writing", score=score, xp_earned=xp)
    db.add(session)
    current_user.xp += xp
    await db.commit()
    return {**feedback, "xp_earned": xp, "submission_id": sub.id}

@writing_router.get("/history")
async def writing_history(
    limit: int = 10, current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    r = await db.execute(
        select(WritingSubmission)
        .where(WritingSubmission.user_id == current_user.id)
        .order_by(desc(WritingSubmission.submitted_at)).limit(limit)
    )
    subs = r.scalars().all()
    return [{"id": s.id, "writing_type": s.writing_type, "word_count": s.word_count,
             "score": s.score, "submitted_at": s.submitted_at} for s in subs]

@writing_router.get("/prompts")
async def writing_prompts(writing_type: str = "essay",
                           current_user: User = Depends(get_current_user)):
    prompts_map = {
        "essay": [
            "1. Discuss the advantages and disadvantages of artificial intelligence in modern education.",
            "2. Should governments implement a four-day work week for all employees? Give reasons and examples.",
            "3. Some believe remote working improves quality of life, while others argue it damages workplace culture. Discuss both views.",
            "4. Environmental degradation is the most pressing crisis of our century. What measures can individuals and governments take?",
            "5. To what extent has social media influenced youth mental health and interpersonal communication?",
            "6. Space exploration requires astronomical funding. Should these financial resources be redirected to solve poverty on Earth?",
            "7. The preservation of historical architecture versus the modernization of urban infrastructure: Discuss both sides.",
            "8. Is university education still necessary for career success in the digital startup economy?"
        ],
        "ielts_task1": [
            "1. [Line Graph] The graph shows global renewable energy consumption trends between 2000 and 2025. Summarize the main features.",
            "2. [Bar Chart] The chart compares plastic waste generation and recycling percentages across six developed nations in 2024.",
            "3. [Pie Charts] The two pie charts illustrate the distribution of household expenditures in Vietnam in 2010 versus 2025.",
            "4. [Process Diagram] The diagram illustrates the multistage manufacturing process of converting recycled plastic bottles into polyester fibers.",
            "5. [Map Comparison] The maps show the urban development and infrastructural transformation of a coastal town between 1995 and today."
        ],
        "ielts_task2": [
            "1. [Opinion] Some argue that international tourism inevitably destroys traditional local culture. To what extent do you agree or disagree?",
            "2. [Discussion] Some people think universities should focus on practical job skills, while others believe education should focus on pure knowledge. Discuss both views.",
            "3. [Problem-Solution] Traffic congestion in major metropolitan cities has reached intolerable levels. What are the causes and what effective solutions can be adopted?",
            "4. [Direct Questions] Modern consumers purchase far more consumer goods than they actually need. What factors drive consumerism, and what are its environmental impacts?",
            "5. [Advantages-Disadvantages] In many countries, cashless digital payments have almost entirely replaced physical cash. Do the advantages outweigh the disadvantages?"
        ],
        "email": [
            "1. Write a formal email applying for a Senior AI Product Manager position at a multinational tech firm.",
            "2. Write a professional email requesting an extension for your university thesis submission due to medical circumstances.",
            "3. Write a polite yet firm complaint email to an airline regarding lost baggage and demanding compensation.",
            "4. Write an email to negotiate price terms and delivery schedules with an overseas manufacturing supplier.",
            "5. Write an invitation email to an industry keynote speaker for an upcoming international tech conference."
        ],
        "cv": [
            "1. Write a compelling Executive Summary for a Full-Stack Software Engineer with 5 years of fintech experience.",
            "2. Craft a high-impact Professional Objective for a Marketing Manager transitioning into Data Analytics.",
            "3. Write a Career Summary and Key Achievements bullet points for a Healthcare Administrator.",
            "4. Formulate an academic CV personal statement applying for a Master of Science scholarship at Oxford."
        ],
        "story": [
            "1. Write an evocative short story about an archaeologist who unearths an unrecorded artifact beneath an ancient temple.",
            "2. Describe your most memorable cross-continental travel experience and the unexpected lesson it taught you.",
            "3. Write a science fiction narrative about the first successful quantum teleportation experiment.",
            "4. Tell a story about two estranged childhood friends who unexpectedly reunite at an international airport terminal."
        ],
        "report": [
            "1. Write an Executive Business Report assessing quarterly sales performance and recommending Q4 growth strategies.",
            "2. Formulate an Incident Report detailing a cybersecurity data breach and outlining mitigation protocols.",
            "3. Write a Feasibility Report on transitioning company vehicle fleets to zero-emission electric vehicles.",
            "4. Draft an Annual Corporate Social Responsibility (CSR) Summary highlighting community sustainability initiatives."
        ]
    }
    return {"prompts": prompts_map.get(writing_type, prompts_map["essay"]), "all_categories": list(prompts_map.keys())}
