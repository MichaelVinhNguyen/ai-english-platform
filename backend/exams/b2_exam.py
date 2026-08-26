# -*- coding: utf-8 -*-
"""
backend/exams/b2_exam.py – Ngân Hàng Đề Thi Chuẩn Hóa CEFR B2 / Cambridge FCE / VSTEP Bậc 4
Format Khảo Thí Thực Tế:
1. Kỹ Năng Nghe (Listening): 35 câu hỏi – 40 phút (Part 1: 8 câu, Part 2: 12 câu, Part 3: 15 câu)
2. Kỹ Năng Đọc (Reading): 40 câu hỏi – 60 phút (4 Passages x 10 câu)
3. Kỹ Năng Viết (Writing): 2 Tasks – 60 phút (Task 1: Formal Letter 150-180 từ, Task 2: Essay 250-280 từ)
4. Kỹ Năng Nói (Speaking): 3 Parts – 14 phút (Part 1: Social Interaction, Part 2: Solution Discussion, Part 3: Topic Development)
"""

B2_STANDARDIZED_EXAM_DATA = {
    "exam_id": "b2-fce-vstep-cefr-2026-01",
    "title": "Đề Thi Chuẩn Hóa Tiếng Anh CEFR B2 / Cambridge FCE / VSTEP Bậc 4 Thực Chiến 2026",
    "level": "B2",
    "standard": "CEFR B2 Vantage / VSTEP Bậc 4 Format 2026",
    "total_time_min": 174,
    "pass_gpa": 6.0,

    # ══════════════════════════════════════════════════════════════════════════
    # 1. KỸ NĂNG NGHE (LISTENING) – 35 CÂU HỎI – 40 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "listening": {
        "title": "Kỹ Năng Nghe – CEFR B2 (Listening Comprehension)",
        "total_questions": 35,
        "time_min": 40,
        "instructions": "Đề thi Nghe B2 gồm 3 phần với 35 câu hỏi trắc nghiệm. Thí sinh lắng nghe và chọn một đáp án đúng nhất (A, B, C hoặc D).",
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Tin Tức Thời Sự & Phỏng Vấn Ngắn (8 câu)",
                "description": "Nghe 8 đoạn tin ngắn, bản tin phỏng vấn hoặc thông báo chuyên đề.",
                "audio_script": "This is Part 1 of the CEFR B2 Listening Test. You will hear eight short extracts. Choose the best answer from A, B, C, or D.",
                "questions": [
                    {
                        "id": "B2_L1",
                        "audio_text": "Radio presenter: Welcome back to Tech Digest. Today, Apex Solutions announced a breakthrough in solid-state battery technology, promising electric vehicles a driving range of over 800 kilometers on a single 15-minute charge.",
                        "question": "What is the primary breakthrough reported about the new solid-state battery?",
                        "options": ["A. It reduces the vehicle weight by 50%", "B. It enables an 800km range with a 15-minute charge", "C. It can only be used in heavy commercial trucks", "D. It operates without any lithium materials"],
                        "correct": "B. It enables an 800km range with a 15-minute charge",
                        "explanation": "Audio khẳng định: 'promising electric vehicles a driving range of over 800 kilometers on a single 15-minute charge'."
                    },
                    {
                        "id": "B2_L2",
                        "audio_text": "Speaker: To foster workforce agility, our corporate management has decided that all employees may work remotely up to two days per week starting next quarter, provided departmental performance quotas remain satisfied.",
                        "question": "Under what condition may employees work remotely two days per week?",
                        "options": ["A. If they take a salary reduction", "B. As long as departmental performance quotas are maintained", "C. Only during the winter months", "D. If they work overtime on weekends"],
                        "correct": "B. As long as departmental performance quotas are maintained",
                        "explanation": "Audio: 'provided departmental performance quotas remain satisfied'."
                    },
                    {
                        "id": "B2_L3",
                        "audio_text": "Scientist: Our recent study on urban biodiversity indicates that planting native flowering shrubs on traffic islands substantially increases the local pollinator population, particularly bumblebees and solitary bees.",
                        "question": "What effect does planting native shrubs on traffic islands produce?",
                        "options": ["A. It creates severe traffic congestion", "B. It significantly boosts local pollinator populations like bees", "C. It requires expensive daily watering systems", "D. It attracts harmful crop pests"],
                        "correct": "B. It significantly boosts local pollinator populations like bees",
                        "explanation": "Audio: 'substantially increases the local pollinator population, particularly bumblebees'."
                    },
                    {
                        "id": "B2_L4",
                        "audio_text": "Broadcaster: The municipal council has approved a $15 million budget to upgrade the civic water filtration infrastructure, aiming to replace all lead service pipes within eighteen months.",
                        "question": "What is the key objective of the municipal water budget?",
                        "options": ["A. Building a new hydroelectric dam", "B. Replacing all lead service pipes within 18 months", "C. Privatizing residential water distribution", "D. Increasing monthly household water taxes"],
                        "correct": "B. Replacing all lead service pipes within 18 months",
                        "explanation": "Audio: 'aiming to replace all lead service pipes within eighteen months'."
                    },
                    {
                        "id": "B2_L5",
                        "audio_text": "Financial reporter: Global crude oil prices fluctuated sharply today following supply disruptions in the North Sea pipeline network, causing benchmark Brent crude to surge above $88 a barrel.",
                        "question": "Why did global crude oil prices surge above $88?",
                        "options": ["A. Increased consumer fuel subsidies", "B. Supply disruptions in the North Sea pipeline network", "C. A sudden decrease in shipping freight costs", "D. Discovery of massive offshore reserves"],
                        "correct": "B. Supply disruptions in the North Sea pipeline network",
                        "explanation": "Audio: 'following supply disruptions in the North Sea pipeline network'."
                    },
                    {
                        "id": "B2_L6",
                        "audio_text": "Doctor: While caffeine can enhance acute mental alertness, consuming energy drinks late in the evening severely disrupts deep REM sleep cycles, impairing cognitive function the next morning.",
                        "question": "What warning does the doctor issue regarding late-evening energy drinks?",
                        "options": ["A. They cause immediate tooth decay", "B. They disrupt deep REM sleep cycles and impair morning cognition", "C. They have no effect on physical energy", "D. They cure chronic sleep insomnia"],
                        "correct": "B. They disrupt deep REM sleep cycles and impair morning cognition",
                        "explanation": "Audio: 'severely disrupts deep REM sleep cycles, impairing cognitive function the next morning'."
                    },
                    {
                        "id": "B2_L7",
                        "audio_text": "Curator: The Modernist Sculpture Pavilion will undergo extensive seismic reinforcement, during which its prominent Renaissance bronze statues will be temporarily relocated to the East Wing.",
                        "question": "Where will the Renaissance bronze statues be moved during construction?",
                        "options": ["A. To an overseas auction house", "B. To the East Wing of the museum", "C. To an underground storage facility", "D. To the city hall lobby"],
                        "correct": "B. To the East Wing of the museum",
                        "explanation": "Audio: 'temporarily relocated to the East Wing'."
                    },
                    {
                        "id": "B2_L8",
                        "audio_text": "Career advisor: Employers in the tech sector increasingly prioritize candidates who demonstrate strong collaboration and empathetic communication over those with purely isolated technical capabilities.",
                        "question": "What attribute is increasingly prioritized by tech sector employers?",
                        "options": ["A. Ability to work completely without supervision", "B. Strong collaboration and empathetic communication skills", "C. High typing speed and hardware repair skills", "D. Willingness to work without vacation"],
                        "correct": "B. Strong collaboration and empathetic communication skills",
                        "explanation": "Audio: 'prioritize candidates who demonstrate strong collaboration and empathetic communication'."
                    }
                ]
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Hội Thoại Học Thuật & Quản Lý Dự Án (12 câu)",
                "description": "Nghe 3 cuộc hội thoại chuyên sâu (mỗi đoạn 4 câu) về chiến lược kinh doanh, nghiên cứu và quản trị.",
                "audio_script": "This is Part 2. You will hear three extended conversations. Choose the best answer for each question.",
                "conversations": [
                    {
                        "conv_id": "b2-conv-1",
                        "context": "Hội thoại 1 (Câu 9 - 12): Triển khai phần mềm đám mây tại doanh nghiệp.",
                        "audio_text": "Elena: Jason, have we finalized the transition roadmap for our cloud database migration?\nJason: We've made substantial progress, Elena. The engineering team verified that AWS data centers in Frankfurt meet all EU General Data Protection Regulation criteria.\nElena: That is critical. What about the estimated system downtime during the cutover next weekend?\nJason: We calculated that the migration will take approximately four hours between 1:00 AM and 5:00 AM on Sunday, which minimizes operational disruption to our retail clients.\nElena: Excellent. Let's make sure our customer support hotline has dedicated engineers standing by throughout Sunday morning.",
                        "questions": [
                            {
                                "id": "B2_L9",
                                "question": "What regulatory standard did the cloud migration team verify in Frankfurt?",
                                "options": ["A. US Federal Aviation Regulations", "B. EU General Data Protection Regulation (GDPR)", "C. Asian Maritime Shipping Code", "D. Global Mining Safety Standards"],
                                "correct": "B. EU General Data Protection Regulation (GDPR)",
                                "explanation": "Jason nêu: 'meet all EU General Data Protection Regulation criteria'."
                            },
                            {
                                "id": "B2_L10",
                                "question": "When is the cutover migration scheduled to take place?",
                                "options": ["A. Friday afternoon during peak hours", "B. Between 1:00 AM and 5:00 AM on Sunday", "C. Next month on a public holiday", "D. Wednesday at noon"],
                                "correct": "B. Between 1:00 AM and 5:00 AM on Sunday",
                                "explanation": "Jason: 'between 1:00 AM and 5:00 AM on Sunday'."
                            },
                            {
                                "id": "B2_L11",
                                "question": "Why was the early Sunday morning timeframe chosen?",
                                "options": ["A. Because server electricity is free", "B. To minimize operational disruption to retail clients", "C. To comply with city noise ordinances", "D. The engineers only work night shifts"],
                                "correct": "B. To minimize operational disruption to retail clients",
                                "explanation": "Jason: 'which minimizes operational disruption to our retail clients'."
                            },
                            {
                                "id": "B2_L12",
                                "question": "What precaution does Elena instruct for Sunday morning?",
                                "options": ["A. Shut down all customer accounts permanently", "B. Have dedicated support engineers standing by", "C. Postpone customer invoices", "D. Issue refunds to all users"],
                                "correct": "B. Have dedicated support engineers standing by",
                                "explanation": "Elena: 'Let's make sure our customer support hotline has dedicated engineers standing by'."
                            }
                        ]
                    },
                    {
                        "conv_id": "b2-conv-2",
                        "context": "Hội thoại 2 (Câu 13 - 16): Sinh viên nghiên cứu sinh thảo luận đề tài xử lý nước thải vi nhựa.",
                        "audio_text": "Professor: Marcus, your proposal on utilizing biochar filtration for capturing microplastics in municipal wastewater shows great promise.\nMarcus: Thank you, Professor Vance. However, I am concerned about the saturation threshold of the biochar filters over continuous 30-day testing periods.\nProfessor: A valid point. You could introduce a modular backwashing cycle using pressurized ozone water to regenerate the porous adsorption capacity.\nMarcus: That could solve the saturation issue without generating hazardous chemical byproducts! I will integrate that variable into my laboratory test matrix this Friday.",
                        "questions": [
                            {
                                "id": "B2_L13",
                                "question": "What is the primary focus of Marcus's research proposal?",
                                "options": ["A. Deep sea oil drilling techniques", "B. Biochar filtration for capturing microplastics in wastewater", "C. Desalination of polar icebergs", "D. Agricultural pesticide synthesis"],
                                "correct": "B. Biochar filtration for capturing microplastics in wastewater",
                                "explanation": "Giáo sư nhận xét: 'utilizing biochar filtration for capturing microplastics in municipal wastewater'."
                            },
                            {
                                "id": "B2_L14",
                                "question": "What technical concern did Marcus express?",
                                "options": ["A. Lack of funding for lab glassware", "B. The saturation threshold of filters over continuous 30-day testing", "C. Inability to read German literature", "D. High cost of safety goggles"],
                                "correct": "B. The saturation threshold of filters over continuous 30-day testing",
                                "explanation": "Marcus: 'concerned about the saturation threshold of the biochar filters over continuous 30-day testing periods'."
                            },
                            {
                                "id": "B2_L15",
                                "question": "What solution did Professor Vance suggest to regenerate filter capacity?",
                                "options": ["A. Burning the filters at extreme heat", "B. A modular backwashing cycle using pressurized ozone water", "C. Replacing the entire system daily", "D. Adding sulfuric acid to the tanks"],
                                "correct": "B. A modular backwashing cycle using pressurized ozone water",
                                "explanation": "Giáo sư: 'modular backwashing cycle using pressurized ozone water'."
                            },
                            {
                                "id": "B2_L16",
                                "question": "What major benefit of the ozone backwashing method did Marcus highlight?",
                                "options": ["A. It reduces lab noise", "B. It solves saturation without producing hazardous chemical byproducts", "C. It guarantees a commercial patent", "D. It cuts electricity usage to zero"],
                                "correct": "B. It solves saturation without producing hazardous chemical byproducts",
                                "explanation": "Marcus: 'without generating hazardous chemical byproducts'."
                            }
                        ]
                    },
                    {
                        "conv_id": "b2-conv-3",
                        "context": "Hội thoại 3 (Câu 17 - 20): Đàm phán phân phối sản phẩm thực phẩm hữu cơ.",
                        "audio_text": "Distributor: Rachel, we love your organic plant-based protein bars, but our retail supermarkets require a guaranteed minimum shelf life of nine months.\nRachel: Currently, our nitrogen-flushed biodegradable packaging delivers seven months of optimal freshness without artificial preservatives.\nDistributor: If you can integrate natural antioxidant rosemary extract into the formulation, we can extend the shelf life to ten months and place an initial order of 100,000 units across 200 stores.\nRachel: Our food science team has already tested rosemary extract with positive taste results. We can finalize the contract by the end of this month.",
                        "questions": [
                            {
                                "id": "B2_L17",
                                "question": "What minimum shelf life did the retail distributor initially request?",
                                "options": ["A. Three months", "B. Six months", "C. Nine months", "D. Twelve months"],
                                "correct": "C. Nine months",
                                "explanation": "Nhà phân phối: 'require a guaranteed minimum shelf life of nine months'."
                            },
                            {
                                "id": "B2_L18",
                                "question": "What was the existing shelf life of Rachel's product?",
                                "options": ["A. Two months", "B. Four months", "C. Seven months", "D. Nine months"],
                                "correct": "C. Seven months",
                                "explanation": "Rachel: 'delivers seven months of optimal freshness'."
                            },
                            {
                                "id": "B2_L19",
                                "question": "What ingredient addition was proposed to extend the shelf life to 10 months?",
                                "options": ["A. Synthetic food coloring", "B. Natural antioxidant rosemary extract", "C. High fructose corn syrup", "D. Sodium benzoate preservative"],
                                "correct": "B. Natural antioxidant rosemary extract",
                                "explanation": "Nhà phân phối đề xuất: 'integrate natural antioxidant rosemary extract'."
                            },
                            {
                                "id": "B2_L20",
                                "question": "What initial order size was promised upon meeting the shelf life target?",
                                "options": ["A. 10,000 units across 20 stores", "B. 50,000 units across 100 stores", "C. 100,000 units across 200 stores", "D. 500,000 units nationwide"],
                                "correct": "C. 100,000 units across 200 stores",
                                "explanation": "Nhà phân phối: 'initial order of 100,000 units across 200 stores'."
                            }
                        ]
                    }
                ]
            },
            {
                "part_id": 3,
                "part_title": "Part 3: Bài Giảng Học Thuật & Thuyết Trình Khoa Học (15 câu)",
                "description": "Nghe 3 bài giảng học thuật (mỗi bài 5 câu) về Năng lượng sạch, Kinh tế học hành vi và Đô thị thông minh.",
                "audio_script": "This is Part 3. You will hear three academic lectures. Choose the best answer for each question.",
                "talks": [
                    {
                        "talk_id": "b2-talk-1",
                        "context": "Bài giảng 1 (Câu 21 - 25): Công nghệ Pin Mặt Trời Perovskite Thế Hệ Mới.",
                        "audio_text": "Good morning class. Today we explore perovskite solar cells, widely considered the most transformative development in photovoltaic science over the past decade. Unlike conventional silicon panels, which require energy-intensive manufacturing at temperatures exceeding 1,400 degrees Celsius, perovskite crystals can be processed from liquid chemical solutions at under 150 degrees. In laboratory trials, tandem perovskite-silicon configurations have achieved energy conversion efficiencies surpassing 33%, vastly outperforming traditional silicon's theoretical threshold of 29%. The primary commercial hurdle remains chemical degradation when exposed to atmospheric moisture, which researchers are actively mitigating through nanoscale polymer encapsulation barriers.",
                        "questions": [
                            {
                                "id": "B2_L21",
                                "question": "What makes perovskite solar cell manufacturing less energy-intensive than silicon?",
                                "options": ["A. It uses radioactive isotopes", "B. Crystals can be processed from liquid solutions at under 150°C", "C. It operates only in complete vacuum chambers", "D. It requires no physical processing equipment"],
                                "correct": "B. Crystals can be processed from liquid solutions at under 150°C",
                                "explanation": "Bài giảng: 'perovskite crystals can be processed from liquid chemical solutions at under 150 degrees'."
                            },
                            {
                                "id": "B2_L22",
                                "question": "What energy conversion efficiency have tandem perovskite-silicon cells achieved in lab trials?",
                                "options": ["A. 15%", "B. 22%", "C. Surpassing 33%", "D. Over 50%"],
                                "correct": "C. Surpassing 33%",
                                "explanation": "Bài giảng: 'tandem perovskite-silicon configurations have achieved energy conversion efficiencies surpassing 33%'."
                            },
                            {
                                "id": "B2_L23",
                                "question": "What is the theoretical efficiency threshold of conventional silicon panels?",
                                "options": ["A. 18%", "B. 25%", "C. 29%", "D. 35%"],
                                "correct": "C. 29%",
                                "explanation": "Bài giảng: 'vastly outperforming traditional silicon's theoretical threshold of 29%'."
                            },
                            {
                                "id": "B2_L24",
                                "question": "What is the primary obstacle preventing immediate large-scale commercialization?",
                                "options": ["A. Extremely high material costs", "B. Chemical degradation when exposed to atmospheric moisture", "C. Excessive weight of perovskite crystals", "D. International patent disputes"],
                                "correct": "B. Chemical degradation when exposed to atmospheric moisture",
                                "explanation": "Bài giảng: 'The primary commercial hurdle remains chemical degradation when exposed to atmospheric moisture'."
                            },
                            {
                                "id": "B2_L25",
                                "question": "How are scientists currently resolving the moisture degradation issue?",
                                "options": ["A. By placing solar panels underwater", "B. Through nanoscale polymer encapsulation barriers", "C. By using heavy lead casing", "D. Through daily chemical spraying"],
                                "correct": "B. Through nanoscale polymer encapsulation barriers",
                                "explanation": "Bài giảng: 'mitigating through nanoscale polymer encapsulation barriers'."
                            }
                        ]
                    },
                    {
                        "talk_id": "b2-talk-2",
                        "context": "Bài giảng 2 (Câu 26 - 30): Kinh Tế Học Hành Vi và Hiệu Ứng Nudge (Thúc Đẩy Nhẹ).",
                        "audio_text": "In behavioral economics, 'Nudge Theory' popularized by Nobel laureate Richard Thaler demonstrates that subtle alterations in choice architecture can significantly steer human decisions without forbidding any options or changing economic incentives. A classic empirical example is the default enrollment mechanism in corporate pension schemes. When employees must actively opt out rather than opt in, participation rates increase dramatically from under 40% to over 85%. Similarly, placing fresh fruit at eye level in school cafeterias while shifting sugary snacks to lower shelves increases healthy food selection by 28% without restricting student autonomy.",
                        "questions": [
                            {
                                "id": "B2_L26",
                                "question": "According to Nudge Theory, how are human decisions influenced?",
                                "options": ["A. By imposing strict financial penalties", "B. Through subtle alterations in choice architecture without restricting options", "C. By eliminating all competing products", "D. Through compulsory government mandates"],
                                "correct": "B. Through subtle alterations in choice architecture without restricting options",
                                "explanation": "Bài giảng: 'subtle alterations in choice architecture can significantly steer human decisions without forbidding any options'."
                            },
                            {
                                "id": "B2_L27",
                                "question": "What happened to pension participation when default enrollment was implemented?",
                                "options": ["A. It declined by 15%", "B. It remained unchanged at 40%", "C. It increased dramatically from under 40% to over 85%", "D. It caused employees to resign"],
                                "correct": "C. It increased dramatically from under 40% to over 85%",
                                "explanation": "Bài giảng: 'participation rates increase dramatically from under 40% to over 85%'."
                            },
                            {
                                "id": "B2_L28",
                                "question": "What cafeteria intervention increased healthy food selection by 28%?",
                                "options": ["A. Doubling the price of soda", "B. Banning all desserts completely", "C. Placing fresh fruit at eye level and shifting sugary snacks lower", "D. Providing free vitamin pills"],
                                "correct": "C. Placing fresh fruit at eye level and shifting sugary snacks lower",
                                "explanation": "Bài giảng: 'placing fresh fruit at eye level in school cafeterias while shifting sugary snacks to lower shelves'."
                            },
                            {
                                "id": "B2_L29",
                                "question": "Who is the prominent economist associated with Nudge Theory mentioned in the lecture?",
                                "options": ["A. Adam Smith", "B. John Maynard Keynes", "C. Richard Thaler", "D. Milton Friedman"],
                                "correct": "C. Richard Thaler",
                                "explanation": "Bài giảng: 'popularized by Nobel laureate Richard Thaler'."
                            },
                            {
                                "id": "B2_L30",
                                "question": "What is a defining characteristic of an authentic 'nudge'?",
                                "options": ["A. It preserves individual autonomy while gently guiding choice", "B. It removes freedom of choice", "C. It requires expensive advertising campaigns", "D. It relies exclusively on tax increases"],
                                "correct": "A. It preserves individual autonomy while gently guiding choice",
                                "explanation": "Bài giảng: 'without forbidding any options or changing economic incentives... without restricting student autonomy'."
                            }
                        ]
                    },
                    {
                        "talk_id": "b2-talk-3",
                        "context": "Bài giảng 3 (Câu 31 - 35): Quy Hoạch Đô Thị Xanh và Khái Niệm Thành Phố 15 Phút.",
                        "audio_text": "Urban planners globally are embracing the '15-Minute City' framework, originally formulated by Professor Carlos Moreno. The core premise posits that all essential daily human needs—including grocery shopping, healthcare, primary education, recreation, and green spaces—should be accessible within a 15-minute walk or bicycle ride from one's residence. Cities like Paris and Melbourne are repurposing motor vehicle lanes into protected cycling corridors and transforming asphalt schoolyards into public community parks outside classroom hours. By decentralizing commercial amenities, this model reduces private vehicle carbon emissions by up to 35% while fostering vibrant, resilient local economies.",
                        "questions": [
                            {
                                "id": "B2_L31",
                                "question": "What is the core premise of the 15-Minute City model?",
                                "options": ["A. Every citizen must commute 15 kilometers by train", "B. All essential daily needs should be within a 15-minute walk or bike ride", "C. Speed limits inside cities are capped at 15 km/h", "D. Workdays are shortened to 15 hours per week"],
                                "correct": "B. All essential daily needs should be within a 15-minute walk or bike ride",
                                "explanation": "Bài giảng: 'all essential daily human needs... should be accessible within a 15-minute walk or bicycle ride'."
                            },
                            {
                                "id": "B2_L32",
                                "question": "Who formulated the 15-Minute City framework?",
                                "options": ["A. Professor Carlos Moreno", "B. David Harvey", "C. Jane Jacobs", "D. Le Corbusier"],
                                "correct": "A. Professor Carlos Moreno",
                                "explanation": "Bài giảng: 'originally formulated by Professor Carlos Moreno'."
                            },
                            {
                                "id": "B2_L33",
                                "question": "What are cities like Paris and Melbourne converting motor vehicle lanes into?",
                                "options": ["A. High-speed toll highways", "B. Protected cycling corridors", "C. Multi-story car parks", "D. Industrial shipping depots"],
                                "correct": "B. Protected cycling corridors",
                                "explanation": "Bài giảng: 'repurposing motor vehicle lanes into protected cycling corridors'."
                            },
                            {
                                "id": "B2_L34",
                                "question": "How are schoolyards utilized outside classroom hours in this urban model?",
                                "options": ["A. Locked for strict security", "B. Converted into public community parks", "C. Rented out as commercial warehouses", "D. Used as car dealerships"],
                                "correct": "B. Converted into public community parks",
                                "explanation": "Bài giảng: 'transforming asphalt schoolyards into public community parks outside classroom hours'."
                            },
                            {
                                "id": "B2_L35",
                                "question": "What environmental impact does this urban decentralization achieve?",
                                "options": ["A. Increases electricity consumption by 50%", "B. Reduces private vehicle carbon emissions by up to 35%", "C. Doubles urban ambient noise levels", "D. Eliminates all public transit"],
                                "correct": "B. Reduces private vehicle carbon emissions by up to 35%",
                                "explanation": "Bài giảng: 'reduces private vehicle carbon emissions by up to 35%'."
                            }
                        ]
                    }
                ]
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 2. KỸ NĂNG ĐỌC (READING) – 40 CÂU HỎI – 60 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "reading": {
        "title": "Kỹ Năng Đọc – CEFR B2 (Reading Comprehension)",
        "total_questions": 40,
        "time_min": 60,
        "instructions": "Đề thi Đọc B2 gồm 4 bài đọc học thuật chuyên đề (mỗi bài 10 câu hỏi) bao quát các lĩnh vực Công nghệ, Năng lượng, Kinh tế và Giáo dục.",
        "passages": [
            {
                "passage_id": "b2-p1",
                "title": "Passage 1: Artificial Intelligence and the Transformation of Global Labor",
                "topic": "Technology & Workforce Transformation",
                "content": "The accelerating deployment of artificial intelligence and machine learning algorithms across diverse industrial sectors is fundamentally reshaping the landscape of global employment. Historically, technological revolutions—from the steam engine to automated assembly lines—primarily disrupted manual physical labor while creating higher-tier supervisory and engineering roles. However, contemporary generative AI models possess the unprecedented capacity to automate complex cognitive tasks, including legal contract analysis, diagnostic radiography interpretation, algorithmic financial trading, and software code generation.\n\nWhile alarmist perspectives predict widespread structural unemployment, mainstream economists emphasize that AI functions predominantly as an augmenting tool rather than an outright human replacement. In professional healthcare, for example, diagnostic deep learning neural networks assist radiologists by detecting early-stage pulmonary nodules with 96% accuracy, reducing diagnostic error margins and expediting clinical workflows. Rather than eliminating medical jobs, AI empowers practitioners to dedicate significantly more time to patient communication, compassionate care, and multidisciplinary treatment planning.\n\nNevertheless, this rapid transition presents acute workforce challenges. The widening skill gap requires comprehensive institutional retraining programs. Educational systems must pivot away from rote memorization toward cultivating distinctly human capabilities, such as ethical reasoning, interdisciplinary critical thinking, collaborative negotiation, and emotional intelligence. Policy experts argue that proactive government investment in lifelong digital education and robust social safety nets will determine whether the AI revolution exacerbates socio-economic inequality or catalyzes widespread societal prosperity.",
                "questions": [
                    {
                        "id": "B2_R1",
                        "question": "How does the current AI revolution fundamentally differ from historical industrial revolutions?",
                        "options": [
                            "A. It only impacts low-wage agricultural workers",
                            "B. It has the capacity to automate complex cognitive and analytical tasks rather than just manual labor",
                            "C. It requires no electrical energy to function",
                            "D. It eliminates all forms of physical machinery"
                        ],
                        "correct": "B. It has the capacity to automate complex cognitive and analytical tasks rather than just manual labor",
                        "explanation": "Đoạn 1 nêu: 'generative AI models possess the unprecedented capacity to automate complex cognitive tasks... rather than primarily manual physical labor'."
                    },
                    {
                        "id": "B2_R2",
                        "question": "According to the passage, which professional tasks can modern AI models perform?",
                        "options": [
                            "A. Legal contract analysis, radiography interpretation, and code generation",
                            "B. Physical surgery without supervision only",
                            "C. Direct emotional psychological healing",
                            "D. Manual manufacturing assembly exclusively"
                        ],
                        "correct": "A. Legal contract analysis, radiography interpretation, and code generation",
                        "explanation": "Đoạn 1 liệt kê: 'legal contract analysis, diagnostic radiography interpretation... and software code generation'."
                    },
                    {
                        "id": "B2_R3",
                        "question": "The word 'alarmist' in paragraph 2 is closest in meaning to:",
                        "options": ["A. Optimistic and joyful", "B. Overly fearful and panic-inducing", "C. Scientific and objective", "D. Indifferent and bored"],
                        "correct": "B. Overly fearful and panic-inducing",
                        "explanation": "'Alarmist' mang nghĩa gây hoang mang, lo sợ thái quá."
                    },
                    {
                        "id": "B2_R4",
                        "question": "How does deep learning assistance benefit healthcare professionals in radiography?",
                        "options": [
                            "A. By replacing all doctors with robots",
                            "B. By detecting early pulmonary nodules with 96% accuracy and reducing diagnostic errors",
                            "C. By cutting medical equipment prices to zero",
                            "D. By eliminating hospital waiting rooms entirely"
                        ],
                        "correct": "B. By detecting early pulmonary nodules with 96% accuracy and reducing diagnostic errors",
                        "explanation": "Đoạn 2 nêu: 'detecting early-stage pulmonary nodules with 96% accuracy, reducing diagnostic error margins'."
                    },
                    {
                        "id": "B2_R5",
                        "question": "What can doctors dedicate more time to when AI assists with diagnostic data?",
                        "options": [
                            "A. Taking extended annual holidays",
                            "B. Patient communication, compassionate care, and multidisciplinary treatment planning",
                            "C. Writing software code for other hospitals",
                            "D. Managing financial accounting spreadsheets"
                        ],
                        "correct": "B. Patient communication, compassionate care, and multidisciplinary treatment planning",
                        "explanation": "Đoạn 2: 'empowers practitioners to dedicate significantly more time to patient communication, compassionate care, and multidisciplinary treatment planning'."
                    },
                    {
                        "id": "B2_R6",
                        "question": "The word 'augmenting' in paragraph 2 suggests that AI is used to:",
                        "options": ["A. Completely destroy existing workflows", "B. Enhance and support human capabilities", "C. Ignore human input", "D. Reduce salary levels"],
                        "correct": "B. Enhance and support human capabilities",
                        "explanation": "'Augmenting' nghĩa là bổ trợ, gia tăng và nâng cao năng lực."
                    },
                    {
                        "id": "B2_R7",
                        "question": "What pedagogical shift is recommended for educational systems in paragraph 3?",
                        "options": [
                            "A. Focusing exclusively on memorizing mathematical formulas",
                            "B. Shifting away from rote memorization toward ethical reasoning and critical thinking",
                            "C. Eliminating all social science curricula",
                            "D. Shortening the school year to three months"
                        ],
                        "correct": "B. Shifting away from rote memorization toward ethical reasoning and critical thinking",
                        "explanation": "Đoạn 3: 'pivot away from rote memorization toward cultivating distinctly human capabilities, such as ethical reasoning, interdisciplinary critical thinking'."
                    },
                    {
                        "id": "B2_R8",
                        "question": "Which human attribute is emphasized as resilient against AI automation?",
                        "options": ["A. Repetitive manual data entry", "B. Emotional intelligence and collaborative negotiation", "C. Copying text verbatim", "D. Memorizing vocabulary lists"],
                        "correct": "B. Emotional intelligence and collaborative negotiation",
                        "explanation": "Đoạn 3 liệt kê: 'interdisciplinary critical thinking, collaborative negotiation, and emotional intelligence'."
                    },
                    {
                        "id": "B2_R9",
                        "question": "What crucial role do policy experts assign to proactive government intervention?",
                        "options": [
                            "A. Banning all computer science research",
                            "B. Investing in lifelong digital education and robust social safety nets",
                            "C. Forcing tech companies to shut down algorithms",
                            "D. Nationalizing all private medical clinics"
                        ],
                        "correct": "B. Investing in lifelong digital education and robust social safety nets",
                        "explanation": "Đoạn 3 kết luận: 'proactive government investment in lifelong digital education and robust social safety nets'."
                    },
                    {
                        "id": "B2_R10",
                        "question": "What is the primary conclusion of the passage regarding the future impact of AI?",
                        "options": [
                            "A. AI will inevitably destroy human civilization within a decade",
                            "B. Its societal outcome depends on how proactively societies adapt through education and policy",
                            "C. AI will have negligible impact on global economics",
                            "D. Manual factory jobs will become the highest paid professions"
                        ],
                        "correct": "B. Its societal outcome depends on how proactively societies adapt through education and policy",
                        "explanation": "Bài viết nhấn mạnh kết quả phụ thuộc vào sự chủ động thích ứng chính sách và giáo dục."
                    }
                ]
            },
            {
                "passage_id": "b2-p2",
                "title": "Passage 2: The Global Transition Toward Decarbonized Renewable Energy",
                "topic": "Environment & Energy Transition",
                "content": "The global imperative to mitigate catastrophic climate change has catalyzed an unprecedented transition from fossil fuel dependency toward clean, renewable energy architectures. Over the past decade, technological innovation and massive industrial scaling have driven down the levelized cost of electricity (LCOE) for utility-scale solar photovoltaic systems and onshore wind turbines by 88% and 68% respectively, rendering renewable generation economically cheaper than new coal or natural gas facilities in most geographic markets.\n\nHowever, integrating intermittent renewable power sources into legacy national electric grids poses formidable engineering and infrastructural challenges. Because solar and wind generation depend inherently on diurnal cycles and meteorological fluctuations, grid operators must maintain dynamic grid stability when solar irradiance drops at sunset or during extended calm windless periods, known technically as 'dunkelflaute'. To prevent widespread blackouts, international utilities are deploying multi-faceted energy storage architectures, including utility-scale lithium-iron-phosphate (LFP) batteries, pumped hydroelectric reservoirs, and green hydrogen electrolysis plants.\n\nFurthermore, modernizing transmission corridors via high-voltage direct current (HVDC) power lines allows surplus renewable power generated in remote desert solar arrays or offshore wind farms to be transmitted thousands of kilometers with minimal transmission loss (under 3% per 1,000 km) to densely populated industrial metropolitan centers. Coupled with AI-driven predictive demand-response algorithms, smart grids dynamically balance supply and consumption in real time. Achieving global carbon neutrality by mid-century will require sustained geopolitical cooperation, streamlined environmental permitting, and substantial capital investment in electrical grid resilience.",
                "questions": [
                    {
                        "id": "B2_R11",
                        "question": "By what percentage has the levelized cost of solar photovoltaic electricity decreased over the past decade?",
                        "options": ["A. 25%", "B. 50%", "C. 68%", "D. 88%"],
                        "correct": "D. 88%",
                        "explanation": "Đoạn 1 nêu rõ: 'solar photovoltaic systems and onshore wind turbines by 88% and 68% respectively'."
                    },
                    {
                        "id": "B2_R12",
                        "question": "What economic milestone have solar and wind achieved in most markets?",
                        "options": [
                            "A. They are now economically cheaper than new coal or natural gas facilities",
                            "B. They require 100% government subsidies to survive",
                            "C. They have replaced all nuclear power plants",
                            "D. They are only feasible in equatorial nations"
                        ],
                        "correct": "A. They are now economically cheaper than new coal or natural gas facilities",
                        "explanation": "Đoạn 1: 'rendering renewable generation economically cheaper than new coal or natural gas facilities'."
                    },
                    {
                        "id": "B2_R13",
                        "question": "What is the primary technical challenge associated with solar and wind power?",
                        "options": [
                            "A. Their electricity is too powerful for home appliances",
                            "B. Their intermittent generation depends on weather and diurnal cycles",
                            "C. They emit dangerous radioactive smoke",
                            "D. They can only generate direct current that cannot be converted"
                        ],
                        "correct": "B. Their intermittent generation depends on weather and diurnal cycles",
                        "explanation": "Đoạn 2: 'Because solar and wind generation depend inherently on diurnal cycles and meteorological fluctuations'."
                    },
                    {
                        "id": "B2_R14",
                        "question": "The German meteorological term 'dunkelflaute' in paragraph 2 refers to:",
                        "options": [
                            "A. A sudden surge in ocean wave energy",
                            "B. Extended periods with minimal solar sunlight and calm windless conditions",
                            "C. High temperatures that damage solar panels",
                            "D. Extreme lightning storms"
                        ],
                        "correct": "B. Extended periods with minimal solar sunlight and calm windless conditions",
                        "explanation": "Đoạn 2: 'extended calm windless periods, known technically as dunkelflaute'."
                    },
                    {
                        "id": "B2_R15",
                        "question": "Which storage solutions are utilities deploying to balance grid fluctuations?",
                        "options": [
                            "A. Lead-acid car batteries only",
                            "B. LFP batteries, pumped hydroelectric reservoirs, and green hydrogen electrolysis",
                            "C. Burning extra diesel in residential basements",
                            "D. Storing electricity in giant underground magnets"
                        ],
                        "correct": "B. LFP batteries, pumped hydroelectric reservoirs, and green hydrogen electrolysis",
                        "explanation": "Đoạn 2 liệt kê: 'utility-scale lithium-iron-phosphate (LFP) batteries, pumped hydroelectric reservoirs, and green hydrogen electrolysis plants'."
                    },
                    {
                        "id": "B2_R16",
                        "question": "What key advantage do High-Voltage Direct Current (HVDC) lines offer?",
                        "options": [
                            "A. They are completely invisible to birds",
                            "B. They transmit electricity thousands of kilometers with minimal transmission loss (under 3% per 1,000 km)",
                            "C. They cost less than copper telephone wires",
                            "D. They produce potable drinking water"
                        ],
                        "correct": "B. They transmit electricity thousands of kilometers with minimal transmission loss (under 3% per 1,000 km)",
                        "explanation": "Đoạn 3: 'transmitted thousands of kilometers with minimal transmission loss (under 3% per 1,000 km)'."
                    },
                    {
                        "id": "B2_R17",
                        "question": "How do AI-driven smart grids contribute to grid stability?",
                        "options": [
                            "A. By shutting down power to factories randomly",
                            "B. By dynamically predicting demand and balancing supply and consumption in real time",
                            "C. By replacing all human electricians",
                            "D. By eliminating the need for power meters"
                        ],
                        "correct": "B. By dynamically predicting demand and balancing supply and consumption in real time",
                        "explanation": "Đoạn 3: 'AI-driven predictive demand-response algorithms, smart grids dynamically balance supply and consumption in real time'."
                    },
                    {
                        "id": "B2_R18",
                        "question": "The word 'imperative' in paragraph 1 is closest in meaning to:",
                        "options": ["A. Urgent necessity", "B. Optional luxury", "C. Minor suggestion", "D. Temporary obstacle"],
                        "correct": "A. Urgent necessity",
                        "explanation": "'Imperative' là nhu cầu cấp bách, mệnh lệnh bức thiết."
                    },
                    {
                        "id": "B2_R19",
                        "question": "The word 'mitigating' in paragraph 1 means:",
                        "options": ["A. Intensifying", "B. Alleviating or reducing the severity of", "C. Ignoring", "D. Creating"],
                        "correct": "B. Alleviating or reducing the severity of",
                        "explanation": "'Mitigate' có nghĩa là giảm thiểu tác hại, xoa dịu mức độ nghiêm trọng."
                    },
                    {
                        "id": "B2_R20",
                        "question": "What three factors are deemed essential for achieving mid-century carbon neutrality?",
                        "options": [
                            "A. Stopping all international trade, closing borders, and rationing electricity",
                            "B. Geopolitical cooperation, streamlined environmental permitting, and capital investment in grid resilience",
                            "C. Relocating all cities to desert regions",
                            "D. Relying exclusively on coal generation"
                        ],
                        "correct": "B. Geopolitical cooperation, streamlined environmental permitting, and capital investment in grid resilience",
                        "explanation": "Đoạn 3 kết luận: 'sustained geopolitical cooperation, streamlined environmental permitting, and substantial capital investment in electrical grid resilience'."
                    }
                ]
            },
            {
                "passage_id": "b2-p3",
                "title": "Passage 3: Behavioral Economics and the Psychology of Financial Choices",
                "topic": "Psychology & Behavioral Finance",
                "content": "Classical neoclassical economic models traditionally operated under the assumption of 'Homo economicus'—the theoretical rational actor who meticulously processes all available information, calculates probabilistic outcomes with mathematical precision, and consistently maximizes personal economic utility. However, the emergence of behavioral economics pioneered by psychologists Daniel Kahneman and Amos Tversky systematically dismantled this foundational premise, demonstrating that real human decision-making is profoundly influenced by cognitive heuristics, emotional impulses, and systematic cognitive biases.\n\nA central discovery of behavioral finance is 'Prospect Theory' and its corollary concept of 'loss aversion'. Empirical experiments repeatedly demonstrate that the psychological pain associated with losing $1,000 is approximately two to two-and-a-half times more intense than the emotional pleasure derived from gaining an identical sum of $1,000. This asymmetry causes retail investors to irrationally hold onto plummeting stocks in hopes of breaking even, while prematurely selling appreciating winning stocks to lock in modest gains—a destructive behavioral pattern known as the 'disposition effect'.\n\nAdditionally, humans frequently succumb to 'present bias', placing disproportionately higher value on immediate gratification over superior long-term welfare. This cognitive bias explains widespread inadequate retirement savings and chronic credit card debt accumulation across developed societies. By recognizing these innate cognitive vulnerabilities, modern behavioral architects design automated financial systems—such as 'Save More Tomorrow' programs that automatically escalate retirement savings rates with future annual salary raises—nudging individuals toward enduring financial security without feeling immediate loss of disposable income.",
                "questions": [
                    {
                        "id": "B2_R21",
                        "question": "What was the core assumption of classical neoclassical economic models?",
                        "options": [
                            "A. Humans are fundamentally emotional and unpredictable",
                            "B. Humans act as rational utility maximizers who process all information perfectly",
                            "C. Decisions are entirely controlled by social media",
                            "D. Financial markets always crash every five years"
                        ],
                        "correct": "B. Humans act as rational utility maximizers who process all information perfectly",
                        "explanation": "Đoạn 1 nêu giả định 'Homo economicus': 'theoretical rational actor who meticulously processes all available information... consistently maximizes personal economic utility'."
                    },
                    {
                        "id": "B2_R22",
                        "question": "Which two pioneering scholars systematically challenged classical rational choice theory?",
                        "options": [
                            "A. Sigmund Freud and Carl Jung",
                            "B. Daniel Kahneman and Amos Tversky",
                            "C. Isaac Newton and Albert Einstein",
                            "D. Bill Gates and Steve Jobs"
                        ],
                        "correct": "B. Daniel Kahneman and Amos Tversky",
                        "explanation": "Đoạn 1: 'pioneered by psychologists Daniel Kahneman and Amos Tversky'."
                    },
                    {
                        "id": "B2_R23",
                        "question": "According to loss aversion research, how much more intense is the psychological pain of losing money compared to gaining it?",
                        "options": ["A. Equal in intensity", "B. Two to two-and-a-half times more intense", "C. Ten times less intense", "D. Completely negligible"],
                        "correct": "B. Two to two-and-a-half times more intense",
                        "explanation": "Đoạn 2: 'pain associated with losing $1,000 is approximately two to two-and-a-half times more intense'."
                    },
                    {
                        "id": "B2_R24",
                        "question": "What investor mistake defines the 'disposition effect' in financial markets?",
                        "options": [
                            "A. Buying only government bonds",
                            "B. Holding declining stocks too long while selling winning stocks prematurely",
                            "C. Trading without an internet connection",
                            "D. Refusing to pay capital gains taxes"
                        ],
                        "correct": "B. Holding declining stocks too long while selling winning stocks prematurely",
                        "explanation": "Đoạn 2: 'retail investors to irrationally hold onto plummeting stocks in hopes of breaking even, while prematurely selling appreciating winning stocks'."
                    },
                    {
                        "id": "B2_R25",
                        "question": "What is 'present bias' as described in paragraph 3?",
                        "options": [
                            "A. Buying expensive birthday gifts for coworkers",
                            "B. Disproportionately valuing immediate gratification over long-term future welfare",
                            "C. Refusing to learn history",
                            "D. Only reading breaking news articles"
                        ],
                        "correct": "B. Disproportionately valuing immediate gratification over long-term future welfare",
                        "explanation": "Đoạn 3: 'placing disproportionately higher value on immediate gratification over superior long-term welfare'."
                    },
                    {
                        "id": "B2_R26",
                        "question": "Which real-world financial problem is directly linked to present bias?",
                        "options": [
                            "A. Insufficient retirement savings and chronic credit card debt",
                            "B. Excessive purchase of real estate insurance",
                            "C. High corporate tax rates",
                            "D. Shortage of physical paper currency"
                        ],
                        "correct": "A. Insufficient retirement savings and chronic credit card debt",
                        "explanation": "Đoạn 3: 'explains widespread inadequate retirement savings and chronic credit card debt accumulation'."
                    },
                    {
                        "id": "B2_R27",
                        "question": "How does the 'Save More Tomorrow' program overcome loss aversion?",
                        "options": [
                            "A. By confiscating 50% of current salary immediately",
                            "B. By automatically committing future salary raises to retirement savings",
                            "C. By banning credit cards for all employees",
                            "D. By offering lottery tickets instead of pensions"
                        ],
                        "correct": "B. By automatically committing future salary raises to retirement savings",
                        "explanation": "Đoạn 3: 'automatically escalate retirement savings rates with future annual salary raises... without feeling immediate loss of disposable income'."
                    },
                    {
                        "id": "B2_R28",
                        "question": "The word 'heuristics' in paragraph 1 refers to:",
                        "options": ["A. Mental shortcuts used in decision making", "B. Complex legal textbooks", "C. High-frequency trading supercomputers", "D. Government currency printing presses"],
                        "correct": "A. Mental shortcuts used in decision making",
                        "explanation": "'Heuristics' là các lối tắt tư duy, quy tắc kinh nghiệm giúp đưa ra quyết định nhanh."
                    },
                    {
                        "id": "B2_R29",
                        "question": "The word 'asymmetry' in paragraph 2 describes:",
                        "options": ["A. Perfect balance", "B. Lack of equality or equivalence between two sides", "C. High financial profit", "D. Random mathematical error"],
                        "correct": "B. Lack of equality or equivalence between two sides",
                        "explanation": "'Asymmetry' là sự bất đối xứng, không cân bằng giữa cảm giác đau đớn khi mất và niềm vui khi được."
                    },
                    {
                        "id": "B2_R30",
                        "question": "What is the broader implication of behavioral economics for policy design?",
                        "options": [
                            "A. Economic incentives never work under any circumstances",
                            "B. Systems should be designed to account for innate human cognitive limitations and biases",
                            "C. Governments should eliminate all private retirement accounts",
                            "D. Only artificial intelligence should be allowed to make financial decisions"
                        ],
                        "correct": "B. Systems should be designed to account for innate human cognitive limitations and biases",
                        "explanation": "Bài viết nhấn mạnh thiết kế hệ thống thông minh phù hợp với đặc điểm tâm lý tự nhiên của con người."
                    }
                ]
            },
            {
                "passage_id": "b2-p4",
                "title": "Passage 4: 21st Century Education and the Imperative of Lifelong Learning",
                "topic": "Education & Lifelong Learning",
                "content": "The contemporary global knowledge economy is defined by rapid technological obsolescence, where the half-life of technical professional skills has plummeted from thirty years in the mid-twentieth century to less than five years today. Consequently, the traditional front-loaded educational model—in which an individual completes formal schooling in their early twenties to sustain a lifelong career until retirement—is no longer viable. In its place, the paradigm of continuous, self-directed 'lifelong learning' has emerged as an indispensable prerequisite for professional relevance and economic mobility.\n\nModern pedagogies are undergoing a profound evolution from instructor-led didactic lecturing toward student-centered 'active learning' modalities. Project-based learning (PBL), problem-solving simulations, and inquiry-based peer instruction empower students to construct knowledge contextually rather than passively absorbing factual information. Furthermore, digital micro-credentials, modular online degree programs, and AI-powered adaptive tutoring platforms are democratizing access to high-caliber tertiary education, enabling working professionals to upskill flexibly without leaving full-time employment.\n\nNevertheless, the efficacy of lifelong learning depends fundamentally on metacognitive competence—the self-awareness of one's own learning processes, strengths, and knowledge deficits. Scholars emphasize that cultivating an agile 'growth mindset' allows individuals to view cognitive setbacks not as permanent deficiencies, but as actionable catalysts for deeper intellectual mastery. Educational institutions must therefore prioritize teaching learners 'how to learn', cultivating intellectual curiosity, digital literacy, and adaptive resilience to thrive amid the dynamic uncertainties of the 21st-century global landscape.",
                "questions": [
                    {
                        "id": "B2_R31",
                        "question": "What dramatic shift has occurred regarding the 'half-life' of technical skills?",
                        "options": [
                            "A. It increased from five years to thirty years",
                            "B. It decreased from thirty years in the 20th century to less than five years today",
                            "C. It has remained completely static",
                            "D. It only affects manual construction workers"
                        ],
                        "correct": "B. It decreased from thirty years in the 20th century to less than five years today",
                        "explanation": "Đoạn 1: 'the half-life of technical professional skills has plummeted from thirty years in the mid-twentieth century to less than five years today'."
                    },
                    {
                        "id": "B2_R32",
                        "question": "Why is the traditional front-loaded educational model no longer viable?",
                        "options": [
                            "A. Because universities have run out of classroom space",
                            "B. Because technical skills become obsolete quickly, requiring continuous upskilling throughout life",
                            "C. Because nobody wants to work after age thirty",
                            "D. Because tuition fees are completely illegal"
                        ],
                        "correct": "B. Because technical skills become obsolete quickly, requiring continuous upskilling throughout life",
                        "explanation": "Đoạn 1 nêu rõ sự lỗi thời nhanh chóng của kỹ năng đòi hỏi học tập suốt đời."
                    },
                    {
                        "id": "B2_R33",
                        "question": "What new educational paradigm has replaced the traditional model?",
                        "options": ["A. Compulsory early retirement", "B. Continuous, self-directed lifelong learning", "C. Purely oral storytelling", "D. Military conscription training"],
                        "correct": "B. Continuous, self-directed lifelong learning",
                        "explanation": "Đoạn 1: 'paradigm of continuous, self-directed lifelong learning has emerged as an indispensable prerequisite'."
                    },
                    {
                        "id": "B2_R34",
                        "question": "Which active learning modalities are mentioned in paragraph 2?",
                        "options": [
                            "A. Silent copying from blackboards",
                            "B. Project-based learning, problem-solving simulations, and peer instruction",
                            "C. Memorizing dictionary pages in order",
                            "D. Watching television without interaction"
                        ],
                        "correct": "B. Project-based learning, problem-solving simulations, and peer instruction",
                        "explanation": "Đoạn 2: 'Project-based learning (PBL), problem-solving simulations, and inquiry-based peer instruction'."
                    },
                    {
                        "id": "B2_R35",
                        "question": "How do digital micro-credentials and adaptive platforms benefit working professionals?",
                        "options": [
                            "A. They force professionals to resign from their jobs",
                            "B. They enable flexible upskilling without leaving full-time employment",
                            "C. They replace all physical libraries",
                            "D. They eliminate the need to take tests"
                        ],
                        "correct": "B. They enable flexible upskilling without leaving full-time employment",
                        "explanation": "Đoạn 2: 'enabling working professionals to upskill flexibly without leaving full-time employment'."
                    },
                    {
                        "id": "B2_R36",
                        "question": "What is 'metacognitive competence' as defined in paragraph 3?",
                        "options": [
                            "A. The ability to memorize 10,000 numbers",
                            "B. Self-awareness of one's own learning processes, strengths, and knowledge deficits",
                            "C. Speaking ten foreign languages simultaneously",
                            "D. Designing complex computer microchips"
                        ],
                        "correct": "B. Self-awareness of one's own learning processes, strengths, and knowledge deficits",
                        "explanation": "Đoạn 3: 'metacognitive competence—the self-awareness of one's own learning processes, strengths, and knowledge deficits'."
                    },
                    {
                        "id": "B2_R37",
                        "question": "How does a 'growth mindset' help individuals process cognitive setbacks?",
                        "options": [
                            "A. By viewing them as permanent proof of failure",
                            "B. By treating setbacks as actionable catalysts for deeper intellectual mastery",
                            "C. By blaming other people for mistakes",
                            "D. By avoiding all challenging tasks in the future"
                        ],
                        "correct": "B. By treating setbacks as actionable catalysts for deeper intellectual mastery",
                        "explanation": "Đoạn 3: 'view cognitive setbacks not as permanent deficiencies, but as actionable catalysts for deeper intellectual mastery'."
                    },
                    {
                        "id": "B2_R38",
                        "question": "The word 'obsolescence' in paragraph 1 is closest in meaning to:",
                        "options": ["A. Becoming outdated and no longer useful", "B. Rapid economic profitability", "C. Physical destruction by fire", "D. Extreme popularity"],
                        "correct": "A. Becoming outdated and no longer useful",
                        "explanation": "'Obsolescence' là tình trạng trở nên lỗi thời, lạc hậu."
                    },
                    {
                        "id": "B2_R39",
                        "question": "The word 'democratizing' in paragraph 2 implies:",
                        "options": ["A. Making access widely available and accessible to diverse populations", "B. Restricting entry to the wealthy elite", "C. Enforcing political voting tests", "D. Reducing quality standards to zero"],
                        "correct": "A. Making access widely available and accessible to diverse populations",
                        "explanation": "'Democratizing' nghĩa là bình dân hóa, mở rộng quyền tiếp cận công bằng cho đông đảo mọi người."
                    },
                    {
                        "id": "B2_R40",
                        "question": "What fundamental responsibility is assigned to 21st-century educational institutions?",
                        "options": [
                            "A. Guaranteeing government employment for all graduates",
                            "B. Teaching learners 'how to learn' and cultivating adaptive resilience",
                            "C. Eliminating all digital technologies from campuses",
                            "D. Focusing solely on sports athletic training"
                        ],
                        "correct": "B. Teaching learners 'how to learn' and cultivating adaptive resilience",
                        "explanation": "Đoạn 3 kết luận: 'prioritize teaching learners how to learn, cultivating intellectual curiosity, digital literacy, and adaptive resilience'."
                    }
                ]
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 3. KỸ NĂNG VIẾT (WRITING) – 2 TASKS – 60 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "writing": {
        "title": "Kỹ Năng Viết – CEFR B2 (Writing Assessment)",
        "time_min": 60,
        "tasks": [
            {
                "task_id": "B2_W1",
                "task_title": "Task 1: Formal Letter / Thư Đề Xuất Doanh Nghiệp (150 - 180 từ)",
                "prompt": "You are a project coordinator at a multinational company. Write a formal letter (150-180 words) to your Operations Director proposing a company-wide initiative to reduce single-use plastics and implement a comprehensive recycling program.\nIn your letter, you should:\n- Explain the environmental and brand reputation reasons for this initiative.\n- Detail three practical steps the company should take (e.g. reusable water stations, digital documentation, waste sorting bins).\n- Request a formal meeting next week to discuss the implementation budget and timeline.",
                "min_words": 150,
                "time_min": 25,
                "instructions": "Sử dụng văn phong trang trọng (Formal Register), cấu trúc câu phức và từ vựng B2 chuẩn mực.",
                "sample_high_score_answer": "Dear Mr. Richardson,\n\nI am writing to formally propose a comprehensive sustainability initiative aimed at eliminating single-use plastics and enhancing waste management across our corporate offices. In today's environmentally conscious commercial landscape, establishing proactive ecological standards not only mitigates environmental footprint but also substantially strengthens our corporate brand reputation among clients and prospective employees.\n\nTo achieve this objective effectively, I recommend three pragmatic measures. Firstly, we should install filtered water refill stations on every floor, alongside providing all staff with branded reusable stainless-steel bottles. Secondly, implementing digital document workflows will eliminate unnecessary paper consumption. Finally, introducing multi-compartment waste sorting bins in common cafeterias will ensure systematic recycling of organic and recyclable materials.\n\nI would welcome the opportunity to discuss the preliminary budget and rollout timeline with you in greater detail. Could we schedule a 30-minute meeting next Tuesday afternoon at your convenience?\n\nThank you for considering this proposal. I look forward to your positive response.\n\nYours sincerely,\nNguyen Minh Anh\nProject Coordinator",
                "rubric": {
                    "task_achievement": "Đáp ứng đầy đủ 3 yêu cầu: lý do môi trường/thương hiệu, 3 giải pháp cụ thể và đề nghị cuộc họp.",
                    "lexical_resource": "Từ vựng trang trọng phong phú (comprehensive sustainability initiative, pragmatic measures, brand reputation, rollout timeline).",
                    "grammatical_range": "Sử dụng câu phức, mệnh đề quan hệ và bị động thành thạo (aimed at eliminating, alongside providing, would welcome the opportunity)."
                }
            },
            {
                "task_id": "B2_W2",
                "task_title": "Task 2: Essay Nghị Luận Xã Hội (250 - 280 từ)",
                "prompt": "Some people believe that artificial intelligence will eventually replace human teachers in classrooms, while others argue that the human element in education can never be substituted by technology.\n\nWrite an academic essay (250-280 words) discussing both views and giving your own opinion. Support your arguments with specific reasons and relevant examples.",
                "min_words": 250,
                "time_min": 35,
                "instructions": "Cấu trúc bài luận 4 đoạn (Mở bài, 2 Thân bài phân tích 2 luồng quan điểm, Kết bài khẳng định lập trường).",
                "sample_high_score_answer": "The rapid advancement of artificial intelligence has sparked intense debate regarding its potential to revolutionize modern pedagogy, leading some to hypothesize that intelligent algorithms could eventually replace human educators. While AI undeniably possesses remarkable capabilities in personalized instruction, I firmly believe that the indispensable human elements of empathy, mentorship, and moral guidance ensure teachers will remain central to education.\n\nOn the one hand, proponents of AI integration highlight its unprecedented efficiency in delivering customized learning experiences. Adaptive learning platforms can instantly analyze vast datasets of student performance, pinpointing precise knowledge deficits and delivering tailored exercises at an optimal pace. Furthermore, automated grading systems relieve teachers of repetitive administrative burdens, such as evaluating standardized multiple-choice assessments. In remote or economically disadvantaged regions where qualified educators are scarce, AI tutors provide scalable, high-quality academic content around the clock.\n\nOn the other hand, education encompasses far more than the mere transmission of cognitive data. Human teachers serve as compassionate mentors who recognize emotional distress, cultivate self-confidence, and inspire intellectual curiosity. An algorithm cannot perceive subtle non-verbal cues of anxiety, nor can it model ethical character and collaborative negotiation in the vibrant social setting of a classroom. When students encounter profound personal setbacks, it is a teacher's empathetic encouragement—rather than algorithmic feedback—that fosters emotional resilience and lifelong character development.\n\nIn conclusion, although artificial intelligence will undoubtedly serve as a powerful pedagogical tool that enhances educational efficiency, it should complement rather than substitute human educators. The future of education lies in harmonious synergy, where technology optimizes data analytics while human teachers nurture the heart and soul of learning.",
                "rubric": {
                    "task_response": "Phân tích trọn vẹn 2 quan điểm và bảo vệ lập trường cá nhân thuyết phục.",
                    "cohesion_coherence": "Chuyển ý tự nhiên, logic chặt chẽ (On the one hand, Furthermore, On the other hand, In conclusion).",
                    "lexical_resource": "Vốn từ học thuật C1/B2 xuất sắc (revolutionize modern pedagogy, tailored exercises, transmission of cognitive data, harmonious synergy)."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 4. KỸ NĂNG NÓI (SPEAKING) – 3 PARTS – 14 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "speaking": {
        "title": "Kỹ Năng Nói – CEFR B2 (Speaking Interview)",
        "time_min": 14,
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Tương Tác Xã Hội & Nghề Nghiệp (3 - 4 phút)",
                "description": "Giám khảo hỏi các câu hỏi về công việc, ngành học, thói quen đọc sách và kế hoạch phát triển bản thân.",
                "questions": [
                    {
                        "id": "B2_S1",
                        "question": "What career path are you pursuing, and what essential skills are required in your field?",
                        "audio_prompt": "Could you please tell me about your chosen career path and the key skills needed to succeed in your field?",
                        "sample_answer": "I am currently pursuing a career in software engineering and data analytics. Beyond technical proficiencies like Python programming and database architecture, success in this field requires strong analytical problem-solving, adaptability to rapidly evolving technologies, and collaborative communication skills to work effectively in cross-functional agile teams."
                    },
                    {
                        "id": "B2_S2",
                        "question": "How do digital media and social networks influence the way people consume information today?",
                        "audio_prompt": "In your view, how have digital media and social networks changed how people consume information?",
                        "sample_answer": "Digital media has democratized information dissemination, providing instant global access to breaking news and diverse perspectives. However, it has also shortened human attention spans and created algorithmic echo chambers, where individuals are rarely exposed to opposing viewpoints, making critical media literacy more crucial than ever before."
                    },
                    {
                        "id": "B2_S3",
                        "question": "Do you prefer studying or working independently, or as part of a collaborative team?",
                        "audio_prompt": "Do you generally prefer working independently, or do you thrive more in a collaborative team setting?",
                        "sample_answer": "While independent work provides deep focus for complex intellectual tasks, I genuinely thrive in collaborative teams. Brainstorming with diverse colleagues sparks innovative ideas that an individual might overlook, and collective problem-solving distributes cognitive workload while accelerating project delivery."
                    }
                ]
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Thảo Luận Giải Pháp & So Sánh Tình Huống (4 - 5 phút)",
                "description": "Thí sinh nhận một tình huống thực tế (ví dụ: công ty giải quyết vấn đề rác thải nhựa hoặc trường học thúc đẩy đọc sách) và so sánh 3 giải pháp đề xuất.",
                "questions": [
                    {
                        "id": "B2_S4",
                        "topic": "Workplace Sustainability Solutions",
                        "question": "A business wants to encourage its workforce to adopt eco-friendly commuting habits. Compare three options: offering free public transit passes, organizing carpooling incentives, or subsidizing electric bicycles. Which is the most effective strategy?",
                        "audio_prompt": "A company wants to promote eco-friendly commuting. Compare free transit passes, carpooling incentives, and electric bicycle subsidies. Which option do you consider most effective?",
                        "sample_answer": "While all three proposals offer distinct ecological merits, subsidizing electric bicycles and providing free public transit passes stand out as the most impactful. Electric bicycles provide flexible point-to-point urban mobility while promoting physical cardiovascular health, especially for employees living within a 10-kilometer radius. However, for workers commuting from distant suburban areas, fully subsidized public transit passes represent the most universally accessible and scalable solution. Therefore, a hybrid approach offering employees a choice between a transit pass or a bike subsidy would achieve the highest participation rate and maximize corporate carbon reduction."
                    }
                ]
            },
            {
                "part_id": 3,
                "part_title": "Part 3: Phát Triển Chủ Đề & Phản Biện Chuyên Sâu (5 - 6 phút)",
                "description": "Thí sinh phát triển một Mindmap chủ đề học thuật và trả lời các câu hỏi phản biện mở rộng từ giám khảo.",
                "questions": [
                    {
                        "id": "B2_S5",
                        "topic": "The Impact of Remote Work on Modern Society",
                        "question": "Discuss the socio-economic impacts of remote work. How does it influence employee productivity, urban real estate, and work-life balance?",
                        "audio_prompt": "Let's discuss the broader impact of remote work. How does it reshape employee productivity, urban real estate, and personal work-life balance?",
                        "sample_answer": "Remote work has catalyzed a fundamental paradigm shift in modern employment. In terms of employee productivity, eliminating long daily commutes saves hours of stressful travel, allowing professionals to allocate more uninterrupted focus to high-value tasks. Economically, reduced demand for centralized corporate offices is prompting city planners to convert commercial skyscrapers into mixed-use residential housing, which revitalizes suburban neighborhoods. On the personal level, while remote work provides unprecedented flexibility to manage family responsibilities, it also risks blurring the boundaries between professional duties and personal downtime. To sustain long-term mental well-being, companies and individuals must establish clear digital boundaries to prevent burnout."
                    }
                ]
            }
        ]
    }
}
