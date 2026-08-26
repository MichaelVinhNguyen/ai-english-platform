import asyncio
import json
from pathlib import Path
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.database import AsyncSessionLocal
from backend.database.models import (
    Vocabulary, GrammarRule, ReadingArticle, ListeningExercise,
    Course, Lesson, Badge, Mission
)

# Dummy rich data for seeding
VOCABULARY_DATA = [
    {"word": "abandon", "ipa": "/əˈbændən/", "word_type": "verb", "level": "B2", "topic": "Daily Life", "definition_en": "to leave a place, thing, or person, usually for ever", "definition_vi": "từ bỏ, bỏ rơi", "examples": ["As a baby he was abandoned by his mother.", "We had to abandon the car."], "synonyms": ["leave", "desert"]},
    {"word": "ability", "ipa": "/əˈbɪləti/", "word_type": "noun", "level": "A2", "topic": "Daily Life", "definition_en": "the physical or mental power or skill needed to do something", "definition_vi": "khả năng, năng lực", "examples": ["She has a remarkable ability to learn languages.", "I have no ability in music."], "synonyms": ["capability", "capacity"]},
    {"word": "absent", "ipa": "/ˈæbsənt/", "word_type": "adjective", "level": "A2", "topic": "Education", "definition_en": "not in the place where you are expected to be", "definition_vi": "vắng mặt", "examples": ["John has been absent from school for three days.", "Why were you absent?"], "synonyms": ["missing", "away"]},
    {"word": "absorb", "ipa": "/əbˈzɔːb/", "word_type": "verb", "level": "B2", "topic": "Science", "definition_en": "to take something in, especially gradually", "definition_vi": "hấp thụ, tiếp thu", "examples": ["Plants absorb carbon dioxide.", "It's hard to absorb so much information."], "synonyms": ["soak up", "assimilate"]},
    {"word": "accelerate", "ipa": "/əkˈseləreɪt/", "word_type": "verb", "level": "C1", "topic": "Technology", "definition_en": "to happen or make something happen sooner or faster", "definition_vi": "tăng tốc, đẩy nhanh", "examples": ["Inflation is likely to accelerate.", "They use special chemicals to accelerate the growth of crops."], "synonyms": ["speed up", "hasten"]},
    {"word": "accommodate", "ipa": "/əˈkɒmədeɪt/", "word_type": "verb", "level": "B2", "topic": "Travel", "definition_en": "to provide with a place to live or to be stored in", "definition_vi": "cung cấp chỗ ở, chứa đựng", "examples": ["The hotel can accommodate up to 500 guests.", "We always try to accommodate our clients' needs."], "synonyms": ["house", "contain"]},
    # A few more to have varied levels
    {"word": "cat", "ipa": "/kæt/", "word_type": "noun", "level": "A1", "topic": "Animals", "definition_en": "a small animal with fur, four legs, a tail, and claws", "definition_vi": "con mèo", "examples": ["I have a pet cat.", "The cat is sleeping."], "synonyms": ["feline"]},
    {"word": "ubiquitous", "ipa": "/juːˈbɪkwɪtəs/", "word_type": "adjective", "level": "C2", "topic": "Technology", "definition_en": "seeming to be everywhere", "definition_vi": "có mặt ở khắp nơi", "examples": ["Mobile phones are ubiquitous.", "The ubiquitous presence of fast food."], "synonyms": ["omnipresent", "everywhere"]},
]

GRAMMAR_DATA = [
    {"title": "Present Simple (Thì Hiện Tại Đơn)", "category": "Tenses", "level": "A1", "explanation": "Thì hiện tại đơn dùng để diễn tả một sự thật hiển nhiên, một chân lý, hoặc một thói quen ở hiện tại.", "examples": [{"en": "I get up early every day.", "vi": "Tôi thức dậy sớm mỗi ngày."}, {"en": "The sun rises in the east.", "vi": "Mặt trời mọc ở đằng đông."}], "tips": ["Thêm 's' hoặc 'es' vào động từ đi sau chủ ngữ ngôi thứ 3 số ít (he, she, it)."]},
    {"title": "Present Continuous (Thì Hiện Tại Tiếp Diễn)", "category": "Tenses", "level": "A1", "explanation": "Thì hiện tại tiếp diễn dùng để diễn tả hành động đang xảy ra tại thời điểm nói hoặc xung quanh thời điểm nói.", "examples": [{"en": "I am studying English now.", "vi": "Tôi đang học tiếng Anh bây giờ."}, {"en": "She is working on a new project.", "vi": "Cô ấy đang làm một dự án mới."}], "tips": ["Cấu trúc: am/is/are + V-ing"]},
    {"title": "Past Simple (Thì Quá Khứ Đơn)", "category": "Tenses", "level": "A2", "explanation": "Thì quá khứ đơn diễn tả hành động đã xảy ra và kết thúc trong quá khứ.", "examples": [{"en": "I visited Paris last year.", "vi": "Tôi đã thăm Paris năm ngoái."}, {"en": "They didn't go to the party.", "vi": "Họ đã không đi dự tiệc."}], "tips": ["Động từ thường thêm '-ed' (ngoại trừ động từ bất quy tắc)."]},
    {"title": "First Conditional (Câu Điều Kiện Loại 1)", "category": "Conditionals", "level": "B1", "explanation": "Câu điều kiện loại 1 diễn tả một sự việc có thể xảy ra ở hiện tại hoặc tương lai.", "examples": [{"en": "If it rains, we will stay at home.", "vi": "Nếu trời mưa, chúng tôi sẽ ở nhà."}, {"en": "If you study hard, you will pass the exam.", "vi": "Nếu bạn học chăm, bạn sẽ qua kỳ thi."}], "tips": ["Mệnh đề If dùng thì Hiện tại đơn, mệnh đề chính dùng Tương lai đơn (will + V)."]},
    {"title": "Passive Voice (Câu Bị Động)", "category": "Passive Voice", "level": "B1", "explanation": "Câu bị động được dùng khi muốn nhấn mạnh vào đối tượng chịu tác động của hành động, thay vì người/vật thực hiện hành động.", "examples": [{"en": "The letter was written by Mary.", "vi": "Bức thư được viết bởi Mary."}, {"en": "A new hospital is being built in the city.", "vi": "Một bệnh viện mới đang được xây dựng trong thành phố."}], "tips": ["Cấu trúc chung: be + V3/ed"]},
]

READING_DATA = [
    {
        "title": "A Day in the Life of a Software Engineer",
        "level": "B1",
        "topic": "Technology",
        "article_type": "blog",
        "word_count": 250,
        "content": "Being a software engineer involves more than just writing code. A typical day starts with a short meeting called a 'stand-up'. In this meeting, team members discuss what they did yesterday, what they will do today, and any problems they are facing. \n\nAfter the meeting, the real work begins. Engineers spend hours writing, testing, and fixing code. They often work together in pairs to solve complex problems. This is called 'pair programming'. \n\nHowever, it's not all about coding. Communication is a big part of the job. Engineers need to write documentation, reply to emails, and talk to clients or other departments to understand their needs. \n\nLearning is also continuous. Technology changes quickly, so engineers must spend time reading articles, watching tutorials, or taking courses to keep their skills up to date. \n\nAt the end of the day, a good software engineer leaves work feeling challenged but satisfied, knowing they have built something useful.",
        "summary": "This article describes the daily routine of a software engineer, highlighting that the job involves meetings, communication, and continuous learning, not just writing code.",
        "questions": [
            {"question": "What happens during a 'stand-up' meeting?", "options": ["People eat breakfast.", "Team members discuss their tasks.", "They write code together.", "They talk to clients."], "answer": "Team members discuss their tasks.", "explanation": "The text says: 'In this meeting, team members discuss what they did yesterday, what they will do today, and any problems they are facing.'"}
        ]
    }
]

LISTENING_DATA = [
    {
        "title": "Ordering Food in a Restaurant",
        "level": "A2",
        "topic": "Daily Life",
        "exercise_type": "comprehension",
        "transcript": "Waiter: Hello, are you ready to order?\nCustomer: Yes, I'd like the grilled chicken salad, please.\nWaiter: Would you like anything to drink?\nCustomer: Just water with ice, thank you.\nWaiter: Any dessert?\nCustomer: No, that will be all for now.",
        "description": "A short conversation between a waiter and a customer in a restaurant."
    }
]

COURSES_DATA = [
    {
        "title": "English for Beginners",
        "description": "A complete guide for complete beginners. Learn basic vocabulary and grammar to start speaking confidently.",
        "level": "A1",
        "category": "general",
        "total_lessons": 5,
        "is_published": True,
        "lessons": [
            {"title": "Greetings and Introductions", "lesson_type": "vocabulary", "content": "Hello, Hi, Good morning. My name is..."},
            {"title": "Verb 'To Be'", "lesson_type": "grammar", "content": "I am, you are, he/she/it is."},
            {"title": "Numbers and Colors", "lesson_type": "vocabulary", "content": "One, two, three... Red, blue, green..."},
            {"title": "Simple Present: Daily Routine", "lesson_type": "grammar", "content": "I wake up at 7 AM. I eat breakfast."},
            {"title": "Basic Conversation Practice", "lesson_type": "speaking", "content": "Practice introducing yourself."}
        ]
    },
    {
        "title": "Business English Intermediate",
        "description": "Improve your professional communication skills. Perfect for emails, meetings, and presentations.",
        "level": "B1",
        "category": "business",
        "total_lessons": 3,
        "is_published": True,
        "lessons": [
            {"title": "Writing Professional Emails", "lesson_type": "writing", "content": "Dear [Name], I am writing to inform you..."},
            {"title": "Participating in Meetings", "lesson_type": "speaking", "content": "I agree with you. In my opinion..."},
            {"title": "Business Vocabulary", "lesson_type": "vocabulary", "content": "Negotiate, budget, strategy, deadline."}
        ]
    }
]


async def seed_data(db: AsyncSession):
    # Check if data already exists to prevent duplicate seeding
    result = await db.execute(select(Vocabulary).limit(1))
    if result.scalar_one_or_none():
        print("Data already seeded.")
        return

    print("Seeding Vocabulary...")
    for vocab_item in VOCABULARY_DATA:
        db.add(Vocabulary(**vocab_item))
    
    print("Seeding Grammar...")
    for grammar_item in GRAMMAR_DATA:
        db.add(GrammarRule(**grammar_item))
        
    print("Seeding Reading...")
    for reading_item in READING_DATA:
        db.add(ReadingArticle(**reading_item))
        
    print("Seeding Listening...")
    for list_item in LISTENING_DATA:
        db.add(ListeningExercise(**list_item))

    print("Seeding Courses...")
    for course_data in COURSES_DATA:
        lessons_data = course_data.pop("lessons", [])
        course = Course(**course_data)
        db.add(course)
        await db.flush() # To get course.id
        for i, lesson_item in enumerate(lessons_data):
            lesson = Lesson(course_id=course.id, order_index=i, **lesson_item)
            db.add(lesson)

    print("Seeding Gamification (Badges & Missions)...")
    badges = [
        {"name": "First Step", "description": "Hoàn thành bài học đầu tiên", "icon": "🎓", "category": "general", "xp_reward": 50},
        {"name": "Vocab Master", "description": "Học 100 từ vựng", "icon": "📚", "category": "vocab", "xp_reward": 100},
        {"name": "3-Day Streak", "description": "Học liên tục 3 ngày", "icon": "🔥", "category": "streak", "xp_reward": 150},
    ]
    for b in badges:
        db.add(Badge(**b))
        
    missions = [
        {"title": "Học 5 từ mới", "description": "Hoàn thành học 5 từ vựng mới hôm nay", "mission_type": "daily", "xp_reward": 20},
        {"title": "Đạt 100 điểm ngữ pháp", "description": "Làm bài tập ngữ pháp để tích lũy điểm", "mission_type": "weekly", "xp_reward": 100},
    ]
    for m in missions:
        db.add(Mission(**m))

    await db.commit()
    print("Rich data seeded successfully!")

async def run_seed():
    from backend.database.database import init_db
    await init_db()  # Make sure tables are created before seeding
    async with AsyncSessionLocal() as session:
        await seed_data(session)

if __name__ == "__main__":
    asyncio.run(run_seed())
