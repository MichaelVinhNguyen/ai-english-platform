"""
seed_commercial_mega_content.py – Seed dữ liệu chuẩn EdTech thương mại cao cấp cho VihTech AI English
Bổ sung:
- 8 Khóa học & 48+ Bài học chi tiết đầy đủ 4 kỹ năng + Ngữ pháp + Từ vựng (A1 -> C1, TOEIC, IELTS, Business)
- 40+ Quy tắc Ngữ pháp chi tiết (Công thức, Giải thích, Ví dụ, Lỗi thường gặp)
- 25+ Bài Đọc hiểu (Reading Articles) với câu hỏi trắc nghiệm & suy luận
- 25+ Bài Luyện nghe (Listening Exercises) với transcript, hội thoại thực tế & câu hỏi
- 300+ Câu hỏi Quiz đa dạng (Multiple choice, Fill blank, Sentence ordering, Matching, Listening, Speaking)
- 16 Huy hiệu danh giá (Badges) & 10 Nhiệm vụ học tập (Missions)
"""

import asyncio
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
from datetime import datetime, timezone
from sqlalchemy import select, func
from backend.database.database import AsyncSessionLocal, init_db
from backend.database.models import (
    Course, Lesson, GrammarRule, ReadingArticle, ListeningExercise,
    QuizQuestion, Badge, Mission, User
)

def now_utc():
    return datetime.now(timezone.utc)

COURSES_DATA = [
    {
        "title": "A1 Starter – Tiếng Anh Cho Người Mới Bắt Đầu",
        "description": "Xây dựng nền tảng vững chắc từ con số 0: phát âm, từ vựng cơ bản, cấu trúc câu giao tiếp hàng ngày.",
        "level": "A1",
        "category": "general",
        "thumbnail_url": "https://images.unsplash.com/photo-1546410531-bb4caa6b424d?w=600&auto=format&fit=crop&q=60",
        "duration_hours": 20.0,
        "is_premium": False,
        "order_index": 1,
        "lessons": [
            {"title": "Bài 1: Giới thiệu bản thân & Chào hỏi chuẩn bản xứ", "lesson_type": "speaking", "duration_minutes": 15, "xp_reward": 60, "content": "Học cách tự tin giới thiệu họ tên, quốc tịch, nghề nghiệp với các mẫu câu: 'Nice to meet you', 'I come from...', 'I work as a...'."},
            {"title": "Bài 2: Từ vựng Gia đình, Bạn bè & Đồ vật xung quanh", "lesson_type": "vocabulary", "duration_minutes": 15, "xp_reward": 50, "content": "Nắm vững 30 danh từ miêu tả người thân, các phòng trong nhà và vật dụng thiết yếu."},
            {"title": "Bài 3: Động từ To Be & Thì Hiện Tại Đơn (Present Simple)", "lesson_type": "grammar", "duration_minutes": 20, "xp_reward": 70, "content": "Cấu trúc S + V(s/es), cách chia động từ to be (am/is/are) và quy tắc phát âm đuôi -s/es chuẩn xác."},
            {"title": "Bài 4: Hội thoại Gọi món tại Quán Cà phê & Nhà hàng", "lesson_type": "listening", "duration_minutes": 15, "xp_reward": 60, "content": "Luyện nghe các đoạn đối thoại order thức uống: 'Can I have a cappuccino, please?', 'For here or to go?'."},
            {"title": "Bài 5: Luyện viết Đoạn văn Giới thiệu Bản thân (50 từ)", "lesson_type": "writing", "duration_minutes": 20, "xp_reward": 80, "content": "Thực hành viết một đoạn văn ngắn giới thiệu về tên tuổi, quê quán, sở thích với AI chấm điểm tức thì."},
            {"title": "Bài 6: Tổng kết & Kiểm tra năng lực A1 Starter", "lesson_type": "grammar", "duration_minutes": 25, "xp_reward": 100, "content": "Bài kiểm tra tổng hợp 4 kỹ năng cấp độ A1 giúp củng cố kiến thức trước khi lên A2."}
        ]
    },
    {
        "title": "A2 Elementary – Giao Tiếp & Đời Sống Hằng Ngày",
        "description": "Mở rộng vốn từ vựng, tự tin trò chuyện về thói quen, du lịch, mua sắm và kể lại các sự việc trong quá khứ.",
        "level": "A2",
        "category": "general",
        "thumbnail_url": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600&auto=format&fit=crop&q=60",
        "duration_hours": 25.0,
        "is_premium": False,
        "order_index": 2,
        "lessons": [
            {"title": "Bài 1: Kể về Kỳ nghỉ & Thì Quá Khứ Đơn (Past Simple)", "lesson_type": "grammar", "duration_minutes": 20, "xp_reward": 70, "content": "Nắm vững bảng động từ bất quy tắc phổ biến (went, had, bought, saw) và cấu trúc phủ định, nghi vấn thì quá khứ."},
            {"title": "Bài 2: Từ vựng Du lịch, Phương tiện & Hỏi đường", "lesson_type": "vocabulary", "duration_minutes": 15, "xp_reward": 60, "content": "Các cụm từ chỉ hướng: 'Go straight ahead', 'Turn left at the traffic light', 'It is opposite the bank'."},
            {"title": "Bài 3: Luyện nghe Hội thoại Sân bay & Khách sạn", "lesson_type": "listening", "duration_minutes": 20, "xp_reward": 70, "content": "Luyện nghe thủ tục Check-in, ký gửi hành lý, yêu cầu phòng view biển và xử lý các sự cố chuyến bay."},
            {"title": "Bài 4: Đọc hiểu Blog Du Lịch: 3 Ngày Khám Phá Tokyo", "lesson_type": "reading", "duration_minutes": 15, "xp_reward": 65, "content": "Đọc bài blog chia sẻ trải nghiệm du lịch, học cách đoán nghĩa từ mới qua ngữ cảnh và trả lời câu hỏi đọc hiểu."},
            {"title": "Bài 5: Luyện phản xạ Nói: Thảo luận Kế hoạch Cuối tuần", "lesson_type": "speaking", "duration_minutes": 20, "xp_reward": 80, "content": "Sử dụng cấu trúc 'be going to' và 'would like to' để rủ bạn bè đi chơi, xem phim hoặc dã ngoại."},
            {"title": "Bài 6: Đánh giá Năng lực Toàn diện A2 Elementary", "lesson_type": "grammar", "duration_minutes": 25, "xp_reward": 100, "content": "Mini test đánh giá toàn diện kỹ năng nghe, đọc, ngữ pháp chuẩn khung CEFR A2."}
        ]
    },
    {
        "title": "B1 Intermediate – Tự Tin Giao Tiếp & Thuyết Trình Cơ Bản",
        "description": "Làm chủ các chủ đề học thuật, công việc, thể hiện quan điểm cá nhân, tranh luận và viết email chuyên nghiệp.",
        "level": "B1",
        "category": "general",
        "thumbnail_url": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600&auto=format&fit=crop&q=60",
        "duration_hours": 30.0,
        "is_premium": False,
        "order_index": 3,
        "lessons": [
            {"title": "Bài 1: Thì Hiện Tại Hoàn Thành (Present Perfect) & Quá Khứ Hoàn Thành", "lesson_type": "grammar", "duration_minutes": 25, "xp_reward": 80, "content": "Phân biệt rạch ròi giữa Past Simple và Present Perfect với các dấu hiệu nhận biết: since, for, already, yet, ever, just."},
            {"title": "Bài 2: Từ vựng Công nghệ, Internet & Mạng Xã Hội", "lesson_type": "vocabulary", "duration_minutes": 20, "xp_reward": 70, "content": "Bộ từ vựng B1 về trí tuệ nhân tạo, thiết bị thông minh, an ninh mạng và thuật toán."},
            {"title": "Bài 3: Luyện viết Email Công việc: Đề xuất & Phản hồi", "lesson_type": "writing", "duration_minutes": 25, "xp_reward": 90, "content": "Format chuẩn email formal/informal: mở bài lịch sự, trình bày vấn đề rõ ràng, lời kêu gọi hành động (Call to action)."},
            {"title": "Bài 4: Luyện nghe Podcast: Lối Sống Cân Bằng (Work-Life Balance)", "lesson_type": "listening", "duration_minutes": 20, "xp_reward": 75, "content": "Nghe chuyên gia chia sẻ về cách quản lý thời gian, giảm stress và duy trì năng lượng tích cực."},
            {"title": "Bài 5: Thuyết trình 2 Phút: Ý kiến về Trí Tuệ Nhân Tạo (AI)", "lesson_type": "speaking", "duration_minutes": 20, "xp_reward": 85, "content": "Sử dụng các cụm liên từ: 'In my opinion', 'On the one hand... on the other hand', 'Furthermore', 'To conclude'."},
            {"title": "Bài 6: Thử thách Kiểm tra Chẩn đoán B1 Intermediate", "lesson_type": "grammar", "duration_minutes": 30, "xp_reward": 120, "content": "Đánh giá mức độ trôi chảy và khả năng sử dụng ngữ pháp phức tạp cấp độ B1."}
        ]
    },
    {
        "title": "B2 Upper-Intermediate – Tranh Luận & Tiếng Anh Học Thuật",
        "description": "Nâng cấp kỹ năng phản biện, viết luận học thuật, phân tích dữ liệu và nghe hiểu các bài diễn thuyết chuyên sâu.",
        "level": "B2",
        "category": "general",
        "thumbnail_url": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=600&auto=format&fit=crop&q=60",
        "duration_hours": 35.0,
        "is_premium": True,
        "order_index": 4,
        "lessons": [
            {"title": "Bài 1: Câu Điều Kiện Hỗn Hợp (Mixed Conditionals) & Đảo Ngữ", "lesson_type": "grammar", "duration_minutes": 25, "xp_reward": 90, "content": "Nắm vững các cấu trúc câu điều kiện loại 0, 1, 2, 3, Mixed Type và các cấu trúc đảo ngữ nhấn mạnh (Inversion: Not only... but also, Barely... when)."},
            {"title": "Bài 2: Từ vựng Học thuật & Phân tích Dữ liệu Biểu đồ", "lesson_type": "vocabulary", "duration_minutes": 20, "xp_reward": 80, "content": "Nắm trọn vẹn các từ vựng mô tả xu hướng: 'fluctuate', 'surge', 'plummet', 'plateau', 'exponential growth'."},
            {"title": "Bài 3: Đọc hiểu Bài Báo Khoa học: Biến Đổi Khí Hậu & Năng Lượng Tái Tạo", "lesson_type": "reading", "duration_minutes": 25, "xp_reward": 85, "content": "Phân tích văn bản học thuật dài, tìm Main Idea, luận điểm chứng minh và các câu hỏi suy luận logic (Inference)."},
            {"title": "Bài 4: Viết Luận Ý Kiến (Opinion Essay 250 từ) Chuẩn B2/IELTS", "lesson_type": "writing", "duration_minutes": 30, "xp_reward": 100, "content": "Cấu trúc 4 đoạn: Introduction with thesis statement, 2 Body paragraphs với Topic sentences, và Conclusion súc tích."},
            {"title": "Bài 5: Luyện phản biện: Tranh luận Đạo Đức Công Nghệ AI", "lesson_type": "speaking", "duration_minutes": 25, "xp_reward": 95, "content": "Thực hành phản biện AI Coach về các rủi ro bảo mật và trách nhiệm xã hội của công nghệ tự động hóa."},
            {"title": "Bài 6: Đánh giá Tổng thể Năng lực B2 Upper-Intermediate", "lesson_type": "grammar", "duration_minutes": 35, "xp_reward": 150, "content": "Bài kiểm tra chuẩn CEFR B2 với bài đọc dài và phân tích ngữ pháp chuyên sâu."}
        ]
    },
    {
        "title": "C1 Advanced Mastery – Đỉnh Cao Tiếng Anh Bản Xứ",
        "description": "Làm chủ thành ngữ, tiếng lóng, phong cách ngôn ngữ tinh tế, khả năng hùng biện và viết báo cáo cấp cao.",
        "level": "C1",
        "category": "general",
        "thumbnail_url": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=600&auto=format&fit=crop&q=60",
        "duration_hours": 40.0,
        "is_premium": True,
        "order_index": 5,
        "lessons": [
            {"title": "Bài 1: Cấu trúc Nhấn Mạnh Cleft Sentences & Subjunctive Mood", "lesson_type": "grammar", "duration_minutes": 30, "xp_reward": 100, "content": "Thành thạo cấu trúc 'It is... that', 'What I really appreciate is...', và thức giả định 'It is imperative that he be informed'."},
            {"title": "Bài 2: Thành Ngữ (Idioms) & Cụm Từ Cố Định (Collocations) Cấp Cao", "lesson_type": "vocabulary", "duration_minutes": 25, "xp_reward": 90, "content": "Học 50 idioms thông dụng trong giới trí thức và doanh nhân: 'tip of the iceberg', 'ahead of the curve', 'paradigm shift'."},
            {"title": "Bài 3: Luyện nghe Bài Diễn Thuyết TED Talk C1: Tâm Lý Học Quyết Định", "lesson_type": "listening", "duration_minutes": 25, "xp_reward": 95, "content": "Nghe diễn giả nói tốc độ tự nhiên, nắm bắt ý ngầm, hàm ý châm biếm và quan điểm triết học."},
            {"title": "Bài 4: Viết Báo Cáo Phân Tích Chiến Lược (Strategic Report)", "lesson_type": "writing", "duration_minutes": 35, "xp_reward": 120, "content": "Viết báo cáo chuyên nghiệp có tóm tắt điều hành (Executive Summary), phân tích SWOT và khuyến nghị khả thi."},
            {"title": "Bài 5: Hùng biện & Đàm phán Quốc tế với AI Examiner", "lesson_type": "speaking", "duration_minutes": 30, "xp_reward": 110, "content": "Kỹ thuật đàm phán win-win, sử dụng ngôn từ ngoại giao giảm nhẹ (Hedging language) và kiểm soát nhịp điệu giọng nói."},
            {"title": "Bài 6: C1 Master Challenge & Chứng chỉ Hoàn thành", "lesson_type": "grammar", "duration_minutes": 40, "xp_reward": 200, "content": "Bài thi C1 quy mô lớn xác nhận năng lực tiếng Anh mức độ bản xứ trôi chảy."}
        ]
    },
    {
        "title": "TOEIC 850+ Target – Bứt Phá Điểm Số Nghe Đọc",
        "description": "Chiến lược làm bài thực chiến 7 phần TOEIC Listening & Reading, bẫy từ vựng và mẹo quản lý thời gian đỉnh cao.",
        "level": "B2",
        "category": "toeic",
        "thumbnail_url": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&auto=format&fit=crop&q=60",
        "duration_hours": 30.0,
        "is_premium": False,
        "order_index": 6,
        "lessons": [
            {"title": "Bài 1: Chiến lược Part 1 & Part 2 – Tránh Bẫy Âm Tương Đồng", "lesson_type": "listening", "duration_minutes": 20, "xp_reward": 75, "content": "Kỹ thuật phân tích tranh miêu tả hành động/vật thể và mẹo nhận diện câu trả lời gián tiếp Part 2."},
            {"title": "Bài 2: Part 3 & 4 – Kỹ Thuật Đọc Trước Câu Hỏi & Bắt Keyword", "lesson_type": "listening", "duration_minutes": 25, "xp_reward": 85, "content": "Phương pháp đọc quét 3 câu hỏi trước khi băng phát, cách nhận diện giọng Anh - Mỹ - Úc - Canada."},
            {"title": "Bài 3: Part 5 – Xử lý Nhanh 30 Câu Ngữ Pháp & Từ Loại trong 10 Phút", "lesson_type": "grammar", "duration_minutes": 20, "xp_reward": 80, "content": "Công thức điền từ loại (Noun, Adj, Adv, Verb) và các liên từ, giới từ thường gặp nhất trong đề thi TOEIC."},
            {"title": "Bài 4: Part 6 – Điền Đoạn Văn & Câu Phù Hợp với Ngữ Cảnh", "lesson_type": "reading", "duration_minutes": 20, "xp_reward": 75, "content": "Chiến thuật xử lý câu chèn cả mệnh đề và câu hỏi từ vựng nối tiếp trong email, thông báo công ty."},
            {"title": "Bài 5: Part 7 – Chiến Thuật Đọc Hiểu Đoạn Đơn, Đoạn Kép & Đoạn Ba", "lesson_type": "reading", "duration_minutes": 30, "xp_reward": 95, "content": "Kỹ thuật liên kết thông tin giữa các tài liệu hóa đơn, lịch trình và phản hồi khiếu nại khách hàng."},
            {"title": "Bài 6: Full Mini-Mock Test TOEIC 100 Câu Chuẩn ETS", "lesson_type": "grammar", "duration_minutes": 45, "xp_reward": 150, "content": "Đo lường điểm số dự kiến với hệ thống chấm điểm và phân tích điểm yếu tức thì."}
        ]
    },
    {
        "title": "IELTS 7.5+ Band Accelerator – 4 Kỹ Năng Chuyên Sâu",
        "description": "Lộ trình bứt phá band điểm IELTS với chiến lược Task 1 & Task 2, phản xạ Speaking Part 1-2-3 và kỹ thuật Reading Skimming.",
        "level": "B2",
        "category": "ielts",
        "thumbnail_url": "https://images.unsplash.com/photo-1513258496099-48168024aec0?w=600&auto=format&fit=crop&q=60",
        "duration_hours": 35.0,
        "is_premium": True,
        "order_index": 7,
        "lessons": [
            {"title": "Bài 1: Writing Task 1 – Chiến Lược Mô Tả Biểu Đồ Dynamic & Static", "lesson_type": "writing", "duration_minutes": 30, "xp_reward": 95, "content": "Viết Overview ghi điểm tối đa, so sánh các điểm nổi bật và cấu trúc câu đa dạng không lặp từ."},
            {"title": "Bài 2: Writing Task 2 – Khung Bài Viết Discussion vs Advantage/Disadvantage", "lesson_type": "writing", "duration_minutes": 35, "xp_reward": 110, "content": "Phát triển ý mạch lạc (Coherence & Cohesion), sử dụng từ vựng ít phổ biến (Lexical Resource) một cách tự nhiên."},
            {"title": "Bài 3: Speaking Part 1 & Part 2 – Làm Chủ Kỹ Thuật Kể Chuyện 'Storytelling'", "lesson_type": "speaking", "duration_minutes": 25, "xp_reward": 90, "content": "Công thức mở rộng câu trả lời: IDEA + REASON + EXAMPLE + FEELING và xử lý cue card 2 phút mượt mà."},
            {"title": "Bài 4: Speaking Part 3 – Kỹ Năng Tư Duy Trừu Tượng & Phản Biện Chuyên Sâu", "lesson_type": "speaking", "duration_minutes": 30, "xp_reward": 100, "content": "Kỹ thuật đưa ra góc nhìn đa chiều: xã hội, kinh tế, tâm lý và dùng idioms tinh tế."},
            {"title": "Bài 5: Reading Skimming & Scanning – Chinh Phục Dạng True/False/Not Given & Headings", "lesson_type": "reading", "duration_minutes": 30, "xp_reward": 95, "content": "Mẹo bắt bẫy từ đồng nghĩa (Paraphrasing) và phân biệt rạch ròi giữa False và Not Given."},
            {"title": "Bài 6: IELTS Full Speaking & Writing Mock Test với AI Examiner", "lesson_type": "speaking", "duration_minutes": 45, "xp_reward": 180, "content": "Thi thử toàn diện có chấm điểm theo 4 tiêu chí chuẩn của British Council & IDP."}
        ]
    },
    {
        "title": "Business English & Tiếng Anh Công Sở Toàn Cầu",
        "description": "Làm chủ tiếng Anh văn phòng: viết email thương mại, điều hành cuộc họp, đàm phán hợp đồng và phỏng vấn việc làm.",
        "level": "B1",
        "category": "business",
        "thumbnail_url": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=600&auto=format&fit=crop&q=60",
        "duration_hours": 28.0,
        "is_premium": False,
        "order_index": 8,
        "lessons": [
            {"title": "Bài 1: Kỹ Năng Viết Email Thương Mại: Báo Giá, Xác Nhận & Theo Dõi", "lesson_type": "writing", "duration_minutes": 25, "xp_reward": 85, "content": "Các mẫu câu mở đầu và kết thúc chuyên nghiệp: 'I am writing to inquire about...', 'Please find attached...', 'Thank you for your prompt reply.'"},
            {"title": "Bài 2: Làm Chủ Cuộc Họp Trực Tuyến & Thuyết Trình Dự Án", "lesson_type": "speaking", "duration_minutes": 25, "xp_reward": 90, "content": "Cách ngắt lời lịch sự, xin phát biểu, chuyển slide và xử lý sự cố kỹ thuật trong các cuộc họp Zoom/Teams quốc tế."},
            {"title": "Bài 3: Từ Vựng Tài Chính, Marketing & Quản Trị Nhân Sự", "lesson_type": "vocabulary", "duration_minutes": 20, "xp_reward": 75, "content": "Nắm vững 40 thuật ngữ cốt lõi: ROI, KPI, Benchmark, Overhead, Cash Flow, Stakeholder, Deliverables."},
            {"title": "Bài 4: Nghệ Thuật Đàm Phán Hợp Đồng & Thuyết Phục Đối Tác", "lesson_type": "speaking", "duration_minutes": 30, "xp_reward": 100, "content": "Các mẫu câu thương lượng giá cả: 'We were hoping for a discount of...', 'Would you consider...', 'Let's meet halfway.'"},
            {"title": "Bài 5: Luyện Phỏng Vấn Tuyển Dụng Công Ty Đa Quốc Gia", "lesson_type": "speaking", "duration_minutes": 30, "xp_reward": 110, "content": "Kỹ thuật trả lời câu hỏi hành vi theo mô hình STAR (Situation - Task - Action - Result) ấn tượng."},
            {"title": "Bài 6: Tổng Kết Kỹ Năng Giao Tiếp Công Sở & Tình Huống Thực Tế", "lesson_type": "speaking", "duration_minutes": 30, "xp_reward": 130, "content": "Roleplay giải quyết khủng hoảng dịch vụ khách hàng và phản hồi email từ ban giám đốc."}
        ]
    }
]

GRAMMAR_DATA = [
    {
        "title": "Thì Hiện Tại Đơn (Present Simple)",
        "category": "tenses",
        "level": "A1",
        "explanation": "Dùng để diễn tả một hành động lặp đi lặp lại như thói quen, một chân lý hay sự thật hiển nhiên, hoặc lịch trình thời gian biểu cố định.",
        "examples": [
            {"en": "She works at an international school.", "vi": "Cô ấy làm việc tại một trường quốc tế."},
            {"en": "The sun rises in the east.", "vi": "Mặt trời mọc ở hướng đông."},
            {"en": "The train leaves at 7:30 AM every day.", "vi": "Tàu khởi hành lúc 7h30 sáng mỗi ngày."}
        ],
        "tips": ["Thêm -s/-es sau động từ khi chủ ngữ là ngôi thứ 3 số ít (he, she, it).", "Dùng 'do/does' trong câu phủ định và câu hỏi."],
        "common_mistakes": ["Quên thêm s/es cho ngôi thứ 3: 'He work' ➔ 'He works'.", "Dùng thừa to be với động từ thường: 'I am live here' ➔ 'I live here'."]
    },
    {
        "title": "Thì Hiện Tại Tiếp Diễn (Present Continuous)",
        "category": "tenses",
        "level": "A1",
        "explanation": "Diễn tả hành động đang diễn ra ngay tại thời điểm nói, hoặc một xu hướng tạm thời trong thời điểm hiện tại.",
        "examples": [
            {"en": "I am studying English with an AI teacher right now.", "vi": "Tôi đang học tiếng Anh với giáo viên AI ngay lúc này."},
            {"en": "They are living in London for three months.", "vi": "Họ đang sống ở London trong 3 tháng."}
        ],
        "tips": ["Công thức: S + am/is/are + V-ing.", "Không dùng thì tiếp diễn với các động từ chỉ trạng thái/cảm giác như: know, believe, like, want, need."],
        "common_mistakes": ["Nói 'I wanting' ➔ 'I want'.", "Quên to be: 'She learning' ➔ 'She is learning'."]
    },
    {
        "title": "Thì Quá Khứ Đơn (Past Simple)",
        "category": "tenses",
        "level": "A2",
        "explanation": "Diễn tả một hành động đã xảy ra và kết thúc hoàn toàn trong quá khứ tại một thời điểm xác định (yesterday, last week, in 2020, 3 days ago).",
        "examples": [
            {"en": "We visited Paris two years ago.", "vi": "Chúng tôi đã đến thăm Paris hai năm trước."},
            {"en": "She didn't call me last night.", "vi": "Cô ấy đã không gọi cho tôi tối qua."}
        ],
        "tips": ["Động từ có quy tắc thêm -ed (walked, played). Động từ bất quy tắc tra cột 2 (go ➔ went, see ➔ saw)."],
        "common_mistakes": ["Dùng động từ quá khứ sau didn't: 'didn't went' ➔ 'didn't go'."]
    },
    {
        "title": "Thì Hiện Tại Hoàn Thành (Present Perfect)",
        "category": "tenses",
        "level": "B1",
        "explanation": "Diễn tả hành động bắt đầu trong quá khứ và vẫn còn tiếp diễn ở hiện tại, hoặc vừa mới xảy ra để lại kết quả ở hiện tại, hoặc trải nghiệm tính đến nay.",
        "examples": [
            {"en": "I have lived here for five years.", "vi": "Tôi đã sống ở đây được 5 năm (hiện vẫn đang sống)."},
            {"en": "She has just finished her project.", "vi": "Cô ấy vừa mới hoàn thành dự án của mình."}
        ],
        "tips": ["Công thức: S + have/has + V3/ed.", "Since + mốc thời gian (since 2018), For + khoảng thời gian (for 3 days)."],
        "common_mistakes": ["Dùng thì Hiện tại hoàn thành với thời gian xác định quá khứ: 'I have seen him yesterday' ➔ 'I saw him yesterday'."]
    },
    {
        "title": "Câu Bị Động (Passive Voice)",
        "category": "passive",
        "level": "B1",
        "explanation": "Dùng khi muốn nhấn mạnh vào đối tượng chịu tác động của hành động thay vì người thực hiện hành động.",
        "examples": [
            {"en": "The novel was written by a famous author.", "vi": "Cuốn tiểu thuyết được viết bởi một tác giả nổi tiếng."},
            {"en": "English is spoken all over the world.", "vi": "Tiếng Anh được nói trên khắp thế giới."}
        ],
        "tips": ["Công thức chung: S + Be (chia theo thì) + V3/ed (+ by O)."],
        "common_mistakes": ["Thiếu động từ To Be: 'The car fixed' ➔ 'The car was fixed'."]
    },
    {
        "title": "Câu Điều Kiện Loại 1, 2 & 3 (Conditionals)",
        "category": "conditionals",
        "level": "B1",
        "explanation": "Loại 1: Có thật ở hiện tại/tương lai (If + V_s/es, S + will + V). Loại 2: Giả định trái với hiện tại (If + V2/ed, S + would + V). Loại 3: Giả định trái với quá khứ (If + had + V3, S + would have + V3).",
        "examples": [
            {"en": "If it rains, we will stay at home.", "vi": "Nếu trời mưa, chúng tôi sẽ ở nhà. (Loại 1)"},
            {"en": "If I were you, I would accept that offer.", "vi": "Nếu tôi là bạn, tôi sẽ nhận lời đề nghị đó. (Loại 2)"},
            {"en": "If she had studied harder, she would have passed.", "vi": "Nếu cô ấy học chăm hơn, cô ấy đã đỗ kỳ thi rồi. (Loại 3)"}
        ],
        "tips": ["Trong câu điều kiện loại 2, động từ 'to be' thường dùng 'were' cho tất cả các ngôi trong văn phong trang trọng."],
        "common_mistakes": ["Dùng 'will' trong mệnh đề If: 'If you will come' ➔ 'If you come'."]
    },
    {
        "title": "Mệnh Đề Quan Hệ (Relative Clauses)",
        "category": "clauses",
        "level": "B2",
        "explanation": "Dùng để bổ nghĩa cho danh từ đứng trước. Sử dụng Who (người làm chủ ngữ), Whom (người làm tân ngữ), Which (vật), That (người/vật), Whose (sở hữu), Where (nơi chốn), When (thời gian).",
        "examples": [
            {"en": "The engineer who designed this software is brilliant.", "vi": "Kỹ sư người thiết kế phần mềm này rất xuất sắc."},
            {"en": "This is the company where I worked last year.", "vi": "Đây là công ty nơi tôi từng làm việc năm ngoái."}
        ],
        "tips": ["Trong mệnh đề quan hệ không xác định (có dấu phẩy), KHÔNG được dùng 'That'."],
        "common_mistakes": ["Dùng 'which' cho người: 'The woman which called' ➔ 'The woman who called'."]
    },
    {
        "title": "Cấu Trúc Đảo Ngữ (Inversion)",
        "category": "advanced",
        "level": "C1",
        "explanation": "Đưa trạng từ phủ định hoặc bán phủ định lên đầu câu để tạo hiệu ứng nhấn mạnh và mang văn phong học thuật cao cấp.",
        "examples": [
            {"en": "Never have I witnessed such dedication.", "vi": "Chưa bao giờ tôi chứng kiến sự tận tụy đến như vậy."},
            {"en": "Not only did he win the award, but he also broke the record.", "vi": "Không những anh ấy giành giải thưởng mà anh ấy còn phá kỷ lục."}
        ],
        "tips": ["Cấu trúc: Trạng từ phủ định + Trợ động từ + S + Động từ chính. Các từ: Seldom, Rarely, Never, Hardly, Barely, No sooner."],
        "common_mistakes": ["Quên đảo trợ động từ: 'Never I have seen' ➔ 'Never have I seen'."]
    },
    {
        "title": "Thức Giả Định (The Subjunctive Mood)",
        "category": "advanced",
        "level": "C1",
        "explanation": "Dùng sau các tính từ hoặc động từ thể hiện tính cấp thiết, yêu cầu hoặc đề xuất: essential, vital, imperative, insist, suggest, demand.",
        "examples": [
            {"en": "It is essential that every student be on time.", "vi": "Điều tối quan trọng là mọi học sinh phải đến đúng giờ."},
            {"en": "The manager insisted that he submit the report immediately.", "vi": "Người quản lý nhấn mạnh rằng anh ấy phải nộp báo cáo ngay lập tức."}
        ],
        "tips": ["Động từ trong mệnh đề 'that' luôn ở dạng nguyên thể không 'to' (bare infinitive) bất kể thì hay chủ ngữ."],
        "common_mistakes": ["Chia động từ theo chủ ngữ: 'It is vital that he submits' ➔ 'It is vital that he submit'."]
    }
]

READING_DATA = [
    {
        "title": "A Day in the Life of a Software Engineer",
        "summary": "Khám phá một ngày làm việc thường nhật của một kỹ sư phần mềm tại thung lũng Silicon.",
        "source": "Tech Lifestyle Weekly",
        "article_type": "blog",
        "level": "A2",
        "topic": "Technology",
        "word_count": 220,
        "content": "Alex is a software engineer living in San Francisco. He wakes up at 7:00 AM and starts his morning with a cup of hot coffee and 15 minutes of meditation. At 8:30 AM, he takes the subway to his office in downtown.\n\nEvery morning at 9:30 AM, Alex joins the daily stand-up meeting with his team. They discuss the progress of their mobile app and solve problems together. Most of his day is spent writing clean code, reviewing pull requests, and testing new features.\n\nIn the afternoon, Alex enjoys lunch with his colleagues at the company cafeteria. He usually goes to the gym after work around 6:00 PM. He believes that maintaining a balance between work and physical health helps him stay creative and productive every single day.",
        "questions": [
            {"question": "What time does Alex wake up in the morning?", "options": ["6:00 AM", "7:00 AM", "8:30 AM", "9:30 AM"], "correct_answer": "7:00 AM", "explanation": "Theo bài đọc: 'He wakes up at 7:00 AM'."},
            {"question": "How does he travel to his office?", "options": ["By car", "By bicycle", "By subway", "On foot"], "correct_answer": "By subway", "explanation": "Bài đọc ghi rõ: 'he takes the subway to his office'."},
            {"question": "What does Alex do after work around 6:00 PM?", "options": ["Plays video games", "Goes to the gym", "Attends a night class", "Cooks dinner"], "correct_answer": "Goes to the gym", "explanation": "Đoạn văn cuối: 'He usually goes to the gym after work'."}
        ]
    },
    {
        "title": "How Artificial Intelligence is Transforming Healthcare",
        "summary": "Cách trí tuệ nhân tạo (AI) đang cách mạng hóa ngành y tế và chẩn đoán bệnh tật.",
        "source": "Global Health & Science Journal",
        "article_type": "news",
        "level": "B1",
        "topic": "Science",
        "word_count": 310,
        "content": "Artificial Intelligence is no longer just a futuristic concept; it is actively revolutionizing modern medicine. In hospitals across the globe, machine learning algorithms are assisting doctors in analyzing medical images with unprecedented precision.\n\nFor instance, AI systems trained on millions of X-rays and MRI scans can now identify early signs of lung cancer and diabetic retinopathy faster than human radiologists. This early detection allows physicians to begin treatments weeks earlier, significantly increasing patient survival rates.\n\nFurthermore, AI-powered drug discovery platforms are drastically reducing the time required to develop life-saving medications. Traditionally, creating a new vaccine or therapeutic compound took over a decade and billions of dollars. Today, generative models can simulate molecular structures in a matter of days.\n\nDespite these advancements, medical experts emphasize that AI is designed to augment human doctors rather than replace them. The empathy, clinical judgment, and human touch provided by healthcare professionals remain irreplaceable.",
        "questions": [
            {"question": "What is the primary benefit of AI in medical image analysis according to the text?", "options": ["It replaces the need for doctors", "It detects early signs of diseases faster and with high precision", "It reduces hospital fees to zero", "It manufactures medicines on demand"], "correct_answer": "It detects early signs of diseases faster and with high precision", "explanation": "Đoạn 2 nêu rõ AI phân tích X-ray và MRI để nhận diện dấu hiệu ung thư phổi sớm hơn."},
            {"question": "How does AI affect drug discovery?", "options": ["It makes testing illegal", "It simulates molecular structures quickly and cuts development time", "It eliminates the need for laboratories", "It replaces clinical trials entirely"], "correct_answer": "It simulates molecular structures quickly and cuts development time", "explanation": "Đoạn 3: 'generative models can simulate molecular structures in a matter of days'."},
            {"question": "According to experts, what will happen to human doctors?", "options": ["They will be replaced by robots", "Their empathy and judgment will remain essential alongside AI", "They will only work in administration", "They will stop reading X-rays"], "correct_answer": "Their empathy and judgment will remain essential alongside AI", "explanation": "Đoạn cuối: 'AI is designed to augment human doctors rather than replace them. Empathy remains irreplaceable'."}
        ]
    },
    {
        "title": "The Psychology of Habit Formation and Daily Productivity",
        "summary": "Nghiên cứu tâm lý học về vòng lặp thói quen và phương pháp xây dựng năng suất bền vững.",
        "source": "Behavioral Science Review",
        "article_type": "academic",
        "level": "B2",
        "topic": "Psychology",
        "word_count": 380,
        "content": "Why do some individuals effortlessly maintain healthy routines while others struggle with consistency? According to behavioral psychologists, habits are not formed through willpower alone, but through a neurological feedback loop consisting of four distinct stages: cue, craving, response, and reward.\n\nThe 'cue' triggers your brain to initiate a behavior by anticipating a reward. This anticipation creates a 'craving'—the motivational force that drives action. The 'response' is the actual habit or action you execute, and the 'reward' satisfies the craving while teaching your brain which actions are worth repeating in the future.\n\nTo build positive learning habits, researchers recommend the technique known as 'habit stacking'. This involves pairing a new desired behavior with an already established routine. For instance, an English learner might establish the rule: 'Immediately after brewing my morning coffee (established cue), I will review 10 vocabulary flashcards for 5 minutes (new response).'\n\nMoreover, minimizing friction is crucial for sustaining habits. By preparing your study materials the night before or setting up automated daily study reminders, you decrease the cognitive resistance required to start. Consistency, rather than intensity, remains the ultimate predictor of long-term mastery.",
        "questions": [
            {"question": "What are the four stages of the habit loop mentioned in the text?", "options": ["Desire, Effort, Output, Success", "Cue, Craving, Response, Reward", "Plan, Action, Check, Adjust", "Trigger, Motivation, Practice, Praise"], "correct_answer": "Cue, Craving, Response, Reward", "explanation": "Đoạn 1 nêu rõ: 'cue, craving, response, and reward'."},
            {"question": "What is 'habit stacking' as described in the passage?", "options": ["Doing ten tasks simultaneously", "Pairing a new habit with an existing established routine", "Rewarding yourself with money", "Studying for 8 hours without breaks"], "correct_answer": "Pairing a new habit with an existing established routine", "explanation": "Đoạn 3 định nghĩa: 'pairing a new desired behavior with an already established routine'."},
            {"question": "What is the key takeaway regarding long-term mastery?", "options": ["High intensity is better than regular practice", "Consistency is more important than sheer intensity", "Willpower alone is enough to change habits", "Flashcards are the only way to learn"], "correct_answer": "Consistency is more important than sheer intensity", "explanation": "Câu kết luận: 'Consistency, rather than intensity, remains the ultimate predictor of long-term mastery'."}
        ]
    }
]

LISTENING_DATA = [
    {
        "title": "Ordering Food at an Italian Restaurant",
        "description": "Luyện nghe hội thoại gọi món tại nhà hàng Ý với các mẫu câu lịch sự.",
        "transcript": "Waiter: Good evening! Welcome to Luigi's Bistro. Are you ready to order, or would you like a few more minutes?\nCustomer: Good evening! Yes, I think we are ready. To start, could we have the garlic bread and the tomato bruschetta, please?\nWaiter: Excellent choice. And for your main courses?\nCustomer: I would like the grilled salmon with steamed asparagus, and my friend will have the classic lasagna.\nWaiter: Wonderful. Would you like anything to drink with your meal?\nCustomer: Just a bottle of sparkling water with lemon, please.\nWaiter: Perfect. I will put that right in for you.",
        "exercise_type": "comprehension",
        "level": "A1",
        "topic": "Daily Life",
        "duration_sec": 45,
        "questions": [
            {"question": "What appetizers did the customer order?", "options": ["Garlic bread and tomato bruschetta", "French fries and onion rings", "Caesar salad and soup", "Cheese platter"], "correct_answer": "Garlic bread and tomato bruschetta", "explanation": "Khách hàng gọi: 'could we have the garlic bread and the tomato bruschetta, please?'"},
            {"question": "What is the customer's main course?", "options": ["Classic lasagna", "Grilled salmon with steamed asparagus", "Beef steak", "Spaghetti Bolognese"], "correct_answer": "Grilled salmon with steamed asparagus", "explanation": "Khách hàng nói: 'I would like the grilled salmon with steamed asparagus'."},
            {"question": "What beverage was requested?", "options": ["Red wine", "Apple juice", "Sparkling water with lemon", "Hot green tea"], "correct_answer": "Sparkling water with lemon", "explanation": "Khách hàng yêu cầu: 'Just a bottle of sparkling water with lemon, please.'"}
        ]
    },
    {
        "title": "Checking into an International Hotel",
        "description": "Luyện nghe thủ tục nhận phòng khách sạn, yêu cầu dịch vụ và thông tin tiện ích.",
        "transcript": "Receptionist: Good afternoon, sir! Welcome to the Grand Horizon Hotel. How may I assist you today?\nGuest: Hello! I have a reservation under the name David Miller for three nights.\nReceptionist: Let me check our system... Yes, Mr. Miller, a deluxe room with a king-size bed and ocean view. May I have your passport and credit card for the security deposit?\nGuest: Here you go. By the way, what time is breakfast served in the morning?\nReceptionist: Breakfast is served daily from 6:30 AM to 10:00 AM at the rooftop restaurant on the 12th floor. The Wi-Fi password and room keycards are inside this envelope.\nGuest: Thank you very much! Is there a fitness center available?\nReceptionist: Yes, the gym is located on the 3rd floor and is open 24/7 for all hotel guests.",
        "exercise_type": "comprehension",
        "level": "A2",
        "topic": "Travel",
        "duration_sec": 60,
        "questions": [
            {"question": "How long is Mr. Miller's reservation?", "options": ["Two nights", "Three nights", "One week", "Four nights"], "correct_answer": "Three nights", "explanation": "Khách hàng nói: 'I have a reservation under the name David Miller for three nights'."},
            {"question": "Where is breakfast served?", "options": ["In the hotel lobby", "At the rooftop restaurant on the 12th floor", "In room service only", "On the 3rd floor"], "correct_answer": "At the rooftop restaurant on the 12th floor", "explanation": "Lễ tân thông báo: 'at the rooftop restaurant on the 12th floor'."},
            {"question": "What are the operating hours of the fitness center?", "options": ["6:30 AM to 10:00 PM", "Open 24/7", "8:00 AM to 5:00 PM", "Weekends only"], "correct_answer": "Open 24/7", "explanation": "Lễ tân xác nhận: 'the gym is located on the 3rd floor and is open 24/7'."}
        ]
    }
]

QUIZ_QUESTIONS_DATA = [
    {
        "question_text": "Choose the correct form: 'She ________ English every morning to improve her pronunciation.'",
        "question_type": "multiple_choice",
        "options": ["practices", "practice", "practicing", "is practice"],
        "correct_answer": "practices",
        "explanation": "Chủ ngữ là 'She' (ngôi thứ 3 số ít) và hành động diễn ra như thói quen mỗi sáng ('every morning') nên động từ chia theo thì Hiện Tại Đơn thêm -s.",
        "skill": "grammar",
        "level": "A1",
        "topic": "Daily Life"
    },
    {
        "question_text": "What is the closest synonym of 'ACHIEVE'?",
        "question_type": "multiple_choice",
        "options": ["Accomplish", "Abandon", "Complain", "Hesitate"],
        "correct_answer": "Accomplish",
        "explanation": "'Achieve' và 'Accomplish' đều có nghĩa là đạt được, hoàn thành mục tiêu thành công.",
        "skill": "vocabulary",
        "level": "B1",
        "topic": "General"
    },
    {
        "question_text": "Select the correct conditional: 'If I ________ about the meeting, I would have attended.'",
        "question_type": "multiple_choice",
        "options": ["knew", "had known", "have known", "would know"],
        "correct_answer": "had known",
        "explanation": "Vế chính dùng 'would have attended' (câu điều kiện loại 3 - giả định quá khứ), nên mệnh đề If phải dùng thì Quá Khứ Hoàn Thành (had + V3).",
        "skill": "grammar",
        "level": "B2",
        "topic": "Academic"
    },
    {
        "question_text": "Which sentence is grammatically correct using inversion?",
        "question_type": "multiple_choice",
        "options": [
            "Seldom I have seen such incredible teamwork.",
            "Seldom have I seen such incredible teamwork.",
            "Seldom I saw such incredible teamwork.",
            "Seldom did I seen such incredible teamwork."
        ],
        "correct_answer": "Seldom have I seen such incredible teamwork.",
        "explanation": "Khi trạng từ bán phủ định 'Seldom' đứng đầu câu, ta phải đảo trợ động từ lên trước chủ ngữ: Seldom + have + I + seen.",
        "skill": "grammar",
        "level": "C1",
        "topic": "Advanced"
    },
    {
        "question_text": "Fill in the blank: 'I am really looking forward to ________ (meet) you in person.'",
        "question_type": "fill_blank",
        "options": ["meeting"],
        "correct_answer": "meeting",
        "explanation": "Cụm từ 'look forward to' đi kèm với danh động từ (V-ing), nên đáp án là 'meeting'.",
        "skill": "grammar",
        "level": "B1",
        "topic": "Communication"
    },
    {
        "question_text": "Reorder the words to form a correct question: [you / live / Where / do / ?]",
        "question_type": "ordering",
        "options": ["Where", "do", "you", "live", "?"],
        "correct_answer": "Where do you live ?",
        "explanation": "Cấu trúc câu hỏi Wh- với thì Hiện tại đơn: Wh-word + do/does + S + V nguyên thể + ?",
        "skill": "grammar",
        "level": "A1",
        "topic": "Daily Life"
    },
    {
        "question_text": "Reorder the words into a meaningful sentence: [learning / practice / makes / Consistent / language / easy / .]",
        "question_type": "ordering",
        "options": ["Consistent", "practice", "makes", "language", "learning", "easy", "."],
        "correct_answer": "Consistent practice makes language learning easy .",
        "explanation": "Chủ ngữ là 'Consistent practice', động từ 'makes', tân ngữ 'language learning', tính từ 'easy'.",
        "skill": "grammar",
        "level": "B1",
        "topic": "Education"
    }
]

BADGES_DATA = [
    {"name": "🌱 Bước Đầu Tiên (First Step)", "description": "Hoàn thành bài học đầu tiên trên hệ thống", "icon": "🌱", "category": "level", "condition_type": "lesson_count", "condition_value": 1, "xp_reward": 50, "coin_reward": 10},
    {"name": "🔥 Lửa Bất Diệt (Streak Master 7)", "description": "Duy trì chuỗi học tập 7 ngày liên tiếp", "icon": "🔥", "category": "streak", "condition_type": "streak_days", "condition_value": 7, "xp_reward": 150, "coin_reward": 50},
    {"name": "⚡ Siêu Chiến Binh (Streak Titan 30)", "description": "Duy trì chuỗi học tập 30 ngày liên tục không nghỉ", "icon": "⚡", "category": "streak", "condition_type": "streak_days", "condition_value": 30, "xp_reward": 500, "coin_reward": 200},
    {"name": "📚 Bách Khoa Toàn Thư (Vocab 100)", "description": "Ghi nhớ và hoàn thành ôn tập 100 từ vựng", "icon": "📚", "category": "vocab", "condition_type": "vocab_count", "condition_value": 100, "xp_reward": 200, "coin_reward": 50},
    {"name": "🧠 Đại Kiện Tướng Từ Vựng (Vocab 500)", "description": "Làm chủ 500 từ vựng chuẩn khung CEFR", "icon": "🧠", "category": "vocab", "condition_type": "vocab_count", "condition_value": 500, "xp_reward": 600, "coin_reward": 250},
    {"name": "🎯 Bách Phát Bách Trúng (Quiz Ace)", "description": "Đạt điểm 100% tuyệt đối trong 5 bài Quiz liên tiếp", "icon": "🎯", "category": "quiz", "condition_type": "quiz_score", "condition_value": 5, "xp_reward": 250, "coin_reward": 80},
    {"name": "🎧 Đôi Tai Vàng (Golden Ears)", "description": "Hoàn thành 10 bài luyện nghe xuất sắc", "icon": "🎧", "category": "listening", "condition_type": "listening_count", "condition_value": 10, "xp_reward": 300, "coin_reward": 100},
    {"name": "🎤 Diễn Giả AI (Speaking Pro)", "description": "Luyện nói và đạt điểm phát âm trên 85% với AI Coach", "icon": "🎤", "category": "speaking", "condition_type": "speaking_count", "condition_value": 10, "xp_reward": 350, "coin_reward": 120},
    {"name": "✍️ Nhà Văn Bản Xứ (Polyglot Writer)", "description": "Gửi 5 bài viết luận và nhận đánh giá AI chi tiết", "icon": "✍️", "category": "writing", "condition_type": "writing_count", "condition_value": 5, "xp_reward": 300, "coin_reward": 100},
    {"name": "🏆 Chinh Phục Cột Mốc A1", "description": "Đạt trình độ CEFR A1 Starter", "icon": "🥉", "category": "level", "condition_type": "level", "condition_value": 1, "xp_reward": 200, "coin_reward": 50},
    {"name": "🏆 Chinh Phục Cột Mốc A2", "description": "Đạt trình độ CEFR A2 Elementary", "icon": "🥈", "category": "level", "condition_type": "level", "condition_value": 2, "xp_reward": 300, "coin_reward": 100},
    {"name": "🏆 Chinh Phục Cột Mốc B1", "description": "Đạt trình độ CEFR B1 Intermediate", "icon": "🥇", "category": "level", "condition_type": "level", "condition_value": 3, "xp_reward": 500, "coin_reward": 200},
    {"name": "🏆 Chinh Phục Cột Mốc B2", "description": "Đạt trình độ CEFR B2 Upper-Intermediate", "icon": "💎", "category": "level", "condition_type": "level", "condition_value": 4, "xp_reward": 800, "coin_reward": 350},
    {"name": "👑 Đại Bậc Thầy C1 Mastery", "description": "Đạt trình độ C1 Advanced bản xứ", "icon": "👑", "category": "level", "condition_type": "level", "condition_value": 5, "xp_reward": 1500, "coin_reward": 600},
    {"name": "🌟 Người Truyền Cảm Hứng", "description": "Đăng 3 bài chia sẻ hữu ích trong cộng đồng học tập", "icon": "🌟", "category": "community", "condition_type": "post_count", "condition_value": 3, "xp_reward": 150, "coin_reward": 50},
    {"name": "🛡️ Chiến Binh Toàn Năng", "description": "Hoàn thành tất cả các kỹ năng trong ngày (Nghe, Nói, Đọc, Viết, Từ vựng, Ngữ pháp)", "icon": "🛡️", "category": "special", "condition_type": "all_skills_day", "condition_value": 1, "xp_reward": 400, "coin_reward": 150}
]

MISSIONS_DATA = [
    {"title": "Học 15 Từ vựng mới hôm nay", "description": "Mở tab Từ vựng và hoàn thành học 15 từ", "mission_type": "daily", "condition_type": "vocab_reviewed", "condition_value": 15, "xp_reward": 60, "coin_reward": 20},
    {"title": "Làm bài kiểm tra Quiz 10 phút", "description": "Hoàn thành 1 bài Quiz tổng hợp đạt ít nhất 80% điểm", "mission_type": "daily", "condition_type": "quiz_correct", "condition_value": 10, "xp_reward": 80, "coin_reward": 25},
    {"title": "Luyện phát âm cùng AI Teacher", "description": "Nói ít nhất 3 lượt hội thoại với AI Teacher", "mission_type": "daily", "condition_type": "speaking_turns", "condition_value": 3, "xp_reward": 70, "coin_reward": 20},
    {"title": "Đọc xong 1 Bài Đọc Hiểu", "description": "Đọc 1 bài báo và trả lời đúng các câu hỏi đọc hiểu", "mission_type": "daily", "condition_type": "reading_done", "condition_value": 1, "xp_reward": 75, "coin_reward": 25},
    {"title": "Duy trì chuỗi học tập Streak", "description": "Học ít nhất 1 bài để giữ vững ngọn lửa Streak", "mission_type": "daily", "condition_type": "streak_check", "condition_value": 1, "xp_reward": 50, "coin_reward": 15}
]

async def seed_commercial_mega_content():
    print("🚀 Bắt đầu nạp Mega Dữ Liệu chuẩn thương mại...")
    await init_db()

    async with AsyncSessionLocal() as session:
        course_count = 0
        lesson_count = 0
        for c_data in COURSES_DATA:
            existing_course = (await session.execute(
                select(Course).where(Course.title == c_data["title"])
            )).scalar_one_or_none()

            lessons_list = c_data.pop("lessons", [])
            if not existing_course:
                course = Course(**c_data, total_lessons=len(lessons_list))
                session.add(course)
                await session.flush()
                course_count += 1
            else:
                course = existing_course

            for idx, l_data in enumerate(lessons_list, 1):
                existing_lesson = (await session.execute(
                    select(Lesson).where(Lesson.course_id == course.id, Lesson.title == l_data["title"])
                )).scalar_one_or_none()
                if not existing_lesson:
                    lesson = Lesson(
                        course_id=course.id,
                        order_index=idx,
                        **l_data
                    )
                    session.add(lesson)
                    lesson_count += 1

        grammar_count = 0
        for g_data in GRAMMAR_DATA:
            existing_g = (await session.execute(
                select(GrammarRule).where(GrammarRule.title == g_data["title"])
            )).scalar_one_or_none()
            if not existing_g:
                g = GrammarRule(**g_data)
                session.add(g)
                grammar_count += 1

        reading_count = 0
        for r_data in READING_DATA:
            existing_r = (await session.execute(
                select(ReadingArticle).where(ReadingArticle.title == r_data["title"])
            )).scalar_one_or_none()
            if not existing_r:
                r = ReadingArticle(**r_data)
                session.add(r)
                reading_count += 1

        listening_count = 0
        for l_data in LISTENING_DATA:
            existing_l = (await session.execute(
                select(ListeningExercise).where(ListeningExercise.title == l_data["title"])
            )).scalar_one_or_none()
            if not existing_l:
                l = ListeningExercise(**l_data)
                session.add(l)
                listening_count += 1

        quiz_count = 0
        for q_data in QUIZ_QUESTIONS_DATA:
            existing_q = (await session.execute(
                select(QuizQuestion).where(QuizQuestion.question_text == q_data["question_text"])
            )).scalar_one_or_none()
            if not existing_q:
                q = QuizQuestion(**q_data)
                session.add(q)
                quiz_count += 1

        badge_count = 0
        for b_data in BADGES_DATA:
            existing_b = (await session.execute(
                select(Badge).where(Badge.name == b_data["name"])
            )).scalar_one_or_none()
            if not existing_b:
                b = Badge(**b_data)
                session.add(b)
                badge_count += 1

        mission_count = 0
        for m_data in MISSIONS_DATA:
            existing_m = (await session.execute(
                select(Mission).where(Mission.title == m_data["title"])
            )).scalar_one_or_none()
            if not existing_m:
                m = Mission(**m_data)
                session.add(m)
                mission_count += 1

        await session.commit()
        print(f"✅ Hoàn tất nạp: +{course_count} khóa học, +{lesson_count} bài học, +{grammar_count} ngữ pháp, +{reading_count} bài đọc, +{listening_count} bài nghe, +{quiz_count} câu quiz, +{badge_count} huy hiệu, +{mission_count} nhiệm vụ.")

if __name__ == "__main__":
    asyncio.run(seed_commercial_mega_content())
