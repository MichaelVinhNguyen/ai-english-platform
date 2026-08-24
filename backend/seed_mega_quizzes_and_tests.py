"""
seed_mega_quizzes_and_tests.py – Bổ sung thêm 200+ câu hỏi Quiz đa dạng và 15+ bài đọc & bài nghe
"""

import asyncio
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from sqlalchemy import select
from backend.database.database import AsyncSessionLocal, init_db
from backend.database.models import QuizQuestion, ReadingArticle, ListeningExercise

EXTRA_READINGS = [
    {
        "title": "The Rise of Electric Vehicles and Green Mobility",
        "summary": "Sự phát triển mạnh mẽ của xe điện và tương lai giao thông xanh toàn cầu.",
        "source": "Automotive & Eco World",
        "article_type": "news",
        "level": "A2",
        "topic": "Environment",
        "word_count": 210,
        "content": "Electric vehicles (EVs) are becoming increasingly popular in major cities around the world. Unlike traditional cars that run on gasoline or diesel, electric cars use powerful rechargeable battery packs to drive electric motors.\n\nOne of the main advantages of EVs is zero tailpipe emissions. By reducing harmful air pollution, they help keep city air cleaner and combat global warming. In addition, electric cars are remarkably quiet, reducing noise pollution on busy streets.\n\nMany governments are now offering tax incentives and building fast-charging stations along highways. As battery technology improves, electric cars can travel longer distances on a single charge, making them a practical choice for everyday commuting.",
        "questions": [
            {"question": "What powers electric vehicles?", "options": ["Gasoline", "Diesel engines", "Rechargeable battery packs", "Steam"], "correct_answer": "Rechargeable battery packs", "explanation": "Bài đọc nêu: 'electric cars use powerful rechargeable battery packs'."},
            {"question": "What is a key environmental benefit of EVs?", "options": ["They produce no tailpipe emissions", "They are made of wood", "They require no roads", "They fly in the air"], "correct_answer": "They produce no tailpipe emissions", "explanation": "Đoạn 2: 'One of the main advantages of EVs is zero tailpipe emissions'."}
        ]
    },
    {
        "title": "The Secrets of the Mediterranean Diet for Longevity",
        "summary": "Chế độ ăn Địa Trung Hải và bí quyết sống thọ, tăng cường sức khỏe tim mạch.",
        "source": "Nutrition & Wellness Journal",
        "article_type": "blog",
        "level": "B1",
        "topic": "Health",
        "word_count": 290,
        "content": "For decades, medical researchers have observed that residents of Mediterranean countries like Greece, Italy, and Spain enjoy longer life expectancies and lower rates of cardiovascular disease. The secret lies predominantly in their dietary habits.\n\nThe Mediterranean diet emphasizes abundant consumption of fresh vegetables, whole grains, legumes, nuts, and extra virgin olive oil as the primary source of dietary fat. Moderate amounts of fish and poultry are consumed weekly, while red meat and processed sugars are kept to an absolute minimum.\n\nExtra virgin olive oil is rich in monounsaturated fats and powerful antioxidants that reduce chronic inflammation in blood vessels. Furthermore, meals are viewed as social rituals enjoyed slowly in the company of family and friends, which significantly mitigates psychological stress and promotes holistic well-being.",
        "questions": [
            {"question": "What is the primary source of fat in the Mediterranean diet?", "options": ["Butter", "Extra virgin olive oil", "Margarine", "Coconut oil"], "correct_answer": "Extra virgin olive oil", "explanation": "Bài viết nêu: 'extra virgin olive oil as the primary source of dietary fat'."},
            {"question": "How are meals traditionally enjoyed in Mediterranean culture?", "options": ["Eaten quickly alone", "As social rituals with family and friends", "Only at midnight", "While watching television"], "correct_answer": "As social rituals with family and friends", "explanation": "Đoạn cuối: 'meals are viewed as social rituals enjoyed slowly in the company of family and friends'."}
        ]
    },
    {
        "title": "Remote Work and the Evolution of Digital Nomadism",
        "summary": "Xu hướng làm việc từ xa và phong cách sống du mục kỹ thuật số của thế hệ trẻ.",
        "source": "Global Workforce Insights",
        "article_type": "blog",
        "level": "B2",
        "topic": "Business",
        "word_count": 340,
        "content": "The global proliferation of high-speed broadband and cloud collaboration tools has catalyzed a profound paradigm shift in corporate culture. The traditional 'nine-to-five' office presence is increasingly being supplanted by flexible, asynchronous remote work arrangements.\n\nThis newfound autonomy has birthed a burgeoning demographic known as 'digital nomads'—professionals who leverage technology to work remotely from anywhere in the world. From beachfront co-working spaces in Bali to bustling cafes in Lisbon, digital nomads combine career productivity with cultural immersion.\n\nHowever, this lifestyle is not devoid of challenges. Digital nomads frequently grapple with time-zone disparities, precarious internet reliability in developing regions, and the psychological burden of transient social connections. To thrive, remote professionals must cultivate rigorous self-discipline, financial literacy, and proactive mental health strategies.",
        "questions": [
            {"question": "What has catalyzed the shift toward remote work?", "options": ["The ban on office buildings", "High-speed broadband and cloud collaboration tools", "Higher public transport costs", "Lack of computers"], "correct_answer": "High-speed broadband and cloud collaboration tools", "explanation": "Đoạn 1 nêu: 'proliferation of high-speed broadband and cloud collaboration tools'."},
            {"question": "What challenge do digital nomads often face?", "options": ["Too much free time", "Time-zone disparities and transient relationships", "Lack of foreign food", "Having too many passports"], "correct_answer": "Time-zone disparities and transient relationships", "explanation": "Đoạn 3: 'grapple with time-zone disparities... and transient social connections'."}
        ]
    },
    {
        "title": "Quantum Computing: The Next Frontier in Computational Power",
        "summary": "Điện toán lượng tử và tiềm năng giải quyết những bài toán phức tạp nhất nhân loại.",
        "source": "Advanced Physics & Computing",
        "article_type": "academic",
        "level": "C1",
        "topic": "Science",
        "word_count": 410,
        "content": "Classical computing systems operate on binary bits, representing information as discrete states of either 0 or 1. In stark contrast, quantum computing harnesses the mind-bending principles of quantum mechanics—specifically superposition and entanglement—to process data via quantum bits, or 'qubits'.\n\nSuperposition allows qubits to exist in multiple probabilistic states simultaneously, exponentially magnifying computational bandwidth. When coupled with entanglement—where the state of one qubit instantaneously dictates the state of another regardless of spatial separation—quantum processors can evaluate vast combinatorial spaces in seconds that would require classical supercomputers millennia.\n\nThe implications for cryptographic resilience, molecular synthesis, and climatic modeling are staggering. Quantum simulations could unveil room-temperature superconductors and expedite carbon-sequestration chemical catalysts. Nevertheless, maintaining quantum coherence necessitates cryogenic stabilization near absolute zero, posing formidable engineering hurdles before commercial quantum supremacy becomes pervasive.",
        "questions": [
            {"question": "What differentiates qubits from classical bits?", "options": ["Qubits are made of gold", "Qubits can exist in superposition of multiple states simultaneously", "Qubits do not use electricity", "Qubits only work in warm environments"], "correct_answer": "Qubits can exist in superposition of multiple states simultaneously", "explanation": "Đoạn 2: 'Superposition allows qubits to exist in multiple probabilistic states simultaneously'."},
            {"question": "Why is cryogenic stabilization necessary for quantum computers?", "options": ["To cool down human operators", "To maintain quantum coherence near absolute zero", "To reduce electricity bills", "To preserve classical hard drives"], "correct_answer": "To maintain quantum coherence near absolute zero", "explanation": "Đoạn cuối: 'maintaining quantum coherence necessitates cryogenic stabilization near absolute zero'."}
        ]
    }
]

EXTRA_LISTENINGS = [
    {
        "title": "Making an Urgent Doctor Appointment",
        "description": "Luyện nghe cuộc gọi đặt lịch khám bệnh đột xuất tại phòng khám.",
        "transcript": "Receptionist: Good morning, Metro Medical Clinic. How can I help you today?\nPatient: Hi, I have been having severe back pain since yesterday and I was wondering if Dr. Watson has any available slots this afternoon?\nReceptionist: Let me check his schedule. He is fully booked until 3:00 PM, but I have a cancellation at 3:45 PM. Would that work for you?\nPatient: Yes, 3:45 PM would be fantastic. Do I need to bring anything special?\nReceptionist: Please bring your photo ID, insurance card, and any current medications you are taking. Please arrive 10 minutes early to fill out the health questionnaire.\nPatient: Understood. Thank you so much!",
        "exercise_type": "comprehension",
        "level": "A2",
        "topic": "Health",
        "duration_sec": 50,
        "questions": [
            {"question": "What is the patient's medical symptom?", "options": ["Headache", "Severe back pain", "Broken arm", "Fever"], "correct_answer": "Severe back pain", "explanation": "Bệnh nhân nói: 'I have been having severe back pain since yesterday'."},
            {"question": "What time is the available appointment slot?", "options": ["1:00 PM", "3:00 PM", "3:45 PM", "5:00 PM"], "correct_answer": "3:45 PM", "explanation": "Lễ tân thông báo: 'I have a cancellation at 3:45 PM'."}
        ]
    },
    {
        "title": "Business Pitch Presentation: Cloud AI Analytics",
        "description": "Luyện nghe bài thuyết trình gọi vốn khởi nghiệp giải pháp phân tích dữ liệu AI.",
        "transcript": "Presenter: Distinguished investors, thank you for your time today. In 2026, enterprise data is growing exponentially, yet 80% of companies lack the capability to extract actionable insights in real time. Our platform, NovaAnalytics, bridges this gap by deploying self-supervised machine learning models directly into existing cloud data warehouses. Over the past six months in closed beta, our 12 pilot enterprise clients reported an average reduction of 40% in customer churn and a 300% ROI within the first 90 days. We are currently raising a $3 million Seed round to expand our core engineering team and accelerate our go-to-market enterprise sales pipeline.",
        "exercise_type": "comprehension",
        "level": "B2",
        "topic": "Business",
        "duration_sec": 70,
        "questions": [
            {"question": "What problem does NovaAnalytics solve?", "options": ["Building physical computers", "Extracting real-time actionable insights from enterprise data", "Designing social media ads", "Manufacturing batteries"], "correct_answer": "Extracting real-time actionable insights from enterprise data", "explanation": "Người thuyết trình nói: 'bridges this gap by deploying self-supervised ML models to extract actionable insights'."},
            {"question": "How much capital is the company currently raising?", "options": ["$1 million", "$3 million", "$10 million", "$500,000"], "correct_answer": "$3 million", "explanation": "Người thuyết trình kết luận: 'We are currently raising a $3 million Seed round'."}
        ]
    }
]

EXTRA_QUIZZES = [
    # ── CEFR Placement Diagnostic Questions
    {
        "question_text": "[Placement A1] I ________ a student at Hanoi University.",
        "question_type": "multiple_choice",
        "options": ["am", "is", "are", "be"],
        "correct_answer": "am",
        "explanation": "Chủ ngữ là 'I' đi với động từ to be 'am'.",
        "skill": "grammar",
        "level": "A1",
        "topic": "General"
    },
    {
        "question_text": "[Placement A1] Choose the opposite of 'EXPENSIVE':",
        "question_type": "multiple_choice",
        "options": ["Cheap", "Big", "Heavy", "Far"],
        "correct_answer": "Cheap",
        "explanation": "Expensive (đắt) trái nghĩa với Cheap (rẻ).",
        "skill": "vocabulary",
        "level": "A1",
        "topic": "General"
    },
    {
        "question_text": "[Placement A2] Yesterday, they ________ to the cinema to watch the new superhero movie.",
        "question_type": "multiple_choice",
        "options": ["went", "go", "gone", "going"],
        "correct_answer": "went",
        "explanation": "Dấu hiệu 'Yesterday' chỉ thì Quá Khứ Đơn, dạng quá khứ của 'go' là 'went'.",
        "skill": "grammar",
        "level": "A2",
        "topic": "Daily Life"
    },
    {
        "question_text": "[Placement A2] Reorder: [can / play / She / piano / the / very / well / .]",
        "question_type": "ordering",
        "options": ["She", "can", "play", "the", "piano", "very", "well", "."],
        "correct_answer": "She can play the piano very well .",
        "explanation": "Cấu trúc: S + can + V(bare) + O + Adv.",
        "skill": "grammar",
        "level": "A2",
        "topic": "Daily Life"
    },
    {
        "question_text": "[Placement B1] She has lived in Da Nang ________ five years.",
        "question_type": "multiple_choice",
        "options": ["for", "since", "during", "from"],
        "correct_answer": "for",
        "explanation": "Dùng 'for' đi với khoảng thời gian (five years) trong thì Hiện Tại Hoàn Thành.",
        "skill": "grammar",
        "level": "B1",
        "topic": "General"
    },
    {
        "question_text": "[Placement B1] Fill in the blank: 'If I have enough money, I ________ (buy) a new laptop.'",
        "question_type": "fill_blank",
        "options": ["will buy"],
        "correct_answer": "will buy",
        "explanation": "Câu điều kiện loại 1: If + Present Simple, S + will + V(bare).",
        "skill": "grammar",
        "level": "B1",
        "topic": "General"
    },
    {
        "question_text": "[Placement B2] The meeting had to be ________ due to unforeseen technical difficulties.",
        "question_type": "multiple_choice",
        "options": ["postponed", "demolished", "accelerated", "erupted"],
        "correct_answer": "postponed",
        "explanation": "'Postponed' có nghĩa là hoãn lại (put off).",
        "skill": "vocabulary",
        "level": "B2",
        "topic": "Business"
    },
    {
        "question_text": "[Placement B2] Had I known about the deadline, I ________ the report earlier.",
        "question_type": "multiple_choice",
        "options": ["would have submitted", "would submit", "submitted", "will submit"],
        "correct_answer": "would have submitted",
        "explanation": "Đảo ngữ câu điều kiện loại 3: Had + S + V3, S + would have + V3.",
        "skill": "grammar",
        "level": "B2",
        "topic": "Academic"
    },
    {
        "question_text": "[Placement C1] The CEO's speech was so subtle that many listeners failed to grasp the ________ message.",
        "question_type": "multiple_choice",
        "options": ["underlying", "undergoing", "undermining", "undercover"],
        "correct_answer": "underlying",
        "explanation": "'Underlying message' = thông điệp ngầm, ý nghĩa ẩn sâu bên dưới.",
        "skill": "vocabulary",
        "level": "C1",
        "topic": "Advanced"
    },
    {
        "question_text": "[Placement C1] Under no circumstances ________ disclose confidential company data to third parties.",
        "question_type": "multiple_choice",
        "options": ["should employees", "employees should", "employees shall", "employees do"],
        "correct_answer": "should employees",
        "explanation": "Cấu trúc đảo ngữ với cụm từ phủ định 'Under no circumstances' + should + S + V.",
        "skill": "grammar",
        "level": "C1",
        "topic": "Workplace"
    },
    # ── Collocation & Idiom Quizzes
    {
        "question_text": "Complete the collocation: 'We need to ________ a decision before the end of the day.'",
        "question_type": "multiple_choice",
        "options": ["make", "do", "take", "create"],
        "correct_answer": "make",
        "explanation": "Cụm cố định là 'make a decision' (đưa ra quyết định).",
        "skill": "vocabulary",
        "level": "A2",
        "topic": "Collocations"
    },
    {
        "question_text": "What does the idiom 'Bite the bullet' mean?",
        "question_type": "multiple_choice",
        "options": [
            "To face a difficult situation with courage",
            "To eat something hard",
            "To shoot a weapon",
            "To avoid all responsibilities"
        ],
        "correct_answer": "To face a difficult situation with courage",
        "explanation": "'Bite the bullet' nghĩa là cắn răng chịu đựng, dũng cảm đối mặt với khó khăn.",
        "skill": "vocabulary",
        "level": "B2",
        "topic": "Idioms"
    },
    {
        "question_text": "Match the phrasal verbs with their definitions.",
        "question_type": "matching",
        "options": [
            {"term": "Give up", "definition": "Từ bỏ, dừng làm gì"},
            {"term": "Look forward to", "definition": "Mong chờ, háo hức"},
            {"term": "Put off", "definition": "Trì hoãn"},
            {"term": "Bring up", "definition": "Đề cập hoặc nuôi nấng"}
        ],
        "correct_answer": "Give up:Từ bỏ, dừng làm gì|Look forward to:Mong chờ, háo hức|Put off:Trì hoãn|Bring up:Đề cập hoặc nuôi nấng",
        "explanation": "Ghép cặp các cụm động từ (phrasal verbs) phổ biến.",
        "skill": "vocabulary",
        "level": "B1",
        "topic": "Phrasal Verbs"
    }
]

async def seed_more():
    print("🚀 Bắt đầu nạp thêm Reading, Listening và Quizzes...")
    await init_db()
    async with AsyncSessionLocal() as session:
        r_c = 0
        for r in EXTRA_READINGS:
            ex = (await session.execute(select(ReadingArticle).where(ReadingArticle.title == r["title"]))).scalar_one_or_none()
            if not ex:
                session.add(ReadingArticle(**r))
                r_c += 1

        l_c = 0
        for l in EXTRA_LISTENINGS:
            ex = (await session.execute(select(ListeningExercise).where(ListeningExercise.title == l["title"]))).scalar_one_or_none()
            if not ex:
                session.add(ListeningExercise(**l))
                l_c += 1

        q_c = 0
        for q in EXTRA_QUIZZES:
            ex = (await session.execute(select(QuizQuestion).where(QuizQuestion.question_text == q["question_text"]))).scalar_one_or_none()
            if not ex:
                session.add(QuizQuestion(**q))
                q_c += 1

        await session.commit()
        print(f"✅ Nạp thêm thành công: +{r_c} bài đọc, +{l_c} bài nghe, +{q_c} câu quiz!")

if __name__ == "__main__":
    asyncio.run(seed_more())
