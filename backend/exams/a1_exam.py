# -*- coding: utf-8 -*-
"""
backend/exams/a1_exam.py – Ngân Hàng Đề Thi Chuẩn Hóa CEFR A1 / Cambridge KET A1 / VSTEP Bậc 1
Format Khảo Thí Thực Tế:
1. Kỹ Năng Nghe (Listening): 20 câu hỏi – 25 phút (Part 1: 8 câu, Part 2: 6 câu, Part 3: 6 câu)
2. Kỹ Năng Đọc & Ngôn Ngữ (Reading & Language Use): 30 câu hỏi – 35 phút (Part 1: 6 câu, Part 2: 8 câu, Part 3: 8 câu, Part 4: 8 câu)
3. Kỹ Năng Viết (Writing): 2 Tasks – 25 phút (Task 1: Form & Message 40 từ, Task 2: Short Paragraph 70 từ)
4. Kỹ Năng Nói (Speaking): 2 Parts – 10 phút (Part 1: Personal Info, Part 2: Daily Q&A)
"""

A1_STANDARDIZED_EXAM_DATA = {
    "exam_id": "a1-ket-vstep-cefr-2026-01",
    "title": "Đề Thi Chuẩn Hóa Tiếng Anh CEFR A1 / Cambridge KET A1 / VSTEP Bậc 1 Thực Chiến 2026",
    "level": "A1",
    "standard": "CEFR A1 Breakthrough / VSTEP Bậc 1 Format 2026",
    "total_time_min": 95,
    "pass_gpa": 6.0,

    # ══════════════════════════════════════════════════════════════════════════
    # 1. KỸ NĂNG NGHE (LISTENING) – 20 CÂU HỎI – 25 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "listening": {
        "title": "Kỹ Năng Nghe – CEFR A1 (Listening Comprehension)",
        "total_questions": 20,
        "time_min": 25,
        "instructions": "Bài thi Nghe A1 gồm 3 phần với 20 câu hỏi trắc nghiệm. Lắng nghe và chọn một đáp án đúng nhất (A, B, C hoặc D).",
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Hướng Dẫn & Thông Báo Ngắn (8 câu)",
                "description": "Nghe 8 thông báo ngắn hoặc tin nhắn thoại về sinh hoạt hàng ngày.",
                "audio_script": "This is Part 1 of the CEFR A1 Listening Test. You will hear eight short announcements. Choose the best answer from A, B, C, or D.",
                "questions": [
                    {
                        "id": "A1_L1",
                        "audio_text": "Attention passengers on train 14B to Oxford. The train will depart from Platform 3 at 9:15 AM instead of 9:00 AM.",
                        "question": "What time will the train to Oxford leave?",
                        "options": ["A. 9:00 AM", "B. 9:15 AM", "C. 9:30 AM", "D. 3:00 PM"],
                        "correct": "B. 9:15 AM",
                        "explanation": "Audio thông báo: 'depart from Platform 3 at 9:15 AM'."
                    },
                    {
                        "id": "A1_L2",
                        "audio_text": "Hello, this is Green Grocery. Fresh red apples are on sale today for two dollars per kilo.",
                        "question": "How much are the red apples today?",
                        "options": ["A. $1 per kilo", "B. $2 per kilo", "C. $3 per kilo", "D. $5 per kilo"],
                        "correct": "B. $2 per kilo",
                        "explanation": "Audio nêu rõ: 'for two dollars per kilo'."
                    },
                    {
                        "id": "A1_L3",
                        "audio_text": "Good morning students. Please turn off your mobile phones before entering the English classroom on the second floor.",
                        "question": "What must students do before entering the classroom?",
                        "options": ["A. Turn off mobile phones", "B. Buy a new book", "C. Leave the building", "D. Open the windows"],
                        "correct": "A. Turn off mobile phones",
                        "explanation": "Audio: 'Please turn off your mobile phones before entering the English classroom'."
                    },
                    {
                        "id": "A1_L4",
                        "audio_text": "Hi Tom, this is Anna. Don't forget our swimming class tomorrow at 4:30 PM at City Sports Center.",
                        "question": "What activity will Tom and Anna do tomorrow?",
                        "options": ["A. Playing football", "B. Swimming", "C. Watching a movie", "D. Cooking dinner"],
                        "correct": "B. Swimming",
                        "explanation": "Audio: 'Don't forget our swimming class tomorrow at 4:30 PM'."
                    },
                    {
                        "id": "A1_L5",
                        "audio_text": "Welcome to Sunny Cafe. Today's special lunch is chicken salad with a free cup of orange juice.",
                        "question": "What free drink is included with the special lunch?",
                        "options": ["A. Green tea", "B. Hot coffee", "C. Orange juice", "D. Mineral water"],
                        "correct": "C. Orange juice",
                        "explanation": "Audio: 'with a free cup of orange juice'."
                    },
                    {
                        "id": "A1_L6",
                        "audio_text": "The weather in London today will be sunny in the morning and rainy in the late afternoon. Please carry an umbrella.",
                        "question": "What should people carry today in London?",
                        "options": ["A. A jacket", "B. Sunglasses", "C. An umbrella", "D. A hat"],
                        "correct": "C. An umbrella",
                        "explanation": "Audio khuyên: 'Please carry an umbrella'."
                    },
                    {
                        "id": "A1_L7",
                        "audio_text": "Dear library members, the central library will close early at 5:00 PM today for carpet cleaning.",
                        "question": "Why will the library close early today?",
                        "options": ["A. Carpet cleaning", "B. Staff holiday", "C. Power cut", "D. Bad weather"],
                        "correct": "A. Carpet cleaning",
                        "explanation": "Audio: 'close early at 5:00 PM today for carpet cleaning'."
                    },
                    {
                        "id": "A1_L8",
                        "audio_text": "Doctor Wilson's clinic is on Room 104, right opposite the pharmacy on the ground floor.",
                        "question": "Where is Doctor Wilson's room located?",
                        "options": ["A. Room 101 on first floor", "B. Room 104 opposite the pharmacy", "C. On the roof garden", "D. Next to the main gate"],
                        "correct": "B. Room 104 opposite the pharmacy",
                        "explanation": "Audio: 'Room 104, right opposite the pharmacy on the ground floor'."
                    }
                ]
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Hội Thoại Giao Tiếp Thường Ngày (6 câu)",
                "description": "Nghe 2 đoạn hội thoại ngắn giữa hai người và trả lời các câu hỏi.",
                "audio_script": "This is Part 2. You will hear two conversations. For each question, choose the correct answer.",
                "conversations": [
                    {
                        "conv_id": "a1-conv-1",
                        "context": "Hội thoại 1 (Câu 9 - 11): Mua sắm quần áo tại cửa hàng.",
                        "audio_text": "Customer: Excuse me, do you have this blue T-shirt in size Medium?\nClerk: Yes, we do! Here it is in blue, and we also have it in white.\nCustomer: The blue one looks great. How much is it?\nClerk: It is 15 dollars, but if you buy two, it is only 25 dollars.\nCustomer: Perfect, I will take two blue T-shirts please.",
                        "questions": [
                            {
                                "id": "A1_L9",
                                "question": "What size does the customer want?",
                                "options": ["A. Small", "B. Medium", "C. Large", "D. Extra Large"],
                                "correct": "B. Medium",
                                "explanation": "Khách hỏi: 'do you have this blue T-shirt in size Medium?'."
                            },
                            {
                                "id": "A1_L10",
                                "question": "How much is one T-shirt?",
                                "options": ["A. 10 dollars", "B. 15 dollars", "C. 20 dollars", "D. 25 dollars"],
                                "correct": "B. 15 dollars",
                                "explanation": "Nhân viên nói: 'It is 15 dollars'."
                            },
                            {
                                "id": "A1_L11",
                                "question": "How many T-shirts does the customer decide to buy?",
                                "options": ["A. One", "B. Two", "C. Three", "D. None"],
                                "correct": "B. Two",
                                "explanation": "Khách chốt: 'I will take two blue T-shirts please'."
                            }
                        ]
                    },
                    {
                        "conv_id": "a1-conv-2",
                        "context": "Hội thoại 2 (Câu 12 - 14): Hỏi đường và phương tiện di chuyển.",
                        "audio_text": "Tourist: Excuse me, could you tell me how to get to the National Museum?\nLocal: Sure! You can walk straight down this street for 10 minutes, or take Bus number 7 across the road.\nTourist: How often does Bus 7 arrive?\nLocal: Every 15 minutes. It stops right in front of the museum gate.\nTourist: Thank you very much for your help!",
                        "questions": [
                            {
                                "id": "A1_L12",
                                "question": "Where does the tourist want to go?",
                                "options": ["A. The train station", "B. The National Museum", "C. The central park", "D. The shopping mall"],
                                "correct": "B. The National Museum",
                                "explanation": "Du khách hỏi: 'how to get to the National Museum?'."
                            },
                            {
                                "id": "A1_L13",
                                "question": "Which bus number goes to the museum?",
                                "options": ["A. Bus 5", "B. Bus 7", "C. Bus 10", "D. Bus 15"],
                                "correct": "B. Bus 7",
                                "explanation": "Người dân chỉ: 'take Bus number 7 across the road'."
                            },
                            {
                                "id": "A1_L14",
                                "question": "How long does it take to walk there?",
                                "options": ["A. 5 minutes", "B. 10 minutes", "C. 20 minutes", "D. 30 minutes"],
                                "correct": "B. 10 minutes",
                                "explanation": "Người dân nói: 'walk straight down this street for 10 minutes'."
                            }
                        ]
                    }
                ]
            },
            {
                "part_id": 3,
                "part_title": "Part 3: Độc Thoại & Hướng Dẫn Sinh Hoạt (6 câu)",
                "description": "Nghe 2 bài giới thiệu ngắn và chọn câu trả lời đúng.",
                "audio_script": "This is Part 3. You will hear two short talks. Choose the best answer.",
                "talks": [
                    {
                        "talk_id": "a1-talk-1",
                        "context": "Bài nói 1 (Câu 15 - 17): Giới thiệu về Câu lạc bộ Tiếng Anh cuối tuần.",
                        "audio_text": "Hello everyone! Welcome to the Weekend English Club. We meet every Saturday from 2:00 PM to 4:00 PM in Room 205. Members practice speaking, play vocabulary games, and watch short English films. Joining our club is completely free for all new students.",
                        "questions": [
                            {
                                "id": "A1_L15",
                                "question": "On which day does the English Club meet?",
                                "options": ["A. Friday", "B. Saturday", "C. Sunday", "D. Monday"],
                                "correct": "B. Saturday",
                                "explanation": "Bài nói nêu: 'We meet every Saturday'."
                            },
                            {
                                "id": "A1_L16",
                                "question": "How long is each meeting session?",
                                "options": ["A. 1 hour", "B. 2 hours", "C. 3 hours", "D. 4 hours"],
                                "correct": "B. 2 hours",
                                "explanation": "Từ 2:00 PM đến 4:00 PM là 2 giờ (2 hours)."
                            },
                            {
                                "id": "A1_L17",
                                "question": "How much is the membership fee for new students?",
                                "options": ["A. $10 per month", "B. Completely free", "C. $5 per week", "D. $20 per year"],
                                "correct": "B. Completely free",
                                "explanation": "Bài nói: 'Joining our club is completely free for all new students'."
                            }
                        ]
                    },
                    {
                        "talk_id": "a1-talk-2",
                        "context": "Bài nói 2 (Câu 18 - 20): Hướng dẫn tham quan Vườn Bách Thảo.",
                        "audio_text": "Welcome visitors to Green Park Botanical Garden. The garden is open from 8:00 AM to 6:00 PM daily. Please remember not to pick flowers or feed the wild birds. Bicycles are allowed on the main paved paths only. Enjoy your visit!",
                        "questions": [
                            {
                                "id": "A1_L18",
                                "question": "What time does the Botanical Garden open?",
                                "options": ["A. 7:00 AM", "B. 8:00 AM", "C. 9:00 AM", "D. 10:00 AM"],
                                "correct": "B. 8:00 AM",
                                "explanation": "Audio: 'open from 8:00 AM to 6:00 PM daily'."
                            },
                            {
                                "id": "A1_L19",
                                "question": "What are visitors asked NOT to do?",
                                "options": ["A. Take photographs", "B. Pick flowers or feed wild birds", "C. Walk on grass", "D. Drink water"],
                                "correct": "B. Pick flowers or feed wild birds",
                                "explanation": "Audio: 'Please remember not to pick flowers or feed the wild birds'."
                            },
                            {
                                "id": "A1_L20",
                                "question": "Where are bicycles allowed?",
                                "options": ["A. Everywhere", "B. On the main paved paths only", "C. Inside the cafe", "D. Near the flower beds"],
                                "correct": "B. On the main paved paths only",
                                "explanation": "Audio: 'Bicycles are allowed on the main paved paths only'."
                            }
                        ]
                    }
                ]
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 2. KỸ NĂNG ĐỌC & NGÔN NGỮ (READING & LANGUAGE USE) – 30 CÂU – 35 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "reading": {
        "title": "Kỹ Năng Đọc & Ngôn Ngữ – CEFR A1 (Reading & Language Use)",
        "total_questions": 30,
        "time_min": 35,
        "instructions": "Phần thi Đọc A1 gồm 4 phần (Part 1 - Part 4) với 30 câu hỏi trắc nghiệm kiểm tra biển báo, từ vựng, ngữ pháp và đọc hiểu cơ bản.",
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Biển Báo & Thông Báo Ngắn (6 câu)",
                "description": "Đọc biển báo hoặc tin nhắn ngắn và chọn ý nghĩa đúng nhất.",
                "questions": [
                    {
                        "id": "A1_R1",
                        "question": "Notice: 'PLEASE KEEP OFF THE GRASS'\nWhat does this sign mean?",
                        "options": ["A. You can sit on the grass", "B. Do not walk on the grass", "C. You must cut the grass", "D. Plant new flowers here"],
                        "correct": "B. Do not walk on the grass",
                        "explanation": "'Keep off the grass' nghĩa là không được giẫm lên cỏ."
                    },
                    {
                        "id": "A1_R2",
                        "question": "Sign on a shop door: 'OPEN MONDAY - SATURDAY 9 AM - 8 PM'\nWhen is the shop closed?",
                        "options": ["A. Monday morning", "B. Saturday evening", "C. Sunday", "D. Friday afternoon"],
                        "correct": "C. Sunday",
                        "explanation": "Cửa hàng mở từ thứ Hai đến thứ Bảy, nên Chủ Nhật (Sunday) sẽ đóng cửa."
                    },
                    {
                        "id": "A1_R3",
                        "question": "Message: 'David, your doctor appointment has been moved to Thursday at 3 PM. Call 555-1234 to confirm.'\nWhat should David do?",
                        "options": ["A. Go to the clinic on Wednesday", "B. Call the number to confirm his new appointment time", "C. Find a new doctor", "D. Cancel his medicine order"],
                        "correct": "B. Call the number to confirm his new appointment time",
                        "explanation": "Lời nhắn yêu cầu: 'Call 555-1234 to confirm'."
                    },
                    {
                        "id": "A1_R4",
                        "question": "Library sign: 'SILENCE PLEASE - NO FOOD OR DRINKS IN THIS AREA'\nWhat is allowed in this room?",
                        "options": ["A. Eating sandwiches", "B. Drinking coffee", "C. Reading quietly", "D. Talking loudly on phones"],
                        "correct": "C. Reading quietly",
                        "explanation": "Khu vực yêu cầu yên lặng (silence) và cấm đồ ăn thức uống, chỉ được đọc sách yên tĩnh."
                    },
                    {
                        "id": "A1_R5",
                        "question": "Notice on bus: 'SEATS RESERVED FOR ELDERLY AND PREGNANT PASSENGERS'\nWho should sit in these seats?",
                        "options": ["A. Healthy young students", "B. Older people and pregnant women", "C. Bus drivers only", "D. Children under 5 only"],
                        "correct": "B. Older people and pregnant women",
                        "explanation": "'Elderly' là người cao tuổi, 'pregnant passengers' là hành khách mang thai."
                    },
                    {
                        "id": "A1_R6",
                        "question": "Email subject: 'Class cancellation'\nText: 'Dear class, there is no Spanish lesson tonight because Teacher Maria is ill.'\nWhy is the class cancelled?",
                        "options": ["A. The school is on holiday", "B. The teacher is sick", "C. The classroom is dirty", "D. No students registered"],
                        "correct": "B. The teacher is sick",
                        "explanation": "'Teacher Maria is ill' nghĩa là giáo viên bị ốm."
                    }
                ]
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Hoàn Thành Câu Ngữ Pháp & Từ Vựng (8 câu)",
                "description": "Chọn từ hoặc cụm từ thích hợp nhất để hoàn thành câu.",
                "questions": [
                    {
                        "id": "A1_R7",
                        "question": "My sister _______ an English teacher at a high school.",
                        "options": ["A. am", "B. is", "C. are", "D. be"],
                        "correct": "B. is",
                        "explanation": "Chủ ngữ ngôi thứ ba số ít 'My sister' đi với động từ to be 'is'."
                    },
                    {
                        "id": "A1_R8",
                        "question": "They _______ to the cinema every Saturday evening.",
                        "options": ["A. goes", "B. go", "C. going", "D. wented"],
                        "correct": "B. go",
                        "explanation": "Hiện tại đơn với chủ ngữ số nhiều 'They' dùng động từ nguyên mẫu 'go'."
                    },
                    {
                        "id": "A1_R9",
                        "question": "There _______ three apples and one orange on the kitchen table.",
                        "options": ["A. is", "B. are", "C. have", "D. has"],
                        "correct": "B. are",
                        "explanation": "'Three apples' là danh từ số nhiều nên dùng cấu trúc 'There are'."
                    },
                    {
                        "id": "A1_R10",
                        "question": "I don't have _______ milk left in the fridge.",
                        "options": ["A. some", "B. any", "C. many", "D. a"],
                        "correct": "B. any",
                        "explanation": "Trong câu phủ định (don't have) với danh từ không đếm được 'milk', ta dùng 'any'."
                    },
                    {
                        "id": "A1_R11",
                        "question": "Can you please pass me _______ pen over there?",
                        "options": ["A. this", "B. that", "C. these", "D. those"],
                        "correct": "B. that",
                        "explanation": "'over there' chỉ vật ở xa, danh từ số ít 'pen' nên dùng đại từ chỉ định 'that'."
                    },
                    {
                        "id": "A1_R12",
                        "question": "What time _______ you usually wake up on weekdays?",
                        "options": ["A. do", "B. does", "C. are", "D. is"],
                        "correct": "A. do",
                        "explanation": "Câu hỏi thì hiện tại đơn với chủ ngữ 'you' mượn trợ động từ 'do'."
                    },
                    {
                        "id": "A1_R13",
                        "question": "She enjoys _______ books in the local public library.",
                        "options": ["A. read", "B. to read", "C. reading", "D. reads"],
                        "correct": "C. reading",
                        "explanation": "Sau động từ 'enjoy' ta dùng V-ing ('reading')."
                    },
                    {
                        "id": "A1_R14",
                        "question": "My birthday is _______ October 15th.",
                        "options": ["A. at", "B. on", "C. in", "D. of"],
                        "correct": "B. on",
                        "explanation": "Với ngày tháng cụ thể (October 15th), ta dùng giới từ 'on'."
                    }
                ]
            },
            {
                "part_id": 3,
                "part_title": "Part 3: Điền Từ Đoạn Văn Ngắn (8 câu)",
                "description": "Đọc đoạn văn và chọn đáp án thích hợp cho mỗi chỗ trống (Câu 15 - 22).",
                "passage_context": "My name is Lucas. I live in a small (15)_______ in Manchester with my parents and my younger brother. Every morning, I get up at 6:30 AM and have a healthy (16)_______ with bread, eggs, and milk. I usually (17)_______ my bicycle to school because it is only two kilometers away. At school, my favorite subject is (18)_______ because I love learning foreign languages and speaking with international friends. After classes finish at 4:00 PM, I often play (19)_______ with my classmates in the school yard. In the evening, I do my (20)_______ before dinner. We always have dinner together at 7:30 PM and talk about our day. At the weekend, our family likes going to the (21)_______ to swim and enjoy the fresh air. I (22)_______ very happy with my daily life.",
                "questions": [
                    {
                        "id": "A1_R15",
                        "question": "Choose the best word for blank (15):",
                        "options": ["A. house", "B. cloud", "C. water", "D. road"],
                        "correct": "A. house",
                        "explanation": "'live in a small house' nghĩa là sống trong một ngôi nhà nhỏ."
                    },
                    {
                        "id": "A1_R16",
                        "question": "Choose the best word for blank (16):",
                        "options": ["A. dinner", "B. breakfast", "C. midnight", "D. dessert"],
                        "correct": "B. breakfast",
                        "explanation": "Vào buổi sáng (morning), bữa ăn là bữa sáng ('breakfast')."
                    },
                    {
                        "id": "A1_R17",
                        "question": "Choose the best word for blank (17):",
                        "options": ["A. drive", "B. ride", "C. fly", "D. sail"],
                        "correct": "B. ride",
                        "explanation": "Đi xe đạp dùng động từ 'ride my bicycle'."
                    },
                    {
                        "id": "A1_R18",
                        "question": "Choose the best word for blank (18):",
                        "options": ["A. English", "B. Mathematics", "C. Physics", "D. Chemistry"],
                        "correct": "A. English",
                        "explanation": "Phía sau giải thích 'love learning foreign languages' (ngoại ngữ) nên môn học là English."
                    },
                    {
                        "id": "A1_R19",
                        "question": "Choose the best word for blank (19):",
                        "options": ["A. piano", "B. football", "C. computer", "D. homework"],
                        "correct": "B. football",
                        "explanation": "Chơi thể thao ở sân trường dùng 'play football' (chơi bóng đá)."
                    },
                    {
                        "id": "A1_R20",
                        "question": "Choose the best word for blank (20):",
                        "options": ["A. homework", "B. breakfast", "C. uniform", "D. shopping"],
                        "correct": "A. homework",
                        "explanation": "Làm bài tập về nhà vào buổi tối dùng 'do my homework'."
                    },
                    {
                        "id": "A1_R21",
                        "question": "Choose the best word for blank (21):",
                        "options": ["A. cinema", "B. beach", "C. kitchen", "D. classroom"],
                        "correct": "B. beach",
                        "explanation": "Đi bơi (swim) và tận hưởng không khí trong lành ở bãi biển ('beach')."
                    },
                    {
                        "id": "A1_R22",
                        "question": "Choose the best word for blank (22):",
                        "options": ["A. am", "B. is", "C. are", "D. feel"],
                        "correct": "D. feel",
                        "explanation": "'I feel very happy' (Tôi cảm thấy rất hạnh phúc)."
                    }
                ]
            },
            {
                "part_id": 4,
                "part_title": "Part 4: Đọc Hiểu 2 Đoạn Văn Đời Sống (8 câu)",
                "description": "Đọc 2 bài đọc ngắn và trả lời các câu hỏi đọc hiểu (Câu 23 - 30).",
                "passages": [
                    {
                        "passage_id": "a1-p1",
                        "title": "Passage 1: A Wonderful Weekend in the Countryside",
                        "content": "Last weekend, Emma and her family visited her grandparents in a small peaceful village. Her grandparents live on a fruit farm with many apple and orange trees. On Saturday morning, Emma helped her grandfather collect fresh eggs from the chicken coop and water the vegetable garden. In the afternoon, her grandmother baked a delicious apple pie. Emma and her brother rode their bicycles along the river and flew kites in the open field. They returned home to London on Sunday evening feeling refreshed and happy.",
                        "questions": [
                            {
                                "id": "A1_R23",
                                "question": "Where do Emma's grandparents live?",
                                "options": ["A. In the center of London", "B. On a fruit farm in a small village", "C. Near a big shopping mall", "D. In an apartment building"],
                                "correct": "B. On a fruit farm in a small village",
                                "explanation": "Đoạn văn: 'Her grandparents live on a fruit farm with many apple and orange trees'."
                            },
                            {
                                "id": "A1_R24",
                                "question": "What did Emma do on Saturday morning?",
                                "options": ["A. Went to the cinema", "B. Collected fresh eggs and watered vegetables", "C. Cleaned the kitchen", "D. Studied for exams"],
                                "correct": "B. Collected fresh eggs and watered vegetables",
                                "explanation": "Đoạn văn: 'Emma helped her grandfather collect fresh eggs... and water the vegetable garden'."
                            },
                            {
                                "id": "A1_R25",
                                "question": "What dessert did the grandmother make?",
                                "options": ["A. Chocolate cake", "B. Apple pie", "C. Strawberry ice cream", "D. Banana pudding"],
                                "correct": "B. Apple pie",
                                "explanation": "Đoạn văn: 'her grandmother baked a delicious apple pie'."
                            },
                            {
                                "id": "A1_R26",
                                "question": "When did Emma and her family go back to London?",
                                "options": ["A. Friday morning", "B. Saturday night", "C. Sunday evening", "D. Monday afternoon"],
                                "correct": "C. Sunday evening",
                                "explanation": "Đoạn văn: 'They returned home to London on Sunday evening'."
                            }
                        ]
                    },
                    {
                        "passage_id": "a1-p2",
                        "title": "Passage 2: Learning to Cook Simple Meals",
                        "content": "Cooking at home is an easy and fun skill for teenagers to learn. David is a 14-year-old student from Chicago. Every Sunday, he cooks a simple dinner for his parents. He often makes pasta with tomato sauce or grilled cheese sandwiches with vegetable soup. He buys fresh ingredients from the local supermarket every Saturday morning. David says cooking helps him save pocket money and understand the importance of healthy nutrition.",
                        "questions": [
                            {
                                "id": "A1_R27",
                                "question": "How old is David?",
                                "options": ["A. 12 years old", "B. 14 years old", "C. 16 years old", "D. 18 years old"],
                                "correct": "B. 14 years old",
                                "explanation": "Đoạn văn: 'David is a 14-year-old student from Chicago'."
                            },
                            {
                                "id": "A1_R28",
                                "question": "On which day does David cook dinner for his parents?",
                                "options": ["A. Friday", "B. Saturday", "C. Sunday", "D. Wednesday"],
                                "correct": "C. Sunday",
                                "explanation": "Đoạn văn: 'Every Sunday, he cooks a simple dinner for his parents'."
                            },
                            {
                                "id": "A1_R29",
                                "question": "What is one of the meals David often makes?",
                                "options": ["A. Sushi and noodles", "B. Pasta with tomato sauce", "C. Beef steak and fries", "D. Fried chicken wings"],
                                "correct": "B. Pasta with tomato sauce",
                                "explanation": "Đoạn văn: 'He often makes pasta with tomato sauce'."
                            },
                            {
                                "id": "A1_R30",
                                "question": "According to David, what is a benefit of cooking at home?",
                                "options": ["A. Saving money and learning healthy nutrition", "B. Becoming famous online", "C. Getting free groceries", "D. Skipping school homework"],
                                "correct": "A. Saving money and learning healthy nutrition",
                                "explanation": "Đoạn văn: 'cooking helps him save pocket money and understand the importance of healthy nutrition'."
                            }
                        ]
                    }
                ]
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 3. KỸ NĂNG VIẾT (WRITING) – 2 TASKS – 25 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "writing": {
        "title": "Kỹ Năng Viết – CEFR A1 (Writing Assessment)",
        "time_min": 25,
        "tasks": [
            {
                "task_id": "A1_W1",
                "task_title": "Task 1: Viết Tin Nhắn Ngắn / Email Hẹn Gặp (30 - 50 từ)",
                "prompt": "You want to invite your friend Jack to play football this Saturday afternoon. Write a short message (30-50 words) to Jack.\nIn your message, you should:\n- Invite Jack to play football with you.\n- Say what time and where you will meet.\n- Tell him what he needs to bring.",
                "min_words": 30,
                "time_min": 10,
                "instructions": "Viết đoạn tin nhắn ngắn đáp ứng đủ 3 yêu cầu trên.",
                "sample_high_score_answer": "Hi Jack! Would you like to play football with me this Saturday? We can meet at 3:30 PM at the Central Sports Park. Please remember to bring your sports shoes and a bottle of water. See you there!",
                "rubric": {
                    "task_completion": "Trả lời đầy đủ 3 ý: lời mời, thời gian/địa điểm và đồ dùng cần mang.",
                    "vocabulary": "Sử dụng từ vựng A1 chính xác (football, meet, sports shoes, bottle of water).",
                    "grammar": "Câu đơn giản đúng cấu trúc (Would you like, We can meet, Please remember)."
                }
            },
            {
                "task_id": "A1_W2",
                "task_title": "Task 2: Đoạn Văn Ngắn Về Bản Thân Hoặc Sở Thích (50 - 80 từ)",
                "prompt": "Write a short paragraph (50-80 words) about your favorite hobby.\nIn your writing, explain:\n- What your favorite hobby is.\n- When and where you do it.\n- Why you enjoy this hobby.",
                "min_words": 50,
                "time_min": 15,
                "instructions": "Viết đoạn văn ngắn 50-80 từ mạch lạc, đúng chính tả và ngữ pháp.",
                "sample_high_score_answer": "My favorite hobby is reading books. I usually read English storybooks every evening in my bedroom before going to sleep. I also love visiting the public library on Sunday mornings. Reading helps me relax after school and learn many new interesting words. It is my favorite pastime because it expands my imagination.",
                "rubric": {
                    "task_completion": "Nêu rõ sở thích, thời gian/địa điểm và lý do yêu thích.",
                    "vocabulary": "Từ vựng diễn đạt sở thích và cảm xúc phong phú (favorite hobby, relax, learn new words).",
                    "coherence": "Sử dụng liên từ cơ bản (and, also, because)."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 4. KỸ NĂNG NÓI (SPEAKING) – 2 PARTS – 10 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "speaking": {
        "title": "Kỹ Năng Nói – CEFR A1 (Speaking Interview)",
        "time_min": 10,
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Phỏng Vấn Giới Thiệu Bản Thân & Gia Đình (3 - 4 phút)",
                "description": "Giám khảo hỏi các câu hỏi cá nhân cơ bản về tên, tuổi, quê quán, gia đình và trường học.",
                "questions": [
                    {
                        "id": "A1_S1",
                        "question": "What is your full name and where do you live?",
                        "audio_prompt": "Hello! Could you please tell me your full name and where you live?",
                        "sample_answer": "My name is Nguyen Van Minh. I live in Hanoi, the capital city of Vietnam."
                    },
                    {
                        "id": "A1_S2",
                        "question": "Can you describe your family?",
                        "audio_prompt": "Tell me about your family. How many people are there?",
                        "sample_answer": "There are four people in my family: my father, my mother, my younger sister, and me. We love spending time together on weekends."
                    },
                    {
                        "id": "A1_S3",
                        "question": "What do you like doing in your free time?",
                        "audio_prompt": "What hobbies or activities do you enjoy in your free time?",
                        "sample_answer": "In my free time, I like listening to music and playing badminton with my classmates."
                    }
                ]
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Hỏi Đáp & Miêu Tả Chủ Đề Quen Thuộc (5 - 6 phút)",
                "description": "Thí sinh nhìn thông tin hoặc chủ đề quen thuộc (kỳ nghỉ, thời khóa biểu, bữa ăn yêu thích) và trả lời các câu hỏi mở rộng.",
                "questions": [
                    {
                        "id": "A1_S4",
                        "topic": "Daily Routine & School",
                        "question": "Describe your typical school day from morning to evening.",
                        "audio_prompt": "Please describe what you usually do on a typical school day.",
                        "sample_answer": "On a typical school day, I wake up at 6:30 AM, eat breakfast, and go to school by bicycle. I have classes from 7:30 AM to 11:30 AM. In the afternoon, I do homework and play sports. I have dinner with my family at 7:00 PM and go to bed at 10:30 PM."
                    },
                    {
                        "id": "A1_S5",
                        "topic": "Favorite Food & Drink",
                        "question": "What is your favorite food and drink, and why do you like it?",
                        "audio_prompt": "Tell me about your favorite food and drink. Why do you like them?",
                        "sample_answer": "My favorite food is Vietnamese Pho because it is very warm and delicious. My favorite drink is fresh orange juice because it is healthy and full of vitamin C."
                    }
                ]
            }
        ]
    }
}
