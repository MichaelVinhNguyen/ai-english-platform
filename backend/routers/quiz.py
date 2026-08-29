"""
quiz.py – Quiz & Exercises: AI generate, submit, score
"""
import json
from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from backend.database.database import get_db
from backend.database.models import User, QuizQuestion, UserQuizAttempt, StudySession
from backend.database.schemas import QuizGenRequest, QuizSubmit, QuizResult, QuizQuestionOut
from backend.services.ai_engine import ai_engine
from backend.services.gamification_service import gamification_service
from backend.routers.auth import get_current_user

router = APIRouter(prefix="/api/quiz", tags=["Quiz"])

CURATED_QUIZ_BANK = {
    "grammar_master": {
        "title": "📌 12 Thì & Ngữ Pháp Trọng Điểm Căn Bản Đến Nâng Cao",
        "description": "Làm chủ Present Perfect, Past Continuous, Inversion, Conditionals, và Passive Voice.",
        "icon": "✏️",
        "level": "A2-C1",
        "questions": [
            {
                "id": 1001,
                "question_text": "By the time we arrived at the cinema, the movie _____.",
                "question_type": "multiple_choice",
                "options": ["had already started", "already started", "has already started", "was already starting"],
                "correct_answer": "had already started",
                "explanation": "Hành động bộ phim bắt đầu xảy ra trước khi chúng tôi đến (quá khứ) nên dùng Quá khứ hoàn thành (Past Perfect)."
            },
            {
                "id": 1002,
                "question_text": "If she _____ harder for the entrance examination, she would have passed with flying colors.",
                "question_type": "multiple_choice",
                "options": ["had studied", "studied", "has studied", "studies"],
                "correct_answer": "had studied",
                "explanation": "Câu điều kiện loại 3 diễn tả giả định trái ngược với quá khứ: If + S + had + V3/ed."
            },
            {
                "id": 1003,
                "question_text": "Hardly _____ home when the heavy storm began to rage.",
                "question_type": "multiple_choice",
                "options": ["had he arrived", "he had arrived", "did he arrived", "he arrived"],
                "correct_answer": "had he arrived",
                "explanation": "Cấu trúc đảo ngữ: Hardly + had + S + V3/ed + when + S + V2/ed."
            },
            {
                "id": 1004,
                "question_text": "The new environmental protection laws _____ by Parliament next Monday.",
                "question_type": "multiple_choice",
                "options": ["will be passed", "will pass", "are passing", "passed"],
                "correct_answer": "will be passed",
                "explanation": "Bị động ở tương lai đơn: S + will be + V3/ed."
            },
            {
                "id": 1005,
                "question_text": "I suggest that the marketing coordinator _____ a detailed campaign proposal.",
                "question_type": "multiple_choice",
                "options": ["submit", "submits", "submitted", "is submitting"],
                "correct_answer": "submit",
                "explanation": "Thức giả định Subjunctive Mood: suggest that + S + (should) V_bare."
            },
            {
                "id": 1006,
                "question_text": "Neither the teacher nor her students _____ pleased with the sudden schedule change.",
                "question_type": "multiple_choice",
                "options": ["were", "was", "is", "has been"],
                "correct_answer": "were",
                "explanation": "Cấu trúc 'Neither S1 nor S2': động từ chia theo chủ ngữ gần nhất S2 (students là số nhiều -> were)."
            },
            {
                "id": 1007,
                "question_text": "No sooner _____ the contract than the client requested major revisions.",
                "question_type": "multiple_choice",
                "options": ["had we signed", "we had signed", "did we sign", "we signed"],
                "correct_answer": "had we signed",
                "explanation": "Cấu trúc đảo ngữ: No sooner + had + S + V3/ed + than + S + V2/ed."
            },
            {
                "id": 1008,
                "question_text": "The manager insisted that every team member _____ on time for the annual briefing.",
                "question_type": "multiple_choice",
                "options": ["be", "is", "are", "was"],
                "correct_answer": "be",
                "explanation": "Thức giả định: insist that + S + (should) be."
            },
            {
                "id": 1009,
                "question_text": "He talked as if he _____ an expert in artificial intelligence, but he only read one article.",
                "question_type": "multiple_choice",
                "options": ["were", "is", "has been", "would be"],
                "correct_answer": "were",
                "explanation": "Cấu trúc As if / As though diễn tả điều không có thật ở hiện tại dùng 'were'."
            },
            {
                "id": 1010,
                "question_text": "_____ you work diligently every day, you will achieve fluency within six months.",
                "question_type": "multiple_choice",
                "options": ["As long as", "Unless", "Although", "In spite of"],
                "correct_answer": "As long as",
                "explanation": "'As long as' mang nghĩa miễn là, chỉ điều kiện tích cực."
            },
            {
                "id": 1011,
                "question_text": "The athlete avoided _____ with the media prior to the championship match.",
                "question_type": "multiple_choice",
                "options": ["speaking", "to speak", "speak", "having spoke"],
                "correct_answer": "speaking",
                "explanation": "Động từ 'avoid' luôn đi kèm V-ing (avoid doing sth)."
            },
            {
                "id": 1012,
                "question_text": "Under no circumstances _____ allowed to disclose customer confidential data.",
                "question_type": "multiple_choice",
                "options": ["are employees", "employees are", "employees have", "do employees"],
                "correct_answer": "are employees",
                "explanation": "Đảo ngữ với cụm phủ định đứng đầu: Under no circumstances + be + S + V3/ed."
            },
            {
                "id": 1013,
                "question_text": "She had her laptop _____ by a certified Apple technician yesterday.",
                "question_type": "multiple_choice",
                "options": ["repaired", "repairing", "repair", "to repair"],
                "correct_answer": "repaired",
                "explanation": "Cấu trúc sai khiến bị động: Have sth done (V3/ed)."
            },
            {
                "id": 1014,
                "question_text": "It was not until midnight _____ the rescue team finally reached the stranded climbers.",
                "question_type": "multiple_choice",
                "options": ["that", "when", "which", "then"],
                "correct_answer": "that",
                "explanation": "Cấu trúc nhấn mạnh: It was not until + time + that + S + V."
            },
            {
                "id": 1015,
                "question_text": "The more you practice speaking English, _____ confident you become.",
                "question_type": "multiple_choice",
                "options": ["the more", "more", "the most", "most"],
                "correct_answer": "the more",
                "explanation": "Cấu trúc so sánh kép: The more... the more..."
            }
        ]
    },
    "toeic_part5": {
        "title": "💼 TOEIC 850+ Part 5-6 Bẫy Từ Loại & Liên Từ ETS",
        "description": "Luyện phản xạ 5-10 giây mỗi câu với các bẫy ngữ pháp và từ vựng xuất hiện nhiều nhất trong đề thi TOEIC.",
        "icon": "🎯",
        "level": "B1-C1",
        "questions": [
            {
                "id": 1016,
                "question_text": "Ms. Johnson presented a _____ comprehensive financial breakdown to the executive committee.",
                "question_type": "multiple_choice",
                "options": ["remarkably", "remarkable", "remark", "remarking"],
                "correct_answer": "remarkably",
                "explanation": "Cần trạng từ (Adv) để bổ nghĩa cho tính từ 'comprehensive' đứng phía sau -> 'remarkably'."
            },
            {
                "id": 1017,
                "question_text": "Employees seeking reimbursement for travel expenses must submit their receipts _____ 30 days.",
                "question_type": "multiple_choice",
                "options": ["within", "among", "during", "between"],
                "correct_answer": "within",
                "explanation": "'Within 30 days' nghĩa là trong vòng 30 ngày (chỉ khoảng thời gian tối đa để hoàn tất)."
            },
            {
                "id": 1018,
                "question_text": "The software upgrade was suspended _____ unexpected server compatibility issues.",
                "question_type": "multiple_choice",
                "options": ["due to", "because", "even though", "in spite"],
                "correct_answer": "due to",
                "explanation": "'Due to + Noun phrase' mang nghĩa vì, do."
            },
            {
                "id": 1019,
                "question_text": "Neither the department supervisor nor the regional managers _____ notified about the schedule alteration.",
                "question_type": "multiple_choice",
                "options": ["were", "was", "is", "has been"],
                "correct_answer": "were",
                "explanation": "Cấu trúc 'Neither S1 nor S2': động từ chia theo chủ ngữ gần nhất S2 ('regional managers' số nhiều -> 'were')."
            },
            {
                "id": 1020,
                "question_text": "The factory increased its manufacturing output _____ maintaining stringent quality standards.",
                "question_type": "multiple_choice",
                "options": ["while", "during", "despite of", "since"],
                "correct_answer": "while",
                "explanation": "'While + V-ing' mang nghĩa trong khi vẫn đồng thời duy trì tiêu chuẩn."
            },
            {
                "id": 1021,
                "question_text": "All visitors are required to register at the front desk _____ entering the laboratory facilities.",
                "question_type": "multiple_choice",
                "options": ["prior to", "already", "except", "instead"],
                "correct_answer": "prior to",
                "explanation": "'Prior to + V-ing/Noun' mang nghĩa trước khi."
            },
            {
                "id": 1022,
                "question_text": "The board of directors commended Mr. Tanaka for his _____ contributions to corporate expansion.",
                "question_type": "multiple_choice",
                "options": ["exceptional", "exceptionally", "exception", "except"],
                "correct_answer": "exceptional",
                "explanation": "Cần tính từ (Adj) đứng trước danh từ 'contributions' để bổ nghĩa."
            },
            {
                "id": 1023,
                "question_text": "The merger will take effect on July 1st _____ approved by the federal antitrust regulator.",
                "question_type": "multiple_choice",
                "options": ["if", "so", "because", "although"],
                "correct_answer": "if",
                "explanation": "'if approved' là mệnh đề điều kiện rút gọn (if it is approved)."
            },
            {
                "id": 1024,
                "question_text": "Our newly launched CRM system allows sales reps to track client inquiries _____ than before.",
                "question_type": "multiple_choice",
                "options": ["more efficiently", "most efficient", "efficiently", "efficiency"],
                "correct_answer": "more efficiently",
                "explanation": "Cần dạng so sánh hơn của trạng từ bổ nghĩa cho động từ 'track' -> 'more efficiently'."
            },
            {
                "id": 1025,
                "question_text": "The keynote speaker was delayed; _____, the opening presentation proceeded smoothly with a surrogate.",
                "question_type": "multiple_choice",
                "options": ["nevertheless", "furthermore", "consequently", "whereas"],
                "correct_answer": "nevertheless",
                "explanation": "'Nevertheless' (tuy nhiên/dù vậy) nối hai vế tương phản mang nghĩa tích cực."
            },
            {
                "id": 1026,
                "question_text": "The human resources division published a revised handbook outlining workplace _____ guidelines.",
                "question_type": "multiple_choice",
                "options": ["safety", "safely", "safer", "safest"],
                "correct_answer": "safety",
                "explanation": "Cụm danh từ ghép 'workplace safety guidelines' (hướng dẫn an toàn nơi làm việc)."
            },
            {
                "id": 1027,
                "question_text": "Customers who purchase items online are entitled to _____ shipping on orders above $50.",
                "question_type": "multiple_choice",
                "options": ["complimentary", "compliment", "complimenting", "complimented"],
                "correct_answer": "complimentary",
                "explanation": "'Complimentary shipping' = miễn phí vận chuyển (thuật ngữ TOEIC phổ biến)."
            },
            {
                "id": 1028,
                "question_text": "The newly hired architect has demonstrated a high degree of _____ in sustainable design.",
                "question_type": "multiple_choice",
                "options": ["expertise", "expert", "expertly", "expertness"],
                "correct_answer": "expertise",
                "explanation": "Cần danh từ trừu tượng mang nghĩa chuyên môn/sự thành thạo -> 'expertise'."
            },
            {
                "id": 1029,
                "question_text": "Please ensure that the conference hall is _____ ventilated before attendees arrive.",
                "question_type": "multiple_choice",
                "options": ["adequately", "adequate", "adequacy", "more adequate"],
                "correct_answer": "adequately",
                "explanation": "Trạng từ 'adequately' đứng trước phân từ 2 'ventilated' để bổ nghĩa (thông thoáng đầy đủ)."
            },
            {
                "id": 1030,
                "question_text": "The quarterly financial statement will be released to shareholders _____ the audit is concluded.",
                "question_type": "multiple_choice",
                "options": ["as soon as", "as long", "so that", "in order to"],
                "correct_answer": "as soon as",
                "explanation": "'As soon as' là liên từ chỉ thời gian (ngay khi cuộc kiểm toán kết thúc)."
            }
        ]
    },
    "ielts_vocab": {
        "title": "🎓 IELTS Academic Band 8.0+ Lexical Resource",
        "description": "Nâng cấp từ vựng học thuật C1-C2, Paraphrasing và cụm Collocations ăn điểm Task 2.",
        "icon": "🏛️",
        "level": "B2-C2",
        "questions": [
            {
                "id": 1031,
                "question_text": "The rapid proliferation of motorized vehicles has _____ urban traffic congestion.",
                "question_type": "multiple_choice",
                "options": ["exacerbated", "mitigated", "alleviated", "eliminated"],
                "correct_answer": "exacerbated",
                "explanation": "'Exacerbate' là từ vựng C1/C2 mang nghĩa làm trầm trọng thêm vấn đề."
            },
            {
                "id": 1032,
                "question_text": "Investing in early childhood education yields _____ long-term socioeconomic benefits.",
                "question_type": "multiple_choice",
                "options": ["substantial", "negligible", "tentative", "meager"],
                "correct_answer": "substantial",
                "explanation": "'Substantial benefits' nghĩa là những lợi ích to lớn, đáng kể."
            },
            {
                "id": 1033,
                "question_text": "Renewable energy infrastructure is considered _____ in mitigating the climate crisis.",
                "question_type": "multiple_choice",
                "options": ["indispensable", "redundant", "dispensable", "superfluous"],
                "correct_answer": "indispensable",
                "explanation": "'Indispensable' mang nghĩa tối quan trọng, không thể thiếu."
            },
            {
                "id": 1034,
                "question_text": "Opponents contend that excessive surveillance constitutes an unwarranted _____ on personal privacy.",
                "question_type": "multiple_choice",
                "options": ["infringement", "enhancement", "embellishment", "adherence"],
                "correct_answer": "infringement",
                "explanation": "'Infringement on privacy' mang nghĩa sự xâm phạm quyền riêng tư."
            },
            {
                "id": 1035,
                "question_text": "The phenomenon of cultural globalization is thought to have an _____ effect on indigenous languages.",
                "question_type": "multiple_choice",
                "options": ["insidious", "innocuous", "auspicious", "exhilarating"],
                "correct_answer": "insidious",
                "explanation": "'Insidious' (ngấm ngầm nguy hại) diễn tả tác động tiêu cực tiềm tàng."
            },
            {
                "id": 1036,
                "question_text": "Technological automation has led to the _____ of several manual labor occupations.",
                "question_type": "multiple_choice",
                "options": ["obsolescence", "perpetuation", "rejuvenation", "flourishing"],
                "correct_answer": "obsolescence",
                "explanation": "'Obsolescence' mang nghĩa sự lỗi thời, bị đào thải."
            },
            {
                "id": 1037,
                "question_text": "Government initiatives should aim to _____ the disparity between affluent and marginalized sectors.",
                "question_type": "multiple_choice",
                "options": ["bridge", "widen", "compound", "perpetuate"],
                "correct_answer": "bridge",
                "explanation": "'Bridge the disparity / gap' là collocation kinh điển mang nghĩa thu hẹp khoảng cách."
            },
            {
                "id": 1038,
                "question_text": "The empirical findings provide _____ evidence supporting the neuroplasticity hypothesis.",
                "question_type": "multiple_choice",
                "options": ["compelling", "dubious", "feeble", "speculative"],
                "correct_answer": "compelling",
                "explanation": "'Compelling evidence' nghĩa là bằng chứng thuyết phục, rõ ràng."
            },
            {
                "id": 1039,
                "question_text": "Many developing nations are increasingly _____ on foreign aid to maintain stability.",
                "question_type": "multiple_choice",
                "options": ["reliant", "autonomous", "sovereign", "immune"],
                "correct_answer": "reliant",
                "explanation": "'Reliant on' mang nghĩa phụ thuộc vào."
            },
            {
                "id": 1040,
                "question_text": "A comprehensive overhaul of the taxation regime is _____ to foster entrepreneurial growth.",
                "question_type": "multiple_choice",
                "options": ["imperative", "futile", "trivial", "dispensable"],
                "correct_answer": "imperative",
                "explanation": "'Imperative' (cấp bách/tất yếu) thường gặp trong bài luận IELTS Writing Task 2."
            },
            {
                "id": 1041,
                "question_text": "The preservation of historical monuments serves to foster a profound sense of cultural _____.",
                "question_type": "multiple_choice",
                "options": ["identity", "alienation", "apathy", "anonymity"],
                "correct_answer": "identity",
                "explanation": "'Cultural identity' là bản sắc văn hóa."
            },
            {
                "id": 1042,
                "question_text": "Urban sprawls often lead to the _____ depletion of natural flora and fauna habitats.",
                "question_type": "multiple_choice",
                "options": ["irreversible", "recoverable", "fleeting", "transitory"],
                "correct_answer": "irreversible",
                "explanation": "'Irreversible depletion' là sự cạn kiệt không thể đảo ngược."
            },
            {
                "id": 1043,
                "question_text": "Educators must strive to _____ critical thinking faculties rather than rote memorization.",
                "question_type": "multiple_choice",
                "options": ["nurture", "suppress", "dampen", "obstruct"],
                "correct_answer": "nurture",
                "explanation": "'Nurture faculties' là nuôi dưỡng, trau dồi năng lực."
            },
            {
                "id": 1044,
                "question_text": "Scientific consensus suggests that greenhouse gas emissions act as the primary _____ of global warming.",
                "question_type": "multiple_choice",
                "options": ["catalyst", "byproduct", "deterrent", "impediment"],
                "correct_answer": "catalyst",
                "explanation": "'Catalyst' (chất xúc tác/nguyên nhân thúc đẩy)."
            },
            {
                "id": 1045,
                "question_text": "The curriculum should be adapted to _____ the evolving demands of the modern knowledge economy.",
                "question_type": "multiple_choice",
                "options": ["accommodate", "disregard", "repudiate", "bypass"],
                "correct_answer": "accommodate",
                "explanation": "'Accommodate demands' mang nghĩa đáp ứng các yêu cầu phát triển."
            }
        ]
    },
    "business_comm": {
        "title": "🤝 Tiếng Anh Doanh Nghiệp & Đàm Phán Thương Mại (Business)",
        "description": "Thực hành các tình huống giao tiếp đàm phán, email chuyên nghiệp và xử lý từ chối khéo léo.",
        "icon": "🏢",
        "level": "B1-C1",
        "questions": [
            {
                "id": 1046,
                "question_text": "We would be pleased to proceed with the contract, _____ that you can expedite delivery to 15 days.",
                "question_type": "multiple_choice",
                "options": ["provided", "supposing", "unless", "in case of"],
                "correct_answer": "provided",
                "explanation": "'Provided that' (với điều kiện là) là mẫu câu đàm phán thương mại chuẩn mực."
            },
            {
                "id": 1047,
                "question_text": "Please find _____ the non-disclosure agreement for your review and signature.",
                "question_type": "multiple_choice",
                "options": ["attached", "attaching", "attachment", "to attach"],
                "correct_answer": "attached",
                "explanation": "'Please find attached...' là cấu trúc thư từ kinh doanh phổ biến nhất."
            },
            {
                "id": 1048,
                "question_text": "Our proprietary machine learning algorithm grants us substantial market _____ over competitors.",
                "question_type": "multiple_choice",
                "options": ["leverage", "reluctance", "stagnation", "hesitation"],
                "correct_answer": "leverage",
                "explanation": "'Market leverage' mang nghĩa đòn bẩy/ưu thế cạnh tranh trên thị trường."
            },
            {
                "id": 1049,
                "question_text": "During the merger talks, both parties reached a mutually beneficial _____ regarding intellectual property rights.",
                "question_type": "multiple_choice",
                "options": ["compromise", "conflict", "impasse", "stalemate"],
                "correct_answer": "compromise",
                "explanation": "'Reach a compromise' là đạt được sự thỏa thuận/nhượng bộ đôi bên cùng có lợi."
            },
            {
                "id": 1050,
                "question_text": "Could you please _____ me in on what was discussed at yesterday's executive strategy session?",
                "question_type": "multiple_choice",
                "options": ["fill", "put", "let", "bring"],
                "correct_answer": "fill",
                "explanation": "'Fill someone in on something' là cập nhật thông tin chi tiết cho ai đó."
            },
            {
                "id": 1051,
                "question_text": "We regret to inform you that our budget constraints prevent us from _____ your sponsorship proposal at this time.",
                "question_type": "multiple_choice",
                "options": ["accommodating", "refusing", "discarding", "abolishing"],
                "correct_answer": "accommodating",
                "explanation": "'Accommodate a proposal' là chấp thuận/đáp ứng đề xuất."
            },
            {
                "id": 1052,
                "question_text": "I am writing to _____ about the current status of our invoice number #48291.",
                "question_type": "multiple_choice",
                "options": ["inquire", "require", "acquire", "inspire"],
                "correct_answer": "inquire",
                "explanation": "'Inquire about' mang nghĩa hỏi thăm/yêu cầu thông tin lịch sự trong email."
            },
            {
                "id": 1053,
                "question_text": "The CFO emphasized the importance of maintaining positive operating cash _____ throughout Q3.",
                "question_type": "multiple_choice",
                "options": ["flow", "flood", "stream", "current"],
                "correct_answer": "flow",
                "explanation": "'Cash flow' là dòng tiền trong doanh nghiệp."
            },
            {
                "id": 1054,
                "question_text": "Let us _____ this discussion until we have obtained exact figures from the audit department.",
                "question_type": "multiple_choice",
                "options": ["table", "shelf", "drawer", "chair"],
                "correct_answer": "table",
                "explanation": "'Table a discussion/motion' (trong tiếng Anh Mỹ) là tạm hoãn thảo luận sang lần sau."
            },
            {
                "id": 1055,
                "question_text": "Our primary objective is to streamline supply chain logistics and reduce operational _____.",
                "question_type": "multiple_choice",
                "options": ["overhead", "overload", "overtake", "overlook"],
                "correct_answer": "overhead",
                "explanation": "'Operational overhead' là chi phí vận hành chung của công ty."
            }
        ]
    },
    "idioms_phrasal": {
        "title": "💡 Thành Ngữ & Cụm Động Từ (Idioms & Phrasal Verbs)",
        "description": "Học cách sử dụng thành ngữ tự nhiên như người bản xứ trong giao tiếp hàng ngày.",
        "icon": "✨",
        "level": "A2-B2",
        "questions": [
            {
                "id": 1056,
                "question_text": "The opening joke by the host helped to _____ and made the audience feel at ease.",
                "question_type": "multiple_choice",
                "options": ["break the ice", "hit the roof", "spill the beans", "bite the bullet"],
                "correct_answer": "break the ice",
                "explanation": "'Break the ice' là thành ngữ mang nghĩa phá vỡ bầu không khí ngượng ngùng lúc đầu."
            },
            {
                "id": 1057,
                "question_text": "I have a crucial exam tomorrow morning, so I definitely need to _____ tonight.",
                "question_type": "multiple_choice",
                "options": ["hit the books", "cost an arm and a leg", "see eye to eye", "burn the candle"],
                "correct_answer": "hit the books",
                "explanation": "'Hit the books' là thành ngữ nghĩa là vùi đầu vào học tập."
            },
            {
                "id": 1058,
                "question_text": "We had to _____ our weekend camping trip due to the unexpected torrential downpour.",
                "question_type": "multiple_choice",
                "options": ["call off", "put off", "look up to", "bring about"],
                "correct_answer": "call off",
                "explanation": "'Call off' mang nghĩa hủy bỏ hoàn toàn chuyến đi."
            },
            {
                "id": 1059,
                "question_text": "Don't worry about the minor mistake; there is no point crying over spilled _____.",
                "question_type": "multiple_choice",
                "options": ["milk", "water", "tea", "coffee"],
                "correct_answer": "milk",
                "explanation": "Thành ngữ: 'Cry over spilled milk' (tiếc rẻ chuyện đã rồi)."
            },
            {
                "id": 1060,
                "question_text": "It took him several months to _____ the loss of his beloved golden retriever.",
                "question_type": "multiple_choice",
                "options": ["get over", "get by", "get away", "get through"],
                "correct_answer": "get over",
                "explanation": "'Get over' nghĩa là vượt qua nỗi buồn hoặc sự mất mát."
            },
            {
                "id": 1061,
                "question_text": "Keep your secret safe; please make sure nobody _____ before tomorrow's surprise party.",
                "question_type": "multiple_choice",
                "options": ["spills the beans", "kicks the bucket", "bites the dust", "burns bridges"],
                "correct_answer": "spills the beans",
                "explanation": "'Spill the beans' nghĩa là vô tình hay cố ý tiết lộ bí mật."
            },
            {
                "id": 1062,
                "question_text": "The cutting-edge VR gaming setup cost him an arm and a _____.",
                "question_type": "multiple_choice",
                "options": ["leg", "hand", "foot", "head"],
                "correct_answer": "leg",
                "explanation": "Thành ngữ 'Cost an arm and a leg' nghĩa là vô cùng đắt đỏ."
            },
            {
                "id": 1063,
                "question_text": "You should _____ on sugary snacks if you want to enhance your physical stamina.",
                "question_type": "multiple_choice",
                "options": ["cut down", "cut out", "cut through", "cut across"],
                "correct_answer": "cut down",
                "explanation": "'Cut down on sth' là cắt giảm lượng tiêu thụ."
            },
            {
                "id": 1064,
                "question_text": "He always looks _____ his elder sister for insightful career advice.",
                "question_type": "multiple_choice",
                "options": ["up to", "down on", "forward to", "out for"],
                "correct_answer": "up to",
                "explanation": "'Look up to someone' là kính trọng, noi gương ai đó."
            },
            {
                "id": 1065,
                "question_text": "When the project was in danger of failing, the entire team decided to bite the _____ and work over the weekend.",
                "question_type": "multiple_choice",
                "options": ["bullet", "apple", "nail", "coin"],
                "correct_answer": "bullet",
                "explanation": "'Bite the bullet' là cắn răng chịu đựng, đương đầu với khó khăn."
            }
        ]
    },
    "error_identification": {
        "title": "🔍 Luyện Kỹ Năng Tìm Lỗi Sai Ngữ Pháp (Error Detection)",
        "description": "Phát hiện nhanh các lỗi hòa hợp chủ vị, sai giới từ, từ loại và mệnh đề quan hệ.",
        "icon": "🔬",
        "level": "B1-B2",
        "questions": [
            {
                "id": 1066,
                "question_text": "Tìm phần gạch chân sai: 'Every student [A: in] the class [B: are] required to submit [C: their] assignment on [D: Friday].'",
                "question_type": "multiple_choice",
                "options": ["in", "are", "their", "Friday"],
                "correct_answer": "are",
                "explanation": "'Every student' là chủ ngữ số ít, động từ to be phải là 'is' thay vì 'are'."
            },
            {
                "id": 1067,
                "question_text": "Tìm phần gạch chân sai: 'She is [A: capable to] [B: speaking] four foreign [C: languages] [D: fluently].'",
                "question_type": "multiple_choice",
                "options": ["capable to", "speaking", "languages", "fluently"],
                "correct_answer": "capable to",
                "explanation": "Cấu trúc đúng là 'capable of + V-ing', không dùng 'capable to'."
            },
            {
                "id": 1068,
                "question_text": "Tìm phần gạch chân sai: 'Despite [A: of the] heavy traffic, he managed [B: to arrive] at the international airport [C: in time] for his [D: departure].'",
                "question_type": "multiple_choice",
                "options": ["of the", "to arrive", "in time", "departure"],
                "correct_answer": "of the",
                "explanation": "'Despite' đi trực tiếp với danh từ, không có 'of' (chỉ 'In spite of' mới có 'of')."
            },
            {
                "id": 1069,
                "question_text": "Tìm phần gạch chân sai: 'The number of [A: participants] in the online webinar [B: have] increased [C: dramatically] over the [D: past week].'",
                "question_type": "multiple_choice",
                "options": ["participants", "have", "dramatically", "past week"],
                "correct_answer": "have",
                "explanation": "Cụm 'The number of + N số nhiều' chia động từ số ít -> phải đổi 'have' thành 'has'."
            },
            {
                "id": 1070,
                "question_text": "Tìm phần gạch chân sai: 'She [A: suggested me] [B: to apply] for the software engineering [C: position] at Google [D: immediately].'",
                "question_type": "multiple_choice",
                "options": ["suggested me", "to apply", "position", "immediately"],
                "correct_answer": "suggested me",
                "explanation": "Cấu trúc 'suggest' không đi với tân ngữ người trực tiếp như 'suggested me', mà dùng 'suggested that I apply' hoặc 'suggested applying'."
            },
            {
                "id": 1071,
                "question_text": "Tìm phần gạch chân sai: 'Neither the [A: chief executive] nor the board [B: members] [C: was] convinced by the [D: proposed strategy].'",
                "question_type": "multiple_choice",
                "options": ["chief executive", "members", "was", "proposed strategy"],
                "correct_answer": "was",
                "explanation": "Chủ ngữ gần nhất là 'board members' (số nhiều) nên động từ phải là 'were' thay vì 'was'."
            },
            {
                "id": 1072,
                "question_text": "Tìm phần gạch chân sai: 'He worked [A: hardly] all night [B: in order to] finish the quarterly report [C: before] the morning [D: deadline].'",
                "question_type": "multiple_choice",
                "options": ["hardly", "in order to", "before", "deadline"],
                "correct_answer": "hardly",
                "explanation": "'Hardly' mang nghĩa hiếm khi/hầu như không. Làm việc chăm chỉ phải dùng 'hard' (He worked hard all night)."
            },
            {
                "id": 1073,
                "question_text": "Tìm phần gạch chân sai: 'The teacher made all [A: the students] [B: to rewrite] their essays [C: because of] excessive spelling [D: errors].'",
                "question_type": "multiple_choice",
                "options": ["the students", "to rewrite", "because of", "errors"],
                "correct_answer": "to rewrite",
                "explanation": "Cấu trúc sai khiến: Make + someone + V-bare (không có 'to'). Do đó sửa 'to rewrite' thành 'rewrite'."
            },
            {
                "id": 1074,
                "question_text": "Tìm phần gạch chân sai: 'If I [A: knew] about your flight arrival [B: yesterday], I [C: would have picked] you up at the airport [D: terminal].'",
                "question_type": "multiple_choice",
                "options": ["knew", "yesterday", "would have picked", "terminal"],
                "correct_answer": "knew",
                "explanation": "Sự việc xảy ra trong quá khứ (yesterday) nên vế IF phải dùng điều kiện loại 3: 'had known' thay vì 'knew'."
            },
            {
                "id": 1075,
                "question_text": "Tìm phần gạch chân sai: 'She is [A: one of the most] intelligent [B: student] [C: that I have] ever taught in my [D: career].'",
                "question_type": "multiple_choice",
                "options": ["one of the most", "student", "that I have", "career"],
                "correct_answer": "student",
                "explanation": "Cấu trúc 'One of the + N số nhiều' -> sửa 'student' thành 'students'."
            }
        ]
    }
}

@router.get("/curated-bank")
async def get_curated_quiz_bank():
    """Lấy danh sách các chủ đề luyện tập mẫu đa dạng có sẵn."""
    return {"categories": CURATED_QUIZ_BANK}

@router.get("/category/{cat_id}")
async def get_quiz_category(cat_id: str):
    """Lấy bộ câu hỏi theo danh mục tuyển chọn."""
    cat = CURATED_QUIZ_BANK.get(cat_id)
    if not cat:
        return {"error": "Category not found"}
    return {
        "id": cat_id,
        "title": cat["title"],
        "description": cat["description"],
        "icon": cat["icon"],
        "level": cat["level"],
        "questions": cat["questions"]
    }

@router.post("/generate")
async def generate_quiz(
    req: QuizGenRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """AI tạo bộ câu hỏi quiz."""
    questions = await ai_engine.generate_quiz(
        skill=req.skill, level=req.level,
        topic=req.topic, count=req.count,
        types=req.question_types
    )

    # Save to DB
    saved = []
    for q in questions:
        qq = QuizQuestion(
            question_text=q.get("question_text", ""),
            question_type=q.get("question_type", "multiple_choice"),
            options=q.get("options", []),
            correct_answer=q.get("correct_answer", ""),
            explanation=q.get("explanation", ""),
            skill=req.skill, level=req.level,
            topic=req.topic, is_ai_generated=True
        )
        db.add(qq)
        await db.flush()
        saved.append({
            "id": qq.id,
            "question_text": qq.question_text,
            "question_type": qq.question_type,
            "options": qq.options,
            "skill": qq.skill, "level": qq.level,
        })
    await db.commit()
    return {"questions": saved, "count": len(saved), "skill": req.skill}


@router.post("/submit", response_model=QuizResult)
async def submit_answer(
    data: QuizSubmit,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Nộp câu trả lời và nhận kết quả."""
    r = await db.execute(select(QuizQuestion).where(QuizQuestion.id == data.question_id))
    q = r.scalar_one_or_none()
    if not q:
        return QuizResult(question_id=data.question_id, is_correct=False,
                          correct_answer="", explanation="Câu hỏi không tồn tại", xp_earned=0)

    is_correct = data.user_answer.strip().lower() == q.correct_answer.strip().lower()
    xp = gamification_service.calculate_xp_reward("quiz_correct") if is_correct else 0

    # Save attempt
    attempt = UserQuizAttempt(
        user_id=current_user.id, question_id=q.id,
        user_answer=data.user_answer, is_correct=is_correct,
        time_taken_sec=data.time_taken_sec, xp_earned=xp
    )
    db.add(attempt)
    current_user.xp += xp
    await db.commit()

    return QuizResult(
        question_id=q.id, is_correct=is_correct,
        correct_answer=q.correct_answer, explanation=q.explanation, xp_earned=xp
    )


@router.post("/submit-batch")
async def submit_batch(
    answers: List[QuizSubmit],
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Nộp nhiều câu trả lời cùng lúc."""
    results = []
    total_xp = 0
    correct_count = 0

    for ans in answers:
        r = await db.execute(select(QuizQuestion).where(QuizQuestion.id == ans.question_id))
        q = r.scalar_one_or_none()
        if not q:
            continue

        is_correct = ans.user_answer.strip().lower() == q.correct_answer.strip().lower()
        xp = 10 if is_correct else 0
        total_xp += xp
        if is_correct:
            correct_count += 1

        attempt = UserQuizAttempt(user_id=current_user.id, question_id=q.id,
                                   user_answer=ans.user_answer, is_correct=is_correct,
                                   time_taken_sec=ans.time_taken_sec, xp_earned=xp)
        db.add(attempt)
        results.append({"question_id": q.id, "is_correct": is_correct,
                         "correct_answer": q.correct_answer, "explanation": q.explanation})

    # Save session
    score = correct_count / len(answers) * 10 if answers else 0
    session = StudySession(user_id=current_user.id, session_type="quiz",
                            score=score, xp_earned=total_xp,
                            details={"total": len(answers), "correct": correct_count})
    db.add(session)
    current_user.xp += total_xp
    await db.commit()

    return {
        "results": results, "score": round(score, 1),
        "correct": correct_count, "total": len(answers),
        "xp_earned": total_xp,
        "percentage": round(correct_count / len(answers) * 100, 1) if answers else 0
    }


@router.get("/history")
async def quiz_history(
    limit: int = 20,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    r = await db.execute(
        select(UserQuizAttempt, QuizQuestion)
        .join(QuizQuestion)
        .where(UserQuizAttempt.user_id == current_user.id)
        .order_by(UserQuizAttempt.attempted_at.desc())
        .limit(limit)
    )
    rows = r.all()
    return [{
        "question": a.question_text, "user_answer": ua.user_answer,
        "correct_answer": a.correct_answer, "is_correct": ua.is_correct,
        "xp_earned": ua.xp_earned, "attempted_at": ua.attempted_at
    } for ua, a in rows]


from scripts.seed_50_quiz_topics import QUIZ_50_TOPICS_METADATA

@router.get("/topics-50-meta")
async def get_50_quiz_topics_meta(
    category: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Trả về danh mục 50 Chủ đề Bài tập & Quiz kèm tiến độ người học."""
    # Count questions per topic in DB
    from sqlalchemy import func
    q_counts = await db.execute(
        select(QuizQuestion.topic, func.count(QuizQuestion.id))
        .where(QuizQuestion.topic.isnot(None))
        .group_by(QuizQuestion.topic)
    )
    counts_map = dict(q_counts.all())

    topics = []
    for t in QUIZ_50_TOPICS_METADATA:
        if category and category != 'ALL' and t["category"].lower() != category.lower():
            continue
        total_q = counts_map.get(t["name"], t["count"])
        topics.append({
            "id": t["id"],
            "name": t["name"],
            "category": t["category"],
            "icon": t["icon"],
            "color": t["color"],
            "description": t["desc"],
            "total_questions": total_q
        })

    return {"topics": topics, "total": len(topics)}


@router.get("/topic-questions/{topic_name}")
async def get_topic_questions(
    topic_name: str,
    limit: int = 30,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Lấy danh sách 20-30 câu hỏi theo chủ đề."""
    r = await db.execute(
        select(QuizQuestion)
        .where(QuizQuestion.topic == topic_name)
        .order_by(QuizQuestion.id.asc())
        .limit(limit)
    )
    items = r.scalars().all()
    questions = []
    for q in items:
        opts = q.options if isinstance(q.options, list) else (json.loads(q.options) if isinstance(q.options, str) else [])
        questions.append({
            "id": q.id,
            "question": q.question_text,
            "question_type": q.question_type or "multiple_choice",
            "options": opts,
            "correct_answer": q.correct_answer,
            "explanation": q.explanation,
            "level": q.level or "B1",
            "topic": q.topic
        })
    return {"topic": topic_name, "questions": questions, "total": len(questions)}
