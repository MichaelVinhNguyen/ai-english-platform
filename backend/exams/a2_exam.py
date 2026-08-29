# -*- coding: utf-8 -*-
"""
backend/exams/a2_exam.py – Ngân Hàng Đề Thi Chuẩn Hóa CEFR A2 / Cambridge KET A2 / VSTEP Bậc 2
Format Khảo Thí Thực Tế:
1. Kỹ Năng Nghe (Listening): 25 câu hỏi – 30 phút (Part 1: 8 câu, Part 2: 8 câu, Part 3: 9 câu)
2. Kỹ Năng Đọc (Reading): 30 câu hỏi – 40 phút (Part 1: 6 câu, Part 2: 8 câu, Part 3: 8 câu, Part 4: 8 câu)
3. Kỹ Năng Viết (Writing): 2 Tasks – 35 phút (Task 1: Email 60-80 từ, Task 2: Short Story 80-100 từ)
4. Kỹ Năng Nói (Speaking): 2 Parts – 12 phút (Part 1: Social Interview, Part 2: Picture & Situation Discussion)
"""

A2_STANDARDIZED_EXAM_DATA = {
    "exam_id": "a2-ket-vstep-cefr-2026-01",
    "title": "Đề Thi Chuẩn Hóa Tiếng Anh CEFR A2 / Cambridge KET A2 / VSTEP Bậc 2 Thực Chiến 2026",
    "level": "A2",
    "standard": "CEFR A2 Waystage / VSTEP Bậc 2 Format 2026",
    "total_time_min": 117,
    "pass_gpa": 6.0,

    # ══════════════════════════════════════════════════════════════════════════
    # 1. KỸ NĂNG NGHE (LISTENING) – 25 CÂU HỎI – 30 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "listening": {
        "title": "Kỹ Năng Nghe – CEFR A2 (Listening Comprehension)",
        "total_questions": 25,
        "time_min": 30,
        "instructions": "Đề thi Nghe A2 gồm 3 phần với 25 câu hỏi trắc nghiệm. Thí sinh lắng nghe và chọn một đáp án đúng nhất (A, B, C hoặc D).",
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Thông Báo Công Cộng & Tin Nhắn Thoại (8 câu)",
                "description": "Nghe 8 mẩu thông tin, tin nhắn thoại hoặc thông báo công cộng.",
                "audio_script": "This is Part 1 of the CEFR A2 Listening Test. You will hear eight short announcements. Choose the best answer from A, B, C, or D.",
                "questions": [
                    {
                        "id": "A2_L1",
                        "audio_text": "Good afternoon passengers. Flight BA308 to Paris is now ready for boarding at Gate B22. Please have your boarding pass and passport ready.",
                        "question": "Which gate should passengers for Paris go to?",
                        "options": ["A. Gate A12", "B. Gate B22", "C. Gate C14", "D. Gate D30"],
                        "correct": "B. Gate B22",
                        "explanation": "Audio thông báo: 'ready for boarding at Gate B22'."
                    },
                    {
                        "id": "A2_L2",
                        "audio_text": "Hi Kevin, this is Dr. Robert's dental surgery. We have an opening for your annual check-up this Friday at 11:15 AM. Please call back to confirm.",
                        "question": "What time is Kevin's check-up appointment offered for Friday?",
                        "options": ["A. 10:15 AM", "B. 11:15 AM", "C. 1:15 PM", "D. 11:45 AM"],
                        "correct": "B. 11:15 AM",
                        "explanation": "Audio: 'this Friday at 11:15 AM'."
                    },
                    {
                        "id": "A2_L3",
                        "audio_text": "Attention shoppers at City Mall. The underground car park will be closed at 9:00 PM tonight for maintenance. Please move your vehicles before that time.",
                        "question": "What will happen at 9:00 PM tonight at City Mall?",
                        "options": ["A. The entire mall will open", "B. The car park will close for maintenance", "C. A musical concert starts", "D. Free parking begins"],
                        "correct": "B. The car park will close for maintenance",
                        "explanation": "Audio: 'The underground car park will be closed at 9:00 PM tonight for maintenance'."
                    },
                    {
                        "id": "A2_L4",
                        "audio_text": "Hello Sarah, this is Mike from the IT department. Your new company laptop is ready for collection at Room 302 on the third floor.",
                        "question": "Where should Sarah collect her new laptop?",
                        "options": ["A. Room 102", "B. Room 203", "C. Room 302", "D. Room 402"],
                        "correct": "C. Room 302",
                        "explanation": "Audio: 'ready for collection at Room 302 on the third floor'."
                    },
                    {
                        "id": "A2_L5",
                        "audio_text": "Weather forecast for tomorrow: heavy rainfall with strong winds in coastal areas. Temperatures will drop significantly to around 12 degrees Celsius.",
                        "question": "What will the temperature be tomorrow?",
                        "options": ["A. 20 degrees Celsius", "B. 16 degrees Celsius", "C. 12 degrees Celsius", "D. 8 degrees Celsius"],
                        "correct": "C. 12 degrees Celsius",
                        "explanation": "Audio: 'temperatures will drop significantly to around 12 degrees Celsius'."
                    },
                    {
                        "id": "A2_L6",
                        "audio_text": "The sports center will host a free yoga workshop this Sunday morning from 9:00 AM to 10:30 AM. Participants should bring their own yoga mats.",
                        "question": "What must participants bring to the yoga workshop?",
                        "options": ["A. Running shoes", "B. A yoga mat", "C. A tennis racket", "D. A swimming costume"],
                        "correct": "B. A yoga mat",
                        "explanation": "Audio: 'Participants should bring their own yoga mats'."
                    },
                    {
                        "id": "A2_L7",
                        "audio_text": "Dear train passengers, due to mechanical problems on the line, the express train to Edinburgh will be delayed by 25 minutes.",
                        "question": "Why is the train to Edinburgh delayed?",
                        "options": ["A. Bad weather", "B. Mechanical problems", "C. Staff strike", "D. Missing driver"],
                        "correct": "B. Mechanical problems",
                        "explanation": "Audio: 'due to mechanical problems on the line'."
                    },
                    {
                        "id": "A2_L8",
                        "audio_text": "Central Art Museum announcement: Admission is half-price for university students every Wednesday afternoon after 2:00 PM.",
                        "question": "When can university students get half-price admission?",
                        "options": ["A. Monday morning", "B. Wednesday afternoon after 2:00 PM", "C. Saturday all day", "D. Friday evening"],
                        "correct": "B. Wednesday afternoon after 2:00 PM",
                        "explanation": "Audio: 'half-price for university students every Wednesday afternoon after 2:00 PM'."
                    }
                ]
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Hội Thoại Thường Nhật & Dịch Vụ (8 câu)",
                "description": "Nghe 2 đoạn hội thoại (mỗi đoạn 4 câu) về đặt dịch vụ, công việc và học tập.",
                "audio_script": "This is Part 2. You will hear two conversations. For each question, choose the best answer.",
                "conversations": [
                    {
                        "conv_id": "a2-conv-1",
                        "context": "Hội thoại 1 (Câu 9 - 12): Đặt phòng và dịch vụ tại khách sạn.",
                        "audio_text": "Receptionist: Good morning, Grand View Hotel. How may I help you?\nGuest: Hello, I would like to book a double room for three nights starting next Thursday, June 18th.\nReceptionist: Certainly, sir. We have a deluxe room with a sea view for $120 per night, including buffet breakfast and free Wi-Fi.\nGuest: Does the room have an air conditioner and an electric kettle?\nReceptionist: Yes, all deluxe rooms are equipped with modern air conditioning, a kettle, and a mini fridge.\nGuest: Great, I will book that room. Can I pay by credit card upon arrival?\nReceptionist: Yes, you can pay when checking in at our front desk.",
                        "questions": [
                            {
                                "id": "A2_L9",
                                "question": "For how many nights does the guest want to book a room?",
                                "options": ["A. Two nights", "B. Three nights", "C. Four nights", "D. Five nights"],
                                "correct": "B. Three nights",
                                "explanation": "Khách nói: 'book a double room for three nights'."
                            },
                            {
                                "id": "A2_L10",
                                "question": "What is the room price per night?",
                                "options": ["A. $90", "B. $100", "C. $120", "D. $150"],
                                "correct": "C. $120",
                                "explanation": "Lễ tân: 'for $120 per night, including buffet breakfast'."
                            },
                            {
                                "id": "A2_L11",
                                "question": "What is included for free with the room?",
                                "options": ["A. Airport shuttle", "B. Buffet breakfast and free Wi-Fi", "C. Spa voucher", "D. Laundry service"],
                                "correct": "B. Buffet breakfast and free Wi-Fi",
                                "explanation": "Lễ tân: 'including buffet breakfast and free Wi-Fi'."
                            },
                            {
                                "id": "A2_L12",
                                "question": "When will the guest pay for the room?",
                                "options": ["A. Immediately by bank transfer", "B. When checking in at the front desk", "C. After checking out", "D. In cash before arrival"],
                                "correct": "B. When checking in at the front desk",
                                "explanation": "Lễ tân: 'you can pay when checking in at our front desk'."
                            }
                        ]
                    },
                    {
                        "conv_id": "a2-conv-2",
                        "context": "Hội thoại 2 (Câu 13 - 16): Thảo luận về dự án học tập nhóm.",
                        "audio_text": "Oliver: Hi Maya, have you started working on our environmental science presentation?\nMaya: Yes, Oliver. I researched the causes of plastic pollution in rivers, but I need some help creating the PowerPoint slides.\nOliver: I can design the slides and find high-resolution charts. Should we practice our speech on Tuesday afternoon?\nMaya: Tuesday sounds good, but I have a math test until 3:00 PM. Can we meet at the library at 3:30 PM?\nOliver: 3:30 PM is perfect. Let's aim to keep the presentation under 10 minutes.",
                        "questions": [
                            {
                                "id": "A2_L13",
                                "question": "What is the topic of Oliver and Maya's presentation?",
                                "options": ["A. Space exploration", "B. Plastic pollution in rivers", "C. Ancient history", "D. Modern computer programming"],
                                "correct": "B. Plastic pollution in rivers",
                                "explanation": "Maya nói: 'I researched the causes of plastic pollution in rivers'."
                            },
                            {
                                "id": "A2_L14",
                                "question": "What task will Oliver handle?",
                                "options": ["A. Writing the conclusion only", "B. Designing PowerPoint slides and charts", "C. Printing flyers", "D. Recording an audio podcast"],
                                "correct": "B. Designing PowerPoint slides and charts",
                                "explanation": "Oliver: 'I can design the slides and find high-resolution charts'."
                            },
                            {
                                "id": "A2_L15",
                                "question": "What time will they meet at the library on Tuesday?",
                                "options": ["A. 2:00 PM", "B. 3:00 PM", "C. 3:30 PM", "D. 4:00 PM"],
                                "correct": "C. 3:30 PM",
                                "explanation": "Maya đề xuất: 'Can we meet at the library at 3:30 PM?' và Oliver đồng ý."
                            },
                            {
                                "id": "A2_L16",
                                "question": "How long should their presentation be?",
                                "options": ["A. Under 5 minutes", "B. Under 10 minutes", "C. Exactly 15 minutes", "D. 20 minutes"],
                                "correct": "B. Under 10 minutes",
                                "explanation": "Oliver: 'Let's aim to keep the presentation under 10 minutes'."
                            }
                        ]
                    }
                ]
            },
            {
                "part_id": 3,
                "part_title": "Part 3: Bài Thuyết Trình & Hướng Dẫn Tham Quan (9 câu)",
                "description": "Nghe 2 bài giới thiệu/thuyết trình ngắn (bài 1: 5 câu, bài 2: 4 câu) và chọn đáp án chính xác.",
                "audio_script": "This is Part 3. You will hear two short presentations. Choose the best answer for each question.",
                "talks": [
                    {
                        "talk_id": "a2-talk-1",
                        "context": "Bài nói 1 (Câu 17 - 21): Giới thiệu về Hội Chợ Khoa Học Học Đường.",
                        "audio_text": "Good morning students! We are delighted to announce our Annual School Science Fair, taking place on Saturday, October 24th in the main school hall. Over 50 student teams will showcase innovative projects in green energy, robotics, and biology. The fair opens at 8:30 AM with an opening speech by Professor Henderson from City University. Visitors can vote for the 'Best Student Innovation Award' until 2:00 PM. The award ceremony will be held at 3:30 PM, and the top three winning teams will receive modern electronic tablets and certificates.",
                        "questions": [
                            {
                                "id": "A2_L17",
                                "question": "On what date will the Science Fair take place?",
                                "options": ["A. October 14th", "B. October 20th", "C. October 24th", "D. November 4th"],
                                "correct": "C. October 24th",
                                "explanation": "Audio: 'taking place on Saturday, October 24th'."
                            },
                            {
                                "id": "A2_L18",
                                "question": "Where will the fair be hosted?",
                                "options": ["A. The school football stadium", "B. The main school hall", "C. The computer lab", "D. The university campus"],
                                "correct": "B. The main school hall",
                                "explanation": "Audio: 'in the main school hall'."
                            },
                            {
                                "id": "A2_L19",
                                "question": "Who will deliver the opening speech at 8:30 AM?",
                                "options": ["A. The school principal", "B. Professor Henderson from City University", "C. The student council president", "D. A local scientist"],
                                "correct": "B. Professor Henderson from City University",
                                "explanation": "Audio: 'opening speech by Professor Henderson from City University'."
                            },
                            {
                                "id": "A2_L20",
                                "question": "Until what time can visitors vote for student awards?",
                                "options": ["A. 11:30 AM", "B. 12:00 PM", "C. 2:00 PM", "D. 3:30 PM"],
                                "correct": "C. 2:00 PM",
                                "explanation": "Audio: 'vote for the Best Student Innovation Award until 2:00 PM'."
                            },
                            {
                                "id": "A2_L21",
                                "question": "What prize will the top three winning teams receive?",
                                "options": ["A. Cash prizes of $500", "B. Electronic tablets and certificates", "C. A trip to Paris", "D. New textbooks"],
                                "correct": "B. Electronic tablets and certificates",
                                "explanation": "Audio: 'winning teams will receive modern electronic tablets and certificates'."
                            }
                        ]
                    },
                    {
                        "talk_id": "a2-talk-2",
                        "context": "Bài nói 2 (Câu 22 - 25): Hướng dẫn tham quan Lâu Đài Cổ Riverside.",
                        "audio_text": "Welcome everyone to Riverside Historic Castle. Built in the 14th century, this castle was originally a royal fortress defending the northern river crossing. Today, you can explore the Grand Banquet Hall, the Armoury Museum, and the King's Private Chambers. Audio guides are available in five languages at the ticket counter. Please note that flash photography is prohibited inside the tapestries gallery to preserve historic artworks. The cafe in the castle courtyard serves hot refreshments and homemade cakes.",
                        "questions": [
                            {
                                "id": "A2_L22",
                                "question": "When was Riverside Castle originally built?",
                                "options": ["A. In the 12th century", "B. In the 14th century", "C. In the 16th century", "D. In the 18th century"],
                                "correct": "B. In the 14th century",
                                "explanation": "Audio: 'Built in the 14th century'."
                            },
                            {
                                "id": "A2_L23",
                                "question": "What was the castle's original purpose?",
                                "options": ["A. A commercial trading post", "B. A royal fortress defending the river crossing", "C. A religious monastery", "D. A public prison"],
                                "correct": "B. A royal fortress defending the river crossing",
                                "explanation": "Audio: 'originally a royal fortress defending the northern river crossing'."
                            },
                            {
                                "id": "A2_L24",
                                "question": "Why is flash photography prohibited in the tapestries gallery?",
                                "options": ["A. To prevent alarming visitors", "B. To preserve historic artworks", "C. To save museum electricity", "D. For copyright security"],
                                "correct": "B. To preserve historic artworks",
                                "explanation": "Audio: 'flash photography is prohibited... to preserve historic artworks'."
                            },
                            {
                                "id": "A2_L25",
                                "question": "Where can visitors find the cafe?",
                                "options": ["A. At the entrance gate", "B. In the castle courtyard", "C. On the roof tower", "D. Inside the armoury"],
                                "correct": "B. In the castle courtyard",
                                "explanation": "Audio: 'The cafe in the castle courtyard serves hot refreshments'."
                            }
                        ]
                    }
                ]
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 2. KỸ NĂNG ĐỌC (READING) – 30 CÂU HỎI – 40 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "reading": {
        "title": "Kỹ Năng Đọc – CEFR A2 (Reading Comprehension)",
        "total_questions": 30,
        "time_min": 40,
        "instructions": "Đề thi Đọc A2 gồm 4 phần với 30 câu hỏi trắc nghiệm kiểm tra biển báo, ghép cặp thông tin, đọc hiểu và điền từ đoạn văn.",
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Biển Báo & Thông Báo Công Việc/Học Tập (6 câu)",
                "description": "Đọc 6 biển báo, email hoặc thông báo ngắn và chọn phương án diễn giải chính xác.",
                "questions": [
                    {
                        "id": "A2_R1",
                        "question": "Notice in swimming pool: 'CHILDREN UNDER 12 MUST BE ACCOMPANIED BY AN ADULT AT ALL TIMES'\nWhat is required at the pool?",
                        "options": ["A. Children under 12 can swim alone", "B. An adult must stay with children under 12", "C. Adults are not allowed in the water", "D. Only children are permitted to swim"],
                        "correct": "B. An adult must stay with children under 12",
                        "explanation": "'Accompanied by an adult' có nghĩa là phải có người lớn đi kèm cùng."
                    },
                    {
                        "id": "A2_R2",
                        "question": "Store notice: 'BUY 1 GET 1 AT 50% DISCOUNT - THIS WEEKEND ONLY'\nWhat is true about this promotion?",
                        "options": ["A. All items are completely free", "B. The second item is half-price when you buy one", "C. The sale lasts for the entire month", "D. You can only buy one item per customer"],
                        "correct": "B. The second item is half-price when you buy one",
                        "explanation": "Mua 1 món thì món thứ 2 được giảm 50% (half-price)."
                    },
                    {
                        "id": "A2_R3",
                        "question": "Email extract: 'Dear team, please submit your travel expense receipts by 5 PM Friday to ensure reimbursement in this month's payroll.'\nWhat must employees do?",
                        "options": ["A. Book new flight tickets", "B. Send receipts before Friday evening to get their money back", "C. Cancel all business trips", "D. Pay company tax"],
                        "correct": "B. Send receipts before Friday evening to get their money back",
                        "explanation": "Nộp hóa đơn (receipts) trước 5 PM thứ Sáu để được hoàn tiền (reimbursement)."
                    },
                    {
                        "id": "A2_R4",
                        "question": "Sign at train station: 'PASSENGERS MUST STAND BEHIND THE YELLOW LINE UNTIL THE TRAIN COMES TO A COMPLETE STOP'\nWhy should passengers stand behind the yellow line?",
                        "options": ["A. For safety while waiting for the train to stop", "B. Because the platform floor is wet", "C. To wait for the ticket checker", "D. The train is fully booked"],
                        "correct": "A. For safety while waiting for the train to stop",
                        "explanation": "Đứng sau vạch vàng để đảm bảo an toàn cho tới khi tàu dừng hẳn."
                    },
                    {
                        "id": "A2_R5",
                        "question": "Text message: 'Hi Liam, the football pitch is flooded due to heavy rain. Our match is rescheduled to Sunday at 2 PM instead.'\nWhat happened to the football match?",
                        "options": ["A. It was moved to Sunday because of rain", "B. It was cancelled permanently", "C. Liam's team won by default", "D. It is moved to an indoor arena tonight"],
                        "correct": "A. It was moved to Sunday because of rain",
                        "explanation": "Sân ngập nước mưa nên trận đấu dời sang Chủ Nhật lúc 2 PM."
                    },
                    {
                        "id": "A2_R6",
                        "question": "Notice: 'PLEASE RETURN ALL BORROWED AUDIO-VISUAL EQUIPMENT TO THE IT DESK AFTER USE'\nWhat should you do with IT equipment?",
                        "options": ["A. Keep it in your locker", "B. Take it home for practice", "C. Bring it back to the IT desk when finished", "D. Leave it on the classroom table"],
                        "correct": "C. Bring it back to the IT desk when finished",
                        "explanation": "'Return... after use' có nghĩa là trả lại bàn IT sau khi dùng xong."
                    }
                ]
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Ghép Nối Nhu Cầu & Dịch Vụ Phù Hợp (8 câu)",
                "description": "Đọc 8 mô tả nhu cầu và chọn dịch vụ / khóa học / địa điểm tương ứng chính xác nhất.",
                "questions": [
                    {
                        "id": "A2_R7",
                        "question": "Claire wants an evening fitness class that focuses on stretching, gentle music, and stress relief.\nWhich class is best for Claire?",
                        "options": ["A. Advanced Boxing & Kickboxing", "B. Relaxing Evening Hatha Yoga", "C. High-Intensity Interval Training", "D. Competitive Marathon Running"],
                        "correct": "B. Relaxing Evening Hatha Yoga",
                        "explanation": "Lớp Yoga nhẹ nhàng buổi tối phù hợp nhất với nhu cầu giãn cơ và xả stress."
                    },
                    {
                        "id": "A2_R8",
                        "question": "James wants to learn how to prepare authentic Italian pasta from an experienced native chef on weekends.\nWhich cooking course should James choose?",
                        "options": ["A. Fast Food Burger Workshop", "B. Weekend Traditional Italian Pasta Masterclass", "C. Japanese Sushi & Sashimi Course", "D. French Bakery & Pastry Course"],
                        "correct": "B. Weekend Traditional Italian Pasta Masterclass",
                        "explanation": "Khóa học làm mỳ Ý truyền thống cuối tuần khớp hoàn toàn với mong muốn của James."
                    },
                    {
                        "id": "A2_R9",
                        "question": "Sophie needs to rent a quiet meeting room for 6 people with high-speed internet and a projector for 3 hours.\nWhich workspace option is suitable?",
                        "options": ["A. Open Coffee Shop Table", "B. Private Executive Meeting Room Suite", "C. Public Library Reading Hall", "D. Outdoor Garden Gazebo"],
                        "correct": "B. Private Executive Meeting Room Suite",
                        "explanation": "Phòng họp riêng tư có máy chiếu và internet tốc độ cao là lựa chọn đúng."
                    },
                    {
                        "id": "A2_R10",
                        "question": "Ben loves outdoor adventures and wants to spend Saturday mountain biking in nature trails with equipment rental included.\nWhich tour package matches Ben's plan?",
                        "options": ["A. Museum Heritage Walking Tour", "B. Mountain Biking Trail Adventure Package", "C. Indoor Swimming Competition", "D. City Bus Sightseeing Pass"],
                        "correct": "B. Mountain Biking Trail Adventure Package",
                        "explanation": "Gói trải nghiệm xe đạp leo núi địa hình thiên nhiên."
                    },
                    {
                        "id": "A2_R11",
                        "question": "Emily wants to adopt a friendly small dog that gets along well with young children and doesn't require a large yard.\nWhich pet profile is ideal for Emily?",
                        "options": ["A. Large Guard Dog (needs big farm)", "B. Gentle Pug Puppy (loves kids, apartment friendly)", "C. Aggressive Hunting Hound", "D. Wild Exotic Parrot"],
                        "correct": "B. Gentle Pug Puppy (loves kids, apartment friendly)",
                        "explanation": "Chó nhỏ hiền lành, yêu trẻ em và phù hợp không gian nhỏ."
                    },
                    {
                        "id": "A2_R12",
                        "question": "Mark wants to study conversational Spanish for travel before his trip to Madrid next month.\nWhich program should he enroll in?",
                        "options": ["A. Academic Latin Literature", "B. Practical Spanish for Travellers Short Course", "C. Advanced Business German", "D. Ancient Greek Linguistics"],
                        "correct": "B. Practical Spanish for Travellers Short Course",
                        "explanation": "Khóa học tiếng Tây Ban Nha giao tiếp thực hành du lịch."
                    },
                    {
                        "id": "A2_R13",
                        "question": "Anna is looking for a weekend part-time job as a barista because she has previous cafe experience and loves coffee.\nWhich job opening fits Anna?",
                        "options": ["A. Night Shift Security Officer", "B. Weekend Coffee Barista at Artisan Roastery", "C. Construction Site Worker", "D. Primary School Mathematics Teacher"],
                        "correct": "B. Weekend Coffee Barista at Artisan Roastery",
                        "explanation": "Công việc Barista làm cuối tuần tại quán cà phê."
                    },
                    {
                        "id": "A2_R14",
                        "question": "Daniel wants to buy an eco-friendly lightweight laptop with long battery life for college lectures.\nWhich device should Daniel purchase?",
                        "options": ["A. Heavy 5kg Desktop PC", "B. Ultra-slim 1.1kg Laptop with 16-hour battery", "C. Old CRT Monitor", "D. Professional Sound Mixing Board"],
                        "correct": "B. Ultra-slim 1.1kg Laptop with 16-hour battery",
                        "explanation": "Laptop siêu nhẹ 1.1kg thời lượng pin 16 tiếng phục vụ việc học tập."
                    }
                ]
            },
            {
                "part_id": 3,
                "part_title": "Part 3: Đọc Hiểu 2 Đoạn Văn Về Lối Sống & Du Lịch Xanh (8 câu)",
                "description": "Đọc 2 bài đọc vừa và chọn câu trả lời chính xác (Câu 15 - 22).",
                "passages": [
                    {
                        "passage_id": "a2-p1",
                        "title": "Passage 1: The Rise of Urban Rooftop Gardening",
                        "content": "In many modern cities around the world, rooftop gardening is becoming extremely popular among apartment dwellers. With limited ground space, urban residents are transforming empty concrete roofs into vibrant green gardens filled with fresh vegetables, herbs, and flowers. Rooftop gardens not only provide families with clean organic produce such as tomatoes and lettuce, but they also help reduce building temperatures during hot summer months. Moreover, caring for plants after a busy workday offers an excellent way to reduce mental stress and foster strong neighborhood communities.",
                        "questions": [
                            {
                                "id": "A2_R15",
                                "question": "Why are rooftop gardens becoming popular in modern cities?",
                                "options": ["A. Because buildings have no roofs", "B. Because of limited ground space in urban areas", "C. Because vegetables are illegal in supermarkets", "D. Because cities are getting colder"],
                                "correct": "B. Because of limited ground space in urban areas",
                                "explanation": "Đoạn văn: 'With limited ground space, urban residents are transforming empty concrete roofs'."
                            },
                            {
                                "id": "A2_R16",
                                "question": "What types of organic vegetables are mentioned in the text?",
                                "options": ["A. Potatoes and corn", "B. Tomatoes and lettuce", "C. Carrots and pumpkins", "D. Mushrooms and onions"],
                                "correct": "B. Tomatoes and lettuce",
                                "explanation": "Đoạn văn: 'clean organic produce such as tomatoes and lettuce'."
                            },
                            {
                                "id": "A2_R17",
                                "question": "What environmental benefit do rooftop gardens provide to buildings in summer?",
                                "options": ["A. They increase building heating", "B. They help reduce building temperatures", "C. They block all sunlight", "D. They clean building windows"],
                                "correct": "B. They help reduce building temperatures",
                                "explanation": "Đoạn văn: 'help reduce building temperatures during hot summer months'."
                            },
                            {
                                "id": "A2_R18",
                                "question": "How does gardening help city residents mentally?",
                                "options": ["A. It makes them tired and stressed", "B. It helps reduce mental stress and connects neighbors", "C. It makes them buy expensive tools", "D. It causes arguments with neighbors"],
                                "correct": "B. It helps reduce mental stress and connects neighbors",
                                "explanation": "Đoạn văn: 'offers an excellent way to reduce mental stress and foster strong neighborhood communities'."
                            }
                        ]
                    },
                    {
                        "passage_id": "a2-p2",
                        "title": "Passage 2: Ecotourism and Sustainable Travel Habits",
                        "content": "Ecotourism is a responsible way of traveling that focuses on preserving natural environments and supporting local indigenous communities. When travelers choose sustainable tourism, they stay in eco-lodges powered by renewable solar energy, minimize single-use plastic consumption, and buy handmade crafts directly from local artisans. In countries like Costa Rica and New Zealand, ecotourism has created thousands of green jobs while protecting endangered wildlife species like sea turtles and rare forest birds. Responsible tourists understand that preserving nature ensures future generations can enjoy these natural wonders.",
                        "questions": [
                            {
                                "id": "A2_R19",
                                "question": "What is the main focus of ecotourism?",
                                "options": ["A. Building luxury shopping centers", "B. Preserving natural environments and supporting local communities", "C. Traveling as fast as possible", "D. Hunting wild animals"],
                                "correct": "B. Preserving natural environments and supporting local communities",
                                "explanation": "Đoạn văn: 'focuses on preserving natural environments and supporting local indigenous communities'."
                            },
                            {
                                "id": "A2_R20",
                                "question": "What kind of accommodation do eco-travelers typically choose?",
                                "options": ["A. Eco-lodges powered by solar energy", "B. Huge high-rise skyscraper hotels", "C. Luxury casino resorts", "D. Underground bunkers"],
                                "correct": "A. Eco-lodges powered by solar energy",
                                "explanation": "Đoạn văn: 'stay in eco-lodges powered by renewable solar energy'."
                            },
                            {
                                "id": "A2_R21",
                                "question": "Which two countries are mentioned as successful examples of ecotourism?",
                                "options": ["A. Canada and Norway", "B. Costa Rica and New Zealand", "C. Egypt and Greece", "D. Brazil and Germany"],
                                "correct": "B. Costa Rica and New Zealand",
                                "explanation": "Đoạn văn: 'In countries like Costa Rica and New Zealand'."
                            },
                            {
                                "id": "A2_R22",
                                "question": "What wildlife species has ecotourism helped protect according to the passage?",
                                "options": ["A. Polar bears and penguins", "B. Sea turtles and rare forest birds", "C. Tigers and African elephants", "D. Whales and sharks"],
                                "correct": "B. Sea turtles and rare forest birds",
                                "explanation": "Đoạn văn: 'protecting endangered wildlife species like sea turtles and rare forest birds'."
                            }
                        ]
                    }
                ]
            },
            {
                "part_id": 4,
                "part_title": "Part 4: Điền Từ Đoạn Văn Ngữ Pháp & Từ Vựng (8 câu)",
                "description": "Đọc đoạn văn và chọn đáp án chính xác cho mỗi chỗ trống (Câu 23 - 30).",
                "passage_context": "Learning a new language opens up (23)_______ exciting opportunities for personal and professional growth. When you speak English, you can easily communicate with people from (24)_______ different countries. Many students find that practicing for 20 minutes every day is much (25)_______ effective than studying for four hours once a week. Mobile applications and online podcasts make it simple to listen to authentic conversations (26)_______ commuting on the bus. In addition, reading English articles helps you expand your vocabulary (27)_______. If you make a mistake while speaking, you should not be (28)_______ because making mistakes is a natural part of learning. With patience and consistent effort, anyone (29)_______ achieve confidence and fluency in English. Start your learning journey today and see how your skills (30)_______ over time!",
                "questions": [
                    {
                        "id": "A2_R23",
                        "question": "Choose the best word for blank (23):",
                        "options": ["A. many", "B. much", "C. little", "D. every"],
                        "correct": "A. many",
                        "explanation": "'opportunities' là danh từ đếm được số nhiều nên dùng 'many'."
                    },
                    {
                        "id": "A2_R24",
                        "question": "Choose the best word for blank (24):",
                        "options": ["A. hundred", "B. hundreds of", "C. hundred of", "D. a hundred"],
                        "correct": "B. hundreds of",
                        "explanation": "Cụm từ chỉ số lượng phiếm định 'hundreds of different countries' (hàng trăm quốc gia)."
                    },
                    {
                        "id": "A2_R25",
                        "question": "Choose the best word for blank (25):",
                        "options": ["A. more", "B. most", "C. very", "D. as"],
                        "correct": "A. more",
                        "explanation": "So sánh hơn với tính từ dài 'effective' có 'than' phía sau là 'much more effective'."
                    },
                    {
                        "id": "A2_R26",
                        "question": "Choose the best word for blank (26):",
                        "options": ["A. while", "B. during", "C. because", "D. although"],
                        "correct": "A. while",
                        "explanation": "'while commuting' (trong khi đang di chuyển)."
                    },
                    {
                        "id": "A2_R27",
                        "question": "Choose the best word for blank (27):",
                        "options": ["A. quick", "B. quickly", "C. quicker", "D. quickest"],
                        "correct": "B. quickly",
                        "explanation": "Bổ nghĩa cho động từ 'expand' dùng phó từ 'quickly'."
                    },
                    {
                        "id": "A2_R28",
                        "question": "Choose the best word for blank (28):",
                        "options": ["A. afraid", "B. happy", "C. excited", "D. proud"],
                        "correct": "A. afraid",
                        "explanation": "'not be afraid' (không nên sợ hãi khi mắc lỗi)."
                    },
                    {
                        "id": "A2_R29",
                        "question": "Choose the best word for blank (29):",
                        "options": ["A. can", "B. must to", "C. should to", "D. ought"],
                        "correct": "A. can",
                        "explanation": "Động từ khuyết thiếu 'can' đi trực tiếp với động từ nguyên mẫu 'achieve'."
                    },
                    {
                        "id": "A2_R30",
                        "question": "Choose the best word for blank (30):",
                        "options": ["A. improve", "B. improves", "C. improved", "D. improving"],
                        "correct": "A. improve",
                        "explanation": "Chủ ngữ 'your skills' (số nhiều) đi với động từ hiện tại 'improve'."
                    }
                ]
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 3. KỸ NĂNG VIẾT (WRITING) – 2 TASKS – 35 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "writing": {
        "title": "Kỹ Năng Viết – CEFR A2 (Writing Assessment)",
        "time_min": 35,
        "tasks": [
            {
                "task_id": "A2_W1",
                "task_title": "Task 1: Viết Email Mời Bạn Tham Gia Sự Kiện (60 - 80 từ)",
                "prompt": "You are organizing a weekend barbecue party at your house next Sunday. Write an email (60-80 words) to your friend Alex.\nIn your email, you should:\n- Invite Alex to the barbecue party.\n- State the time, location, and planned activities.\n- Ask Alex if he can bring some music or games.",
                "min_words": 60,
                "time_min": 15,
                "instructions": "Viết email thân mật đúng văn phong, đáp ứng đủ 3 nội dung yêu cầu.",
                "sample_high_score_answer": "Hi Alex,\nI hope you are doing well. I am hosting a barbecue party at my house next Sunday, June 21st, and I would love for you to come! The party starts at 4:00 PM in our back garden. We will grill delicious sausages, make fresh burgers, and play board games together. Could you please bring your portable Bluetooth speaker so we can listen to some great music? Let me know if you can make it!\nBest regards,\nTom",
                "rubric": {
                    "task_completion": "Nêu đầy đủ lời mời, thời gian địa điểm (4 PM Sunday, back garden) và nhờ mang loa Bluetooth.",
                    "vocabulary": "Từ vựng tiệc nướng và sinh hoạt sinh động (barbecue party, grill sausages, board games, portable speaker).",
                    "grammar": "Sử dụng đúng thì hiện tại tiếp diễn chỉ tương lai và câu hỏi lịch sự (Could you please...)."
                }
            },
            {
                "task_id": "A2_W2",
                "task_title": "Task 2: Kể Về Một Chuyến Đi / Trải Nghiệm Đáng Nhớ (80 - 100 từ)",
                "prompt": "Write a short story (80-100 words) about a memorable trip you took with your friends or family.\nIn your story, describe:\n- Where you went and who you went with.\n- What exciting things you did during the trip.\n- Why this trip was so memorable to you.",
                "min_words": 80,
                "time_min": 20,
                "instructions": "Sử dụng thì quá khứ đơn (Past Simple) và các từ nối thời gian mạch lạc.",
                "sample_high_score_answer": "Last summer, my family took a memorable five-day holiday to Da Nang beach. We stayed at a lovely hotel near the coast. Every morning, we woke up early to watch the sunrise and swam in the cool ocean waves. On the third day, we explored the Marble Mountains and took beautiful photos of the ancient pagodas. In the evenings, we enjoyed delicious seafood at a local seaside restaurant. This trip was truly unforgettable because my family spent quality time together and created wonderful memories away from our busy daily schedules.",
                "rubric": {
                    "task_completion": "Mô tả đầy đủ địa điểm, người đi cùng, các hoạt động và cảm xúc ý nghĩa.",
                    "grammar": "Sử dụng thì quá khứ đơn chính xác (took, stayed, woke up, swam, explored, enjoyed).",
                    "cohesion": "Liên kết câu mạch lạc (Every morning, On the third day, In the evenings, because)."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 4. KỸ NĂNG NÓI (SPEAKING) – 2 PARTS – 12 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "speaking": {
        "title": "Kỹ Năng Nói – CEFR A2 (Speaking Interview)",
        "time_min": 12,
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Phỏng Vấn Xã Hội & Đời Sống Học Tập (4 - 5 phút)",
                "description": "Giám khảo trao đổi các chủ đề về công việc, trường lớp, thói quen sinh hoạt và sở thích cá nhân.",
                "questions": [
                    {
                        "id": "A2_S1",
                        "question": "Tell me about your favorite subject at school or your current job.",
                        "audio_prompt": "Could you please tell me about your favorite subject at school or your current job?",
                        "sample_answer": "My favorite subject is English because it allows me to connect with people worldwide. I enjoy learning grammar and practicing communication through songs and podcasts."
                    },
                    {
                        "id": "A2_S2",
                        "question": "What do you usually do on weekends to relax?",
                        "audio_prompt": "What do you usually do on weekends to relax and recharge?",
                        "sample_answer": "On weekends, I usually play football with my neighborhood friends on Saturday mornings, and on Sundays, I love reading books or cooking special dinners with my family."
                    },
                    {
                        "id": "A2_S3",
                        "question": "Describe a place in your hometown that you really enjoy visiting.",
                        "audio_prompt": "Tell me about a place in your hometown that you really enjoy visiting.",
                        "sample_answer": "In my hometown, I really love visiting West Lake. It is a huge freshwater lake where people can cycle, enjoy coffee at lakeside cafes, and watch the beautiful sunset."
                    }
                ]
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Thảo Luận Tình Huống & Đưa Ra Lời Khuyên (6 - 7 phút)",
                "description": "Thí sinh nhận một tình huống giả định (ví dụ: lên kế hoạch kỳ nghỉ, chọn quà sinh nhật cho bạn bè) và thảo luận các lựa chọn.",
                "questions": [
                    {
                        "id": "A2_S4",
                        "topic": "Holiday Planning with Friends",
                        "question": "Your friend wants to plan a 3-day weekend trip. Compare going to a beach resort versus a mountain camping site. Which do you recommend?",
                        "audio_prompt": "Your friend wants to plan a 3-day weekend trip. Would you recommend going to a beach resort or a mountain camping site, and why?",
                        "sample_answer": "Both options are great, but I would strongly recommend a beach resort. At the beach, we can swim, try watersports, and enjoy fresh seafood easily. In contrast, mountain camping requires a lot of heavy equipment and can be difficult if it rains unexpectedly. Therefore, a beach trip is much more relaxing and convenient for a short weekend."
                    },
                    {
                        "id": "A2_S5",
                        "topic": "Healthy Living Habits",
                        "question": "What advice would you give to a friend who wants to improve their physical health and energy levels?",
                        "audio_prompt": "What advice would you give to a friend who wants to improve their health and feel more energetic?",
                        "sample_answer": "I would advise my friend to drink at least two liters of water daily, exercise for 30 minutes like jogging or cycling, and ensure they get 7 to 8 hours of quality sleep every night. Also, reducing fast food and eating more fresh fruits and vegetables will make a big difference."
                    }
                ]
            }
        ]
    }
}
