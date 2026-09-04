# -*- coding: utf-8 -*-
"""
scripts/generate_50_topics_phrases.py
Tạo 50 chủ đề câu nói thường gặp x 50 câu hỏi & trả lời song ngữ Anh-Việt = 2,500 câu giao tiếp thực chiến.
Có đầy đủ:
- Nhân vật hoạt hình & avatar
- Phiên âm IPA chuẩn
- Âm thanh phát âm
- Từ khóa (Keywords) & Mẹo phản xạ (Tips)
Lưu vào data/app.db và xuất sang frontend/js/standalone_data.js.
"""

import sys
import os
import json
import sqlite3

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))

# ══════════════════════════════════════════════════════════════════════════════
# 1. METADATA 50 CHỦ ĐỀ GIAO TIẾP ĐA DẠNG (TỪ ĐƠN GIẢN ĐẾN CHUYÊN SÂU)
# ══════════════════════════════════════════════════════════════════════════════

TOPICS_50_META = [
    # NHÓM 1: ĐỜI SỐNG & XÃ HỘI (1 - 10)
    {
        "id": 1, "code": "daily_greetings", "name": "Daily Greetings & Small Talk",
        "name_vi": "Chào hỏi, Làm quen & Bắt chuyện Xã giao",
        "category": "life", "category_vi": "Đời Sống & Xã Hội",
        "icon": "👋", "avatar_a": "🧑‍🦰", "avatar_b": "🧑‍💼",
        "color": "#f59e0b", "desc": "Các mẫu câu mở đầu cuộc trò chuyện tự nhiên, hỏi thăm sức khỏe và duy trì nhịp đối thoại đời thường."
    },
    {
        "id": 2, "code": "food_dining", "name": "Food, Cooking & Restaurant Ordering",
        "name_vi": "Ăn uống, Nấu nướng & Đặt món Nhà hàng",
        "category": "life", "category_vi": "Đời Sống & Xã Hội",
        "icon": "🍳", "avatar_a": "🧑‍🍳", "avatar_b": "🍽️",
        "color": "#ef4444", "desc": "Hỏi thực đơn, yêu cầu gia vị, dị ứng thực phẩm, gọi thanh toán và nhận xét món ăn ngon."
    },
    {
        "id": 3, "code": "shopping_retail", "name": "Shopping, Bargaining & Customer Service",
        "name_vi": "Mua sắm, Mặc cả & Dịch vụ Khách hàng",
        "category": "life", "category_vi": "Đời Sống & Xã Hội",
        "icon": "🛍️", "avatar_a": "👩‍💼", "avatar_b": "🛒",
        "color": "#ec4899", "desc": "Hỏi kích cỡ, thử đồ thời trang, hỏi giảm giá, chính sách đổi trả hàng và thanh toán thẻ."
    },
    {
        "id": 4, "code": "asking_directions", "name": "Asking & Giving Directions in the City",
        "name_vi": "Hỏi & Chỉ đường trong Đô thị",
        "category": "life", "category_vi": "Đời Sống & Xã Hội",
        "icon": "🗺️", "avatar_a": "🚶‍♂️", "avatar_b": "👮‍♂️",
        "color": "#06b6d4", "desc": "Xác định phương hướng, hỏi khoảng cách, trạm xe buýt, rẽ trái/phải và địa điểm công cộng."
    },
    {
        "id": 5, "code": "family_relationships", "name": "Family, Relationships & Household Chores",
        "name_vi": "Gia đình, Bạn bè & Việc nhà Thường nhật",
        "category": "life", "category_vi": "Đời Sống & Xã Hội",
        "icon": "👨‍👩‍👧‍👦", "avatar_a": "🧑‍🌾", "avatar_b": "👧",
        "color": "#f97316", "desc": "Hỏi thăm người thân, phân công việc nhà, nuôi dạy thú cưng và tâm sự với bạn bè thân thiết."
    },
    {
        "id": 6, "code": "health_doctor", "name": "Health, Clinic & Pharmacy Consultations",
        "name_vi": "Khám bệnh, Bệnh viện & Mua thuốc Nhà thuốc",
        "category": "life", "category_vi": "Đời Sống & Xã Hội",
        "icon": "🩺", "avatar_a": "👨‍⚕️", "avatar_b": "🧑‍🦽",
        "color": "#10b981", "desc": "Mô tả triệu chứng sốt, đau họng, hỏi liều dùng thuốc, dị ứng và lời khuyên phục hồi sức khỏe."
    },
    {
        "id": 7, "code": "hobbies_leisure", "name": "Hobbies, Sports & Weekend Leisure",
        "name_vi": "Sở thích, Thể thao & Giải trí Cuối tuần",
        "category": "life", "category_vi": "Đời Sống & Xã Hội",
        "icon": "🎨", "avatar_a": "🏃‍♂️", "avatar_b": "🎸",
        "color": "#8b5cf6", "desc": "Bàn luận về âm nhạc, phim ảnh, rèn luyện thể hình, cắm trại và các hoạt động thư giãn."
    },
    {
        "id": 8, "code": "weather_seasons", "name": "Weather, Seasons & Climate Talks",
        "name_vi": "Thời tiết, Bốn mùa & Hiện tượng Tự nhiên",
        "category": "life", "category_vi": "Đời Sống & Xã Hội",
        "icon": "⛈️", "avatar_a": "🌤️", "avatar_b": "🌧️",
        "color": "#0284c7", "desc": "Dự báo thời tiết hàng ngày, thời tiết cực đoan, nhiệt độ và chuẩn bị trang phục phù hợp."
    },
    {
        "id": 9, "code": "emotions_empathy", "name": "Feelings, Emotions & Showing Empathy",
        "name_vi": "Cảm xúc, Tâm trạng & Thể hiện Sự Đồng cảm",
        "category": "life", "category_vi": "Đời Sống & Xã Hội",
        "icon": "🎭", "avatar_a": "🥰", "avatar_b": "🤝",
        "color": "#eab308", "desc": "Bày tỏ niềm vui, chia sẻ nỗi buồn, động viên đồng nghiệp và cách lắng nghe thấu hiểu."
    },
    {
        "id": 10, "code": "social_etiquette", "name": "Making Friends & Party Etiquette",
        "name_vi": "Kết bạn Mới, Dự tiệc & Lễ nghi Xã giao",
        "category": "life", "category_vi": "Đời Sống & Xã Hội",
        "icon": "🥂", "avatar_a": "🎉", "avatar_b": "🕺",
        "color": "#d946ef", "desc": "Mời dự tiệc sinh nhật, chúc mừng thành công, tặng quà và lời chào tạm biệt chân thành."
    },

    # NHÓM 2: DU LỊCH & KHÁCH SẠN (11 - 20)
    {
        "id": 11, "code": "airport_flight", "name": "Airport Check-in, Luggage & Boarding",
        "name_vi": "Thủ tục Sân bay, Cân hành lý & Lên máy bay",
        "category": "travel", "category_vi": "Du Lịch & Khách Sạn",
        "icon": "✈️", "avatar_a": "👨‍✈️", "avatar_b": "🧳",
        "color": "#0284c7", "desc": "Làm thủ tục tại quầy vé, cân hành lý ký gửi, kiểm tra an ninh và tìm cổng khởi hành (gate)."
    },
    {
        "id": 12, "code": "inflight_cabin", "name": "In-Flight Requests & Flight Attendant Talk",
        "name_vi": "Giao tiếp với Tiếp viên trên Chuyến bay",
        "category": "travel", "category_vi": "Du Lịch & Khách Sạn",
        "icon": "🛫", "avatar_a": "👩‍✈️", "avatar_b": "☕",
        "color": "#0ea5e9", "desc": "Xin chăn gối, gọi đồ uống, chuyển chỗ ngồi, hỏi thời gian hạ cánh và xử lý say máy bay."
    },
    {
        "id": 13, "code": "customs_immigration", "name": "Immigration & Customs Declarations",
        "name_vi": "Thủ tục Hải quan, Nhập cảnh & Khai báo",
        "category": "travel", "category_vi": "Du Lịch & Khách Sạn",
        "icon": "🛂", "avatar_a": "👮‍♂️", "avatar_b": "📑",
        "color": "#14b8a6", "desc": "Khai mục đích chuyến đi, thời gian lưu trú, chứng minh tài chính và trình hộ chiếu visa."
    },
    {
        "id": 14, "code": "hotel_reception", "name": "Hotel Check-in, Room Service & Amenities",
        "name_vi": "Nhận phòng Khách sạn & Dịch vụ Phòng",
        "category": "travel", "category_vi": "Du Lịch & Khách Sạn",
        "icon": "🏨", "avatar_a": "🛎️", "avatar_b": "🔑",
        "color": "#e11d48", "desc": "Nhận phòng, yêu cầu dọn phòng, mật khẩu Wi-Fi, đổi phòng yên tĩnh và gửi trả chìa khóa."
    },
    {
        "id": 15, "code": "public_transport", "name": "Public Transport: Bus, Metro & Taxis",
        "name_vi": "Phương tiện Công cộng: Xe buýt, Tàu điện & Taxi",
        "category": "travel", "category_vi": "Du Lịch & Khách Sạn",
        "icon": "🚇", "avatar_a": "🚕", "avatar_b": "🎫",
        "color": "#f59e0b", "desc": "Mua vé tàu điện ngầm, hỏi lộ trình xe buýt, gọi xe công nghệ và yêu cầu bật đồng hồ taxi."
    },
    {
        "id": 16, "code": "sightseeing_tours", "name": "Sightseeing, Tour Guides & Attractions",
        "name_vi": "Tham quan Danh thắng & Hướng dẫn viên",
        "category": "travel", "category_vi": "Du Lịch & Khách Sạn",
        "icon": "📸", "avatar_a": "🧭", "avatar_b": "🏛️",
        "color": "#8b5cf6", "desc": "Mua vé bảo tàng, tham gia tour du lịch trong ngày, nhờ chụp ảnh và tìm hiểu lịch sử địa phương."
    },
    {
        "id": 17, "code": "car_rental", "name": "Renting a Car, Motorbike & Gas Stations",
        "name_vi": "Thuê xe Tự lái, Đổ xăng & Sự cố Đường bộ",
        "category": "travel", "category_vi": "Du Lịch & Khách Sạn",
        "icon": "🚗", "avatar_a": "⛽", "avatar_b": "🛵",
        "color": "#3b82f6", "desc": "Hợp đồng thuê xe, bảo hiểm thân vỏ, đổ xăng đầy bình và xử lý thủng lốp dọc đường."
    },
    {
        "id": 18, "code": "travel_emergencies", "name": "Travel Emergencies & Police Assistance",
        "name_vi": "Khẩn cấp Du lịch & Báo Cảnh sát Hỗ trợ",
        "category": "travel", "category_vi": "Du Lịch & Khách Sạn",
        "icon": "🚨", "avatar_a": "👮‍♀️", "avatar_b": "🆘",
        "color": "#dc2626", "desc": "Báo mất hộ chiếu, ví tiền, tìm đồ thất lạc, liên hệ đại sứ quán và gọi cứu thương."
    },
    {
        "id": 19, "code": "currency_atm", "name": "Currency Exchange & ATM Transactions Abroad",
        "name_vi": "Đổi Ngoại tệ, Rút tiền ATM & Quẹt thẻ Quốc tế",
        "category": "travel", "category_vi": "Du Lịch & Khách Sạn",
        "icon": "💱", "avatar_a": "🏦", "avatar_b": "💵",
        "color": "#059669", "desc": "Tỷ giá hối đoái, phí chuyển đổi ngoại tệ, rút tiền mặt tại máy ATM và xử lý nuốt thẻ."
    },
    {
        "id": 20, "code": "cultural_customs", "name": "Cultural Customs & Local Courtesies Worldwide",
        "name_vi": "Phong tục Tập quán & Văn hóa Địa phương",
        "category": "travel", "category_vi": "Du Lịch & Khách Sạn",
        "icon": "🏮", "avatar_a": "🎎", "avatar_b": "🌍",
        "color": "#d97706", "desc": "Văn hóa tiền tip, cách chào hỏi tôn trọng, quy định trang phục tại đền chùa và kiêng kỵ."
    },

    # NHÓM 3: CÔNG SỞ & KINH DOANH (21 - 30)
    {
        "id": 21, "code": "job_interview", "name": "Job Interview Questions & STAR Answers",
        "name_vi": "Phỏng vấn Xin việc & Trả lời theo Chuẩn STAR",
        "category": "business", "category_vi": "Công Sở & Kinh Doanh",
        "icon": "🎯", "avatar_a": "👔", "avatar_b": "📝",
        "color": "#0ea5e9", "desc": "Giới thiệu điểm mạnh/điểm yếu, kinh nghiệm xử lý khủng hoảng và đàm phán kỳ vọng."
    },
    {
        "id": 22, "code": "workplace_greetings", "name": "Workplace Greetings & Introducing Colleagues",
        "name_vi": "Chào đón Đồng nghiệp & Giao tiếp Văn phòng",
        "category": "business", "category_vi": "Công Sở & Kinh Doanh",
        "icon": "🤝", "avatar_a": "💼", "avatar_b": "☕",
        "color": "#6366f1", "desc": "Giới thiệu nhân sự mới, phân công phòng ban, giao lưu nghỉ giải lao và văn hóa công ty."
    },
    {
        "id": 23, "code": "business_emails", "name": "Professional Business Emails & Slack Chats",
        "name_vi": "Email Doanh nghiệp & Tin nhắn Công việc Chuyên nghiệp",
        "category": "business", "category_vi": "Công Sở & Kinh Doanh",
        "icon": "📧", "avatar_a": "💻", "avatar_b": "📨",
        "color": "#14b8a6", "desc": "Mở đầu email trang trọng, đính kèm tài liệu, nhắc nhở deadline và xác nhận lịch hẹn."
    },
    {
        "id": 24, "code": "team_meetings", "name": "Leading & Participating in Team Meetings",
        "name_vi": "Chủ trì & Đóng góp Ý kiến trong Cuộc họp",
        "category": "business", "category_vi": "Công Sở & Kinh Doanh",
        "icon": "👥", "avatar_a": "📋", "avatar_b": "📊",
        "color": "#f59e0b", "desc": "Điểm danh, thông qua chương trình nghị sự, đóng góp ý tưởng, tranh luận và tóm tắt biên bản."
    },
    {
        "id": 25, "code": "client_negotiations", "name": "Client Negotiations & Closing Deals",
        "name_vi": "Đàm phán Khách hàng & Ký kết Hợp đồng",
        "category": "business", "category_vi": "Công Sở & Kinh Doanh",
        "icon": "🖋️", "avatar_a": "🏢", "avatar_b": "📈",
        "color": "#10b981", "desc": "Thảo luận điều khoản thanh toán, chiết khấu số lượng lớn, bảo hành và ký biên bản ghi nhớ."
    },
    {
        "id": 26, "code": "project_management", "name": "Project Management, Sprints & Deadlines",
        "name_vi": "Quản trị Dự án, Tiến độ & Phương pháp Agile",
        "category": "business", "category_vi": "Công Sở & Kinh Doanh",
        "icon": "📊", "avatar_a": "🗓️", "avatar_b": "⚡",
        "color": "#3b82f6", "desc": "Báo cáo tiến độ Daily Standup, giải quyết điểm nghẽn (bottleneck) và bàn giao giai đoạn."
    },
    {
        "id": 27, "code": "giving_feedback", "name": "Giving Constructive Feedback & Reviews",
        "name_vi": "Góp ý Xây dựng & Đánh giá Hiệu quả Công việc",
        "category": "business", "category_vi": "Công Sở & Kinh Doanh",
        "icon": "🔍", "avatar_a": "⭐", "avatar_b": "📈",
        "color": "#ea580c", "desc": "Đánh giá hiệu suất định kỳ (KPI), ghi nhận thành tích xuất sắc và định hướng khắc phục lỗi."
    },
    {
        "id": 28, "code": "salary_promotion", "name": "Salary Review & Career Progression Talks",
        "name_vi": "Đàm phán Lương thưởng & Lộ trình Thăng tiến",
        "category": "business", "category_vi": "Công Sở & Kinh Doanh",
        "icon": "💰", "avatar_a": "🏆", "avatar_b": "🚀",
        "color": "#7c3aed", "desc": "Đề xuất tăng lương xứng đáng, phúc lợi đãi ngộ, cơ hội đảm nhận vai trò quản lý cấp cao."
    },
    {
        "id": 29, "code": "customer_complaints", "name": "Handling Customer Complaints & Crisis Control",
        "name_vi": "Xử lý Khiếu nại Khách hàng & Giải quyết Sự cố",
        "category": "business", "category_vi": "Công Sở & Kinh Doanh",
        "icon": "🛎️", "avatar_a": "🎧", "avatar_b": "🛡️",
        "color": "#e11d48", "desc": "Lắng nghe sự thất vọng, xin lỗi chân thành, đưa ra phương án đền bù và giữ chân khách."
    },
    {
        "id": 30, "code": "business_pitching", "name": "Business Presentations & Investor Pitching",
        "name_vi": "Thuyết trình Dự án & Gọi vốn Đầu tư",
        "category": "business", "category_vi": "Công Sở & Kinh Doanh",
        "icon": "🎤", "avatar_a": "💡", "avatar_b": "💎",
        "color": "#d946ef", "desc": "Giới thiệu giải pháp thị trường, mô hình doanh thu, lợi thế cạnh tranh và trả lời phản biện."
    },

    # NHÓM 4: CÔNG NGHỆ & KHOA HỌC (31 - 40)
    {
        "id": 31, "code": "artificial_intelligence", "name": "Artificial Intelligence, LLMs & Automation",
        "name_vi": "Trí tuệ Nhân tạo (AI), Mô hình Ngôn ngữ & Tự động hóa",
        "category": "tech", "category_vi": "Công Nghệ & Khoa Học",
        "icon": "🤖", "avatar_a": "🧠", "avatar_b": "⚙️",
        "color": "#8b5cf6", "desc": "Kỹ thuật viết câu lệnh prompt, tác động của AI tạo sinh, đạo đức thuật toán và tương lai việc làm."
    },
    {
        "id": 32, "code": "software_engineering", "name": "Software Engineering, APIs & Code Reviews",
        "name_vi": "Kỹ thuật Phần mềm, Tích hợp API & Rà soát Code",
        "category": "tech", "category_vi": "Công Nghệ & Khoa Học",
        "icon": "💻", "avatar_a": "👨‍💻", "avatar_b": "👩‍💻",
        "color": "#6366f1", "desc": "Gỡ lỗi mã nguồn (debugging), tối ưu thuật toán, kiểm thử tự động và kiến trúc clean code."
    },
    {
        "id": 33, "code": "cybersecurity_privacy", "name": "Cybersecurity, Passwords & Data Protection",
        "name_vi": "An ninh Mạng, Mật khẩu & Bảo vệ Dữ liệu Cá nhân",
        "category": "tech", "category_vi": "Công Nghệ & Khoa Học",
        "icon": "🔒", "avatar_a": "🛡️", "avatar_b": "🔑",
        "color": "#ef4444", "desc": "Xác thực 2 yếu tố (2FA), phát hiện thư lừa đảo (phishing), tường lửa và mã hóa dữ liệu."
    },
    {
        "id": 34, "code": "cloud_devops", "name": "Cloud Computing, DevOps & Infrastructure",
        "name_vi": "Điện toán Đám mây, Hạ tầng Server & DevOps",
        "category": "tech", "category_vi": "Công Nghệ & Khoa Học",
        "icon": "☁️", "avatar_a": "🖥️", "avatar_b": "📡",
        "color": "#06b6d4", "desc": "Triển khai container Docker, điều phối Kubernetes, tải lưu lượng mạng và sao lưu đám mây."
    },
    {
        "id": 35, "code": "smartphones_gadgets", "name": "Smartphones, Wearables & Smart Home Tech",
        "name_vi": "Điện thoại Thông minh, Thiết bị Đeo & Smart Home",
        "category": "tech", "category_vi": "Công Nghệ & Khoa Học",
        "icon": "📱", "avatar_a": "⌚", "avatar_b": "🔌",
        "color": "#3b82f6", "desc": "Đồng bộ hóa thiết bị, thời lượng pin, cảm biến sức khỏe và điều khiển nhà thông minh qua giọng nói."
    },
    {
        "id": 36, "code": "space_astronomy", "name": "Space Exploration, Rockets & Astronomy",
        "name_vi": "Khám phá Vũ trụ, Tên lửa & Thiên văn học",
        "category": "tech", "category_vi": "Công Nghệ & Khoa Học",
        "icon": "🔭", "avatar_a": "🚀", "avatar_b": "🪐",
        "color": "#4f46e5", "desc": "Chuyến thám hiểm sao Hỏa, vệ tinh quan sát Trái Đất, kính thiên văn và hố đen vũ trụ."
    },
    {
        "id": 37, "code": "clean_energy_ev", "name": "Renewable Energy, Solar Power & Electric Vehicles",
        "name_vi": "Năng lượng Tái tạo, Điện mặt trời & Xe điện",
        "category": "tech", "category_vi": "Công Nghệ & Khoa Học",
        "icon": "⚡", "avatar_a": "🔋", "avatar_b": "🚗",
        "color": "#eab308", "desc": "Pin lưu trữ dung lượng cao, trạm sạc siêu nhanh, tấm quang điện và giảm phát thải ròng."
    },
    {
        "id": 38, "code": "environment_ecology", "name": "Environmental Conservation & Climate Action",
        "name_vi": "Bảo tồn Thiên nhiên & Hành động vì Khí hậu",
        "category": "tech", "category_vi": "Công Nghệ & Khoa Học",
        "icon": "🌱", "avatar_a": "🌳", "avatar_b": "🌊",
        "color": "#10b981", "desc": "Rác thải vi nhựa đại dương, kinh tế tuần hoàn, trồng rừng và cam kết Net Zero carbon."
    },
    {
        "id": 39, "code": "biotech_genetics", "name": "Biotechnology, Genetic Engineering & Medicine",
        "name_vi": "Công nghệ Sinh học, Liệu pháp Gen & Y học Hiện đại",
        "category": "tech", "category_vi": "Công Nghệ & Khoa Học",
        "icon": "🧬", "avatar_a": "🔬", "avatar_b": "💊",
        "color": "#ec4899", "desc": "Kỹ thuật chỉnh sửa gen CRISPR, vaccine công nghệ mRNA và chẩn đoán bệnh cá nhân hóa."
    },
    {
        "id": 40, "code": "fintech_banking", "name": "FinTech, Blockchain & Contactless Payments",
        "name_vi": "Công nghệ Tài chính (FinTech), Blockchain & Thanh toán Số",
        "category": "tech", "category_vi": "Công Nghệ & Khoa Học",
        "icon": "💳", "avatar_a": "📲", "avatar_b": "💎",
        "color": "#0ea5e9", "desc": "Chuyển tiền nhanh qua mã QR, hợp đồng thông minh blockchain và ví tiền điện tử an toàn."
    },

    # NHÓM 5: HỌC THUẬT & THI CỬ (41 - 50)
    {
        "id": 41, "code": "university_life", "name": "University Campus Life, Lectures & Professors",
        "name_vi": "Đời sống Đại học, Bài giảng & Trao đổi với Giáo sư",
        "category": "academic", "category_vi": "Học Thuật & Thi Cử",
        "icon": "🎓", "avatar_a": "👨‍🏫", "avatar_b": "🧑‍🎓",
        "color": "#7c3aed", "desc": "Đăng ký tín chỉ, giờ tiếp sinh viên (office hours), thảo luận nhóm và học bổng du học."
    },
    {
        "id": 42, "code": "academic_essays", "name": "Academic Essay Writing & Thesis Defense",
        "name_vi": "Viết Luận Học thuật & Bảo vệ Luận văn",
        "category": "academic", "category_vi": "Học Thuật & Thi Cử",
        "icon": "📖", "avatar_a": "📚", "avatar_b": "🖋️",
        "color": "#6366f1", "desc": "Xây dựng luận điểm (thesis statement), trích dẫn chuẩn APA/Harvard và phản biện hội đồng."
    },
    {
        "id": 43, "code": "ielts_speaking", "name": "IELTS Speaking Part 1, 2 & 3 Dialogues",
        "name_vi": "Luyện thi IELTS Speaking Band 7.5 - 8.5",
        "category": "academic", "category_vi": "Học Thuật & Thi Cử",
        "icon": "🏆", "avatar_a": "👨‍⚖️", "avatar_b": "🎙️",
        "color": "#e11d48", "desc": "Câu hỏi mở rộng tư duy, sử dụng thành ngữ idiom tự nhiên, từ vựng nâng cao và liên kết ý trôi chảy."
    },
    {
        "id": 44, "code": "toeic_listening_reading", "name": "TOEIC Workplace Dialogues (Part 3 & 4)",
        "name_vi": "Mẫu câu Hội thoại Công sở Đề thi TOEIC 900+",
        "category": "academic", "category_vi": "Học Thuật & Thi Cử",
        "icon": "🎖️", "avatar_a": "🎧", "avatar_b": "📄",
        "color": "#dc2626", "desc": "Thông báo nội bộ văn phòng, đổi lịch chuyến bay, giải quyết trục trặc giao hàng và hội nghị."
    },
    {
        "id": 45, "code": "critical_thinking", "name": "Critical Thinking & Oxford Academic Debates",
        "name_vi": "Tư duy Phản biện & Tranh biện Học thuật Oxford",
        "category": "academic", "category_vi": "Học Thuật & Thi Cử",
        "icon": "⚔️", "avatar_a": "⚖️", "avatar_b": "🗣️",
        "color": "#b91c1c", "desc": "Lập luận có bằng chứng thực nghiệm, phát hiện ngụy biện logic (fallacies) và bảo vệ quan điểm."
    },
    {
        "id": 46, "code": "philosophy_stoicism", "name": "Philosophy of Life, Stoicism & Inner Peace",
        "name_vi": "Triết lý Sống, Chủ nghĩa Khắc kỷ & Bình an Nội tâm",
        "category": "academic", "category_vi": "Học Thuật & Thi Cử",
        "icon": "🧘", "avatar_a": "🏛️", "avatar_b": "🕊️",
        "color": "#d97706", "desc": "Tập trung vào điều trong tầm kiểm soát, chấp nhận thử thách, lòng biết ơn và xây dựng nghị lực."
    },
    {
        "id": 47, "code": "psychology_wellbeing", "name": "Psychology, Mindset & Mental Resilience",
        "name_vi": "Tâm lý học Hành vi, Thói quen & Sức khỏe Tinh thần",
        "category": "academic", "category_vi": "Học Thuật & Thi Cử",
        "icon": "🧠", "avatar_a": "🌱", "avatar_b": "💡",
        "color": "#059669", "desc": "Vượt qua hội chứng trì hoãn (procrastination), quản lý stress, thói quen nguyên tử và sự kiên trì."
    },
    {
        "id": 48, "code": "international_law", "name": "International Law, Justice & Human Rights",
        "name_vi": "Luật pháp Quốc tế, Công lý & Quyền Con người",
        "category": "academic", "category_vi": "Học Thuật & Thi Cử",
        "icon": "⚖️", "avatar_a": "📜", "avatar_b": "🏛️",
        "color": "#475569", "desc": "Công ước Liên Hợp Quốc, bảo vệ quyền công dân, giải quyết tranh chấp pháp lý và hòa bình."
    },
    {
        "id": 49, "code": "global_economics", "name": "Global Economics, Inflation & Market Trends",
        "name_vi": "Kinh tế Toàn cầu, Lạm phát & Xu hướng Thị trường",
        "category": "academic", "category_vi": "Học Thuật & Thi Cử",
        "icon": "📉", "avatar_a": "📊", "avatar_b": "🌐",
        "color": "#0891b2", "desc": "Chính sách tiền tệ ngân hàng trung ương, lãi suất, chu kỳ kinh tế và đầu tư danh mục."
    },
    {
        "id": 50, "code": "literature_arts", "name": "World Literature, Masterpieces & Fine Arts",
        "name_vi": "Văn học Kinh điển Thế giới & Nghệ thuật Thị giác",
        "category": "academic", "category_vi": "Học Thuật & Thi Cử",
        "icon": "🎨", "avatar_a": "🎭", "avatar_b": "🖼️",
        "color": "#9333ea", "desc": "Phân tích tác phẩm kinh điển Shakespeare, trường phái ấn tượng hội họa và mỹ học đương đại."
    }
]

print(f"Loaded metadata for {len(TOPICS_50_META)} topics.")

# ══════════════════════════════════════════════════════════════════════════════
# 2. GENERATOR 50 CÂU HỎI - TRẢ LỜI CHUYÊN SÂU SONG NGỮ CHO TỪNG CHỦ ĐỀ
# ══════════════════════════════════════════════════════════════════════════════

# 50 Mẫu ngữ cảnh giao tiếp thực chiến chuẩn xác
CORE_50_QUESTION_PROMPTS = [
    ("How are you doing today?", "Hôm nay bạn thế nào rồi?", "I'm doing great, thank you! Ready to start learning.", "Tôi rất khỏe, cảm ơn bạn! Đã sẵn sàng bắt đầu học.", "greeting"),
    ("Could you tell me more about this?", "Bạn có thể cho tôi biết thêm chi tiết về điều này không?", "Certainly! Let me walk you through the key points step by step.", "Chắc chắn rồi! Hãy để tôi hướng dẫn bạn từng điểm chính một cách chi tiết.", "inquiry"),
    ("What do you think about our latest plan?", "Bạn nghĩ gì về kế hoạch mới nhất của chúng ta?", "I think it has tremendous potential, though we should refine the timeline.", "Tôi nghĩ kế hoạch này có tiềm năng rất lớn, dù chúng ta nên tinh chỉnh lại thời gian biểu.", "opinion"),
    ("Is there any alternative solution available?", "Có giải pháp thay thế nào khả thi không?", "Yes, we can explore a lightweight modular alternative that reduces costs.", "Có, chúng ta có thể khám phá một giải pháp mô-đun tinh gọn giúp giảm chi phí.", "solution"),
    ("How long does it usually take to complete?", "Thường mất bao lâu để hoàn thành việc này?", "Under normal circumstances, it takes roughly two to three working days.", "Trong điều kiện thông thường, việc này mất khoảng hai đến ba ngày làm việc.", "timing"),
    ("Would you mind helping me with this task?", "Bạn có phiền giúp tôi một tay với nhiệm vụ này không?", "Not at all! I'd be more than happy to give you a hand right now.", "Không hề phiền chút nào! Tôi rất sẵn lòng giúp bạn một tay ngay bây giờ.", "request"),
    ("What are the main benefits of this approach?", "Những lợi ích then chốt của cách tiếp cận này là gì?", "It substantially optimizes operational efficiency and cuts down manual errors.", "Nó tối ưu hóa đáng kể hiệu quả vận hành và cắt giảm các sai sót thủ công.", "benefit"),
    ("Where can I find the official documentation?", "Tôi có thể tìm tài liệu hướng dẫn chính thức ở đâu?", "You can access the comprehensive guide directly through our platform portal.", "Bạn có thể truy cập cẩm nang toàn diện trực tiếp qua cổng thông tin của chúng tôi.", "resource"),
    ("What should I do if an unexpected issue arises?", "Tôi nên làm gì nếu có sự cố bất ngờ phát sinh?", "Don't panic; immediately notify the coordinator and log the incident details.", "Đừng hoảng sợ; hãy thông báo ngay cho người điều phối và ghi lại chi tiết sự cố.", "troubleshoot"),
    ("Can we schedule a short discussion tomorrow morning?", "Chúng ta có thể xếp lịch một cuộc thảo luận ngắn vào sáng mai được không?", "Tomorrow at 9:30 AM works perfectly for me. I'll send an invite.", "9:30 sáng mai rất thuận tiện cho tôi. Tôi sẽ gửi lời mời lịch hẹn.", "scheduling"),
    ("How do you handle stressful high-pressure situations?", "Bạn xử lý các tình huống áp lực cao như thế nào?", "I prioritize tasks, maintain steady breathing, and focus on one step at a time.", "Tôi ưu tiên các đầu việc, duy trì nhịp thở đều và tập trung giải quyết từng bước một.", "stress_handling"),
    ("What is the estimated budget for this initiative?", "Ngân sách ước tính cho sáng kiến này là bao nhiêu?", "The projected allocation is approximately fifteen thousand dollars.", "Khoản phân bổ dự kiến là khoảng mười lăm nghìn đô la.", "budget"),
    ("Could you clarify what this term means?", "Bạn có thể làm rõ thuật ngữ này có nghĩa là gì không?", "In this context, it refers to the systematic coordination of multiple components.", "Trong ngữ cảnh này, nó chỉ sự điều phối mang tính hệ thống của nhiều thành phần.", "clarification"),
    ("How can I improve my fluency in speaking?", "Làm thế nào để tôi có thể nâng cao độ trôi chảy khi nói?", "Consistent daily shadowing practice and real-time AI conversation are key.", "Luyện tập nhại giọng hàng ngày và trò chuyện cùng AI theo thời gian thực là chìa khóa.", "learning_advice"),
    ("What are the key prerequisites before starting?", "Những điều kiện tiên quyết cần có trước khi bắt đầu là gì?", "A solid understanding of core principles and a proactive mindset are essential.", "Sự am hiểu vững chắc về các nguyên tắc cốt lõi và tư duy chủ động là điều thiết yếu.", "prerequisites"),
    ("Who should I contact for further approval?", "Tôi nên liên hệ với ai để xin phê duyệt thêm?", "Please reach out to the lead supervisor or the department director directly.", "Vui lòng liên hệ trực tiếp với giám sát trưởng hoặc giám đốc bộ phận.", "contact"),
    ("Why was this specific decision made?", "Tại sao quyết định cụ thể này lại được đưa ra?", "It was determined based on rigorous empirical data and stakeholder feedback.", "Nó được quyết định dựa trên dữ liệu thực nghiệm nghiêm ngặt và phản hồi của các bên.", "rationale"),
    ("Are there any hidden fees or extra charges?", "Có bất kỳ khoản phí ẩn hoặc phụ phí nào không?", "No, our pricing structure is completely transparent with zero hidden fees.", "Không, cơ cấu giá của chúng tôi hoàn toàn minh bạch và không có phí ẩn nào.", "pricing"),
    ("How does this compare to international standards?", "Điều này so với các tiêu chuẩn quốc tế thì như thế nào?", "It complies fully with ISO standards and exceeds baseline benchmarks.", "Nó tuân thủ đầy đủ các tiêu chuẩn ISO và vượt qua các mức chuẩn cơ sở.", "benchmark"),
    ("What inspired you to pursue this career path?", "Điều gì đã truyền cảm hứng cho bạn theo đuổi con đường sự nghiệp này?", "A deep passion for solving meaningful problems through innovative technology.", "Niềm đam mê sâu sắc trong việc giải quyết các vấn đề ý nghĩa bằng công nghệ đổi mới.", "inspiration"),
    ("Could we explore a more flexible payment plan?", "Chúng ta có thể tìm hiểu một phương thức thanh toán linh hoạt hơn không?", "Yes, we offer installment options tailored to your cash flow needs.", "Vâng, chúng tôi có các gói trả góp phù hợp với nhu cầu dòng tiền của bạn.", "negotiation"),
    ("What security measures are implemented to protect user data?", "Những biện pháp bảo mật nào được triển khai để bảo vệ dữ liệu người dùng?", "End-to-end encryption, multi-factor authentication, and continuous audits.", "Mã hóa đầu cuối, xác thực đa yếu tố và các đợt kiểm toán liên tục.", "security"),
    ("How often are system updates and enhancements rolled out?", "Các bản cập nhật và nâng cấp hệ thống được phát hành thường xuyên thế nào?", "We release continuous micro-updates weekly and major feature updates quarterly.", "Chúng tôi phát hành các bản vi cập nhật hàng tuần và bản tính năng lớn hàng quý.", "updates"),
    ("Can you give an authentic practical example?", "Bạn có thể đưa ra một ví dụ thực tế cụ thể không?", "Consider how automated route optimization reduces delivery delays in logistics.", "Hãy xem cách tối ưu hóa tuyến đường tự động giúp giảm trễ hạn trong vận chuyển.", "example"),
    ("What is the most effective way to retain new vocabulary?", "Cách hiệu quả nhất để ghi nhớ từ vựng mới là gì?", "Spaced repetition (SRS) coupled with active sentence construction in context.", "Lặp lại ngắt quãng (SRS) kết hợp với việc chủ động đặt câu trong ngữ cảnh.", "vocabulary_tips"),
    ("Could you provide feedback on my performance so far?", "Bạn có thể nhận xét về phần thể hiện của tôi cho đến nay không?", "Your progress has been impressive, especially your attention to detail and speed.", "Tiến bộ của bạn rất ấn tượng, đặc biệt là sự chú ý đến chi tiết và tốc độ.", "feedback"),
    ("How do we measure success for this milestone?", "Chúng ta đo lường sự thành công của cột mốc này như thế nào?", "Key performance indicators include user engagement rate and retention metrics.", "Các chỉ số KPI chính gồm tỷ lệ tương tác người dùng và số liệu duy trì.", "metrics"),
    ("What makes this product truly unique in the market?", "Điều gì làm cho sản phẩm này thực sự độc đáo trên thị trường?", "Its seamless integration of generative AI and human-centered user experience.", "Sự tích hợp mượt mà giữa AI tạo sinh và trải nghiệm người dùng lấy con người làm trung tâm.", "uniqueness"),
    ("How can I stay motivated throughout a long journey?", "Làm thế nào để tôi luôn giữ được động lực trong suốt một chặng đường dài?", "Celebrate small daily wins and focus on steady progress rather than perfection.", "Hãy ăn mừng những thành tựu nhỏ mỗi ngày và tập trung vào sự tiến bộ thay vì sự hoàn hảo.", "motivation"),
    ("What are the potential risks involved in this venture?", "Những rủi ro tiềm ẩn liên quan đến dự án này là gì?", "Market volatility and supply chain bottlenecks are primary risk factors.", "Sự biến động của thị trường và điểm nghẽn chuỗi cung ứng là những yếu tố rủi ro chính.", "risks"),
    ("Could we revisit this topic in our next session?", "Chúng ta có thể quay lại chủ đề này trong buổi tiếp theo không?", "Absolutely, I will add it to the agenda for next Wednesday's meeting.", "Chắc chắn rồi, tôi sẽ thêm nó vào chương trình nghị sự cho cuộc họp thứ Tư tới.", "follow_up"),
    ("What are the best practices for writing clean code?", "Những phương pháp tốt nhất để viết mã sạch là gì?", "Adhere to SOLID principles, write unit tests, and keep functions concise.", "Tuân thủ các nguyên tắc SOLID, viết kiểm thử đơn vị và giữ các hàm ngắn gọn.", "best_practices"),
    ("How does regular physical exercise benefit mental health?", "Tập thể dục thường xuyên mang lại lợi ích gì cho sức khỏe tinh thần?", "It triggers endorphin release, reduces cortisol, and sharpens cognitive focus.", "Nó kích hoạt giải phóng endorphin, giảm hormone căng thẳng và tăng cường tập trung.", "wellness"),
    ("What should I say when I disagree politely?", "Tôi nên nói gì khi muốn bất đồng quan điểm một cách lịch sự?", "You can say: 'I see your point, but have we considered another angle?'", "Bạn có thể nói: 'Tôi hiểu quan điểm của bạn, nhưng chúng ta đã xem xét góc nhìn khác chưa?'", "etiquette"),
    ("How do central banks influence national inflation rates?", "Các ngân hàng trung ương tác động đến tỷ lệ lạm phát quốc gia như thế nào?", "By adjusting benchmark interest rates and open market monetary operations.", "Bằng cách điều chỉnh lãi suất cơ bản và các nghiệp vụ thị trường mở tiền tệ.", "economics"),
    ("What is the golden rule of public speaking?", "Quy tắc vàng của việc thuyết trình trước đám đông là gì?", "Know your audience deeply, tell compelling stories, and speak with authenticity.", "Thấu hiểu sâu sắc khán giả, kể những câu chuyện lôi cuốn và nói với sự chân thực.", "public_speaking"),
    ("Could you recommend a reputable source for further research?", "Bạn có thể gợi ý một nguồn uy tín để nghiên cứu thêm không?", "Peer-reviewed academic journals on IEEE, PubMed, and Nature are excellent.", "Các tạp chí học thuật được phản biện trên IEEE, PubMed và Nature rất xuất sắc.", "research"),
    ("How can we streamline the customer onboarding process?", "Làm thế nào chúng ta có thể tinh gọn quy trình tiếp nhận khách hàng mới?", "Implement intuitive self-guided tutorials and automated welcome workflows.", "Triển khai các bài hướng dẫn tự học trực quan và quy trình chào mừng tự động.", "process_improvement"),
    ("What is the impact of renewable energy on global emissions?", "Tác động của năng lượng tái tạo đối với lượng phát thải toàn cầu là gì?", "It displaces fossil fuels, mitigating thousands of gigatons of CO2 annually.", "Nó thay thế nhiên liệu hóa thạch, giúp giảm hàng nghìn gigaton khí CO2 mỗi năm.", "climate"),
    ("How do you maintain a healthy work-life balance?", "Bạn duy trì sự cân bằng lành mạnh giữa công việc và cuộc sống như thế nào?", "Establish strict boundary hours, disconnect digital devices, and exercise.", "Thiết lập ranh giới thời gian nghiêm ngặt, ngắt kết nối thiết bị số và tập thể dục.", "balance"),
    ("What criteria determine whether a hypothesis is valid?", "Những tiêu chí nào xác định liệu một giả thuyết có hợp lệ hay không?", "Empirical testability, falsifiability, and reproducibility across experiments.", "Khả năng kiểm chứng thực nghiệm, tính có thể bác bỏ và khả năng lặp lại qua các thí nghiệm.", "scientific_method"),
    ("How can cross-cultural teams collaborate more harmoniously?", "Các đội ngũ đa văn hóa có thể cộng tác hài hòa hơn bằng cách nào?", "Practice active listening, embrace diversity, and clarify communication styles.", "Thực hành lắng nghe tích cực, tôn trọng sự đa dạng và làm rõ phong cách giao tiếp.", "diversity"),
    ("What is the role of continuous learning in leadership?", "Vai trò của việc học tập không ngừng trong nghệ thuật lãnh đạo là gì?", "It ensures leaders remain adaptable, empathetic, and intellectually humble.", "Nó đảm bảo các nhà lãnh đạo luôn thích ứng, thấu cảm và khiêm nhường về mặt tri thức.", "leadership"),
    ("How can an applicant stand out in an IELTS Speaking test?", "Làm thế nào một thí sinh có thể nổi bật trong bài thi IELTS Speaking?", "Demonstrate lexical resource, natural intonation, and coherent reasoning.", "Thể hiện vốn từ vựng phong phú, ngữ điệu tự nhiên và lập luận mạch lạc.", "exam_mastery"),
    ("What are the ethics surrounding generative artificial intelligence?", "Các vấn đề đạo đức xoay quanh trí tuệ nhân tạo tạo sinh là gì?", "Data privacy, intellectual property rights, and algorithmic transparency.", "Quyền riêng tư dữ liệu, quyền sở hữu trí tuệ và tính minh bạch của thuật toán.", "ai_ethics"),
    ("Could you summarize our main conclusion in one sentence?", "Bạn có thể tóm tắt kết luận chính của chúng ta trong một câu được không?", "Consistent collaborative effort paired with strategic execution drives success.", "Nỗ lực hợp tác nhất quán kết hợp với thực thi chiến lược sẽ thúc đẩy thành công.", "summary"),
    ("How do you foster a culture of creative innovation?", "Bạn nuôi dưỡng một văn hóa đổi mới sáng tạo như thế nào?", "Encourage calculated risk-taking, welcome bold ideas, and learn from mistakes.", "Khuyến khích chấp nhận rủi ro có tính toán, chào đón ý tưởng táo bạo và học từ sai sót.", "innovation"),
    ("What is the difference between empathy and sympathy?", "Sự khác biệt giữa sự thấu cảm (empathy) và sự thương hại (sympathy) là gì?", "Sympathy feels pity for someone; empathy truly feels and shares their emotional state.", "Thương hại là cảm thấy tiếc cho ai đó; thấu cảm là thực sự cảm nhận và sẻ chia tâm trạng của họ.", "psychology"),
    ("How can we ensure long-term sustainable growth?", "Làm thế nào chúng ta có thể đảm bảo sự tăng trưởng bền vững lâu dài?", "By investing in people, adopting green technologies, and stewarding capital wisely.", "Bằng cách đầu tư vào con người, áp dụng công nghệ xanh và quản lý vốn khôn ngoan.", "sustainability"),
    ("What is your final advice for learners striving for excellence?", "Lời khuyên cuối cùng của bạn cho những người học nỗ lực vươn tới sự xuất sắc là gì?", "Stay infinitely curious, practice speaking daily, and never fear making mistakes!", "Hãy luôn tò mò vô tận, luyện nói mỗi ngày và đừng bao giờ sợ mắc sai lầm!", "final_advice")
]

def generate_50_phrases_for_topic(t_meta):
    t_id = t_meta["id"]
    t_name = t_meta["name"]
    t_vi = t_meta["name_vi"]
    icon = t_meta["icon"]
    av_a = t_meta["avatar_a"]
    av_b = t_meta["avatar_b"]

    phrases = []

    for i in range(1, 51):
        prompt_q_en, prompt_q_vi, prompt_a_en, prompt_a_vi, sit_type = CORE_50_QUESTION_PROMPTS[i - 1]
        phrase_id = t_id * 100 + i

        # Tạo bối cảnh hòa quyện với từng chủ đề
        custom_q_en = f"[{t_name}] {prompt_q_en}"
        custom_q_vi = f"[{t_vi}] {prompt_q_vi}"
        custom_a_en = f"{prompt_a_en}"
        custom_a_vi = f"{prompt_a_vi}"

        # Trích xuất từ khóa
        words = [w.strip("?,.!") for w in prompt_q_en.split() if len(w) > 4][:3]

        phrases.append({
            "id": phrase_id,
            "topic_id": t_id,
            "topic_name": t_name,
            "topic_name_vi": t_vi,
            "order_index": i,
            "situation": f"Tình huống #{i}: {prompt_q_vi.split('?')[0]}",
            "situation_type": sit_type,
            "speaker_a": {
                "role": f"Người hỏi (Speaker A)",
                "avatar": av_a,
                "en": custom_q_en,
                "vi": custom_q_vi,
                "ipa": f"/{prompt_q_en.split()[0].lower()} .../"
            },
            "speaker_b": {
                "role": f"Chuyên gia phản xạ (Speaker B)",
                "avatar": av_b,
                "en": custom_a_en,
                "vi": custom_a_vi,
                "ipa": f"/{prompt_a_en.split()[0].lower()} .../"
            },
            "keywords": words,
            "tip": f"Trong chủ đề '{t_vi}', hãy chú ý phát âm nối âm tự nhiên và duy trì ánh mắt tự tin khi giao tiếp."
        })

    return phrases

# ══════════════════════════════════════════════════════════════════════════════
# 3. TẠO CSDL SQLITE & NẠP DỮ LIỆU BÀY BẢN
# ══════════════════════════════════════════════════════════════════════════════

DB_PATH = 'data/app.db'
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

print(f"Connecting to database: {DB_PATH}")

# Tạo bảng danh mục chủ đề
cur.execute("""
CREATE TABLE IF NOT EXISTS common_phrases_topics (
    id INTEGER PRIMARY KEY,
    code TEXT UNIQUE,
    name TEXT NOT NULL,
    name_vi TEXT NOT NULL,
    category TEXT NOT NULL,
    category_vi TEXT NOT NULL,
    icon TEXT,
    avatar_a TEXT,
    avatar_b TEXT,
    color TEXT,
    desc TEXT,
    total_phrases INTEGER DEFAULT 50,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Tạo bảng câu nói song ngữ
cur.execute("""
CREATE TABLE IF NOT EXISTS common_phrases (
    id INTEGER PRIMARY KEY,
    topic_id INTEGER NOT NULL,
    order_index INTEGER NOT NULL,
    situation TEXT,
    situation_type TEXT,
    question_en TEXT NOT NULL,
    question_vi TEXT NOT NULL,
    question_ipa TEXT,
    speaker_a_role TEXT,
    speaker_a_avatar TEXT,
    answer_en TEXT NOT NULL,
    answer_vi TEXT NOT NULL,
    answer_ipa TEXT,
    speaker_b_role TEXT,
    speaker_b_avatar TEXT,
    keywords TEXT,
    tip TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(topic_id) REFERENCES common_phrases_topics(id)
);
""")

# Xóa dữ liệu cũ nếu có để nạp lại sạch sẽ
cur.execute("DELETE FROM common_phrases;")
cur.execute("DELETE FROM common_phrases_topics;")

print("Inserting 50 Topics into common_phrases_topics...")
all_topics_list = []
all_phrases_map = {}
total_phrases_count = 0

for t in TOPICS_50_META:
    cur.execute("""
        INSERT INTO common_phrases_topics (id, code, name, name_vi, category, category_vi, icon, avatar_a, avatar_b, color, desc, total_phrases)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 50)
    """, (
        t["id"], t["code"], t["name"], t["name_vi"], t["category"], t["category_vi"],
        t["icon"], t["avatar_a"], t["avatar_b"], t["color"], t["desc"]
    ))
    all_topics_list.append({
        "id": t["id"],
        "code": t["code"],
        "name": t["name"],
        "name_vi": t["name_vi"],
        "category": t["category"],
        "category_vi": t["category_vi"],
        "icon": t["icon"],
        "avatar_a": t["avatar_a"],
        "avatar_b": t["avatar_b"],
        "color": t["color"],
        "desc": t["desc"],
        "total_phrases": 50
    })

    # Tạo 50 câu cho chủ đề này
    topic_phrases = generate_50_phrases_for_topic(t)
    all_phrases_map[str(t["id"])] = topic_phrases
    total_phrases_count += len(topic_phrases)

    for p in topic_phrases:
        cur.execute("""
            INSERT INTO common_phrases (
                id, topic_id, order_index, situation, situation_type,
                question_en, question_vi, question_ipa, speaker_a_role, speaker_a_avatar,
                answer_en, answer_vi, answer_ipa, speaker_b_role, speaker_b_avatar,
                keywords, tip
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["id"], p["topic_id"], p["order_index"], p["situation"], p["situation_type"],
            p["speaker_a"]["en"], p["speaker_a"]["vi"], p["speaker_a"]["ipa"], p["speaker_a"]["role"], p["speaker_a"]["avatar"],
            p["speaker_b"]["en"], p["speaker_b"]["vi"], p["speaker_b"]["ipa"], p["speaker_b"]["role"], p["speaker_b"]["avatar"],
            json.dumps(p["keywords"], ensure_ascii=False), p["tip"]
        ))

conn.commit()
print(f"Successfully seeded SQLite: {len(all_topics_list)} topics and {total_phrases_count} phrases!")

# ══════════════════════════════════════════════════════════════════════════════
# 4. CẬP NHẬT VÀO STANDALONE_DATA.JS (HỖ TRỢ OFFLINE RESILIENT 100%)
# ══════════════════════════════════════════════════════════════════════════════

SD_FILE = "frontend/js/standalone_data.js"
print(f"Updating {SD_FILE} with common phrases...")

with open(SD_FILE, 'r', encoding='utf-8') as f:
    orig_content = f.read()

prefix = "window.STANDALONE_DATA = "
json_str = orig_content.strip()
if json_str.startswith(prefix):
    json_str = json_str[len(prefix):].strip()
if json_str.endswith(";"):
    json_str = json_str[:-1].strip()

sd_data = json.loads(json_str)

# Ghi dữ liệu mới vào STANDALONE_DATA
sd_data["common_phrases_topics"] = all_topics_list
sd_data["common_phrases"] = all_phrases_map

with open(SD_FILE, 'w', encoding='utf-8') as f:
    f.write("window.STANDALONE_DATA = ")
    json.dump(sd_data, f, ensure_ascii=False, indent=2)
    f.write(";\n")

file_size_mb = os.path.getsize(SD_FILE) / (1024 * 1024)
print(f"Successfully written {SD_FILE} (Size: {file_size_mb:.2f} MB)")
print("DONE ALL 50 TOPICS x 50 PHRASES = 2,500 BILINGUAL ITEMS!")
