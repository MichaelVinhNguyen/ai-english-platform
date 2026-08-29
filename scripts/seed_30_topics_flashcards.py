"""
seed_30_topics_flashcards.py
Master seed script for 30 topics x 50 words = 1,500 rich flashcard words.
Inserts/updates database data/app.db and exports JSON dataset.
"""

import io
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
import sys

# Ensure UTF-8 output on Windows
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_DIR))

from scripts.topics_data_1_to_10 import TOPICS_1_TO_10
from scripts.topics_data_11_to_20 import TOPICS_11_TO_20
from scripts.topics_data_21_to_30 import TOPICS_21_TO_30

DB_PATH = BASE_DIR / "data" / "app.db"
JSON_OUT_PATH = BASE_DIR / "data" / "vocabulary" / "flashcards_30_topics_1500_words.json"

# Topic metadata dictionary (Category, Icon, Theme Color, Vietnamese Description)
TOPICS_INFO = {
    "Daily Life & Routines": {"icon": "☕", "color": "#f59e0b", "category": "General Life", "desc": "Thói quen hàng ngày, sinh hoạt và nhịp sống đô thị"},
    "Food, Cooking & Dining": {"icon": "🍳", "color": "#ef4444", "category": "Lifestyle", "desc": "Nghệ thuật ẩm thực, kỹ thuật nấu ăn và trải nghiệm nhà hàng"},
    "Travel, Tourism & Transportation": {"icon": "✈️", "color": "#3b82f6", "category": "Travel", "desc": "Hành trình khám phá, thủ tục bay và các loại hình giao thông"},
    "Technology & Artificial Intelligence": {"icon": "🤖", "color": "#8b5cf6", "category": "Technology", "desc": "Công nghệ số, AI, an ninh mạng và kỷ nguyên thông minh"},
    "Business, Management & Workplace": {"icon": "💼", "color": "#0ea5e9", "category": "Business", "desc": "Kinh doanh, văn hóa công sở, quản trị và đàm phán"},
    "Finance, Banking & Investment": {"icon": "💳", "color": "#10b981", "category": "Finance", "desc": "Tài chính, ngân hàng, thị trường chứng khoán và đầu tư"},
    "Health, Medicine & Wellness": {"icon": "🩺", "color": "#ec4899", "category": "Health", "desc": "Y tế, sức khỏe thể chất, chế độ dinh dưỡng và phòng bệnh"},
    "Education & Academic Life": {"icon": "🎓", "color": "#6366f1", "category": "Academic", "desc": "Trường học, nghiên cứu học thuật, phương pháp học tập"},
    "Environment, Nature & Climate": {"icon": "🌱", "color": "#14b8a6", "category": "Science", "desc": "Hệ sinh thái, biến đổi khí hậu và phát triển bền vững"},
    "Shopping, Fashion & Retail": {"icon": "🛍️", "color": "#f43f5e", "category": "Lifestyle", "desc": "Thời trang, mua sắm bán lẻ, phong cách và xu hướng"},
    "Entertainment, Cinema & Arts": {"icon": "🎬", "color": "#a855f7", "category": "Entertainment", "desc": "Điện ảnh, âm nhạc, nghệ thuật thị giác và giải trí"},
    "Sports, Fitness & Outdoor Activities": {"icon": "⚽", "color": "#eab308", "category": "Sports", "desc": "Thể thao, rèn luyện thể lực và các hoạt động dã ngoại"},
    "Emotions, Personality & Character": {"icon": "🎭", "color": "#d946ef", "category": "Psychology", "desc": "Cảm xúc con người, phẩm chất tính cách và tâm lý"},
    "Family, Relationships & Society": {"icon": "👨‍👩‍👧‍👦", "color": "#f97316", "category": "Social", "desc": "Gia đình, tình bạn, quan hệ xã hội và cộng đồng"},
    "Media, News & Communication": {"icon": "📡", "color": "#06b6d4", "category": "Media", "desc": "Báo chí truyền thông, mạng xã hội và kênh thông tin"},
    "Law, Crime & Justice": {"icon": "⚖️", "color": "#64748b", "category": "Society", "desc": "Hệ thống luật pháp, tư pháp, quyền công dân và tội phạm"},
    "Politics, Diplomacy & Global Affairs": {"icon": "🏛️", "color": "#475569", "category": "Politics", "desc": "Chính trị, ngoại giao quốc tế và các hiệp ước toàn cầu"},
    "Science, Space & Astronomy": {"icon": "🔭", "color": "#4f46e5", "category": "Science", "desc": "Khoa học vũ trụ, thiên văn học và khám phá dải ngân hà"},
    "Architecture, Housing & Real Estate": {"icon": "🏢", "color": "#78716c", "category": "Industry", "desc": "Kiến trúc công trình, thị trường nhà ở và bất động sản"},
    "Job Interview & Career Development": {"icon": "🎯", "color": "#0284c7", "category": "Career", "desc": "Phỏng vấn xin việc, phát triển kỹ năng nghề và thăng tiến"},
    "Marketing, Advertising & Branding": {"icon": "📢", "color": "#f59e0b", "category": "Marketing", "desc": "Tiếp thị số, quảng cáo sáng tạo và định vị thương hiệu"},
    "Logistics, Supply Chain & E-commerce": {"icon": "📦", "color": "#ea580c", "category": "Business", "desc": "Chuỗi cung ứng, kho vận và sàn thương mại điện tử"},
    "Hospitality, Hotel & Customer Service": {"icon": "🛎️", "color": "#e11d48", "category": "Service", "desc": "Dịch vụ khách hàng, quản trị khách sạn và du lịch lưu trú"},
    "Culture, Traditions & Festivals": {"icon": "🏮", "color": "#b91c1c", "category": "Culture", "desc": "Di sản văn hóa, phong tục tập quán và lễ hội truyền thống"},
    "Hobbies, Leisure & Creative Skills": {"icon": "🎨", "color": "#9333ea", "category": "Leisure", "desc": "Sở thích cá nhân, sáng tạo nghệ thuật và kỹ năng thủ công"},
    "Weather, Seasons & Natural Disasters": {"icon": "⛈️", "color": "#0284c7", "category": "Nature", "desc": "Khí tượng thủy văn, bốn mùa và các hiện tượng thiên nhiên"},
    "Philosophy, Psychology & Mindfulness": {"icon": "🧘", "color": "#059669", "category": "Mind", "desc": "Triết học nhân sinh, sức khỏe tinh thần và chánh niệm"},
    "Animals, Wildlife & Marine Biology": {"icon": "🐬", "color": "#0284c7", "category": "Nature", "desc": "Động vật hoang dã, sinh vật biển và bảo tồn tự nhiên"},
    "Innovation, Startups & Entrepreneurship": {"icon": "🚀", "color": "#7c3aed", "category": "Business", "desc": "Tinh thần khởi nghiệp, gọi vốn và đổi mới đột phá"},
    "Idioms, Phrasal Verbs & Slang for Speaking": {"icon": "💬", "color": "#db2777", "category": "Communication", "desc": "Thành ngữ, cụm động từ tự nhiên và tiếng lóng bản xứ"}
}

def seed_flashcards():
    # Merge all 30 topics
    all_topics = {}
    all_topics.update(TOPICS_1_TO_10)
    all_topics.update(TOPICS_11_TO_20)
    all_topics.update(TOPICS_21_TO_30)

    print(f"Total topics to seed: {len(all_topics)}")
    total_words = 0

    json_export = []

    for topic_name, words in all_topics.items():
        meta = TOPICS_INFO.get(topic_name, {"icon": "📚", "color": "#3b82f6", "category": "General", "desc": ""})
        topic_entry = {
            "topic": topic_name,
            "icon": meta["icon"],
            "color": meta["color"],
            "category": meta["category"],
            "description": meta["desc"],
            "total_words": len(words),
            "words": []
        }

        for item in words:
            word, ipa, word_type, level, def_vi, def_en, examples, synonyms, collocations = item
            word_dict = {
                "word": word,
                "ipa": ipa,
                "word_type": word_type,
                "level": level,
                "topic": topic_name,
                "definition_vi": def_vi,
                "definition_en": def_en,
                "examples": examples,
                "synonyms": synonyms,
                "collocations": collocations
            }
            topic_entry["words"].append(word_dict)
            total_words += 1

        json_export.append(topic_entry)

    # Save to JSON
    JSON_OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(JSON_OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(json_export, f, ensure_ascii=False, indent=2)
    print(f"Exported JSON dataset with {len(json_export)} topics and {total_words} words to {JSON_OUT_PATH}")

    # Seed into SQLite DB
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Ensure vocabularies table exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vocabularies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word VARCHAR(200) NOT NULL,
            ipa VARCHAR(200),
            word_type VARCHAR(30),
            definition_en TEXT,
            definition_vi TEXT,
            examples JSON,
            synonyms JSON,
            antonyms JSON,
            collocations JSON,
            audio_url VARCHAR(500),
            image_url VARCHAR(500),
            level VARCHAR(5),
            topic VARCHAR(100),
            created_at DATETIME
        )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS ix_vocabularies_word ON vocabularies (word)")

    now_iso = datetime.now(timezone.utc).isoformat()
    inserted_count = 0
    updated_count = 0

    for topic_item in json_export:
        t_name = topic_item["topic"]
        for w in topic_item["words"]:
            # Check if this exact word in this topic exists
            cursor.execute("SELECT id FROM vocabularies WHERE word = ? AND topic = ?", (w["word"], t_name))
            row = cursor.fetchone()

            ex_json = json.dumps(w["examples"], ensure_ascii=False)
            syn_json = json.dumps(w["synonyms"], ensure_ascii=False)
            col_json = json.dumps(w["collocations"], ensure_ascii=False)

            if row:
                v_id = row[0]
                cursor.execute("""
                    UPDATE vocabularies
                    SET ipa = ?, word_type = ?, definition_vi = ?, definition_en = ?,
                        examples = ?, synonyms = ?, collocations = ?, level = ?
                    WHERE id = ?
                """, (w["ipa"], w["word_type"], w["definition_vi"], w["definition_en"],
                      ex_json, syn_json, col_json, w["level"], v_id))
                updated_count += 1
            else:
                cursor.execute("""
                    INSERT INTO vocabularies (word, ipa, word_type, definition_vi, definition_en, examples, synonyms, antonyms, collocations, audio_url, image_url, level, topic, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    w["word"], w["ipa"], w["word_type"], w["definition_vi"], w["definition_en"],
                    ex_json, syn_json, json.dumps([]), col_json, None, None,
                    w["level"], t_name, now_iso
                ))
                inserted_count += 1

    conn.commit()

    # Verification Query
    cursor.execute("SELECT count(*) FROM vocabularies")
    total_in_db = cursor.fetchone()[0]

    cursor.execute("SELECT topic, count(*) FROM vocabularies WHERE topic IN ({seq}) GROUP BY topic".format(
        seq=",".join(["?"] * len(all_topics))
    ), list(all_topics.keys()))
    topic_counts = cursor.fetchall()

    conn.close()

    print(f"\n[OK] Database Seeding Complete!")
    print(f"Inserted: {inserted_count}, Updated: {updated_count}")
    print(f"Total vocabulary in DB: {total_in_db}")
    print(f"\nBreakdown of the 30 Flashcard Topics:")
    for t_name, cnt in topic_counts:
        meta = TOPICS_INFO.get(t_name, {})
        icon = meta.get("icon", "📚")
        print(f"  {icon} {t_name}: {cnt} words")

if __name__ == "__main__":
    seed_flashcards()
