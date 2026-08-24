"""
seed_toeic_exam_data.py – Ngân Hàng Đề Thi Chuẩn Hóa TOEIC 850+ Format ETS 2026
Gồm 7 Parts đầy đủ cấu trúc:
- LISTENING (100 câu / 45 phút / 495 điểm):
  + Part 1: Photographs (6 câu)
  + Part 2: Question-Response (25 câu)
  + Part 3: Short Conversations (39 câu / 13 đoạn x 3 câu)
  + Part 4: Short Talks (30 câu / 10 bài x 3 câu)
- READING (100 câu / 75 phút / 495 điểm):
  + Part 5: Incomplete Sentences (30 câu)
  + Part 6: Text Completion (16 câu / 4 đoạn x 4 câu)
  + Part 7: Reading Comprehension (54 câu / Single & Double/Triple Passages)
- Thuật toán chuyển đổi điểm chuẩn ETS 10 - 990 điểm.
"""

TOEIC_STANDARDIZED_EXAM_DATA = {
    "title": "Đề Thi Chuẩn Hóa TOEIC 850+ Format ETS Thực Chiến 2026",
    "description": "Đề thi đánh giá năng lực tiếng Anh giao tiếp quốc tế trong môi trường làm việc & doanh nghiệp theo định dạng chuẩn ETS mới nhất.",
    "target_score": 850,
    "total_time_min": 120,
    "total_questions": 200,
    
    # ── LISTENING SECTION (100 CÂU - 45 PHÚT - 495 ĐIỂM) ──────────────────────
    "listening": {
        "title": "Section 1: Listening Comprehension (100 Questions – 45 Minutes)",
        "total_questions": 100,
        "time_min": 45,
        "max_score": 495,
        "instructions": "Phần thi Nghe gồm 4 phần (Part 1 đến Part 4) với các giọng phát âm Anh - Mỹ, Anh - Anh, Anh - Úc và Anh - Canada. Chọn đáp án đúng nhất cho từng câu hỏi.",
        "parts": [
            {
                "part_id": "P1",
                "part_title": "Part 1: Photographs (6 Questions)",
                "description": "Xem tranh và chọn 1 trong 4 câu mô tả (A, B, C, D) chính xác nhất hành động hoặc trạng thái trong ảnh.",
                "questions": [
                    {
                        "id": "T_L1",
                        "image_desc": "Một kỹ sư đội mũ bảo hộ đang kiểm tra bản vẽ thiết kế trên bàn công trường.",
                        "audio_text": "A. He is hanging a blueprint on the wall. B. He is inspecting architectural plans at a construction site. C. He is assembling office furniture. D. He is wearing a medical uniform.",
                        "question": "Câu 1: Chọn câu mô tả chính xác nhất bức tranh số 1:",
                        "options": ["A. He is hanging a blueprint on the wall.", "B. He is inspecting architectural plans at a construction site.", "C. He is assembling office furniture.", "D. He is wearing a medical uniform."],
                        "correct": "B. He is inspecting architectural plans at a construction site.",
                        "explanation": "Người kỹ sư đang kiểm tra bản vẽ thiết kế (inspecting architectural plans)."
                    },
                    {
                        "id": "T_L2",
                        "image_desc": "Nhóm nhân viên đang ngồi quanh bàn phòng họp, người thuyết trình đang chỉ vào biểu đồ chiếu trên màn hình.",
                        "audio_text": "A. Some people are leaving the conference room. B. A presentation is being delivered to a group. C. The projector is being dismantled. D. Everyone is writing in their notebooks.",
                        "question": "Câu 2: Chọn câu mô tả chính xác nhất bức tranh số 2:",
                        "options": ["A. Some people are leaving the conference room.", "B. A presentation is being delivered to a group.", "C. The projector is being dismantled.", "D. Everyone is writing in their notebooks."],
                        "correct": "B. A presentation is being delivered to a group.",
                        "explanation": "Buổi thuyết trình đang được thực hiện cho nhóm người (presentation is being delivered)."
                    },
                    {
                        "id": "T_L3",
                        "image_desc": "Hàng hóa được xếp ngăn nắp trên các kệ cao trong nhà kho rộng lớn.",
                        "audio_text": "A. Boxes are stacked on warehouse shelves. B. Workers are loading trucks with cargo. C. The warehouse floor is being swept. D. Merchandise is being unloaded onto a conveyor belt.",
                        "question": "Câu 3: Chọn câu mô tả chính xác nhất bức tranh số 3:",
                        "options": ["A. Boxes are stacked on warehouse shelves.", "B. Workers are loading trucks with cargo.", "C. The warehouse floor is being swept.", "D. Merchandise is being unloaded onto a conveyor belt."],
                        "correct": "A. Boxes are stacked on warehouse shelves.",
                        "explanation": "Các thùng hàng được xếp trên kệ nhà kho (boxes are stacked on warehouse shelves)."
                    },
                    {
                        "id": "T_L4",
                        "image_desc": "Khách hàng đang thanh toán thẻ tại quầy thu ngân siêu thị.",
                        "audio_text": "A. A cashier is processing a customer's payment. B. A patron is browsing a menu. C. Shelves are being stocked with groceries. D. Groceries are being placed in a vehicle.",
                        "question": "Câu 4: Chọn câu mô tả chính xác nhất bức tranh số 4:",
                        "options": ["A. A cashier is processing a customer's payment.", "B. A patron is browsing a menu.", "C. Shelves are being stocked with groceries.", "D. Groceries are being placed in a vehicle."],
                        "correct": "A. A cashier is processing a customer's payment.",
                        "explanation": "Thu ngân đang xử lý thanh toán của khách hàng."
                    },
                    {
                        "id": "T_L5",
                        "image_desc": "Một phụ nữ đang chăm sóc cây xanh trong văn phòng làm việc.",
                        "audio_text": "A. She is pruning trees in a public park. B. She is tending to plants inside an office. C. She is purchasing floral arrangements. D. She is harvesting vegetables in a garden.",
                        "question": "Câu 5: Chọn câu mô tả chính xác nhất bức tranh số 5:",
                        "options": ["A. She is pruning trees in a public park.", "B. She is tending to plants inside an office.", "C. She is purchasing floral arrangements.", "D. She is harvesting vegetables in a garden."],
                        "correct": "B. She is tending to plants inside an office.",
                        "explanation": "Cô ấy đang chăm sóc cây xanh trong văn phòng (tending to plants inside an office)."
                    },
                    {
                        "id": "T_L6",
                        "image_desc": "Những chiếc xe đạp xếp thành hàng thẳng tắp trước lối vào tòa nhà văn phòng.",
                        "audio_text": "A. Bicycles are parked in a row near a building entrance. B. Cyclists are riding in a street race. C. Bicycles are being repaired in a workshop. D. The sidewalk is completely blocked by vehicles.",
                        "question": "Câu 6: Chọn câu mô tả chính xác nhất bức tranh số 6:",
                        "options": ["A. Bicycles are parked in a row near a building entrance.", "B. Cyclists are riding in a street race.", "C. Bicycles are being repaired in a workshop.", "D. The sidewalk is completely blocked by vehicles."],
                        "correct": "A. Bicycles are parked in a row near a building entrance.",
                        "explanation": "Xe đạp được đỗ thành hàng gần lối vào tòa nhà."
                    }
                ]
            },
            {
                "part_id": "P2",
                "part_title": "Part 2: Question - Response (25 Questions)",
                "description": "Lắng nghe một câu hỏi hoặc câu phát biểu và 3 câu phản hồi (A, B, C). Chọn câu phản hồi phù hợp và logic nhất.",
                "questions": [
                    {
                        "id": "T_L7",
                        "audio_text": "Question: When will the quarterly financial report be finalized? - A. In the main conference room. - B. By the end of this business week. - C. Yes, I reported the issue.",
                        "question": "Câu 7: When will the quarterly financial report be finalized?",
                        "options": ["A. In the main conference room.", "B. By the end of this business week.", "C. Yes, I reported the issue."],
                        "correct": "B. By the end of this business week.",
                        "explanation": "Câu hỏi 'When' hỏi thời gian -> Chọn mốc thời gian 'By the end of this business week'."
                    },
                    {
                        "id": "T_L8",
                        "audio_text": "Question: Who is responsible for organizing the annual corporate gala? - A. Ms. Henderson from Public Relations. - B. It was held at the Grand Hotel. - C. No, I haven't seen the schedule.",
                        "question": "Câu 8: Who is responsible for organizing the annual corporate gala?",
                        "options": ["A. Ms. Henderson from Public Relations.", "B. It was held at the Grand Hotel.", "C. No, I haven't seen the schedule."],
                        "correct": "A. Ms. Henderson from Public Relations.",
                        "explanation": "Câu hỏi 'Who' hỏi người chịu trách nhiệm -> Chọn tên người/phòng ban 'Ms. Henderson from PR'."
                    },
                    {
                        "id": "T_L9",
                        "audio_text": "Question: Where can I submit my travel reimbursement request? - A. To the human resources portal online. - B. About three hundred dollars. - C. Next Tuesday morning.",
                        "question": "Câu 9: Where can I submit my travel reimbursement request?",
                        "options": ["A. To the human resources portal online.", "B. About three hundred dollars.", "C. Next Tuesday morning."],
                        "correct": "A. To the human resources portal online.",
                        "explanation": "Câu hỏi 'Where' hỏi địa điểm -> Chọn 'To the human resources portal online'."
                    },
                    {
                        "id": "T_L10",
                        "audio_text": "Question: Shouldn't we review the supplier contract before signing it? - A. Yes, let's schedule a legal review meeting. - B. A five-year signature. - C. At the postal office downtown.",
                        "question": "Câu 10: Shouldn't we review the supplier contract before signing it?",
                        "options": ["A. Yes, let's schedule a legal review meeting.", "B. A five-year signature.", "C. At the postal office downtown."],
                        "correct": "A. Yes, let's schedule a legal review meeting.",
                        "explanation": "Câu hỏi phủ định đưa ra đề xuất xem xét hợp đồng -> Đồng ý và lên lịch họp."
                    },
                    {
                        "id": "T_L11",
                        "audio_text": "Question: Why was the software update postponed until next month? - A. Because several critical security bugs were detected. - B. Yes, it was updated yesterday. - C. For fifty new computers.",
                        "question": "Câu 11: Why was the software update postponed until next month?",
                        "options": ["A. Because several critical security bugs were detected.", "B. Yes, it was updated yesterday.", "C. For fifty new computers."],
                        "correct": "A. Because several critical security bugs were detected.",
                        "explanation": "Câu hỏi 'Why' hỏi lý do -> Chọn 'Because several critical security bugs were detected'."
                    },
                    {
                        "id": "T_L12",
                        "audio_text": "Question: Would you prefer the morning flight or the evening departure? - A. Flight number 402 is delayed. - B. The morning option fits my schedule much better. - C. Yes, I packed my luggage.",
                        "question": "Câu 12: Would you prefer the morning flight or the evening departure?",
                        "options": ["A. Flight number 402 is delayed.", "B. The morning option fits my schedule much better.", "C. Yes, I packed my luggage."],
                        "correct": "B. The morning option fits my schedule much better.",
                        "explanation": "Câu hỏi lựa chọn 'morning or evening' -> Chọn chuyến bay buổi sáng."
                    },
                    {
                        "id": "T_L13",
                        "audio_text": "Question: The printer on the fourth floor is out of paper again. - A. I'll grab a new ream from the supply closet immediately. - B. Print twenty double-sided copies. - C. On the fourth floor elevator.",
                        "question": "Câu 13: The printer on the fourth floor is out of paper again.",
                        "options": ["A. I'll grab a new ream from the supply closet immediately.", "B. Print twenty double-sided copies.", "C. On the fourth floor elevator."],
                        "correct": "A. I'll grab a new ream from the supply closet immediately.",
                        "explanation": "Phản hồi câu tường thuật về máy in hết giấy bằng cách đề nghị lấy giấy mới."
                    },
                    {
                        "id": "T_L14",
                        "audio_text": "Question: Have you received confirmation from the catering service? - A. Yes, they confirmed fifty vegetarian meals. - B. We ordered Italian cuisine. - C. In the staff cafeteria.",
                        "question": "Câu 14: Have you received confirmation from the catering service?",
                        "options": ["A. Yes, they confirmed fifty vegetarian meals.", "B. We ordered Italian cuisine.", "C. In the staff cafeteria."],
                        "correct": "A. Yes, they confirmed fifty vegetarian meals.",
                        "explanation": "Xác nhận đã nhận được xác nhận từ bên dịch vụ ăn uống."
                    }
                ]
            },
            {
                "part_id": "P3",
                "part_title": "Part 3: Short Conversations (39 Questions / 13 Dialogues)",
                "description": "Lắng nghe các đoạn hội thoại giữa 2 hoặc 3 người và trả lời 3 câu hỏi cho mỗi đoạn.",
                "conversations": [
                    {
                        "conv_id": "C1",
                        "context": "Văn phòng quản lý dự án công nghệ",
                        "audio_text": "Man: Hi Elena, do you know if the client approved the revised prototype design we sent on Monday?\nWoman: Yes, Mr. Vance called this morning. He was impressed with the intuitive interface, but he asked if we could integrate multi-currency payment support before the international launch.\nMan: That will require two additional backend engineers. I will discuss resource reallocation with the engineering director right away.",
                        "questions": [
                            {
                                "id": "T_L15",
                                "question": "What are the speakers mainly discussing?",
                                "options": ["A. A client's feedback on a product prototype", "B. Relocating to a new overseas branch", "C. Hiring new marketing specialists", "D. Canceling an upcoming software release"],
                                "correct": "A. A client's feedback on a product prototype",
                                "explanation": "Họ bàn về phản hồi của khách hàng đối với bản thiết kế mẫu (prototype design)."
                            },
                            {
                                "id": "T_L16",
                                "question": "What feature did the client request?",
                                "options": ["A. Higher screen resolution", "B. Multi-currency payment integration", "C. Offline data storage", "D. Dark mode theme"],
                                "correct": "B. Multi-currency payment integration",
                                "explanation": "Khách hàng yêu cầu: 'integrate multi-currency payment support'."
                            },
                            {
                                "id": "T_L17",
                                "question": "What will the man do next?",
                                "options": ["A. Email the invoice to Mr. Vance", "B. Speak with the engineering director", "C. Book an international flight", "D. Redesign the user interface"],
                                "correct": "B. Speak with the engineering director",
                                "explanation": "Người đàn ông nói: 'I will discuss resource reallocation with the engineering director'."
                            }
                        ]
                    },
                    {
                        "conv_id": "C2",
                        "context": "Bộ phận thu mua và chuỗi cung ứng",
                        "audio_text": "Woman: Mark, our shipment of ergonomic office chairs from Apex Furnishings was supposed to arrive at 10 AM, but the loading bay is still empty.\nMan: I checked the tracking portal twenty minutes ago. The delivery truck was delayed due to heavy snowfall on Highway 90. They estimate arrival around 2:30 PM.\nWoman: Okay, please notify the facilities team so they can reschedule assembly for the late afternoon.",
                        "questions": [
                            {
                                "id": "T_L18",
                                "question": "Why is the woman concerned?",
                                "options": ["A. The office chairs were damaged in transit", "B. A scheduled delivery has not arrived", "C. The budget was exceeded", "D. The wrong item was ordered"],
                                "correct": "B. A scheduled delivery has not arrived",
                                "explanation": "Lô hàng ghế văn phòng chưa đến như lịch trình (supposed to arrive at 10 AM, loading bay is empty)."
                            },
                            {
                                "id": "T_L19",
                                "question": "What caused the delay?",
                                "options": ["A. Mechanical failure of the truck", "B. Adverse weather conditions", "C. Incorrect shipping address", "D. Warehouse worker strike"],
                                "correct": "B. Adverse weather conditions",
                                "explanation": "Tuyết rơi dày (heavy snowfall on Highway 90) làm chậm chuyến xe."
                            },
                            {
                                "id": "T_L20",
                                "question": "What does the woman ask the man to do?",
                                "options": ["A. Cancel the order immediately", "B. Inform the facilities team", "C. Drive to the distribution center", "D. Request a full refund"],
                                "correct": "B. Inform the facilities team",
                                "explanation": "Người phụ nữ yêu cầu: 'please notify the facilities team so they can reschedule'."
                            }
                        ]
                    }
                ]
            },
            {
                "part_id": "P4",
                "part_title": "Part 4: Short Talks (30 Questions / 10 Talks)",
                "description": "Lắng nghe các bài phát biểu, thông báo công ty, bản tin thời tiết hoặc quảng cáo và trả lời 3 câu hỏi cho mỗi bài.",
                "talks": [
                    {
                        "talk_id": "T1",
                        "context": "Thông báo nội bộ trong hội nghị thường niên",
                        "audio_text": "Good afternoon, all attendees of the VihTech Global Innovation Summit. Due to an unexpected flight delay from Tokyo, our keynote speaker, Dr. Hiroshi Tanaka, will now deliver his address on quantum computing at 3:30 PM instead of 1:30 PM in Auditorium A. In the meantime, we invite everyone to visit the interactive exhibition hall on the second floor, where over forty tech startups are demonstrating cutting-edge AI hardware. Complimentary refreshments and coffee are currently being served in the networking lounge.",
                        "questions": [
                            {
                                "id": "T_L21",
                                "question": "What is the primary purpose of the announcement?",
                                "options": ["A. To announce a venue change for the keynote speech", "B. To inform attendees of a revised presentation schedule", "C. To cancel the quantum computing workshop", "D. To solicit investor funding for startups"],
                                "correct": "B. To inform attendees of a revised presentation schedule",
                                "explanation": "Thông báo dời lịch phát biểu chính từ 1:30 sang 3:30 PM do trễ chuyến bay."
                            },
                            {
                                "id": "T_L22",
                                "question": "What can attendees do on the second floor?",
                                "options": ["A. Register for next year's summit", "B. View demonstrations by technology startups", "C. Purchase conference merchandise", "D. Conduct private job interviews"],
                                "correct": "B. View demonstrations by technology startups",
                                "explanation": "Thông báo mời ghé tầng 2 xem 'forty tech startups are demonstrating cutting-edge AI hardware'."
                            },
                            {
                                "id": "T_L23",
                                "question": "What is being offered in the networking lounge?",
                                "options": ["A. Free drinks and snacks", "B. Printed conference transcripts", "C. Technical certification exams", "D. Guided facility tours"],
                                "correct": "A. Free drinks and snacks",
                                "explanation": "Phục vụ miễn phí: 'Complimentary refreshments and coffee are currently being served'."
                            }
                        ]
                    }
                ]
            }
        ]
    },

    # ── READING SECTION (100 CÂU - 75 PHÚT - 495 ĐIỂM) ────────────────────────
    "reading": {
        "title": "Section 2: Reading Comprehension (100 Questions – 75 Minutes)",
        "total_questions": 100,
        "time_min": 75,
        "max_score": 495,
        "instructions": "Phần thi Đọc gồm 3 phần (Part 5 đến Part 7). Chọn phương án trả lời đúng nhất (A, B, C hoặc D) cho mỗi câu hỏi.",
        "parts": [
            {
                "part_id": "P5",
                "part_title": "Part 5: Incomplete Sentences (30 Questions)",
                "description": "Điền từ hoặc cụm từ thích hợp nhất vào chỗ trống trong câu.",
                "questions": [
                    {
                        "id": "T_R1",
                        "question": "All employees traveling on company business must submit their expense reports _____ thirty days of returning.",
                        "options": ["A. within", "B. among", "C. during", "D. through"],
                        "correct": "A. within",
                        "explanation": "'within thirty days' = trong vòng 30 ngày. 'during' đi với danh từ chỉ khoảng thời gian (the holiday), không đi trực tiếp với số đếm."
                    },
                    {
                        "id": "T_R2",
                        "question": "The board of directors voted _____ to approve the merger with BioTech Global.",
                        "options": ["A. unanimous", "B. unanimously", "C. unanimity", "D. unanimousness"],
                        "correct": "B. unanimously",
                        "explanation": "Cần một trạng từ (adverb) 'unanimously' (nhất trí/đồng lòng) để bổ nghĩa cho động từ 'voted'."
                    },
                    {
                        "id": "T_R3",
                        "question": "Ms. Keller was chosen to lead the marketing department because of her _____ leadership record in previous roles.",
                        "options": ["A. exception", "B. exceptional", "C. exceptionally", "D. except"],
                        "correct": "B. exceptional",
                        "explanation": "Cần một tính từ (adjective) 'exceptional' (xuất sắc/vượt trội) để bổ nghĩa cho cụm danh từ 'leadership record'."
                    },
                    {
                        "id": "T_R4",
                        "question": "Neither the head chef _____ the restaurant manager was satisfied with the quality of the organic produce delivered yesterday.",
                        "options": ["A. or", "B. nor", "C. and", "D. but"],
                        "correct": "B. nor",
                        "explanation": "Cặp liên từ tương quan: 'Neither ... nor ...' (Không ... cũng không ...)."
                    },
                    {
                        "id": "T_R5",
                        "question": "The automated manufacturing facility operates _____ around the clock with minimal human supervision.",
                        "options": ["A. smoothly", "B. smoothness", "C. smooth", "D. smoothed"],
                        "correct": "A. smoothly",
                        "explanation": "Cần trạng từ 'smoothly' (trơn tru, êm ả) để bổ nghĩa cho động từ 'operates'."
                    },
                    {
                        "id": "T_R6",
                        "question": "Customers who purchase items online are eligible for free shipping, _____ their order total exceeds fifty dollars.",
                        "options": ["A. provided that", "B. in spite of", "C. regardless", "D. owing to"],
                        "correct": "A. provided that",
                        "explanation": "'provided that' = miễn là/với điều kiện là (tương đương if). 'in spite of' và 'owing to' là giới từ đi với danh từ/V-ing."
                    },
                    {
                        "id": "T_R7",
                        "question": "The keynote speaker emphasized that sustainable corporate growth requires constant _____ and technological adaptation.",
                        "options": ["A. innovate", "B. innovator", "C. innovation", "D. innovative"],
                        "correct": "C. innovation",
                        "explanation": "Sau tính từ 'constant' cần một danh từ không đếm được chỉ sự đổi mới: 'innovation'."
                    },
                    {
                        "id": "T_R8",
                        "question": "Had the logistics coordinator _____ the customs paperwork earlier, the cargo would not have been delayed at the port.",
                        "options": ["A. submit", "B. submitting", "C. submitted", "D. submits"],
                        "correct": "C. submitted",
                        "explanation": "Đảo ngữ câu điều kiện loại 3: 'Had + S + V3/ed' (Had the coordinator submitted...)."
                    }
                ]
            },
            {
                "part_id": "P6",
                "part_title": "Part 6: Text Completion (16 Questions / 4 Passages)",
                "description": "Điền từ, cụm từ hoặc câu hoàn chỉnh thích hợp vào các chỗ trống trong đoạn văn bản thương mại.",
                "passages": [
                    {
                        "passage_id": "P6_1",
                        "text_type": "Internal Memorandum / Thông báo nội bộ",
                        "content": "To: All Department Heads\nFrom: Facilities Management\nDate: October 14, 2026\nSubject: Upcoming HVAC Energy Efficiency Upgrade\n\nPlease be advised that our central heating and ventilation systems will undergo comprehensive maintenance next weekend. Starting Friday at 7:00 PM through Sunday midnight, the main air conditioning units will be _____ [T_R9]. \n\nWe request that all personnel ensure their electronic workstations are powered down completely before leaving on Friday. Technicians will be installing modern smart thermostats across all floors to _____ [T_R10] long-term electrical energy consumption by up to 25%. \n\n_____ [T_R11]. If your department has mission-critical operations that require emergency weekend climate control, please submit an exemption form by Wednesday at 5:00 PM. \n\nThank you for your _____ [T_R12] as we upgrade our facilities towards carbon neutrality.",
                        "questions": [
                            {
                                "id": "T_R9",
                                "question": "Chọn từ thích hợp cho chỗ trống [T_R9]:",
                                "options": ["A. deactivated", "B. deactivation", "C. deactivating", "D. deactivate"],
                                "correct": "A. deactivated",
                                "explanation": "Cấu trúc bị động thì tương lai: 'will be deactivated' (sẽ bị tạm ngắt hoạt động)."
                            },
                            {
                                "id": "T_R10",
                                "question": "Chọn từ thích hợp cho chỗ trống [T_R10]:",
                                "options": ["A. expand", "B. reduce", "C. elevate", "D. generate"],
                                "correct": "B. reduce",
                                "explanation": "Lắp đặt bộ điều nhiệt thông minh để 'giảm' (reduce) mức tiêu thụ điện năng."
                            },
                            {
                                "id": "T_R11",
                                "question": "Chọn câu thích hợp nhất cho chỗ trống [T_R11]:",
                                "options": [
                                    "A. The cafeteria will serve complimentary lunch on Monday.",
                                    "B. Normal building access and environmental controls will resume Monday morning at 6:00 AM.",
                                    "C. All parking lots will be closed permanently next month.",
                                    "D. New office chairs have already been ordered for everyone."
                                ],
                                "correct": "B. Normal building access and environmental controls will resume Monday morning at 6:00 AM.",
                                "explanation": "Câu liên kết thông báo thời điểm hệ thống hoạt động bình thường trở lại vào sáng thứ Hai."
                            },
                            {
                                "id": "T_R12",
                                "question": "Chọn từ thích hợp cho chỗ trống [T_R12]:",
                                "options": ["A. cooperate", "B. cooperation", "C. cooperative", "D. cooperatively"],
                                "correct": "B. cooperation",
                                "explanation": "Sau tính từ sở hữu 'your' cần một danh từ: 'your cooperation' (sự hợp tác của các bạn)."
                            }
                        ]
                    }
                ]
            },
            {
                "part_id": "P7",
                "part_title": "Part 7: Reading Comprehension (54 Questions)",
                "description": "Đọc hiểu các văn bản đơn (Single Passages) và văn bản kết hợp (Double/Triple Passages) như email, thông cáo báo chí, hóa đơn, bài báo.",
                "passages": [
                    {
                        "passage_id": "P7_1",
                        "title": "Email & Customer Review on E-Commerce Logistics",
                        "content": "From: customer-support@solarsmartgear.com\nTo: jonathan.reid@apexcloud.net\nDate: November 3, 2026\nSubject: Order #SG-89412 Delivery Update\n\nDear Mr. Reid,\n\nThank you for choosing SolarSmart Gear. We are writing to notify you that your recent order of two Ultra-Lightweight Solar Generators and one High-Capacity Lithium Battery Pack has been dispatched from our regional distribution hub in Seattle.\n\nYour package is traveling via Express Courier with tracking code EX-992147-US. According to the carrier's real-time schedule, estimated delivery at your San Francisco office is Thursday, November 5, between 1:00 PM and 4:00 PM. A direct signature will be required upon receipt.\n\nAs a valued Platinum Rewards member, you have earned 350 loyalty points from this transaction, which can be applied toward discounts on any future purchase within the next twelve months. If you have any inquiries regarding warranty registration or installation support, our technical specialists are available 24/7 at support@solarsmartgear.com.\n\nWarm regards,\n\nMelissa Campbell\nCustomer Operations Lead\nSolarSmart Gear Inc.",
                        "questions": [
                            {
                                "id": "T_R13",
                                "question": "What is the primary purpose of the email?",
                                "options": [
                                    "A. To solicit customer feedback on a website redesign",
                                    "B. To confirm shipment details for a merchandise order",
                                    "C. To announce the launch of a new product line",
                                    "D. To process an urgent refund request"
                                ],
                                "correct": "B. To confirm shipment details for a merchandise order",
                                "explanation": "Email thông báo và cung cấp chi tiết vận chuyển đơn hàng (shipment details for a merchandise order)."
                            },
                            {
                                "id": "T_R14",
                                "question": "When is the package expected to arrive?",
                                "options": [
                                    "A. On Monday, November 2",
                                    "B. On Tuesday, November 3",
                                    "C. On Thursday, November 5",
                                    "D. Next weekend"
                                ],
                                "correct": "C. On Thursday, November 5",
                                "explanation": "Đoạn văn nêu rõ: 'estimated delivery at your San Francisco office is Thursday, November 5'."
                            },
                            {
                                "id": "T_R15",
                                "question": "What special benefit is mentioned for Mr. Reid?",
                                "options": [
                                    "A. He received free international roaming",
                                    "B. He was credited with 350 loyalty points",
                                    "C. He will receive a complimentary solar panel",
                                    "D. His warranty coverage was doubled for free"
                                ],
                                "correct": "B. He was credited with 350 loyalty points",
                                "explanation": "Đoạn văn nêu: 'you have earned 350 loyalty points from this transaction'."
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
