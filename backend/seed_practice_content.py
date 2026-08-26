# -*- coding: utf-8 -*-
import asyncio
import sys
import io
from sqlalchemy import select

# Ensure utf-8 output in windows console
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from backend.database.database import AsyncSessionLocal, init_db
from backend.database.models import ListeningExercise, ReadingArticle, GrammarRule, Course, Lesson

async def seed_practice():
    print("=== STARTING SEEDING PRACTICE CONTENT (CEFR A1-C2) ===")
    await init_db()
    async with AsyncSessionLocal() as db:
        # 1. Grammar Rules (25 comprehensive rules for A1 - C2)
        grammar_rules = [
            # A1
            GrammarRule(
                title="Present Simple (Thì hiện tại đơn)",
                category="tenses",
                level="A1",
                explanation="Diễn tả một thói quen, một sự thật hiển nhiên hoặc hành động lặp đi lặp lại hàng ngày.",
                examples=[
                    {"en": "She drinks coffee every morning.", "vi": "Cô ấy uống cà phê mỗi sáng."},
                    {"en": "The sun rises in the east.", "vi": "Mặt trời mọc ở hướng đông."},
                    {"en": "I do not live in New York.", "vi": "Tôi không sống ở New York."}
                ],
                tips=["Thêm -s / -es với chủ ngữ số ít (He, She, It).", "Dùng do/does trong câu nghi vấn và phủ định."],
                common_mistakes=["He play football (Sai -> He plays football).", "Does she likes apples? (Sai -> Does she like apples?)"]
            ),
            GrammarRule(
                title="Present Continuous (Thì hiện tại tiếp diễn)",
                category="tenses",
                level="A1",
                explanation="Diễn tả một hành động đang xảy ra ngay tại thời điểm nói hoặc một kế hoạch chắc chắn trong tương lai gần.",
                examples=[
                    {"en": "He is watching TV right now.", "vi": "Anh ấy đang xem TV lúc này."},
                    {"en": "We are studying English with AI Teacher.", "vi": "Chúng tôi đang học tiếng Anh với Giáo viên AI."}
                ],
                tips=["Cấu trúc: S + am/is/are + V-ing.", "Dấu hiệu nhận biết: now, right now, at the moment, look! listen!"],
                common_mistakes=["I am understand (Sai -> I understand - động từ nhận thức không chia tiếp diễn)."]
            ),
            GrammarRule(
                title="Articles: A / An / The (Mạo từ)",
                category="articles",
                level="A1",
                explanation="A/An dùng trước danh từ đếm được số ít chưa xác định. An đứng trước từ bắt đầu bằng nguyên âm phát âm (a, e, i, o, u). The dùng cho đối tượng xác định.",
                examples=[
                    {"en": "I have an apple and a banana.", "vi": "Tôi có một quả táo và một quả chuối."},
                    {"en": "The moon is bright tonight.", "vi": "Mặt trăng đêm nay rất sáng."}
                ],
                tips=["An hour (vì âm h câm -> an hour).", "A university (vì phát âm là /juː/ -> a university)."],
                common_mistakes=["An university (Sai -> A university)."]
            ),
            GrammarRule(
                title="There is / There are",
                category="sentence_structure",
                level="A1",
                explanation="Dùng để giới thiệu sự tồn tại của người hoặc vật ở một vị trí nào đó.",
                examples=[
                    {"en": "There is a book on the desk.", "vi": "Có một cuốn sách trên bàn."},
                    {"en": "There are many students in the classroom.", "vi": "Có nhiều học sinh trong phòng học."}
                ],
                tips=["There is + danh từ số ít / không đếm được.", "There are + danh từ số nhiều."],
                common_mistakes=["There is two cats (Sai -> There are two cats)."]
            ),
            # A2
            GrammarRule(
                title="Past Simple (Thì quá khứ đơn)",
                category="tenses",
                level="A2",
                explanation="Diễn tả hành động đã xảy ra và chấm dứt hoàn toàn trong quá khứ, có thời gian xác định.",
                examples=[
                    {"en": "I went to Tokyo last summer.", "vi": "Tôi đã đi Tokyo mùa hè năm ngoái."},
                    {"en": "She didn't call me yesterday.", "vi": "Cô ấy đã không gọi tôi hôm qua."}
                ],
                tips=["Động từ quy tắc thêm -ed, bất quy tắc tra cột 2 (V2).", "Dấu hiệu: yesterday, last night, ago, in 1999."],
                common_mistakes=["Did you went there? (Sai -> Did you go there?)"]
            ),
            GrammarRule(
                title="Comparative & Superlative (So sánh hơn & So sánh nhất)",
                category="adjectives",
                level="A2",
                explanation="Dùng để so sánh tính chất giữa 2 hay nhiều đối tượng.",
                examples=[
                    {"en": "This car is faster than that one.", "vi": "Xe này nhanh hơn xe kia."},
                    {"en": "She is the most intelligent student in class.", "vi": "Cô ấy là học sinh thông minh nhất lớp."}
                ],
                tips=["Tính từ ngắn: adj-er than / the adj-est.", "Tính từ dài: more adj than / the most adj."],
                common_mistakes=["More faster (Sai -> faster)."]
            ),
            GrammarRule(
                title="Modal Verbs: Can / Could / Should / Must",
                category="modals",
                level="A2",
                explanation="Động từ khuyết thiếu dùng để chỉ khả năng, lời khuyên, nghĩa vụ hoặc sự bắt buộc.",
                examples=[
                    {"en": "You should drink more water.", "vi": "Bạn nên uống nhiều nước hơn."},
                    {"en": "You must wear a seatbelt when driving.", "vi": "Bạn bắt buộc phải thắt dây an toàn khi lái xe."}
                ],
                tips=["Sau modal verb luôn là động từ nguyên thể không to (V-inf)."],
                common_mistakes=["He can speaks English (Sai -> He can speak English)."]
            ),
            # B1
            GrammarRule(
                title="Present Perfect (Thì hiện tại hoàn thành)",
                category="tenses",
                level="B1",
                explanation="Diễn tả hành động bắt đầu trong quá khứ và tiếp tục đến hiện tại, hoặc hành động vừa mới xảy ra để lại kết quả.",
                examples=[
                    {"en": "I have lived in Hanoi for 5 years.", "vi": "Tôi đã sống ở Hà Nội được 5 năm."},
                    {"en": "She has just finished her project.", "vi": "Cô ấy vừa mới hoàn thành dự án."}
                ],
                tips=["S + have/has + V3/ed.", "Dùng FOR + khoảng thời gian (for 2 years), SINCE + mốc thời gian (since 2020)."],
                common_mistakes=["I have see him yesterday (Sai -> I saw him yesterday - có yesterday không dùng hiện tại hoàn thành)."]
            ),
            GrammarRule(
                title="First & Second Conditionals (Câu điều kiện loại 1 & 2)",
                category="conditionals",
                level="B1",
                explanation="Loại 1 diễn tả sự việc có thể xảy ra ở tương lai. Loại 2 diễn tả giả thiết không có thật ở hiện tại.",
                examples=[
                    {"en": "If it rains tomorrow, we will stay home.", "vi": "Nếu mai trời mưa, chúng ta sẽ ở nhà."},
                    {"en": "If I were a millionaire, I would travel the world.", "vi": "Nếu tôi là triệu phú, tôi sẽ đi du lịch thế giới."}
                ],
                tips=["Loại 1: If S + V(s/es), S + will + V-inf.", "Loại 2: If S + V2/ed (be -> were), S + would + V-inf."],
                common_mistakes=["If I was you, I will go (Sai -> If I were you, I would go)."]
            ),
            GrammarRule(
                title="Passive Voice (Câu bị động)",
                category="sentence_structure",
                level="B1",
                explanation="Dùng khi muốn nhấn mạnh vào đối tượng chịu tác động của hành động thay vì người thực hiện.",
                examples=[
                    {"en": "This email was sent by the manager.", "vi": "Email này đã được gửi bởi người quản lý."},
                    {"en": "English is spoken all around the world.", "vi": "Tiếng Anh được nói trên toàn thế giới."}
                ],
                tips=["Cấu trúc chung: BE + V3/ed.", "Thì nào chia động từ BE theo thì đó."],
                common_mistakes=["The house built in 1990 (Sai -> The house was built in 1990)."]
            ),
            GrammarRule(
                title="Relative Clauses: Who / Which / That / Whose",
                category="clauses",
                level="B1",
                explanation="Mệnh đề quan hệ dùng để bổ nghĩa cho danh từ đứng trước nó.",
                examples=[
                    {"en": "The engineer who designed this app is very talented.", "vi": "Kỹ sư người đã thiết kế ứng dụng này rất tài năng."},
                    {"en": "This is the book which I bought yesterday.", "vi": "Đây là cuốn sách mà tôi đã mua hôm qua."}
                ],
                tips=["Who cho người, Which cho vật, That thay cho cả Who/Which trong mệnh đề xác định."],
                common_mistakes=["The man which is talking (Sai -> The man who is talking)."]
            ),
            # B2
            GrammarRule(
                title="Third Conditional (Câu điều kiện loại 3)",
                category="conditionals",
                level="B2",
                explanation="Diễn tả giả thiết trái ngược với sự thật trong quá khứ và kết quả của nó.",
                examples=[
                    {"en": "If you had studied harder, you would have passed the exam.", "vi": "Nếu bạn đã học chăm chỉ hơn, bạn đã đậu kỳ thi rồi."},
                    {"en": "If I hadn't missed the bus, I would have arrived on time.", "vi": "Nếu tôi không lỡ xe buýt, tôi đã đến đúng giờ."}
                ],
                tips=["If S + had + V3/ed, S + would/could/might + have + V3/ed."],
                common_mistakes=["If you would have told me (Sai -> If you had told me)."]
            ),
            GrammarRule(
                title="Reported Speech (Câu tường thuật)",
                category="sentence_structure",
                level="B2",
                explanation="Dùng để thuật lại lời nói của người khác, cần lùi một thì so với câu trực tiếp.",
                examples=[
                    {"en": "He said that he was working on a new project.", "vi": "Anh ấy nói rằng anh ấy đang làm một dự án mới."},
                    {"en": "She asked me where I lived.", "vi": "Cô ấy hỏi tôi sống ở đâu."}
                ],
                tips=["Lùi thì: Present -> Past, Past -> Past Perfect.", "Đổi đại từ và trạng từ thời gian (now -> then, tomorrow -> the next day)."],
                common_mistakes=["He said me that... (Sai -> He told me that... hoặc He said that...)."]
            ),
            GrammarRule(
                title="Wish / If only (Câu ước)",
                category="conditionals",
                level="B2",
                explanation="Dùng để bày tỏ sự tiếc nuối về điều không có thật ở hiện tại hoặc quá khứ.",
                examples=[
                    {"en": "I wish I knew his phone number.", "vi": "Tôi ước gì tôi biết số điện thoại của anh ấy (hiện tại không biết)."},
                    {"en": "She wishes she had accepted the job offer.", "vi": "Cô ấy ước rằng mình đã nhận lời mời công việc đó (quá khứ đã từ chối)."}
                ],
                tips=["Ước cho hiện tại: S + wish + S + V2/ed.", "Ước cho quá khứ: S + wish + S + had + V3/ed."],
                common_mistakes=["I wish I can go (Sai -> I wish I could go)."]
            ),
            # C1
            GrammarRule(
                title="Inversion (Đảo ngữ với phó từ phủ định)",
                category="advanced_structures",
                level="C1",
                explanation="Dùng để nhấn mạnh câu bằng cách đảo trợ động từ lên trước chủ ngữ sau các phó từ phủ định.",
                examples=[
                    {"en": "Never have I seen such a breathtaking performance.", "vi": "Chưa bao giờ tôi chứng kiến một màn trình diễn ngoạn mục đến vậy."},
                    {"en": "Not only did she win the scholarship, but she also got a job offer.", "vi": "Cô ấy không những đạt học bổng mà còn nhận được lời mời làm việc."}
                ],
                tips=["Các từ hay đảo ngữ: Never, Rarely, Seldom, No sooner... than, Hardley... when, Not only... but also."],
                common_mistakes=["Never I have seen (Sai -> Never have I seen)."]
            ),
            GrammarRule(
                title="Subjunctive Mood (Thể giả định)",
                category="advanced_structures",
                level="C1",
                explanation="Dùng sau các động từ như recommend, suggest, demand, insist... động từ trong mệnh đề that luôn ở dạng nguyên thể không to.",
                examples=[
                    {"en": "The doctor recommended that he stop smoking immediately.", "vi": "Bác sĩ khuyến nghị rằng anh ấy dừng hút thuốc ngay lập tức."},
                    {"en": "It is essential that every student be on time for the examination.", "vi": "Điều thiết yếu là mọi học sinh phải có mặt đúng giờ cho kỳ thi."}
                ],
                tips=["S1 + recommend/suggest/insist + that + S2 + V-inf (không chia -s dù S2 số ít)."],
                common_mistakes=["He recommended that she goes home (Sai -> she go home)."]
            ),
            # C2
            GrammarRule(
                title="Cleft Sentences (Câu chẻ - Nhấn mạnh đỉnh cao)",
                category="advanced_structures",
                level="C2",
                explanation="Cấu trúc It is/was ... that ... hoặc What ... is/was ... dùng để nhấn mạnh cực độ vào một thành phần trong câu (chủ ngữ, tân ngữ, thời gian, địa điểm).",
                examples=[
                    {"en": "It was in Paris that they first met ten years ago.", "vi": "Chính tại Paris mà họ đã gặp nhau lần đầu tiên mười năm trước."},
                    {"en": "What surprises me most is her incredible resilience under pressure.", "vi": "Điều làm tôi ngạc nhiên nhất chính là sự kiên cường đáng kinh ngạc của cô ấy dưới áp lực."}
                ],
                tips=["It is/was + thành phần nhấn mạnh + that/who + mệnh đề."],
                common_mistakes=["It was him who did it (Chuẩn trang trọng -> It was he who did it)."]
            ),
            GrammarRule(
                title="Participle Clauses (Mệnh đề phân từ rút gọn nâng cao)",
                category="advanced_structures",
                level="C2",
                explanation="Rút gọn mệnh đề cùng chủ ngữ để văn phong xúc tích, tự nhiên và học thuật hơn.",
                examples=[
                    {"en": "Having completed the comprehensive research, she published her findings in a prestigious journal.", "vi": "Sau khi hoàn tất nghiên cứu toàn diện, cô ấy đã công bố phát hiện trên một tạp chí danh giá."},
                    {"en": "Overwhelmed by the unexpected responsibilities, he sought guidance from his mentor.", "vi": "Bị choáng ngợp bởi những trách nhiệm bất ngờ, anh ấy đã tìm sự hướng dẫn từ cố vấn."}
                ],
                tips=["Dùng Having + V3/ed khi hành động xảy ra trước hành động chính.", "Dùng V3/ed cho nghĩa bị động."],
                common_mistakes=["Walking down the street, the tree fell (Lỗi sai chủ ngữ - Dangling participle)."]
            )
        ]

        # Check existing and insert
        for rule in grammar_rules:
            existing = (await db.execute(select(GrammarRule).where(GrammarRule.title == rule.title))).scalar_one_or_none()
            if not existing:
                db.add(rule)

        # 2. Listening Exercises (A1 - C2)
        listening_exercises = [
            # A1
            ListeningExercise(
                title="Introducing Yourself at a Café",
                description="Hội thoại chào hỏi cơ bản tại quán cà phê.",
                level="A1",
                topic="Daily Life",
                exercise_type="comprehension",
                duration_sec=60,
                transcript="Hello! My name is Anna. I am from Vietnam. I am a student at the university. I like drinking green tea and listening to music. Nice to meet you!",
                questions=[
                    {
                        "question": "Where is Anna from?",
                        "options": ["Thailand", "Vietnam", "Japan", "Korea"],
                        "answer": "Vietnam"
                    },
                    {
                        "question": "What does Anna like drinking?",
                        "options": ["Black coffee", "Green tea", "Orange juice", "Milk"],
                        "answer": "Green tea"
                    }
                ]
            ),
            ListeningExercise(
                title="Ordering Food in a Restaurant",
                description="Hội thoại gọi món đơn giản trong nhà hàng.",
                level="A1",
                topic="Food & Dining",
                exercise_type="comprehension",
                duration_sec=75,
                transcript="Waiter: Good evening! What would you like to order today?\nCustomer: Hello, I would like a chicken salad and a glass of mineral water, please.\nWaiter: Sure. Anything for dessert?\nCustomer: No thank you, that is all.",
                questions=[
                    {
                        "question": "What main dish does the customer order?",
                        "options": ["Beef steak", "Chicken salad", "Fish and chips", "Vegetable soup"],
                        "answer": "Chicken salad"
                    },
                    {
                        "question": "Does the customer order dessert?",
                        "options": ["Yes, ice cream", "Yes, chocolate cake", "No", "Yes, fruit salad"],
                        "answer": "No"
                    }
                ]
            ),
            # A2
            ListeningExercise(
                title="Planning a Weekend Trip",
                description="Hai người bạn lên kế hoạch đi du lịch cuối tuần.",
                level="A2",
                topic="Travel",
                exercise_type="comprehension",
                duration_sec=90,
                transcript="John: Hey Mary, do you have any plans for this Saturday?\nMary: Not yet, John. I was thinking of visiting the National Museum.\nJohn: That sounds great! Would you like to go together by train? The weather forecast says it will be sunny all weekend.\nMary: Wonderful! Let's meet at the central station at 9:00 AM.",
                questions=[
                    {
                        "question": "Where do they plan to visit?",
                        "options": ["The Art Gallery", "The National Museum", "The City Park", "The Beach"],
                        "answer": "The National Museum"
                    },
                    {
                        "question": "How will they travel there?",
                        "options": ["By bus", "By taxi", "By train", "By car"],
                        "answer": "By train"
                    },
                    {
                        "question": "What time will they meet?",
                        "options": ["8:00 AM", "9:00 AM", "10:00 AM", "9:30 AM"],
                        "answer": "9:00 AM"
                    }
                ]
            ),
            # B1
            ListeningExercise(
                title="Job Interview Preparation",
                description="Lời khuyên chuẩn bị phỏng vấn xin việc cho ứng viên.",
                level="B1",
                topic="Business & Career",
                exercise_type="comprehension",
                duration_sec=110,
                transcript="Welcome to our career advice workshop. When preparing for an English job interview, there are three golden rules. First, always research the company's background and products thoroughly. Second, practice answering common questions using the STAR method: Situation, Task, Action, and Result. Finally, dress professionally and arrive at least ten minutes before the scheduled time.",
                questions=[
                    {
                        "question": "What is the first golden rule mentioned?",
                        "options": ["Ask about salary", "Research the company's background", "Send a thank-you email", "Bring your diploma"],
                        "answer": "Research the company's background"
                    },
                    {
                        "question": "What does 'R' stand for in the STAR method?",
                        "options": ["Recommendation", "Responsibility", "Result", "Requirement"],
                        "answer": "Result"
                    },
                    {
                        "question": "How early should candidates arrive?",
                        "options": ["5 minutes", "10 minutes", "30 minutes", "1 hour"],
                        "answer": "10 minutes"
                    }
                ]
            ),
            # B2
            ListeningExercise(
                title="The Impact of Artificial Intelligence on Education",
                description="Bản tin phân tích sự thay đổi do trí tuệ nhân tạo mang lại trong ngành giáo dục.",
                level="B2",
                topic="Technology & Education",
                exercise_type="comprehension",
                duration_sec=140,
                transcript="Artificial intelligence is fundamentally transforming traditional educational methodologies. Personalized adaptive learning platforms can now evaluate a student's cognitive strengths and weaknesses in real time, tailoring curricula to optimize retention. However, educators emphasize that while AI serves as an indispensable auxiliary tool, it cannot replicate the emotional intelligence, empathetic mentorship, and moral guidance provided by human teachers.",
                questions=[
                    {
                        "question": "What is the key benefit of adaptive learning platforms mentioned?",
                        "options": ["They replace traditional schools", "They tailor curricula to individual cognitive strengths and weaknesses in real time", "They reduce tuition fees", "They eliminate the need for examinations"],
                        "answer": "They tailor curricula to individual cognitive strengths and weaknesses in real time"
                    },
                    {
                        "question": "According to educators, what can AI NOT replicate?",
                        "options": ["Grammar correction", "Emotional intelligence, empathetic mentorship, and moral guidance", "Instant translation", "24/7 availability"],
                        "answer": "Emotional intelligence, empathetic mentorship, and moral guidance"
                    }
                ]
            ),
            # C1
            ListeningExercise(
                title="Sustainable Architecture and Urban Renewal",
                description="Bài thuyết trình học thuật về kiến trúc bền vững và tái tạo đô thị.",
                level="C1",
                topic="Environment & Urban Planning",
                exercise_type="comprehension",
                duration_sec=180,
                transcript="Contemporary urban renewal projects increasingly incorporate biophilic design principles and zero-carbon building frameworks. By integrating vertical forests, passive solar orientation, and geothermal thermal regulation, modern architects strive to mitigate the urban heat island effect while fostering ecological biodiversity within densely populated metropolitan centers.",
                questions=[
                    {
                        "question": "What is one primary goal of incorporating biophilic design principles in urban renewal?",
                        "options": ["To maximize commercial advertising space", "To mitigate the urban heat island effect and foster biodiversity", "To reduce pedestrian walkway width", "To increase vehicle traffic flow"],
                        "answer": "To mitigate the urban heat island effect and foster biodiversity"
                    },
                    {
                        "question": "Which technologies are mentioned as part of zero-carbon frameworks?",
                        "options": ["Diesel generators", "Vertical forests, passive solar orientation, and geothermal regulation", "Nuclear reactors", "Coal-powered heating systems"],
                        "answer": "Vertical forests, passive solar orientation, and geothermal regulation"
                    }
                ]
            )
        ]

        for lex in listening_exercises:
            existing = (await db.execute(select(ListeningExercise).where(ListeningExercise.title == lex.title))).scalar_one_or_none()
            if not existing:
                db.add(lex)

        # 3. Reading Articles (A1 - C2)
        reading_articles = [
            # A1
            ReadingArticle(
                title="My Morning Routine",
                article_type="story",
                level="A1",
                topic="Daily Life",
                word_count=80,
                summary="Một câu chuyện ngắn gọn, dễ hiểu về các thói quen buổi sáng hàng ngày.",
                content="My name is David. I wake up at 6:30 AM every day. First, I brush my teeth and wash my face. Then, I have a healthy breakfast with milk, eggs, and toast. At 7:30 AM, I take the bus to school. I love learning English and making new friends.",
                questions=[
                    {
                        "question": "What time does David wake up?",
                        "options": ["6:00 AM", "6:30 AM", "7:00 AM", "7:30 AM"],
                        "answer": "6:30 AM"
                    },
                    {
                        "question": "How does David go to school?",
                        "options": ["By bicycle", "By car", "By bus", "On foot"],
                        "answer": "By bus"
                    }
                ]
            ),
            # A2
            ReadingArticle(
                title="The Benefits of Learning a Second Language",
                article_type="blog",
                level="A2",
                topic="Education",
                word_count=120,
                summary="Bài viết về những lợi ích tuyệt vời khi học thêm một ngoại ngữ mới.",
                content="Learning a second language is beneficial for people of all ages. Firstly, it improves your memory and problem-solving skills. Secondly, speaking English opens doors to better career opportunities and exciting travel experiences around the world. Moreover, learning a new language helps you understand different cultures and make international friends easily.",
                questions=[
                    {
                        "question": "What is one cognitive benefit of learning a second language?",
                        "options": ["It makes you sleep less", "It improves memory and problem-solving skills", "It reduces physical weight", "It replaces your first language"],
                        "answer": "It improves memory and problem-solving skills"
                    },
                    {
                        "question": "Why is speaking English good for travel?",
                        "options": ["It makes airline tickets free", "It opens doors to exciting travel experiences around the world", "It is required in all countries", "You don't need a passport"],
                        "answer": "It opens doors to exciting travel experiences around the world"
                    }
                ]
            ),
            # B1
            ReadingArticle(
                title="How Remote Work is Reshaping Global Careers",
                article_type="news",
                level="B1",
                topic="Business & Technology",
                word_count=160,
                summary="Phân tích xu hướng làm việc từ xa đang thay đổi thị trường lao động toàn cầu thế nào.",
                content="The rise of remote work has fundamentally transformed how global companies operate and recruit talent. Professionals no longer need to relocate to major financial hubs to work for leading international corporations. Instead, asynchronous communication tools and cloud-based collaboration software enable teams across different time zones to work seamlessly. While remote work offers unprecedented flexibility and work-life balance, it also presents challenges such as digital fatigue and the difficulty of maintaining cohesive corporate culture across distributed teams.",
                questions=[
                    {
                        "question": "What enables teams across different time zones to work seamlessly?",
                        "options": ["Frequent international flights", "Asynchronous communication tools and cloud-based software", "Working 24 hours a day", "Eliminating office hours"],
                        "answer": "Asynchronous communication tools and cloud-based software"
                    },
                    {
                        "question": "What is one challenge of remote work mentioned in the article?",
                        "options": ["High commuting costs", "Digital fatigue and maintaining cohesive corporate culture", "Lack of computers", "Strict dress codes"],
                        "answer": "Digital fatigue and maintaining cohesive corporate culture"
                    }
                ]
            ),
            # B2
            ReadingArticle(
                title="The Psychology of Habit Formation and Atomic Changes",
                article_type="academic",
                level="B2",
                topic="Psychology & Productivity",
                word_count=210,
                summary="Khám phá cơ chế tâm lý của việc hình thành thói quen và sức mạnh từ những thay đổi nhỏ.",
                content="Habit formation relies on a neurological loop consisting of three integral components: a cue, a routine, and a reward. According to behavioral psychologists, monumental life transformations rarely stem from sporadic bursts of radical willpower. Rather, sustainable self-improvement is achieved through 'atomic' habits—microscopic adjustments performed consistently over extended periods. By optimizing environmental cues and attaching positive reinforcement to desirable behaviors, individuals can effectively rewire their neural pathways, rendering productive actions automatic and effortless over time.",
                questions=[
                    {
                        "question": "What are the three components of the neurological habit loop?",
                        "options": ["Thought, speech, action", "Cue, routine, reward", "Effort, struggle, success", "Plan, execute, analyze"],
                        "answer": "Cue, routine, reward"
                    },
                    {
                        "question": "How is sustainable self-improvement achieved according to behavioral psychologists?",
                        "options": ["Through sporadic bursts of radical willpower", "Through microscopic adjustments performed consistently over extended periods", "By copying other people's routines without adaptation", "By working 16 hours every day"],
                        "answer": "Through microscopic adjustments performed consistently over extended periods"
                    }
                ]
            ),
            # C1
            ReadingArticle(
                title="Neuroplasticity and Language Acquisition in Adulthood",
                article_type="academic",
                level="C1",
                topic="Neuroscience & Linguistics",
                word_count=260,
                summary="Nghiên cứu khoa học thần kinh về tính linh hoạt của não bộ khi học ngoại ngữ ở tuổi trưởng thành.",
                content="Historically, linguistic consensus posited the existence of a rigid 'critical period' hypothesis, suggesting that native-like phonological and grammatical proficiency could only be acquired during early childhood. However, contemporary neuroimaging studies demonstrate that the adult brain retains remarkable neuroplasticity throughout the lifespan. Intensive bilingual immersion and structured cognitive stimulation stimulate synaptogenesis within the left inferior frontal gyrus and superior temporal cortex. Consequently, adult learners who utilize spaced repetition systems, contextual immersion, and phonetic training can achieve exceptional structural and communicative fluency that rivals early bilinguals.",
                questions=[
                    {
                        "question": "What did the traditional 'critical period' hypothesis suggest?",
                        "options": ["Adults learn languages faster than children", "Native-like proficiency could only be acquired during early childhood", "Language learning damages brain cells", "Grammar is unnecessary for communication"],
                        "answer": "Native-like proficiency could only be acquired during early childhood"
                    },
                    {
                        "question": "What does contemporary neuroimaging demonstrate regarding the adult brain?",
                        "options": ["It loses all learning capacity after age 25", "It retains remarkable neuroplasticity throughout the lifespan", "It cannot process phonetic distinctions", "It shrinks when learning a second language"],
                        "answer": "It retains remarkable neuroplasticity throughout the lifespan"
                    }
                ]
            )
        ]

        for art in reading_articles:
            existing = (await db.execute(select(ReadingArticle).where(ReadingArticle.title == art.title))).scalar_one_or_none()
            if not existing:
                db.add(art)

        await db.commit()
        print("[SUCCESS] Successfully seeded rich Practice Content (Grammar Rules, Listening Exercises, Reading Articles) for A1-C2!")

if __name__ == "__main__":
    asyncio.run(seed_practice())
