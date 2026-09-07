"""
scripts/flashcard_topics_def.py
Definition of all 50 Flashcard Topics with CEFR levels, categories, icons, colors, descriptions, and images.
Covers 30 Standard Topics (1-30) + 20 Advanced Specialized/Exam Topics (31-50).
"""

ALL_50_TOPICS_META = [
    # Tier 1: Core Daily & Social Life (A1 - B1)
    {
        "id": 1,
        "topic": "Daily Life & Routines",
        "icon": "☕",
        "color": "#f59e0b",
        "category": "Lifestyle",
        "level": "A1-A2",
        "description": "Thói quen hàng ngày, vệ sinh cá nhân, nếp sinh hoạt gia đình và nhịp sống đô thị.",
        "image_url": "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 2,
        "topic": "Food, Cooking & Dining",
        "icon": "🍳",
        "color": "#ef4444",
        "category": "Lifestyle",
        "level": "A1-B1",
        "description": "Nghệ thuật ẩm thực, phương pháp nấu nướng, nguyên liệu gia vị và trải nghiệm nhà hàng.",
        "image_url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 3,
        "topic": "Travel, Tourism & Transportation",
        "icon": "✈️",
        "color": "#3b82f6",
        "category": "Travel",
        "level": "A2-B1",
        "description": "Hành trình khám phá thế giới, thủ tục sân bay, khách sạn và các phương tiện giao thông.",
        "image_url": "https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 4,
        "topic": "Technology & Artificial Intelligence",
        "icon": "🤖",
        "color": "#8b5cf6",
        "category": "Technology",
        "level": "B2-C1",
        "description": "Công nghệ thông tin, trí tuệ nhân tạo, chuyển đổi số và các ứng dụng thông minh.",
        "image_url": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 5,
        "topic": "Business, Management & Workplace",
        "icon": "💼",
        "color": "#0ea5e9",
        "category": "Business",
        "level": "B1-B2",
        "description": "Kinh doanh thương mại, quản trị doanh nghiệp, văn hóa công sở và đàm phán hợp đồng.",
        "image_url": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 6,
        "topic": "Finance, Banking & Investment",
        "icon": "💳",
        "color": "#10b981",
        "category": "Finance",
        "level": "B2-C1",
        "description": "Tài chính tiền tệ, hệ thống ngân hàng, thị trường chứng khoán và quản lý tài sản cá nhân.",
        "image_url": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 7,
        "topic": "Health, Medicine & Wellness",
        "icon": "🩺",
        "color": "#ec4899",
        "category": "Health",
        "level": "B1-B2",
        "description": "Y tế cộng đồng, chăm sóc sức khỏe thể chất, dinh dưỡng, điều trị và rèn luyện lối sống.",
        "image_url": "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 8,
        "topic": "Education & Academic Life",
        "icon": "🎓",
        "color": "#6366f1",
        "category": "Academic",
        "level": "B1-B2",
        "description": "Môi trường học đường, giảng dạy, thi cử học thuật, phương pháp học và nghiên cứu khoa học.",
        "image_url": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 9,
        "topic": "Environment, Nature & Climate",
        "icon": "🌱",
        "color": "#14b8a6",
        "category": "Nature",
        "level": "B2-C1",
        "description": "Bảo tồn thiên nhiên, hệ sinh thái, biến đổi khí hậu toàn cầu và năng lượng tái tạo.",
        "image_url": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 10,
        "topic": "Shopping, Fashion & Retail",
        "icon": "🛍️",
        "color": "#f43f5e",
        "category": "Lifestyle",
        "level": "A1-A2",
        "description": "Thời trang may mặc, mua sắm bán lẻ, phong cách trang phục và thói quen tiêu dùng.",
        "image_url": "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=700&auto=format&fit=crop&q=80"
    },

    # Topics 11-20: Social, Culture, Arts & Entertainment
    {
        "id": 11,
        "topic": "Entertainment, Cinema & Arts",
        "icon": "🎬",
        "color": "#a855f7",
        "category": "Entertainment",
        "level": "A2-B1",
        "description": "Nghệ thuật điện ảnh, âm nhạc, sân khấu biểu diễn, hội họa và các phương tiện giải trí.",
        "image_url": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 12,
        "topic": "Sports, Fitness & Outdoor Activities",
        "icon": "⚽",
        "color": "#eab308",
        "category": "Sports",
        "level": "A2-B1",
        "description": "Các môn thể thao đối kháng, thể hình Gym, vận động ngoài trời và thi đấu thể thao.",
        "image_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 13,
        "topic": "Emotions, Personality & Character",
        "icon": "🎭",
        "color": "#d946ef",
        "category": "Psychology",
        "level": "B1-B2",
        "description": "Cung bậc cảm xúc con người, phẩm chất tính cách, tâm lý xã hội và hành vi ứng xử.",
        "image_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 14,
        "topic": "Family, Relationships & Society",
        "icon": "👨‍👩‍👧‍👦",
        "color": "#f97316",
        "category": "Social",
        "level": "A1-A2",
        "description": "Mối quan hệ gia đình, tình bạn bè, hôn nhân, tương tác xã hội và cộng đồng dân cư.",
        "image_url": "https://images.unsplash.com/photo-1511895426328-dc8714191300?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 15,
        "topic": "Media, News & Communication",
        "icon": "📡",
        "color": "#06b6d4",
        "category": "Media",
        "level": "B1-B2",
        "description": "Báo chí truyền hình, mạng xã hội, phát thanh số và các kênh truyền thông đại chúng.",
        "image_url": "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 16,
        "topic": "Law, Crime & Justice",
        "icon": "⚖️",
        "color": "#64748b",
        "category": "Society",
        "level": "B2-C1",
        "description": "Hệ thống tư pháp pháp luật, quyền công dân, xét xử tại tòa án và phòng chống tội phạm.",
        "image_url": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 17,
        "topic": "Politics, Diplomacy & Global Affairs",
        "icon": "🏛️",
        "color": "#475569",
        "category": "Politics",
        "level": "B2-C1",
        "description": "Thể chế chính trị, quan hệ bang giao quốc tế, bầu cử chính phủ và hiệp ước toàn cầu.",
        "image_url": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 18,
        "topic": "Science, Space & Astronomy",
        "icon": "🔭",
        "color": "#4f46e5",
        "category": "Science",
        "level": "B2-C1",
        "description": "Khám phá vũ trụ bao la, hệ mặt trời, vật lý thiên văn và nghiên cứu khoa học cơ bản.",
        "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 19,
        "topic": "Architecture, Housing & Real Estate",
        "icon": "🏢",
        "color": "#78716c",
        "category": "Industry",
        "level": "B1-B2",
        "description": "Kiến trúc công trình xây dựng, thiết kế nội thất, thị trường bất động sản và nhà ở.",
        "image_url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 20,
        "topic": "Job Interview & Career Development",
        "icon": "🎯",
        "color": "#0284c7",
        "category": "Career",
        "level": "B1-B2",
        "description": "Kỹ năng phỏng vấn xin việc, đàm phán lương bổng, viết CV và lộ trình thăng tiến nghề nghiệp.",
        "image_url": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=700&auto=format&fit=crop&q=80"
    },

    # Topics 21-30: Business, Society, Psychology & Idioms
    {
        "id": 21,
        "topic": "Marketing, Advertising & Branding",
        "icon": "📢",
        "color": "#f59e0b",
        "category": "Marketing",
        "level": "B1-B2",
        "description": "Chiến lược tiếp thị số, định vị thương hiệu, nghiên cứu thị trường và quảng bá sản phẩm.",
        "image_url": "https://images.unsplash.com/photo-1533750349088-cd871a92f312?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 22,
        "topic": "Logistics, Supply Chain & E-commerce",
        "icon": "📦",
        "color": "#ea580c",
        "category": "Business",
        "level": "B1-B2",
        "description": "Quản trị chuỗi cung ứng, vận tải kho bãi hàng hóa, xuất nhập khẩu và thương mại điện tử.",
        "image_url": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 23,
        "topic": "Hospitality, Hotel & Customer Service",
        "icon": "🛎️",
        "color": "#e11d48",
        "category": "Service",
        "level": "A2-B1",
        "description": "Nghiệp vụ lưu trú khách sạn, kỹ năng phục vụ khách hàng, quầy lễ tân và dịch vụ lữ hành.",
        "image_url": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 24,
        "topic": "Culture, Traditions & Festivals",
        "icon": "🏮",
        "color": "#b91c1c",
        "category": "Culture",
        "level": "A2-B1",
        "description": "Di sản văn hóa dân tộc, lễ hội truyền thống, phong tục tập quán và tín ngưỡng tâm linh.",
        "image_url": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 25,
        "topic": "Hobbies, Leisure & Creative Skills",
        "icon": "🎨",
        "color": "#9333ea",
        "category": "Leisure",
        "level": "A1-A2",
        "description": "Sở thích đam mê cá nhân, rèn luyện kỹ năng khéo tay, thủ công mỹ nghệ và sáng tác.",
        "image_url": "https://images.unsplash.com/photo-1460661419201-fd4cecdf8a8b?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 26,
        "topic": "Weather, Seasons & Natural Disasters",
        "icon": "⛈️",
        "color": "#0284c7",
        "category": "Nature",
        "level": "A1-A2",
        "description": "Khí tượng thủy văn, bốn mùa luân chuyển, hiện tượng thời tiết cực đoan và thiên tai.",
        "image_url": "https://images.unsplash.com/photo-1534088568595-a066f410bcda?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 27,
        "topic": "Philosophy, Psychology & Mindfulness",
        "icon": "🧘",
        "color": "#059669",
        "category": "Mind",
        "level": "B2-C1",
        "description": "Tư tưởng triết học, tâm lý học hành vi, rèn luyện chánh niệm và sức khỏe tinh thần.",
        "image_url": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 28,
        "topic": "Animals, Wildlife & Marine Biology",
        "icon": "🐬",
        "color": "#0891b2",
        "category": "Nature",
        "level": "A2-B1",
        "description": "Thế giới muông thú hoang dã, sinh vật biển đại dương sâu thẳm và bảo tồn động vật.",
        "image_url": "https://images.unsplash.com/photo-1535268647677-300dbf3d78d1?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 29,
        "topic": "Innovation, Startups & Entrepreneurship",
        "icon": "🚀",
        "color": "#7c3aed",
        "category": "Business",
        "level": "B2-C1",
        "description": "Khởi nghiệp đổi mới sáng tạo, vườn ươm công nghệ, gọi vốn mạo hiểm và tăng trưởng đột phá.",
        "image_url": "https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 30,
        "topic": "Idioms, Phrasal Verbs & Slang for Speaking",
        "icon": "💬",
        "color": "#db2777",
        "category": "Communication",
        "level": "B2-C1",
        "description": "Thành ngữ tiếng Anh đời thường, cụm động từ tự nhiên và tiếng lóng giao tiếp bản xứ chuẩn.",
        "image_url": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=700&auto=format&fit=crop&q=80"
    },

    # Topics 31-40: Specialized Engineering, Science & Tech (C1 - C2)
    {
        "id": 31,
        "topic": "Software Engineering & Full-Stack Development",
        "icon": "💻",
        "color": "#2563eb",
        "category": "Technology",
        "level": "C1-C2",
        "description": "Kỹ nghệ phần mềm, kiến trúc vi dịch vụ, mô hình dữ liệu, Git CI/CD và lập trình web.",
        "image_url": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 32,
        "topic": "Machine Learning, Deep Learning & LLMs",
        "icon": "🧠",
        "color": "#7c3aed",
        "category": "Technology",
        "level": "C1-C2",
        "description": "Học máy chuyên sâu, mạng thần kinh nhân tạo, mô hình ngôn ngữ lớn LLM và thị giác máy tính.",
        "image_url": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 33,
        "topic": "Cloud Computing, DevOps & Microservices",
        "icon": "☁️",
        "color": "#0284c7",
        "category": "Technology",
        "level": "C1-C2",
        "description": "Điện toán đám mây AWS/GCP, điều phối vùng chứa Docker/Kubernetes và hạ tầng CI/CD.",
        "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 34,
        "topic": "Cybersecurity, Ethical Hacking & Cryptography",
        "icon": "🛡️",
        "color": "#dc2626",
        "category": "Technology",
        "level": "C1-C2",
        "description": "An ninh không gian mạng, mật mã học hiện đại, kiểm thử xâm nhập và phòng vệ mạng dữ liệu.",
        "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 35,
        "topic": "Data Science, Big Data & Analytics",
        "icon": "📊",
        "color": "#059669",
        "category": "Technology",
        "level": "C1-C2",
        "description": "Khoa học dữ liệu lớn, phân tích định lượng thống kê, trực quan hóa và khai phá dữ liệu.",
        "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 36,
        "topic": "Medicine, Clinical Diagnostics & Surgery",
        "icon": "🏥",
        "color": "#e11d48",
        "category": "Specialized",
        "level": "C1-C2",
        "description": "Y khoa lâm sàng, chẩn đoán hình ảnh bệnh lý, kỹ thuật phẫu thuật ngoại khoa và hồi sức cấp cứu.",
        "image_url": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 37,
        "topic": "Pharmacology, Biotechnology & Genetics",
        "icon": "🧬",
        "color": "#0d9488",
        "category": "Specialized",
        "level": "C1-C2",
        "description": "Dược lý học phát triển thuốc mới, công nghệ sinh học phân tử, liệu pháp gen và tế bào gốc.",
        "image_url": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 38,
        "topic": "Corporate Law, Intellectual Property & Litigation",
        "icon": "📜",
        "color": "#b45309",
        "category": "Specialized",
        "level": "C1-C2",
        "description": "Luật doanh nghiệp quốc tế, sở hữu trí tuệ, tranh tụng tòa án và trọng tài thương mại.",
        "image_url": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 39,
        "topic": "Investment Banking, Stocks & Capital Markets",
        "icon": "📈",
        "color": "#15803d",
        "category": "Business",
        "level": "C1-C2",
        "description": "Ngân hàng đầu tư định chế, quỹ phòng hộ, phát hành IPO, sáp nhập M&A và thị trường vốn.",
        "image_url": "https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 40,
        "topic": "Aviation, Flight Operations & Aerospace",
        "icon": "🛩️",
        "color": "#0369a1",
        "category": "Specialized",
        "level": "C1-C2",
        "description": "Kỹ thuật hàng không thương mại, điều hành bay buồng lái, kiểm soát không lưu và khí động học.",
        "image_url": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=700&auto=format&fit=crop&q=80"
    },

    # Topics 41-50: Heavy Industry, Diplomacy & Advanced Exams (C1 - C2)
    {
        "id": 41,
        "topic": "Civil Engineering, Structural Design & Urban Planning",
        "icon": "🏗️",
        "color": "#ca8a04",
        "category": "Specialized",
        "level": "C1-C2",
        "description": "Kỹ thuật xây dựng kết cấu dân dụng, quy hoạch đô thị thông minh và hạ tầng giao thông cầu đường.",
        "image_url": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 42,
        "topic": "Industrial Robotics, Automation & Smart Manufacturing",
        "icon": "🏭",
        "color": "#475569",
        "category": "Specialized",
        "level": "C1-C2",
        "description": "Tự động hóa nhà máy thông minh Industry 4.0, cánh tay robot công nghiệp và quản trị Six Sigma.",
        "image_url": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 43,
        "topic": "Maritime Logistics, Shipping & Port Operations",
        "icon": "🚢",
        "color": "#0e7490",
        "category": "Specialized",
        "level": "C1-C2",
        "description": "Vận tải đường biển quốc tế, khai thác cảng container, bảo hiểm hàng hải và thủ tục hải quan.",
        "image_url": "https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 44,
        "topic": "International Relations, Geopolitics & Diplomacy",
        "icon": "🌐",
        "color": "#4338ca",
        "category": "Specialized",
        "level": "C1-C2",
        "description": "Ngoại giao đa phương, địa chính trị toàn cầu, đàm phán giải quyết xung đột và an ninh quốc tế.",
        "image_url": "https://images.unsplash.com/photo-1526470608268-f674ce90ebd4?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 45,
        "topic": "TOEIC Business: Contracts, Sales & Negotiation",
        "icon": "📝",
        "color": "#c026d3",
        "category": "Exam",
        "level": "B2-C1",
        "description": "Từ vựng trọng tâm TOEIC 850+: Đàm phán giá, điều khoản hợp đồng thương mại và chào hàng B2B.",
        "image_url": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 46,
        "topic": "TOEIC Corporate: HR, Personnel & Office Operations",
        "icon": "👥",
        "color": "#9333ea",
        "category": "Exam",
        "level": "B2-C1",
        "description": "Từ vựng trọng tâm TOEIC 850+: Quản trị nhân sự, phúc lợi nhân viên, quy chế và vận hành công ty.",
        "image_url": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 47,
        "topic": "IELTS Academic Band 8.0+: Academic Vocabulary & Collocations",
        "icon": "📚",
        "color": "#dc2626",
        "category": "Exam",
        "level": "C1-C2",
        "description": "Từ vựng học thuật đỉnh cao IELTS Band 8.0+: Cụm từ hàn lâm, thuật ngữ văn bản luận điểm chặt chẽ.",
        "image_url": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 48,
        "topic": "IELTS Scientific Research, Methodology & Critical Thinking",
        "icon": "🔬",
        "color": "#0284c7",
        "category": "Exam",
        "level": "C1-C2",
        "description": "Từ vựng IELTS Task 2 & Reading chuyên khảo: Phương pháp nghiên cứu khoa học và tư duy phản biện.",
        "image_url": "https://images.unsplash.com/photo-1507668077129-56e32842fceb?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 49,
        "topic": "IELTS Social Issues: Demographic Shifts & Urbanization",
        "icon": "🏙️",
        "color": "#d97706",
        "category": "Exam",
        "level": "C1-C2",
        "description": "Từ vựng IELTS chuyên đề Xã hội học: Biến động nhân khẩu học, già hóa dân số và làn sóng đô thị hóa.",
        "image_url": "https://images.unsplash.com/photo-1477959858617-67f30bc75b82?w=700&auto=format&fit=crop&q=80"
    },
    {
        "id": 50,
        "topic": "High-Level Debate, Rhetoric & Philosophical Discourse",
        "icon": "🏛️",
        "color": "#4f46e5",
        "category": "Exam",
        "level": "C1-C2",
        "description": "Nghệ thuật hùng biện đỉnh cao, phân tích ngụy biện logic, thuật tu từ và diễn ngôn triết học.",
        "image_url": "https://images.unsplash.com/photo-1544717305-2782549b5136?w=700&auto=format&fit=crop&q=80"
    }
]
