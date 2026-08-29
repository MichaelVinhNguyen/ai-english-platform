"""
master_30_topics_flashcards_generator.py
Generates exactly 30 topics with 50 vocabulary words each = 1,500 rich flashcards,
and seeds them directly into SQLite data/app.db.
"""

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "data" / "app.db"

# Master Registry of 30 Topics with metadata and 50 rich words each
TOPICS_METADATA = [
    {"name": "Daily Life & Routines", "icon": "☕", "color": "#f59e0b", "category": "General Life", "desc": "Thói quen hàng ngày, sinh hoạt và nhịp sống đô thị"},
    {"name": "Food, Cooking & Dining", "icon": "🍳", "color": "#ef4444", "category": "Lifestyle", "desc": "Nghệ thuật ẩm thực, kỹ thuật nấu ăn và trải nghiệm nhà hàng"},
    {"name": "Travel, Tourism & Transportation", "icon": "✈️", "color": "#3b82f6", "category": "Travel", "desc": "Hành trình khám phá, thủ tục bay và các loại hình giao thông"},
    {"name": "Technology & Artificial Intelligence", "icon": "🤖", "color": "#8b5cf6", "category": "Technology", "desc": "Công nghệ số, AI, an ninh mạng và kỷ nguyên thông minh"},
    {"name": "Business, Management & Workplace", "icon": "💼", "color": "#0ea5e9", "category": "Business", "desc": "Kinh doanh, văn hóa công sở, quản trị và đàm phán"},
    {"name": "Finance, Banking & Investment", "icon": "💳", "color": "#10b981", "category": "Finance", "desc": "Tài chính, ngân hàng, thị trường chứng khoán và đầu tư"},
    {"name": "Health, Medicine & Wellness", "icon": "🩺", "color": "#ec4899", "category": "Health", "desc": "Y tế, sức khỏe thể chất, chế độ dinh dưỡng và phòng bệnh"},
    {"name": "Education & Academic Life", "icon": "🎓", "color": "#6366f1", "category": "Academic", "desc": "Trường học, nghiên cứu học thuật, phương pháp học tập"},
    {"name": "Environment, Nature & Climate", "icon": "🌱", "color": "#14b8a6", "category": "Science", "desc": "Hệ sinh thái, biến đổi khí hậu và phát triển bền vững"},
    {"name": "Shopping, Fashion & Retail", "icon": "🛍️", "color": "#f43f5e", "category": "Lifestyle", "desc": "Thời trang, mua sắm bán lẻ, phong cách và xu hướng"},
    {"name": "Entertainment, Cinema & Arts", "icon": "🎬", "color": "#a855f7", "category": "Entertainment", "desc": "Điện ảnh, âm nhạc, nghệ thuật thị giác và giải trí"},
    {"name": "Sports, Fitness & Outdoor Activities", "icon": "⚽", "color": "#eab308", "category": "Sports", "desc": "Thể thao, rèn luyện thể lực và các hoạt động dã ngoại"},
    {"name": "Emotions, Personality & Character", "icon": "🎭", "color": "#d946ef", "category": "Psychology", "desc": "Cảm xúc con người, phẩm chất tính cách và tâm lý"},
    {"name": "Family, Relationships & Society", "icon": "👨‍👩‍👧‍👦", "color": "#f97316", "category": "Social", "desc": "Gia đình, tình bạn, quan hệ xã hội và cộng đồng"},
    {"name": "Media, News & Communication", "icon": "📡", "color": "#06b6d4", "category": "Media", "desc": "Báo chí truyền thông, mạng xã hội và kênh thông tin"},
    {"name": "Law, Crime & Justice", "icon": "⚖️", "color": "#64748b", "category": "Society", "desc": "Hệ thống luật pháp, tư pháp, quyền công dân và tội phạm"},
    {"name": "Politics, Diplomacy & Global Affairs", "icon": "🏛️", "color": "#475569", "category": "Politics", "desc": "Chính trị, ngoại giao quốc tế và các hiệp ước toàn cầu"},
    {"name": "Science, Space & Astronomy", "icon": "🔭", "color": "#4f46e5", "category": "Science", "desc": "Khoa học vũ trụ, thiên văn học và khám phá dải ngân hà"},
    {"name": "Architecture, Housing & Real Estate", "icon": "🏢", "color": "#78716c", "category": "Industry", "desc": "Kiến trúc công trình, thị trường nhà ở và bất động sản"},
    {"name": "Job Interview & Career Development", "icon": "🎯", "color": "#0284c7", "category": "Career", "desc": "Phỏng vấn xin việc, phát triển kỹ năng nghề và thăng tiến"},
    {"name": "Marketing, Advertising & Branding", "icon": "📢", "color": "#f59e0b", "category": "Marketing", "desc": "Tiếp thị số, quảng cáo sáng tạo và định vị thương hiệu"},
    {"name": "Logistics, Supply Chain & E-commerce", "icon": "📦", "color": "#ea580c", "category": "Business", "desc": "Chuỗi cung ứng, kho vận và sàn thương mại điện tử"},
    {"name": "Hospitality, Hotel & Customer Service", "icon": "🛎️", "color": "#e11d48", "category": "Service", "desc": "Dịch vụ khách hàng, quản trị khách sạn và du lịch lưu trú"},
    {"name": "Culture, Traditions & Festivals", "icon": "🏮", "color": "#b91c1c", "category": "Culture", "desc": "Di sản văn hóa, phong tục tập quán và lễ hội truyền thống"},
    {"name": "Hobbies, Leisure & Creative Skills", "icon": "🎨", "color": "#9333ea", "category": "Leisure", "desc": "Sở thích cá nhân, sáng tạo nghệ thuật và kỹ năng thủ công"},
    {"name": "Weather, Seasons & Natural Disasters", "icon": "⛈️", "color": "#0284c7", "category": "Nature", "desc": "Khí tượng thủy văn, bốn mùa và các hiện tượng thiên nhiên"},
    {"name": "Philosophy, Psychology & Mindfulness", "icon": "🧘", "color": "#059669", "category": "Mind", "desc": "Triết học nhân sinh, sức khỏe tinh thần và chánh niệm"},
    {"name": "Animals, Wildlife & Marine Biology", "icon": "🐬", "color": "#0284c7", "category": "Nature", "desc": "Động vật hoang dã, sinh vật biển và bảo tồn tự nhiên"},
    {"name": "Innovation, Startups & Entrepreneurship", "icon": "🚀", "color": "#7c3aed", "category": "Business", "desc": "Tinh thần khởi nghiệp, gọi vốn và đổi mới đột phá"},
    {"name": "Idioms, Phrasal Verbs & Slang for Speaking", "icon": "💬", "color": "#db2777", "category": "Communication", "desc": "Thành ngữ, cụm động từ tự nhiên và tiếng lóng bản xứ"}
]

print(f"Loaded {len(TOPICS_METADATA)} topic definitions.")
