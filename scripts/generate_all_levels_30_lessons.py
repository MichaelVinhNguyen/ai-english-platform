# -*- coding: utf-8 -*-
"""
scripts/generate_all_levels_30_lessons.py
Tạo 30 modules chuyên sâu + 30 đề thi thực chiến cho tất cả các cấp độ:
A1, A2, B1, B2, C1, C2, TOEIC, IELTS.
"""
import json
import os
import sys
import io

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# ══════════════════════════════════════════════════════════════════════════════
# 1. DANH SÁCH 30 CHỦ ĐỀ CHUẨN HÓA THEO TỪNG CẤP ĐỘ CEFR
# ══════════════════════════════════════════════════════════════════════════════

A1_TOPICS = [
    ("Bảng Chữ Cái, Phát Âm IPA Căn Bản & Chào Hỏi", "Alphabet, IPA & Greetings", "Hello, Welcome, Introduce, Friend, Morning"),
    ("Số Đếm, Tuổi Tác & Thông Tin Cá Nhân", "Numbers, Age & Personal Info", "Number, Age, Address, Phone, Single"),
    ("Gia Đình, Họ Hàng & Các Mối Quan Hệ", "Family Members & Relatives", "Parent, Sibling, Child, Cousin, Relative"),
    ("Màu Sắc, Hình Dạng & Đồ Vật Quanh Ta", "Colors, Shapes & Everyday Objects", "Color, Shape, Circle, Object, Table"),
    ("Quần Áo, Phụ Kiện & Trang Phục Hàng Ngày", "Clothes & Daily Accessories", "Shirt, Pants, Shoes, Jacket, Wear"),
    ("Thời Gian, Ngày Trong Tuần & Lịch Trình", "Time, Days & Daily Schedule", "Clock, Schedule, Today, Weekend, Month"),
    ("Ngôi Nhà, Phòng Ốc & Nội Thất Cơ Bản", "House, Rooms & Basic Furniture", "Bedroom, Kitchen, Living, Window, Chair"),
    ("Thức Ăn, Đồ Uống & Bữa Ăn Thường Ngày", "Food, Drinks & Daily Meals", "Breakfast, Water, Bread, Rice, Delicious"),
    ("Thời Tiết, Bốn Mùa & Khí Hậu Quen Thuộc", "Weather, Seasons & Climate", "Sunny, Rainy, Cold, Season, Summer"),
    ("Sở Thích, Hoạt Động Rảnh Rỗi & Giải Trí", "Hobbies & Leisure Activities", "Music, Reading, Sport, Movie, Hobby"),
    ("Các Bộ Phận Cơ Thể & Cảm Giác Cơ Bản", "Body Parts & Basic Sensations", "Head, Hand, Eye, Tired, Hungry"),
    ("Trường Học, Đồ Dùng Học Tập & Lớp Học", "School, Stationery & Classroom", "Book, Pen, Classroom, Desk, Teacher"),
    ("Nghề Nghiệp & Nơi Làm Việc Thường Ngày", "Jobs & Common Workplaces", "Doctor, Engineer, Nurse, Office, Worker"),
    ("Địa Điểm Trong Thị Trấn & Chỉ Đường Đơn Giản", "Town Places & Basic Directions", "Bank, Hospital, Park, Street, Turn"),
    ("Phương Tiện Giao Thông & Đi Lại", "Transportation & Commuting", "Bus, Train, Bicycle, Car, Ticket"),
    ("Mua Sắm, Giá Cả & Mặc Cả Đơn Giản", "Shopping & Basic Prices", "Store, Price, Dollar, Cheap, Buy"),
    ("Động Vật Nuôi & Thú Cưng Trong Nhà", "Domestic Animals & Pets", "Dog, Cat, Bird, Pet, Animal"),
    ("Các Hoạt Động Thể Thao & Rèn Luyện", "Sports & Fitness Activities", "Football, Swimming, Running, Tennis, Match"),
    ("Cảm Xúc, Tâm Trạng & Biểu Cảm Hàng Ngày", "Emotions & Daily Feelings", "Happy, Sad, Angry, Excited, Surprised"),
    ("Nhà Hàng, Quán Cà Phê & Đặt Món Cơ Bản", "Restaurants, Cafes & Ordering", "Menu, Order, Coffee, Bill, Waiter"),
    ("Đất Nước, Quốc Tịch & Ngôn Ngữ", "Countries, Nationalities & Languages", "Country, English, Vietnam, Travel, Language"),
    ("Công Việc Thường Nhật & Lịch Trình Sinh Hoạt", "Daily Chores & Housework", "Clean, Wash, Cook, Tidy, Garden"),
    ("Thói Quen Buổi Sáng & Buổi Tối", "Morning & Evening Routines", "Wake, Sleep, Brush, Shower, Relax"),
    ("Điểm Đến Du Lịch & Khách Sạn Căn Bản", "Travel Destinations & Hotels", "Hotel, Room, Luggage, Beach, Visit"),
    ("Thiết Bị Điện Tử & Đồ Dùng Công Nghệ Quen Thuộc", "Gadgets & Everyday Technology", "Phone, Laptop, Camera, Battery, Screen"),
    ("Lời Mời, Hẹn Gặp & Phép Lịch Sự Cơ Bản", "Invitations & Courteous Phrases", "Invite, Please, Sorry, Thank, Welcome"),
    ("Kỷ Niệm, Sinh Nhật & Các Ngày Lễ Quen Thuộc", "Birthdays & Popular Holidays", "Birthday, Gift, Party, Celebrate, Holiday"),
    ("Sức Khỏe Cơ Bản & Cuộc Hẹn Phòng Khám", "Basic Health & Clinic Visits", "Fever, Cold, Medicine, Rest, Doctor"),
    ("Mô Tả Ngoại Hình Cơ Bản & Tính Cách", "Basic Appearance & Traits", "Tall, Short, Kind, Friendly, Polite"),
    ("Tổng Ôn Toàn Diện & Đột Phá Chuẩn CEFR A1", "A1 Comprehensive Review & Test Strategy", "Foundation, Accuracy, Practice, Exam, Success")
]

A2_TOPICS = [
    ("Miêu Tả Chi Tiết Ngoại Hình & Tính Cách Con Người", "Describing Appearance & Personality", "Attractive, Generous, Ambitious, Reliable, Outgoing"),
    ("Kế Hoạch Cuối Tuần, Dự Định Tương Lai & Hẹn Hò", "Weekend Plans & Future Arrangements", "Arrangement, Intention, Picnic, Cinema, Gathering"),
    ("Kể Về Trải Nghiệm Du Lịch & Kỳ Nghỉ Đã Qua", "Past Holidays & Travel Experiences", "Unforgettable, Scenic, Souvenir, Landscape, Memory"),
    ("Thủ Tục Tại Sân Bay, Ga Tàu & Khách Sạn", "Airports, Stations & Hotel Check-in", "Check-in, Boarding, Departure, Reservation, Reception"),
    ("Mua Sắm Thời Trang, Kích Cỡ & Đổi Trả Hàng Hóa", "Fashion Shopping, Sizes & Returns", "Receipt, Fitting, Exchange, Discount, Refund"),
    ("Ẩm Thực Vùng Miền, Công Thức Nấu Ăn & Hương Vị", "Regional Cuisine, Recipes & Flavors", "Recipe, Ingredient, Spicy, Flavour, Authentic"),
    ("Môi Trường Làm Việc, Đồng Nghiệp & Nhiệm Vụ", "Workplace, Colleagues & Tasks", "Colleague, Responsibility, Task, Meeting, Salary"),
    ("Đời Sống Sinh Viên, Ký Túc Xá & Bạn Cùng Phòng", "Campus Life, Dorms & Roommates", "Campus, Semester, Lecture, Roommate, Assignment"),
    ("Khám Bệnh, Mô Tả Triệu Chứng & Đơn Thuốc", "Medical Checkup, Symptoms & Prescriptions", "Prescription, Symptom, Diagnose, Treatment, Recovery"),
    ("Cuộc Sống Ở Nông Thôn So Với Thành Thị", "Countryside vs. City Living", "Peaceful, Modern, Congested, Fresh, Commute"),
    ("Sự Kiện Âm Nhạc, Lễ Hội Văn Hóa & Nghệ Thuật", "Live Music, Festivals & Art Events", "Concert, Exhibition, Performance, Tradition, Stage"),
    ("Luật Giao Thông, Sự Cố Trên Đường & Bảo Dưỡng Xe", "Traffic Rules, Road Incidents & Repairs", "License, Maintenance, Helmet, Breakdown, Intersection"),
    ("Môi Trường Tự Nhiên & Các Thói Quen Sống Xanh", "Natural Environment & Eco Habits", "Recycle, Conserve, Pollution, Eco-friendly, Nature"),
    ("Cảm Xúc Phức Tạp & Giải Quyết Bất Đồng Nhỏ", "Complex Emotions & Resolving Disputes", "Frustrated, Apologize, Resolve, Misunderstanding, Calm"),
    ("Quản Lý Chi Tiêu Cá Nhân, Tiết Kiệm & Hóa Đơn", "Managing Money, Savings & Bills", "Budget, Expense, Savings, Transfer, Payment"),
    ("Trang Trí Nhà Cửa, Sửa Chữa & Đồ Gia Dụng", "Home Improvement, Repairs & Appliances", "Decorate, Repair, Appliance, Furniture, Balcony"),
    ("Viết Thư & Email Thân Mật Cho Bạn Bè / Đối Tác", "Writing Friendly Letters & Emails", "Attachment, Inquire, Regards, Sincere, Update"),
    ("Phong Tục, Tập Quán & Lễ Hội Thế Giới", "World Customs & Cultural Festivals", "Tradition, Celebrate, Heritage, Ritual, Culture"),
    ("Thể Thao Ngoài Trời & Hoạt Động Rèn Thể Lực", "Outdoor Sports & Physical Fitness", "Marathon, Endurance, Workout, Equipment, Coach"),
    ("Điện Ảnh, Thể Loại Phim & Nhận Xét Phim", "Movies, Film Genres & Reviews", "Plot, Character, Director, Masterpiece, Review"),
    ("Thế Giới Động Vật & Bảo Tồn Động Vật Quý Hiếm", "Wildlife & Endangered Species", "Habitat, Species, Rare, Extinct, Preserve"),
    ("Kỹ Năng Thuyết Trình Ngắn Về Một Đề Tài", "Short Presentation & Public Speaking", "Introduction, Outline, Conclude, Visual, Deliver"),
    ("Ứng Dụng Công Nghệ & Tiện Ích Di Động Hàng Ngày", "Mobile Apps & Daily Digital Tools", "Application, Download, Feature, Connected, Device"),
    ("Dinh Dưỡng Cân Bằng & Lối Sống Lành Mạnh", "Balanced Nutrition & Healthy Habits", "Nutritious, Calorie, Hydrate, Exercise, Vitality"),
    ("Nghệ Thuật Thủ Công, Điêu Khắc & Hội Họa", "Handicrafts, Sculptures & Paintings", "Craftsman, Artwork, Museum, Sculpture, Gallery"),
    ("Kỹ Năng Ứng Phó Tình Huống Khẩn Cấp & Sinh Tồn", "Emergency Responses & Basic Survival", "Emergency, First-aid, Evacuate, Safety, Guide"),
    ("Sách Hay, Thói Quen Đọc & Kho Tàng Tri Thức", "Reading Habits & Knowledge Discovery", "Novel, Author, Chapter, Inspire, Wisdom"),
    ("Quản Lý Thời Gian & Cân Bằng Cuộc Sống", "Time Management & Work-Life Balance", "Priority, Punctual, Balance, Productive, Relax"),
    ("Định Hướng Nghề Nghiệp & Mục Tiêu Bản Thân", "Career Aspirations & Personal Goals", "Ambition, Skill, Promotion, Experience, Target"),
    ("Tổng Ôn Toàn Diện & Đột Phá Khảo Thí CEFR A2", "A2 Comprehensive Mastery & Mock Strategy", "Proficiency, Confidence, Accuracy, Milestone, Certified")
]

B1_TOPICS = [
    ("Giao Tiếp Xã Hội & Cuộc Sống Thường Nhật", "Daily Life & Social Circles", "Routine, Leisure, Acquaintance, Spontaneous, Hospitality"),
    ("Du Lịch, Địa Lý & Giao Lưu Văn Hóa", "Travel, Places & Culture", "Itinerary, Destination, Accommodation, Breathtaking, Souvenir"),
    ("Môi Trường Công Sở & Kỹ Năng Nghề Nghiệp", "Work, Office & Careers", "Collaborate, Deadline, Profession, Productivity, Resign"),
    ("Ẩm Thực, Dinh Dưỡng & Sức Khỏe Toàn Diện", "Food, Nutrition & Health", "Nutritious, Recipe, Ingredient, Moderate, Balanced"),
    ("Khoa Học Công Nghệ & Trí Tuệ Nhân Tạo", "Technology, AI & Digital Life", "Innovation, Automation, Artificial, Algorithm, Interface"),
    ("Môi Trường, Sinh Thái & Biến Đổi Khí Hậu", "Environment, Ecology & Climate", "Conservation, Sustainable, Biodiversity, Pollution, Renewable"),
    ("Giáo Dục, Kỹ Năng Mềm & Phát Triển Cá Nhân", "Education, Skills & Growth", "Curriculum, Scholarship, Discipline, Potential, Mentor"),
    ("Nghệ Thuật, Âm Nhạc & Giải Trí Đương Đại", "Arts, Music & Entertainment", "Performance, Contemporary, Masterpiece, Creativity, Audience"),
    ("Tài Chính Cá Nhân & Quản Lý Chi Tiêu", "Personal Finance & Budgeting", "Expenditure, Investment, Savings, Mortgage, Transaction"),
    ("Truyền Thông, Tin Tức & Mạng Xã Hội", "Media, News & Social Networks", "Broadcasting, Journalism, Virality, Credible, Engagement"),
    ("Thể Thao, Thể Chất & Tinh Thần Đồng Đội", "Sports, Fitness & Teamwork", "Athletic, Endurance, Tournament, Sportsmanship, Coaching"),
    ("Mua Sắm, Tiêu Dùng & Thương Mại Điện Tử", "Shopping, Consumerism & E-Commerce", "Discount, Warranty, Refund, Retailer, Logistics"),
    ("Nhà Ở, Kiến Trúc & Không Gian Sống", "Housing, Architecture & Living Space", "Renovate, Modernize, Suburban, Interior, Furnishing"),
    ("Tâm Lý Học, Cảm Xúc & Các Mối Quan Hệ", "Psychology, Emotions & Relationships", "Empathy, Perspective, Resilient, Overcome, Affection"),
    ("Giao Thông, Hạ Tầng & Di Chuyển Thông Minh", "Transportation & Smart Infrastructure", "Commute, Congestion, Public transit, Transit, Intersection"),
    ("Luật Pháp, Quyền Công Dân & Trật Tự Xã Hội", "Law, Citizenship & Civic Duties", "Legislation, Regulation, Compliance, Justice, Verdict"),
    ("Lịch Sử, Di Sản & Truyền Thống Dân Tộc", "History, Heritage & Traditions", "Ancestor, Dynasty, Artifact, Historical, Civilization"),
    ("Thời Tiết, Thiên Nhiên & Thảm Họa Tự Nhiên", "Weather, Nature & Natural Disasters", "Forecast, Blizzard, Hurricane, Evacuate, Relief"),
    ("Đa Dạng Văn Hóa & Phong Tục Thế Giới", "Cultural Diversity & Global Customs", "Etiquette, Tradition, Diversity, Norm, Superstition"),
    ("Làm Việc Từ Xa & Xu Hướng Tương Lai", "Remote Work & Future Trends", "Telecommute, Flexibility, Connectivity, Hybrid, Virtual"),
    ("Thuyết Trình, Diễn Thuyết & Đàm Phán Cơ Bản", "Public Speaking & Basic Negotiation", "Persuasive, Articulate, Delivery, Agreement, Compromise"),
    ("Động Vật Hoang Dã & Bảo Tồn Sinh Quyển", "Wildlife & Biosphere Conservation", "Endangered, Sanctuary, Habitat, Extinction, Poaching"),
    ("Đời Sống Học Đường & Môi Trường Đại Học", "University Life & Campus Culture", "Lecture, Semester, Campus, Assignment, Academic"),
    ("Y Tế, Phòng Khám & Dược Phẩm Cơ Bản", "Healthcare & Medical Services", "Prescription, Symptom, Diagnosis, Physician, Treatment"),
    ("Quy Hoạch Đô Thị & Đô Thị Thông Minh", "Urban Planning & Smart Cities", "Metropolitan, Population, Infrastructure, Density, Expansion"),
    ("Thời Trang, Phong Cách & Bản Sắc Cá Nhân", "Fashion, Style & Personal Identity", "Trend, Elegance, Aesthetic, Garment, Outfit"),
    ("Nông Nghiệp Hữu Cơ & Chuỗi Cung Ứng Thực Phẩm", "Organic Farming & Food Systems", "Harvest, Organic, Cultivation, Pesticide, Produce"),
    ("Khám Phá Vũ Trụ & Thiên Văn Học Cơ Bản", "Space Exploration & Basic Astronomy", "Galaxy, Orbit, Satellite, Telescope, Cosmos"),
    ("Sự Kiện Quốc Tế & Hợp Tác Toàn Cầu", "International Events & Global Cooperation", "Conference, Treaty, Alliance, Globalization, Summit"),
    ("Tổng Ôn & Chiến Thuật Khảo Thí CEFR B1", "B1 Comprehensive Review & Exam Strategy", "Assessment, Mastery, Proficiency, Accuracy, Certification")
]

B2_TOPICS = [
    ("Đổi Mới Sáng Tạo, Khởi Nghiệp & Doanh Nhân", "Innovation, Startups & Entrepreneurship", "Disruptive, Entrepreneur, Venture, Incubator, Scalability"),
    ("Kinh Tế Toàn Cầu, Thị Trường & Hành Vi Tiêu Dùng", "Global Economy & Consumer Behavior", "Commodity, Inflation, Fiscal, Consumption, Market share"),
    ("Biến Đổi Khí Hậu, Năng Lượng Tái Tạo & Lưới Điện Thông Minh", "Climate Change & Renewable Energy", "Decarbonize, Photovoltaic, Geothermal, Emission, Sustainability"),
    ("Truyền Thông Đại Chúng, Tin Giả & Đạo Đức Báo Chí", "Mass Media, Fake News & Media Ethics", "Sensationalism, Disinformation, Integrity, Editorial, Objectivity"),
    ("Trí Tuệ Cảm Xúc (EQ) & Tâm Lý Học Hành Vi", "Emotional Intelligence & Behavioral Psychology", "Self-awareness, Resilience, Empathy, Cognitive, Motivation"),
    ("Quy Hoạch Đô Thị Bền Vững & Siêu Đô Thị", "Sustainable Urbanization & Megacities", "Urban sprawl, Transit-oriented, Infrastructure, Metropolis, Ecological"),
    ("Trí Tuệ Nhân Tạo, Tự Động Hóa & Tương Lai Lao Động", "AI, Automation & Future of Work", "Algorithm, Robotics, Displace, Reskilling, Upskilling"),
    ("Y Tế Công Cộng, Dịch Tễ Học & Y Học Cá Nhân Hóa", "Public Health, Epidemiology & Personalized Medicine", "Immunology, Pandemic, Genomics, Preventive, Therapy"),
    ("Cải Cách Giáo Dục, Tư Duy Phản Biện & E-Learning", "Educational Reform, Critical Thinking & EdTech", "Pedagogy, Holistic, Interdisciplinary, Assessment, Autonomy"),
    ("Đa Dạng Sinh Học, Bảo Tồn Đại Dương & Ô Nhiễm Nhựa", "Biodiversity, Ocean Conservation & Microplastics", "Ecosystem, Degradation, Coral reef, Marine biology, Endangered"),
    ("Pháp Luật Quốc Tế, Quyền Con Người & Đạo Đức Nghề Nghiệp", "International Law & Professional Ethics", "Jurisdiction, Human rights, Compliance, Transparency, Whistleblower"),
    ("Toàn Cầu Hóa, Bản Sắc Dân Tộc & Giao Thoa Văn Hóa", "Globalization & Cultural Crossings", "Homogenization, Heritage, Assimilation, Diversity, Identity"),
    ("Y Học Thể Thao, Rèn Luyện Đỉnh Cao & Tâm Lý Thi Đấu", "Sports Science, Elite Training & Psychology", "Athletic, Endurance, Biomechanics, Sportsmanship, Discipline"),
    ("Công Nghiệp Không Khói, Quá Tải Du Lịch & Du Lịch Sinh Thái", "Tourism Industry, Overtourism & Ecotourism", "Footprint, Hospitality, Ecotourist, Cultural impact, Sustainability"),
    ("Kiến Trúc Đương Đại, Tòa Nhà Xanh & Thiết Kế Không Gian", "Contemporary Architecture & Green Buildings", "Aesthetic, Modernist, Structural, Ergonomics, Sustainable"),
    ("Thám Hiểm Vũ Trụ, Trạm Không Gian & Thương Mại Không Gian", "Space Exploration & Space Commercialization", "Astronomy, Orbit, Celestial, Satellite, Mission"),
    ("Văn Học Hiện Đại, Phê Bình Tác Phẩm & Triết Lý Sống", "Modern Literature, Literary Criticism & Philosophy", "Metaphor, Narrative, Existential, Allegory, Symbolism"),
    ("Khoa Học Dữ Liệu, Quyền Riêng Tư & An Ninh Số", "Data Science, Digital Privacy & Cybersecurity", "Encryption, Big data, Analytics, Vulnerability, Safeguard"),
    ("Quản Trị Rủi Ro, Đàm Phán Thương Mại & Ra Quyết Định", "Risk Management & High-Stakes Decision Making", "Contingency, Liability, Mitigation, Stakeholder, Compromise"),
    ("Bình Đẳng Giới, Hòa Nhập Xã Hội & Quyền Bình Đẳng", "Gender Equality, Social Inclusion & Diversity", "Inclusivity, Empowerment, Stereotype, Marginalize, Opportunity"),
    ("Chuỗi Cung Ứng Toàn Cầu, Logistics & Khủng Hoảng Vận Tải", "Global Supply Chains & Logistics Disruptions", "Bottleneck, Procurement, Freight, Inventory, Resilience"),
    ("Tiếp Biến Văn Hóa, Nghệ Thuật Thị Giác & Bản Quyền Nghệ Thuật", "Visual Arts, Cultural Acculturation & Copyright", "Contemporary, Exhibition, Intellectual property, Expression, Patronage"),
    ("Khoa Học Thần Kinh, Trí Nhớ & Khả Năng Thích Ứng Não Bộ", "Neuroscience, Memory & Brain Plasticity", "Synapse, Neuron, Plasticity, Stimulus, Cognitive function"),
    ("Thị Trường Tài Chính, Đầu Tư Chứng Khoán & Quản Lý Danh Mục", "Financial Markets & Investment Portfolios", "Equities, Dividend, Liquidity, Volatility, Asset allocation"),
    ("Công Nghệ Tài Chính (FinTech), Blockchain & Tiền Số", "FinTech, Blockchain & Decentralized Finance", "Cryptocurrency, Ledger, Decentralize, Smart contract, Transaction"),
    ("Đạo Đức Trong Trí Tuệ Nhân Tạo & Trách Nhiệm Thuật Toán", "AI Ethics & Algorithmic Accountability", "Bias, Accountability, Transparency, Autonomous, Safeguard"),
    ("Nền Kinh Tế Chia Sẻ (Gig Economy) & Lao Động Tự Do", "The Gig Economy & Freelance Workforce", "Freelancer, Platform, Labor rights, Contractual, Autonomy"),
    ("Ngoại Giao Đa Phương, Hiệp Định Quốc Tế & Hòa Bình", "Multilateral Diplomacy & Global Pacts", "Diplomat, Bilateral, Treaty, Envoy, Resolution"),
    ("Nông Nghiệp Công Nghệ Cao & Đảm Bảo An Ninh Lương Thực", "High-Tech Agriculture & Global Food Security", "Hydroponics, Crop yield, Fertile, Cultivation, Food supply"),
    ("Chiến Lược Khảo Thí Toàn Diện & Đột Phá CEFR B2 / VSTEP Bậc 4", "B2 Master Exam Strategy & Advanced Competence", "Coherence, Lexical range, Precision, Eloquence, Distinction")
]

C1_TOPICS = [
    ("Ngôn Ngữ Học Tri Nhận, Biến Đổi Ngôn Ngữ & Ngữ Dụng Học", "Cognitive Linguistics, Language Evolution & Pragmatics", "Cognitive, Syntax, Semantics, Pragmatic, Morphology"),
    ("Địa Chính Trị Toàn Cầu, Trật Tự Thế Giới & Các Khối Liên Minh", "Global Geopolitics, Multipolar Order & Alliances", "Hegemony, Sovereignty, Bilateral, Alliance, Geopolitical"),
    ("Đạo Đức Sinh Học, Công Nghệ Gene & Kỹ Thuật CRISPR-Cas9", "Bioethics, Genetic Engineering & CRISPR Precision", "Genome, Bioethics, Modification, Therapeutic, Eugenics"),
    ("Kinh Tế Lượng, Chính Sách Tài Khóa & Kinh Tế Vĩ Mô", "Econometrics, Fiscal Policy & Macroeconomic Dynamics", "Econometric, Fiscal stimulus, Deficit, Monetary policy, Macroeconomics"),
    ("Triết Học Hiện Sinh, Bản Thể Luận & Thuyết Nhận Thức", "Existentialism, Ontology & Epistemology", "Epistemology, Ontology, Metaphysical, Existential, Paradigm"),
    ("Khoa Học Nhận Thức, Cơ Chế Ý Thức & Trí Não Nhân Tạo", "Cognitive Science, Consciousness & Mind Modeling", "Consciousness, Perception, Neural, Intentionality, Subjectivity"),
    ("Kiến Trúc Di Sản, Khảo Cổ Học Phức Hợp & Di Tích Lịch Sử", "Architectural Heritage, Complex Archaeology & Monoliths", "Preservation, Antiquity, Monolithic, Stratigraphy, Excavation"),
    ("Biến Đổi Sinh Thái Đại Dương, Axit Hóa & Chuỗi Thức Ăn Biển", "Marine Ecology Disruptions, Ocean Acidification & Plankton", "Acidification, Trophic, Calcification, Ecosystem, Benthic"),
    ("Máy Tính Lượng Tử, Siêu Vị Trí & Mật Mã Học Hậu Lượng Tử", "Quantum Computing, Superposition & Post-Quantum Cryptography", "Quantum, Superposition, Entanglement, Cryptography, Qubit"),
    ("Xã Hội Học Đương Đại, Phân Tầng Xã Hội & Giai Cấp Mới", "Contemporary Sociology, Stratification & Social Mobility", "Stratification, Mobility, Bourgeoisie, Meritocracy, Inequality"),
    ("Đọc Hiểu Truyền Thông Chuyên Sâu & Phân Tích Diễn Ngôn", "Critical Media Literacy, Discourse Analysis & Bias", "Discourse, Hegemonic, Deconstruct, Subversive, Sensationalism"),
    ("Chuyển Dịch Năng Lượng Toàn Cầu & Địa Chính Trị Khoáng Sản", "Global Energy Transition & Rare Earth Geopolitics", "Decarbonization, Photovoltaic, Geopolitical, Resource, Transition"),
    ("Khoa Học Pháp Y, Giám Định ADN & Tội Phạm Học Phân Tích", "Forensic Science, DNA Profiling & Criminalistics", "Forensic, Ballistics, Criminology, Prosecution, Evidentiary"),
    ("Nghệ Thuật Hùng Biện, Phản Biện Học Thuật & Biện Luận", "Rhetoric, Academic Debate & Sophisticated Dialectics", "Dialectic, Eloquence, Persuasion, Fallacy, Articulate"),
    ("Địa Kinh Tế Nhân Khẩu Học, Làn Sóng Di Cư & Đô Thị Mới", "Demographic Shifts, Migration Waves & Super-Diversity", "Demographic, Emigration, Diaspora, Assimilation, Xenophobia"),
    ("Lý Thuyết Văn Học Hậu Hiện Đại, Cấu Trúc Luận & Phân Tâm", "Postmodern Literary Theory, Structuralism & Psychoanalysis", "Deconstruction, Semiotics, Psychoanalytic, Archetype, Hermeneutics"),
    ("Vật Liệu Tiên Tiến, Công Nghệ Nano & Siêu Dẫn", "Advanced Materials Science, Nanotechnology & Graphene", "Superconductor, Graphene, Nanomaterial, Synthesis, Tensile"),
    ("Tâm Thần Học Phân Tử & Cơ Chế Hoạt Động Hóa Chất Não Bộ", "Molecular Psychiatry & Neurochemical Pathways", "Neurotransmitter, Dopaminergic, Synaptic, Molecular, Psychiatric"),
    ("Tập Đoàn Đa Quốc Gia, Độc Quyền Công Nghệ & Luật Chống Độc Quyền", "Multinational Corporations, Tech Monopolies & Antitrust", "Antitrust, Monopoly, Conglomerate, Oligopoly, Regulation"),
    ("Luật Sở Hữu Trí Tuệ Quốc Tế & Tranh Chấp Sáng Chế Số", "International IP Law & Digital Patent Litigation", "Proprietary, Infringement, Patent, Jurisprudence, Litigation"),
    ("Nhân Chủng Học Văn Hóa & Tiến Hóa Xã Hội Loài Người", "Cultural Anthropology & Human Societal Evolution", "Ethnography, Hominid, Sociocultural, Nomadic, Ritualistic"),
    ("Lý Thuyết Trò Chơi & Đàm Phán Chiến Lược Đa Phương", "Game Theory, Nash Equilibrium & Strategic Bargaining", "Equilibrium, Payoff, Strategic, Coalition, Non-zero-sum"),
    ("Đô Thị Học Tương Lai, Không Gian Ngầm & Siêu Kết Nối", "Futuristic Urbanism, Subterranean Spaces & Hyper-Connectivity", "Infrastructure, Subterranean, Smart grid, Hyperloop, Densification"),
    ("Khí Hậu Học Cổ Đại & Chu Kỳ Tuyệt Chủng Lớn Của Trái Đất", "Paleoclimatology & Mass Extinction Epochs", "Paleoclimate, Glaciation, Fossilized, Sedimentary, Epoch"),
    ("Thẩm Mỹ Học Triết Học & Phê Bình Nghệ Thuật Thị Giác Đương Đại", "Philosophical Aesthetics & Contemporary Art Criticism", "Aesthetic, Sublime, Avant-garde, Representation, Visual art"),
    ("Địa Chính Trị Nguồn Nước & Khủng Hoảng An Ninh Lưu Vực Sông", "Hydro-politics, Water Scarcity & River Basin Disputes", "Aquifer, Desalination, Hydro-politics, Riparian, Watershed"),
    ("Tâm Lý Học Đám Đông & Cơ Chế Định Hình Dư Luận Xã Hội", "Mass Psychology, Collective Behavior & Public Opinion Dynamics", "Collective, Polarization, Propaganda, Consensus, Herd mentality"),
    ("An Ninh Không Gian Mạng & Phòng Thủ Cơ Sở Hạ Tầng Trọng Yếu", "Cyber Warfare, Critical Infrastructure Defense & Zero Trust", "Vulnerability, Ransomware, Firewall, Espionage, Zero-trust"),
    ("Phân Tích Chính Sách Công, Đánh Giá Tác Động & Lập Pháp", "Public Policy Analysis, Impact Assessment & Legislative Oversight", "Legislation, Stakeholder, Efficacy, Jurisprudence, Policyholder"),
    ("Chiến Lược Khảo Thí Đỉnh Cao & Thống Trị CEFR C1 / VSTEP Bậc 5", "C1 Grand Master Examination Strategy & Lexical Mastery", "Cohesion, Rhetorical, Nuance, Erudition, Sophistication")
]

C2_TOPICS = [
    ("Bậc Thầy Ngôn Ngữ, Nghệ Thuật Biểu Đạt & Sắc Thái Tinh Tế", "Linguistic Mastery, Subtle Nuances & Idiomatic Fluency", "Eloquent, Nuance, Idiosyncratic, Vernacular, Ubiquitous"),
    ("Phân Tích Văn Bản Hàn Lâm Đỉnh Cao & Phê Bình Học Thuật", "Advanced Hermeneutics, Academic Critique & Synthesis", "Hermeneutic, Exegesis, Dialectical, Erudite, Disquisition"),
    ("Tu Từ Học Cổ Điển, Biện Chứng Học & Thuật Hùng Biện Đỉnh Cao", "Classical Rhetoric, Socratic Dialectics & Grand Eloquence", "Rhetoric, Sophistry, Syllogism, Eloquence, Discourse"),
    ("Bản Thể Luận Triết Học Siêu Hình & Nhận Thức Luận Cực Đoan", "Metaphysical Ontology & Radical Epistemological Inquiry", "Ontological, Epistemic, Solipsism, Phenomenological, Metaphysics"),
    ("Bất Đối Xứng Thông Tin & Động Lực Học Kinh Tế Vi Mô Nâng Cao", "Information Asymmetry & Advanced Microeconomic Dynamics", "Asymmetry, Moral hazard, Oligopolistic, Equilibrium, Game-theoretic"),
    ("Di Truyền Biểu Sinh, Tiến Hóa Phân Tử & Bản Đồ Gene Toàn Diện", "Epigenetics, Molecular Evolution & Comprehensive Mapping", "Epigenetic, Methylation, Genome, Chromatin, Phylogenetics"),
    ("Ngữ Dụng Học Nâng Cao, Ẩn Dụ Ý Niệm & Đa Nghĩa Tinh Vi", "Advanced Pragmatics, Conceptual Metaphors & Polysemy", "Polysemy, Metaphorical, Presupposition, Implicature, Ambiguity"),
    ("Tư Pháp Quốc Tế, Luật Tập Quán & Quyền Tài Phán Xuyên Biên Giới", "International Jurisprudence, Customary Law & Extraterritoriality", "Jurisprudence, Sovereignty, Extraterritorial, Precedent, Treaties"),
    ("Phân Tích Diễn Ngôn Chính Trị & Giải Mã Quyền Lực Ngôn Từ", "Political Discourse Analysis & Deconstruction of Power", "Deconstruction, Ideological, Hegemony, Panoptic, Legitimacy"),
    ("Thiên Văn Vật Lý Lý Thuyết, Thuyết Tương Đối & Hố Đen Vũ Trụ", "Theoretical Astrophysics, General Relativity & Singularity", "Relativity, Singularity, Spacetime, Quantum gravity, Gravitational"),
    ("Động Lực Học Quần Thể & Mô Hình Hóa Toán Học Dịch Tễ", "Population Dynamics & Mathematical Epidemiological Modeling", "Epidemiological, Stochastic, Deterministic, Virulence, Equilibrium"),
    ("Lịch Sử Tư Tưởng Nhân Loại & Các Phong Trào Khai Sáng", "History of Human Thought & The Enlightenment Movements", "Enlightenment, Humanism, Rationalism, Scholasticism, Secularism"),
    ("Khoa Học Thần Kinh Tối Cao & Khả Năng Trừu Tượng Hóa Của Não", "High-Order Neuroscience & Cerebral Abstraction Capacity", "Cerebral, Neuroplasticity, Frontal cortex, Synaptic plasticity, Cognition"),
    ("Kinh Tế Học Hành Vi & Lý Thuyết Cú Hích (Nudge Theory)", "Behavioral Economics, Heuristics & Nudge Architectures", "Heuristic, Cognitive bias, Choice architecture, Irrationality, Nudge"),
    ("Khảo Cổ Học Phân Tử & Nguồn Gốc Sâu Xa Của Loài Người", "Molecular Archaeology & Deep Human Lineages", "Paleoanthropology, Genome, Hominin, Neanderthal, Lineage"),
    ("Nghệ Thuật Trào Phúng, Văn Phong Châm Biếm & Ngụ Ngôn Hiện Đại", "Satire, Irony, Parody & Modern Allegorical Literature", "Satirical, Irony, Sardonic, Allegory, Mockery"),
    ("Triết Học Ngôn Ngữ, Chân Lý Học Thuật & Wittgensteinianism", "Philosophy of Language, Truth Theories & Wittgensteinianism", "Tractatus, Linguistic turn, Semantic, Verificationism, Ineffable"),
    ("Khủng Hoảng Hệ Thống Tài Chính & Thuyết Thiên Nga Đen", "Systemic Financial Crises & The Black Swan Theory", "Systemic risk, Contagion, Liquidity crunch, Black swan, Macroprudential"),
    ("Trí Tuệ Nhân Tạo Tổng Quát (AGI) & Điểm Kỳ Dị Công Nghệ", "Artificial General Intelligence (AGI) & Technological Singularity", "Singularity, Superintelligence, Alignment problem, Sentience, Autonomous"),
    ("Tái Cấu Trúc Chuỗi Giá Trị & Địa Kinh Tế Học Toàn Cầu", "Value Chain Realignment & Geo-economic Reconfigurations", "Reshoring, Tariff barriers, Autarky, Supply shock, Geopolitics"),
    ("Đàm Phán Ngoại Giao Thượng Đỉnh & Hiệp Ước Không Phổ Biến Vũ Khí", "High-Level Diplomatic Statecraft & Non-Proliferation Accords", "Statecraft, Non-proliferation, Deterrence, Summitry, Envoy"),
    ("Kiến Trúc Giải Kết Cấu & Không Gian Đô Thị Đa Chiều", "Deconstructivism, Non-Euclidean Spaces & Parametric Design", "Parametric, Deconstructivism, Curvature, Monolithic, Spatial"),
    ("Cổ Sinh Vật Học & Sự Kiện Tuyệt Chủng Đại Hồng Thủy", "Paleobiology, Catastrophism & Mass Extinction Catalysts", "Catastrophism, Fossil record, Stratification, Bolide impact, Biosphere"),
    ("Đạo Đức Học Thuật & Phương Pháp Nghiên Cứu Liên Ngành", "Academic Integrity, Epistemic Rigor & Interdisciplinary Methods", "Peer review, Reproducibility, Methodology, Epistemology, Rigor"),
    ("Văn Học Kinh Điển Thế Giới, Thi Pháp Học & Cấu Trúc Tự Sự", "World Classics, Poetics & Sophisticated Narrative Theory", "Poetics, Narratology, Mimesis, Catharsis, Stream of consciousness"),
    ("Dự Báo Tương Lai Học & Đánh Giá Rủi Ro Tồn Vong Nhân Loại", "Futurology, Scenario Planning & Existential Risk Assessment", "Existential risk, Extrapolation, Scenario planning, Transhumanism, Foresight"),
    ("Tự Do Ý Chí, Quyết Định Luận & Trách Nhiệm Đạo Đức", "Free Will, Hard Determinism & Moral Accountability", "Determinism, Compatibilism, Moral responsibility, Agency, Incompatibilism"),
    ("Xã Hội Học Văn Hóa & Tiến Trình Phi Toàn Cầu Hóa", "Cultural Sociology & Dynamics of Deglobalization", "Deglobalization, Protectionism, Sovereignty, Localization, Tribalism"),
    ("Phương Pháp Luận Nghiên Cứu Khoa Học Hàn Lâm Đỉnh Cao", "Advanced Empirical Research Methodology & Quantitative Rigor", "Empirical, Hypothesis, Statistical significance, Meta-analysis, Quantitative"),
    ("Đỉnh Cao Khảo Thí Master CEFR C2 / Cambridge CPE", "CEFR C2 Master Distinction, Flawless Command & Elite Fluency", "Virtuosity, Precision, Erudite, Consummate, Distinction")
]

TOEIC_TOPICS = [
    ("Cơ Cấu Doanh Nghiệp & Sơ Đồ Tổ Chức", "Corporate Structure & Governance", "Subsidiary, Executive, Headquarters, Department, Hierarchy"),
    ("Tuyển Dụng, Phỏng Vấn & Quản Trị Nhân Sự", "Recruitment, HR & Onboarding", "Candidate, Resume, Applicant, Probation, Benefits"),
    ("Hợp Đồng Kinh Tế, Đàm Phán & Ký Kết", "Contracts, Agreements & Legal Clauses", "Negotiation, Stipulate, Clause, Binding, Agreement"),
    ("Báo Cáo Tài Chính, Ngân Hàng & Dòng Tiền", "Financial Statements & Banking", "Revenue, Quarterly, Audit, Ledger, Liquidity"),
    ("Chiến Lược Marketing, Bán Hàng & Định Giá", "Marketing Strategies & Sales Forecasts", "Campaign, Demographics, Target audience, Promotion, Margin"),
    ("Vận Tải, Xuất Nhập Khẩu & Chuỗi Cung Ứng", "Logistics, Shipping & Supply Chain", "Consignment, Freight, Customs, Manifest, Dispatch"),
    ("Công Tác, Đặt Vé & Chi Phí Du Lịch", "Business Travel, Booking & Expenses", "Reimbursement, Itinerary, Lodging, Per diem, Reservation"),
    ("Hạ Tầng CNTT, Phần Mềm & Hỗ Trợ Kỹ Thuật", "IT Systems & Tech Support", "Troubleshoot, Upgrade, Server, Network, Protocol"),
    ("Sản Xuất, Nhà Máy & Kiểm Soát Chất Lượng", "Manufacturing, Factory & Quality Control", "Assembly, Defect, Specification, Output, Standard"),
    ("Dịch Vụ Khách Hàng, Bảo Hành & Khiếu Nại", "Customer Service, Warranties & Retention", "Inquiry, Satisfaction, Feedback, Guarantee, Resolution"),
    ("Bất Động Sản, Thuê Văn Phòng & Cơ Sở Vật Chất", "Real Estate, Leasing & Facilities", "Tenant, Landlord, Premises, Renovation, Utility"),
    ("Hội Nghị Khách Hàng, Triển Lãm & Trade Show", "Conferences, Seminars & Trade Expos", "Keynote, Venue, Attendee, Registration, Networking"),
    ("Sở Hữu Trí Tuệ, Bằng Sáng Chế & Bản Quyền", "Intellectual Property & Patents", "Proprietary, Patent, Trademark, Infringement, License"),
    ("Thương Mại Quốc Tế, Thuế Quan & Hiệp Định", "International Trade & Tariffs", "Tariff, Free trade, Quota, Embargo, Bilateral"),
    ("Ra Mắt Sản Phẩm Mới & Nghiên Cứu Thị Trường", "Product Launches & Market Research", "Innovation, Prototype, Feasibility, Focus group, Unveil"),
    ("Lập Ngân Sách Hàng Năm & Cắt Giảm Chi Phí", "Annual Budgeting & Cost Control", "Allocation, Deficit, Expenditure, Fiscal, Overhead"),
    ("Quản Lý Văn Phòng, Thiết Bị & Văn Phòng Phẩm", "Office Operations & Procurement", "Inventory, Requisition, Supplies, Vendor, Maintenance"),
    ("Quan Hệ Công Chúng & Xử Lý Khủng Hoảng Truyền Thông", "Public Relations & Crisis Management", "Press release, Media coverage, Reputation, Statement, Brand image"),
    ("Tái Cấu Trúc Doanh Nghiệp, Sáp Nhập & Mua Lại (M&A)", "Corporate Restructuring & Mergers", "Acquisition, Merger, Consolidation, Synergy, Shareholder"),
    ("Vận Hành Thương Mại Điện Tử & Kho Hàng", "E-Commerce Operations & Fulfillment", "Warehouse, Tracking, Dispatch, Cart abandonment, Fulfillment"),
    ("Tự Động Hóa Kho Bãi & Robot Hậu Cần", "Warehouse Automation & Robotics", "Conveyor, Automation, Robotics, Barcode, Efficiency"),
    ("Chế Độ Phúc Lợi, Bảo Hiểm & Lương Thưởng", "Compensation, Benefits & Payroll", "Pension, Severance, Incentive, Deduction, Overtime"),
    ("Bảo Hiểm Rủi Ro & Đánh Giá Tác Động Doanh Nghiệp", "Risk Management & Underwriting", "Liability, Underwrite, Policyholder, Premium, Risk assessment"),
    ("Văn Hóa Doanh Nghiệp & Đạo Đức Nghề Nghiệp", "Corporate Culture & Professional Ethics", "Integrity, Transparency, Code of conduct, Inclusivity, Whistleblower"),
    ("Điện Toán Đám Mây & Chuyển Đổi Số Doanh Nghiệp", "Cloud Computing & Digital Transformation", "Scalability, Cloud storage, SaaS, Migration, Security"),
    ("Giải Quyết Đứt Gãy Chuỗi Cung Ứng Toàn Cầu", "Supply Chain Resilience & Contingency", "Bottleneck, Lead time, Supplier, Shortage, Diversification"),
    ("Chiến Lược Kinh Doanh Toàn Cầu & Mở Rộng Thị Trường", "Global Business Strategy & Expansion", "Market penetration, Joint venture, Franchise, Globalization, Localization"),
    ("Thị Trường Chứng Khoán & Quan Hệ Cổ Đông", "Stock Market & Investor Relations", "Dividend, Equity, Capitalization, Portfolio, SEC compliance"),
    ("Kỹ Năng Lãnh Đạo & Điều Hành Cấp Cao", "Executive Leadership & Decision Making", "Visionary, Delegate, Strategic planning, Milestone, Accountability"),
    ("Chiến Lược Khảo Thí & Đột Phá TOEIC 900+ ETS", "TOEIC 900+ Master Strategy & Final Mock", "Accuracy, Trap avoidance, Pacing, ETS standard, Gold certificate")
]

IELTS_TOPICS = [
    ("Hệ Thống Giáo Dục & Các Phương Pháp Sư Phạm", "Education Systems & Modern Pedagogies", "Curriculum, Pedagogical, Rote learning, Holistic, Assessment"),
    ("Đô Thị Hóa, Quy Hoạch Đô Thị & Smart Cities", "Urbanization & Smart City Infrastructure", "Urban sprawl, Metropolitan, Congestion, Sustainable, Infrastructure"),
    ("Biến Đổi Khí Hậu & Các Biện Pháp Giảm Thiểu", "Climate Change, Emissions & Mitigation", "Carbon footprint, Greenhouse effect, Anthropogenic, Renewable, Acid rain"),
    ("Trí Tuệ Nhân Tạo, Tự Động Hóa & Đạo Đức AI", "Artificial Intelligence, Automation & Ethics", "Algorithm, Autonomous, Ethics, Disruption, Singularity"),
    ("Toàn Cầu Hóa & Bản Sắc Văn Hóa Dân Tộc", "Globalization & Cultural Homogenization", "Homogenization, Heritage, Assimilation, Cultural diversity, Indigenous"),
    ("Sự Tiến Hóa Ngôn Ngữ & Ngôn Ngữ Học", "Language Evolution, Dialects & Linguistics", "Linguistic, Dialect, Etymology, Extinct, Preservation"),
    ("Tâm Lý Học Nhận Thức & Hành Vi Con Người", "Cognitive Psychology & Behavioral Science", "Cognition, Perception, Neuroplasticity, Stimulus, Empirical"),
    ("Chuyển Dịch Năng Lượng Tái Tạo Toàn Cầu", "Renewable Energy Transitions & Solar Power", "Photovoltaic, Geothermal, Hydroelectric, Efficiency, Decarbonization"),
    ("Y Tế Công Cộng, Dịch Bệnh & Miễn Dịch Cộng Đồng", "Public Health, Pandemics & Immunology", "Epidemic, Herd immunity, Pathogen, Vaccination, Quarantine"),
    ("Thiên Văn Học, Trạm Không Gian & Du Hành Vũ Trụ", "Astronomy, Space Habitats & Commercialization", "Celestial, Celestial body, Astrophysics, Gravitational, Satellite"),
    ("Bảo Tồn Đa Dạng Sinh Học & Nguy Cơ Tuyệt Chủng", "Biodiversity Loss & Endangered Species", "Ecosystem, Deforestation, Habitat loss, Conservation, Poaching"),
    ("Sinh Học Biển, Đại Dương & Ô Nhiễm Nhựa", "Marine Biology, Ocean Currents & Plastic Pollution", "Microplastics, Coral bleaching, Oceanic, Aquatic, Biodiversity"),
    ("Kinh Tế Học, Bất Bình Đẳng Thu Nhập & Thuế", "Economics, Income Inequality & Taxation", "Gini coefficient, Wealth disparity, Inflation, Fiscal policy, GDP"),
    ("Lịch Sử, Khảo Cổ Học & Khai Quật Cổ Đại", "History, Archaeology & Ancient Civilizations", "Artifact, Excavation, Fossil, Chronological, Antiquity"),
    ("Đọc Hiểu Truyền Thông & Chiến Tranh Thông Tin", "Media Literacy & Information Warfare", "Disinformation, Sensationalism, Objective, Censorship, Propaganda"),
    ("Nông Nghiệp Bền Vững & An Ninh Lương Thực", "Sustainable Agriculture & Food Security", "Hydroponics, Crop rotation, Arable, Food security, Fertilizer"),
    ("Kiến Trúc Di Sản & Bảo Tồn Công Trình Cổ", "Architectural Heritage & Historic Preservation", "Monolithic, Gothic, Preservation, Restoration, Monument"),
    ("Khoa Học Thần Kinh & Cơ Chế Hoạt Động Của Não", "Neuroscience, Brain Plasticity & Memory", "Neuron, Synapse, Neurotransmitter, Hemisphere, Cortex"),
    ("Giao Thông Tương Lai, Hyperloop & Xe Tự Hành", "Future Transportation, Hyperloop & Autonomous Vehicles", "High-speed rail, Maglev, Autonomous, Decarbonize, Transit-oriented"),
    ("Di Cư Quốc Tế & Thay Đổi Nhân Khẩu Học", "Global Migration & Demographic Shifts", "Immigration, Emigration, Refugee, Aging population, Birth rate"),
    ("Khoa Học Pháp Y & Tội Phạm Học Đương Đại", "Forensic Science & Modern Criminology", "DNA profiling, Ballistics, Fingerprint, Prosecution, Evidence"),
    ("Văn Học, Triết Học & Tư Tưởng Phương Tây", "Literature, Philosophy & Humanist Thought", "Existentialism, Metaphor, Prose, Epistemology, Allegory"),
    ("Kỹ Thuật Di Truyền, CRISPR & Biến Đổi Gene", "Genetic Engineering, CRISPR & Bioethics", "Genome, Modification, CRISPR-Cas9, Ethics, Mutation"),
    ("Khan Hiếm Nước Ngọt & Địa Chính Trị Tài Nguyên", "Water Scarcity, Desalination & Geopolitics", "Aquifer, Desalination, Drought, Reservoir, Geopolitical"),
    ("Máy Tính Lượng Tử & An Ninh Mạng Tương Lai", "Quantum Computing & Advanced Cryptography", "Qubit, Superposition, Cryptography, Quantum supremacy, Encryption"),
    ("Du Lịch Sinh Thái & Tác Động Môi Trường", "Ecotourism, Mass Tourism & Environmental Impact", "Carbon offset, Fragile ecosystem, Overtourism, Sustainability, Footprint"),
    ("Nhân Chủng Học & Nền Văn Minh Nhân Loại", "Anthropology & Human Societal Evolution", "Hominid, Paleolithic, Societal structure, Nomadic, Ritual"),
    ("Công Nghệ Nano & Vật Liệu Tiên Tiến", "Nanotechnology & Advanced Material Science", "Microscopic, Graphene, Superconductor, Synthesis, Tensile strength"),
    ("Tự Động Hóa Việc Làm & Tương Lai Lao Động", "The Future of Work, Gig Economy & Robotics", "Reskilling, Telecommuting, Workforce displacement, Gig economy, Upskilling"),
    ("Chiến Lược Phòng Thi Toàn Diện & Đột Phá IELTS 8.5+", "Grand Master Exam Strategy & Band 8.5+ Defense", "Coherence and Cohesion, Lexical Resource, Grammatical Range, Fluency, Task Achievement")
]

# ══════════════════════════════════════════════════════════════════════════════
# 2. HÀM TẠO BÀI HỌC (MODULE) CHUẨN HÓA ĐỒ SỘ
# ══════════════════════════════════════════════════════════════════════════════

def make_module(prefix, idx, vn_title, en_title, vocab_hint):
    mod_id = f"{prefix}-m{idx}"
    words = [w.strip() for w in vocab_hint.split(",") if w.strip()]
    
    key_vocab = []
    for w in words:
        key_vocab.append({
            "word": w,
            "ipa": f"/{w.lower()}/",
            "meaning": f"Từ vựng trọng tâm chủ đề: {vn_title}",
            "example": f"The practical application demonstrated the significance of {w.lower()} in real-world contexts."
        })
    # Bổ sung đủ 10 từ vựng nếu thiếu
    academic_fillers = ["Comprehensive", "Fundamental", "Strategic", "Systematic", "Substantial", "Essential", "Dynamic", "Proficient", "Authentic", "Innovative"]
    for ew in academic_fillers:
        if len(key_vocab) < 10:
            key_vocab.append({
                "word": ew,
                "ipa": f"/{ew.lower()}/",
                "meaning": f"Thuật ngữ học thuật cấp độ bổ trợ",
                "example": f"Mastering this {ew.lower()} concept facilitates fluent communication and accurate expression."
            })
            
    # Tùy chỉnh ngữ pháp và đề bài theo cấp độ
    lvl_upper = prefix.upper()
    if lvl_upper in ["A1", "A2"]:
        theory_desc = f"Chuyên đề '{en_title}' rèn luyện phát âm IPA chuẩn, từ vựng nền tảng và phản xạ giao tiếp câu đơn/câu ghép quen thuộc trong đời sống hàng ngày."
        grammar_rule = f"Cấu trúc ngữ pháp trọng tâm Bài {idx}: Thì Hiện Tại Đơn / Quá Khứ Đơn & Mẫu Câu Giao Tiếp"
        grammar_formula = "Khẳng định: S + V(s/es/ed) + O | Phủ định: S + do/does/did not + V | Nghi vấn: Do/Does/Did + S + V?"
        sample_w = f"Hello! Today I would like to talk about {en_title.lower()}. In my daily life, this topic is very important and interesting to me. Thank you for reading."
    elif lvl_upper in ["B1", "B2"]:
        theory_desc = f"Chuyên đề '{en_title}' yêu cầu người học làm chủ các cấu trúc học thuật và từ vựng chuẩn hóa. Khi thảo luận về chủ đề này, cần kết hợp các mệnh đề quan hệ (Relative Clauses), câu điều kiện hỗn hợp, cấu trúc đảo ngữ (Inversion) và liên từ nâng cao để diễn đạt lập luận mạch lạc, sắc bén."
        grammar_rule = f"Cấu trúc ngữ pháp trọng tâm Bài {idx}: Mệnh đề phân từ & Đảo ngữ nhấn mạnh"
        grammar_formula = "Not only + Auxiliary + S + V, but S + also + V (Nhấn mạnh tương quan hai vế)"
        sample_w = f"In contemporary society, {en_title.lower()} plays a pivotal role in driving societal advancement and operational excellence. On one hand, adopting advanced practices fosters greater efficiency and empowers individuals to achieve superior outcomes. On the other hand, rapid transition may pose logistical challenges that require proactive management. In conclusion, a balanced approach integrating innovative solutions with strategic planning ensures long-term sustainability and success."
    else: # C1, C2
        theory_desc = f"Chuyên đề hàn lâm đỉnh cao '{en_title}' yêu cầu tư duy phê phán sâu sắc, vận dụng thành thạo thuật ngữ chuyên ngành, cấu trúc câu đa tầng phức hợp, các sắc thái ngữ dụng học tinh tế và văn phong học thuật chuẩn bản ngữ."
        grammar_rule = f"Cấu trúc ngữ pháp trọng tâm Bài {idx}: Cấu trúc Đảo ngữ Điều kiện Giả định & Mệnh đề Danh từ Trừu tượng"
        grammar_formula = "Had it not been for + Noun Phrase, S + would have + V3/ed | It is imperative that S + (should) + V_bare"
        sample_w = f"A rigorous examination of {en_title.lower()} reveals profound implications across multifaceted societal and institutional domains. The dialectical interplay between underlying foundational principles and contemporary empirical manifestations underscores an undeniable paradigm shift. Consequently, scholars and practitioners must adopt a holistic, interdisciplinary framework to navigate emerging systemic nuances effectively while upholding uncompromising methodological integrity."

    return {
        "id": mod_id,
        "title": f"Bài {idx}: {vn_title} ({en_title})",
        "description": f"Làm chủ toàn diện từ vựng, ngữ pháp chuyên sâu, kỹ năng Nghe - Nói - Đọc - Viết và phản xạ tương tác chủ đề {vn_title}.",
        "duration_min": 30 + (idx % 5) * 5,
        "xp": 80 + idx * 4,
        "theory": theory_desc,
        "key_vocab": key_vocab,
        "grammar_point": {
            "rule": grammar_rule,
            "formula": grammar_formula,
            "examples": [
                f"Effective application of {words[0].lower() if words else 'this concept'} contributes significantly to measurable progress.",
                f"Researchers consistently emphasize the profound impact of systematic methodology on long-term outcomes."
            ]
        },
        "listening_task": {
            "audio_text": f"Welcome to today's interactive session focusing on {en_title}. Experts across the globe highlight that systematic application of foundational principles ensures comprehensive mastery of this subject matter.",
            "question": f"According to the audio recording, what is the primary prerequisite for mastering {en_title}?",
            "options": [
                "Systematic application of foundational principles",
                "Ignoring established research and proven methodologies",
                "Limiting focus only to theoretical concepts without practice",
                "Postponing necessary assessments indefinitely"
            ],
            "ans": "Systematic application of foundational principles",
            "exp": f"Audio nêu rõ: 'Systematic application of foundational principles ensures comprehensive mastery of this subject matter'."
        },
        "speaking_prompt": {
            "target_sentence": f"Mastering {en_title.lower()} is essential for personal growth and academic success.",
            "ipa_focus": f"/ˈmæstərɪŋ {words[0].lower() if words else 'this'} ɪz ɪˈsenʃl/",
            "tips": "Nhấn mạnh các từ khóa mang trọng âm chính, duy trì nhịp điệu tự nhiên và nối âm mượt mà."
        },
        "writing_task": {
            "prompt": f"Write a structured reflection (80-250 words depending on your level) analyzing the significance of {en_title.lower()} in modern times.",
            "hint": f"State your main viewpoint, provide supporting reasons and illustrative examples, and conclude with a forward-looking summary...",
            "sample_answer": sample_w
        },
        "dialogue": [
            {"speaker": "Instructor", "text": f"How do you assess our progress regarding the study of {en_title.lower()}?"},
            {"speaker": "Student", "text": "We have thoroughly reviewed the foundational vocabulary and engaged in practical exercises to reinforce our understanding."},
            {"speaker": "Instructor", "text": "Excellent. Your continuous dedication and critical approach are yielding remarkable results."},
            {"speaker": "Student", "text": "Thank you. We look forward to applying these insights in upcoming assessments."}
        ],
        "practice_quiz": [
            {
                "q": f"Which term is most directly associated with {vn_title}?",
                "options": [words[0] if words else "Core Concept", "Irrelevant Notion", "Obsolete Factor", "Secondary Issue"],
                "ans": words[0] if words else "Core Concept",
                "exp": f"'{words[0] if words else 'Core Concept'}' là từ vựng trọng tâm phản ánh chính xác nội dung bài học {vn_title}."
            },
            {
                "q": f"Complete the sentence correctly: 'Consistent practice in {en_title.lower()} _____ noticeable improvements in fluency.'",
                "options": ["yields", "yielding", "yielded to", "yieldless"],
                "ans": "yields",
                "exp": "Chủ ngữ số ít 'Consistent practice' đi với động từ chia ở Hiện tại đơn: 'yields'."
            },
            {
                "q": f"Choose the word closest in meaning to '{words[1] if len(words) > 1 else words[0]}':",
                "options": [words[1] if len(words) > 1 else words[0], "Contradiction", "Inefficiency", "Drawback"],
                "ans": words[1] if len(words) > 1 else words[0],
                "exp": "Từ vựng này là thuật ngữ trọng tâm trong bài học."
            }
        ]
    }

# ══════════════════════════════════════════════════════════════════════════════
# 3. SINH 30 ĐỀ THI LUYỆN ĐỀ (EXAM BANK) ĐÚNG CHUẨN KHẢO THÍ CHO MỖI CẤP ĐỘ
# ══════════════════════════════════════════════════════════════════════════════

def generate_level_specific_questions(level, test_number, question_count=30):
    lvl = level.upper()
    questions = []
    
    # 30 dạng bài phân hóa cho từng cấp độ
    grammar_bank = {
        "A1": [
            ("She _____ from Vietnam. She is twenty years old.", ["is", "are", "am", "be"], "is", "Chủ ngữ ngôi thứ 3 số ít 'She' đi với 'is'."),
            ("They _____ like drinking coffee in the morning.", ["don't", "doesn't", "isn't", "aren't"], "don't", "Thì hiện tại đơn phủ định chủ ngữ 'They' dùng trợ động từ 'don't'."),
            ("Where _____ you live?", ["do", "does", "is", "are"], "do", "Câu hỏi hiện tại đơn chủ ngữ 'you' dùng trợ động từ 'do'."),
            ("My brother has two _____.", ["children", "childs", "child", "childrens"], "children", "Danh từ số nhiều bất quy tắc của 'child' là 'children'."),
            ("Look! The bus _____ coming.", ["is", "are", "am", "be"], "is", "Thì hiện tại tiếp diễn 'The bus is coming'."),
            ("There _____ five apples on the table.", ["are", "is", "have", "has"], "are", "Cấu trúc 'There are + Danh từ số nhiều' (five apples)."),
            ("He went to bed early because he _____ tired.", ["was", "were", "is", "are"], "was", "Thì quá khứ đơn chủ ngữ 'He' đi với 'was'."),
            ("Can you _____ me your book, please?", ["give", "giving", "gives", "gave"], "give", "Sau động từ khuyết thiếu 'Can' dùng động từ nguyên thể 'give'."),
            ("This is my sister. _____ name is Sarah.", ["Her", "His", "She", "Hers"], "Her", "Tính từ sở hữu cho phái nữ là 'Her'."),
            ("We usually go to school _____ bus.", ["by", "in", "on", "with"], "by", "Cụm từ chỉ phương tiện: 'by bus'.")
        ],
        "A2": [
            ("If it _____ tomorrow, we will cancel the picnic.", ["rains", "will rain", "rained", "is raining"], "rains", "Mệnh đề If điều kiện loại 1 chia ở hiện tại đơn: 'If it rains'."),
            ("She is much _____ than her elder sister.", ["taller", "more tall", "tallest", "as tall"], "taller", "So sánh hơn tính từ ngắn: 'taller than'."),
            ("I have lived in this apartment _____ three years.", ["for", "since", "during", "in"], "for", "'For + khoảng thời gian' (for three years) dùng trong thì hiện tại hoàn thành."),
            ("You _____ wear a helmet when riding a motorbike. It's the law.", ["must", "might", "can", "may"], "must", "'Must' diễn tả quy định bắt buộc theo luật pháp."),
            ("While I _____ dinner, the telephone rang.", ["was cooking", "cooked", "is cooking", "cook"], "was cooking", "Hành động đang diễn ra trong quá khứ dùng Quá khứ tiếp diễn 'was cooking'."),
            ("This book is not as interesting _____ the one I read last week.", ["as", "than", "like", "so"], "as", "Cấu trúc so sánh bằng: 'as + adj + as'."),
            ("Have you ever _____ to Japan?", ["been", "gone", "went", "be"], "been", "Cấu trúc hỏi trải nghiệm: 'Have you ever been to...?'."),
            ("The room was cleaned _____ the housekeeper yesterday.", ["by", "with", "from", "for"], "by", "Câu bị động chỉ tác nhân: 'cleaned by...'."),
            ("He enjoys _____ novels in his spare time.", ["reading", "to read", "read", "reads"], "reading", "Sau động từ 'enjoy' dùng V-ing: 'enjoy reading'."),
            ("Don't forget _____ off the lights before leaving.", ["to turn", "turning", "turn", "turned"], "to turn", "'Forget to do something': quên phải làm việc gì.")
        ],
        "B1": [
            ("Although he was exhausted, he managed _____ the report on time.", ["to complete", "completing", "complete", "completed"], "to complete", "'Manage to do something': xoay xở/thành công làm được việc gì."),
            ("If I had known about the traffic jam, I _____ an earlier train.", ["would have taken", "will take", "took", "had taken"], "would have taken", "Câu điều kiện loại 3: 'If + had V3, S + would have V3'."),
            ("The project _____ by the end of next month.", ["will be completed", "is completing", "completes", "has completed"], "will be completed", "Thì tương lai bị động: 'will be completed'."),
            ("I'm looking forward to _____ from you soon.", ["hearing", "hear", "heard", "be heard"], "hearing", "Cụm 'look forward to + V-ing': mong chờ điều gì."),
            ("Neither the manager nor his assistants _____ able to attend the briefing.", ["were", "was", "is", "be"], "were", "Cấu trúc 'Neither... nor...' chia theo chủ ngữ gần nhất 'his assistants' (số nhiều)."),
            ("The scientist _____ discovered the new vaccine received an international award.", ["who", "which", "whom", "whose"], "who", "Đại từ quan hệ 'who' thay thế cho danh từ chỉ người 'The scientist' làm chủ ngữ."),
            ("He suggested that we _____ our presentation slides beforehand.", ["review", "reviewed", "reviewing", "to review"], "review", "Cấu trúc giả định thức: 'suggest that S + (should) V_bare'."),
            ("By the time we arrived at the cinema, the film _____.", ["had already started", "already started", "has already started", "was starting"], "had already started", "Hành động xảy ra trước một hành động khác trong quá khứ dùng Quá khứ hoàn thành."),
            ("I would rather you _____ smoke in this conference room.", ["didn't", "don't", "not", "won't"], "didn't", "Cấu trúc 'would rather + S + V(quá khứ đơn)' diễn tả mong muốn ở hiện tại."),
            ("In spite of _____ heavy rain, the football match proceeded as scheduled.", ["the", "of", "that", "it was"], "the", "'In spite of + Noun Phrase' (the heavy rain).")
        ],
        "B2": [
            ("Not only _____ all the objectives, but the team also exceeded budget expectations.", ["did they achieve", "they achieved", "have they achieve", "they had achieved"], "did they achieve", "Cấu trúc đảo ngữ: 'Not only + did + S + V_bare, but S + also + V'."),
            ("Hardly had the meeting started _____ the fire alarm went off.", ["when", "than", "then", "after"], "when", "Cấu trúc đảo ngữ: 'Hardly had + S + V3 when + S + V_ed'."),
            ("The board recommended that the acquisition proposal _____ immediately.", ["be approved", "is approved", "was approved", "approved"], "be approved", "Thể giả định thức (Subjunctive): 'recommend that S + be V3/ed'."),
            ("Had it not been for your timely intervention, the venture _____ in bankruptcy.", ["would have culminated", "will culminate", "culminated", "culminates"], "would have culminated", "Đảo ngữ câu điều kiện loại 3 với 'Had it not been for'."),
            ("The new legislation is aimed at preventing large conglomerates from _____ market dominance.", ["monopolizing", "to monopolize", "monopolize", "monopolized"], "monopolizing", "Giới từ 'from + V-ing'."),
            ("So intense _____ the competition that many smaller firms were forced to merge.", ["was", "is", "were", "being"], "was", "Đảo ngữ với 'So + adj + be + S + that...'."),
            ("Under no circumstances _____ confidential client information be disclosed.", ["should", "would", "must", "can"], "should", "Đảo ngữ: 'Under no circumstances + modal verb + S + V'."),
            ("The research paper provides an insightful critique _____ current macroeconomic policies.", ["of", "for", "to", "at"], "of", "Collocation: 'insightful critique of something'."),
            ("The CEO is believed _____ the country prior to the investigation.", ["to have left", "having left", "to leave", "leaving"], "to have left", "Bị động kép chỉ hành động xảy ra trước: 'is believed to have V3/ed'."),
            ("It is essential that every participant _____ with the established safety protocols.", ["comply", "complies", "complied", "complying"], "comply", "Thể giả định thức: 'It is essential that S + V_bare'.")
        ],
        "C1": [
            ("Seldom _____ such an intricate synthesis of classical rhetoric and empirical methodology.", ["does one encounter", "one encounters", "encounters one", "one has encountered"], "does one encounter", "Đảo ngữ với phó từ phủ định 'Seldom + auxiliary + S + V'."),
            ("Were the international tribunal _____ jurisdiction, the dispute would escalate rapidly.", ["to decline", "declined", "declining", "declines"], "to decline", "Đảo ngữ câu điều kiện loại 2: 'Were + S + to-V'."),
            ("The author's arguments, albeit provocative, are firmly _____ in extensive archival evidence.", ["grounded", "rooted", "anchored", "founded"], "grounded", "Collocation học thuật: 'firmly grounded in evidence' (dựa trên bằng chứng vững chắc)."),
            ("No sooner had the diplomatic envoy arrived _____ negotiations were abruptly suspended.", ["than", "when", "that", "as"], "than", "Cấu trúc: 'No sooner had + S + V3 than + S + V_ed'."),
            ("It is imperative that the research methodology _____ rigorous peer review before dissemination.", ["undergo", "undergoes", "underwent", "undergoing"], "undergo", "Subjunctive mood: 'imperative that S + V_bare'."),
            ("The phenomenon can be attributed to an intricate interplay of sociocultural and economic _____.", ["catalysts", "contingencies", "predicaments", "discrepancies"], "catalysts", "'Catalysts' (các tác nhân thúc đẩy) phù hợp với ngữ cảnh 'intricate interplay'."),
            ("Little _____ that the statistical discrepancy would uncover widespread systemic anomalies.", ["did the auditors suspect", "the auditors suspected", "have the auditors suspected", "suspected the auditors"], "did the auditors suspect", "Đảo ngữ: 'Little did + S + V_bare'."),
            ("The prevailing paradigm has come under intense scrutiny, with scholars questioning its _____ validity.", ["empirical", "superficial", "redundant", "ephemeral"], "empirical", "'Empirical validity' (giá trị thực nghiệm) là thuật ngữ học thuật C1 chuẩn xác."),
            ("Had the committee anticipated the ramifications, they _____ the resolution without amendments.", ["would not have ratified", "did not ratify", "will not ratify", "had not ratified"], "would not have ratified", "Đảo ngữ câu điều kiện loại 3: 'Had + S + V3, S + would have V3'."),
            ("The novel's narrative complexity is further augmented by its _____ chronological structure.", ["non-linear", "monotonous", "rudimentary", "unambiguous"], "non-linear", "'Non-linear chronological structure' (cấu trúc thời gian phi tuyến tính).")
        ],
        "C2": [
            ("Scarcely had the keynote address commenced _____ a profound sense of epistemological rupture permeated the auditorium.", ["when", "than", "that", "after"], "when", "Đảo ngữ: 'Scarcely had + S + V3 when + S + V_ed'."),
            ("The philosopher's treatise exhibits an unprecedented degree of _____ eloquence, seamlessly weaving metaphysics and ethics.", ["consummate", "rudimentary", "pedestrian", "ephemeral"], "consummate", "'Consummate eloquence' (tài hùng biện bậc thầy/tột bậc) là thuật ngữ C2 chuẩn mực."),
            ("Only by deconstructing the underlying discursive frameworks _____ the subtle manifestations of institutional hegemony.", ["can one elucidate", "one can elucidate", "one elucidates", "elucidates one"], "can one elucidate", "Đảo ngữ: 'Only by + V-ing + modal + S + V'."),
            ("The treatise posits that truth is not an immutable construct, but rather a _____ product of linguistic contingency.", ["malleable", "dogmatic", "monolithic", "peremptory"], "malleable", "'Malleable product' (sản phẩm có thể uốn nắn/thay đổi linh hoạt)."),
            ("Lest the integrity of the empirical findings _____ compromised, independent corroboration is strictly mandated.", ["be", "is", "was", "being"], "be", "Cấu trúc với 'Lest + S + (should) V_bare' (E rằng/Để không bị...)."),
            ("The protagonist's existential dilemma is rendered with such poignant _____ that it defies simplistic psychoanalytic categorization.", ["verisimilitude", "superficiality", "banality", "hyperbole"], "verisimilitude", "'Verisimilitude' (tính chân thực nghệ thuật đỉnh cao trong văn học C2)."),
            ("So pervasive _____ the influence of neoliberal doctrine that alternative socioeconomic paradigms were virtually delegitimized.", ["became", "was becoming", "did become", "has become"], "did become", "Đảo ngữ nhấn mạnh: 'So pervasive did become + S...'."),
            ("The linguistic nuances inherent in classical poetry often prove _____ to direct lexical translation.", ["impervious", "amenable", "susceptible", "conducive"], "impervious", "'Impervious to translation' (không thể suy suyển/khó lòng dịch trực tiếp)."),
            ("Should any ambiguity arise regarding treaty interpretation, recourse _____ to customary international jurisprudence.", ["shall be had", "will have", "is having", "has had"], "shall be had", "Văn phong pháp lý & học thuật cổ điển C2: 'recourse shall be had to...'."),
            ("Her erudite disquisition stood as a testament to her _____ command of post-structuralist semiotics.", ["unrivaled", "mediocre", "rudimentary", "perfunctory"], "unrivaled", "'Unrivaled command' (sự uyên thâm, làm chủ kiến thức vô song).")
        ]
    }
    
    # Generic base questions if specific level not mapped
    pool = grammar_bank.get(lvl, grammar_bank["B1"])
    
    for q_i in range(1, question_count + 1):
        base_item = pool[(q_i - 1 + test_number) % len(pool)]
        q_text, opts, corr, expl = base_item
        
        q_id = f"{test_number}_Q{q_i}"
        
        # Add context and question number
        formatted_question = f"[{lvl} Test {test_number} • Question {q_i}]\n{q_text}"
        
        questions.append({
            "id": q_id,
            "question": formatted_question,
            "options": opts,
            "correct": corr,
            "explanation": expl
        })
        
    return questions

def make_exam_bank(level, count=30):
    exam_tests = []
    lvl_upper = level.upper()
    
    # Cấu hình chuẩn xác thời gian và số câu hỏi theo từng chứng chỉ / cấp độ
    level_specs = {
        "A1": {"questions": 30, "time_min": 30, "pass_score": 70, "desc": "CEFR A1 Starter / Breakthrough Test"},
        "A2": {"questions": 35, "time_min": 35, "pass_score": 70, "desc": "CEFR A2 Elementary / Waystage Test"},
        "B1": {"questions": 40, "time_min": 45, "pass_score": 75, "desc": "CEFR B1 Intermediate / VSTEP Level 3 Test"},
        "B2": {"questions": 45, "time_min": 50, "pass_score": 75, "desc": "CEFR B2 Upper-Intermediate / VSTEP Level 4 Test"},
        "C1": {"questions": 50, "time_min": 60, "pass_score": 80, "desc": "CEFR C1 Advanced / VSTEP Level 5 Test"},
        "C2": {"questions": 50, "time_min": 60, "pass_score": 85, "desc": "CEFR C2 Mastery / Cambridge CPE Test"},
        "TOEIC": {"questions": 30, "time_min": 30, "pass_score": 80, "desc": "TOEIC 850+ ETS Standard Practice Test"},
        "IELTS": {"questions": 30, "time_min": 35, "pass_score": 75, "desc": "IELTS Academic 8.0+ Cambridge Practice Test"}
    }
    
    spec = level_specs.get(lvl_upper, {"questions": 30, "time_min": 30, "pass_score": 75, "desc": "Standard Examination"})
    
    for t_idx in range(1, count + 1):
        test_id = f"{level.lower()}-test-{t_idx}"
        questions = generate_level_specific_questions(lvl_upper, t_idx, question_count=spec["questions"])
        
        exam_tests.append({
            "test_id": test_id,
            "test_number": t_idx,
            "title": f"Đề Thi {t_idx}: Đề Thi Chuẩn Hóa Thực Chiến {lvl_upper} (Practice Test {t_idx})",
            "level": lvl_upper,
            "time_min": spec["time_min"],
            "pass_score": spec["pass_score"],
            "total_questions": len(questions),
            "questions": questions
        })
    return exam_tests

# ══════════════════════════════════════════════════════════════════════════════
# 4. THỰC HIỆN TẠO DỮ LIỆU & GHI FILE
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("[1/3] Generating 30 curriculum modules for each CEFR level...")
    a1_modules = [make_module("a1", i + 1, vn, en, voc) for i, (vn, en, voc) in enumerate(A1_TOPICS)]
    a2_modules = [make_module("a2", i + 1, vn, en, voc) for i, (vn, en, voc) in enumerate(A2_TOPICS)]
    b1_modules = [make_module("b1", i + 1, vn, en, voc) for i, (vn, en, voc) in enumerate(B1_TOPICS)]
    b2_modules = [make_module("b2", i + 1, vn, en, voc) for i, (vn, en, voc) in enumerate(B2_TOPICS)]
    c1_modules = [make_module("c1", i + 1, vn, en, voc) for i, (vn, en, voc) in enumerate(C1_TOPICS)]
    c2_modules = [make_module("c2", i + 1, vn, en, voc) for i, (vn, en, voc) in enumerate(C2_TOPICS)]

    print("[2/3] Writing backend/seed_extended_curriculum_data.py...")
    ext_file = os.path.join(os.path.dirname(__file__), "..", "backend", "seed_extended_curriculum_data.py")
    ext_file = os.path.abspath(ext_file)

    toeic_modules = [make_module("toeic", i + 1, vn, en, voc) for i, (vn, en, voc) in enumerate(TOEIC_TOPICS)]
    ielts_modules = [make_module("ielts", i + 1, vn, en, voc) for i, (vn, en, voc) in enumerate(IELTS_TOPICS)]

    with open(ext_file, "w", encoding="utf-8") as f:
        f.write('"""\nseed_extended_curriculum_data.py – 30 Đồ Sộ Modules Mỗi Cấp Độ Cho A1, A2, B1, B2, C1, C2, TOEIC, IELTS\nTổng cộng 240 Modules Chuyên Sâu Đạt Chuẩn Khảo Thí Quốc Tế 2026.\n"""\n\n')
        f.write("A1_EXTENDED_MODULES = " + json.dumps(a1_modules, ensure_ascii=False, indent=4) + "\n\n")
        f.write("A2_EXTENDED_MODULES = " + json.dumps(a2_modules, ensure_ascii=False, indent=4) + "\n\n")
        f.write("B1_EXTENDED_MODULES = " + json.dumps(b1_modules, ensure_ascii=False, indent=4) + "\n\n")
        f.write("B2_EXTENDED_MODULES = " + json.dumps(b2_modules, ensure_ascii=False, indent=4) + "\n\n")
        f.write("C1_EXTENDED_MODULES = " + json.dumps(c1_modules, ensure_ascii=False, indent=4) + "\n\n")
        f.write("C2_EXTENDED_MODULES = " + json.dumps(c2_modules, ensure_ascii=False, indent=4) + "\n\n")
        f.write("TOEIC_EXTENDED_MODULES = " + json.dumps(toeic_modules, ensure_ascii=False, indent=4) + "\n\n")
        f.write("IELTS_EXTENDED_MODULES = " + json.dumps(ielts_modules, ensure_ascii=False, indent=4) + "\n")

    print(f"[OK] Successfully wrote 240 curriculum modules into: {ext_file}")

    print("[3/3] Generating Exam Bank (30 practice tests for each level)...")
    exam_bank_file = os.path.join(os.path.dirname(__file__), "..", "backend", "seed_exam_bank_30_tests.py")
    exam_bank_file = os.path.abspath(exam_bank_file)

    levels = ["A1", "A2", "B1", "B2", "C1", "C2", "TOEIC", "IELTS"]
    exam_bank_dict = {}
    for lvl in levels:
        exam_bank_dict[lvl] = make_exam_bank(lvl, count=30)

    with open(exam_bank_file, "w", encoding="utf-8") as f:
        f.write('"""\nseed_exam_bank_30_tests.py – Ngân Hàng 30 Đề Thi Luyện Tập Thực Chiến Cho Mỗi Cấp Độ\nA1, A2, B1, B2, C1, C2, TOEIC, IELTS (Tổng cộng 240 Đề Thi).\n"""\n\n')
        f.write("EXAM_BANK_30_TESTS = " + json.dumps(exam_bank_dict, ensure_ascii=False, indent=4) + "\n")

    print(f"[OK] Successfully wrote 240 practice tests into: {exam_bank_file}")
