"""
seed_b1_exam_data.py – Ngan hang de thi Tieng Anh B1 Chuan Hoa 4 Ky Nang Cap Nhat 2026
Format khao thi thuc te:
1. Ky nang Nghe (Listening): 35 cau hoi – 40 phut (Part 1: 8 cau, Part 2: 12 cau, Part 3: 15 cau)
2. Ky nang Doc (Reading): 40 cau hoi – 60 phut (4 Passages x 10 cau)
3. Ky nang Viet (Writing): 2 Tasks – 60 phut (Task 1: Email 120 tu, Task 2: Essay 250 tu)
4. Ky nang Noi (Speaking): 3 Parts – 12 phut (Part 1: Social, Part 2: Solution Discussion, Part 3: Topic Development)
"""

B1_STANDARDIZED_EXAM_DATA = {
    "exam_id": "b1-vstep-cefr-2026-01",
    "title": "Đề Thi Chuẩn Hóa Tiếng Anh CEFR B1 / VSTEP Bậc 3 Thực Chiến 2026",
    "level": "B1",
    "standard": "CEFR B1 / VSTEP Bậc 3 / Cambridge PET Format 2026",
    "total_time_min": 172, # 40 + 60 + 60 + 12
    "pass_gpa": 6.0, # Thang diem 10.0, dat tu 6.0 tro len la Dat chuan B1
    
    # ══════════════════════════════════════════════════════════════════════════
    # 1. KỸ NĂNG NGHE (LISTENING) – 35 CÂU HỎI – 40 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "listening": {
        "title": "Kỹ Năng Nghe (Listening Comprehension)",
        "total_questions": 35,
        "time_min": 40,
        "instructions": "Bài thi Nghe gồm 3 phần (Part 1, Part 2, Part 3) với 35 câu hỏi trắc nghiệm. Thí sinh được nghe audio và chọn một đáp án đúng nhất (A, B, C hoặc D).",
        "parts": [
            # ── PART 1: 8 CÂU THÔNG BÁO / HƯỚNG DẪN NGẮN (SHORT ANNOUNCEMENTS) ──
            {
                "part_id": 1,
                "part_title": "Part 1: Hướng Dẫn & Thông Báo Ngắn (8 câu)",
                "description": "Nghe 8 thông báo, hướng dẫn ngắn hoặc tin nhắn thoại và chọn câu trả lời đúng.",
                "audio_script": "This is Part 1. You will hear eight short announcements or instructions. For each question, choose the best answer from A, B, C, or D.",
                "questions": [
                    {
                        "id": "L1",
                        "audio_text": "Attention passengers on Flight VN248 to Da Nang. Due to adverse weather conditions at the destination airport, boarding has been delayed by 45 minutes. Please remain seated near Gate 12.",
                        "question": "Why is the flight to Da Nang delayed?",
                        "options": [
                            "A. Technical problems with the aircraft",
                            "B. Bad weather at the destination airport",
                            "C. The flight crew has not arrived",
                            "D. Gate 12 is under maintenance"
                        ],
                        "correct": "B. Bad weather at the destination airport",
                        "explanation": "Audio thông báo: 'Due to adverse weather conditions at the destination airport, boarding has been delayed by 45 minutes'."
                    },
                    {
                        "id": "L2",
                        "audio_text": "Good morning staff members. Please be reminded that the annual fire safety drill will take place tomorrow at 10:30 AM. When the alarm sounds, please use the emergency stairs, not the elevators.",
                        "question": "What are staff advised to do during the fire drill?",
                        "options": [
                            "A. Take the elevators to the lobby",
                            "B. Continue working at their desks",
                            "C. Use the emergency stairs",
                            "D. Call the fire department immediately"
                        ],
                        "correct": "C. Use the emergency stairs",
                        "explanation": "Audio nêu rõ: 'When the alarm sounds, please use the emergency stairs, not the elevators'."
                    },
                    {
                        "id": "L3",
                        "audio_text": "Thank you for calling City Central Library. We are open Monday through Friday from 8:00 AM to 8:00 PM, and on weekends from 9:00 AM to 5:00 PM. To renew your book loans, press 1.",
                        "question": "What time does the library close on Saturday?",
                        "options": [
                            "A. 8:00 AM",
                            "B. 8:00 PM",
                            "C. 5:00 PM",
                            "D. 9:00 AM"
                        ],
                        "correct": "C. 5:00 PM",
                        "explanation": "Audio nêu: 'and on weekends from 9:00 AM to 5:00 PM'. Thứ 7 thuộc weekend nên đóng cửa lúc 5:00 PM."
                    },
                    {
                        "id": "L4",
                        "audio_text": "Hello, this is Dr. Miller's dental clinic calling for Sarah Jenkins. We would like to confirm your teeth cleaning appointment tomorrow at 3:15 PM. Please bring your insurance card with you.",
                        "question": "What is Sarah asked to bring to her appointment?",
                        "options": [
                            "A. Her passport",
                            "B. Her insurance card",
                            "C. A medical receipt",
                            "D. Cash only"
                        ],
                        "correct": "B. Her insurance card",
                        "explanation": "Audio: 'Please bring your insurance card with you'."
                    },
                    {
                        "id": "L5",
                        "audio_text": "Attention shoppers! For the next two hours only, all summer clothing on the second floor is discounted by 40%. Don't miss this special seasonal clearance promotion!",
                        "question": "What item is on sale on the second floor?",
                        "options": [
                            "A. Electronics and home appliances",
                            "B. Winter coats and shoes",
                            "C. Summer clothing",
                            "D. Sports equipment"
                        ],
                        "correct": "C. Summer clothing",
                        "explanation": "Audio: 'all summer clothing on the second floor is discounted by 40%'."
                    },
                    {
                        "id": "L6",
                        "audio_text": "Welcome to Metro Transit. Train services on the Green Line are temporarily suspended between Central Station and University Park due to track maintenance. Shuttle buses are operating outside the main exit.",
                        "question": "How can passengers travel between Central Station and University Park?",
                        "options": [
                            "A. By taking the express train",
                            "B. By taking the replacement shuttle buses",
                            "C. By walking through the underground tunnel",
                            "D. By taking a river boat"
                        ],
                        "correct": "B. By taking the replacement shuttle buses",
                        "explanation": "Audio: 'Shuttle buses are operating outside the main exit'."
                    },
                    {
                        "id": "L7",
                        "audio_text": "Hi Mark, this is Linda from the project team. Our afternoon meeting has been moved from Conference Room A to Room C on the third floor because the projector in Room A is broken.",
                        "question": "Why was the meeting location changed?",
                        "options": [
                            "A. The projector in Room A is broken",
                            "B. Too many participants attended",
                            "C. Room C is larger",
                            "D. The third floor is quieter"
                        ],
                        "correct": "A. The projector in Room A is broken",
                        "explanation": "Audio: 'because the projector in Room A is broken'."
                    },
                    {
                        "id": "L8",
                        "audio_text": "Here is today's local weather forecast. Expect heavy rain and strong winds throughout the morning, but conditions will clear up by late afternoon with mild sunshine and temperatures around 24 degrees Celsius.",
                        "question": "What will the weather be like in the late afternoon?",
                        "options": [
                            "A. Heavy thunderstorms",
                            "B. Freezing cold with snow",
                            "C. Mild sunshine and clearer skies",
                            "D. Dense fog"
                        ],
                        "correct": "C. Mild sunshine and clearer skies",
                        "explanation": "Audio: 'conditions will clear up by late afternoon with mild sunshine'."
                    }
                ]
            },
            
            # ── PART 2: 12 CÂU HỘI THOẠI THỰC TẾ (3 CONVERSATIONS x 4 QUESTIONS) ──
            {
                "part_id": 2,
                "part_title": "Part 2: Đoạn Hội Thoại Đời Sống & Công Sở (12 câu)",
                "description": "Nghe 3 đoạn đối thoại. Mỗi đoạn có 4 câu hỏi trắc nghiệm.",
                "conversations": [
                    {
                        "conv_id": "conv-1",
                        "context": "Hội thoại 1 (Câu 9 - 12): Cuộc trò chuyện giữa hai đồng nghiệp về kế hoạch tổ chức sự kiện của công ty.",
                        "audio_text": "Woman: Hi David, have you finalized the venue for our annual company gala next month?\nMan: Almost, Emily. We looked at Grand Palace Hotel and Riverside Resort. The Riverside Resort offered a 20% discount on catering, but Grand Palace has a larger stage for the musical performance.\nWoman: I think having a good stage is essential because our CEO wants to present the awards properly. How about the transportation?\nMan: That's a good point. Grand Palace is located right next to the central subway station, so employees won't have trouble getting there after work.\nWoman: Great, let's book Grand Palace then. I will send out the formal invitations by Friday afternoon.",
                        "questions": [
                            {
                                "id": "L9",
                                "question": "What event are the speakers planning?",
                                "options": [
                                    "A. A new product launch",
                                    "B. An annual company gala and awards ceremony",
                                    "C. A weekend sports festival",
                                    "D. A training workshop"
                                ],
                                "correct": "B. An annual company gala and awards ceremony",
                                "explanation": "Người nữ hỏi: 'have you finalized the venue for our annual company gala next month?' và đề cập CEO trao giải thưởng."
                            },
                            {
                                "id": "L10",
                                "question": "What advantage did Riverside Resort offer?",
                                "options": [
                                    "A. Free parking for all guests",
                                    "B. A 20% discount on catering food and drinks",
                                    "C. A larger performance stage",
                                    "D. Closer proximity to the subway"
                                ],
                                "correct": "B. A 20% discount on catering food and drinks",
                                "explanation": "Người nam nói: 'The Riverside Resort offered a 20% discount on catering'."
                            },
                            {
                                "id": "L11",
                                "question": "Why did they finally choose Grand Palace Hotel?",
                                "options": [
                                    "A. It was much cheaper than other venues",
                                    "B. It has a larger stage and is convenient for subway transport",
                                    "C. The CEO personally owns the hotel",
                                    "D. It provides free musical equipment"
                                ],
                                "correct": "B. It has a larger stage and is convenient for subway transport",
                                "explanation": "Họ đồng ý chọn vì có 'larger stage' và 'located right next to the central subway station'."
                            },
                            {
                                "id": "L12",
                                "question": "What will Emily do by Friday afternoon?",
                                "options": [
                                    "A. Call Riverside Resort to cancel",
                                    "B. Send out formal invitations to employees",
                                    "C. Book the musical band",
                                    "D. Prepare the CEO's presentation speech"
                                ],
                                "correct": "B. Send out formal invitations to employees",
                                "explanation": "Emily nói: 'I will send out the formal invitations by Friday afternoon'."
                            }
                        ]
                    },
                    {
                        "conv_id": "conv-2",
                        "context": "Hội thoại 2 (Câu 13 - 16): Sinh viên hỏi giảng viên về bài tiểu luận cuối kỳ.",
                        "audio_text": "Student: Excuse me, Professor Adams. Could I ask you a few questions regarding our environmental science term paper?\nProfessor: Of course, Liam. Come on in. What seems to be the problem?\nStudent: I am researching renewable energy adoption in developing countries, but I am finding it difficult to gather reliable statistical data from recent years.\nProfessor: That is a common challenge. Have you checked the International Energy Agency database available through our university library portal?\nStudent: Not yet, I only searched on public academic search engines.\nProfessor: The university library gives you full access to peer-reviewed journals and global data. Also, remember that your paper should be between 2,500 and 3,000 words, due on December 15th.",
                        "questions": [
                            {
                                "id": "L13",
                                "question": "What is Liam's research topic for the term paper?",
                                "options": [
                                    "A. Marine biology conservation",
                                    "B. Renewable energy adoption in developing countries",
                                    "C. Nuclear power plant safety",
                                    "D. Urban waste management systems"
                                ],
                                "correct": "B. Renewable energy adoption in developing countries",
                                "explanation": "Sinh viên nói: 'I am researching renewable energy adoption in developing countries'."
                            },
                            {
                                "id": "L14",
                                "question": "What difficulty is Liam experiencing?",
                                "options": [
                                    "A. He cannot choose a thesis title",
                                    "B. He is finding it hard to find reliable recent statistical data",
                                    "C. His computer hard drive crashed",
                                    "D. He missed the midterm exam"
                                ],
                                "correct": "B. He is finding it hard to find reliable recent statistical data",
                                "explanation": "Liam chia sẻ: 'I am finding it difficult to gather reliable statistical data from recent years'."
                            },
                            {
                                "id": "L15",
                                "question": "What resource does Professor Adams recommend?",
                                "options": [
                                    "A. Wikipedia articles",
                                    "B. The International Energy Agency database via the library portal",
                                    "C. Interviewing local government officials",
                                    "D. Buying a commercial textbook"
                                ],
                                "correct": "B. The International Energy Agency database via the library portal",
                                "explanation": "Giáo sư khuyên: 'Have you checked the International Energy Agency database available through our university library portal?'."
                            },
                            {
                                "id": "L16",
                                "question": "What is the word limit requirement for Liam's term paper?",
                                "options": [
                                    "A. 1,000 to 1,500 words",
                                    "B. 2,500 to 3,000 words",
                                    "C. 4,000 to 5,000 words",
                                    "D. Exactly 2,000 words"
                                ],
                                "correct": "B. 2,500 to 3,000 words",
                                "explanation": "Giáo sư dặn: 'your paper should be between 2,500 and 3,000 words'."
                            }
                        ]
                    },
                    {
                        "conv_id": "conv-3",
                        "context": "Hội thoại 3 (Câu 17 - 20): Khách hàng trao đổi với nhân viên dịch vụ khách hàng về chuyến du lịch.",
                        "audio_text": "Agent: Good afternoon, Horizon Travel Agency. How may I assist you today?\nCustomer: Hello, I booked a 5-day package tour to Kyoto for two people departing on October 10th. My booking reference is KZ-982.\nAgent: Yes, Mr. Thompson. I have your file on my screen. How can I help with this booking?\nCustomer: My wife has an unexpected business trip, so we would like to postpone our departure to October 24th if possible.\nAgent: Let me check our flight and hotel availability for October 24th. Yes, we have twin rooms available at the same hotel. Since you are changing dates more than two weeks in advance, there is only a minimal rebooking fee of $30 per person.\nCustomer: That sounds very reasonable. Please proceed with the change and email me the updated itinerary.",
                        "questions": [
                            {
                                "id": "L17",
                                "question": "Where was the customer's tour booked to go?",
                                "options": [
                                    "A. Tokyo",
                                    "B. Kyoto",
                                    "C. Seoul",
                                    "D. Bangkok"
                                ],
                                "correct": "B. Kyoto",
                                "explanation": "Khách hàng nói: 'I booked a 5-day package tour to Kyoto for two people'."
                            },
                            {
                                "id": "L18",
                                "question": "Why does the customer want to change the departure date?",
                                "options": [
                                    "A. The weather in Kyoto is rainy",
                                    "B. His wife has an unexpected business trip",
                                    "C. They found a cheaper flight",
                                    "D. He lost his passport"
                                ],
                                "correct": "B. His wife has an unexpected business trip",
                                "explanation": "Khách hàng giải thích: 'My wife has an unexpected business trip'."
                            },
                            {
                                "id": "L19",
                                "question": "What is the new departure date requested?",
                                "options": [
                                    "A. October 10th",
                                    "B. October 17th",
                                    "C. October 24th",
                                    "D. November 1st"
                                ],
                                "correct": "C. October 24th",
                                "explanation": "Khách hàng muốn dời ngày: 'we would like to postpone our departure to October 24th'."
                            },
                            {
                                "id": "L20",
                                "question": "How much is the rebooking fee per person?",
                                "options": [
                                    "A. Free of charge",
                                    "B. $30",
                                    "C. $50",
                                    "D. $100"
                                ],
                                "correct": "B. $30",
                                "explanation": "Nhân viên thông báo: 'there is only a minimal rebooking fee of $30 per person'."
                            }
                        ]
                    }
                ]
            },
            
            # ── PART 3: 15 CÂU BÀI NÓI / BÀI GIẢNG HỌC THUẬT (3 TALKS x 5 QUESTIONS) ──
            {
                "part_id": 3,
                "part_title": "Part 3: Bài Giảng & Bài Nói Chuyện Học Thuật (15 câu)",
                "description": "Nghe 3 bài nói chuyện hoặc bài giảng học thuật. Mỗi bài có 5 câu hỏi trắc nghiệm.",
                "talks": [
                    {
                        "talk_id": "talk-1",
                        "context": "Bài nói 1 (Câu 21 - 25): Hướng dẫn viên giới thiệu về lịch sử và kiến trúc của một bảo tàng nghệ thuật hiện đại.",
                        "audio_text": "Good morning and welcome to the Metropolitan Gallery of Modern Art. My name is Arthur, and I will be your guide today. The gallery was founded in 1978 by a local philanthropist named Eleanor Vance. What makes this building unique is its architectural design: the exterior is built entirely from recycled steel and solar-reflective glass, which reduces our energy consumption by nearly 40 percent. On the ground floor, you will find our permanent collection of early 20th-century impressionist paintings. The second floor currently hosts a temporary exhibition featuring contemporary digital sculptures by young Asian artists. Please remember that flash photography is strictly prohibited in all exhibition halls to protect delicate pigments. We will finish our tour at the sculpture garden terrace around 11:30 AM, where complimentary tea will be served.",
                        "questions": [
                            {
                                "id": "L21",
                                "question": "When was the Metropolitan Gallery of Modern Art founded?",
                                "options": [
                                    "A. 1958",
                                    "B. 1978",
                                    "C. 1998",
                                    "D. 2008"
                                ],
                                "correct": "B. 1978",
                                "explanation": "Audio: 'The gallery was founded in 1978'."
                            },
                            {
                                "id": "L22",
                                "question": "What is special about the gallery building's construction?",
                                "options": [
                                    "A. It is built entirely underwater",
                                    "B. It uses recycled steel and solar-reflective glass to save energy",
                                    "C. It is the tallest wooden building in the city",
                                    "D. It was constructed inside an ancient castle"
                                ],
                                "correct": "B. It uses recycled steel and solar-reflective glass to save energy",
                                "explanation": "Audio: 'the exterior is built entirely from recycled steel and solar-reflective glass, which reduces our energy consumption by nearly 40 percent'."
                            },
                            {
                                "id": "L23",
                                "question": "What exhibition is displayed on the second floor?",
                                "options": [
                                    "A. Renaissance oil paintings",
                                    "B. Contemporary digital sculptures by young Asian artists",
                                    "C. Ancient Greek pottery",
                                    "D. Historical photography of World War II"
                                ],
                                "correct": "B. Contemporary digital sculptures by young Asian artists",
                                "explanation": "Audio: 'The second floor currently hosts a temporary exhibition featuring contemporary digital sculptures by young Asian artists'."
                            },
                            {
                                "id": "L24",
                                "question": "What rule must visitors strictly follow in exhibition halls?",
                                "options": [
                                    "A. No drinking water",
                                    "B. No flash photography",
                                    "C. Must wear formal suits",
                                    "D. Cannot speak English"
                                ],
                                "correct": "B. No flash photography",
                                "explanation": "Audio: 'flash photography is strictly prohibited in all exhibition halls'."
                            },
                            {
                                "id": "L25",
                                "question": "Where will the guided tour end?",
                                "options": [
                                    "A. At the souvenir gift shop",
                                    "B. At the sculpture garden terrace",
                                    "C. In the basement auditorium",
                                    "D. Near the front entrance ticket counter"
                                ],
                                "correct": "B. At the sculpture garden terrace",
                                "explanation": "Audio: 'We will finish our tour at the sculpture garden terrace around 11:30 AM'."
                            }
                        ]
                    },
                    {
                        "talk_id": "talk-2",
                        "context": "Bài giảng 2 (Câu 26 - 30): Giảng viên tâm lý học nói về tác động của giấc ngủ đối với khả năng ghi nhớ và học tập.",
                        "audio_text": "In today's cognitive psychology lecture, we examine the crucial relationship between sleep quality and memory consolidation. Many university students believe that pulling an all-nighter before an exam helps cram more information into their brain. However, neurological research shows the exact opposite. During Stage 3 deep sleep and Rapid Eye Movement (REM) sleep, the hippocampus transfers newly acquired facts to the neocortex for long-term storage. If you sleep less than six hours, your cognitive processing speed drops by up to 30 percent the following morning. Furthermore, sleep deprivation elevates cortisol, the body's primary stress hormone, which impairs emotional regulation and decision-making. To optimize academic performance, scientists recommend maintaining a regular sleep schedule of seven to eight hours per night and avoiding blue-light screens at least 45 minutes before bedtime.",
                        "questions": [
                            {
                                "id": "L26",
                                "question": "What happens during Stage 3 deep sleep and REM sleep?",
                                "options": [
                                    "A. The brain completely shuts down all metabolic activities",
                                    "B. The hippocampus transfers new facts to the neocortex for long-term storage",
                                    "C. The body stops producing red blood cells",
                                    "D. Memory is permanently erased to free up brain capacity"
                                ],
                                "correct": "B. The hippocampus transfers new facts to the neocortex for long-term storage",
                                "explanation": "Audio: 'During Stage 3 deep sleep and REM sleep, the hippocampus transfers newly acquired facts to the neocortex for long-term storage'."
                            },
                            {
                                "id": "L27",
                                "question": "By how much does cognitive processing speed drop after sleeping less than six hours?",
                                "options": [
                                    "A. By up to 10 percent",
                                    "B. By up to 30 percent",
                                    "C. By up to 50 percent",
                                    "D. It increases slightly"
                                ],
                                "correct": "B. By up to 30 percent",
                                "explanation": "Audio: 'If you sleep less than six hours, your cognitive processing speed drops by up to 30 percent'."
                            },
                            {
                                "id": "L28",
                                "question": "What hormone increases when a person suffers from sleep deprivation?",
                                "options": [
                                    "A. Insulin",
                                    "B. Melatonin",
                                    "C. Cortisol",
                                    "D. Dopamine"
                                ],
                                "correct": "C. Cortisol",
                                "explanation": "Audio: 'sleep deprivation elevates cortisol, the body's primary stress hormone'."
                            },
                            {
                                "id": "L29",
                                "question": "How many hours of sleep per night do scientists recommend for optimal performance?",
                                "options": [
                                    "A. 4 to 5 hours",
                                    "B. 5 to 6 hours",
                                    "C. 7 to 8 hours",
                                    "D. 10 to 12 hours"
                                ],
                                "correct": "C. 7 to 8 hours",
                                "explanation": "Audio: 'scientists recommend maintaining a regular sleep schedule of seven to eight hours per night'."
                            },
                            {
                                "id": "L30",
                                "question": "What should students avoid doing 45 minutes before going to bed?",
                                "options": [
                                    "A. Drinking warm water",
                                    "B. Using blue-light digital screens",
                                    "C. Reading printed books",
                                    "D. Meditating in a quiet room"
                                ],
                                "correct": "B. Using blue-light digital screens",
                                "explanation": "Audio: 'and avoiding blue-light screens at least 45 minutes before bedtime'."
                            }
                        ]
                    },
                    {
                        "talk_id": "talk-3",
                        "context": "Bài nói 3 (Câu 31 - 35): Nhà bảo tồn môi trường trình bày về các sáng kiến giảm thiểu rác thải nhựa đại dương.",
                        "audio_text": "Distinguished guests, our oceans currently face an unprecedented crisis. Every year, an estimated 11 million metric tons of plastic waste enter marine ecosystems, threatening over 800 species of sea animals. To combat this catastrophe, the Global Ocean Coalition launched the 'Clean Waves Initiative' in 2024. This program operates on three main fronts: First, deploying solar-powered automated cleanup barriers across 20 of the world's most polluting rivers to intercept plastic before it reaches the sea. Second, partnering with coastal communities to establish circular recycling facilities that transform collected plastics into durable construction bricks. Third, promoting legislative policies to ban single-use microplastics in consumer packaging. Within just two years, the initiative has successfully removed over 45,000 tons of debris from coastal waters and created 1,200 green jobs in developing nations.",
                        "questions": [
                            {
                                "id": "L31",
                                "question": "How much plastic waste enters marine ecosystems every year?",
                                "options": [
                                    "A. 1 million metric tons",
                                    "B. 5 million metric tons",
                                    "C. 11 million metric tons",
                                    "D. 50 million metric tons"
                                ],
                                "correct": "C. 11 million metric tons",
                                "explanation": "Audio: 'Every year, an estimated 11 million metric tons of plastic waste enter marine ecosystems'."
                            },
                            {
                                "id": "L32",
                                "question": "What is the name of the program launched in 2024?",
                                "options": [
                                    "A. Save The Blue Planet",
                                    "B. Clean Waves Initiative",
                                    "C. Ocean Barrier Network",
                                    "D. Pure Water Coalition"
                                ],
                                "correct": "B. Clean Waves Initiative",
                                "explanation": "Audio: 'the Global Ocean Coalition launched the Clean Waves Initiative in 2024'."
                            },
                            {
                                "id": "L33",
                                "question": "Where are the solar-powered automated cleanup barriers deployed?",
                                "options": [
                                    "A. In deep ocean trenches",
                                    "B. Across 20 of the most polluting rivers",
                                    "C. Along tourist beach resorts",
                                    "D. Inside private fish farms"
                                ],
                                "correct": "B. Across 20 of the most polluting rivers",
                                "explanation": "Audio: 'deploying solar-powered automated cleanup barriers across 20 of the world's most polluting rivers'."
                            },
                            {
                                "id": "L34",
                                "question": "What product is manufactured from recycled ocean plastic in coastal facilities?",
                                "options": [
                                    "A. Cheap plastic bags",
                                    "B. Disposable food containers",
                                    "C. Durable construction bricks",
                                    "D. Synthetic clothing fibers"
                                ],
                                "correct": "C. Durable construction bricks",
                                "explanation": "Audio: 'transform collected plastics into durable construction bricks'."
                            },
                            {
                                "id": "L35",
                                "question": "How many green jobs has the project created in developing nations?",
                                "options": [
                                    "A. 300 jobs",
                                    "B. 500 jobs",
                                    "C. 1,200 jobs",
                                    "D. 10,000 jobs"
                                ],
                                "correct": "C. 1,200 jobs",
                                "explanation": "Audio: 'and created 1,200 green jobs in developing nations'."
                            }
                        ]
                    }
                ]
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 2. KỸ NĂNG ĐỌC (READING) – 40 CÂU HỎI – 60 PHÚT (4 PASSAGES)
    # ══════════════════════════════════════════════════════════════════════════
    "reading": {
        "title": "Kỹ Năng Đọc Hiểu (Reading Comprehension)",
        "total_questions": 40,
        "time_min": 60,
        "instructions": "Bài thi Đọc gồm 4 bài đọc (Passage 1 đến Passage 4) với tổng cộng 40 câu hỏi trắc nghiệm. Thí sinh đọc văn bản và chọn câu trả lời đúng nhất (A, B, C hoặc D) cho mỗi câu hỏi.",
        "passages": [
            # ── PASSAGE 1: ĐỜI SỐNG, CÔNG SỞ & THÔNG BÁO DOANH NGHIỆP (CÂU 1 - 10) ──
            {
                "passage_id": 1,
                "title": "Passage 1: Chuyển Đổi Không Gian Làm Việc Linh Hoạt (Hybrid Workplace Policy)",
                "topic": "Workplace & Corporate Life",
                "text": """In response to shifting employee expectations and technological advancements, Apex Global Solutions announced its new Hybrid Workplace Framework, effective from the start of the next fiscal quarter. Under this policy, employees whose job responsibilities do not require physical presence on-site are permitted to work remotely up to three days per week.

To facilitate seamless collaboration between remote and in-office team members, the company has invested over $2.5 million into renovating headquarters facilities. Traditional individual cubicles have been replaced with dynamic 'hot-desking' hubs, ergonomic focus pods, and interactive conference rooms equipped with high-definition digital cameras and smart whiteboards. Employees can reserve desks and meeting spaces via a dedicated mobile intranet application up to one week in advance.

According to a survey conducted by the Human Resources department, 82 percent of staff reported higher job satisfaction and better work-life balance during the preliminary trial period. Furthermore, commuting times were reduced by an average of 4.5 hours per week for each participating employee. However, managers emphasized that core collaboration hours—between 10:00 AM and 3:00 PM—must be maintained regardless of physical location to ensure timely responsiveness to global client inquiries.

To support remote work infrastructure, Apex will provide each eligible worker with a one-time home office stipend of $800, which can be spent on high-speed internet subsidies, ergonomic chairs, or auxiliary computer monitors. All company-issued laptops must adhere strictly to multi-factor authentication and data encryption protocols established by the IT Security Division.""",
                "questions": [
                    {
                        "id": "R1",
                        "question": "What is the primary purpose of the text?",
                        "options": [
                            "A. To advertise a new commercial software for mobile phones",
                            "B. To describe a company's new hybrid workplace policy and its implementation",
                            "C. To announce the immediate closure of corporate headquarters",
                            "D. To report on financial losses in the last fiscal quarter"
                        ],
                        "correct": "B. To describe a company's new hybrid workplace policy and its implementation",
                        "explanation": "Toàn bài giới thiệu chính sách làm việc kết hợp mới của công ty Apex Global Solutions."
                    },
                    {
                        "id": "R2",
                        "question": "How many days per week are eligible employees allowed to work remotely?",
                        "options": [
                            "A. Exactly one day",
                            "B. Up to three days",
                            "C. All five working days",
                            "D. Only on alternate weekends"
                        ],
                        "correct": "B. Up to three days",
                        "explanation": "Đoạn 1 nêu: 'are permitted to work remotely up to three days per week'."
                    },
                    {
                        "id": "R3",
                        "question": "How much money did Apex invest in renovating headquarters facilities?",
                        "options": [
                            "A. $800,000",
                            "B. $1.5 million",
                            "C. Over $2.5 million",
                            "D. Exactly $5 million"
                        ],
                        "correct": "C. Over $2.5 million",
                        "explanation": "Đoạn 2 nêu: 'the company has invested over $2.5 million into renovating headquarters facilities'."
                    },
                    {
                        "id": "R4",
                        "question": "How can employees reserve desks and meeting spaces at the office?",
                        "options": [
                            "A. By writing on a paper sign-up sheet in the lobby",
                            "B. Through a dedicated mobile intranet application",
                            "C. By calling the HR director directly",
                            "D. Desks cannot be reserved in advance"
                        ],
                        "correct": "B. Through a dedicated mobile intranet application",
                        "explanation": "Đoạn 2 nêu: 'Employees can reserve desks and meeting spaces via a dedicated mobile intranet application'."
                    },
                    {
                        "id": "R5",
                        "question": "The word 'preliminary' in paragraph 3 is closest in meaning to:",
                        "options": [
                            "A. final",
                            "B. initial / introductory",
                            "C. permanent",
                            "D. unsuccessful"
                        ],
                        "correct": "B. initial / introductory",
                        "explanation": "'preliminary' nghĩa là giai đoạn thử nghiệm ban đầu (initial / introductory)."
                    },
                    {
                        "id": "R6",
                        "question": "What positive outcome was observed during the trial period?",
                        "options": [
                            "A. 82% of staff reported higher job satisfaction and better balance",
                            "B. Office electricity costs dropped to zero",
                            "C. All client complaints completely vanished",
                            "D. Commuting times increased slightly"
                        ],
                        "correct": "A. 82% of staff reported higher job satisfaction and better balance",
                        "explanation": "Đoạn 3 nêu: '82 percent of staff reported higher job satisfaction and better work-life balance'."
                    },
                    {
                        "id": "R7",
                        "question": "What are the designated 'core collaboration hours' specified by management?",
                        "options": [
                            "A. 8:00 AM to 12:00 PM",
                            "B. 10:00 AM to 3:00 PM",
                            "C. 1:00 PM to 5:00 PM",
                            "D. 9:00 AM to 6:00 PM"
                        ],
                        "correct": "B. 10:00 AM to 3:00 PM",
                        "explanation": "Đoạn 3: 'managers emphasized that core collaboration hours—between 10:00 AM and 3:00 PM—must be maintained'."
                    },
                    {
                        "id": "R8",
                        "question": "How much home office stipend does Apex provide to eligible workers?",
                        "options": [
                            "A. $300",
                            "B. $500",
                            "C. $800",
                            "D. $1,200"
                        ],
                        "correct": "C. $800",
                        "explanation": "Đoạn 4 nêu: 'provide each eligible worker with a one-time home office stipend of $800'."
                    },
                    {
                        "id": "R9",
                        "question": "The word 'subsidies' in paragraph 4 refers to:",
                        "options": [
                            "A. financial aids / allowances",
                            "B. disciplinary fines",
                            "C. computer hardware warranties",
                            "D. travel taxes"
                        ],
                        "correct": "A. financial aids / allowances",
                        "explanation": "'subsidies' là các khoản hỗ trợ tài chính / trợ cấp (financial aids / allowances)."
                    },
                    {
                        "id": "R10",
                        "question": "What must all company-issued laptops comply with?",
                        "options": [
                            "A. Free distribution to family members",
                            "B. Multi-factor authentication and data encryption protocols",
                            "C. Weekly replacement with newer models",
                            "D. No internet connection allowed"
                        ],
                        "correct": "B. Multi-factor authentication and data encryption protocols",
                        "explanation": "Đoạn cuối nêu: 'All company-issued laptops must adhere strictly to multi-factor authentication and data encryption protocols'."
                    }
                ]
            },

            # ── PASSAGE 2: KHOA HỌC SỨC KHỎE & DINH DƯỠNG (CÂU 11 - 20) ──
            {
                "passage_id": 2,
                "title": "Passage 2: Chế Độ Ăn Địa Trung Hải & Lợi Ích Tim Mạch (The Mediterranean Diet)",
                "topic": "Health & Nutritional Science",
                "text": """For decades, nutritional epidemiologists have puzzled over the remarkable longevity and low incidence of cardiovascular disease documented in Mediterranean communities. Despite consuming moderate to high amounts of dietary fats, populations living in countries such as Greece, Southern Italy, and Spain consistently outlive their Northern European and American counterparts. Today, scientific consensus attributes this phenomenon to the traditional Mediterranean Diet.

At the core of this dietary pattern is the abundant consumption of minimally processed plant-based foods. Fresh vegetables, fruits, legumes, whole grains, nuts, and seeds form the foundation of daily meals. Extra virgin olive oil serves as the principal culinary fat, replacing saturated animal fats like butter and lard. Olive oil is exceptionally rich in monounsaturated oleic acid and polyphenols, potent antioxidants that diminish systemic inflammation and inhibit arterial plaque accumulation.

Moderate intake of fish and seafood—particularly fatty fish like salmon, sardines, and mackerel—supplies vital omega-3 fatty acids that stabilize heart rhythms and reduce blood triglyceride levels. In contrast, red meat and processed deli meats are consumed sparingly, often limited to a few times per month. Dairy products, primarily yogurt and traditional cheeses, are eaten in modest portions, providing calcium and beneficial gut probiotics.

Moreover, the Mediterranean lifestyle encompasses more than just food choices. Physical activity is seamlessly woven into daily routines through walking, gardening, and active recreation. Meals are viewed as social rituals, shared unhurriedly with family and friends, which significantly lowers chronic psychological stress. Clinical trials indicate that strict adherence to the Mediterranean diet reduces the risk of stroke, type 2 diabetes, and cognitive decline by up to 35 percent.""",
                "questions": [
                    {
                        "id": "R11",
                        "question": "What surprising medical fact about Mediterranean populations is mentioned in paragraph 1?",
                        "options": [
                            "A. They avoid all forms of physical exercise",
                            "B. They enjoy high longevity despite consuming moderate to high amounts of dietary fats",
                            "C. They suffer from widespread vitamin deficiencies",
                            "D. They consume red meat with every meal"
                        ],
                        "correct": "B. They enjoy high longevity despite consuming moderate to high amounts of dietary fats",
                        "explanation": "Đoạn 1 nêu: 'Despite consuming moderate to high amounts of dietary fats, populations... consistently outlive their counterparts'."
                    },
                    {
                        "id": "R12",
                        "question": "What foods form the foundation of daily Mediterranean meals?",
                        "options": [
                            "A. Refined sugars and pastries",
                            "B. Fast food hamburgers and fries",
                            "C. Fresh vegetables, fruits, legumes, whole grains, nuts, and seeds",
                            "D. High-protein canned meat"
                        ],
                        "correct": "C. Fresh vegetables, fruits, legumes, whole grains, nuts, and seeds",
                        "explanation": "Đoạn 2 nêu: 'Fresh vegetables, fruits, legumes, whole grains, nuts, and seeds form the foundation of daily meals'."
                    },
                    {
                        "id": "R13",
                        "question": "What is the principal culinary fat used in Mediterranean cooking?",
                        "options": [
                            "A. Butter",
                            "B. Lard",
                            "C. Extra virgin olive oil",
                            "D. Palm oil"
                        ],
                        "correct": "C. Extra virgin olive oil",
                        "explanation": "Đoạn 2: 'Extra virgin olive oil serves as the principal culinary fat'."
                    },
                    {
                        "id": "R14",
                        "question": "Why is extra virgin olive oil beneficial for cardiovascular health?",
                        "options": [
                            "A. It raises blood sugar rapidly",
                            "B. It contains oleic acid and polyphenols that reduce inflammation and plaque accumulation",
                            "C. It contains no calories",
                            "D. It replaces the need for drinking water"
                        ],
                        "correct": "B. It contains oleic acid and polyphenols that reduce inflammation and plaque accumulation",
                        "explanation": "Đoạn 2: 'rich in monounsaturated oleic acid and polyphenols, potent antioxidants that diminish systemic inflammation and inhibit arterial plaque accumulation'."
                    },
                    {
                        "id": "R15",
                        "question": "How often is red meat consumed in a traditional Mediterranean diet?",
                        "options": [
                            "A. Three times every day",
                            "B. Twice a week",
                            "C. Sparingly, often limited to a few times per month",
                            "D. Never under any circumstances"
                        ],
                        "correct": "C. Sparingly, often limited to a few times per month",
                        "explanation": "Đoạn 3: 'In contrast, red meat and processed deli meats are consumed sparingly, often limited to a few times per month'."
                    },
                    {
                        "id": "R16",
                        "question": "The word 'modest' in paragraph 3 is closest in meaning to:",
                        "options": [
                            "A. excessive",
                            "B. moderate / limited",
                            "C. dangerous",
                            "D. expensive"
                        ],
                        "correct": "B. moderate / limited",
                        "explanation": "'modest portions' nghĩa là khẩu phần vừa phải, có chừng mực (moderate / limited)."
                    },
                    {
                        "id": "R17",
                        "question": "What health benefit do omega-3 fatty acids from fish provide?",
                        "options": [
                            "A. They stabilize heart rhythms and reduce triglycerides",
                            "B. They cure all viral infections instantly",
                            "C. They replace the necessity of sleep",
                            "D. They increase blood pressure"
                        ],
                        "correct": "A. They stabilize heart rhythms and reduce triglycerides",
                        "explanation": "Đoạn 3: 'supplies vital omega-3 fatty acids that stabilize heart rhythms and reduce blood triglyceride levels'."
                    },
                    {
                        "id": "R18",
                        "question": "What lifestyle factor beyond diet contributes to Mediterranean wellness?",
                        "options": [
                            "A. Spending hours playing video games",
                            "B. Unhurried social meals with loved ones and regular gentle physical activity",
                            "C. Working overtime without breaks",
                            "D. Taking synthetic diet pills"
                        ],
                        "correct": "B. Unhurried social meals with loved ones and regular gentle physical activity",
                        "explanation": "Đoạn 4 mô tả: 'Meals are viewed as social rituals, shared unhurriedly with family and friends... Physical activity is seamlessly woven into daily routines'."
                    },
                    {
                        "id": "R19",
                        "question": "The word 'adherence' in paragraph 4 is closest in meaning to:",
                        "options": [
                            "A. objection",
                            "B. commitment / following strictly",
                            "C. ignorance",
                            "D. departure"
                        ],
                        "correct": "B. commitment / following strictly",
                        "explanation": "'adherence' nghĩa là sự tuân thủ nghiêm ngặt theo chế độ (commitment / following strictly)."
                    },
                    {
                        "id": "R20",
                        "question": "By up to what percentage can strict adherence reduce the risk of stroke and type 2 diabetes?",
                        "options": [
                            "A. 10 percent",
                            "B. 20 percent",
                            "C. 35 percent",
                            "D. 80 percent"
                        ],
                        "correct": "C. 35 percent",
                        "explanation": "Đoạn 4: 'reduces the risk of stroke, type 2 diabetes, and cognitive decline by up to 35 percent'."
                    }
                ]
            },

            # ── PASSAGE 3: CÔNG NGHỆ & TRÍ TUỆ NHÂN TẠO TRONG GIÁO DỤC (CÂU 21 - 30) ──
            {
                "passage_id": 3,
                "title": "Passage 3: Trí Tuệ Nhân Tạo & Cách Mạng Hóa Giáo Dục (AI in Education)",
                "topic": "Technology & Educational Evolution",
                "text": """The rapid integration of Artificial Intelligence (AI) into modern pedagogy is transforming the landscape of education worldwide. For centuries, traditional classroom models relied upon a standardized curriculum where one teacher instructed thirty or forty students simultaneously at a uniform pace. This 'one-size-fits-all' paradigm inevitably left behind students who needed additional reinforcement while failing to challenge high-achieving pupils.

Intelligent Tutoring Systems (ITS) powered by machine learning algorithms are dismantling these pedagogical constraints. By analyzing student response patterns, completion speed, and error frequencies in real time, adaptive learning platforms dynamically recalibrate lesson difficulty. When a learner struggles with a quadratic equation in mathematics or past participle verbs in English, the system immediately generates scaffolding hints, visual concept maps, and targeted micro-lessons tailored to their exact cognitive deficit.

Contrary to early fears that AI would render human educators obsolete, emerging evidence suggests that technology acts as a force multiplier for teachers. Automated grading software and administrative assistants handle repetitive burdens—such as evaluating multiple-choice quizzes, drafting progress reports, and tracking attendance. Consequently, teachers reclaim up to twelve hours per week, allowing them to dedicate quality time to mentorship, socio-emotional counseling, and creative project guidance.

Nonetheless, experts emphasize that ethical safeguards must accompany AI deployment. Issues surrounding student data privacy, algorithmic bias, and equitable access to digital devices remain pressing concerns. If advanced AI learning tools are only accessible to affluent school districts, educational inequality will widen. Governments and educational policymakers must ensure that AI literacy and infrastructure are universally distributed across all socioeconomic strata.""",
                "questions": [
                    {
                        "id": "R21",
                        "question": "What major limitation of traditional classroom models is identified in paragraph 1?",
                        "options": [
                            "A. School buildings were poorly constructed",
                            "B. A uniform pace failed to accommodate diverse student learning speeds and needs",
                            "C. Teachers lacked academic degrees",
                            "D. Students refused to take exams"
                        ],
                        "correct": "B. A uniform pace failed to accommodate diverse student learning speeds and needs",
                        "explanation": "Đoạn 1 nêu: 'This 'one-size-fits-all' paradigm inevitably left behind students who needed additional reinforcement while failing to challenge high-achieving pupils'."
                    },
                    {
                        "id": "R22",
                        "question": "How do Intelligent Tutoring Systems (ITS) adapt to individual students?",
                        "options": [
                            "A. By assigning identical homework to the entire class",
                            "B. By analyzing response patterns, completion speed, and error frequencies in real time",
                            "C. By randomly shuffling questions without logic",
                            "D. By replacing all digital computers with paper textbooks"
                        ],
                        "correct": "B. By analyzing response patterns, completion speed, and error frequencies in real time",
                        "explanation": "Đoạn 2: 'By analyzing student response patterns, completion speed, and error frequencies in real time, adaptive learning platforms dynamically recalibrate lesson difficulty'."
                    },
                    {
                        "id": "R23",
                        "question": "What does the system do when a student struggles with a concept?",
                        "options": [
                            "A. Disqualifies the student from the course",
                            "B. Generates scaffolding hints, concept maps, and targeted micro-lessons",
                            "C. Shuts down the computer automatically",
                            "D. Charges an extra subscription fee"
                        ],
                        "correct": "B. Generates scaffolding hints, concept maps, and targeted micro-lessons",
                        "explanation": "Đoạn 2: 'the system immediately generates scaffolding hints, visual concept maps, and targeted micro-lessons tailored to their exact cognitive deficit'."
                    },
                    {
                        "id": "R24",
                        "question": "The word 'obsolete' in paragraph 3 is closest in meaning to:",
                        "options": [
                            "A. essential",
                            "B. out of date / no longer needed",
                            "C. wealthy",
                            "D. popular"
                        ],
                        "correct": "B. out of date / no longer needed",
                        "explanation": "'obsolete' nghĩa là lỗi thời, không còn được cần đến (out of date / no longer needed)."
                    },
                    {
                        "id": "R25",
                        "question": "According to the passage, how does AI benefit human educators?",
                        "options": [
                            "A. It replaces teachers entirely in all schools",
                            "B. It automates repetitive administrative tasks, saving up to 12 hours per week for mentorship",
                            "C. It reduces teachers' salaries",
                            "D. It eliminates the need for lesson planning"
                        ],
                        "correct": "B. It automates repetitive administrative tasks, saving up to 12 hours per week for mentorship",
                        "explanation": "Đoạn 3: 'Automated grading software... handle repetitive burdens... Consequently, teachers reclaim up to twelve hours per week, allowing them to dedicate quality time to mentorship'."
                    },
                    {
                        "id": "R26",
                        "question": "The phrase 'force multiplier' in paragraph 3 implies that AI:",
                        "options": [
                            "A. decreases teacher effectiveness",
                            "B. greatly enhances and amplifies teachers' capabilities",
                            "C. forces teachers to work overtime",
                            "D. creates computer viruses"
                        ],
                        "correct": "B. greatly enhances and amplifies teachers' capabilities",
                        "explanation": "'force multiplier' là hệ số nhân lực, giúp gia tăng đáng kể hiệu năng và năng lực của giáo viên."
                    },
                    {
                        "id": "R27",
                        "question": "Which of the following is NOT mentioned as an ethical concern in paragraph 4?",
                        "options": [
                            "A. Student data privacy",
                            "B. Algorithmic bias",
                            "C. Teacher dress codes",
                            "D. Equitable access to digital devices"
                        ],
                        "correct": "C. Teacher dress codes",
                        "explanation": "Đoạn 4 đề cập privacy, bias, equitable access; không đề cập 'Teacher dress codes'."
                    },
                    {
                        "id": "R28",
                        "question": "The word 'affluent' in paragraph 4 is closest in meaning to:",
                        "options": [
                            "A. impoverished",
                            "B. wealthy / rich",
                            "C. rural",
                            "D. overcrowded"
                        ],
                        "correct": "B. wealthy / rich",
                        "explanation": "'affluent' có nghĩa là giàu có, thịnh vượng (wealthy / rich)."
                    },
                    {
                        "id": "R29",
                        "question": "What risk arises if AI tools are only available to wealthy districts?",
                        "options": [
                            "A. Educational inequality will widen",
                            "B. Schools will run out of electricity",
                            "C. All students will get perfect test scores",
                            "D. Classrooms will become too quiet"
                        ],
                        "correct": "A. Educational inequality will widen",
                        "explanation": "Đoạn 4: 'If advanced AI learning tools are only accessible to affluent school districts, educational inequality will widen'."
                    },
                    {
                        "id": "R30",
                        "question": "What is the author's concluding recommendation?",
                        "options": [
                            "A. Ban AI from all educational institutions permanently",
                            "B. Ensure AI literacy and infrastructure are universally distributed to all students",
                            "C. Allow private tech companies to manage public schools",
                            "D. Cancel all standardized examinations"
                        ],
                        "correct": "B. Ensure AI literacy and infrastructure are universally distributed to all students",
                        "explanation": "Đoạn cuối: 'Governments and educational policymakers must ensure that AI literacy and infrastructure are universally distributed across all socioeconomic strata'."
                    }
                ]
            },

            # ── PASSAGE 4: MÔI TRƯỜNG & NĂNG LƯỢNG TÁI TẠO ĐÔ THỊ (CÂU 31 - 40) ──
            {
                "passage_id": 4,
                "title": "Passage 4: Thành Phố Xanh & Khí Hậu Tương Lai (Urban Sustainability)",
                "topic": "Environment & Sustainable Architecture",
                "text": """As metropolitan areas expand at an unprecedented rate, modern cities are responsible for over 70 percent of global carbon emissions and two-thirds of worldwide energy consumption. Urban sprawl has exacerbated the 'Urban Heat Island' effect, where concrete, asphalt, and high-density buildings absorb solar radiation during the day and re-emit it at night, raising metropolitan temperatures by up to 5 degrees Celsius compared to surrounding rural regions.

To counteract these environmental challenges, urban planners and architectural engineers are pioneering sustainable 'Eco-City' designs. A prominent innovation is the mandatory integration of green roofs and vertical gardens on commercial skyscrapers. Incorporating living vegetation onto rooftops not only provides thermal insulation—lowering indoor air-conditioning demand by 25 percent—but also absorbs stormwater runoff, mitigating flash floods during severe monsoon downpours.

Simultaneously, transportation infrastructure is undergoing a radical decarbonization transition. Municipalities across Europe and Asia are expanding dedicated electric bus rapid transit (BRT) lanes, bike-sharing networks, and pedestrian-only commercial zones. Cities such as Copenhagen and Amsterdam have demonstrated that when safe, segregated cycling lanes are constructed, more than 40 percent of daily commuter trips shift from fossil-fuel automobiles to bicycles.

Finally, smart energy microgrids powered by distributed solar photovoltaic panels and urban wind turbines allow neighborhoods to generate, store, and trade localized renewable electricity. When residential buildings produce surplus energy during sunny midday hours, battery storage hubs store the excess power to feed back into the central grid during peak evening hours. Through the synergy of renewable architecture, green mobility, and intelligent energy management, modern metropolises can transition from environmental liabilities into sustainable ecological havens.""",
                "questions": [
                    {
                        "id": "R31",
                        "question": "What proportion of global carbon emissions do cities produce according to paragraph 1?",
                        "options": [
                            "A. Less than 20 percent",
                            "B. Around 50 percent",
                            "C. Over 70 percent",
                            "D. Exactly 100 percent"
                        ],
                        "correct": "C. Over 70 percent",
                        "explanation": "Đoạn 1 nêu: 'modern cities are responsible for over 70 percent of global carbon emissions'."
                    },
                    {
                        "id": "R32",
                        "question": "What causes the 'Urban Heat Island' effect?",
                        "options": [
                            "A. Volcanic eruptions near city centers",
                            "B. Concrete, asphalt, and dense buildings absorbing and re-emitting solar heat",
                            "C. Excessive planting of urban trees",
                            "D. Ocean water evaporating into the air"
                        ],
                        "correct": "B. Concrete, asphalt, and dense buildings absorbing and re-emitting solar heat",
                        "explanation": "Đoạn 1: 'where concrete, asphalt, and high-density buildings absorb solar radiation during the day and re-emit it at night'."
                    },
                    {
                        "id": "R33",
                        "question": "How much can metropolitan temperatures rise due to the Urban Heat Island effect?",
                        "options": [
                            "A. By up to 1 degree Celsius",
                            "B. By up to 5 degrees Celsius",
                            "C. By over 20 degrees Celsius",
                            "D. Temperatures drop below freezing"
                        ],
                        "correct": "B. By up to 5 degrees Celsius",
                        "explanation": "Đoạn 1: 'raising metropolitan temperatures by up to 5 degrees Celsius compared to surrounding rural regions'."
                    },
                    {
                        "id": "R34",
                        "question": "What dual benefit do green roofs provide on skyscrapers?",
                        "options": [
                            "A. They produce commercial wood and gold",
                            "B. They provide thermal insulation and absorb stormwater runoff to prevent flash floods",
                            "C. They replace the building foundation",
                            "D. They attract dangerous wild predators"
                        ],
                        "correct": "B. They provide thermal insulation and absorb stormwater runoff to prevent flash floods",
                        "explanation": "Đoạn 2: 'not only provides thermal insulation—lowering indoor air-conditioning demand by 25 percent—but also absorbs stormwater runoff, mitigating flash floods'."
                    },
                    {
                        "id": "R35",
                        "question": "The word 'mitigating' in paragraph 2 is closest in meaning to:",
                        "options": [
                            "A. worsening",
                            "B. reducing / alleviating",
                            "C. creating",
                            "D. ignoring"
                        ],
                        "correct": "B. reducing / alleviating",
                        "explanation": "'mitigating' có nghĩa là giảm thiểu, làm nhẹ bớt (reducing / alleviating)."
                    },
                    {
                        "id": "R36",
                        "question": "What transport shift occurred in Copenhagen and Amsterdam after building segregated bike lanes?",
                        "options": [
                            "A. People bought more luxury sports cars",
                            "B. Over 40 percent of daily commuter trips shifted to bicycles",
                            "C. All buses stopped running",
                            "D. Pedestrians were banned from streets"
                        ],
                        "correct": "B. Over 40 percent of daily commuter trips shifted to bicycles",
                        "explanation": "Đoạn 3: 'more than 40 percent of daily commuter trips shift from fossil-fuel automobiles to bicycles'."
                    },
                    {
                        "id": "R37",
                        "question": "The word 'surplus' in paragraph 4 is closest in meaning to:",
                        "options": [
                            "A. shortage",
                            "B. excess / extra amount",
                            "C. expensive",
                            "D. damaged"
                        ],
                        "correct": "B. excess / extra amount",
                        "explanation": "'surplus' nghĩa là lượng thặng dư, dồi dào vượt mức nhu cầu (excess / extra amount)."
                    },
                    {
                        "id": "R38",
                        "question": "How do smart microgrids handle excess energy generated during sunny hours?",
                        "options": [
                            "A. They discard it as heat into the air",
                            "B. Battery hubs store it to feed back into the central grid during peak evening hours",
                            "C. They shut down all solar panels immediately",
                            "D. They convert it into chemical pollution"
                        ],
                        "correct": "B. Battery hubs store it to feed back into the central grid during peak evening hours",
                        "explanation": "Đoạn 4: 'battery storage hubs store the excess power to feed back into the central grid during peak evening hours'."
                    },
                    {
                        "id": "R39",
                        "question": "The word 'liabilities' in the final sentence most nearly means:",
                        "options": [
                            "A. assets",
                            "B. burdens / disadvantages",
                            "C. legal lawyers",
                            "D. tourist attractions"
                        ],
                        "correct": "B. burdens / disadvantages",
                        "explanation": "'environmental liabilities' là các gánh nặng / hiểm họa môi trường (burdens / disadvantages)."
                    },
                    {
                        "id": "R40",
                        "question": "Which of the following would be the best title for Passage 4?",
                        "options": [
                            "A. The Decline of European Bicycle Manufacturers",
                            "B. Transforming Metropolises into Sustainable Eco-Cities",
                            "C. The High Costs of Solar Panels in Rural Areas",
                            "D. Why Cities Should Stop Constructing Skyscrapers"
                        ],
                        "correct": "B. Transforming Metropolises into Sustainable Eco-Cities",
                        "explanation": "Bài đọc tổng quan các giải pháp kiến trúc xanh, giao thông xanh và vi lưới điện giúp thành phố trở thành đô thị sinh thái bền vững."
                    }
                ]
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 3. KỸ NĂNG VIẾT (WRITING) – 2 TASKS – 60 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "writing": {
        "title": "Kỹ Năng Viết (Writing Mastery)",
        "total_tasks": 2,
        "time_min": 60,
        "instructions": "Bài thi Viết gồm 2 phần (Task 1 và Task 2). Tổng thời gian làm bài là 60 phút. Thí sinh cần phân bổ khoảng 20 phút cho Task 1 (tối thiểu 120 từ) và 40 phút cho Task 2 (tối thiểu 250 từ).",
        "tasks": [
            {
                "task_id": "W1",
                "task_number": 1,
                "task_type": "Social / Formal Email Response",
                "suggested_time_min": 20,
                "word_requirement": "Khoảng 120 từ (100 - 150 words)",
                "weight_percentage": 33.3,
                "prompt": """You received an email from an English friend named Oliver, who is planning to visit your home city for a 4-day vacation next month:

"Hi there! I am finally visiting your city next month for four days! I am so excited. Could you give me some advice on what kind of clothes I should pack for the weather? Also, which famous attractions or local food spots must I not miss? And finally, do you have any free time next weekend so we can meet up for coffee or dinner? Let me know soon! Best, Oliver."

Write an email response to Oliver. In your email, you should:
1. Advise him on suitable clothing for the current weather.
2. Recommend at least two famous tourist spots and delicious local specialties.
3. Suggest a specific time and location to meet up together.""",
                "sample_high_band": """Dear Oliver,

I am thrilled to hear that you are visiting my city next month! You are going to have a fantastic time here.

Regarding the weather, it is usually warm and sunny during the day but can get slightly chilly in the evenings. Therefore, I recommend packing lightweight T-shirts, comfortable jeans, and a light jacket or cardigan for night strolls.

While you are here, you definitely should not miss visiting the historic Old Quarter and the picturesque Hoan Kiem Lake. For food, you must try traditional Pho noodle soup and crispy Banh Mi from local street vendors; their flavors are unforgettable!

I would love to catch up with you. I am completely free next Saturday afternoon, so let's meet at 'Cong Cafe' near the city theater around 4:00 PM.

Safe travels, and see you very soon!

Warm regards,
[Your Name]""",
                "scoring_criteria": {
                    "task_fulfillment": "Trả lời đầy đủ 3 yêu cầu đề bài (Trang phục, Địa điểm/Món ăn, Hẹn gặp).",
                    "coherence_cohesion": "Bố cục email chuẩn (Chào hỏi, 3 đoạn thân bài, Lời kết), liên từ mượt mà (Regarding, Therefore, While, For food).",
                    "lexical_resource": "Từ vựng tự nhiên, phù hợp văn cảnh giao lưu bạn bè (thrilled, picturesque, unforgettable, catch up).",
                    "grammatical_accuracy": "Ngữ pháp chính xác, dùng đúng thì tương lai, câu đề nghị và câu điều kiện."
                }
            },
            {
                "task_id": "W2",
                "task_number": 2,
                "task_type": "Opinion / Discussion Essay",
                "suggested_time_min": 40,
                "word_requirement": "Khoảng 250 từ (230 - 300 words)",
                "weight_percentage": 66.7,
                "prompt": """Read the following statement:

"Some people believe that studying online from home is much more effective than attending traditional in-person classes at school or university. Others argue that physical classrooms are essential for comprehensive learning and social development."

Write an essay (at least 250 words) to discuss both views and give your own opinion. Support your arguments with relevant examples and explanations.""",
                "sample_high_band": """In recent years, the rapid advancement of educational technology has sparked intense debate over whether online remote learning is superior to traditional classroom education. While virtual schooling offers remarkable flexibility, I believe that physical classrooms remain irreplaceable for comprehensive academic and social development.

On the one hand, advocates of online education highlight its undeniable convenience and accessibility. Learners can attend lectures delivered by top global professors from the comfort of their homes, eliminating exhausting daily commutes and saving substantial transportation costs. Furthermore, recorded webinars and digital archives enable students to review complex concepts at their own personalized pace. For working adults or individuals residing in remote rural areas, e-learning provides unprecedented opportunities to acquire degrees without disrupting their professional careers.

On the other hand, traditional face-to-face schooling provides crucial benefits that virtual platforms cannot replicate. Foremost among these is interpersonal interaction. In a brick-and-mortar classroom, students actively collaborate on group projects, engage in spontaneous debates, and build vital social skills such as teamwork, empathy, and leadership. Moreover, the direct physical presence of teachers fosters greater discipline and accountability, preventing the severe distractions and lack of focus frequently associated with prolonged computer screen usage. Real-time laboratory experiments and physical sports activities also enrich the holistic educational experience.

In conclusion, although online learning serves as an exceptional supplementary tool that offers extraordinary convenience, traditional classrooms remain indispensable for nurturing well-rounded individuals. A hybrid educational model that thoughtfully blends digital resources with immersive classroom interactions represents the optimal path forward for future education.""",
                "scoring_criteria": {
                    "task_response": "Phân tích rõ ràng cả 2 quan điểm (ưu điểm Online vs ưu điểm Offline) và nêu rõ lập trường cá nhân (Hybrid/Offline).",
                    "coherence_cohesion": "Dàn bài 4 đoạn học thuật chuẩn mực, các câu nối liên kết chặt chẽ (On the one hand, On the other hand, Furthermore, In conclusion).",
                    "lexical_resource": "Vốn từ vựng học thuật phong phú (undeniable convenience, interpersonal interaction, brick-and-mortar, holistic educational experience).",
                    "grammatical_range": "Cấu trúc câu phức, mệnh đề quan hệ, câu ghép và mệnh đề nhượng bộ chuẩn xác."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 4. KỸ NĂNG NÓI (SPEAKING) – 3 PARTS – 12 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "speaking": {
        "title": "Kỹ Năng Nói (Speaking Fluency & Interaction)",
        "total_parts": 3,
        "time_min": 12,
        "instructions": "Bài thi Nói gồm 3 phần thi phản xạ trực tiếp với AI Examiner. Tổng thời gian khoảng 12 phút (Part 1: 3 phút, Part 2: 4 phút, Part 3: 5 phút).",
        "parts": [
            {
                "part_id": "S1",
                "part_title": "Part 1: Tương Tác Xã Hội (Social Interaction - 3 phút)",
                "description": "Thí sinh trả lời các câu hỏi ngắn quen thuộc về 2 chủ đề đời sống (Sở thích, Thói quen hàng ngày, Du lịch hoặc Công việc).",
                "topics": [
                    {
                        "topic_name": "Topic 1: Daily Routine & Free Time",
                        "questions": [
                            {
                                "q_id": "S1-Q1",
                                "text": "What do you usually do in your free time or on weekends?",
                                "sample_response": "In my spare time, I love reading English non-fiction books and going cycling in the local park with my friends. It helps me recharge my energy after a hectic week of work."
                            },
                            {
                                "q_id": "S1-Q2",
                                "text": "Do you prefer spending your holidays in the countryside or in a bustling city?",
                                "sample_response": "I definitely prefer spending my holidays in the peaceful countryside because the fresh air, lush green landscapes, and tranquil atmosphere help me relieve mental stress completely."
                            },
                            {
                                "q_id": "S1-Q3",
                                "text": "How important is physical exercise in your daily routine?",
                                "sample_response": "Physical exercise is extremely essential for me. I try to jog for at least 30 minutes every morning to stay fit, improve my cardiovascular endurance, and maintain high concentration."
                            }
                        ]
                    },
                    {
                        "topic_name": "Topic 2: Learning English & Technology",
                        "questions": [
                            {
                                "q_id": "S1-Q4",
                                "text": "Why are you currently preparing for the B1 English exam?",
                                "sample_response": "I am studying for the B1 certificate because it is a key requirement for my university graduation and it opens up fantastic career opportunities in multinational companies."
                            },
                            {
                                "q_id": "S1-Q5",
                                "text": "What digital apps or websites do you find most helpful for learning English?",
                                "sample_response": "I frequently use AI English learning apps and listen to BBC podcasts. The interactive flashcards and instant pronunciation feedback make vocabulary retention much faster."
                            }
                        ]
                    }
                ]
            },
            {
                "part_id": "S2",
                "part_title": "Part 2: Thảo Luận Giải Pháp (Solution Discussion - 4 phút)",
                "description": "Thí sinh được đưa ra một tình huống với 3 phương án lựa chọn. Cần chọn 1 phương án tốt nhất, đưa ra lý do bảo vệ và giải thích tại sao 2 phương án còn lại chưa tối ưu.",
                "situation": """Situation: Your university student club has been granted a funding of $2,000 to organize an end-of-year team bonding activity. Three options are proposed:
1. Option A: A 2-day outdoor camping trip at a mountain national park.
2. Option B: A luxurious buffet dinner party at a five-star downtown hotel.
3. Option C: Purchasing new board games and technology equipment for the club activity room.

Which option do you think is the best choice? Explain your reasons and why you did not choose the other two options.""",
                "sample_response": """In this situation, among the three proposed options, I strongly believe that Option A—organizing a 2-day outdoor camping trip at a mountain national park—is the best choice for our student club.

There are several compelling reasons for my decision. Firstly, camping in nature provides authentic team bonding experiences. Members will have to work collaboratively to pitch tents, prepare BBQ meals, and engage in campfire games, which fosters strong camaraderie and interpersonal trust. Secondly, a 2-day getaway allows students to disconnect from digital screens and enjoy refreshing mountain air.

Regarding Option B, a buffet dinner at a five-star hotel would be overly formal and expensive. While the food is delightful, the event would only last for a couple of hours and does not encourage deep teamwork. As for Option C, buying board games and equipment is useful, but it does not create unforgettable shared memories like an adventurous trip. 

Therefore, Option A is undoubtedly the most meaningful and impactful investment for our club members.""",
                "tips": "Nêu rõ sự lựa chọn ngay câu mở đầu (I strongly believe Option A is the best...). Đưa ra 2 lý do chứng minh và phản biện ngắn gọn Option B & C."
            },
            {
                "part_id": "S3",
                "part_title": "Part 3: Phát Triển Chủ Đề (Topic Development - 5 phút)",
                "description": "Thí sinh phát triển một chủ đề dựa trên sơ đồ tư duy (Mindmap) có 3 ý gợi ý và 1 ý tự chọn, sau đó trả lời các câu hỏi mở rộng của giám khảo.",
                "topic_title": "The Advantages of Living in a Smart Green City",
                "mindmap_branches": [
                    {"branch": "1. Better Public Health", "detail": "Cleaner air, lower pollution, and abundant green parks reduce respiratory and chronic diseases."},
                    {"branch": "2. Efficient Eco-Friendly Transport", "detail": "Electric buses, subways, and cycling lanes minimize traffic congestion and commuting stress."},
                    {"branch": "3. Lower Energy Costs", "detail": "Smart renewable solar grids and energy-efficient buildings reduce monthly household bills."},
                    {"branch": "4. [Your Own Idea] High Quality of Life & Safety", "detail": "Smart IoT waste management and AI public surveillance create a safe and serene environment."}
                ],
                "sample_presentation": """Today, I would like to talk about the prominent advantages of residing in a smart green city. In my opinion, modern eco-cities offer immense benefits that transform human well-being across several dimensions.

First and foremost, green cities dramatically enhance public health. By replacing fossil-fuel factories with renewable energy and expanding urban forests, air quality improves significantly. Citizens have abundant access to green parks for jogging and outdoor recreation, which lowers the incidence of respiratory issues and mental fatigue.

Secondly, smart metropolises boast highly efficient, eco-friendly transportation networks. With the integration of electric metro lines and dedicated cycling corridors, traffic congestion is virtually eliminated, allowing commuters to save precious time and travel comfortably.

Lastly, living in an eco-city brings substantial economic savings through renewable energy. Solar-powered smart microgrids allow households to cut down on electricity expenses while contributing to global climate protection. In addition, intelligent waste management systems ensure a spotless, aesthetic urban landscape.

In conclusion, living in a smart green city not only preserves the planet for future generations but also guarantees a healthier, happier, and more sustainable lifestyle for all citizens.""",
                "follow_up_questions": [
                    {
                        "q_id": "S3-FQ1",
                        "question": "Do you think developing nations can afford to build smart green cities in the near future?",
                        "sample_answer": "Yes, although the initial capital investment is high, international green climate funds and decreasing solar technology costs will make green city infrastructure increasingly affordable for developing nations."
                    },
                    {
                        "q_id": "S3-FQ2",
                        "question": "What can individual citizens do right now to make their current city greener?",
                        "sample_answer": "Individual citizens can make a significant difference by using public transit or bicycles, sorting household recyclables diligently, planting trees on balconies, and reducing single-use plastic consumption."
                    }
                ]
            }
        ]
    }
}
