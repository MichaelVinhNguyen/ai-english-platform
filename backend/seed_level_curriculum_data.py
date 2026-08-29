"""
seed_level_curriculum_data.py – Ngân hàng bài học chi tiết và đề thi thực chiến theo từng cấp độ tiếng Anh
Chuẩn hóa theo khung tham chiếu Châu Âu (CEFR A1-C2) & Các chứng chỉ Quốc tế (TOEIC, IELTS, Business, Tech AI).
"""

LEVEL_CURRICULUM_DATA = {
    "A1": {
        "level": "A1",
        "title": "CEFR A1 – Mất Gốc & Nhập Môn Căn Bản (Breakthrough)",
        "badge": "Beginner / Mới bắt đầu",
        "color": "#10b981",
        "target_audience": "Người mới bắt đầu, mất gốc, muốn xây dựng nền tảng phát âm IPA, từ vựng sinh hoạt và giao tiếp cơ bản.",
        "outcome": "Nắm vững bảng chữ cái & 44 âm IPA, 600+ từ vựng quen thuộc, tự giới thiệu bản thân, hỏi đáp thông tin cơ bản về thời gian, gia đình, sở thích, mua sắm và thời tiết.",
        "modules": [
            {
                "id": "a1-m1",
                "title": "Bài 1: Bảng Chữ Cái, Phát Âm IPA Căn Bản & Chào Hỏi",
                "description": "Làm quen phát âm chuẩn quốc tế, nguyên âm, phụ âm và các mẫu câu chào hỏi hàng ngày.",
                "duration_min": 25,
                "xp": 60,
                "theory": "Trong tiếng Anh, phát âm chuẩn theo bảng phiên âm quốc tế IPA (International Phonetic Alphabet) là chìa khóa để nghe và nói tốt. Có 44 âm cơ bản gồm 20 nguyên âm (vowels) và 24 phụ âm (consonants). Mẫu câu chào hỏi cơ bản: 'Hello! How are you?', 'Good morning!', 'Nice to meet you!'.",
                "key_vocab": [
                    {
                        "word": "Hello / Hi",
                        "ipa": "/həˈloʊ/ /haɪ/",
                        "meaning": "Xin chào",
                        "example": "Hello, my name is Alex."
                    },
                    {
                        "word": "Good morning",
                        "ipa": "/ɡʊd ˈmɔːrnɪŋ/",
                        "meaning": "Chào buổi sáng",
                        "example": "Good morning, teacher!"
                    },
                    {
                        "word": "Pleasure",
                        "ipa": "/ˈpleʒər/",
                        "meaning": "Niềm vinh hạnh / Rất vui",
                        "example": "It's a pleasure to meet you."
                    },
                    {
                        "word": "Farewell",
                        "ipa": "/ˌferˈwel/",
                        "meaning": "Lời tạm biệt",
                        "example": "Farewell, see you tomorrow."
                    },
                    {
                        "word": "Introduce",
                        "ipa": "/ˌɪntrəˈduːs/",
                        "meaning": "Giới thiệu",
                        "example": "Let me introduce myself."
                    },
                    {
                        "word": "Friend",
                        "ipa": "/frend/",
                        "meaning": "Người bạn",
                        "example": "She is my best friend."
                    },
                    {
                        "word": "Morning",
                        "ipa": "/ˈmɔːrnɪŋ/",
                        "meaning": "Buổi sáng",
                        "example": "Good morning, how are you today?"
                    },
                    {
                        "word": "Evening",
                        "ipa": "/ˈiːvnɪŋ/",
                        "meaning": "Buổi tối",
                        "example": "Have a wonderful evening with your family."
                    },
                    {
                        "word": "Welcome",
                        "ipa": "/ˈwelkəm/",
                        "meaning": "Chào mừng / Hoan nghênh",
                        "example": "Welcome to our English class!"
                    },
                    {
                        "word": "Student",
                        "ipa": "/ˈstuːdnt/",
                        "meaning": "Học sinh / Sinh viên",
                        "example": "He is an eager English student."
                    },
                    {
                        "word": "Teacher",
                        "ipa": "/ˈtiːtʃər/",
                        "meaning": "Giáo viên",
                        "example": "The teacher explains the lesson clearly."
                    },
                    {
                        "word": "Happy",
                        "ipa": "/ˈhæpi/",
                        "meaning": "Hạnh phúc / Vui vẻ",
                        "example": "I feel very happy to learn new words."
                    }
                ],
                "grammar_point": {
                    "rule": "Đại từ nhân xưng & Động từ 'To Be' ở hiện tại đơn (I am, You/We/They are, He/She/It is)",
                    "formula": "Khẳng định: S + am/is/are + Noun/Adj | Phủ định: S + am/is/are + not...",
                    "examples": [
                        "I am a student. (Tôi là một học sinh.)",
                        "She is very friendly. (Cô ấy rất thân thiện.)",
                        "They are not at home. (Họ không có ở nhà.)"
                    ]
                },
                "listening_task": {
                    "audio_text": "Hello, my name is David. I am twenty-five years old and I am a software engineer from Canada.",
                    "question": "What is David's profession?",
                    "options": [
                        "Doctor",
                        "Software Engineer",
                        "Teacher",
                        "Student"
                    ],
                    "ans": "Software Engineer",
                    "exp": "Trong đoạn nói: 'I am a software engineer'."
                },
                "speaking_prompt": {
                    "target_sentence": "Hello, nice to meet you. My name is Alex and I am from Vietnam.",
                    "ipa_focus": "/həˈloʊ naɪs tu miːt ju/",
                    "tips": "Nhấn mạnh vào từ 'nice' và 'meet', nối âm nhẹ giữa 'meet' và 'you'."
                },
                "writing_task": {
                    "prompt": "Hãy viết 2 câu tự giới thiệu tên, tuổi và nghề nghiệp của bạn bằng tiếng Anh.",
                    "hint": "Cấu trúc: Hello, my name is [Name]. I am [Age] years old and I am a [Job].",
                    "sample_answer": "Hello, my name is Linh. I am twenty-two years old and I am a graphic designer."
                },
                "dialogue": [
                    {
                        "speaker": "David",
                        "text": "Good morning! I am David. Nice to meet you."
                    },
                    {
                        "speaker": "Lan",
                        "text": "Good morning, David! My name is Lan. Where are you from?"
                    },
                    {
                        "speaker": "David",
                        "text": "I am from Canada. Are you from Vietnam?"
                    },
                    {
                        "speaker": "Lan",
                        "text": "Yes, I am from Hanoi. Welcome to Vietnam!"
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Chọn câu đúng để giới thiệu tên mình:",
                        "options": [
                            "I is Nam.",
                            "I are Nam.",
                            "I am Nam.",
                            "I be Nam."
                        ],
                        "ans": "I am Nam.",
                        "exp": "Với chủ ngữ 'I', động từ to be chia là 'am'."
                    },
                    {
                        "q": "Đáp lại lời chào 'Nice to meet you!':",
                        "options": [
                            "Nice to meet you too!",
                            "Good night!",
                            "I am fine not.",
                            "Yes, I am."
                        ],
                        "ans": "Nice to meet you too!",
                        "exp": "'Nice to meet you too!' là cách phản xạ lịch sự và chuẩn mực nhất."
                    },
                    {
                        "q": "Từ nào sau đây có nghĩa là 'Chào buổi sáng'?",
                        "options": [
                            "Good night",
                            "Good morning",
                            "Good evening",
                            "Goodbye"
                        ],
                        "ans": "Good morning",
                        "exp": "'Good morning' là chào buổi sáng."
                    },
                    {
                        "q": "'She _____ my English teacher.' Điền từ thích hợp:",
                        "options": [
                            "am",
                            "are",
                            "is",
                            "be"
                        ],
                        "ans": "is",
                        "exp": "Chủ ngữ 'She' đi với động từ to be 'is'."
                    }
                ]
            },
            {
                "id": "a1-m2",
                "title": "Bài 2: Số Đếm, Thời Gian & Thông Tin Cá Nhân",
                "description": "Học cách nói tuổi, số điện thoại, ngày giờ và hỏi thăm thông tin liên lạc.",
                "duration_min": 30,
                "xp": 70,
                "theory": "Học cách đếm từ 1 đến 100, nói giờ chính xác ('What time is it?', 'It is seven o'clock.') và hỏi tuổi, địa chỉ ('How old are you?', 'What is your phone number?').",
                "key_vocab": [
                    {
                        "word": "O'clock",
                        "ipa": "/əˈklɑːk/",
                        "meaning": "Đúng ... giờ",
                        "example": "The meeting starts at eight o'clock."
                    },
                    {
                        "word": "Address",
                        "ipa": "/ˈædres/",
                        "meaning": "Địa chỉ",
                        "example": "What is your current address?"
                    },
                    {
                        "word": "Phone number",
                        "ipa": "/foʊn ˈnʌmbər/",
                        "meaning": "Số điện thoại",
                        "example": "Can I have your phone number?"
                    },
                    {
                        "word": "Birthday",
                        "ipa": "/ˈbɜːrθdeɪ/",
                        "meaning": "Ngày sinh nhật",
                        "example": "My birthday is in September."
                    },
                    {
                        "word": "Minute",
                        "ipa": "/ˈmɪnɪt/",
                        "meaning": "Phút",
                        "example": "Wait for five minutes, please."
                    },
                    {
                        "word": "Morning",
                        "ipa": "/ˈmɔːrnɪŋ/",
                        "meaning": "Buổi sáng",
                        "example": "I study English every morning."
                    },
                    {
                        "word": "Evening",
                        "ipa": "/ˈiːvnɪŋ/",
                        "meaning": "Buổi tối",
                        "example": "Have a wonderful evening with your family."
                    },
                    {
                        "word": "Welcome",
                        "ipa": "/ˈwelkəm/",
                        "meaning": "Chào mừng / Hoan nghênh",
                        "example": "Welcome to our English class!"
                    },
                    {
                        "word": "Friend",
                        "ipa": "/frend/",
                        "meaning": "Bạn bè",
                        "example": "She is my best friend from school."
                    },
                    {
                        "word": "Student",
                        "ipa": "/ˈstuːdnt/",
                        "meaning": "Học sinh / Sinh viên",
                        "example": "He is an eager English student."
                    },
                    {
                        "word": "Teacher",
                        "ipa": "/ˈtiːtʃər/",
                        "meaning": "Giáo viên",
                        "example": "The teacher explains the lesson clearly."
                    },
                    {
                        "word": "Happy",
                        "ipa": "/ˈhæpi/",
                        "meaning": "Hạnh phúc / Vui vẻ",
                        "example": "I feel very happy to learn new words."
                    }
                ],
                "grammar_point": {
                    "rule": "Từ để hỏi thông tin cá nhân: What, Where, How old, When",
                    "formula": "Wh-word + to be + Subject...?",
                    "examples": [
                        "What is your name? - My name is Peter.",
                        "Where are you from? - I am from Da Nang.",
                        "How old are you? - I am twenty-two years old."
                    ]
                },
                "listening_task": {
                    "audio_text": "Please note down my phone number: 0912-345-678. You can call me at three o'clock.",
                    "question": "What time can you call?",
                    "options": [
                        "At 2 o'clock",
                        "At 3 o'clock",
                        "At 5 o'clock",
                        "At 8 o'clock"
                    ],
                    "ans": "At 3 o'clock",
                    "exp": "Audio đề cập: 'You can call me at three o'clock'."
                },
                "speaking_prompt": {
                    "target_sentence": "My phone number is 0912-345-678 and my birthday is in July.",
                    "ipa_focus": "/maɪ foʊn ˈnʌmbər ɪz/",
                    "tips": "Ngắt nhịp tự nhiên giữa các cụm 3 số điện thoại."
                },
                "writing_task": {
                    "prompt": "Viết câu hỏi và câu trả lời về địa chỉ sinh sống hiện tại của bạn.",
                    "hint": "Where do you live? / What is your address? -> I live in...",
                    "sample_answer": "Where do you live? - I live in Ho Chi Minh City, Vietnam."
                },
                "dialogue": [
                    {
                        "speaker": "Clerk",
                        "text": "Can I have your full name and phone number, please?"
                    },
                    {
                        "speaker": "Minh",
                        "text": "Yes, my name is Minh Tran and my number is 0912-345-678."
                    },
                    {
                        "speaker": "Clerk",
                        "text": "Thank you. What time would you like to book your lesson?"
                    },
                    {
                        "speaker": "Minh",
                        "text": "At three o'clock this afternoon, please."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Để hỏi tuổi một người, ta dùng:",
                        "options": [
                            "How old are you?",
                            "How many years are you?",
                            "What old you have?",
                            "Where is your age?"
                        ],
                        "ans": "How old are you?",
                        "exp": "Cấu trúc chuẩn là 'How old are you?'."
                    },
                    {
                        "q": "Chọn câu đúng chỉ giờ giấc:",
                        "options": [
                            "It is at seven o'clock.",
                            "It is seven o'clock.",
                            "It has seven clock.",
                            "It makes seven hours."
                        ],
                        "ans": "It is seven o'clock.",
                        "exp": "Cấu trúc chỉ giờ: 'It is + [Số] + o'clock'."
                    },
                    {
                        "q": "'It is half past eight' nghĩa là mấy giờ?",
                        "options": [
                            "8 giờ đúng",
                            "8 giờ 15 phút",
                            "8 giờ 30 phút",
                            "8 giờ kém 15"
                        ],
                        "ans": "8 giờ 30 phút",
                        "exp": "'Half past' nghĩa là qua 30 phút (rưỡi)."
                    }
                ]
            },
            {
                "id": "a1-m3",
                "title": "Bài 3: Gia Đình, Đồ Vật & Miêu Tả Xung Quanh",
                "description": "Từ vựng các thành viên trong gia đình, đồ dùng phòng học và tính từ miêu tả cơ bản.",
                "duration_min": 30,
                "xp": 75,
                "theory": "Đại từ chỉ định (Demonstratives: This, That, These, Those) và Tính từ sở hữu (Possessive Adjectives: My, Your, His, Her, Our, Their) giúp miêu tả đồ vật và mối quan hệ gia đình.",
                "key_vocab": [
                    {
                        "word": "Family",
                        "ipa": "/ˈfæməli/",
                        "meaning": "Gia đình",
                        "example": "I love spending time with my family."
                    },
                    {
                        "word": "Parents",
                        "ipa": "/ˈperənts/",
                        "meaning": "Bố mẹ",
                        "example": "My parents live in Hanoi."
                    },
                    {
                        "word": "Sibling",
                        "ipa": "/ˈsɪblɪŋ/",
                        "meaning": "Anh chị em ruột",
                        "example": "I have two siblings."
                    },
                    {
                        "word": "Comfortable",
                        "ipa": "/ˈkʌmftəbl/",
                        "meaning": "Thoải mái / Tiện nghi",
                        "example": "This sofa is very comfortable."
                    },
                    {
                        "word": "Notebook",
                        "ipa": "/ˈnoʊtbʊk/",
                        "meaning": "Vở ghi chép",
                        "example": "I write new words in my notebook."
                    },
                    {
                        "word": "Beautiful",
                        "ipa": "/ˈbjuːtɪfl/",
                        "meaning": "Xinh đẹp",
                        "example": "She has a beautiful house."
                    },
                    {
                        "word": "Morning",
                        "ipa": "/ˈmɔːrnɪŋ/",
                        "meaning": "Buổi sáng",
                        "example": "Good morning, how are you today?"
                    },
                    {
                        "word": "Evening",
                        "ipa": "/ˈiːvnɪŋ/",
                        "meaning": "Buổi tối",
                        "example": "Have a wonderful evening with your family."
                    },
                    {
                        "word": "Welcome",
                        "ipa": "/ˈwelkəm/",
                        "meaning": "Chào mừng / Hoan nghênh",
                        "example": "Welcome to our English class!"
                    },
                    {
                        "word": "Friend",
                        "ipa": "/frend/",
                        "meaning": "Bạn bè",
                        "example": "She is my best friend from school."
                    },
                    {
                        "word": "Student",
                        "ipa": "/ˈstuːdnt/",
                        "meaning": "Học sinh / Sinh viên",
                        "example": "He is an eager English student."
                    },
                    {
                        "word": "Teacher",
                        "ipa": "/ˈtiːtʃər/",
                        "meaning": "Giáo viên",
                        "example": "The teacher explains the lesson clearly."
                    }
                ],
                "grammar_point": {
                    "rule": "This / That / These / Those & Tính từ sở hữu",
                    "formula": "This/That is + Noun (số ít) | These/Those are + Nouns (số nhiều)",
                    "examples": [
                        "This is my brother. (Đây là anh trai tôi.)",
                        "These are my new books. (Đây là những cuốn sách mới của tôi.)"
                    ]
                },
                "listening_task": {
                    "audio_text": "There are four people in my family: my father, my mother, my younger sister, and me.",
                    "question": "How many people are there in the family?",
                    "options": [
                        "Three",
                        "Four",
                        "Five",
                        "Six"
                    ],
                    "ans": "Four",
                    "exp": "Audio nêu rõ: 'There are four people in my family'."
                },
                "speaking_prompt": {
                    "target_sentence": "This is my family and these are my favorite books.",
                    "ipa_focus": "/ðɪs ɪz maɪ ˈfæməli/",
                    "tips": "Phát âm chuẩn âm /ð/ rung lưỡi trong 'This' và 'these'."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu giới thiệu về gia đình hoặc các thành viên sống cùng bạn.",
                    "hint": "There are... in my family. I live with my...",
                    "sample_answer": "There are four members in my family. I live with my parents and my younger brother."
                },
                "dialogue": [
                    {
                        "speaker": "Hoa",
                        "text": "Is this your family photo, Tom?"
                    },
                    {
                        "speaker": "Tom",
                        "text": "Yes, that is my father on the left and this is my mother."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "_____ are my notebooks on the table.",
                        "options": [
                            "These",
                            "This",
                            "That",
                            "It"
                        ],
                        "ans": "These",
                        "exp": "Đi với danh từ số nhiều 'notebooks' và động từ 'are', ta dùng 'These'."
                    },
                    {
                        "q": "'Her father is a doctor.' Từ 'Her' mang nghĩa:",
                        "options": [
                            "Của tôi",
                            "Của anh ấy",
                            "Của cô ấy",
                            "Của họ"
                        ],
                        "ans": "Của cô ấy",
                        "exp": "'Her' là tính từ sở hữu chỉ giống cái số ít (cô ấy)."
                    }
                ]
            },
            {
                "id": "a1-m4",
                "title": "Bài 4: Món Ăn, Thức Uống & Sở Thích Hàng Ngày (Food & Hobbies)",
                "description": "Học cách nói về món ăn yêu thích, cách gọi món đơn giản và diễn đạt sở thích cá nhân.",
                "duration_min": 30,
                "xp": 80,
                "theory": "Sử dụng động từ 'like', 'love', 'prefer' kết hợp với danh từ hoặc V-ing để biểu đạt sở thích. Mẫu câu gọi đồ ăn tại quán cafe/nhà hàng: 'I would like a cup of coffee, please.'",
                "key_vocab": [
                    {
                        "word": "Delicious",
                        "ipa": "/dɪˈlɪʃəs/",
                        "meaning": "Ngon miệng",
                        "example": "This soup is really delicious."
                    },
                    {
                        "word": "Beverage",
                        "ipa": "/ˈbevərɪdʒ/",
                        "meaning": "Đồ uống",
                        "example": "Water is my favorite beverage."
                    },
                    {
                        "word": "Order",
                        "ipa": "/ˈɔːrdər/",
                        "meaning": "Gọi món / Đặt hàng",
                        "example": "Are you ready to order?"
                    },
                    {
                        "word": "Hobby",
                        "ipa": "/ˈhɑːbi/",
                        "meaning": "Sở thích",
                        "example": "Reading books is my main hobby."
                    },
                    {
                        "word": "Morning",
                        "ipa": "/ˈmɔːrnɪŋ/",
                        "meaning": "Buổi sáng",
                        "example": "Good morning, how are you today?"
                    },
                    {
                        "word": "Evening",
                        "ipa": "/ˈiːvnɪŋ/",
                        "meaning": "Buổi tối",
                        "example": "Have a wonderful evening with your family."
                    },
                    {
                        "word": "Welcome",
                        "ipa": "/ˈwelkəm/",
                        "meaning": "Chào mừng / Hoan nghênh",
                        "example": "Welcome to our English class!"
                    },
                    {
                        "word": "Friend",
                        "ipa": "/frend/",
                        "meaning": "Bạn bè",
                        "example": "She is my best friend from school."
                    },
                    {
                        "word": "Student",
                        "ipa": "/ˈstuːdnt/",
                        "meaning": "Học sinh / Sinh viên",
                        "example": "He is an eager English student."
                    },
                    {
                        "word": "Teacher",
                        "ipa": "/ˈtiːtʃər/",
                        "meaning": "Giáo viên",
                        "example": "The teacher explains the lesson clearly."
                    },
                    {
                        "word": "Happy",
                        "ipa": "/ˈhæpi/",
                        "meaning": "Hạnh phúc / Vui vẻ",
                        "example": "I feel very happy to learn new words."
                    }
                ],
                "grammar_point": {
                    "rule": "Cấu trúc Like / Enjoy + V-ing & Danh từ đếm được / không đếm được (Countable & Uncountable Nouns)",
                    "formula": "S + like/love + V-ing/Noun | A/An/Some/Any",
                    "examples": [
                        "I like drinking orange juice in the summer.",
                        "Would you like some tea? - Yes, please."
                    ]
                },
                "listening_task": {
                    "audio_text": "Good afternoon. I would like a chicken sandwich and a glass of mineral water, please.",
                    "question": "What drink did the customer order?",
                    "options": [
                        "Mineral water",
                        "Orange juice",
                        "Hot coffee",
                        "Green tea"
                    ],
                    "ans": "Mineral water",
                    "exp": "Khách hàng gọi: 'a glass of mineral water'."
                },
                "speaking_prompt": {
                    "target_sentence": "I really enjoy eating Vietnamese Pho and drinking green tea.",
                    "ipa_focus": "/aɪ ˈrɪəli ɪnˈdʒɔɪ ˈiːtɪŋ/",
                    "tips": "Nhấn mạnh vào các từ mang thông tin: 'really enjoy', 'Pho', 'green tea'."
                },
                "writing_task": {
                    "prompt": "Viết 2-3 câu mô tả món ăn hoặc đồ uống bạn yêu thích nhất và lý do.",
                    "hint": "My favorite food is... because it is...",
                    "sample_answer": "My favorite food is Vietnamese Pho. It is delicious, warm, and very healthy."
                },
                "dialogue": [
                    {
                        "speaker": "Waiter",
                        "text": "Are you ready to order your lunch, sir?"
                    },
                    {
                        "speaker": "Customer",
                        "text": "Yes, I would like a beef salad and fresh orange juice."
                    },
                    {
                        "speaker": "Waiter",
                        "text": "Certainly! It will be ready in ten minutes."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Do you have _____ milk left in the fridge?",
                        "options": [
                            "any",
                            "a",
                            "an",
                            "many"
                        ],
                        "ans": "any",
                        "exp": "Trong câu hỏi với danh từ không đếm được 'milk', ta dùng 'any'."
                    },
                    {
                        "q": "I love _____ music in my free time.",
                        "options": [
                            "listening to",
                            "listen",
                            "listens",
                            "to listening"
                        ],
                        "ans": "listening to",
                        "exp": "Sau 'love' dùng V-ing 'listening to'."
                    }
                ]
            },
            {
                "id": "a1-m5",
                "title": "Bài 5: Màu Sắc, Trang Phục & Mua Sắm Cơ Bản (Colors & Clothes)",
                "description": "Từ vựng trang phục hàng ngày, màu sắc, cách hỏi giá tiền và kích cỡ cơ bản.",
                "duration_min": 30,
                "xp": 80,
                "theory": "Học cách miêu tả trang phục đang mặc ('I am wearing a blue shirt') và các câu hỏi giá tiền ('How much is this shirt?', 'How much are these shoes?').",
                "key_vocab": [
                    {
                        "word": "Clothes",
                        "ipa": "/kloʊðz/",
                        "meaning": "Quần áo",
                        "example": "I need to buy some new clothes."
                    },
                    {
                        "word": "Jacket",
                        "ipa": "/ˈdʒækɪt/",
                        "meaning": "Áo khoác",
                        "example": "This warm jacket is perfect for winter."
                    },
                    {
                        "word": "Size",
                        "ipa": "/saɪz/",
                        "meaning": "Kích cỡ",
                        "example": "Do you have this in size Medium?"
                    },
                    {
                        "word": "Expensive",
                        "ipa": "/ɪkˈspensɪv/",
                        "meaning": "Đắt đỏ",
                        "example": "That luxury watch is too expensive."
                    },
                    {
                        "word": "Morning",
                        "ipa": "/ˈmɔːrnɪŋ/",
                        "meaning": "Buổi sáng",
                        "example": "Good morning, how are you today?"
                    },
                    {
                        "word": "Evening",
                        "ipa": "/ˈiːvnɪŋ/",
                        "meaning": "Buổi tối",
                        "example": "Have a wonderful evening with your family."
                    },
                    {
                        "word": "Welcome",
                        "ipa": "/ˈwelkəm/",
                        "meaning": "Chào mừng / Hoan nghênh",
                        "example": "Welcome to our English class!"
                    },
                    {
                        "word": "Friend",
                        "ipa": "/frend/",
                        "meaning": "Bạn bè",
                        "example": "She is my best friend from school."
                    },
                    {
                        "word": "Student",
                        "ipa": "/ˈstuːdnt/",
                        "meaning": "Học sinh / Sinh viên",
                        "example": "He is an eager English student."
                    },
                    {
                        "word": "Teacher",
                        "ipa": "/ˈtiːtʃər/",
                        "meaning": "Giáo viên",
                        "example": "The teacher explains the lesson clearly."
                    },
                    {
                        "word": "Happy",
                        "ipa": "/ˈhæpi/",
                        "meaning": "Hạnh phúc / Vui vẻ",
                        "example": "I feel very happy to learn new words."
                    }
                ],
                "grammar_point": {
                    "rule": "Hiện tại tiếp diễn miêu tả trang phục đang mặc (S + am/is/are + wearing)",
                    "formula": "S + am/is/are + wearing + [Color] + [Clothes]",
                    "examples": [
                        "He is wearing a black suit.",
                        "She is wearing a beautiful yellow dress."
                    ]
                },
                "listening_task": {
                    "audio_text": "Excuse me, how much is this red jacket? - It is forty-five dollars.",
                    "question": "How much is the red jacket?",
                    "options": [
                        "$35",
                        "$45",
                        "$55",
                        "$65"
                    ],
                    "ans": "$45",
                    "exp": "Audio nêu rõ: 'It is forty-five dollars'."
                },
                "speaking_prompt": {
                    "target_sentence": "I am wearing a white T-shirt and blue jeans today.",
                    "ipa_focus": "/aɪ əm ˈwerɪŋ ə waɪt ˈtiː ʃɜːrt/",
                    "tips": "Nói rõ âm /w/ trong 'wearing' và 'white'."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu miêu tả trang phục bạn hoặc người bên cạnh đang mặc.",
                    "hint": "Today I am wearing... It looks...",
                    "sample_answer": "Today I am wearing a black jacket and blue jeans. It is very comfortable."
                },
                "dialogue": [
                    {
                        "speaker": "Shop Assistant",
                        "text": "Can I help you find anything, madam?"
                    },
                    {
                        "speaker": "Customer",
                        "text": "Yes, I am looking for a blue dress in size Small."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "How _____ are these black shoes?",
                        "options": [
                            "much",
                            "many",
                            "price",
                            "cost"
                        ],
                        "ans": "much",
                        "exp": "Hỏi giá tiền số nhiều dùng 'How much are...?'."
                    },
                    {
                        "q": "She _____ wearing a pink hat.",
                        "options": [
                            "is",
                            "am",
                            "are",
                            "be"
                        ],
                        "ans": "is",
                        "exp": "Chủ ngữ 'She' đi với 'is wearing'."
                    }
                ]
            },
            {
                "id": "a1-m6",
                "title": "Bài 6: Thời Tiết, Cảm Xúc & Hoạt Động Thường Nhật",
                "description": "Miêu tả thời tiết nắng, mưa, lạnh và cách biểu đạt cảm xúc vui, buồn, mệt mỏi.",
                "duration_min": 30,
                "xp": 85,
                "theory": "Mẫu câu hỏi thời tiết: 'What is the weather like today?' -> 'It is sunny and warm.' Tính từ chỉ cảm xúc: happy, tired, excited, hungry.",
                "key_vocab": [
                    {
                        "word": "Sunny",
                        "ipa": "/ˈsʌni/",
                        "meaning": "Có nắng",
                        "example": "It is a sunny day in Hanoi."
                    },
                    {
                        "word": "Rainy",
                        "ipa": "/ˈreɪni/",
                        "meaning": "Có mưa",
                        "example": "Take an umbrella on rainy days."
                    },
                    {
                        "word": "Excited",
                        "ipa": "/ɪkˈsaɪtɪd/",
                        "meaning": "Hào hứng / Phấn khích",
                        "example": "I am excited about our weekend trip."
                    },
                    {
                        "word": "Tired",
                        "ipa": "/ˈtaɪərd/",
                        "meaning": "Mệt mỏi",
                        "example": "I feel a bit tired after work."
                    },
                    {
                        "word": "Morning",
                        "ipa": "/ˈmɔːrnɪŋ/",
                        "meaning": "Buổi sáng",
                        "example": "Good morning, how are you today?"
                    },
                    {
                        "word": "Evening",
                        "ipa": "/ˈiːvnɪŋ/",
                        "meaning": "Buổi tối",
                        "example": "Have a wonderful evening with your family."
                    },
                    {
                        "word": "Welcome",
                        "ipa": "/ˈwelkəm/",
                        "meaning": "Chào mừng / Hoan nghênh",
                        "example": "Welcome to our English class!"
                    },
                    {
                        "word": "Friend",
                        "ipa": "/frend/",
                        "meaning": "Bạn bè",
                        "example": "She is my best friend from school."
                    },
                    {
                        "word": "Student",
                        "ipa": "/ˈstuːdnt/",
                        "meaning": "Học sinh / Sinh viên",
                        "example": "He is an eager English student."
                    },
                    {
                        "word": "Teacher",
                        "ipa": "/ˈtiːtʃər/",
                        "meaning": "Giáo viên",
                        "example": "The teacher explains the lesson clearly."
                    },
                    {
                        "word": "Happy",
                        "ipa": "/ˈhæpi/",
                        "meaning": "Hạnh phúc / Vui vẻ",
                        "example": "I feel very happy to learn new words."
                    }
                ],
                "grammar_point": {
                    "rule": "Cấu trúc miêu tả thời tiết và cảm xúc với tính từ: It is + Adj | S + feel/am + Adj",
                    "formula": "It is sunny/rainy/cold | S + am/is/are + happy/tired",
                    "examples": [
                        "It is very cold outside.",
                        "I am happy to see you again."
                    ]
                },
                "listening_task": {
                    "audio_text": "The weather today in London is rainy and windy, but tomorrow will be bright and sunny.",
                    "question": "What is the weather like today?",
                    "options": [
                        "Hot and sunny",
                        "Rainy and windy",
                        "Snowy and cold",
                        "Dry and warm"
                    ],
                    "ans": "Rainy and windy",
                    "exp": "Audio nêu rõ: 'The weather today is rainy and windy'."
                },
                "speaking_prompt": {
                    "target_sentence": "It is sunny today and I feel very happy and energetic.",
                    "ipa_focus": "/ɪt ɪz ˈsʌni təˈdeɪ ænd aɪ fiːl ˈhæpi/",
                    "tips": "Ngữ điệu vui tươi, nhấn mạnh vào 'sunny', 'happy', 'energetic'."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu mô tả thời tiết hôm nay và cảm xúc hiện tại của bạn.",
                    "hint": "Today the weather is... I feel...",
                    "sample_answer": "Today the weather is sunny and warm. I feel excited to learn new English lessons."
                },
                "dialogue": [
                    {
                        "speaker": "Alex",
                        "text": "What is the weather like in Da Nang right now?"
                    },
                    {
                        "speaker": "Mai",
                        "text": "It is sunny and windy, perfect for walking on the beach!"
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "'It is raining outside, don't forget your _____.'",
                        "options": [
                            "umbrella",
                            "sunglasses",
                            "swimsuit",
                            "shorts"
                        ],
                        "ans": "umbrella",
                        "exp": "Trời mưa thì cần mang theo ô (umbrella)."
                    },
                    {
                        "q": "How do you feel today? - I _____ very energetic.",
                        "options": [
                            "feel",
                            "feels",
                            "feeling",
                            "am feel"
                        ],
                        "ans": "feel",
                        "exp": "Chủ ngữ 'I' đi với động từ nguyên mẫu 'feel'."
                    }
                ]
            }
        ],
        "exam": {
            "title": "Bài Thi Chuẩn Đầu Ra CEFR A1 (Breakthrough Mastery Test)",
            "time_min": 20,
            "pass_score": 75,
            "questions": [
                {
                    "id": 1,
                    "question": "What is the correct response to: 'How do you do?'",
                    "options": [
                        "How do you do?",
                        "I am doing homework.",
                        "Yes, I do.",
                        "I am twenty."
                    ],
                    "correct": "How do you do?",
                    "explanation": "'How do you do?' là lời chào trang trọng khi gặp lần đầu, câu trả lời chuẩn là 'How do you do?'."
                },
                {
                    "id": 2,
                    "question": "She _____ a doctor at the central hospital.",
                    "options": [
                        "are",
                        "am",
                        "is",
                        "be"
                    ],
                    "correct": "is",
                    "explanation": "Chủ ngữ ngôi thứ 3 số ít 'She' đi với động từ to be 'is'."
                },
                {
                    "id": 3,
                    "question": "_____ are you from? - I am from Japan.",
                    "options": [
                        "What",
                        "Where",
                        "When",
                        "Who"
                    ],
                    "correct": "Where",
                    "explanation": "Hỏi về quê quán, nguồn gốc xuất xứ dùng từ để hỏi 'Where'."
                },
                {
                    "id": 4,
                    "question": "They _____ students. They are teachers.",
                    "options": [
                        "isn't",
                        "aren't",
                        "am not",
                        "not be"
                    ],
                    "correct": "aren't",
                    "explanation": "Chủ ngữ 'They' số nhiều đi với dạng phủ định 'aren't' (are not)."
                },
                {
                    "id": 5,
                    "question": "_____ books on the top shelf belong to my professor.",
                    "options": [
                        "Those",
                        "This",
                        "That",
                        "An"
                    ],
                    "correct": "Those",
                    "explanation": "Sách ở xa số nhiều dùng 'Those'."
                },
                {
                    "id": 6,
                    "question": "What time is it? - It is half _____ seven.",
                    "options": [
                        "past",
                        "to",
                        "after",
                        "before"
                    ],
                    "correct": "past",
                    "explanation": "'Half past seven' nghĩa là 7 giờ rưỡi (7:30)."
                },
                {
                    "id": 7,
                    "question": "My father usually _____ coffee in the morning.",
                    "options": [
                        "drinks",
                        "drink",
                        "drinking",
                        "drank"
                    ],
                    "correct": "drinks",
                    "explanation": "Hiện tại đơn với chủ ngữ ngôi thứ 3 số ít 'My father' thêm 's' vào động từ."
                },
                {
                    "id": 8,
                    "question": "I would like _____ orange, please.",
                    "options": [
                        "an",
                        "a",
                        "two",
                        "some"
                    ],
                    "correct": "an",
                    "explanation": "'Orange' bắt đầu bằng nguyên âm /ɒ/ nên dùng mạo từ 'an'."
                },
                {
                    "id": 9,
                    "question": "Are there _____ apples on the table?",
                    "options": [
                        "any",
                        "a",
                        "an",
                        "much"
                    ],
                    "correct": "any",
                    "explanation": "Câu hỏi với danh từ đếm được số nhiều dùng 'any'."
                },
                {
                    "id": 10,
                    "question": "Peter lives with _____ parents in London.",
                    "options": [
                        "his",
                        "her",
                        "their",
                        "him"
                    ],
                    "correct": "his",
                    "explanation": "Tính từ sở hữu cho nam số ít (Peter) là 'his'."
                },
                {
                    "id": 11,
                    "question": "How _____ is this shirt? - It is $20.",
                    "options": [
                        "much",
                        "many",
                        "old",
                        "often"
                    ],
                    "correct": "much",
                    "explanation": "Hỏi giá tiền dùng 'How much'."
                },
                {
                    "id": 12,
                    "question": "My sister is very good _____ English.",
                    "options": [
                        "at",
                        "in",
                        "on",
                        "with"
                    ],
                    "correct": "at",
                    "explanation": "Cấu trúc 'good at something' nghĩa là giỏi về cái gì."
                },
                {
                    "id": 13,
                    "question": "We _____ go to school on Sundays.",
                    "options": [
                        "don't",
                        "doesn't",
                        "aren't",
                        "not"
                    ],
                    "correct": "don't",
                    "explanation": "Chủ ngữ 'We' ở hiện tại đơn dùng trợ động từ phủ định 'don't'."
                },
                {
                    "id": 14,
                    "question": "Choose the word with the /iː/ sound:",
                    "options": [
                        "Meet",
                        "Sit",
                        "Pen",
                        "Cat"
                    ],
                    "correct": "Meet",
                    "explanation": "'Meet' phát âm là /miːt/ (nguyên âm dài i:)."
                },
                {
                    "id": 15,
                    "question": "Goodbye! Have a nice _____!",
                    "options": [
                        "day",
                        "sun",
                        "sky",
                        "name"
                    ],
                    "correct": "day",
                    "explanation": "'Have a nice day!' là lời chúc phổ biến khi tạm biệt."
                }
            ]
        }
    },
    "A2": {
        "level": "A2",
        "title": "CEFR A2 – Tiếng Anh Sơ Cấp (Elementary Communication)",
        "badge": "Elementary / Sơ cấp vững vàng",
        "color": "#3b82f6",
        "target_audience": "Người đã biết căn bản, muốn giao tiếp các tình huống mua sắm, du lịch, thói quen và quá khứ.",
        "outcome": "Vốn từ 1500+, sử dụng thành thạo Thì Hiện Tại Đơn, Quá Khứ Đơn, Tương Lai Đơn; giao tiếp tự tin khi đi du lịch, nhà hàng, chỉ đường và đặt phòng khách sạn.",
        "modules": [
            {
                "id": "a2-m1",
                "title": "Bài 1: Thì Hiện Tại Đơn & Lịch Trình Thói Quen (Daily Routine)",
                "description": "Làm chủ thì hiện tại đơn, trạng từ tần suất (always, usually, sometimes, never) và miêu tả một ngày làm việc.",
                "duration_min": 30,
                "xp": 80,
                "theory": "Thì Hiện Tại Đơn (Present Simple) dùng để diễn tả thói quen, chân lý hiển nhiên hoặc lịch trình cố định. Với He/She/It: động từ thêm -s/-es. Trạng từ chỉ tần suất đứng trước động từ thường và sau động từ to be.",
                "key_vocab": [
                    {
                        "word": "Routine",
                        "ipa": "/ruːˈtiːn/",
                        "meaning": "Lịch trình thói quen",
                        "example": "My daily routine starts at 6 AM."
                    },
                    {
                        "word": "Commute",
                        "ipa": "/kəˈmjuːt/",
                        "meaning": "Quãng đường đi làm",
                        "example": "I commute to work by bus."
                    },
                    {
                        "word": "Usually",
                        "ipa": "/ˈjuːʒuəli/",
                        "meaning": "Thường xuyên",
                        "example": "He usually drinks coffee in the morning."
                    },
                    {
                        "word": "Prepare",
                        "ipa": "/prɪˈper/",
                        "meaning": "Chuẩn bị",
                        "example": "She prepares breakfast for her family."
                    },
                    {
                        "word": "Schedule",
                        "ipa": "/ˈskedʒuːl/",
                        "meaning": "Lịch trình",
                        "example": "I have a busy schedule today."
                    },
                    {
                        "word": "Luggage",
                        "ipa": "/ˈlʌɡɪdʒ/",
                        "meaning": "Hành lý",
                        "example": "Please keep your luggage close to you."
                    },
                    {
                        "word": "Reservation",
                        "ipa": "/ˌrezərˈveɪʃn/",
                        "meaning": "Sự đặt chỗ trước",
                        "example": "I made a hotel reservation for our vacation."
                    },
                    {
                        "word": "Pharmacy",
                        "ipa": "/ˈfɑːrməsi/",
                        "meaning": "Hiệu thuốc",
                        "example": "You can buy this medicine at the local pharmacy."
                    },
                    {
                        "word": "Grocery",
                        "ipa": "/ˈɡroʊsəri/",
                        "meaning": "Hàng tạp hóa / Thực phẩm",
                        "example": "We need to buy some groceries for dinner."
                    }
                ],
                "grammar_point": {
                    "rule": "Hiện tại đơn với động từ thường: Khẳng định, Phủ định (don't/doesn't) và Nghi vấn (Do/Does...?)",
                    "formula": "S + V(s/es) | S + do/does + not + V_inf | Do/Does + S + V_inf?",
                    "examples": [
                        "I usually wake up early. (Tôi thường dậy sớm.)",
                        "He doesn't like spicy food. (Anh ấy không thích ăn cay.)",
                        "Do you work on weekends? (Bạn có làm việc vào cuối tuần không?)"
                    ]
                },
                "listening_task": {
                    "audio_text": "Every morning, Sarah drinks green tea and reads the newspaper before heading to work at eight thirty.",
                    "question": "What does Sarah drink in the morning?",
                    "options": [
                        "Black coffee",
                        "Green tea",
                        "Orange juice",
                        "Milk"
                    ],
                    "ans": "Green tea",
                    "exp": "Đoạn nghe có câu: 'Sarah drinks green tea'."
                },
                "speaking_prompt": {
                    "target_sentence": "I usually wake up at six thirty and commute to work by bus.",
                    "ipa_focus": "/aɪ ˈjuːʒuəli weɪk ʌp/",
                    "tips": "Nối âm 'wake up' thành /weɪ-kʌp/."
                },
                "writing_task": {
                    "prompt": "Viết đoạn văn ngắn 3 câu mô tả thói quen buổi sáng của bạn.",
                    "hint": "Every morning I wake up at... Then I... After that I...",
                    "sample_answer": "Every morning I wake up at 6:30 AM. Then I brush my teeth and prepare a quick breakfast. After that, I commute to work by motorbike."
                },
                "dialogue": [
                    {
                        "speaker": "Mark",
                        "text": "What time do you usually finish work, Anna?"
                    },
                    {
                        "speaker": "Anna",
                        "text": "I usually finish at five thirty, but sometimes I stay late on Fridays."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "She _____ to the gym three times a week.",
                        "options": [
                            "goes",
                            "go",
                            "going",
                            "is go"
                        ],
                        "ans": "goes",
                        "exp": "Chủ ngữ 'She' ngôi 3 số ít thêm 'es' vào động từ tận cùng bằng 'o'."
                    },
                    {
                        "q": "_____ you often drink coffee in the morning?",
                        "options": [
                            "Do",
                            "Does",
                            "Are",
                            "Is"
                        ],
                        "ans": "Do",
                        "exp": "Với chủ ngữ 'you', trợ động từ là 'Do'."
                    }
                ]
            },
            {
                "id": "a2-m2",
                "title": "Bài 2: Thì Quá Khứ Đơn & Kể Lại Chuyến Du Lịch (Travel & Past Simple)",
                "description": "Làm chủ động từ quy tắc (-ed) và bất quy tắc (went, saw, ate, bought), hỏi đáp về kỳ nghỉ đã qua.",
                "duration_min": 35,
                "xp": 85,
                "theory": "Thì Quá Khứ Đơn (Past Simple) dùng để diễn tả hành động đã xảy ra và kết thúc trong quá khứ với thời gian xác định (yesterday, last week, in 2024, 2 days ago). Trợ động từ phủ định và nghi vấn là 'did / didn't'.",
                "key_vocab": [
                    {
                        "word": "Vacation",
                        "ipa": "/veɪˈkeɪʃn/",
                        "meaning": "Kỳ nghỉ",
                        "example": "We had a wonderful vacation in Da Nang."
                    },
                    {
                        "word": "Destination",
                        "ipa": "/ˌdestɪˈneɪʃn/",
                        "meaning": "Điểm đến",
                        "example": "Phu Quoc is a popular destination."
                    },
                    {
                        "word": "Explore",
                        "ipa": "/ɪkˈsplɔːr/",
                        "meaning": "Khám phá",
                        "example": "We explored ancient temples."
                    },
                    {
                        "word": "Souvenir",
                        "ipa": "/ˌsuːvəˈnɪr/",
                        "meaning": "Quà lưu niệm",
                        "example": "I bought some souvenirs for my friends."
                    },
                    {
                        "word": "Schedule",
                        "ipa": "/ˈskedʒuːl/",
                        "meaning": "Lịch trình / Thời gian biểu",
                        "example": "I check my daily schedule every morning."
                    },
                    {
                        "word": "Commute",
                        "ipa": "/kəˈmjuːt/",
                        "meaning": "Đi lại hàng ngày",
                        "example": "My morning commute takes about twenty minutes."
                    },
                    {
                        "word": "Luggage",
                        "ipa": "/ˈlʌɡɪdʒ/",
                        "meaning": "Hành lý",
                        "example": "Please keep your luggage close to you."
                    },
                    {
                        "word": "Reservation",
                        "ipa": "/ˌrezərˈveɪʃn/",
                        "meaning": "Sự đặt chỗ trước",
                        "example": "I made a hotel reservation for our vacation."
                    },
                    {
                        "word": "Pharmacy",
                        "ipa": "/ˈfɑːrməsi/",
                        "meaning": "Hiệu thuốc",
                        "example": "You can buy this medicine at the local pharmacy."
                    },
                    {
                        "word": "Grocery",
                        "ipa": "/ˈɡroʊsəri/",
                        "meaning": "Hàng tạp hóa / Thực phẩm",
                        "example": "We need to buy some groceries for dinner."
                    }
                ],
                "grammar_point": {
                    "rule": "Thì Quá khứ đơn: S + V2/ed | S + didn't + V_inf | Did + S + V_inf?",
                    "formula": "Khẳng định: S + V-ed / V2 (Irregular) | Phủ định: S + did not + V_inf",
                    "examples": [
                        "I visited Hoi An ancient town last summer. (Tôi đã thăm phố cổ Hội An mùa hè trước.)",
                        "We didn't go swimming because of the heavy rain. (Chúng tôi đã không đi bơi vì mưa to.)"
                    ]
                },
                "listening_task": {
                    "audio_text": "Last summer, our family flew to Da Nang. We stayed in a seaside hotel and ate delicious fresh seafood.",
                    "question": "Where did the family stay?",
                    "options": [
                        "In a mountain cabin",
                        "In a seaside hotel",
                        "At a friend's house",
                        "In the city center"
                    ],
                    "ans": "In a seaside hotel",
                    "exp": "Audio nêu rõ: 'We stayed in a seaside hotel'."
                },
                "speaking_prompt": {
                    "target_sentence": "Last summer I traveled to Da Nang and visited many beautiful beaches.",
                    "ipa_focus": "/lɑːst ˈsʌmər aɪ ˈtrævld/",
                    "tips": "Chú ý đuôi -ed trong 'traveled' phát âm là /d/, 'visited' phát âm là /ɪd/."
                },
                "writing_task": {
                    "prompt": "Viết 3 câu về một chuyến đi đáng nhớ trong quá khứ của bạn.",
                    "hint": "Last year I went to... The weather was... I enjoyed...",
                    "sample_answer": "Last year, I went to Nha Trang with my family. The weather was sunny and the sea was crystal clear. I really enjoyed tasting fresh seafood."
                },
                "dialogue": [
                    {
                        "speaker": "Ben",
                        "text": "How was your trip to Da Lat last weekend, Linh?"
                    },
                    {
                        "speaker": "Linh",
                        "text": "It was fantastic! The weather was cool and we visited beautiful flower gardens."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "They _____ a new car two days ago.",
                        "options": [
                            "bought",
                            "buy",
                            "buying",
                            "have bought"
                        ],
                        "ans": "bought",
                        "exp": "'Two days ago' là dấu hiệu quá khứ đơn, quá khứ của 'buy' là 'bought'."
                    },
                    {
                        "q": "We didn't _____ the museum yesterday because it was closed.",
                        "options": [
                            "visit",
                            "visited",
                            "visiting",
                            "visits"
                        ],
                        "ans": "visit",
                        "exp": "Sau 'didn't' động từ trở về nguyên mẫu 'visit'."
                    }
                ]
            },
            {
                "id": "a2-m3",
                "title": "Bài 3: Chỉ Đường, Mua Sắm & Giao Tiếp Nơi Công Cộng",
                "description": "Mẫu câu hỏi đường, chỉ hướng (turn left, go straight), hỏi giá và thương lượng mua sắm.",
                "duration_min": 30,
                "xp": 80,
                "theory": "Giới từ chỉ nơi chốn (next to, opposite, between, behind) và các mẫu câu lịch sự hỏi đường: 'Excuse me, could you tell me how to get to...?'",
                "key_vocab": [
                    {
                        "word": "Intersection",
                        "ipa": "/ˌɪntərˈsekʃn/",
                        "meaning": "Ngã tư / Giao lộ",
                        "example": "Turn right at the next intersection."
                    },
                    {
                        "word": "Opposite",
                        "ipa": "/ˈɑːpəzɪt/",
                        "meaning": "Đối diện",
                        "example": "The pharmacy is opposite the bank."
                    },
                    {
                        "word": "Discount",
                        "ipa": "/ˈdɪskaʊnt/",
                        "meaning": "Giảm giá",
                        "example": "Can I get a 10% discount?"
                    },
                    {
                        "word": "Receipt",
                        "ipa": "/rɪˈsiːt/",
                        "meaning": "Hóa đơn / Biên lai",
                        "example": "Here is your receipt and change."
                    },
                    {
                        "word": "Schedule",
                        "ipa": "/ˈskedʒuːl/",
                        "meaning": "Lịch trình / Thời gian biểu",
                        "example": "I check my daily schedule every morning."
                    },
                    {
                        "word": "Commute",
                        "ipa": "/kəˈmjuːt/",
                        "meaning": "Đi lại hàng ngày",
                        "example": "My morning commute takes about twenty minutes."
                    },
                    {
                        "word": "Luggage",
                        "ipa": "/ˈlʌɡɪdʒ/",
                        "meaning": "Hành lý",
                        "example": "Please keep your luggage close to you."
                    },
                    {
                        "word": "Reservation",
                        "ipa": "/ˌrezərˈveɪʃn/",
                        "meaning": "Sự đặt chỗ trước",
                        "example": "I made a hotel reservation for our vacation."
                    },
                    {
                        "word": "Pharmacy",
                        "ipa": "/ˈfɑːrməsi/",
                        "meaning": "Hiệu thuốc",
                        "example": "You can buy this medicine at the local pharmacy."
                    },
                    {
                        "word": "Grocery",
                        "ipa": "/ˈɡroʊsəri/",
                        "meaning": "Hàng tạp hóa / Thực phẩm",
                        "example": "We need to buy some groceries for dinner."
                    }
                ],
                "grammar_point": {
                    "rule": "Câu mệnh lệnh & Động từ khuyết thiếu 'Could / Can' để yêu cầu lịch sự",
                    "formula": "Excuse me, could you please + V_inf...? | Go straight on... / Turn left at...",
                    "examples": [
                        "Could you show me the way to the post office?",
                        "Turn right at the traffic lights and walk for 100 meters."
                    ]
                },
                "listening_task": {
                    "audio_text": "Excuse me, go straight for two blocks, then turn left at the bookstore. The museum is on your right.",
                    "question": "Where is the museum located?",
                    "options": [
                        "On the left",
                        "On the right",
                        "Behind the bookstore",
                        "Across the river"
                    ],
                    "ans": "On the right",
                    "exp": "Người chỉ đường nói: 'The museum is on your right'."
                },
                "speaking_prompt": {
                    "target_sentence": "Excuse me, could you tell me where the nearest pharmacy is?",
                    "ipa_focus": "/ɪkˈskjuːz miː kʊd juː tel miː/",
                    "tips": "Ngữ điệu lên giọng ở cuối câu hỏi Yes/No hoặc câu hỏi lịch sự."
                },
                "writing_task": {
                    "prompt": "Viết đoạn văn ngắn 3 câu chỉ đường từ nhà bạn ra siêu thị gần nhất.",
                    "hint": "From my house, turn... Go straight for... It is on your...",
                    "sample_answer": "From my house, turn left and walk straight for 200 meters. Turn right at the convenience store. The supermarket is on your left."
                },
                "dialogue": [
                    {
                        "speaker": "Tourist",
                        "text": "Excuse me, how can I get to the central market?"
                    },
                    {
                        "speaker": "Local",
                        "text": "Go straight along this street and take the second turning on the left."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "The coffee shop is _____ the bank and the bookstore.",
                        "options": [
                            "between",
                            "among",
                            "across",
                            "next"
                        ],
                        "ans": "between",
                        "exp": "Vị trí nằm giữa 2 địa điểm dùng 'between A and B'."
                    },
                    {
                        "q": "Go _____ on until you see the roundabout.",
                        "options": [
                            "straight",
                            "direct",
                            "right",
                            "left"
                        ],
                        "ans": "straight",
                        "exp": "Cụm chỉ đường đi thẳng: 'Go straight on'."
                    }
                ]
            },
            {
                "id": "a2-m4",
                "title": "Bài 4: Sức Khỏe, Thăm Khám Bác Sĩ & Lời Khuyên (Health & Doctor)",
                "description": "Từ vựng triệu chứng thông thường (headache, fever, sore throat), mẫu câu đi khám và đưa lời khuyên (Should / Shouldn't).",
                "duration_min": 30,
                "xp": 80,
                "theory": "Sử dụng 'have a + [Bệnh]' để nói về triệu chứng ('I have a headache', 'She has a fever'). Dùng 'should / shouldn't + V_inf' để đưa ra lời khuyên sức khỏe.",
                "key_vocab": [
                    {
                        "word": "Prescription",
                        "ipa": "/prɪˈskrɪpʃn/",
                        "meaning": "Đơn thuốc",
                        "example": "The doctor gave me a prescription for antibiotics."
                    },
                    {
                        "word": "Symptom",
                        "ipa": "/ˈsɪmptəm/",
                        "meaning": "Triệu chứng",
                        "example": "Fever is a common symptom of the flu."
                    },
                    {
                        "word": "Appointment",
                        "ipa": "/əˈpɔɪntmənt/",
                        "meaning": "Cuộc hẹn khám",
                        "example": "I have an appointment with Dr. Miller at 2 PM."
                    },
                    {
                        "word": "Recover",
                        "ipa": "/rɪˈkʌvər/",
                        "meaning": "Hồi phục",
                        "example": "Drink plenty of water to recover quickly."
                    },
                    {
                        "word": "Schedule",
                        "ipa": "/ˈskedʒuːl/",
                        "meaning": "Lịch trình / Thời gian biểu",
                        "example": "I check my daily schedule every morning."
                    },
                    {
                        "word": "Commute",
                        "ipa": "/kəˈmjuːt/",
                        "meaning": "Đi lại hàng ngày",
                        "example": "My morning commute takes about twenty minutes."
                    },
                    {
                        "word": "Luggage",
                        "ipa": "/ˈlʌɡɪdʒ/",
                        "meaning": "Hành lý",
                        "example": "Please keep your luggage close to you."
                    },
                    {
                        "word": "Reservation",
                        "ipa": "/ˌrezərˈveɪʃn/",
                        "meaning": "Sự đặt chỗ trước",
                        "example": "I made a hotel reservation for our vacation."
                    },
                    {
                        "word": "Pharmacy",
                        "ipa": "/ˈfɑːrməsi/",
                        "meaning": "Hiệu thuốc",
                        "example": "You can buy this medicine at the local pharmacy."
                    },
                    {
                        "word": "Grocery",
                        "ipa": "/ˈɡroʊsəri/",
                        "meaning": "Hàng tạp hóa / Thực phẩm",
                        "example": "We need to buy some groceries for dinner."
                    }
                ],
                "grammar_point": {
                    "rule": "Động từ khuyết thiếu Should / Shouldn't & Cấu trúc Mustn't",
                    "formula": "S + should/shouldn't + V_inf",
                    "examples": [
                        "You should get plenty of rest.",
                        "You shouldn't drink iced water when you have a sore throat."
                    ]
                },
                "listening_task": {
                    "audio_text": "Good morning. I have a severe headache and a mild fever since yesterday evening.",
                    "question": "What symptoms does the patient have?",
                    "options": [
                        "Headache and fever",
                        "Broken leg",
                        "Stomachache only",
                        "Toothache"
                    ],
                    "ans": "Headache and fever",
                    "exp": "Audio nêu rõ: 'headache and a mild fever'."
                },
                "speaking_prompt": {
                    "target_sentence": "You should drink warm water and take this medicine twice a day.",
                    "ipa_focus": "/juː ʃəd drɪŋk wɔːrm ˈwɔːtər/",
                    "tips": "Nhấn mạnh 'drink warm water' và 'twice a day'."
                },
                "writing_task": {
                    "prompt": "Viết 2-3 câu đưa lời khuyên cho một người bạn đang bị cảm cúm.",
                    "hint": "You should take... You shouldn't stay up...",
                    "sample_answer": "You should stay in bed and drink plenty of warm lemon water. You shouldn't stay up late working."
                },
                "dialogue": [
                    {
                        "speaker": "Doctor",
                        "text": "How long have you felt unwell?"
                    },
                    {
                        "speaker": "Patient",
                        "text": "For two days. I have a sore throat and feel exhausted."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "You _____ stay in bed when you have a high fever.",
                        "options": [
                            "should",
                            "shouldn't",
                            "mustn't",
                            "are"
                        ],
                        "ans": "should",
                        "exp": "Lời khuyên tích cực dùng 'should'."
                    },
                    {
                        "q": "She has _____ terrible headache.",
                        "options": [
                            "a",
                            "an",
                            "the",
                            "some"
                        ],
                        "ans": "a",
                        "exp": "Cụm thành ngữ chỉ bệnh: 'have a headache'."
                    }
                ]
            },
            {
                "id": "a2-m5",
                "title": "Bài 5: Kế Hoạch Tương Lai & Dự Định (Future Plans: Will & Be Going To)",
                "description": "Phân biệt 'will' (quyết định tức thì, dự đoán) và 'be going to' (kế hoạch đã định trước).",
                "duration_min": 30,
                "xp": 85,
                "theory": "Sử dụng 'be going to + V_inf' khi có kế hoạch hoặc bằng chứng rõ ràng ở hiện tại ('Look at those black clouds! It is going to rain.'). Sử dụng 'will + V_inf' khi đưa ra quyết định ngay lúc nói hoặc lời hứa.",
                "key_vocab": [
                    {
                        "word": "Intention",
                        "ipa": "/ɪnˈtenʃn/",
                        "meaning": "Ý định",
                        "example": "My intention is to study abroad next year."
                    },
                    {
                        "word": "Promise",
                        "ipa": "/ˈprɑːmɪs/",
                        "meaning": "Lời hứa",
                        "example": "I promise I will help you with your homework."
                    },
                    {
                        "word": "Arrangement",
                        "ipa": "/əˈreɪndʒmənt/",
                        "meaning": "Sự sắp xếp",
                        "example": "We have made all travel arrangements."
                    },
                    {
                        "word": "Career",
                        "ipa": "/kəˈrɪr/",
                        "meaning": "Sự nghiệp",
                        "example": "She wants to build a career in technology."
                    },
                    {
                        "word": "Schedule",
                        "ipa": "/ˈskedʒuːl/",
                        "meaning": "Lịch trình / Thời gian biểu",
                        "example": "I check my daily schedule every morning."
                    },
                    {
                        "word": "Commute",
                        "ipa": "/kəˈmjuːt/",
                        "meaning": "Đi lại hàng ngày",
                        "example": "My morning commute takes about twenty minutes."
                    },
                    {
                        "word": "Luggage",
                        "ipa": "/ˈlʌɡɪdʒ/",
                        "meaning": "Hành lý",
                        "example": "Please keep your luggage close to you."
                    },
                    {
                        "word": "Reservation",
                        "ipa": "/ˌrezərˈveɪʃn/",
                        "meaning": "Sự đặt chỗ trước",
                        "example": "I made a hotel reservation for our vacation."
                    },
                    {
                        "word": "Pharmacy",
                        "ipa": "/ˈfɑːrməsi/",
                        "meaning": "Hiệu thuốc",
                        "example": "You can buy this medicine at the local pharmacy."
                    },
                    {
                        "word": "Grocery",
                        "ipa": "/ˈɡroʊsəri/",
                        "meaning": "Hàng tạp hóa / Thực phẩm",
                        "example": "We need to buy some groceries for dinner."
                    }
                ],
                "grammar_point": {
                    "rule": "Thì Tương lai gần (Be going to) vs Tương lai đơn (Will)",
                    "formula": "S + am/is/are + going to + V_inf | S + will + V_inf",
                    "examples": [
                        "I am going to visit my grandparents this Sunday.",
                        "Don't worry, I will carry that heavy bag for you."
                    ]
                },
                "listening_task": {
                    "audio_text": "Next month, my brother is going to start a new job as a graphic designer in Singapore.",
                    "question": "What is the speaker's brother going to do?",
                    "options": [
                        "Start a new job in Singapore",
                        "Travel on vacation",
                        "Study at university",
                        "Buy a house"
                    ],
                    "ans": "Start a new job in Singapore",
                    "exp": "Audio nêu rõ: 'is going to start a new job as a graphic designer in Singapore'."
                },
                "speaking_prompt": {
                    "target_sentence": "I am going to enroll in an advanced English communication course next week.",
                    "ipa_focus": "/aɪ əm ˈɡoʊɪŋ tə ɪnˈroʊl/",
                    "tips": "Nói 'going to' mượt mà, nhấn âm 'advanced English course'."
                },
                "writing_task": {
                    "prompt": "Viết 3 câu về kế hoạch bạn dự định thực hiện trong kỳ nghỉ cuối tuần tới.",
                    "hint": "This weekend, I am going to... I will also...",
                    "sample_answer": "This weekend, I am going to visit the national museum with my friends. In the evening, we will have dinner at an Italian restaurant. I hope the weather will be pleasant."
                },
                "dialogue": [
                    {
                        "speaker": "Lucas",
                        "text": "What are your plans for the summer holiday?"
                    },
                    {
                        "speaker": "Maya",
                        "text": "I am going to travel to Da Nang for four days. I bought the flight tickets yesterday!"
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Look at the dark clouds! It _____ rain.",
                        "options": [
                            "is going to",
                            "will",
                            "was",
                            "rains"
                        ],
                        "ans": "is going to",
                        "exp": "Có bằng chứng rõ ràng ở hiện tại (dark clouds) dùng 'is going to'."
                    },
                    {
                        "q": "The phone is ringing! - I _____ answer it.",
                        "options": [
                            "will",
                            "am going to",
                            "have",
                            "am"
                        ],
                        "ans": "will",
                        "exp": "Quyết định đưa ra ngay tại thời điểm nói dùng 'will'."
                    }
                ]
            },
            {
                "id": "a2-m6",
                "title": "Bài 6: Sở Thích, Âm Nhạc, Phim Ảnh & So Sánh (Hobbies & Media)",
                "description": "Tính từ miêu tả cảm xúc (interested, bored) và so sánh hơn / so sánh nhất (Comparative & Superlative).",
                "duration_min": 30,
                "xp": 85,
                "theory": "Tính từ tận cùng -ed chỉ cảm xúc người trải nghiệm ('I am interested in art'), tính từ tận cùng -ing chỉ tính chất của sự vật ('This movie is interesting'). So sánh hơn: short-adj + er than / more + long-adj than.",
                "key_vocab": [
                    {
                        "word": "Fascinating",
                        "ipa": "/ˈfæsɪneɪtɪŋ/",
                        "meaning": "Lôi cuốn / Hấp dẫn",
                        "example": "This documentary is truly fascinating."
                    },
                    {
                        "word": "Soundtrack",
                        "ipa": "/ˈsaʊndtræk/",
                        "meaning": "Nhạc phim",
                        "example": "The movie has an emotional soundtrack."
                    },
                    {
                        "word": "Audience",
                        "ipa": "/ˈɔːdiəns/",
                        "meaning": "Khán giả",
                        "example": "The audience cheered at the end of the concert."
                    },
                    {
                        "word": "Popular",
                        "ipa": "/ˈpɑːpjələr/",
                        "meaning": "Phổ biến / Được ưa chuộng",
                        "example": "Pop music is very popular among teenagers."
                    },
                    {
                        "word": "Schedule",
                        "ipa": "/ˈskedʒuːl/",
                        "meaning": "Lịch trình / Thời gian biểu",
                        "example": "I check my daily schedule every morning."
                    },
                    {
                        "word": "Commute",
                        "ipa": "/kəˈmjuːt/",
                        "meaning": "Đi lại hàng ngày",
                        "example": "My morning commute takes about twenty minutes."
                    },
                    {
                        "word": "Luggage",
                        "ipa": "/ˈlʌɡɪdʒ/",
                        "meaning": "Hành lý",
                        "example": "Please keep your luggage close to you."
                    },
                    {
                        "word": "Reservation",
                        "ipa": "/ˌrezərˈveɪʃn/",
                        "meaning": "Sự đặt chỗ trước",
                        "example": "I made a hotel reservation for our vacation."
                    },
                    {
                        "word": "Pharmacy",
                        "ipa": "/ˈfɑːrməsi/",
                        "meaning": "Hiệu thuốc",
                        "example": "You can buy this medicine at the local pharmacy."
                    },
                    {
                        "word": "Grocery",
                        "ipa": "/ˈɡroʊsəri/",
                        "meaning": "Hàng tạp hóa / Thực phẩm",
                        "example": "We need to buy some groceries for dinner."
                    }
                ],
                "grammar_point": {
                    "rule": "So sánh hơn & So sánh nhất của tính từ (Comparatives & Superlatives)",
                    "formula": "Short: adj-er than / the adj-est | Long: more adj than / the most adj",
                    "examples": [
                        "Action movies are more exciting than romantic comedies.",
                        "This is the most thrilling novel I have ever read."
                    ]
                },
                "listening_task": {
                    "audio_text": "I really love listening to acoustic guitar music because it helps me relax after stressful workdays.",
                    "question": "Why does the speaker love acoustic guitar?",
                    "options": [
                        "It is loud",
                        "It helps him relax",
                        "It is exciting",
                        "It makes him dance"
                    ],
                    "ans": "It helps him relax",
                    "exp": "Audio nêu rõ: 'because it helps me relax'."
                },
                "speaking_prompt": {
                    "target_sentence": "In my opinion, this sci-fi movie is more captivating than the previous one.",
                    "ipa_focus": "/ɪn maɪ əˈpɪnjən ðɪs ˈsaɪ faɪ ˈmuːvi/",
                    "tips": "Nói rõ 'captivating' và giữ ngữ điệu nhận xét tự nhiên."
                },
                "writing_task": {
                    "prompt": "Viết 2-3 câu so sánh 2 bộ phim hoặc 2 ca sĩ bạn yêu thích.",
                    "hint": "... is more interesting than... because...",
                    "sample_answer": "In my opinion, Christopher Nolan's films are more thought-provoking than standard Hollywood action blockbusters because they feature intricate storylines."
                },
                "dialogue": [
                    {
                        "speaker": "Chloe",
                        "text": "Which genre of music do you prefer?"
                    },
                    {
                        "speaker": "Sam",
                        "text": "I prefer jazz because it is much more soothing than rock music."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "This is the _____ book in the entire library.",
                        "options": [
                            "most interesting",
                            "more interesting",
                            "interestingest",
                            "interestinger"
                        ],
                        "ans": "most interesting",
                        "exp": "So sánh nhất tính từ dài: 'the most interesting'."
                    },
                    {
                        "q": "I feel _____ after watching that horror film.",
                        "options": [
                            "terrified",
                            "terrifying",
                            "terrify",
                            "terrifies"
                        ],
                        "ans": "terrified",
                        "exp": "Chỉ cảm xúc của người dùng tính từ đuôi -ed 'terrified'."
                    }
                ]
            }
        ],
        "exam": {
            "title": "Bài Thi Chuẩn Đầu Ra CEFR A2 (Elementary Mastery Test)",
            "time_min": 25,
            "pass_score": 75,
            "questions": [
                {
                    "id": 1,
                    "question": "Yesterday we _____ to the cinema to watch the new superhero movie.",
                    "options": [
                        "went",
                        "go",
                        "gone",
                        "was going"
                    ],
                    "correct": "went",
                    "explanation": "Quá khứ của động từ 'go' là 'went'."
                },
                {
                    "id": 2,
                    "question": "I haven't seen Mark _____ last Monday.",
                    "options": [
                        "since",
                        "for",
                        "in",
                        "during"
                    ],
                    "correct": "since",
                    "explanation": "'Since' đi với mốc thời gian trong quá khứ (last Monday)."
                },
                {
                    "id": 3,
                    "question": "This jacket is _____ than the blue one.",
                    "options": [
                        "more expensive",
                        "expensiver",
                        "most expensive",
                        "as expensive"
                    ],
                    "correct": "more expensive",
                    "explanation": "So sánh hơn của tính từ dài 'expensive' là 'more expensive'."
                },
                {
                    "id": 4,
                    "question": "Turn left at the traffic lights and the bank is on your _____.",
                    "options": [
                        "right",
                        "straight",
                        "across",
                        "near"
                    ],
                    "correct": "right",
                    "explanation": "Vị trí bên tay phải dùng 'on your right'."
                },
                {
                    "id": 5,
                    "question": "While I was studying, my brother _____ listening to loud music.",
                    "options": [
                        "was",
                        "were",
                        "did",
                        "is"
                    ],
                    "correct": "was",
                    "explanation": "Hành động song song trong quá khứ tiếp diễn với chủ ngữ 'my brother' dùng 'was'."
                },
                {
                    "id": 6,
                    "question": "Could you please tell me _____ the train station is?",
                    "options": [
                        "where",
                        "what",
                        "which",
                        "how many"
                    ],
                    "correct": "where",
                    "explanation": "Hỏi vị trí của địa điểm dùng từ để hỏi 'where'."
                },
                {
                    "id": 7,
                    "question": "We _____ in this city since 2018.",
                    "options": [
                        "have lived",
                        "lived",
                        "live",
                        "are living"
                    ],
                    "correct": "have lived",
                    "explanation": "Dấu hiệu 'since 2018' chỉ hành động bắt đầu từ quá khứ kéo dài đến hiện tại dùng Hiện tại hoàn thành."
                },
                {
                    "id": 8,
                    "question": "She didn't _____ any milk at the store.",
                    "options": [
                        "buy",
                        "bought",
                        "buys",
                        "buying"
                    ],
                    "correct": "buy",
                    "explanation": "Sau trợ động từ phủ định 'didn't', động từ trở về nguyên mẫu (V_inf)."
                },
                {
                    "id": 9,
                    "question": "If it rains tomorrow, we _____ stay at home.",
                    "options": [
                        "will",
                        "would",
                        "are",
                        "did"
                    ],
                    "correct": "will",
                    "explanation": "Câu điều kiện loại 1 diễn tả sự việc có thể xảy ra ở tương lai: If + V(s/es), S + will + V_inf."
                },
                {
                    "id": 10,
                    "question": "He is the _____ student in our English class.",
                    "options": [
                        "smartest",
                        "smarter",
                        "most smart",
                        "smart"
                    ],
                    "correct": "smartest",
                    "explanation": "So sánh nhất của tính từ ngắn 'smart' là 'the smartest'."
                },
                {
                    "id": 11,
                    "question": "What are you going to do _____ the weekend?",
                    "options": [
                        "at",
                        "in",
                        "to",
                        "for"
                    ],
                    "correct": "at",
                    "explanation": "Cụm từ chỉ thời gian: 'at the weekend' (UK) hoặc 'on the weekend' (US)."
                },
                {
                    "id": 12,
                    "question": "You _____ wear a helmet when riding a motorbike.",
                    "options": [
                        "must",
                        "can",
                        "might",
                        "shall"
                    ],
                    "correct": "must",
                    "explanation": "'Must' chỉ sự bắt buộc, quy định luật pháp."
                },
                {
                    "id": 13,
                    "question": "I enjoy _____ books in my free time.",
                    "options": [
                        "reading",
                        "read",
                        "to read",
                        "reads"
                    ],
                    "correct": "reading",
                    "explanation": "Sau động từ 'enjoy' là V-ing ('reading')."
                },
                {
                    "id": 14,
                    "question": "Excuse me, how _____ does this souvenir cost?",
                    "options": [
                        "much",
                        "many",
                        "price",
                        "often"
                    ],
                    "correct": "much",
                    "explanation": "Hỏi giá tiền dùng 'how much does it cost'."
                },
                {
                    "id": 15,
                    "question": "I visited Paris _____ 2022.",
                    "options": [
                        "in",
                        "at",
                        "on",
                        "since"
                    ],
                    "correct": "in",
                    "explanation": "Đi trước năm dùng giới từ 'in'."
                }
            ]
        }
    },
    "B1": {
        "level": "B1",
        "title": "CEFR B1 – Tiếng Anh Trung Cấp (Intermediate Threshold)",
        "badge": "Intermediate / Tự tin giao tiếp",
        "color": "#eab308",
        "target_audience": "Người muốn nâng cao khả năng đàm thoại, tự tin trình bày quan điểm, viết email và làm việc cơ bản.",
        "outcome": "Vốn từ 2500+, làm chủ Thì Hiện Tại Hoàn Thành, Câu Bị Động, Câu Điều Kiện Loại 1 & 2; tự tin bảo vệ ý kiến, mô tả ước mơ, thảo luận công việc.",
        "modules": [
            {
                "id": "b1-m1",
                "title": "Bài 1: Thì Hiện Tại Hoàn Thành & Trải Nghiệm Cá Nhân (Experiences)",
                "description": "Phân biệt Present Perfect và Past Simple, sử dụng các dấu hiệu already, yet, ever, never, since, for.",
                "duration_min": 35,
                "xp": 90,
                "theory": "Thì Hiện Tại Hoàn Thành (Present Perfect) diễn tả trải nghiệm cho tới hiện tại mà không đề cập thời gian cụ thể ('Have you ever visited London?'), hoặc hành động bắt đầu trong quá khứ và vẫn tiếp diễn ở hiện tại.",
                "key_vocab": [
                    {
                        "word": "Experience",
                        "ipa": "/ɪkˈspɪriəns/",
                        "meaning": "Kinh nghiệm / Trải nghiệm",
                        "example": "Traveling alone is a great experience."
                    },
                    {
                        "word": "Achievement",
                        "ipa": "/əˈtʃiːvmənt/",
                        "meaning": "Thành tựu",
                        "example": "Passing the B1 exam was a proud achievement."
                    },
                    {
                        "word": "Opportunity",
                        "ipa": "/ˌɑːpərˈtuːnəti/",
                        "meaning": "Cơ hội",
                        "example": "This job offers excellent career opportunities."
                    },
                    {
                        "word": "Challenge",
                        "ipa": "/ˈtʃælɪndʒ/",
                        "meaning": "Thử thách",
                        "example": "Learning a new language is a fun challenge."
                    },
                    {
                        "word": "Accomplish",
                        "ipa": "/əˈkɑːmplɪʃ/",
                        "meaning": "Hoàn thành / Đạt được",
                        "example": "We accomplished our project goals on time."
                    },
                    {
                        "word": "Manufacture",
                        "ipa": "/ˌmænjuˈfæktʃər/",
                        "meaning": "Sản xuất / Chế tạo",
                        "example": "These smartphones are manufactured locally."
                    },
                    {
                        "word": "Deadline",
                        "ipa": "/ˈdedlaɪn/",
                        "meaning": "Hạn chót",
                        "example": "The strict project deadline is next Friday."
                    },
                    {
                        "word": "Colleague",
                        "ipa": "/ˈkɑːliːɡ/",
                        "meaning": "Đồng nghiệp",
                        "example": "My colleagues are very supportive and skilled."
                    },
                    {
                        "word": "Implement",
                        "ipa": "/ˈɪmplɪment/",
                        "meaning": "Triển khai / Thực thi",
                        "example": "The management decided to implement new policies."
                    },
                    {
                        "word": "Coordinate",
                        "ipa": "/koʊˈɔːrdɪneɪt/",
                        "meaning": "Phối hợp / Điều phối",
                        "example": "She coordinates all team activities efficiently."
                    }
                ],
                "grammar_point": {
                    "rule": "Thì Hiện Tại Hoàn Thành: S + have/has + V3/ed",
                    "formula": "Khẳng định: S + have/has + V3/ed | Phủ định: S + have/has + not + V3/ed",
                    "examples": [
                        "I have worked at this company for three years. (Tôi đã làm việc tại công ty này được 3 năm.)",
                        "Have you ever tried scuba diving? (Bạn đã bao giờ thử lặn có bình khí chưa?)"
                    ]
                },
                "listening_task": {
                    "audio_text": "I have worked in digital marketing for five years, and during this time I have managed several international campaigns.",
                    "question": "How long has the speaker worked in marketing?",
                    "options": [
                        "3 years",
                        "5 years",
                        "8 years",
                        "10 years"
                    ],
                    "ans": "5 years",
                    "exp": "Audio nêu rõ: 'for five years'."
                },
                "speaking_prompt": {
                    "target_sentence": "I have studied English for two years and I have made significant progress.",
                    "ipa_focus": "/aɪ həv ˈstʌdid ˈɪŋɡlɪʃ fər tuː jɪrz/",
                    "tips": "Nối âm tự nhiên 'have made' và phát âm chuẩn âm /s/ trong 'progress'."
                },
                "writing_task": {
                    "prompt": "Viết đoạn văn 4 câu kể về một thành tựu hoặc trải nghiệm đáng nhớ nhất của bạn.",
                    "hint": "One of my proudest achievements is... I have learned how to... It has helped me...",
                    "sample_answer": "One of my proudest achievements is completing an online programming course. I have worked on various practical projects and learned how to build web applications. This experience has boosted my confidence significantly."
                },
                "dialogue": [
                    {
                        "speaker": "Emma",
                        "text": "Have you ever traveled abroad alone, John?"
                    },
                    {
                        "speaker": "John",
                        "text": "Yes, I have been to Japan twice. It was an eye-opening adventure."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "She _____ in this city since she was ten years old.",
                        "options": [
                            "has lived",
                            "lives",
                            "lived",
                            "is living"
                        ],
                        "ans": "has lived",
                        "exp": "Hành động từ quá khứ đến hiện tại với 'since' dùng thì Hiện tại hoàn thành."
                    },
                    {
                        "q": "Have you finished your assignment _____?",
                        "options": [
                            "yet",
                            "already",
                            "since",
                            "ever"
                        ],
                        "ans": "yet",
                        "exp": "Trong câu hỏi hiện tại hoàn thành đứng cuối câu dùng 'yet'."
                    }
                ]
            },
            {
                "id": "b1-m2",
                "title": "Bài 2: Câu Bị Động & Quy Trình Làm Việc (Passive Voice & Processes)",
                "description": "Chuyển đổi chủ động - bị động, ứng dụng trong mô tả quy trình sản xuất, công nghệ và dịch vụ.",
                "duration_min": 35,
                "xp": 95,
                "theory": "Câu bị động (Passive Voice) được dùng khi người nói muốn nhấn mạnh vào đối tượng chịu tác động của hành động thay vì người thực hiện hành động, thường thấy trong báo chí, tài liệu kỹ thuật và báo cáo công việc.",
                "key_vocab": [
                    {
                        "word": "Manufacture",
                        "ipa": "/ˌmænjuˈfæktʃər/",
                        "meaning": "Sản xuất / Chế tạo",
                        "example": "These smartphones are manufactured in Vietnam."
                    },
                    {
                        "word": "Implement",
                        "ipa": "/ˈɪmplɪment/",
                        "meaning": "Triển khai / Thực thi",
                        "example": "The new policy will be implemented next month."
                    },
                    {
                        "word": "Inspect",
                        "ipa": "/ɪnˈspekt/",
                        "meaning": "Kiểm tra kỹ lưỡng",
                        "example": "All components are inspected carefully."
                    },
                    {
                        "word": "Distribute",
                        "ipa": "/dɪˈstrɪbjuːt/",
                        "meaning": "Phân phối",
                        "example": "The products are distributed worldwide."
                    },
                    {
                        "word": "Accomplish",
                        "ipa": "/əˈkɑːmplɪʃ/",
                        "meaning": "Hoàn thành / Đạt được",
                        "example": "We accomplished our project goals on time."
                    },
                    {
                        "word": "Deadline",
                        "ipa": "/ˈdedlaɪn/",
                        "meaning": "Hạn chót",
                        "example": "The strict project deadline is next Friday."
                    },
                    {
                        "word": "Colleague",
                        "ipa": "/ˈkɑːliːɡ/",
                        "meaning": "Đồng nghiệp",
                        "example": "My colleagues are very supportive and skilled."
                    },
                    {
                        "word": "Coordinate",
                        "ipa": "/koʊˈɔːrdɪneɪt/",
                        "meaning": "Phối hợp / Điều phối",
                        "example": "She coordinates all team activities efficiently."
                    }
                ],
                "grammar_point": {
                    "rule": "Công thức câu bị động các thì: S + To Be (chia theo thì) + V3/ed (+ by O)",
                    "formula": "Hiện tại: S + am/is/are + V3 | Quá khứ: S + was/were + V3 | Tương lai: S + will be + V3",
                    "examples": [
                        "English is spoken all around the world.",
                        "The report was submitted yesterday afternoon."
                    ]
                },
                "listening_task": {
                    "audio_text": "Before shipment, each electric vehicle is thoroughly inspected by our quality assurance team to guarantee passenger safety.",
                    "question": "What happens before shipment?",
                    "options": [
                        "Vehicles are sold",
                        "Vehicles are inspected",
                        "Vehicles are painted",
                        "Vehicles are exported"
                    ],
                    "ans": "Vehicles are inspected",
                    "exp": "Audio nêu rõ: 'each electric vehicle is thoroughly inspected'."
                },
                "speaking_prompt": {
                    "target_sentence": "All customer feedback is carefully reviewed by our support department every morning.",
                    "ipa_focus": "/ɔːl ˈkʌstəmər ˈfiːdbæk ɪz ˈkeərfəli rɪˈvjuːd/",
                    "tips": "Nhấn trọng âm vào 'carefully reviewed' và 'support department'."
                },
                "writing_task": {
                    "prompt": "Viết 3 câu bị động mô tả quy trình xử lý đơn hàng tại một cửa hàng online.",
                    "hint": "Orders are placed... Then packages are prepared... Finally, items are delivered...",
                    "sample_answer": "First, orders are placed online by customers. Next, goods are carefully packed at the warehouse. Finally, packages are delivered to customers by express courier."
                },
                "dialogue": [
                    {
                        "speaker": "Manager",
                        "text": "Has the contract been signed by both parties yet?"
                    },
                    {
                        "speaker": "Assistant",
                        "text": "Yes, it was signed this morning and has already been sent to legal counsel."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "This famous bridge _____ in 1937.",
                        "options": [
                            "was built",
                            "is built",
                            "built",
                            "has built"
                        ],
                        "ans": "was built",
                        "exp": "Hành động xây cầu xảy ra và kết thúc trong quá khứ (1937) ở dạng bị động là 'was built'."
                    },
                    {
                        "q": "The new feature will _____ released next week.",
                        "options": [
                            "be",
                            "is",
                            "been",
                            "being"
                        ],
                        "ans": "be",
                        "exp": "Bị động tương lai: 'will be + V3/ed'."
                    }
                ]
            },
            {
                "id": "b1-m3",
                "title": "Bài 3: Câu Điều Kiện Loại 1 & 2 (Conditionals & Imaginary Scenarios)",
                "description": "Phân biệt tình huống có thể xảy ra ở hiện tại/tương lai (Type 1) và giả định trái thực tế (Type 2).",
                "duration_min": 35,
                "xp": 95,
                "theory": "Câu điều kiện loại 1: Diễn tả điều kiện có thật ở hiện tại/tương lai. Câu điều kiện loại 2: Diễn tả giả định không có thật hoặc khó xảy ra ở hiện tại ('If I were you, I would take the job.').",
                "key_vocab": [
                    {
                        "word": "Hypothetical",
                        "ipa": "/ˌhaɪpəˈθetɪkl/",
                        "meaning": "Mang tính giả định",
                        "example": "Let's consider a hypothetical situation."
                    },
                    {
                        "word": "Consequence",
                        "ipa": "/ˈkɑːnsəkwens/",
                        "meaning": "Hậu quả / Kết quả",
                        "example": "Every decision carries consequences."
                    },
                    {
                        "word": "Advise",
                        "ipa": "/ədˈvaɪz/",
                        "meaning": "Khuyên bảo",
                        "example": "I advise you to practice daily."
                    },
                    {
                        "word": "Promising",
                        "ipa": "/ˈprɑːmɪsɪŋ/",
                        "meaning": "Đầy triển vọng",
                        "example": "This is a promising opportunity."
                    },
                    {
                        "word": "Accomplish",
                        "ipa": "/əˈkɑːmplɪʃ/",
                        "meaning": "Hoàn thành / Đạt được",
                        "example": "We accomplished our project goals on time."
                    },
                    {
                        "word": "Manufacture",
                        "ipa": "/ˌmænjuˈfæktʃər/",
                        "meaning": "Sản xuất / Chế tạo",
                        "example": "These smartphones are manufactured locally."
                    },
                    {
                        "word": "Deadline",
                        "ipa": "/ˈdedlaɪn/",
                        "meaning": "Hạn chót",
                        "example": "The strict project deadline is next Friday."
                    },
                    {
                        "word": "Colleague",
                        "ipa": "/ˈkɑːliːɡ/",
                        "meaning": "Đồng nghiệp",
                        "example": "My colleagues are very supportive and skilled."
                    },
                    {
                        "word": "Implement",
                        "ipa": "/ˈɪmplɪment/",
                        "meaning": "Triển khai / Thực thi",
                        "example": "The management decided to implement new policies."
                    },
                    {
                        "word": "Coordinate",
                        "ipa": "/koʊˈɔːrdɪneɪt/",
                        "meaning": "Phối hợp / Điều phối",
                        "example": "She coordinates all team activities efficiently."
                    }
                ],
                "grammar_point": {
                    "rule": "Loại 1: If + S + V(s/es), S + will + V_inf | Loại 2: If + S + V2/were, S + would + V_inf",
                    "formula": "Type 1: If you study hard, you will pass. | Type 2: If I won the lottery, I would travel the world.",
                    "examples": [
                        "If I have free time this weekend, I will visit the art gallery.",
                        "If I were the CEO, I would invest more in artificial intelligence."
                    ]
                },
                "listening_task": {
                    "audio_text": "If our team secures the government grant, we will expand our AI laboratory and hire ten new researchers.",
                    "question": "What will happen if they get the grant?",
                    "options": [
                        "Close the lab",
                        "Expand the AI laboratory",
                        "Move to another country",
                        "Stop research"
                    ],
                    "ans": "Expand the AI laboratory",
                    "exp": "Audio nêu rõ: 'we will expand our AI laboratory'."
                },
                "speaking_prompt": {
                    "target_sentence": "If I had more free time, I would learn how to speak Spanish fluently.",
                    "ipa_focus": "/ɪf aɪ hæd mɔːr friː taɪm/",
                    "tips": "Hạ giọng nhẹ ở vế If và nhấn mạnh vào 'Spanish fluently'."
                },
                "writing_task": {
                    "prompt": "Viết 3 câu nêu điều bạn sẽ làm nếu trở thành một tỷ phú (Dùng câu điều kiện loại 2).",
                    "hint": "If I were a billionaire, I would... I would also...",
                    "sample_answer": "If I were a billionaire, I would establish charity funds for underprivileged children. I would also invest heavily in renewable energy and travel around the world."
                },
                "dialogue": [
                    {
                        "speaker": "David",
                        "text": "What would you do if you lost your passport in a foreign country?"
                    },
                    {
                        "speaker": "Sarah",
                        "text": "If that happened, I would immediately contact the local embassy for assistance."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "If I _____ you, I would accept the job offer immediately.",
                        "options": [
                            "were",
                            "am",
                            "was",
                            "be"
                        ],
                        "ans": "were",
                        "exp": "Trong câu điều kiện loại 2, 'were' được dùng chuẩn cho tất cả các ngôi chủ ngữ."
                    },
                    {
                        "q": "If it rains tomorrow, we _____ the outdoor concert.",
                        "options": [
                            "will cancel",
                            "canceled",
                            "would cancel",
                            "cancel"
                        ],
                        "ans": "will cancel",
                        "exp": "Câu điều kiện loại 1 mệnh đề chính dùng 'will + V_inf'."
                    }
                ]
            },
            {
                "id": "b1-m4",
                "title": "Bài 4: Động Từ Khuyết Thiếu Suy Đoán & Lời Khuyên (Modals of Deduction)",
                "description": "Sử dụng Must, Can't, Might, May để suy đoán khả năng xảy ra ở hiện tại và đưa ra khuyến nghị chuyên nghiệp.",
                "duration_min": 35,
                "xp": 95,
                "theory": "Suy đoán chắc chắn 99% dùng 'Must' ('He must be the new director'). Chắc chắn không thể dùng 'Can't' ('She can't be at home, I saw her at the office'). Khả năng 50% dùng 'Might / May / Could'.",
                "key_vocab": [
                    {
                        "word": "Deduction",
                        "ipa": "/dɪˈdʌkʃn/",
                        "meaning": "Sự suy luận logic",
                        "example": "Logical deduction is essential in detective work."
                    },
                    {
                        "word": "Plausible",
                        "ipa": "/ˈplɔːzəbl/",
                        "meaning": "Hợp lý / Có thể chấp nhận",
                        "example": "That explanation sounds plausible."
                    },
                    {
                        "word": "Probability",
                        "ipa": "/ˌprɑːbəˈbɪləti/",
                        "meaning": "Xác suất / Khả năng",
                        "example": "There is a high probability of rain."
                    },
                    {
                        "word": "Evidence",
                        "ipa": "/ˈevɪdəns/",
                        "meaning": "Bằng chứng",
                        "example": "The police collected substantial evidence."
                    },
                    {
                        "word": "Accomplish",
                        "ipa": "/əˈkɑːmplɪʃ/",
                        "meaning": "Hoàn thành / Đạt được",
                        "example": "We accomplished our project goals on time."
                    },
                    {
                        "word": "Manufacture",
                        "ipa": "/ˌmænjuˈfæktʃər/",
                        "meaning": "Sản xuất / Chế tạo",
                        "example": "These smartphones are manufactured locally."
                    },
                    {
                        "word": "Deadline",
                        "ipa": "/ˈdedlaɪn/",
                        "meaning": "Hạn chót",
                        "example": "The strict project deadline is next Friday."
                    },
                    {
                        "word": "Colleague",
                        "ipa": "/ˈkɑːliːɡ/",
                        "meaning": "Đồng nghiệp",
                        "example": "My colleagues are very supportive and skilled."
                    },
                    {
                        "word": "Implement",
                        "ipa": "/ˈɪmplɪment/",
                        "meaning": "Triển khai / Thực thi",
                        "example": "The management decided to implement new policies."
                    },
                    {
                        "word": "Coordinate",
                        "ipa": "/koʊˈɔːrdɪneɪt/",
                        "meaning": "Phối hợp / Điều phối",
                        "example": "She coordinates all team activities efficiently."
                    }
                ],
                "grammar_point": {
                    "rule": "Modals of deduction: Must / Can't / Might + V_inf (Hiện tại)",
                    "formula": "S + must/can't/might/may + V_inf",
                    "examples": [
                        "The lights are on, so someone must be inside.",
                        "He can't be ill; I just saw him playing football."
                    ]
                },
                "listening_task": {
                    "audio_text": "The conference room is completely booked for the entire morning, so the executive board must be having their annual meeting.",
                    "question": "What is the speaker's deduction about the meeting?",
                    "options": [
                        "It is canceled",
                        "The board must be having their meeting",
                        "Nobody is there",
                        "It will start tomorrow"
                    ],
                    "ans": "The board must be having their meeting",
                    "exp": "Audio suy đoán: 'the executive board must be having their annual meeting'."
                },
                "speaking_prompt": {
                    "target_sentence": "She has been working for ten consecutive hours, so she must be utterly exhausted.",
                    "ipa_focus": "/ʃi məst bi ˈʌtərli ɪɡˈzɔːstɪd/",
                    "tips": "Nhấn mạnh vào 'must be utterly exhausted'."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu suy đoán về một người vừa nhận được học bổng du học Mỹ.",
                    "hint": "He must feel very... He might be preparing...",
                    "sample_answer": "He must feel extremely thrilled after receiving the scholarship. He might be preparing all his visa documents right now."
                },
                "dialogue": [
                    {
                        "speaker": "Detective",
                        "text": "The front door was locked from the inside, so the culprit must have exited through the window."
                    },
                    {
                        "speaker": "Officer",
                        "text": "That is a very plausible deduction."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Look at his brand new sports car! He _____ be earning a huge salary.",
                        "options": [
                            "must",
                            "can't",
                            "shouldn't",
                            "mustn't"
                        ],
                        "ans": "must",
                        "exp": "Suy đoán chắc chắn ở hiện tại dựa trên bằng chứng dùng 'must'."
                    },
                    {
                        "q": "Mary _____ be in Paris right now; I had lunch with her in Hanoi two hours ago!",
                        "options": [
                            "can't",
                            "must",
                            "might",
                            "may"
                        ],
                        "ans": "can't",
                        "exp": "Suy đoán chắc chắn không thể xảy ra dùng 'can't'."
                    }
                ]
            },
            {
                "id": "b1-m5",
                "title": "Bài 5: Mệnh Đề Quan Hệ Xác Định & Không Xác Định (Relative Clauses)",
                "description": "Làm chủ Who, Whom, Whose, Which, That và phân biệt mệnh đề có dấu phẩy (Non-defining).",
                "duration_min": 35,
                "xp": 95,
                "theory": "Mệnh đề xác định (Defining) cung cấp thông tin bắt buộc, không có dấu phẩy. Mệnh đề không xác định (Non-defining) bổ sung thông tin phụ, ngăn cách bởi dấu phẩy và TUYỆT ĐỐI không dùng 'that'.",
                "key_vocab": [
                    {
                        "word": "Architect",
                        "ipa": "/ˈɑːrkɪtekt/",
                        "meaning": "Kiến trúc sư",
                        "example": "The architect who designed this building won an award."
                    },
                    {
                        "word": "Masterpiece",
                        "ipa": "/ˈmæstərpiːs/",
                        "meaning": "Kiệt tác",
                        "example": "The Mona Lisa is a timeless masterpiece."
                    },
                    {
                        "word": "Essential",
                        "ipa": "/ɪˈsenʃl/",
                        "meaning": "Thiết yếu",
                        "example": "Water is essential for life."
                    },
                    {
                        "word": "Landmark",
                        "ipa": "/ˈlændmɑːrk/",
                        "meaning": "Địa danh biểu tượng",
                        "example": "The Eiffel Tower is a famous landmark."
                    },
                    {
                        "word": "Accomplish",
                        "ipa": "/əˈkɑːmplɪʃ/",
                        "meaning": "Hoàn thành / Đạt được",
                        "example": "We accomplished our project goals on time."
                    },
                    {
                        "word": "Manufacture",
                        "ipa": "/ˌmænjuˈfæktʃər/",
                        "meaning": "Sản xuất / Chế tạo",
                        "example": "These smartphones are manufactured locally."
                    },
                    {
                        "word": "Deadline",
                        "ipa": "/ˈdedlaɪn/",
                        "meaning": "Hạn chót",
                        "example": "The strict project deadline is next Friday."
                    },
                    {
                        "word": "Colleague",
                        "ipa": "/ˈkɑːliːɡ/",
                        "meaning": "Đồng nghiệp",
                        "example": "My colleagues are very supportive and skilled."
                    },
                    {
                        "word": "Implement",
                        "ipa": "/ˈɪmplɪment/",
                        "meaning": "Triển khai / Thực thi",
                        "example": "The management decided to implement new policies."
                    },
                    {
                        "word": "Coordinate",
                        "ipa": "/koʊˈɔːrdɪneɪt/",
                        "meaning": "Phối hợp / Điều phối",
                        "example": "She coordinates all team activities efficiently."
                    }
                ],
                "grammar_point": {
                    "rule": "Defining vs Non-defining Relative Clauses",
                    "formula": "Non-defining: Noun, who/which/whose + clause, + Main Verb...",
                    "examples": [
                        "Dr. Smith, who graduated from Harvard, is leading the research.",
                        "The laptop which I bought yesterday runs smoothly."
                    ]
                },
                "listening_task": {
                    "audio_text": "Professor Nguyen, who has spent twenty years studying marine biology, published a groundbreaking paper on coral reefs.",
                    "question": "What is true about Professor Nguyen?",
                    "options": [
                        "He is a student",
                        "He spent 20 years studying marine biology",
                        "He is an architect",
                        "He just started research"
                    ],
                    "ans": "He spent 20 years studying marine biology",
                    "exp": "Audio bổ sung thông tin qua mệnh đề quan hệ: 'who has spent twenty years studying marine biology'."
                },
                "speaking_prompt": {
                    "target_sentence": "My brother, who lives in Melbourne, is coming to visit us next Christmas.",
                    "ipa_focus": "/maɪ ˈbrʌðər huː lɪvz ɪn ˈmelbərn/",
                    "tips": "Ngắt nghỉ nhẹ ở 2 vị trí dấu phẩy trước và sau mệnh đề quan hệ."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu giới thiệu về một người bạn hoặc một địa danh du lịch có sử dụng mệnh đề quan hệ.",
                    "hint": "Da Nang, which is located in central Vietnam, is famous for... My teacher, who...",
                    "sample_answer": "Da Nang, which is a coastal city in central Vietnam, is famous for its picturesque beaches. My English mentor, who holds a master's degree in linguistics, inspired me to study abroad."
                },
                "dialogue": [
                    {
                        "speaker": "Guide",
                        "text": "This ancient citadel, which was built in 1802, attracts millions of tourists every year."
                    },
                    {
                        "speaker": "Tourist",
                        "text": "The preservation work done here is truly remarkable."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "My uncle, _____ works for the United Nations, travels to Geneva frequently.",
                        "options": [
                            "who",
                            "that",
                            "which",
                            "whom"
                        ],
                        "ans": "who",
                        "exp": "Trong mệnh đề không xác định (có dấu phẩy) chỉ người, dùng 'who', không được dùng 'that'."
                    },
                    {
                        "q": "The company _____ innovative software revolutionized mobile banking has gone public.",
                        "options": [
                            "whose",
                            "who",
                            "which",
                            "whom"
                        ],
                        "ans": "whose",
                        "exp": "Chỉ sở hữu (phần mềm của công ty) dùng đại từ quan hệ 'whose'."
                    }
                ]
            },
            {
                "id": "b1-m6",
                "title": "Bài 6: Giao Tiếp Công Sở, Viết Email & Trình Bày Ý Kiến (Workplace English)",
                "description": "Viết email trao đổi công việc chuyên nghiệp, mở đầu/kết thư lịch sự, đưa đề xuất và nêu quan điểm.",
                "duration_min": 35,
                "xp": 100,
                "theory": "Mẫu câu mở đầu email: 'I am writing to inquire about...', 'Further to our previous conversation...'. Kết thư: 'I look forward to hearing from you.', 'Best regards'. Nêu quan điểm: 'In my view', 'From my standpoint'.",
                "key_vocab": [
                    {
                        "word": "Inquire",
                        "ipa": "/ɪnˈkwaɪər/",
                        "meaning": "Hỏi thăm / Thắc mắc",
                        "example": "I am writing to inquire about the job vacancy."
                    },
                    {
                        "word": "Collaborate",
                        "ipa": "/kəˈlæbəreɪt/",
                        "meaning": "Hợp tác làm việc",
                        "example": "We collaborate with international research teams."
                    },
                    {
                        "word": "Deadline",
                        "ipa": "/ˈdedlaɪn/",
                        "meaning": "Hạn chót",
                        "example": "The project deadline has been extended to Friday."
                    },
                    {
                        "word": "Feedback",
                        "ipa": "/ˈfiːdbæk/",
                        "meaning": "Phản hồi",
                        "example": "Constructive feedback helps improve product quality."
                    },
                    {
                        "word": "Accomplish",
                        "ipa": "/əˈkɑːmplɪʃ/",
                        "meaning": "Hoàn thành / Đạt được",
                        "example": "We accomplished our project goals on time."
                    },
                    {
                        "word": "Manufacture",
                        "ipa": "/ˌmænjuˈfæktʃər/",
                        "meaning": "Sản xuất / Chế tạo",
                        "example": "These smartphones are manufactured locally."
                    },
                    {
                        "word": "Colleague",
                        "ipa": "/ˈkɑːliːɡ/",
                        "meaning": "Đồng nghiệp",
                        "example": "My colleagues are very supportive and skilled."
                    },
                    {
                        "word": "Implement",
                        "ipa": "/ˈɪmplɪment/",
                        "meaning": "Triển khai / Thực thi",
                        "example": "The management decided to implement new policies."
                    },
                    {
                        "word": "Coordinate",
                        "ipa": "/koʊˈɔːrdɪneɪt/",
                        "meaning": "Phối hợp / Điều phối",
                        "example": "She coordinates all team activities efficiently."
                    }
                ],
                "grammar_point": {
                    "rule": "Cấu trúc đề xuất lịch sự: Would you mind + V-ing? / Could you please + V_inf?",
                    "formula": "Would you mind + V-ing...? | I would appreciate it if you could + V_inf...",
                    "examples": [
                        "Would you mind reviewing this draft proposal?",
                        "I would appreciate it if you could send the updated invoice."
                    ]
                },
                "listening_task": {
                    "audio_text": "Good morning team. Please ensure all quarterly financial spreadsheets are submitted to the finance manager before 5 PM today.",
                    "question": "What is the deadline for submitting the spreadsheets?",
                    "options": [
                        "12 PM today",
                        "5 PM today",
                        "Tomorrow morning",
                        "Next Monday"
                    ],
                    "ans": "5 PM today",
                    "exp": "Audio nêu rõ: 'before 5 PM today'."
                },
                "speaking_prompt": {
                    "target_sentence": "I am writing to confirm our scheduled video conference for tomorrow morning at nine.",
                    "ipa_focus": "/aɪ əm ˈraɪtɪŋ tə kənˈfɜːrm/",
                    "tips": "Giọng điệu chuyên nghiệp, dứt khoát và rõ ràng."
                },
                "writing_task": {
                    "prompt": "Viết email ngắn 4 câu gửi đồng nghiệp nhờ xem xét và phản hồi lại bản kế hoạch dự án.",
                    "hint": "Dear [Name], I hope this email finds you well... Attached is the draft... Could you please review... Best regards.",
                    "sample_answer": "Dear Nam, I hope this email finds you well. Attached is the latest draft of our marketing proposal for Q3. Could you please review the budget allocation and share your feedback by tomorrow afternoon? Thank you for your assistance. Best regards, Linh."
                },
                "dialogue": [
                    {
                        "speaker": "Alice",
                        "text": "Have you reviewed the revised budget breakdown?"
                    },
                    {
                        "speaker": "Bob",
                        "text": "Yes, everything looks solid. I will forward it to accounting immediately."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Would you mind _____ me with these financial reports?",
                        "options": [
                            "helping",
                            "help",
                            "to help",
                            "helped"
                        ],
                        "ans": "helping",
                        "exp": "Sau 'Would you mind' dùng động từ V-ing ('helping')."
                    },
                    {
                        "q": "Choose the most appropriate sign-off for a formal business email:",
                        "options": [
                            "Best regards,",
                            "See ya!",
                            "Cheers mate,",
                            "Bye bye,"
                        ],
                        "ans": "Best regards,",
                        "exp": "'Best regards,' là cách kết thư trang trọng và chuyên nghiệp chuẩn mực."
                    }
                ]
            }
        ],
        "exam": {
            "title": "Bài Thi Chuẩn Đầu Ra CEFR B1 (Intermediate Mastery Test)",
            "time_min": 30,
            "pass_score": 75,
            "questions": [
                {
                    "id": 1,
                    "question": "By the time we arrived at the concert, the band _____ performing.",
                    "options": [
                        "had already started",
                        "already started",
                        "has started",
                        "starts"
                    ],
                    "correct": "had already started",
                    "explanation": "Hành động xảy ra trước một thời điểm trong quá khứ dùng Quá khứ hoàn thành (Past Perfect)."
                },
                {
                    "id": 2,
                    "question": "The new hospital _____ by the prime minister next Monday.",
                    "options": [
                        "will be inaugurated",
                        "is inaugurated",
                        "inaugurates",
                        "has inaugurated"
                    ],
                    "correct": "will be inaugurated",
                    "explanation": "Bị động ở tương lai: 'will be + V3/ed'."
                },
                {
                    "id": 3,
                    "question": "If she _____ harder, she would pass the Cambridge exam easily.",
                    "options": [
                        "studied",
                        "studies",
                        "will study",
                        "study"
                    ],
                    "correct": "studied",
                    "explanation": "Vế điều kiện trong câu loại 2: If + S + V2/ed."
                },
                {
                    "id": 4,
                    "question": "I am not used to _____ up so early on cold winter mornings.",
                    "options": [
                        "waking",
                        "wake",
                        "woke",
                        "woken"
                    ],
                    "correct": "waking",
                    "explanation": "Cấu trúc 'be used to + V-ing' nghĩa là quen với việc gì."
                },
                {
                    "id": 5,
                    "question": "The manager asked me _____ I had finished the financial report.",
                    "options": [
                        "if",
                        "what",
                        "that",
                        "weather"
                    ],
                    "correct": "if",
                    "explanation": "Câu tường thuật dạng câu hỏi Yes/No dùng 'if' hoặc 'whether'."
                },
                {
                    "id": 6,
                    "question": "Despite _____ heavily, the marathon runners continued their race.",
                    "options": [
                        "raining",
                        "it rained",
                        "of rain",
                        "rains"
                    ],
                    "correct": "raining",
                    "explanation": "Sau giới từ 'Despite' là danh từ hoặc V-ing."
                },
                {
                    "id": 7,
                    "question": "This smartphone is equipped _____ advanced facial recognition technology.",
                    "options": [
                        "with",
                        "by",
                        "for",
                        "to"
                    ],
                    "correct": "with",
                    "explanation": "Cụm 'equipped with' nghĩa là được trang bị với."
                },
                {
                    "id": 8,
                    "question": "He succeeded in passing the interview _____ his thorough preparation.",
                    "options": [
                        "due to",
                        "although",
                        "even though",
                        "because"
                    ],
                    "correct": "due to",
                    "explanation": "Sau 'due to' là một cụm danh từ (his thorough preparation)."
                },
                {
                    "id": 9,
                    "question": "I would rather you _____ not tell anyone about our secret.",
                    "options": [
                        "did",
                        "do",
                        "would",
                        "had"
                    ],
                    "correct": "did",
                    "explanation": "Cấu trúc 'would rather S + V_past' dùng để diễn tả mong muốn ai đó làm/không làm gì ở hiện tại."
                },
                {
                    "id": 10,
                    "question": "The teacher suggested that we _____ more practice tests before the final exam.",
                    "options": [
                        "take",
                        "took",
                        "taking",
                        "taken"
                    ],
                    "correct": "take",
                    "explanation": "Thể giả định (Subjunctive): S + suggest that + S + (should) + V_inf."
                },
                {
                    "id": 11,
                    "question": "Neither John nor his colleagues _____ willing to accept the compromise.",
                    "options": [
                        "were",
                        "was",
                        "is",
                        "be"
                    ],
                    "correct": "were",
                    "explanation": "Cấu trúc 'Neither S1 nor S2' động từ hòa hợp theo S2 số nhiều 'his colleagues'."
                },
                {
                    "id": 12,
                    "question": "The book _____ you recommended was truly captivating.",
                    "options": [
                        "which",
                        "who",
                        "whom",
                        "where"
                    ],
                    "correct": "which",
                    "explanation": "Đại từ quan hệ thay thế cho danh từ chỉ vật 'The book' là 'which' hoặc 'that'."
                },
                {
                    "id": 13,
                    "question": "You shouldn't have _____ that confidential file without permission.",
                    "options": [
                        "deleted",
                        "delete",
                        "deleting",
                        "deletes"
                    ],
                    "correct": "deleted",
                    "explanation": "'Should have + V3' chỉ sự việc lẽ ra nên/không nên làm trong quá khứ."
                },
                {
                    "id": 14,
                    "question": "We are looking forward to _____ your delegation next week.",
                    "options": [
                        "meeting",
                        "meet",
                        "met",
                        "have met"
                    ],
                    "correct": "meeting",
                    "explanation": "Cụm 'look forward to + V-ing' nghĩa là mong chờ điều gì."
                },
                {
                    "id": 15,
                    "question": "He has lived in Germany for five years; _____, his German is still basic.",
                    "options": [
                        "however",
                        "therefore",
                        "moreover",
                        "otherwise"
                    ],
                    "correct": "however",
                    "explanation": "'However' (tuy nhiên) dùng để nối hai vế có ý nghĩa tương phản."
                }
            ]
        }
    },
    "B2": {
        "level": "B2",
        "title": "CEFR B2 – Trung Cao Cấp (Vantage Academic & Professional)",
        "badge": "Upper-Intermediate / Thành thạo học thuật",
        "color": "#f97316",
        "target_audience": "Học sinh sinh viên thi IELTS 6.0-6.5, du học sinh, nhân viên làm việc môi trường quốc tế cần viết luận và thuyết trình lưu loát.",
        "outcome": "Vốn từ 4000+, sử dụng thành thạo Mệnh Đề Quan Hệ Rút Gọn, Đảo Ngữ cơ bản, Câu Điều Kiện Hỗn Hợp; viết luận phân tích mạch lạc và phản biện tự tin.",
        "modules": [
            {
                "id": "b2-m1",
                "title": "Bài 1: Mệnh Đề Quan Hệ Nâng Cao & Rút Gọn (Reduced Relative Clauses)",
                "description": "Làm chủ kỹ thuật rút gọn mệnh đề dạng V-ing (chủ động), V3/ed (bị động) và To-V để câu văn học thuật cô đọng.",
                "duration_min": 40,
                "xp": 100,
                "theory": "Kỹ thuật rút gọn mệnh đề quan hệ (Reduced Relative Clauses) là điểm phân biệt giữa người học trung cấp và cao cấp. Dạng chủ động rút thành V-ing ('The woman who is standing there' -> 'The woman standing there'). Dạng bị động rút thành V3/ed ('The research that was conducted in 2024' -> 'The research conducted in 2024').",
                "key_vocab": [
                    {
                        "word": "Comprehensive",
                        "ipa": "/ˌkɑːmprɪˈhensɪv/",
                        "meaning": "Toàn diện / Bao quát",
                        "example": "The committee presented a comprehensive analysis."
                    },
                    {
                        "word": "Correlation",
                        "ipa": "/ˌkɔːrəˈleɪʃn/",
                        "meaning": "Mối tương quan",
                        "example": "Studies show a positive correlation between exercise and longevity."
                    },
                    {
                        "word": "Facilitate",
                        "ipa": "/fəˈsɪlɪteɪt/",
                        "meaning": "Tạo điều kiện thuận lợi",
                        "example": "Modern tools facilitate collaborative research."
                    },
                    {
                        "word": "Discrepancy",
                        "ipa": "/dɪˈskrepənsi/",
                        "meaning": "Sự sai lệch / Khác biệt",
                        "example": "Auditors noticed a slight discrepancy in the figures."
                    },
                    {
                        "word": "Nevertheless",
                        "ipa": "/ˌnevərðəˈles/",
                        "meaning": "Tuy nhiên / Dẫu vậy",
                        "example": "The challenge was huge; nevertheless, we succeeded."
                    },
                    {
                        "word": "Substantiate",
                        "ipa": "/səbˈstænʃieɪt/",
                        "meaning": "Chứng minh / Cung cấp bằng chứng",
                        "example": "You must substantiate your arguments with empirical data."
                    },
                    {
                        "word": "Perspective",
                        "ipa": "/pərˈspektɪv/",
                        "meaning": "Góc nhìn / Quan điểm",
                        "example": "Let us examine the issue from a global perspective."
                    }
                ],
                "grammar_point": {
                    "rule": "Rút gọn mệnh đề quan hệ: Chủ động (V-ing), Bị động (V3/ed), Dạng số thứ tự / The only (To-V)",
                    "formula": "Active: Noun + V-ing | Passive: Noun + V3/ed | First/Last/Only: Noun + To-V",
                    "examples": [
                        "Students achieving high scores will receive academic scholarships.",
                        "Neil Armstrong was the first man to walk on the moon."
                    ]
                },
                "listening_task": {
                    "audio_text": "The environmental report published yesterday highlights several alarming trends affecting global coral reef ecosystems.",
                    "question": "What does the newly published report highlight?",
                    "options": [
                        "Economic growth",
                        "Alarming trends in coral reefs",
                        "Tourism expansion",
                        "Space exploration"
                    ],
                    "ans": "Alarming trends in coral reefs",
                    "exp": "Audio nêu rõ: 'highlights several alarming trends affecting coral reef ecosystems'."
                },
                "speaking_prompt": {
                    "target_sentence": "Researchers conducting clinical trials have observed substantial improvements in patient recovery times.",
                    "ipa_focus": "/rɪˈsɜːrtʃərz kənˈdʌktɪŋ ˈklɪnɪkl ˈtraɪəlz/",
                    "tips": "Giữ nhịp điệu học thuật đều đặn, ngắt nghỉ đúng cụm danh từ rút gọn."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu học thuật sử dụng mệnh đề quan hệ rút gọn (1 câu chủ động V-ing, 1 câu bị động V3/ed).",
                    "hint": "Individuals engaging in... Products manufactured in...",
                    "sample_answer": "Individuals engaging in regular physical exercise demonstrate higher levels of cognitive endurance. Furthermore, electronic components manufactured under strict standards exhibit minimal failure rates."
                },
                "dialogue": [
                    {
                        "speaker": "Professor",
                        "text": "Have you reviewed the findings outlined in section three?"
                    },
                    {
                        "speaker": "Researcher",
                        "text": "Yes, the data gathered from the laboratory trials confirmed our initial hypothesis."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "The scientist _____ the breakthrough Nobel prize will deliver the keynote address.",
                        "options": [
                            "awarded",
                            "awarding",
                            "was awarded",
                            "who awarded"
                        ],
                        "ans": "awarded",
                        "exp": "Rút gọn mệnh đề bị động 'who was awarded' thành 'awarded'."
                    },
                    {
                        "q": "The woman _____ next to Dr. Brown is our department chair.",
                        "options": [
                            "standing",
                            "stood",
                            "is standing",
                            "stands"
                        ],
                        "ans": "standing",
                        "exp": "Rút gọn mệnh đề chủ động 'who is standing' thành 'standing'."
                    }
                ]
            },
            {
                "id": "b2-m2",
                "title": "Bài 2: Đảo Ngữ Nhấn Mạnh & Diễn Thuyết Phản Biện (Inversion for Emphasis)",
                "description": "Sử dụng đảo ngữ với trạng từ phủ định (Not only, Seldom, Rarely, Under no circumstances) để nâng cấp bài nói và viết luận.",
                "duration_min": 40,
                "xp": 105,
                "theory": "Đảo ngữ (Inversion) đưa trạng từ phủ định hoặc bán phủ định lên đầu câu để tạo ấn tượng mạnh mẽ và trang trọng. Cấu trúc: Trạng từ phủ định + Trợ động từ + Chủ ngữ + Động từ chính.",
                "key_vocab": [
                    {
                        "word": "Unprecedented",
                        "ipa": "/ʌnˈpresɪdentɪd/",
                        "meaning": "Chưa từng có tiền lệ",
                        "example": "The city witnessed unprecedented economic growth."
                    },
                    {
                        "word": "Perspective",
                        "ipa": "/pərˈspektɪv/",
                        "meaning": "Góc nhìn / Quan điểm",
                        "example": "We must analyze this issue from a broader perspective."
                    },
                    {
                        "word": "Controversy",
                        "ipa": "/ˈkɑːntrəvɜːrsi/",
                        "meaning": "Sự tranh cãi",
                        "example": "The proposal provoked heated controversy among scholars."
                    },
                    {
                        "word": "Substantial",
                        "ipa": "/səbˈstænʃl/",
                        "meaning": "Đáng kể / To lớn",
                        "example": "They made substantial progress in reducing emissions."
                    },
                    {
                        "word": "Comprehensive",
                        "ipa": "/ˌkɑːmprɪˈhensɪv/",
                        "meaning": "Toàn diện / Bao quát",
                        "example": "We conducted a comprehensive market analysis."
                    },
                    {
                        "word": "Nevertheless",
                        "ipa": "/ˌnevərðəˈles/",
                        "meaning": "Tuy nhiên / Dẫu vậy",
                        "example": "The challenge was huge; nevertheless, we succeeded."
                    },
                    {
                        "word": "Substantiate",
                        "ipa": "/səbˈstænʃieɪt/",
                        "meaning": "Chứng minh / Cung cấp bằng chứng",
                        "example": "You must substantiate your arguments with empirical data."
                    },
                    {
                        "word": "Discrepancy",
                        "ipa": "/dɪˈskrepənsi/",
                        "meaning": "Sự khác biệt / Điểm bất đồng",
                        "example": "There is a minor discrepancy in the quarterly financial report."
                    },
                    {
                        "word": "Facilitate",
                        "ipa": "/fəˈsɪlɪteɪt/",
                        "meaning": "Tạo điều kiện thuận lợi",
                        "example": "The new software facilitates seamless cross-border communication."
                    }
                ],
                "grammar_point": {
                    "rule": "Cấu trúc đảo ngữ: Negative adverb + Aux + S + V",
                    "formula": "Not only + aux + S + V, but S also... | Seldom/Rarely + aux + S + V...",
                    "examples": [
                        "Not only does renewable energy reduce emissions, but it also creates green jobs.",
                        "Under no circumstances should sensitive data be shared publicly."
                    ]
                },
                "listening_task": {
                    "audio_text": "Seldom have we witnessed such rapid technological transformation across every sector of global commerce.",
                    "question": "What has rarely been witnessed according to the speaker?",
                    "options": [
                        "A decrease in trade",
                        "Rapid technological transformation",
                        "Slow economic changes",
                        "Political elections"
                    ],
                    "ans": "Rapid technological transformation",
                    "exp": "Audio nêu rõ: 'Seldom have we witnessed such rapid technological transformation'."
                },
                "speaking_prompt": {
                    "target_sentence": "Not only did the startup achieve profitability within six months, but it also expanded internationally.",
                    "ipa_focus": "/nɑːt ˈoʊnli dɪd ðə ˈstɑːrtʌp əˈtʃiːv/",
                    "tips": "Nhấn mạnh có lực vào từ 'Not only' và giữ hơi vững khi nói mệnh đề sau."
                },
                "writing_task": {
                    "prompt": "Viết đoạn văn ngắn 3 câu sử dụng ít nhất 1 cấu trúc đảo ngữ để lập luận về tầm quan trọng của giáo dục.",
                    "hint": "Not only does education empower... Seldom do countries flourish without...",
                    "sample_answer": "Education is undeniably the cornerstone of modern civilization. Not only does quality education empower individuals with critical thinking, but it also fosters sustainable socioeconomic development. Seldom do nations prosper without investing heavily in their academic institutions."
                },
                "dialogue": [
                    {
                        "speaker": "Debater A",
                        "text": "Under no circumstances can we compromise on environmental safety protocols."
                    },
                    {
                        "speaker": "Debater B",
                        "text": "I completely agree; rarely has deregulation led to sustainable long-term prosperity."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Rarely _____ such dedication among undergraduate researchers.",
                        "options": [
                            "have I seen",
                            "I have seen",
                            "did I saw",
                            "I saw"
                        ],
                        "ans": "have I seen",
                        "exp": "Đảo ngữ với trạng từ bán phủ định 'Rarely' đưa trợ động từ 'have' lên trước chủ ngữ 'I'."
                    },
                    {
                        "q": "Not only _____ the exam with honors, but she also won first prize in the debate.",
                        "options": [
                            "did she pass",
                            "she passed",
                            "passed she",
                            "she had passed"
                        ],
                        "ans": "did she pass",
                        "exp": "Đảo ngữ với 'Not only' trong quá khứ đơn: 'did she pass'."
                    }
                ]
            },
            {
                "id": "b2-m3",
                "title": "Bài 3: Câu Điều Kiện Loại 3 & Hỗn Hợp (Third & Mixed Conditionals)",
                "description": "Diễn đạt sự hối tiếc, giả định trái ngược với quá khứ và kết quả liên đới đến hiện tại.",
                "duration_min": 40,
                "xp": 105,
                "theory": "Điều kiện loại 3: If + had + V3, S + would have + V3 (giả định quá khứ). Điều kiện hỗn hợp (Mixed Conditionals): Giả định quá khứ dẫn đến kết quả hiện tại ('If I had studied harder in college, I would have a better job now').",
                "key_vocab": [
                    {
                        "word": "Retrospect",
                        "ipa": "/ˈretrəspekt/",
                        "meaning": "Nhìn lại quá khứ",
                        "example": "In retrospect, we made the right decision."
                    },
                    {
                        "word": "Unforeseen",
                        "ipa": "/ˌʌnfɔːrˈsiːn/",
                        "meaning": "Không lường trước được",
                        "example": "We encountered unforeseen technical complications."
                    },
                    {
                        "word": "Regret",
                        "ipa": "/rɪˈɡret/",
                        "meaning": "Hối tiếc",
                        "example": "He expressed deep regret over the mistake."
                    },
                    {
                        "word": "Outcome",
                        "ipa": "/ˈaʊtkʌm/",
                        "meaning": "Kết quả cuối cùng",
                        "example": "The final outcome exceeded our expectations."
                    },
                    {
                        "word": "Comprehensive",
                        "ipa": "/ˌkɑːmprɪˈhensɪv/",
                        "meaning": "Toàn diện / Bao quát",
                        "example": "We conducted a comprehensive market analysis."
                    },
                    {
                        "word": "Nevertheless",
                        "ipa": "/ˌnevərðəˈles/",
                        "meaning": "Tuy nhiên / Dẫu vậy",
                        "example": "The challenge was huge; nevertheless, we succeeded."
                    },
                    {
                        "word": "Substantiate",
                        "ipa": "/səbˈstænʃieɪt/",
                        "meaning": "Chứng minh / Cung cấp bằng chứng",
                        "example": "You must substantiate your arguments with empirical data."
                    },
                    {
                        "word": "Discrepancy",
                        "ipa": "/dɪˈskrepənsi/",
                        "meaning": "Sự khác biệt / Điểm bất đồng",
                        "example": "There is a minor discrepancy in the quarterly financial report."
                    },
                    {
                        "word": "Perspective",
                        "ipa": "/pərˈspektɪv/",
                        "meaning": "Góc nhìn / Quan điểm",
                        "example": "Let us examine the issue from a global perspective."
                    },
                    {
                        "word": "Facilitate",
                        "ipa": "/fəˈsɪlɪteɪt/",
                        "meaning": "Tạo điều kiện thuận lợi",
                        "example": "The new software facilitates seamless cross-border communication."
                    }
                ],
                "grammar_point": {
                    "rule": "Mixed Conditionals (Quá khứ -> Hiện tại)",
                    "formula": "If + S + had + V3/ed, S + would + V_inf (now)",
                    "examples": [
                        "If we had invested in AI five years ago, our company would be the market leader today.",
                        "If she had taken the earlier flight, she would be in Tokyo right now."
                    ]
                },
                "listening_task": {
                    "audio_text": "If our engineering team had conducted stress testing earlier, we would not be facing these critical server outages today.",
                    "question": "What caused the current server outage?",
                    "options": [
                        "Power failure",
                        "Lack of early stress testing",
                        "Cyber attack",
                        "Hardware theft"
                    ],
                    "ans": "Lack of early stress testing",
                    "exp": "Audio nêu rõ: 'If our engineering team had conducted stress testing earlier, we would not be facing these outages today'."
                },
                "speaking_prompt": {
                    "target_sentence": "If I had mastered English five years ago, I would be leading international projects right now.",
                    "ipa_focus": "/ɪf aɪ həd ˈmæstərd ˈɪŋɡlɪʃ/",
                    "tips": "Nhấn mạnh 'mastered English' và 'leading international projects'."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu điều kiện hỗn hợp giả định về một quyết định học tập hoặc công việc trong quá khứ đã ảnh hưởng đến bạn hôm nay.",
                    "hint": "If I had chosen... I would be...",
                    "sample_answer": "If I had dedicated more time to studying artificial intelligence during university, I would be working as a machine learning engineer today."
                },
                "dialogue": [
                    {
                        "speaker": "Executive",
                        "text": "If we had signed the partnership agreement last quarter, we would have dominated the European market by now."
                    },
                    {
                        "speaker": "Advisor",
                        "text": "True, but in retrospect, waiting allowed us to secure much better valuation terms."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "If he _____ his passport yesterday, he would be flying to London today.",
                        "options": [
                            "hadn't lost",
                            "didn't lose",
                            "hasn't lost",
                            "wouldn't lose"
                        ],
                        "ans": "hadn't lost",
                        "exp": "Vế điều kiện trong quá khứ của câu điều kiện hỗn hợp dùng 'hadn't + V3'."
                    },
                    {
                        "q": "Had they informed us earlier, we _____ alternative arrangements.",
                        "options": [
                            "would have made",
                            "will make",
                            "made",
                            "would make"
                        ],
                        "ans": "would have made",
                        "exp": "Đảo ngữ câu điều kiện loại 3: 'Had + S + V3, S + would have + V3'."
                    }
                ]
            },
            {
                "id": "b2-m4",
                "title": "Bài 4: Thể Giả Định & Động Từ Cầu Khiến (Subjunctive & Causative Verbs)",
                "description": "Sử dụng cấu trúc 'recommend / suggest that S + V_inf' và động từ cầu khiến (Have/Get something done).",
                "duration_min": 40,
                "xp": 105,
                "theory": "Thể giả định hiện tại (Present Subjunctive) dùng động từ nguyên mẫu không 'to' sau các động từ/tính từ yêu cầu, đề xuất: recommend, insist, suggest, crucial, vital, imperative. Thể cầu khiến: 'have something done' (thuê/nhờ ai làm gì).",
                "key_vocab": [
                    {
                        "word": "Imperative",
                        "ipa": "/ɪmˈperətɪv/",
                        "meaning": "Cấp bách / Bắt buộc",
                        "example": "It is imperative that we adhere to safety standards."
                    },
                    {
                        "word": "Mandatory",
                        "ipa": "/ˈmændətɔːri/",
                        "meaning": "Mang tính bắt buộc",
                        "example": "Attendance at the seminar is mandatory."
                    },
                    {
                        "word": "Stipulate",
                        "ipa": "/ˈstɪpjuleɪt/",
                        "meaning": "Quy định rõ trong điều khoản",
                        "example": "The contract stipulates that payments be made monthly."
                    },
                    {
                        "word": "Crucial",
                        "ipa": "/ˈkruːʃl/",
                        "meaning": "Tối quan trọng",
                        "example": "Early detection is crucial for successful treatment."
                    },
                    {
                        "word": "Comprehensive",
                        "ipa": "/ˌkɑːmprɪˈhensɪv/",
                        "meaning": "Toàn diện / Bao quát",
                        "example": "We conducted a comprehensive market analysis."
                    },
                    {
                        "word": "Nevertheless",
                        "ipa": "/ˌnevərðəˈles/",
                        "meaning": "Tuy nhiên / Dẫu vậy",
                        "example": "The challenge was huge; nevertheless, we succeeded."
                    },
                    {
                        "word": "Substantiate",
                        "ipa": "/səbˈstænʃieɪt/",
                        "meaning": "Chứng minh / Cung cấp bằng chứng",
                        "example": "You must substantiate your arguments with empirical data."
                    },
                    {
                        "word": "Discrepancy",
                        "ipa": "/dɪˈskrepənsi/",
                        "meaning": "Sự khác biệt / Điểm bất đồng",
                        "example": "There is a minor discrepancy in the quarterly financial report."
                    },
                    {
                        "word": "Perspective",
                        "ipa": "/pərˈspektɪv/",
                        "meaning": "Góc nhìn / Quan điểm",
                        "example": "Let us examine the issue from a global perspective."
                    },
                    {
                        "word": "Facilitate",
                        "ipa": "/fəˈsɪlɪteɪt/",
                        "meaning": "Tạo điều kiện thuận lợi",
                        "example": "The new software facilitates seamless cross-border communication."
                    }
                ],
                "grammar_point": {
                    "rule": "Present Subjunctive: It is essential/vital/imperative that + S + (should) + V_inf",
                    "formula": "S + insist/recommend/demand + that + S + V_inf",
                    "examples": [
                        "The doctor recommended that he take a week off work.",
                        "It is vital that every employee wear protective gear in the laboratory."
                    ]
                },
                "listening_task": {
                    "audio_text": "The safety auditor insisted that all emergency exits be inspected and cleared of obstacles immediately.",
                    "question": "What did the auditor insist on?",
                    "options": [
                        "Closing the factory",
                        "Inspecting emergency exits immediately",
                        "Hiring new staff",
                        "Buying new machines"
                    ],
                    "ans": "Inspecting emergency exits immediately",
                    "exp": "Audio nêu rõ: 'insisted that all emergency exits be inspected and cleared'."
                },
                "speaking_prompt": {
                    "target_sentence": "It is crucial that our engineering team resolve the latency bottleneck before product launch.",
                    "ipa_focus": "/ɪt ɪz ˈkruːʃl ðæt ˈaʊər ˌendʒɪˈnɪərɪŋ tiːm/",
                    "tips": "Giữ giọng điệu dứt khoát, chuyên nghiệp và trang trọng."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu đề xuất chính sách công ty sử dụng cấu trúc thể giả định (recommend that... / imperative that...).",
                    "hint": "The manager suggested that all employees... It is imperative that data...",
                    "sample_answer": "The cybersecurity director recommended that all staff change their system passwords biweekly. Furthermore, it is imperative that confidential customer records remain encrypted at all times."
                },
                "dialogue": [
                    {
                        "speaker": "Auditor",
                        "text": "We demand that all financial records be submitted for external audit by Monday."
                    },
                    {
                        "speaker": "CFO",
                        "text": "Certainly, our accounting department is compiling the requested ledger books right now."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "The committee demanded that the chairperson _____ a detailed explanation.",
                        "options": [
                            "provide",
                            "provides",
                            "provided",
                            "providing"
                        ],
                        "ans": "provide",
                        "exp": "Thể giả định sau động từ 'demand that + S + V_inf'."
                    },
                    {
                        "q": "We need to have our company website _____ before the international conference.",
                        "options": [
                            "redesigned",
                            "redesign",
                            "redesigning",
                            "to redesign"
                        ],
                        "ans": "redesigned",
                        "exp": "Cấu trúc cầu khiến bị động: 'have + something + V3/ed' ('have our website redesigned')."
                    }
                ]
            },
            {
                "id": "b2-m5",
                "title": "Bài 5: Liên Từ Nâng Cao, Tranh Luận & Viết Luận Phân Tích (Essay Connectors)",
                "description": "Làm chủ liên từ học thuật (Furthermore, Nevertheless, In contrast, Consequently, On the contrary) trong viết luận B2.",
                "duration_min": 40,
                "xp": 110,
                "theory": "Liên từ học thuật phân loại theo chức năng: Bổ sung (Furthermore, Moreover), Tương phản (Nevertheless, Conversely, In contrast), Kết quả (Consequently, Hence, Thus), và Nhượng bộ (Granted that, Albeit).",
                "key_vocab": [
                    {
                        "word": "Consequently",
                        "ipa": "/ˈkɑːnsəkwentli/",
                        "meaning": "Do đó / Kết quả là",
                        "example": "The company cut costs; consequently, profits rose."
                    },
                    {
                        "word": "Nevertheless",
                        "ipa": "/ˌnevərðəˈles/",
                        "meaning": "Tuy nhiên / Dẫu vậy",
                        "example": "The journey was perilous; nevertheless, they persisted."
                    },
                    {
                        "word": "Conversely",
                        "ipa": "/kənˈvɜːrsli/",
                        "meaning": "Ngược lại",
                        "example": "Northern regions experienced heavy rain; conversely, the south suffered drought."
                    },
                    {
                        "word": "Furthermore",
                        "ipa": "/ˈfɜːrðərmɔːr/",
                        "meaning": "Hơn thế nữa",
                        "example": "The proposal is economical; furthermore, it is eco-friendly."
                    },
                    {
                        "word": "Comprehensive",
                        "ipa": "/ˌkɑːmprɪˈhensɪv/",
                        "meaning": "Toàn diện / Bao quát",
                        "example": "We conducted a comprehensive market analysis."
                    },
                    {
                        "word": "Substantiate",
                        "ipa": "/səbˈstænʃieɪt/",
                        "meaning": "Chứng minh / Cung cấp bằng chứng",
                        "example": "You must substantiate your arguments with empirical data."
                    },
                    {
                        "word": "Discrepancy",
                        "ipa": "/dɪˈskrepənsi/",
                        "meaning": "Sự khác biệt / Điểm bất đồng",
                        "example": "There is a minor discrepancy in the quarterly financial report."
                    },
                    {
                        "word": "Perspective",
                        "ipa": "/pərˈspektɪv/",
                        "meaning": "Góc nhìn / Quan điểm",
                        "example": "Let us examine the issue from a global perspective."
                    },
                    {
                        "word": "Facilitate",
                        "ipa": "/fəˈsɪlɪteɪt/",
                        "meaning": "Tạo điều kiện thuận lợi",
                        "example": "The new software facilitates seamless cross-border communication."
                    }
                ],
                "grammar_point": {
                    "rule": "Cách dùng dấu câu với trạng từ liên kết (Conjunctive Adverbs): Semicolon + Adverb + Comma",
                    "formula": "Clause 1; [Furthermore / Nevertheless / Consequently], Clause 2.",
                    "examples": [
                        "Renewable energy reduces pollution; moreover, it fosters long-term economic stability.",
                        "The algorithm was highly complex; nevertheless, it operated with remarkable speed."
                    ]
                },
                "listening_task": {
                    "audio_text": "Urban migration accelerates economic activity; however, it frequently exacerbates housing shortages and strains public transport infrastructure.",
                    "question": "What is a negative consequence of urban migration mentioned?",
                    "options": [
                        "Decreased jobs",
                        "Housing shortages and transport strain",
                        "Lower inflation",
                        "Rural development"
                    ],
                    "ans": "Housing shortages and transport strain",
                    "exp": "Audio chỉ ra: 'exacerbates housing shortages and strains public transport infrastructure'."
                },
                "speaking_prompt": {
                    "target_sentence": "Electric vehicles produce zero direct emissions; nevertheless, the carbon footprint of battery manufacturing must be addressed.",
                    "ipa_focus": "/ˌnevərðəˈles ðə ˈkɑːrbən ˈfʊtprɪnt/",
                    "tips": "Ngắt nghỉ rõ ràng ở vị trí dấu chấm phẩy và liên từ 'nevertheless'."
                },
                "writing_task": {
                    "prompt": "Viết đoạn văn học thuật 3 câu bàn về việc làm việc từ xa (Remote work), sử dụng ít nhất 2 liên từ học thuật.",
                    "hint": "Remote work enhances flexibility; furthermore... Conversely...",
                    "sample_answer": "Remote employment significantly enhances work-life balance and eliminates grueling commutes; furthermore, it allows organizations to recruit top global talent. Conversely, prolonged isolation may impair spontaneous team synergy. Consequently, hybrid workplace models have emerged as the optimal compromise."
                },
                "dialogue": [
                    {
                        "speaker": "Panelist A",
                        "text": "AI automation will inevitably displace repetitive clerical jobs."
                    },
                    {
                        "speaker": "Panelist B",
                        "text": "Nevertheless, historical precedent demonstrates that technological revolutions consistently generate higher-order employment opportunities."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "The experimental trial was grueling; _____, the breakthrough findings justified every sacrifice.",
                        "options": [
                            "nevertheless",
                            "because",
                            "so that",
                            "in order to"
                        ],
                        "ans": "nevertheless",
                        "exp": "Trạng từ liên kết tương phản trang trọng đứng sau dấu chấm phẩy là 'nevertheless'."
                    },
                    {
                        "q": "The company failed to innovate; _____, it lost its market share within two years.",
                        "options": [
                            "consequently",
                            "although",
                            "despite",
                            "whereas"
                        ],
                        "ans": "consequently",
                        "exp": "Trạng từ chỉ kết quả 'consequently' (kết quả là)."
                    }
                ]
            },
            {
                "id": "b2-m6",
                "title": "Bài 6: Thuyết Trình Dự Án & Phản Biện Hội Thảo (Project Pitching & Q&A)",
                "description": "Nghệ thuật mở đầu bài thuyết trình, dẫn dắt số liệu trực quan, xử lý câu hỏi khó từ ban giám khảo.",
                "duration_min": 40,
                "xp": 110,
                "theory": "Kỹ thuật thuyết trình chuẩn quốc tế: Hook mở đầu -> Signposting (chỉ dẫn cấu trúc: 'First, I will delve into... Next, we will examine...') -> Handling tough questions ('That is an insightful question; allow me to clarify...').",
                "key_vocab": [
                    {
                        "word": "Delve",
                        "ipa": "/delv/",
                        "meaning": "Đi sâu tìm hiểu",
                        "example": "Let us delve into the statistical breakdown."
                    },
                    {
                        "word": "Insightful",
                        "ipa": "/ˈɪnsaɪtfl/",
                        "meaning": "Sâu sắc / Thấu đáo",
                        "example": "Thank you for that insightful inquiry."
                    },
                    {
                        "word": "Benchmark",
                        "ipa": "/ˈbentʃmɑːrk/",
                        "meaning": "Tiêu chuẩn đối sánh",
                        "example": "Our performance benchmarks exceed industry averages."
                    },
                    {
                        "word": "Demonstrate",
                        "ipa": "/ˈdemənstreɪt/",
                        "meaning": "Chứng minh / Thể hiện rõ",
                        "example": "The graph demonstrates steady quarterly growth."
                    },
                    {
                        "word": "Comprehensive",
                        "ipa": "/ˌkɑːmprɪˈhensɪv/",
                        "meaning": "Toàn diện / Bao quát",
                        "example": "We conducted a comprehensive market analysis."
                    },
                    {
                        "word": "Nevertheless",
                        "ipa": "/ˌnevərðəˈles/",
                        "meaning": "Tuy nhiên / Dẫu vậy",
                        "example": "The challenge was huge; nevertheless, we succeeded."
                    },
                    {
                        "word": "Substantiate",
                        "ipa": "/səbˈstænʃieɪt/",
                        "meaning": "Chứng minh / Cung cấp bằng chứng",
                        "example": "You must substantiate your arguments with empirical data."
                    },
                    {
                        "word": "Discrepancy",
                        "ipa": "/dɪˈskrepənsi/",
                        "meaning": "Sự khác biệt / Điểm bất đồng",
                        "example": "There is a minor discrepancy in the quarterly financial report."
                    },
                    {
                        "word": "Perspective",
                        "ipa": "/pərˈspektɪv/",
                        "meaning": "Góc nhìn / Quan điểm",
                        "example": "Let us examine the issue from a global perspective."
                    },
                    {
                        "word": "Facilitate",
                        "ipa": "/fəˈsɪlɪteɪt/",
                        "meaning": "Tạo điều kiện thuận lợi",
                        "example": "The new software facilitates seamless cross-border communication."
                    }
                ],
                "grammar_point": {
                    "rule": "Signposting Language & Rhetorical Questions in Presentations",
                    "formula": "To begin with, let us examine X... Turning our attention to Y... To sum up...",
                    "examples": [
                        "As the visual on slide four illustrates, our user retention rate has doubled.",
                        "How can we achieve carbon neutrality by 2030? Let us explore three viable strategies."
                    ]
                },
                "listening_task": {
                    "audio_text": "Good afternoon, esteemed board members. Today, I will present our five-year strategic roadmap for artificial intelligence commercialization across Southeast Asia.",
                    "question": "What is the presentation about?",
                    "options": [
                        "Quarterly tax report",
                        "Five-year AI strategic roadmap",
                        "Office relocation",
                        "Hiring policy"
                    ],
                    "ans": "Five-year AI strategic roadmap",
                    "exp": "Audio nêu rõ: 'five-year strategic roadmap for artificial intelligence commercialization'."
                },
                "speaking_prompt": {
                    "target_sentence": "As the data on the chart demonstrates, our market expansion strategy has yielded a thirty percent revenue increase.",
                    "ipa_focus": "/æz ðə ˈdeɪtə ɑːn ðə tʃɑːrt ˈdemənstreɪts/",
                    "tips": "Nói với phong thái tự tin, ngắt nhịp đúng sau cụm 'on the chart demonstrates'."
                },
                "writing_task": {
                    "prompt": "Viết đoạn mở đầu bài thuyết trình (3 câu) giới thiệu bản thân, chủ đề và 2 phần chính của bài nói.",
                    "hint": "Good morning everyone. My name is... Today I am honored to present... My talk is divided into two parts: first... second...",
                    "sample_answer": "Good morning distinguished guests. My name is Minh Anh, and I am honored to present our green architecture initiative today. My presentation is structured into two main parts: first, an overview of sustainable building materials, and second, an analysis of long-term energy savings."
                },
                "dialogue": [
                    {
                        "speaker": "Presenter",
                        "text": "To summarize, adopting modular solar arrays will reduce operational expenditures by 25%."
                    },
                    {
                        "speaker": "Investor",
                        "text": "What is the anticipated payback period for this initial capital expenditure?"
                    },
                    {
                        "speaker": "Presenter",
                        "text": "That is an excellent question. Based on our financial modeling, full amortization will occur within 3.5 years."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Which signposting phrase is ideal for transitioning to a new presentation topic?",
                        "options": [
                            "Turning our attention to...",
                            "Stop talking now.",
                            "I am done with that.",
                            "Let us leave the room."
                        ],
                        "ans": "Turning our attention to...",
                        "exp": "'Turning our attention to...' là cụm chuyển ý chuyên nghiệp và lịch sự."
                    },
                    {
                        "q": "How should a speaker professionally acknowledge a difficult question from the audience?",
                        "options": [
                            "Thank you for that insightful question.",
                            "Why are you asking that?",
                            "I don't know and don't care.",
                            "That question is irrelevant."
                        ],
                        "ans": "Thank you for that insightful question.",
                        "exp": "'Thank you for that insightful question' là cách mở lời tôn trọng và thông minh."
                    }
                ]
            }
        ],
        "exam": {
            "title": "Bài Thi Chuẩn Đầu Ra CEFR B2 (Vantage Mastery Test)",
            "time_min": 35,
            "pass_score": 75,
            "questions": [
                {
                    "id": 1,
                    "question": "Not only _____ the international championship, but she also set a new world record.",
                    "options": [
                        "did she win",
                        "she won",
                        "won she",
                        "has she won"
                    ],
                    "correct": "did she win",
                    "explanation": "Đảo ngữ quá khứ đơn: 'Not only did + S + V_inf'."
                },
                {
                    "id": 2,
                    "question": "The scientific paper _____ by Dr. Watson received widespread acclaim.",
                    "options": [
                        "published",
                        "publishing",
                        "was published",
                        "which published"
                    ],
                    "correct": "published",
                    "explanation": "Rút gọn mệnh đề quan hệ ở dạng bị động 'which was published' thành 'published'."
                },
                {
                    "id": 3,
                    "question": "Had you informed me earlier, I _____ alternate arrangements for the delegation.",
                    "options": [
                        "would have made",
                        "will make",
                        "made",
                        "would make"
                    ],
                    "correct": "would have made",
                    "explanation": "Đảo ngữ câu điều kiện loại 3: Had + S + V3, S + would have + V3."
                },
                {
                    "id": 4,
                    "question": "The company's innovative marketing campaign led to a _____ increase in annual revenue.",
                    "options": [
                        "substantial",
                        "negligible",
                        "frivolous",
                        "meager"
                    ],
                    "correct": "substantial",
                    "explanation": "'Substantial increase' mang nghĩa sự gia tăng đáng kể, vượt bậc."
                },
                {
                    "id": 5,
                    "question": "Under no circumstances _____ allowed to operate the machinery without supervision.",
                    "options": [
                        "are visitors",
                        "visitors are",
                        "visitors be",
                        "do visitors"
                    ],
                    "correct": "are visitors",
                    "explanation": "Đảo ngữ với 'Under no circumstances' đảo to be 'are' lên trước chủ ngữ."
                },
                {
                    "id": 6,
                    "question": "The committee reached a consensus _____ the proposed educational reforms.",
                    "options": [
                        "regarding",
                        "regards",
                        "with regard",
                        "as regarding"
                    ],
                    "correct": "regarding",
                    "explanation": "'Regarding' là giới từ mang nghĩa 'về / liên quan tới'."
                },
                {
                    "id": 7,
                    "question": "She spoke with such eloquence that she easily _____ the skeptical audience.",
                    "options": [
                        "persuaded",
                        "dissuaded",
                        "confused",
                        "alienated"
                    ],
                    "correct": "persuaded",
                    "explanation": "'Persuaded' mang nghĩa thuyết phục được khán giả hoài nghi."
                },
                {
                    "id": 8,
                    "question": "It is imperative that every candidate _____ on time for the examination.",
                    "options": [
                        "arrive",
                        "arrives",
                        "arrived",
                        "must arrive"
                    ],
                    "correct": "arrive",
                    "explanation": "Thể giả định sau tính từ 'imperative': It is imperative that S + (should) + V_inf."
                },
                {
                    "id": 9,
                    "question": "The new transit system is designed to _____ traffic congestion during peak hours.",
                    "options": [
                        "alleviate",
                        "aggravate",
                        "deteriorate",
                        "inflate"
                    ],
                    "correct": "alleviate",
                    "explanation": "'Alleviate congestion' mang nghĩa làm giảm thiểu tình trạng ùn tắc giao thông."
                },
                {
                    "id": 10,
                    "question": "_____ exhausted after the marathon, Liam managed to cross the finish line with a smile.",
                    "options": [
                        "Although",
                        "Despite",
                        "In spite",
                        "Even"
                    ],
                    "correct": "Although",
                    "explanation": "'Although exhausted' là dạng rút gọn của 'Although he was exhausted'."
                },
                {
                    "id": 11,
                    "question": "There is a glaring discrepancy _____ the declared earnings and the audit report.",
                    "options": [
                        "between",
                        "among",
                        "within",
                        "towards"
                    ],
                    "correct": "between",
                    "explanation": "'Discrepancy between A and B' nghĩa là sự sai lệch giữa hai đối tượng."
                },
                {
                    "id": 12,
                    "question": "No sooner had the keynote speaker begun _____ the projector malfunctioned.",
                    "options": [
                        "than",
                        "when",
                        "then",
                        "that"
                    ],
                    "correct": "than",
                    "explanation": "Cấu trúc 'No sooner had + S + V3 + than + S + V_past'."
                },
                {
                    "id": 13,
                    "question": "The government is implementing policies to foster _____ economic growth.",
                    "options": [
                        "sustainable",
                        "transient",
                        "reckless",
                        "stagnant"
                    ],
                    "correct": "sustainable",
                    "explanation": "'Sustainable economic growth' là tăng trưởng kinh tế bền vững."
                },
                {
                    "id": 14,
                    "question": "He was accused of _____ proprietary company information to a competitor.",
                    "options": [
                        "leaking",
                        "to leak",
                        "leak",
                        "leaked"
                    ],
                    "correct": "leaking",
                    "explanation": "Sau giới từ 'of' trong cấu trúc 'accuse of' ta dùng V-ing ('leaking')."
                },
                {
                    "id": 15,
                    "question": "The findings are consistent _____ previous empirical studies in cognitive psychology.",
                    "options": [
                        "with",
                        "to",
                        "for",
                        "against"
                    ],
                    "correct": "with",
                    "explanation": "Cụm tính từ 'consistent with' nghĩa là nhất quán, phù hợp với."
                }
            ]
        }
    },
    "C1": {
        "level": "C1",
        "title": "CEFR C1 – Cao Cấp (Effective Operational Proficiency)",
        "badge": "Advanced / Chuyên gia ngôn ngữ",
        "color": "#dc2626",
        "target_audience": "Lãnh đạo, giảng viên, nghiên cứu sinh, ứng viên mục tiêu IELTS 7.5-8.0+ cần làm chủ diễn ngôn học thuật và ngoại giao cấp cao.",
        "outcome": "Vốn từ 6000+, thành thạo Giả Định Cách (Subjunctive), Câu Điều Kiện Hỗn Hợp (Mixed Conditionals), Nuances, Collocations cao cấp và nghệ thuật thuyết phục ngoại giao.",
        "modules": [
            {
                "id": "c1-m1",
                "title": "Bài 1: Giả Định Cách, Cleft Sentences & Sắc Thái Ngôn Từ (Nuances)",
                "description": "Làm chủ Subjunctive Mood và Câu chẻ (It is/was... that) để định hình trọng tâm lập luận và văn phong học thuật sắc sảo.",
                "duration_min": 45,
                "xp": 120,
                "theory": "Ở trình độ C1, người học sử dụng Cleft Sentences ('It is precisely this lack of oversight that precipitated the crisis') để dồn trọng âm thông tin vào yếu tố then chốt, kết hợp Subjunctive Mood để biểu đạt tính chuẩn xác và tính trang trọng bậc cao.",
                "key_vocab": [
                    {
                        "word": "Eloquent",
                        "ipa": "/ˈeləkwənt/",
                        "meaning": "Hùng hồn / Lưu loát",
                        "example": "She delivered an eloquent keynote address."
                    },
                    {
                        "word": "Exemplify",
                        "ipa": "/ɪɡˈzemplɪfaɪ/",
                        "meaning": "Là ví dụ điển hình cho",
                        "example": "His career exemplifies relentless perseverance."
                    },
                    {
                        "word": "Meticulous",
                        "ipa": "/məˈtɪkjələs/",
                        "meaning": "Tỉ mỉ / Cẩn trọng",
                        "example": "The researchers conducted meticulous laboratory checks."
                    },
                    {
                        "word": "Ambiguity",
                        "ipa": "/ˌæmbɪˈɡjuːəti/",
                        "meaning": "Sự mơ hồ / Đa nghĩa",
                        "example": "The contractual terms leave no room for ambiguity."
                    },
                    {
                        "word": "Ubiquitous",
                        "ipa": "/juːˈbɪkwɪtəs/",
                        "meaning": "Phổ biến khắp nơi",
                        "example": "Smart devices have become ubiquitous in contemporary society."
                    },
                    {
                        "word": "Epitome",
                        "ipa": "/ɪˈpɪtəmi/",
                        "meaning": "Hình mẫu hoàn hảo / Biểu tượng",
                        "example": "Her speech was the epitome of diplomatic eloquence."
                    },
                    {
                        "word": "Pragmatic",
                        "ipa": "/præɡˈmætɪk/",
                        "meaning": "Thực dụng / Thực tế",
                        "example": "We adopted a pragmatic approach to resolve the dispute."
                    },
                    {
                        "word": "Nuance",
                        "ipa": "/ˈnuːɑːns/",
                        "meaning": "Sắc thái tinh tế",
                        "example": "Understanding semantic nuances is crucial for advanced translation."
                    },
                    {
                        "word": "Juxtaposition",
                        "ipa": "/ˌdʒʌkstəpəˈzɪʃn/",
                        "meaning": "Sự đặt cạnh nhau đối chiếu",
                        "example": "The juxtaposition of traditional and modern values created intense debate."
                    }
                ],
                "grammar_point": {
                    "rule": "Cleft Sentences & Subjunctive Mood",
                    "formula": "It is/was + Focus Element + that/who + Clause | S + demand/insist that + S + V_inf",
                    "examples": [
                        "It was her exceptional leadership that galvanized the entire organization.",
                        "The board insisted that all financial disclosures be audited independently."
                    ]
                },
                "listening_task": {
                    "audio_text": "It was precisely the convergence of artificial intelligence and biotechnology that enabled this unprecedented medical breakthrough.",
                    "question": "What enabled the breakthrough?",
                    "options": [
                        "Biotech alone",
                        "The convergence of AI and biotechnology",
                        "Government subsidy",
                        "Random luck"
                    ],
                    "ans": "The convergence of AI and biotechnology",
                    "exp": "Audio nhấn mạnh cấu trúc câu chẻ: 'It was precisely the convergence of AI and biotechnology that enabled...'."
                },
                "speaking_prompt": {
                    "target_sentence": "It is imperative that policymakers address systemic inequalities before enacting macroeconomic reforms.",
                    "ipa_focus": "/ɪt ɪz ɪmˈperətɪv ðæt ˈpɑːləsimeɪkərz/",
                    "tips": "Giữ ngữ điệu đĩnh đạc, nhấn âm rõ vào 'systemic inequalities' và 'macroeconomic reforms'."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu học thuật C1 sử dụng Cleft sentence (It was... that) để phân tích nguyên nhân thành công của một tập đoàn công nghệ.",
                    "hint": "It was primarily their relentless innovation that... What distinguishes them from rivals is...",
                    "sample_answer": "It was primarily their relentless dedication to user privacy that solidified consumer trust in an increasingly volatile digital landscape. What truly distinguishes the enterprise from its competitors is its unwavering focus on long-term sustainability rather than transient quarterly profits."
                },
                "dialogue": [
                    {
                        "speaker": "Diplomat A",
                        "text": "We insist that the treaty language remain unambiguous regarding maritime sovereignty."
                    },
                    {
                        "speaker": "Diplomat B",
                        "text": "It is our shared intent that no clause be open to misinterpretation by any signatory state."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "The committee recommended that the draft resolution _____ immediately.",
                        "options": [
                            "be ratified",
                            "is ratified",
                            "was ratified",
                            "will be ratified"
                        ],
                        "ans": "be ratified",
                        "exp": "Thể giả định Subjunctive: 'recommend that + S + (should) be + V3'."
                    },
                    {
                        "q": "It was during the 1920s _____ jazz music gained international prominence.",
                        "options": [
                            "that",
                            "which",
                            "where",
                            "when"
                        ],
                        "ans": "that",
                        "exp": "Cấu trúc câu chẻ chuẩn 'It was [time phrase] that [clause]'."
                    }
                ]
            },
            {
                "id": "c1-m2",
                "title": "Bài 2: Thành Ngữ & Cụm Từ Học Thuật Cấp Cao (Academic Idioms & Collocations)",
                "description": "Làm chủ các collocations C1 hiếm gặp (strike a chord, double-edged sword, tip of the iceberg, paradigm shift) trong tranh luận.",
                "duration_min": 45,
                "xp": 120,
                "theory": "Ở bậc C1, việc sử dụng thành thạo Advanced Collocations giúp bài viết đạt band điểm cao nhất. Tránh dịch 'word-by-word' và thay thế bằng các cụm tự nhiên: 'foster innovation', 'exert pressure', 'precipitate a crisis', 'paradigm shift'.",
                "key_vocab": [
                    {
                        "word": "Paradigm",
                        "ipa": "/ˈpærədaɪm/",
                        "meaning": "Mô hình / Khuôn mẫu tư duy",
                        "example": "Quantum computing represents a fundamental paradigm shift."
                    },
                    {
                        "word": "Double-edged sword",
                        "ipa": "/ˈdʌbl edʒd sɔːrd/",
                        "meaning": "Con dao hai lưỡi",
                        "example": "Artificial intelligence is a double-edged sword for employment."
                    },
                    {
                        "word": "Catalyst",
                        "ipa": "/ˈkætəlɪst/",
                        "meaning": "Chất xúc tác",
                        "example": "The crisis acted as a catalyst for educational reform."
                    },
                    {
                        "word": "Ubiquity",
                        "ipa": "/juːˈbɪkwəti/",
                        "meaning": "Sự phổ biến ở khắp nơi",
                        "example": "The ubiquity of smartphones has altered human communication."
                    },
                    {
                        "word": "Ubiquitous",
                        "ipa": "/juːˈbɪkwɪtəs/",
                        "meaning": "Phổ biến khắp nơi",
                        "example": "Smart devices have become ubiquitous in contemporary society."
                    },
                    {
                        "word": "Epitome",
                        "ipa": "/ɪˈpɪtəmi/",
                        "meaning": "Hình mẫu hoàn hảo / Biểu tượng",
                        "example": "Her speech was the epitome of diplomatic eloquence."
                    },
                    {
                        "word": "Pragmatic",
                        "ipa": "/præɡˈmætɪk/",
                        "meaning": "Thực dụng / Thực tế",
                        "example": "We adopted a pragmatic approach to resolve the dispute."
                    },
                    {
                        "word": "Nuance",
                        "ipa": "/ˈnuːɑːns/",
                        "meaning": "Sắc thái tinh tế",
                        "example": "Understanding semantic nuances is crucial for advanced translation."
                    },
                    {
                        "word": "Juxtaposition",
                        "ipa": "/ˌdʒʌkstəpəˈzɪʃn/",
                        "meaning": "Sự đặt cạnh nhau đối chiếu",
                        "example": "The juxtaposition of traditional and modern values created intense debate."
                    }
                ],
                "grammar_point": {
                    "rule": "Adverbial Participle Clauses for Conciseness in High-Level Prose",
                    "formula": "Having + V3/ed, Main Clause | Present Participle (V-ing), Main Clause",
                    "examples": [
                        "Having analyzed the geopolitical landscape, the think-tank published its strategic forecast.",
                        "Realizing the imminent regulatory scrutiny, the conglomerate restructured its subsidiaries."
                    ]
                },
                "listening_task": {
                    "audio_text": "The introduction of generative AI models has proven to be a double-edged sword, offering immense productivity gains while simultaneously raising formidable copyright quandaries.",
                    "question": "How is generative AI described by the speaker?",
                    "options": [
                        "A useless tool",
                        "A double-edged sword",
                        "A cheap software",
                        "A temporary trend"
                    ],
                    "ans": "A double-edged sword",
                    "exp": "Audio nhấn mạnh thành ngữ: 'proven to be a double-edged sword'."
                },
                "speaking_prompt": {
                    "target_sentence": "This policy intervention served as a catalyst for green technological innovation across the continent.",
                    "ipa_focus": "/sɜːrvd æz ə ˈkætəlɪst fər ɡriːn/",
                    "tips": "Giữ phong thái học giả, phát âm chuẩn trọng âm 'catalyst' và 'innovation'."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu phân tích tác động của mạng xã hội, sử dụng cụm từ 'double-edged sword' và mệnh đề phân từ (Having + V3 hoặc V-ing).",
                    "hint": "Social media platforms represent a double-edged sword... Having connected billions of people...",
                    "sample_answer": "Social media platforms undeniably represent a double-edged sword in contemporary discourse. Having democratized access to information globally, these networks concurrently facilitate the virality of disinformation and polarization."
                },
                "dialogue": [
                    {
                        "speaker": "Professor",
                        "text": "Does this discovery herald a paradigm shift in astrophysics?"
                    },
                    {
                        "speaker": "Fellow",
                        "text": "Unquestionably; it fundamentally dismantles several longstanding theoretical tenets."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Choose the most sophisticated idiom for 'a major change in thinking':",
                        "options": [
                            "Paradigm shift",
                            "New thought",
                            "Big change",
                            "Mind move"
                        ],
                        "ans": "Paradigm shift",
                        "exp": "'Paradigm shift' là thuật ngữ học thuật chỉ bước chuyển biến căn bản trong nhận thức/tư duy."
                    },
                    {
                        "q": "_____ the preliminary trials, the pharmaceutical firm advanced to human testing.",
                        "options": [
                            "Having concluded",
                            "Concluding were",
                            "Have concluded",
                            "Concluded having"
                        ],
                        "ans": "Having concluded",
                        "exp": "Mệnh đề phân từ hoàn thành (Perfect Participle): 'Having + V3/ed'."
                    }
                ]
            },
            {
                "id": "c1-m3",
                "title": "Bài 3: Đàm Phán Ngoại Giao & Diễn Ngôn Lãnh Đạo (Diplomatic Discourse)",
                "description": "Nghệ thuật phát biểu ngoại giao, sử dụng từ ngữ trung lập, kiềm chế và cách hóa giải bất đồng ý kiến (Diplomatic Hedging).",
                "duration_min": 45,
                "xp": 125,
                "theory": "Kỹ thuật 'Hedging' trong tiếng Anh ngoại giao: Sử dụng các động từ tình thái và trạng từ giảm nhẹ (seem to, appear to, arguably, conceivably, to some extent) để đưa ra quan điểm vừa sắc bén vừa tránh xung đột trực diện.",
                "key_vocab": [
                    {
                        "word": "Equivocal",
                        "ipa": "/ɪˈkwɪvəkl/",
                        "meaning": "Mập mờ / Nước đôi",
                        "example": "His equivocal statement left both parties dissatisfied."
                    },
                    {
                        "word": "Consensus",
                        "ipa": "/kənˈsensəs/",
                        "meaning": "Sự đồng thuận chung",
                        "example": "The summit concluded with a unanimous consensus."
                    },
                    {
                        "word": "Conciliatory",
                        "ipa": "/kənˈsɪliətɔːri/",
                        "meaning": "Mang tính hòa giải",
                        "example": "The ambassador adopted a conciliatory tone."
                    },
                    {
                        "word": "Imperative",
                        "ipa": "/ɪmˈperətɪv/",
                        "meaning": "Mệnh lệnh cấp thiết",
                        "example": "De-escalation remains our highest diplomatic imperative."
                    },
                    {
                        "word": "Ubiquitous",
                        "ipa": "/juːˈbɪkwɪtəs/",
                        "meaning": "Phổ biến khắp nơi",
                        "example": "Smart devices have become ubiquitous in contemporary society."
                    },
                    {
                        "word": "Epitome",
                        "ipa": "/ɪˈpɪtəmi/",
                        "meaning": "Hình mẫu hoàn hảo / Biểu tượng",
                        "example": "Her speech was the epitome of diplomatic eloquence."
                    },
                    {
                        "word": "Pragmatic",
                        "ipa": "/præɡˈmætɪk/",
                        "meaning": "Thực dụng / Thực tế",
                        "example": "We adopted a pragmatic approach to resolve the dispute."
                    },
                    {
                        "word": "Nuance",
                        "ipa": "/ˈnuːɑːns/",
                        "meaning": "Sắc thái tinh tế",
                        "example": "Understanding semantic nuances is crucial for advanced translation."
                    },
                    {
                        "word": "Juxtaposition",
                        "ipa": "/ˌdʒʌkstəpəˈzɪʃn/",
                        "meaning": "Sự đặt cạnh nhau đối chiếu",
                        "example": "The juxtaposition of traditional and modern values created intense debate."
                    }
                ],
                "grammar_point": {
                    "rule": "Diplomatic Hedging: It would appear that... / One might argue that...",
                    "formula": "It is arguably the case that X... / Evidence seems to suggest Y...",
                    "examples": [
                        "It would be prudent to defer the vote until all delegations have convened.",
                        "One could conceivably argue that unilateral measures might exacerbate tensions."
                    ]
                },
                "listening_task": {
                    "audio_text": "The ambassador emphasized that while disagreements persist, both nations share a mutual imperative to maintain open diplomatic communication channels.",
                    "question": "What is the shared imperative mentioned?",
                    "options": [
                        "Impose sanctions",
                        "Maintain open diplomatic communication",
                        "Sever ties",
                        "Declare trade war"
                    ],
                    "ans": "Maintain open diplomatic communication",
                    "exp": "Audio nêu rõ: 'share a mutual imperative to maintain open diplomatic communication channels'."
                },
                "speaking_prompt": {
                    "target_sentence": "We believe a conciliatory approach will foster long-term stability and mutual prosperity.",
                    "ipa_focus": "/ə kənˈsɪliətɔːri əˈproʊtʃ wɪl ˈfɔːstər/",
                    "tips": "Giọng điệu điềm tĩnh, trọng lượng và thuyết phục."
                },
                "writing_task": {
                    "prompt": "Viết thông cáo ngoại giao 3 câu kêu gọi các bên kiềm chế và đối thoại hòa bình (Sử dụng kỹ thuật Hedging).",
                    "hint": "In light of recent developments, it would appear prudent... We strongly urge all parties to...",
                    "sample_answer": "In light of recent escalations, it would appear prudent for all stakeholders to exercise maximum restraint. We urge involved parties to prioritize constructive diplomatic dialogue over unilateral measures. De-escalation remains the most viable path toward enduring regional peace."
                },
                "dialogue": [
                    {
                        "speaker": "Delegate A",
                        "text": "Our delegation finds clause four somewhat contentious in its present wording."
                    },
                    {
                        "speaker": "Delegate B",
                        "text": "We would be amenable to redrafting the sentence to ensure equitable reciprocity."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Which expression represents the highest level of diplomatic hedging?",
                        "options": [
                            "It would appear prudent to suggest...",
                            "You are totally wrong.",
                            "We reject everything you said.",
                            "This is stupid."
                        ],
                        "ans": "It would appear prudent to suggest...",
                        "exp": "'It would appear prudent to suggest...' là mẫu câu giảm nhẹ ngoại giao chuẩn mực."
                    },
                    {
                        "q": "The committee reached a unanimous _____ on maritime safety protocols.",
                        "options": [
                            "consensus",
                            "discord",
                            "friction",
                            "quarrel"
                        ],
                        "ans": "consensus",
                        "exp": "'Unanimous consensus' là sự đồng thuận nhất trí 100%."
                    }
                ]
            }
        ],
        "exam": {
            "title": "Bài Thi Chuẩn Đầu Ra CEFR C1 (Advanced Mastery Test)",
            "time_min": 40,
            "pass_score": 75,
            "questions": [
                {
                    "id": 1,
                    "question": "The judge recommended that the defendant _____ compensation to the affected community.",
                    "options": [
                        "pay",
                        "pays",
                        "paid",
                        "is paying"
                    ],
                    "correct": "pay",
                    "explanation": "Subjunctive mood: S + recommend that + S + (should) + V_inf."
                },
                {
                    "id": 2,
                    "question": "It was her profound resilience _____ inspired thousands of young scientists across the globe.",
                    "options": [
                        "that",
                        "which",
                        "whom",
                        "what"
                    ],
                    "correct": "that",
                    "explanation": "Cấu trúc Cleft sentence chuẩn: 'It was [Noun Phrase] that [Clause]'."
                },
                {
                    "id": 3,
                    "question": "The board reached a decision that was completely _____ with our corporate ethos.",
                    "options": [
                        "congruent",
                        "belligerent",
                        "negligent",
                        "insolent"
                    ],
                    "correct": "congruent",
                    "explanation": "'Congruent with' mang nghĩa hoàn toàn phù hợp, tương thích với."
                },
                {
                    "id": 4,
                    "question": "Had the preliminary data been scrutinized more thoroughly, the catastrophic failure _____ averted.",
                    "options": [
                        "could have been",
                        "can be",
                        "was",
                        "will have been"
                    ],
                    "correct": "could have been",
                    "explanation": "Đảo ngữ câu điều kiện loại 3: Had + S + V3, S + could/would have been + V3."
                },
                {
                    "id": 5,
                    "question": "His argument was so _____ that even the staunchest critics conceded their position.",
                    "options": [
                        "cogent",
                        "redundant",
                        "feeble",
                        "opaque"
                    ],
                    "correct": "cogent",
                    "explanation": "'Cogent argument' là lập luận chặt chẽ, đầy tính thuyết phục."
                },
                {
                    "id": 6,
                    "question": "The economic sanctions had a _____ effect on domestic manufacturing.",
                    "options": [
                        "detrimental",
                        "complimentary",
                        "fictitious",
                        "benevolent"
                    ],
                    "correct": "detrimental",
                    "explanation": "'Detrimental effect' mang nghĩa tác động tiêu cực, gây tổn hại."
                },
                {
                    "id": 7,
                    "question": "_____ what may, the diplomatic delegation will attend the climate symposium.",
                    "options": [
                        "Come",
                        "Comes",
                        "Coming",
                        "Came"
                    ],
                    "correct": "Come",
                    "explanation": "Thành ngữ cố định thể giả định: 'Come what may' (Dù có bất cứ chuyện gì xảy ra)."
                },
                {
                    "id": 8,
                    "question": "The author's prose is characterized by its remarkable brevity and _____.",
                    "options": [
                        "lucidity",
                        "obscurity",
                        "monotony",
                        "verbosity"
                    ],
                    "correct": "lucidity",
                    "explanation": "'Lucidity' (sự trong sáng, minh bạch, rõ ràng) song hành cùng 'brevity' (sự cô đọng)."
                },
                {
                    "id": 9,
                    "question": "Much _____ he admired the painting, he could not justify its exorbitant price tag.",
                    "options": [
                        "as",
                        "so",
                        "though",
                        "even"
                    ],
                    "correct": "as",
                    "explanation": "Cấu trúc nhượng bộ: 'Much as + S + V' (Mặc dù rất...)."
                },
                {
                    "id": 10,
                    "question": "The university is renowned for its _____ academic standards and rigorous peer review.",
                    "options": [
                        "exacting",
                        "lenient",
                        "cursory",
                        "apathetic"
                    ],
                    "correct": "exacting",
                    "explanation": "'Exacting academic standards' chỉ các tiêu chuẩn học thuật nghiêm ngặt, khắt khe."
                },
                {
                    "id": 11,
                    "question": "The startup's valuation soared exponentially, _____ all market forecasts.",
                    "options": [
                        "defying",
                        "defied",
                        "defies",
                        "having defied"
                    ],
                    "correct": "defying",
                    "explanation": "Phân từ hiện tại 'defying' đóng vai trò mệnh đề trạng ngữ chỉ kết quả/hành động song song."
                },
                {
                    "id": 12,
                    "question": "Little _____ that his groundbreaking discovery would revolutionize pharmacology.",
                    "options": [
                        "did the researcher realize",
                        "the researcher realized",
                        "realized the researcher",
                        "had realized the researcher"
                    ],
                    "correct": "did the researcher realize",
                    "explanation": "Đảo ngữ với 'Little': 'Little did + S + V_inf'."
                },
                {
                    "id": 13,
                    "question": "The geopolitical crisis precipitated a sharp escalation in oil _____.",
                    "options": [
                        "volatility",
                        "stagnation",
                        "redundancy",
                        "complacency"
                    ],
                    "correct": "volatility",
                    "explanation": "'Volatility' chỉ sự biến động mạnh, bất ổn về giá cả."
                },
                {
                    "id": 14,
                    "question": "He displayed an innate propensity _____ synthesizing intricate concepts quickly.",
                    "options": [
                        "for",
                        "to",
                        "at",
                        "with"
                    ],
                    "correct": "for",
                    "explanation": "Cụm danh từ: 'propensity for (doing) something' (thiên hướng tự nhiên về việc gì)."
                },
                {
                    "id": 15,
                    "question": "The treaty was rendered _____ following the unprovoked cross-border incursion.",
                    "options": [
                        "null and void",
                        "safe and sound",
                        "short and sweet",
                        "high and dry"
                    ],
                    "correct": "null and void",
                    "explanation": "'Null and void' là thuật ngữ pháp lý chỉ văn bản bị vô hiệu lực hoàn toàn."
                }
            ]
        }
    },
    "C2": {
        "level": "C2",
        "title": "CEFR C2 – Bậc Thầy Bản Ngữ (Mastery & Scholarly Eloquence)",
        "badge": "Mastery / Đỉnh cao bản ngữ",
        "color": "#7c2d12",
        "target_audience": "Dịch giả cao cấp, giáo sư, nhà ngoại giao, cây bút học thuật quốc tế muốn đạt độ tinh xảo tối thượng của ngôn từ tiếng Anh.",
        "outcome": "Vốn từ 8000+, thẩm thấu mọi tầng nghĩa ẩn dụ, tu từ học thuật uyên bác, nắm bắt trọn vẹn văn học cổ điển và các tài liệu triết học, khoa học phức tạp nhất.",
        "modules": [
            {
                "id": "c2-m1",
                "title": "Bài 1: Tu Từ Học Thuật, Thành Ngữ Cổ Điển & Văn Phong Uyên Bác",
                "description": "Nắm vững các biện pháp tu từ đỉnh cao (Litotes, Chiasmus, Oxymoron, Zeugma) và thành ngữ văn học giàu chiều sâu.",
                "duration_min": 50,
                "xp": 150,
                "theory": "Ở bậc C2 Mastery, tiếng Anh không chỉ là công cụ truyền tải thông tin mà là nghệ thuật biểu đạt. Nắm bắt các biện pháp tu từ như Chiasmus ('Ask not what your country can do for you — ask what you can do for your country') và Litotes (nói giảm nói tránh bằng phủ định kép: 'It is no small achievement') mang lại chiều sâu trí tuệ vô song.",
                "key_vocab": [
                    {
                        "word": "Quintessential",
                        "ipa": "/ˌkwɪntɪˈsenʃl/",
                        "meaning": "Tinh túy / Điển hình bậc nhất",
                        "example": "She is the quintessential scholar of modern linguistics."
                    },
                    {
                        "word": "Ubiquitous",
                        "ipa": "/juːˈbɪkwɪtəs/",
                        "meaning": "Hiện diện khắp mọi nơi",
                        "example": "Smartphones have become ubiquitous in contemporary society."
                    },
                    {
                        "word": "Ephemeral",
                        "ipa": "/ɪˈfemərəl/",
                        "meaning": "Phù du / Chóng tàn",
                        "example": "Fame in the digital age is often ephemeral."
                    },
                    {
                        "word": "Juxtaposition",
                        "ipa": "/ˌdʒʌkstəpəˈzɪʃn/",
                        "meaning": "Sự đặt cạnh nhau đối chiếu",
                        "example": "The novel relies on the juxtaposition of wealth and squalor."
                    },
                    {
                        "word": "Paradigm",
                        "ipa": "/ˈpærədaɪm/",
                        "meaning": "Mô hình mẫu / Hệ hình tư duy",
                        "example": "Quantum mechanics caused a major paradigm shift in modern physics."
                    },
                    {
                        "word": "Perspicacious",
                        "ipa": "/ˌpɜːrspɪˈkeɪʃəs/",
                        "meaning": "Sáng suốt / Nhìn thấu đáo",
                        "example": "Her perspicacious analysis uncovered the root cause of the economic crisis."
                    },
                    {
                        "word": "Surreptitious",
                        "ipa": "/ˌsɜːrəpˈtɪʃəs/",
                        "meaning": "Lén lút / Kín đáo",
                        "example": "They made surreptitious arrangements to protect sensitive intellectual property."
                    }
                ],
                "grammar_point": {
                    "rule": "Phép tu từ Chiasmus & Nghệ thuật cấu trúc câu đa tầng bậc thầy",
                    "formula": "Parallelism with Inverted Order: AB - BA | Compound-Complex layered sentences",
                    "examples": [
                        "We should eat to live, not live to eat.",
                        "Her prose was not unmindful of the subtle contradictions inherent in human nature."
                    ]
                },
                "listening_task": {
                    "audio_text": "The philosopher argued that the juxtaposition of ephemeral digital culture with enduring human aspirations creates a unique paradox in contemporary existential thought.",
                    "question": "What creates the paradox according to the philosopher?",
                    "options": [
                        "Economic inequality",
                        "Juxtaposition of ephemeral culture and enduring aspirations",
                        "Technological regression",
                        "Political instability"
                    ],
                    "ans": "Juxtaposition of ephemeral culture and enduring aspirations",
                    "exp": "Audio nêu rõ: 'juxtaposition of ephemeral digital culture with enduring human aspirations creates a unique paradox'."
                },
                "speaking_prompt": {
                    "target_sentence": "To synthesize such disparate philosophical traditions without compromising their nuanced tenets is truly an intellectual triumph.",
                    "ipa_focus": "/tə ˈsɪnθəsaɪz sʌtʃ ˈdɪspərət ˌfɪləˈsɑːfɪkl/",
                    "tips": "Giữ phong thái điềm đạm, nhấn nhá tinh tế ở 'disparate' và 'nuanced tenets'."
                },
                "writing_task": {
                    "prompt": "Viết đoạn văn triết học 3 câu sử dụng ít nhất 1 từ vựng C2 (ubiquitous, ephemeral, juxtaposition) và cấu trúc Litotes.",
                    "hint": "It is no small wonder that... The juxtaposition of... renders...",
                    "sample_answer": "It is no small irony that in an era characterized by ubiquitous connectivity, genuine human intimacy remains elusive. The striking juxtaposition of boundless information and profound existential alienation exemplifies modern angst. Consequently, our fixation on ephemeral digital validation often overshadows timeless philosophical contemplation."
                },
                "dialogue": [
                    {
                        "speaker": "Scholar A",
                        "text": "His magnum opus exhibits a quintessential mastery of classical rhetoric and profound hermeneutics."
                    },
                    {
                        "speaker": "Scholar B",
                        "text": "Indeed; rarely does one encounter such seamless synergy between empirical rigor and poetic elegance."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Identify the rhetorical figure in: 'It was not unappreciated by the audience.'",
                        "options": [
                            "Litotes",
                            "Hyperbole",
                            "Chiasmus",
                            "Oxymoron"
                        ],
                        "ans": "Litotes",
                        "exp": "'Not unappreciated' (phủ định kép để nhấn mạnh ý khẳng định tế nhị) là ví dụ kinh điển của phép Litotes."
                    },
                    {
                        "q": "What figure of speech is: 'Never let a Fool Kiss You or a Kiss Fool You'?",
                        "options": [
                            "Chiasmus",
                            "Simile",
                            "Metaphor",
                            "Personification"
                        ],
                        "ans": "Chiasmus",
                        "exp": "Đảo chéo cấu trúc tu từ (A-B thành B-A) là phép Chiasmus."
                    }
                ]
            },
            {
                "id": "c2-m2",
                "title": "Bài 2: Diễn Ngôn Triết Học, Mỹ Học & Tư Tưởng Hiện Sinh (Philosophical Discourse)",
                "description": "Thẩm thấu văn phong hàn lâm về đạo đức học, mỹ học và các lý thuyết triết học kinh điển.",
                "duration_min": 50,
                "xp": 150,
                "theory": "Phân tích các khái niệm trừu tượng bậc cao: Epistemology (nhận thức luận), Hermeneutics (thông dịch học), Ontology (bản thể luận). Văn phong C2 tinh tế sử dụng Subjunctive phức hợp và Nominals cô đọng.",
                "key_vocab": [
                    {
                        "word": "Epistemological",
                        "ipa": "/ɪˌpɪstəməˈlɑːdʒɪkl/",
                        "meaning": "Thuộc về nhận thức luận",
                        "example": "The theory presents severe epistemological challenges."
                    },
                    {
                        "word": "Hermeneutic",
                        "ipa": "/ˌhɜːrməˈnuːtɪk/",
                        "meaning": "Thuộc về giải thích học / thông diễn",
                        "example": "A hermeneutic reading reveals multiple layers of irony."
                    },
                    {
                        "word": "Ineffable",
                        "ipa": "/ɪnˈefəbl/",
                        "meaning": "Không thể diễn tả bằng lời",
                        "example": "The aesthetic experience possessed an ineffable sublime quality."
                    },
                    {
                        "word": "Ontological",
                        "ipa": "/ˌɑːntəˈlɑːdʒɪkl/",
                        "meaning": "Thuộc về bản thể luận",
                        "example": "What is the ontological status of simulated consciousness?"
                    },
                    {
                        "word": "Quintessential",
                        "ipa": "/ˌkwɪntɪˈsenʃl/",
                        "meaning": "Kinh điển / Tinh túy nhất",
                        "example": "He represents the quintessential Renaissance intellectual."
                    },
                    {
                        "word": "Paradigm",
                        "ipa": "/ˈpærədaɪm/",
                        "meaning": "Mô hình mẫu / Hệ hình tư duy",
                        "example": "Quantum mechanics caused a major paradigm shift in modern physics."
                    },
                    {
                        "word": "Perspicacious",
                        "ipa": "/ˌpɜːrspɪˈkeɪʃəs/",
                        "meaning": "Sáng suốt / Nhìn thấu đáo",
                        "example": "Her perspicacious analysis uncovered the root cause of the economic crisis."
                    },
                    {
                        "word": "Surreptitious",
                        "ipa": "/ˌsɜːrəpˈtɪʃəs/",
                        "meaning": "Lén lút / Kín đáo",
                        "example": "They made surreptitious arrangements to protect sensitive intellectual property."
                    }
                ],
                "grammar_point": {
                    "rule": "Complex Layered Nominalizations in Philosophical English",
                    "formula": "The [Adjective] [Nominalization] of [Abstract Concept] underscores [Subordinate Clause]",
                    "examples": [
                        "The dialectical reconciliation of individual autonomy and collective duty remains a perennial conundrum in political philosophy."
                    ]
                },
                "listening_task": {
                    "audio_text": "The lecturer postulated that the hermeneutic circle is not a vicious paradox, but rather the very condition under which all historical understanding is generated.",
                    "question": "What did the lecturer postulate about the hermeneutic circle?",
                    "options": [
                        "It is a useless paradox",
                        "It is the condition for historical understanding",
                        "It must be banned",
                        "It was invented recently"
                    ],
                    "ans": "It is the condition for historical understanding",
                    "exp": "Audio nêu rõ: 'the very condition under which all historical understanding is generated'."
                },
                "speaking_prompt": {
                    "target_sentence": "To contemplate the ineffable complexity of existence requires both empirical rigor and poetic imagination.",
                    "ipa_focus": "/tə ˈkɑːntəmpleɪt ði ɪnˈefəbl kəmˈpleksəti/",
                    "tips": "Giọng đọc truyền cảm, phong thái uyên bác bậc thầy."
                },
                "writing_task": {
                    "prompt": "Viết đoạn văn triết học 3 câu luận về mối quan hệ giữa nhận thức và chân lý, sử dụng các từ epistemological, hermeneutic hoặc ineffable.",
                    "hint": "The epistemological quest for objective truth... Through hermeneutic engagement...",
                    "sample_answer": "The relentless epistemological quest for objective truth inevitably confronts the limitations of human perception. Through disciplined hermeneutic engagement with classical texts, one discovers that meaning is dynamic rather than static. Consequently, certain dimensions of human consciousness remain ineffable, transcending reductionist empirical categorization."
                },
                "dialogue": [
                    {
                        "speaker": "Philosopher A",
                        "text": "Does simulated cognition possess genuine ontological presence?"
                    },
                    {
                        "speaker": "Philosopher B",
                        "text": "That is arguably the foundational quandary of 21st-century philosophy of mind."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "What is the meaning of 'ineffable' in literary and philosophical prose?",
                        "options": [
                            "Beyond expression in words",
                            "Extremely cheap",
                            "Easily broken",
                            "Very noisy"
                        ],
                        "ans": "Beyond expression in words",
                        "exp": "'Ineffable' mang nghĩa kỳ diệu, thâm sâu đến mức không ngôn từ nào diễn tả xiết."
                    },
                    {
                        "q": "Which philosophical branch examines the nature of knowledge and belief?",
                        "options": [
                            "Epistemology",
                            "Thermodynamics",
                            "Geology",
                            "Cardiology"
                        ],
                        "ans": "Epistemology",
                        "exp": "'Epistemology' là nhận thức luận trong triết học."
                    }
                ]
            }
        ],
        "exam": {
            "title": "Bài Thi Khảo Thí Bậc Thầy CEFR C2 (Mastery & Scholarly Test)",
            "time_min": 45,
            "pass_score": 80,
            "questions": [
                {
                    "id": 1,
                    "question": "His monumental contribution to quantum electrodynamics was _____ in the history of modern physics.",
                    "options": [
                        "epoch-making",
                        "heavy-handed",
                        "short-lived",
                        "half-hearted"
                    ],
                    "correct": "epoch-making",
                    "explanation": "'Epoch-making' mang nghĩa mở ra một kỷ nguyên mới, mang tính bước ngoặt vĩ đại."
                },
                {
                    "id": 2,
                    "question": "The treaty was celebrated as a milestone, _____ it failed to resolve the underlying territorial disputes.",
                    "options": [
                        "notwithstanding that",
                        "inasmuch as",
                        "seeing that",
                        "for fear that"
                    ],
                    "correct": "notwithstanding that",
                    "explanation": "'Notwithstanding that' là liên từ học thuật cao cấp mang nghĩa 'mặc dù / dẫu cho'."
                },
                {
                    "id": 3,
                    "question": "The novelist's latest masterpiece is a _____ exploration of existential solitude.",
                    "options": [
                        "profound",
                        "frivolous",
                        "facile",
                        "shallow"
                    ],
                    "correct": "profound",
                    "explanation": "'Profound exploration' là sự khám phá sâu sắc, uyên thâm."
                },
                {
                    "id": 4,
                    "question": "Her rhetorical style was characterized by biting sarcasm and merciless _____.",
                    "options": [
                        "invective",
                        "panegyric",
                        "platitude",
                        "eulogy"
                    ],
                    "correct": "invective",
                    "explanation": "'Invective' là lời công kích kịch liệt, văn phong chỉ trích gay gắt."
                },
                {
                    "id": 5,
                    "question": "The company's apparent insolvency turned out to be a mere _____ to deceive corporate raiders.",
                    "options": [
                        "subterfuge",
                        "candor",
                        "probity",
                        "serendipity"
                    ],
                    "correct": "subterfuge",
                    "explanation": "'Subterfuge' là mưu mẹo, kế đánh lạc hướng tinh vi."
                },
                {
                    "id": 6,
                    "question": "She navigates the intricacies of international arbitration with _____ ease.",
                    "options": [
                        "consummate",
                        "amateurish",
                        "inept",
                        "perfunctory"
                    ],
                    "correct": "consummate",
                    "explanation": "'Consummate ease / skill' mang nghĩa sự điêu luyện, tài ba bậc thầy."
                },
                {
                    "id": 7,
                    "question": "The archeological discovery sheds light on the _____ practices of ancient Mesopotamian priesthood.",
                    "options": [
                        "esoteric",
                        "commonplace",
                        "banal",
                        "mundane"
                    ],
                    "correct": "esoteric",
                    "explanation": "'Esoteric' mang nghĩa thâm sâu, bí truyền, chỉ dành cho số ít người am hiểu."
                },
                {
                    "id": 8,
                    "question": "Far be it from me to _____ upon your executive prerogatives.",
                    "options": [
                        "infringe",
                        "bestow",
                        "rejoice",
                        "absolve"
                    ],
                    "correct": "infringe",
                    "explanation": "Cấu trúc: 'infringe upon (rights / prerogatives)' nghĩa là xâm phạm đến đặc quyền."
                },
                {
                    "id": 9,
                    "question": "The evidence presented by the prosecution was entirely _____, lacking tangible corroboration.",
                    "options": [
                        "circumstantial",
                        "irrefutable",
                        "conclusive",
                        "indisputable"
                    ],
                    "correct": "circumstantial",
                    "explanation": "'Circumstantial evidence' mang nghĩa bằng chứng gián tiếp, suy đoán."
                },
                {
                    "id": 10,
                    "question": "He delivered an impromptu speech that was both perspicacious and _____.",
                    "options": [
                        "pellucid",
                        "turbid",
                        "opaque",
                        "turgid"
                    ],
                    "correct": "pellucid",
                    "explanation": "'Pellucid' mang nghĩa trong sáng, rõ ràng, mạch lạc thấu suốt."
                },
                {
                    "id": 11,
                    "question": "The minister's sudden resignation set off a _____ of speculation across the political spectrum.",
                    "options": [
                        "flurry",
                        "scarcity",
                        "dearth",
                        "cessation"
                    ],
                    "correct": "flurry",
                    "explanation": "'A flurry of speculation' là một làn sóng suy đoán dồn dập."
                },
                {
                    "id": 12,
                    "question": "His theoretical framework stands as a bulwark against creeping post-modern _____.",
                    "options": [
                        "nihilism",
                        "altruism",
                        "optimism",
                        "dogmatism"
                    ],
                    "correct": "nihilism",
                    "explanation": "'Nihilism' là thuyết hư vô trong triết học."
                },
                {
                    "id": 13,
                    "question": "The two conflicting ideologies are fundamentally _____ and cannot be synthesized.",
                    "options": [
                        "irreconcilable",
                        "harmonious",
                        "concordant",
                        "amendable"
                    ],
                    "correct": "irreconcilable",
                    "explanation": "'Irreconcilable' mang nghĩa hoàn toàn không thể hòa giải hay dung hợp."
                },
                {
                    "id": 14,
                    "question": "Her eloquent testimony left an indelible impression on the jurors.",
                    "options": [
                        "indelible",
                        "erasable",
                        "evanescent",
                        "fleeting"
                    ],
                    "correct": "indelible",
                    "explanation": "'Indelible impression' là ấn tượng sâu đậm không thể phai mờ."
                },
                {
                    "id": 15,
                    "question": "Were it not for his timely intervention, the corporation _____ into liquidation.",
                    "options": [
                        "would have plunged",
                        "plunges",
                        "will plunge",
                        "had plunged"
                    ],
                    "correct": "would have plunged",
                    "explanation": "Cấu trúc đảo ngữ điều kiện: 'Were it not for N, S + would have + V3'."
                }
            ]
        }
    },
    "TOEIC": {
        "level": "TOEIC",
        "title": "TOEIC 850+ – Luyện Thi Thực Chiến Chuẩn ETS Format 2026",
        "badge": "ETS Standard / 850-990",
        "color": "#8b5cf6",
        "target_audience": "Người đi làm, sinh viên cần chứng chỉ TOEIC 800-900+ phục vụ tuyển dụng doanh nghiệp đa quốc gia và thăng tiến.",
        "outcome": "Làm chủ 7 Part đề thi ETS: Bẫy tranh ảnh Part 1, Phản xạ hỏi đáp Part 2, Hội thoại ngắn Part 3, Độc thoại Part 4, Ngữ pháp & Từ loại Part 5, Điền đoạn văn Part 6, Đọc hiểu đơn/kép/ba Part 7.",
        "modules": [
            {
                "id": "toeic-m1",
                "title": "Bài 1: Chiến Thuật TOEIC Part 5 & Bẫy Từ Loại / Giới Từ",
                "description": "Nhận diện nhanh cấu trúc câu, bẫy từ loại (Noun, Verb, Adj, Adv), đại từ quan hệ và giới từ công sở trong 30 giây.",
                "duration_min": 35,
                "xp": 105,
                "theory": "Part 5 yêu cầu tốc độ xử lý nhanh (trung bình 20-25 giây/câu). Chiến thuật: Xác định vị trí từ cần điền (đứng trước danh từ cần tính từ, đứng sau động từ to be/linking verbs cần tính từ, bổ nghĩa động từ/cả câu dùng trạng từ -ly). Chú ý các đuôi phổ biến: -tion, -sion, -ment (Noun); -able, -ive, -al (Adj); -ly (Adv).",
                "key_vocab": [
                    {
                        "word": "Eligible",
                        "ipa": "/ˈelɪdʒəbl/",
                        "meaning": "Đủ điều kiện",
                        "example": "Employees with two years of service are eligible for promotion."
                    },
                    {
                        "word": "Implement",
                        "ipa": "/ˈɪmplɪment/",
                        "meaning": "Triển khai / Thực thi",
                        "example": "The executive committee voted to implement the new guidelines."
                    },
                    {
                        "word": "Complimentary",
                        "ipa": "/ˌkɑːmplɪˈmentri/",
                        "meaning": "Miễn phí (quà tặng/dịch vụ)",
                        "example": "The hotel offers complimentary shuttle service to the airport."
                    },
                    {
                        "word": "Tentative",
                        "ipa": "/ˈtentətɪv/",
                        "meaning": "Dự kiến / Chưa chính thức",
                        "example": "We have reached a tentative agreement on the project budget."
                    },
                    {
                        "word": "Specification",
                        "ipa": "/ˌspesɪfɪˈkeɪʃn/",
                        "meaning": "Thông số kỹ thuật / Đặc tả",
                        "example": "The product complies with all international specifications."
                    },
                    {
                        "word": "Reimbursement",
                        "ipa": "/ˌriːɪmˈbɜːrsmənt/",
                        "meaning": "Khoản hoàn tiền / Thanh toán lại",
                        "example": "Submit your travel receipts for prompt reimbursement."
                    },
                    {
                        "word": "Inventory",
                        "ipa": "/ˈɪnvəntɔːri/",
                        "meaning": "Hàng tồn kho",
                        "example": "The warehouse is conducting its annual inventory audit."
                    },
                    {
                        "word": "Compliance",
                        "ipa": "/kəmˈplaɪəns/",
                        "meaning": "Sự tuân thủ quy định",
                        "example": "The factory operates in strict compliance with environmental regulations."
                    },
                    {
                        "word": "Merchandise",
                        "ipa": "/ˈmɜːrtʃəndaɪs/",
                        "meaning": "Hàng hóa thương mại",
                        "example": "Defective merchandise can be returned within 30 days."
                    }
                ],
                "grammar_point": {
                    "rule": "Quy tắc trật tự từ loại TOEIC: Mạo từ/Sở hữu + (Trạng từ) + (Tính từ) + Danh từ chính",
                    "formula": "a/an/the/my + (adv) + (adj) + NOUN",
                    "examples": [
                        "a remarkably successful product launch",
                        "an exceptionally talented software engineer"
                    ]
                },
                "listening_task": {
                    "audio_text": "Attention passengers on flight 402 to Chicago: Due to scheduled maintenance, boarding has been delayed by twenty-five minutes. Please wait near Gate 14.",
                    "question": "Why has the flight been delayed?",
                    "options": [
                        "Bad weather",
                        "Scheduled maintenance",
                        "Crew shortage",
                        "Airport closure"
                    ],
                    "ans": "Scheduled maintenance",
                    "exp": "Audio nêu rõ: 'Due to scheduled maintenance, boarding has been delayed'."
                },
                "speaking_prompt": {
                    "target_sentence": "All sales representatives are required to submit their quarterly expense reports by Friday afternoon.",
                    "ipa_focus": "/ɔːl seɪlz ˌreprɪˈzentətɪvz ɑːr rɪˈkwaɪərd/",
                    "tips": "Nhấn mạnh rõ các cụm từ công sở quan trọng: 'sales representatives', 'quarterly expense reports'."
                },
                "writing_task": {
                    "prompt": "Viết email phản hồi ngắn 3 câu gửi khách hàng xác nhận đã nhận đơn hàng và thời gian giao dự kiến.",
                    "hint": "Thank you for your order #... We are pleased to confirm that... Your package will be delivered by...",
                    "sample_answer": "Thank you for your recent order #84920. We are pleased to confirm that your items have been packaged and dispatched from our warehouse. Your shipment is scheduled for delivery by Wednesday morning."
                },
                "dialogue": [
                    {
                        "speaker": "Manager",
                        "text": "Has the vendor finalized the quotation for the new office equipment?"
                    },
                    {
                        "speaker": "Procurement Officer",
                        "text": "Yes, they offered a 15% volume discount if we place the order before the end of the fiscal quarter."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Mr. Henderson reviewed the financial proposal _____ before submitting it to the board.",
                        "options": [
                            "thoroughly",
                            "thorough",
                            "thoroughness",
                            "more thorough"
                        ],
                        "ans": "thoroughly",
                        "exp": "Bổ nghĩa cho động từ 'reviewed' ta cần trạng từ 'thoroughly'."
                    },
                    {
                        "q": "All employees must wear their identification badges at _____ times.",
                        "options": [
                            "all",
                            "every",
                            "each",
                            "whole"
                        ],
                        "ans": "all",
                        "exp": "Cụm từ cố định 'at all times' nghĩa là luôn luôn, mọi lúc."
                    }
                ]
            },
            {
                "id": "toeic-m2",
                "title": "Bài 2: Chiến Thuật TOEIC Part 1 & Part 2 – Phản Xạ Nghe Bẫy Tranh & Hỏi Đáp",
                "description": "Giải mã bẫy tranh người/vật Part 1 (bị động being + V3) và câu trả lời gián tiếp Part 2.",
                "duration_min": 35,
                "xp": 110,
                "theory": "Part 1: Bẫy hành động (being V3) vs trạng thái (has been V3). Part 2: Bẫy lặp từ (same-sound words), bẫy câu trả lời gián tiếp ('Where is the printer?' -> 'I just ordered ink yesterday' hoặc 'Ask Sarah').",
                "key_vocab": [
                    {
                        "word": "Merchandise",
                        "ipa": "/ˈmɜːrtʃəndaɪs/",
                        "meaning": "Hàng hóa trưng bày",
                        "example": "Merchandise is arranged neatly on the shelves."
                    },
                    {
                        "word": "Pedestrian",
                        "ipa": "/pəˈdestriən/",
                        "meaning": "Người đi bộ",
                        "example": "Pedestrians are crossing the street at the zebra crossing."
                    },
                    {
                        "word": "Renovation",
                        "ipa": "/ˌrenəˈveɪʃn/",
                        "meaning": "Sự cải tạo / Trùng tu",
                        "example": "The cafeteria is closed for annual renovation."
                    },
                    {
                        "word": "Postpone",
                        "ipa": "/poʊstˈpoʊn/",
                        "meaning": "Hoãn lại",
                        "example": "The workshop was postponed due to inclement weather."
                    },
                    {
                        "word": "Specification",
                        "ipa": "/ˌspesɪfɪˈkeɪʃn/",
                        "meaning": "Thông số kỹ thuật / Đặc tả",
                        "example": "The product complies with all international specifications."
                    },
                    {
                        "word": "Reimbursement",
                        "ipa": "/ˌriːɪmˈbɜːrsmənt/",
                        "meaning": "Khoản hoàn tiền / Thanh toán lại",
                        "example": "Submit your travel receipts for prompt reimbursement."
                    },
                    {
                        "word": "Inventory",
                        "ipa": "/ˈɪnvəntɔːri/",
                        "meaning": "Hàng tồn kho",
                        "example": "The warehouse is conducting its annual inventory audit."
                    },
                    {
                        "word": "Compliance",
                        "ipa": "/kəmˈplaɪəns/",
                        "meaning": "Sự tuân thủ quy định",
                        "example": "The factory operates in strict compliance with environmental regulations."
                    }
                ],
                "grammar_point": {
                    "rule": "Bẫy thì hiện tại tiếp diễn bị động trong TOEIC Part 1 (S + is/are being + V3)",
                    "formula": "Có người đang thao tác: is being + V3 | Không có người: has been + V3",
                    "examples": [
                        "Boxes are being loaded into the truck. (Có người đang bốc hàng)",
                        "Boxes are stacked in the warehouse. (Hàng hóa đã được xếp sẵn)"
                    ]
                },
                "listening_task": {
                    "audio_text": "Who is responsible for organizing the annual charity gala? - Option A: In the grand ballroom. Option B: Ms. Jenkins from Human Resources. Option C: Yes, at 7 PM.",
                    "question": "Which option correctly answers the question?",
                    "options": [
                        "Option A",
                        "Option B",
                        "Option C",
                        "None of the above"
                    ],
                    "ans": "Option B",
                    "exp": "Hỏi 'Who' thì câu trả lời đúng chỉ người 'Ms. Jenkins from HR'."
                },
                "speaking_prompt": {
                    "target_sentence": "Merchandise is being arranged neatly on display racks throughout the retail store.",
                    "ipa_focus": "/ˈmɜːrtʃəndaɪs ɪz ˈbiːɪŋ əˈreɪndʒd/",
                    "tips": "Nhấn mạnh 'merchandise' và 'display racks'."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu miêu tả một bức ảnh văn phòng công sở có người đang thảo luận trước màn hình máy chiếu.",
                    "hint": "Colleagues are gathered around... A presentation is being displayed...",
                    "sample_answer": "Several colleagues are gathered around a conference table in a modern meeting room. A financial chart is being projected onto the screen at the front."
                },
                "dialogue": [
                    {
                        "speaker": "Interviewer",
                        "text": "Could you tell me who authorized this purchase order?"
                    },
                    {
                        "speaker": "Clerk",
                        "text": "Mr. Davis in procurement signed off on it yesterday afternoon."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "In TOEIC Part 1, if no person is in the photo, statements with 'is being + V3' are almost always:",
                        "options": [
                            "Incorrect (Traps)",
                            "Always correct",
                            "Only correct on Mondays",
                            "Irrelevant"
                        ],
                        "ans": "Incorrect (Traps)",
                        "exp": "'Being + V3' đòi hỏi có người đang thực hiện hành động; nếu tranh không có người thì đây là bẫy sai."
                    },
                    {
                        "q": "When is the project deadline? - Choose the best indirect response:",
                        "options": [
                            "Ask the team lead; she updated the schedule.",
                            "Yes, at 5 PM.",
                            "Because of rain.",
                            "In the conference room."
                        ],
                        "ans": "Ask the team lead; she updated the schedule.",
                        "exp": "Câu trả lời gián tiếp 'Ask the team lead' là đặc sản câu hỏi Part 2 điểm cao."
                    }
                ]
            },
            {
                "id": "toeic-m3",
                "title": "Bài 3: Chiến Thuật TOEIC Part 7 – Đọc Hiểu Đơn, Kép & Ba Đoạn Văn (Triple Passages)",
                "description": "Kỹ thuật quét thông tin (Scanning), đọc lướt (Skimming) và nối thông tin chéo giữa 3 tài liệu trong 55 phút.",
                "duration_min": 40,
                "xp": 115,
                "theory": "Part 7 chiếm 54 câu hỏi. Cần quản lý thời gian nghiêm ngặt (dành 55 phút cho Part 7). Kỹ năng Cross-referencing: Đọc câu hỏi trước, xác định từ khóa (Dates, Names, Order Numbers), liên kết dữ liệu giữa Email - Hóa đơn - Thông báo.",
                "key_vocab": [
                    {
                        "word": "Reimbursement",
                        "ipa": "/ˌriːɪmˈbɜːrsmənt/",
                        "meaning": "Sự hoàn tiền / Thanh toán lại",
                        "example": "Submit travel receipts for expense reimbursement."
                    },
                    {
                        "word": "Itinerary",
                        "ipa": "/aɪˈtɪnəreri/",
                        "meaning": "Lịch trình chuyến đi",
                        "example": "Please review your flight itinerary."
                    },
                    {
                        "word": "Discrepancy",
                        "ipa": "/dɪˈskrepənsi/",
                        "meaning": "Sự không khớp / Sai lệch",
                        "example": "There is a billing discrepancy on invoice #102."
                    },
                    {
                        "word": "Warranty",
                        "ipa": "/ˈwɔːrənti/",
                        "meaning": "Bảo hành",
                        "example": "The laptop comes with a two-year warranty."
                    },
                    {
                        "word": "Specification",
                        "ipa": "/ˌspesɪfɪˈkeɪʃn/",
                        "meaning": "Thông số kỹ thuật / Đặc tả",
                        "example": "The product complies with all international specifications."
                    },
                    {
                        "word": "Inventory",
                        "ipa": "/ˈɪnvəntɔːri/",
                        "meaning": "Hàng tồn kho",
                        "example": "The warehouse is conducting its annual inventory audit."
                    },
                    {
                        "word": "Compliance",
                        "ipa": "/kəmˈplaɪəns/",
                        "meaning": "Sự tuân thủ quy định",
                        "example": "The factory operates in strict compliance with environmental regulations."
                    },
                    {
                        "word": "Merchandise",
                        "ipa": "/ˈmɜːrtʃəndaɪs/",
                        "meaning": "Hàng hóa thương mại",
                        "example": "Defective merchandise can be returned within 30 days."
                    }
                ],
                "grammar_point": {
                    "rule": "Kỹ thuật Paraphrasing trong câu hỏi suy luận TOEIC Part 7",
                    "formula": "Văn bản gốc -> Câu hỏi trắc nghiệm (Đồng nghĩa học thuật)",
                    "examples": [
                        "Text: 'call off the meeting' -> Answer: 'cancel the conference'",
                        "Text: 'at no additional cost' -> Answer: 'complimentary / free of charge'"
                    ]
                },
                "listening_task": {
                    "audio_text": "According to the revised itinerary, the sales seminar has been moved from Thursday to Friday morning to accommodate our overseas delegates.",
                    "question": "Why was the seminar rescheduled?",
                    "options": [
                        "To save money",
                        "To accommodate overseas delegates",
                        "Due to power failure",
                        "Speaker got sick"
                    ],
                    "ans": "To accommodate overseas delegates",
                    "exp": "Audio nêu rõ: 'to accommodate our overseas delegates'."
                },
                "speaking_prompt": {
                    "target_sentence": "All reimbursement claims must be submitted to the finance department within ten business days.",
                    "ipa_focus": "/ɔːl ˌriːɪmˈbɜːrsmənt kleɪmz/",
                    "tips": "Nói rõ 'reimbursement claims' và 'within ten business days'."
                },
                "writing_task": {
                    "prompt": "Viết email phản hồi 3 câu khiếu nại về việc đơn hàng bị giao thiếu 5 sản phẩm và yêu cầu gửi bù.",
                    "hint": "We received shipment #... However, there is a discrepancy... Please dispatch the remaining units...",
                    "sample_answer": "We received shipment #9021 yesterday; however, upon inspection, we discovered a discrepancy of five missing monitor units. Please dispatch the remaining five items immediately via express courier. We appreciate your prompt attention to this matter."
                },
                "dialogue": [
                    {
                        "speaker": "Accountant",
                        "text": "Did the client attach the original receipt for their travel reimbursement?"
                    },
                    {
                        "speaker": "Assistant",
                        "text": "Yes, all boarding passes and hotel invoices are attached to the form."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "In TOEIC Part 7, 'at no extra charge' is paraphrased as:",
                        "options": [
                            "Complimentary",
                            "Expensive",
                            "Penalized",
                            "Delayed"
                        ],
                        "ans": "Complimentary",
                        "exp": "'At no extra charge' đồng nghĩa với 'Complimentary' (miễn phí)."
                    },
                    {
                        "q": "What should a candidate read first before tackling a Triple Passage set?",
                        "options": [
                            "The questions and keywords",
                            "Every single line of text",
                            "The copyright footer",
                            "The author's biography"
                        ],
                        "ans": "The questions and keywords",
                        "exp": "Đọc câu hỏi và bắt từ khóa trước giúp định vị thông tin nhanh trong 3 đoạn văn."
                    }
                ]
            }
        ],
        "exam": {
            "title": "Đề Thi Thử TOEIC Full Format Chuẩn ETS 2026",
            "time_min": 35,
            "pass_score": 75,
            "questions": [
                {
                    "id": 1,
                    "question": "The board of directors voted _____ to approve the acquisition of the logistics firm.",
                    "options": [
                        "unanimously",
                        "unanimous",
                        "unanimity",
                        "more unanimous"
                    ],
                    "correct": "unanimously",
                    "explanation": "Bổ nghĩa cho động từ 'voted' cần trạng từ 'unanimously' (nhất trí đồng thuận)."
                },
                {
                    "id": 2,
                    "question": "Ms. Tanaka is _____ for overseeing all international supply chain operations.",
                    "options": [
                        "responsible",
                        "responsibly",
                        "responsibility",
                        "responsive"
                    ],
                    "correct": "responsible",
                    "explanation": "Cấu trúc 'be responsible for' (chịu trách nhiệm về)."
                },
                {
                    "id": 3,
                    "question": "The conference organizers provided _____ beverages throughout the afternoon workshop.",
                    "options": [
                        "complimentary",
                        "compliment",
                        "complimenting",
                        "complimented"
                    ],
                    "correct": "complimentary",
                    "explanation": "'Complimentary beverages' nghĩa là đồ uống miễn phí phục vụ hội thảo."
                },
                {
                    "id": 4,
                    "question": "All attendees must register at the reception desk _____ entering the main auditorium.",
                    "options": [
                        "prior to",
                        "except",
                        "in spite",
                        "whereas"
                    ],
                    "correct": "prior to",
                    "explanation": "'Prior to + V-ing/Noun' mang nghĩa trước khi làm việc gì."
                },
                {
                    "id": 5,
                    "question": "The marketing department achieved a _____ increase in customer engagement this quarter.",
                    "options": [
                        "substantial",
                        "substance",
                        "substantially",
                        "substantiate"
                    ],
                    "correct": "substantial",
                    "explanation": "Đứng trước danh từ 'increase' cần tính từ 'substantial'."
                },
                {
                    "id": 6,
                    "question": "Please submit your receipts to accounting _____ Friday in order to receive reimbursement.",
                    "options": [
                        "by",
                        "at",
                        "during",
                        "while"
                    ],
                    "correct": "by",
                    "explanation": "Chỉ hạn chót (deadline) trước một thời điểm ta dùng giới từ 'by'."
                },
                {
                    "id": 7,
                    "question": "Neither the project manager nor the software developers _____ notified of the schedule change.",
                    "options": [
                        "were",
                        "was",
                        "has been",
                        "is"
                    ],
                    "correct": "were",
                    "explanation": "Chủ ngữ gần nhất 'the software developers' số nhiều nên động từ chia 'were'."
                },
                {
                    "id": 8,
                    "question": "The updated safety manual outlines strict guidelines for _____ hazardous materials.",
                    "options": [
                        "handling",
                        "handle",
                        "handled",
                        "to handle"
                    ],
                    "correct": "handling",
                    "explanation": "Sau giới từ 'for' ta dùng danh động từ V-ing ('handling')."
                },
                {
                    "id": 9,
                    "question": "_____ the severe snowstorm, the flight departed on time without any delay.",
                    "options": [
                        "Despite",
                        "Although",
                        "Even though",
                        "Because"
                    ],
                    "correct": "Despite",
                    "explanation": "Sau 'Despite' là cụm danh từ (the severe snowstorm)."
                },
                {
                    "id": 10,
                    "question": "The company decided to _____ its overseas manufacturing operations to reduce costs.",
                    "options": [
                        "relocate",
                        "relocating",
                        "relocated",
                        "relocation"
                    ],
                    "correct": "relocate",
                    "explanation": "Cấu trúc 'decide to + V_inf'."
                },
                {
                    "id": 11,
                    "question": "The newly installed server has proven to be extremely _____ during peak traffic.",
                    "options": [
                        "reliable",
                        "reliably",
                        "reliance",
                        "rely"
                    ],
                    "correct": "reliable",
                    "explanation": "Sau linking verb 'prove to be' và trạng từ 'extremely' cần tính từ 'reliable'."
                },
                {
                    "id": 12,
                    "question": "Employees who wish to enroll in the retirement savings plan must _____ form 401B.",
                    "options": [
                        "complete",
                        "completed",
                        "completing",
                        "completion"
                    ],
                    "correct": "complete",
                    "explanation": "Sau động từ khuyết thiếu 'must' là động từ nguyên mẫu 'complete'."
                },
                {
                    "id": 13,
                    "question": "Sales figures for the third quarter were _____ higher than originally projected.",
                    "options": [
                        "significantly",
                        "significant",
                        "significance",
                        "signifying"
                    ],
                    "correct": "significantly",
                    "explanation": "Bổ nghĩa cho tính từ so sánh hơn 'higher' ta dùng trạng từ 'significantly'."
                },
                {
                    "id": 14,
                    "question": "We apologize for any _____ caused by the temporary maintenance of our mobile app.",
                    "options": [
                        "inconvenience",
                        "inconvenient",
                        "inconveniently",
                        "inconveniencing"
                    ],
                    "correct": "inconvenience",
                    "explanation": "Sau 'any' cần một danh từ ('inconvenience')."
                },
                {
                    "id": 15,
                    "question": "The CEO congratulated the research team on their _____ technological breakthrough.",
                    "options": [
                        "exceptional",
                        "exceptionally",
                        "exception",
                        "excepting"
                    ],
                    "correct": "exceptional",
                    "explanation": "Đứng trước cụm danh từ 'technological breakthrough' cần tính từ 'exceptional'."
                }
            ]
        }
    },
    "IELTS": {
        "level": "IELTS",
        "title": "IELTS 8.0+ – Luyện Thi Học Thuật Toàn Diện 4 Kỹ Năng",
        "badge": "IELTS Academic / 7.5-9.0",
        "color": "#06b6d4",
        "target_audience": "Sĩ tử luyện thi IELTS Academic mục tiêu 7.5 - 8.5+ săn học bổng toàn phần, định cư và học tập tại các đại học Ivy League/Russell Group.",
        "outcome": "Làm chủ Writing Task 1 (Mô tả biểu đồ xu hướng, quy trình, bản đồ) & Writing Task 2 (Nghị luận xã hội chuẩn 4 tiêu chí TR, CC, LR, GRA), Speaking 3 Part phản xạ tự nhiên, Paraphrasing C1/C2 đỉnh cao.",
        "modules": [
            {
                "id": "ielts-m1",
                "title": "Bài 1: IELTS Writing Task 2 – Lập Luận Chặt Chẽ & Paraphrasing C1/C2",
                "description": "Phát triển luận điểm (PEEL framework), liên kết mạch lạc (Cohesion & Coherence) và tránh lặp từ bằng từ vựng Band 8.0+.",
                "duration_min": 45,
                "xp": 130,
                "theory": "Để đạt Band 8.0+ Writing Task 2, thí sinh cần thỏa mãn tiêu chí Lexical Resource (từ vựng học thuật, ít phổ biến, collocations tự nhiên) và Grammatical Range and Accuracy (sử dụng linh hoạt câu phức, câu đảo ngữ, mệnh đề quan hệ rút gọn, thể bị động). Khung lập luận PEEL: Point (Nêu ý chính) -> Explanation (Giải thích cơ chế) -> Evidence/Example (Dẫn chứng thực tế) -> Link (Chốt lại vấn đề).",
                "key_vocab": [
                    {
                        "word": "Exacerbate",
                        "ipa": "/ɪɡˈzæsərbeɪt/",
                        "meaning": "Làm trầm trọng thêm",
                        "example": "Unplanned urbanization exacerbates traffic congestion."
                    },
                    {
                        "word": "Detrimental",
                        "ipa": "/ˌdetrɪˈmentl/",
                        "meaning": "Có hại / Gây tổn hại",
                        "example": "Excessive screen time exerts detrimental impacts on sleep patterns."
                    },
                    {
                        "word": "Mitigate",
                        "ipa": "/ˈmɪtɪɡeɪt/",
                        "meaning": "Giảm nhẹ / Xoa dịu",
                        "example": "Afforestation policies help mitigate carbon emissions."
                    },
                    {
                        "word": "Indispensable",
                        "ipa": "/ˌɪndɪˈspensəbl/",
                        "meaning": "Không thể thiếu",
                        "example": "Critical thinking is indispensable for academic research."
                    },
                    {
                        "word": "Deteriorate",
                        "ipa": "/dɪˈtɪriəreɪt/",
                        "meaning": "Suy giảm / Xuống cấp",
                        "example": "Air quality continues to deteriorate in heavily industrialized zones."
                    },
                    {
                        "word": "Fluctuation",
                        "ipa": "/ˌflʌktʃuˈeɪʃn/",
                        "meaning": "Sự biến động dữ liệu",
                        "example": "The graph depicts noticeable fluctuations in renewable energy production."
                    },
                    {
                        "word": "Exponential",
                        "ipa": "/ˌekspəˈnenʃl/",
                        "meaning": "Tăng theo cấp số nhân",
                        "example": "Urban populations have experienced exponential growth over recent decades."
                    },
                    {
                        "word": "Sustainable",
                        "ipa": "/səˈsteɪnəbl/",
                        "meaning": "Bền vững",
                        "example": "Sustainable development balances economic progress with environmental preservation."
                    }
                ],
                "grammar_point": {
                    "rule": "Cấu trúc lập luận tương phản học thuật: While / Whereas & Although clauses",
                    "formula": "While it is argued that X, compelling evidence suggests that Y...",
                    "examples": [
                        "While proponents advocate for technological automation, its socioeconomic repercussions on blue-collar employment cannot be overlooked."
                    ]
                },
                "listening_task": {
                    "audio_text": "While urban expansion fosters commercial growth, it inevitably exerts severe pressure on surrounding natural ecosystems and clean water supplies.",
                    "question": "What is the consequence of urban expansion mentioned?",
                    "options": [
                        "Decreased commerce",
                        "Severe pressure on natural ecosystems",
                        "Improved air quality",
                        "Lower housing costs"
                    ],
                    "ans": "Severe pressure on natural ecosystems",
                    "exp": "Audio nêu rõ: 'exerts severe pressure on surrounding natural ecosystems'."
                },
                "speaking_prompt": {
                    "target_sentence": "From my perspective, adopting sustainable renewable energy sources is imperative to mitigate global climate change.",
                    "ipa_focus": "/frəm maɪ pərˈspektɪv əˈdɑːptɪŋ/",
                    "tips": "Nhấn mạnh tự nhiên vào các từ trọng tâm: 'imperative', 'mitigate', 'climate change'."
                },
                "writing_task": {
                    "prompt": "Viết một đoạn thân bài (Body paragraph) 4 câu thảo luận về lợi ích của trí tuệ nhân tạo trong y tế theo cấu trúc PEEL.",
                    "hint": "Point: AI revolutionizes healthcare... Explanation: By analyzing medical scans... Example: For instance, diagnostic algorithms... Link: Consequently...",
                    "sample_answer": "First and foremost, artificial intelligence enhances diagnostic precision in modern healthcare. By analyzing vast repositories of medical imaging within seconds, machine learning algorithms can detect malignant tumors far earlier than conventional manual assessments. For instance, recent clinical trials demonstrated that AI-assisted screening reduced false-negative mammogram results by 30%. Consequently, integrating such intelligent systems not only optimizes clinical workflows but also directly saves patient lives."
                },
                "dialogue": [
                    {
                        "speaker": "Examiner",
                        "text": "Do you believe governments should prioritize environmental protection over industrial expansion?"
                    },
                    {
                        "speaker": "Candidate",
                        "text": "Undoubtedly. While industrial growth yields short-term economic gains, environmental degradation entails catastrophic long-term consequences that far outweigh transient financial benefits."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Choose the best academic paraphrase for 'make the problem worse':",
                        "options": [
                            "Exacerbate the issue",
                            "Do bad things to the issue",
                            "Make it hard",
                            "Increase the problem"
                        ],
                        "ans": "Exacerbate the issue",
                        "exp": "'Exacerbate the issue' là cụm từ học thuật C1/C2 chuẩn mực thay thế cho 'make the problem worse'."
                    },
                    {
                        "q": "Which connector expresses strong academic concession?",
                        "options": [
                            "Notwithstanding the fact that",
                            "Because",
                            "So that",
                            "And also"
                        ],
                        "ans": "Notwithstanding the fact that",
                        "exp": "'Notwithstanding the fact that' là liên từ nhượng bộ trang trọng bậc cao."
                    }
                ]
            },
            {
                "id": "ielts-m2",
                "title": "Bài 2: IELTS Writing Task 1 – Mô Tả Biểu Đồ Xu Hướng, Quy Trình & Bản Đồ",
                "description": "Cấu trúc 4 đoạn chuẩn mực (Intro, Overview, Body 1, Body 2), từ vựng miêu tả biến động số liệu và quy trình sản xuất.",
                "duration_min": 40,
                "xp": 120,
                "theory": "Writing Task 1 yêu cầu mô tả khách quan trong 20 phút (150+ từ). Cốt lõi là đoạn OVERVIEW (nêu 2 đặc điểm nổi bật nhất không đưa số liệu cụ thể). Từ vựng xu hướng: soar, plummet, fluctuate, level off, plateau.",
                "key_vocab": [
                    {
                        "word": "Plummet",
                        "ipa": "/ˈplʌmɪt/",
                        "meaning": "Lao dốc / Giảm mạnh",
                        "example": "Oil prices plummeted by 30% during the quarter."
                    },
                    {
                        "word": "Fluctuate",
                        "ipa": "/ˈflʌktʃueɪt/",
                        "meaning": "Biến động liên tục",
                        "example": "Tourist arrivals fluctuated wildly between seasons."
                    },
                    {
                        "word": "Plateau",
                        "ipa": "/plæˈtoʊ/",
                        "meaning": "Chạm mức ổn định đi ngang",
                        "example": "Sales leveled off and reached a plateau in 2023."
                    },
                    {
                        "word": "Exponential",
                        "ipa": "/ˌekspəˈnenʃl/",
                        "meaning": "Tăng theo cấp số nhân",
                        "example": "The platform witnessed exponential subscriber growth."
                    },
                    {
                        "word": "Deteriorate",
                        "ipa": "/dɪˈtɪriəreɪt/",
                        "meaning": "Suy giảm / Xuống cấp",
                        "example": "Air quality continues to deteriorate in heavily industrialized zones."
                    },
                    {
                        "word": "Fluctuation",
                        "ipa": "/ˌflʌktʃuˈeɪʃn/",
                        "meaning": "Sự biến động dữ liệu",
                        "example": "The graph depicts noticeable fluctuations in renewable energy production."
                    },
                    {
                        "word": "Sustainable",
                        "ipa": "/səˈsteɪnəbl/",
                        "meaning": "Bền vững",
                        "example": "Sustainable development balances economic progress with environmental preservation."
                    }
                ],
                "grammar_point": {
                    "rule": "Cấu trúc miêu tả xu hướng: There was a [adj] [noun] in X / S experienced a [adj] [noun]",
                    "formula": "There was a dramatic surge in X | X witnessed a steady downward trend",
                    "examples": [
                        "There was a substantial rise in renewable energy adoption between 2015 and 2025.",
                        "Global carbon emissions experienced a transient dip during the lockdown."
                    ]
                },
                "listening_task": {
                    "audio_text": "The line graph illustrates clean energy investments from 2010 to 2024, showing a dramatic upward trajectory that peaked at four hundred billion dollars.",
                    "question": "What does the line graph illustrate?",
                    "options": [
                        "Fossil fuel sales",
                        "Clean energy investments from 2010 to 2024",
                        "Automobile exports",
                        "Government debt"
                    ],
                    "ans": "Clean energy investments from 2010 to 2024",
                    "exp": "Audio nêu rõ: 'illustrates clean energy investments from 2010 to 2024'."
                },
                "speaking_prompt": {
                    "target_sentence": "Overall, clean energy adoption experienced an exponential surge throughout the surveyed decade.",
                    "ipa_focus": "/ɪksˈpɪriənst ən ˌekspəˈnenʃl sɜːrdʒ/",
                    "tips": "Nói rõ cụm từ học thuật 'exponential surge'."
                },
                "writing_task": {
                    "prompt": "Viết đoạn Overview 2 câu cho biểu đồ thể hiện sự gia tăng người dùng internet và giảm sút người đọc báo giấy từ 2010 đến 2025.",
                    "hint": "Overall, it is clear that internet usage... while print newspaper circulation...",
                    "sample_answer": "Overall, it is readily apparent that global internet penetration experienced a dramatic upward trajectory throughout the period. Conversely, print newspaper readership witnessed a steady and continuous decline."
                },
                "dialogue": [
                    {
                        "speaker": "Tutor",
                        "text": "What is the single most vital component of an IELTS Academic Task 1 report?"
                    },
                    {
                        "speaker": "Student",
                        "text": "The Overview paragraph, which synthesizes the overarching trends without bogging down in minute data points."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "In IELTS Task 1, should you include your personal opinion about why the numbers changed?",
                        "options": [
                            "No, strictly factual description only",
                            "Yes, write at least 50 words of opinion",
                            "Only if you agree with the data",
                            "Always put opinion in intro"
                        ],
                        "ans": "No, strictly factual description only",
                        "exp": "Task 1 là bài báo cáo khách quan học thuật, tuyệt đối không đưa quan điểm cá nhân."
                    },
                    {
                        "q": "Which verb describes a sharp, sudden decrease?",
                        "options": [
                            "Plummet",
                            "Rocket",
                            "Plateau",
                            "Soar"
                        ],
                        "ans": "Plummet",
                        "exp": "'Plummet' mang nghĩa lao dốc, sụt giảm nghiêm trọng."
                    }
                ]
            },
            {
                "id": "ielts-m3",
                "title": "Bài 3: IELTS Speaking Part 1-3 – Phản Xạ Tự Nhiên, Trôi Chảy & Phát Triển Ý (Fluency & Coherence)",
                "description": "Chiến lược trả lời Part 1 tự nhiên, mở rộng câu chuyện Part 2 (Storytelling framework) và bàn luận trừu tượng Part 3.",
                "duration_min": 40,
                "xp": 125,
                "theory": "Part 1: Trả lời 2-3 câu ngắn gọn, không 'Yes/No'. Part 2: Nói liên tục 2 phút dùng kỹ thuật Storytelling (Bối cảnh -> Sự việc -> Đỉnh điểm -> Bài học). Part 3: Mở rộng góc nhìn vĩ mô (On a societal level, Economically speaking...).",
                "key_vocab": [
                    {
                        "word": "Spontaneous",
                        "ipa": "/spɑːnˈteɪniəs/",
                        "meaning": "Tự nhiên / Tự phát",
                        "example": "Spontaneous speaking shows high fluency."
                    },
                    {
                        "word": "Elaborate",
                        "ipa": "/ɪˈlæbəreɪt/",
                        "meaning": "Mở rộng / Giải thích chi tiết",
                        "example": "Could you elaborate on your viewpoint?"
                    },
                    {
                        "word": "Perspective",
                        "ipa": "/pərˈspektɪv/",
                        "meaning": "Góc nhìn",
                        "example": "From a macroeconomic perspective, inflation harms consumers."
                    },
                    {
                        "word": "Substantial",
                        "ipa": "/səbˈstænʃl/",
                        "meaning": "Đáng kể",
                        "example": "Tourism yields substantial revenue."
                    },
                    {
                        "word": "Deteriorate",
                        "ipa": "/dɪˈtɪriəreɪt/",
                        "meaning": "Suy giảm / Xuống cấp",
                        "example": "Air quality continues to deteriorate in heavily industrialized zones."
                    },
                    {
                        "word": "Fluctuation",
                        "ipa": "/ˌflʌktʃuˈeɪʃn/",
                        "meaning": "Sự biến động dữ liệu",
                        "example": "The graph depicts noticeable fluctuations in renewable energy production."
                    },
                    {
                        "word": "Exponential",
                        "ipa": "/ˌekspəˈnenʃl/",
                        "meaning": "Tăng theo cấp số nhân",
                        "example": "Urban populations have experienced exponential growth over recent decades."
                    },
                    {
                        "word": "Sustainable",
                        "ipa": "/səˈsteɪnəbl/",
                        "meaning": "Bền vững",
                        "example": "Sustainable development balances economic progress with environmental preservation."
                    }
                ],
                "grammar_point": {
                    "rule": "Discourse Markers for Speaking Part 3: From a macroeconomic perspective / Broadly speaking",
                    "formula": "Well, looking at this issue from a societal perspective, I believe...",
                    "examples": [
                        "Broadly speaking, urban lifestyle promotes individualism, whereas rural communities value solidarity."
                    ]
                },
                "listening_task": {
                    "audio_text": "In response to the examiner's inquiry regarding artificial intelligence in schools, the candidate discussed both personalized learning benefits and risks of diminished critical thinking.",
                    "question": "What two aspects did the candidate discuss?",
                    "options": [
                        "Cost and speed",
                        "Personalized learning and risks of diminished thinking",
                        "Sports and music",
                        "Salary and vacations"
                    ],
                    "ans": "Personalized learning and risks of diminished thinking",
                    "exp": "Audio nêu rõ: 'discussed both personalized learning benefits and risks of diminished critical thinking'."
                },
                "speaking_prompt": {
                    "target_sentence": "Broadly speaking, technological advancements have transformed education into a more interactive and personalized experience.",
                    "ipa_focus": "/ˈbrɔːdli ˈspiːkɪŋ ˌteknəˈlɑːdʒɪkl/",
                    "tips": "Giữ ngữ điệu tự nhiên, không ngập ngừng ậm ừ."
                },
                "writing_task": {
                    "prompt": "Viết dàn ý 3 câu trả lời Speaking Part 3 cho câu hỏi: 'Do you think modern technology makes people feel more isolated?'",
                    "hint": "Well, looking at it from a psychological angle... While connectivity is ubiquitous... Consequently...",
                    "sample_answer": "From a psychological perspective, while digital tools enable instantaneous global connectivity, they frequently replace meaningful face-to-face interactions with superficial online validations. Consequently, many individuals experience profound emotional isolation despite being perpetually online."
                },
                "dialogue": [
                    {
                        "speaker": "Examiner",
                        "text": "How do you foresee the future of remote education in the next two decades?"
                    },
                    {
                        "speaker": "Candidate",
                        "text": "Well, looking at current technological trajectories, I anticipate that immersive virtual reality classrooms will bridge geographic divides and democratize elite academic resources globally."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "In IELTS Speaking Part 3, how should answers generally be framed?",
                        "options": [
                            "General, societal and abstract perspectives",
                            "Personal stories only about your dog",
                            "Single word 'Yes' or 'No'",
                            "Memorized canned scripts"
                        ],
                        "ans": "General, societal and abstract perspectives",
                        "exp": "Part 3 yêu cầu thảo luận các vấn đề trừu tượng mang tính xã hội vĩ mô."
                    },
                    {
                        "q": "Which connector is best to buy 2 seconds of thinking time naturally?",
                        "options": [
                            "Well, that is an intriguing question to consider...",
                            "Shut up examiner.",
                            "I don't know.",
                            "Wait 5 minutes."
                        ],
                        "ans": "Well, that is an intriguing question to consider...",
                        "exp": "'Well, that is an intriguing question to consider...' là filler phrase bản ngữ tự nhiên."
                    }
                ]
            }
        ],
        "exam": {
            "title": "Đề Thi Thử Chuẩn Hóa IELTS Academic Band 8.0+",
            "time_min": 40,
            "pass_score": 75,
            "questions": [
                {
                    "id": 1,
                    "question": "The relentless burning of fossil fuels has _____ the rate of global warming.",
                    "options": [
                        "accelerated",
                        "abated",
                        "deterred",
                        "relinquished"
                    ],
                    "correct": "accelerated",
                    "explanation": "'Accelerate the rate' mang nghĩa đẩy nhanh tốc độ biến đổi khí hậu."
                },
                {
                    "id": 2,
                    "question": "A comprehensive education system should nurture both academic excellence and _____ competencies.",
                    "options": [
                        "socio-emotional",
                        "superficial",
                        "redundant",
                        "fictional"
                    ],
                    "correct": "socio-emotional",
                    "explanation": "'Socio-emotional competencies' là năng lực cảm xúc - xã hội."
                },
                {
                    "id": 3,
                    "question": "Governments must implement stringent regulations to _____ excessive industrial effluent discharge.",
                    "options": [
                        "curb",
                        "stimulate",
                        "encourage",
                        "promote"
                    ],
                    "correct": "curb",
                    "explanation": "'Curb effluent discharge' mang nghĩa kìm hãm, hạn chế việc xả nước thải công nghiệp."
                },
                {
                    "id": 4,
                    "question": "The data revealed a marked disparity _____ urban and rural educational infrastructure.",
                    "options": [
                        "between",
                        "among",
                        "within",
                        "towards"
                    ],
                    "correct": "between",
                    "explanation": "'Disparity between A and B' nghĩa là sự chênh lệch giữa hai đối tượng."
                },
                {
                    "id": 5,
                    "question": "While technological automation enhances efficiency, it poses a _____ threat to unskilled labor.",
                    "options": [
                        "palpable",
                        "negligible",
                        "fanciful",
                        "trivial"
                    ],
                    "correct": "palpable",
                    "explanation": "'Palpable threat' là mối đe dọa rõ rệt, hiện hữu."
                },
                {
                    "id": 6,
                    "question": "The findings of this empirical research are directly _____ to urban planning in developing nations.",
                    "options": [
                        "applicable",
                        "alienated",
                        "incompatible",
                        "irrelevant"
                    ],
                    "correct": "applicable",
                    "explanation": "'Applicable to' mang nghĩa có thể áp dụng vào."
                },
                {
                    "id": 7,
                    "question": "Over-reliance on synthetic fertilizers often leads to soil _____ over time.",
                    "options": [
                        "degradation",
                        "enrichment",
                        "cultivation",
                        "prosperity"
                    ],
                    "correct": "degradation",
                    "explanation": "'Soil degradation' là sự thoái hóa đất."
                },
                {
                    "id": 8,
                    "question": "It is widely acknowledged that early childhood intervention yields _____ societal returns.",
                    "options": [
                        "immense",
                        "meager",
                        "scanty",
                        "trivial"
                    ],
                    "correct": "immense",
                    "explanation": "'Immense returns' mang nghĩa lợi ích to lớn, khổng lồ."
                },
                {
                    "id": 9,
                    "question": "_____ the advent of digital libraries, physical books retain irreplaceable aesthetic value.",
                    "options": [
                        "Notwithstanding",
                        "Due to",
                        "Owing to",
                        "Because of"
                    ],
                    "correct": "Notwithstanding",
                    "explanation": "'Notwithstanding the advent of...' mang nghĩa 'Dẫu cho sự ra đời của...'."
                },
                {
                    "id": 10,
                    "question": "Scholars continue to debate whether genetic predisposition _____ environmental factors in shaping cognitive development.",
                    "options": [
                        "outweighs",
                        "balances",
                        "neutralizes",
                        "negates"
                    ],
                    "correct": "outweighs",
                    "explanation": "'Outweighs' nghĩa là vượt trội hơn, có sức nặng hơn."
                },
                {
                    "id": 11,
                    "question": "Public transport subsidies can effectively _____ commuters from utilizing private motor vehicles.",
                    "options": [
                        "dissuade",
                        "compel",
                        "entice",
                        "coerce"
                    ],
                    "correct": "dissuade",
                    "explanation": "Cấu trúc: 'dissuade someone from doing something' (khuyên can, làm ai từ bỏ việc gì)."
                },
                {
                    "id": 12,
                    "question": "The architectural design seamlessly incorporates passive cooling to maximize energy _____.",
                    "options": [
                        "efficiency",
                        "deficiency",
                        "wastage",
                        "loss"
                    ],
                    "correct": "efficiency",
                    "explanation": "'Energy efficiency' là hiệu suất năng lượng."
                },
                {
                    "id": 13,
                    "question": "Proponents of renewable energy argue that wind and solar power are environmentally _____.",
                    "options": [
                        "benign",
                        "malevolent",
                        "destructive",
                        "detrimental"
                    ],
                    "correct": "benign",
                    "explanation": "'Environmentally benign' mang nghĩa thân thiện, không gây hại cho môi trường."
                },
                {
                    "id": 14,
                    "question": "The graph depicts a dramatic surge in electric vehicle adoptions _____ 2020 and 2025.",
                    "options": [
                        "between",
                        "from",
                        "at",
                        "during"
                    ],
                    "correct": "between",
                    "explanation": "'Between [Year] and [Year]' là cấu trúc chuẩn miêu tả Task 1."
                },
                {
                    "id": 15,
                    "question": "Without adequate oversight, the rapid commercialization of biotechnology could precipitate _____ ethical dilemmas.",
                    "options": [
                        "unprecedented",
                        "obsolete",
                        "archaic",
                        "banal"
                    ],
                    "correct": "unprecedented",
                    "explanation": "'Unprecedented ethical dilemmas' là những nan đề đạo đức chưa từng có tiền lệ."
                }
            ]
        }
    },
    "BUSINESS": {
        "level": "BUSINESS",
        "title": "Business English – Tiếng Anh Thương Mại & Đàm Phán Quốc Tế",
        "badge": "Business BIZ / Ngoại Giao Thương Mại",
        "color": "#ec4899",
        "target_audience": "Doanh nhân, giám đốc kinh doanh, chuyên viên đàm phán, quản lý dự án làm việc với đối tác nước ngoài.",
        "outcome": "Làm chủ nghệ thuật đàm phán hợp đồng, viết email thương mại trang trọng (formal business correspondence), thuyết trình dự án đầu tư (Pitching), và xử lý khiếu nại khách hàng khéo léo.",
        "modules": [
            {
                "id": "biz-m1",
                "title": "Bài 1: Đàm Phán Hợp Đồng, Thương Lượng Giá & Viết Email Ngoại Giao",
                "description": "Các mẫu câu đàm phán nhượng bộ, điều khoản thanh toán (payment terms), thời hạn giao hàng (lead time) và email chốt deal.",
                "duration_min": 40,
                "xp": 110,
                "theory": "Trong đàm phán thương mại quốc tế, phong cách ngoại giao mềm mỏng nhưng kiên định (Firm yet Courteous) là chìa khóa. Sử dụng cấu trúc điều kiện ngoại giao ('Provided that...', 'On condition that...') để tạo thế cân bằng khi đàm phán giảm giá.",
                "key_vocab": [
                    {
                        "word": "Procurement",
                        "ipa": "/prəˈkjʊrmənt/",
                        "meaning": "Hoạt động mua sắm / Thu mua",
                        "example": "Our procurement division negotiates bulk purchase discounts."
                    },
                    {
                        "word": "Feasibility",
                        "ipa": "/ˌfiːzəˈbɪləti/",
                        "meaning": "Tính khả thi của dự án",
                        "example": "We conducted a thorough financial feasibility study."
                    },
                    {
                        "word": "Compromise",
                        "ipa": "/ˈkɑːmprəmaɪz/",
                        "meaning": "Sự thỏa hiệp / Thống nhất đôi bên",
                        "example": "Both parties reached a fair compromise on warranty terms."
                    },
                    {
                        "word": "Memorandum",
                        "ipa": "/ˌmeməˈrændəm/",
                        "meaning": "Biên bản ghi nhớ (MOU)",
                        "example": "We signed a memorandum of understanding with our European distributor."
                    },
                    {
                        "word": "Stakeholder",
                        "ipa": "/ˈsteɪkhoʊldər/",
                        "meaning": "Các bên liên quan",
                        "example": "We must align with key stakeholders before finalizing the agreement."
                    },
                    {
                        "word": "Deliverable",
                        "ipa": "/dɪˈlɪvərəbl/",
                        "meaning": "Sản phẩm / Kết quả bàn giao",
                        "example": "All project deliverables must be signed off by Friday."
                    },
                    {
                        "word": "Due Diligence",
                        "ipa": "/ˌduː ˈdɪlɪdʒəns/",
                        "meaning": "Thẩm định chuyên sâu",
                        "example": "The acquisition is subject to satisfactory due diligence."
                    },
                    {
                        "word": "Benchmark",
                        "ipa": "/ˈbentʃmɑːrk/",
                        "meaning": "Tiêu chuẩn đối sánh",
                        "example": "Our EBITDA margins set the industry benchmark for profitability."
                    }
                ],
                "grammar_point": {
                    "rule": "Cấu trúc điều kiện ngoại giao thương mại: Provided that / On condition that / As long as",
                    "formula": "We are willing to grant X, provided that you agree to Y",
                    "examples": [
                        "We can offer a 10% discount, provided that your initial order volume exceeds 5,000 units.",
                        "On condition that the shipment arrives before June 15, we will waive the penalty clause."
                    ]
                },
                "listening_task": {
                    "audio_text": "We are delighted to confirm that our board has approved the partnership proposal, provided that your team can guarantee delivery within forty-five days.",
                    "question": "Under what condition is the partnership approved?",
                    "options": [
                        "10% price cut",
                        "Delivery within 45 days",
                        "Free training",
                        "Five-year contract"
                    ],
                    "ans": "Delivery within 45 days",
                    "exp": "Audio nêu rõ: 'provided that your team can guarantee delivery within forty-five days'."
                },
                "speaking_prompt": {
                    "target_sentence": "We are prepared to finalize the distribution agreement, provided that our mutual exclusivity rights are respected.",
                    "ipa_focus": "/prəˈvaɪdɪd ðæt aʊər ˈmjuːtʃuəl/",
                    "tips": "Giữ phong thái tự tin, điềm đạm và nhấn âm rõ vào 'finalize' và 'exclusivity rights'."
                },
                "writing_task": {
                    "prompt": "Viết email ngắn 3 câu gửi đối tác để đề xuất lịch hẹn họp bàn về việc ký kết hợp đồng thương mại.",
                    "hint": "I would like to schedule a meeting... Could you please confirm your availability... Looking forward to...",
                    "sample_answer": "I would like to propose a meeting next Tuesday at 10 AM to finalize the terms of our distribution agreement. Please let me know if this timeframe suits your schedule. I look forward to our fruitful collaboration."
                },
                "dialogue": [
                    {
                        "speaker": "Buyer",
                        "text": "Your quotation is slightly higher than our allocated procurement budget."
                    },
                    {
                        "speaker": "Supplier",
                        "text": "If you commit to a two-year supply agreement, we would be happy to adjust the unit price by 8%."
                    },
                    {
                        "speaker": "Buyer",
                        "text": "That sounds like a fair compromise. Let's proceed with drafting the memorandum of understanding."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "Which phrase is the most professional way to make a polite request in business?",
                        "options": [
                            "We would appreciate it if you could...",
                            "You must send us...",
                            "Give us the file now.",
                            "Hurry up and answer."
                        ],
                        "ans": "We would appreciate it if you could...",
                        "exp": "'We would appreciate it if you could...' là mẫu câu lịch sự và chuẩn mực ngoại giao cao cấp trong kinh doanh."
                    },
                    {
                        "q": "What does the abbreviation 'MOU' stand for in business agreements?",
                        "options": [
                            "Memorandum of Understanding",
                            "Management of Units",
                            "Method of Utilization",
                            "Manual of Operations"
                        ],
                        "ans": "Memorandum of Understanding",
                        "exp": "'MOU' là viết tắt của Memorandum of Understanding (Biên bản ghi nhớ hợp tác)."
                    }
                ]
            },
            {
                "id": "biz-m2",
                "title": "Bài 2: Pitching Gọi Vốn, Thuyết Trình Kêu Gọi Đầu Tư & Định Giá (Venture Pitch)",
                "description": "Mẫu câu trình bày mô hình kinh doanh (TAM, SAM, SOM), chỉ số tài chính (CAC, LTV, Burn Rate, ARR) và chốt thỏa thuận cổ phần.",
                "duration_min": 40,
                "xp": 115,
                "theory": "Kỹ thuật Pitching trước quỹ đầu tư mạo hiểm (Venture Capital): Problem -> Solution -> Market Size (TAM) -> Traction & Unit Economics -> Go-To-Market -> The Ask & Use of Funds.",
                "key_vocab": [
                    {
                        "word": "Traction",
                        "ipa": "/ˈtrækʃn/",
                        "meaning": "Sự tăng trưởng khách hàng thực tế",
                        "example": "Our platform has demonstrated explosive user traction."
                    },
                    {
                        "word": "Valuation",
                        "ipa": "/ˌvæljuˈeɪʃn/",
                        "meaning": "Định giá doanh nghiệp",
                        "example": "The pre-money valuation was set at $20 million."
                    },
                    {
                        "word": "Retention",
                        "ipa": "/rɪˈtenʃn/",
                        "meaning": "Tỷ lệ giữ chân khách hàng",
                        "example": "A 92% annual net revenue retention proves strong product-market fit."
                    },
                    {
                        "word": "Synergy",
                        "ipa": "/ˈsɪnərdʒi/",
                        "meaning": "Hiệu ứng cộng hưởng",
                        "example": "The partnership creates tremendous operational synergy."
                    },
                    {
                        "word": "Stakeholder",
                        "ipa": "/ˈsteɪkhoʊldər/",
                        "meaning": "Các bên liên quan",
                        "example": "We must align with key stakeholders before finalizing the agreement."
                    },
                    {
                        "word": "Deliverable",
                        "ipa": "/dɪˈlɪvərəbl/",
                        "meaning": "Sản phẩm / Kết quả bàn giao",
                        "example": "All project deliverables must be signed off by Friday."
                    },
                    {
                        "word": "Due Diligence",
                        "ipa": "/ˌduː ˈdɪlɪdʒəns/",
                        "meaning": "Thẩm định chuyên sâu",
                        "example": "The acquisition is subject to satisfactory due diligence."
                    },
                    {
                        "word": "Benchmark",
                        "ipa": "/ˈbentʃmɑːrk/",
                        "meaning": "Tiêu chuẩn đối sánh",
                        "example": "Our EBITDA margins set the industry benchmark for profitability."
                    }
                ],
                "grammar_point": {
                    "rule": "Persuasive Business Framing: By leveraging X, we achieve Y which captures Z",
                    "formula": "Our proprietary technology enables us to deliver X at a fraction of Y",
                    "examples": [
                        "By automating customer onboarding, we compressed CAC by 60% while expanding gross margins."
                    ]
                },
                "listening_task": {
                    "audio_text": "We are seeking five million dollars in Series A funding to scale our AI-driven supply chain platform across Japan and South Korea.",
                    "question": "What is the capital ask in this pitch?",
                    "options": [
                        "$5 million",
                        "$15 million",
                        "$500,000",
                        "$50 million"
                    ],
                    "ans": "$5 million",
                    "exp": "Audio nêu rõ: 'seeking five million dollars in Series A funding'."
                },
                "speaking_prompt": {
                    "target_sentence": "Our proprietary AI engine reduces customer acquisition cost by forty percent while doubling lifetime value.",
                    "ipa_focus": "/ˈkʌstəmər ˌækwɪˈzɪʃn kɔːst/",
                    "tips": "Nói dứt khoát, thuyết phục và làm nổi bật các con số phần trăm."
                },
                "writing_task": {
                    "prompt": "Viết đoạn Executive Summary 3 câu giới thiệu startup AI của bạn trước các nhà đầu tư mạo hiểm.",
                    "hint": "We are building the next-generation... Our platform has achieved... We are raising...",
                    "sample_answer": "We are building the next-generation autonomous customer support infrastructure for e-commerce enterprises. Over the past twelve months, we have achieved $2.4M in Annual Recurring Revenue with 140% net revenue retention. We are currently raising a $6M Series A round to accelerate international expansion."
                },
                "dialogue": [
                    {
                        "speaker": "Venture Partner",
                        "text": "What is your current Customer Acquisition Cost and Payback Period?"
                    },
                    {
                        "speaker": "Founder",
                        "text": "Our blended CAC is currently $320, with an average payback period of just under four months."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "What does the abbreviation 'LTV' represent in startup finance?",
                        "options": [
                            "Lifetime Value of a Customer",
                            "Long Time Vacation",
                            "Legal Tax Valuation",
                            "Lowest Trading Volume"
                        ],
                        "ans": "Lifetime Value of a Customer",
                        "exp": "'LTV' là Giá trị vòng đời của một khách hàng (Customer Lifetime Value)."
                    },
                    {
                        "q": "Which metric proves that existing customers are paying more over time?",
                        "options": [
                            "Net Revenue Retention > 100%",
                            "High employee turnover",
                            "Zero sales",
                            "High burn rate"
                        ],
                        "ans": "Net Revenue Retention > 100%",
                        "exp": "Chỉ số Net Revenue Retention (NRR) > 100% chứng minh doanh thu từ khách hàng cũ liên tục tăng trưởng."
                    }
                ]
            }
        ],
        "exam": {
            "title": "Bài Đánh Giá Năng Lực Tiếng Anh Thương Mại Quốc Tế",
            "time_min": 30,
            "pass_score": 75,
            "questions": [
                {
                    "id": 1,
                    "question": "Provided that all regulatory approvals are granted, the merger will be _____ by the end of Q3.",
                    "options": [
                        "finalized",
                        "final",
                        "finalize",
                        "finalizing"
                    ],
                    "correct": "finalized",
                    "explanation": "Cấu trúc bị động ở tương lai: 'will be + V3/ed' -> 'finalized'."
                },
                {
                    "id": 2,
                    "question": "Our primary objective during this fiscal year is to expand our market _____ in Southeast Asia.",
                    "options": [
                        "share",
                        "divider",
                        "slice",
                        "portion"
                    ],
                    "correct": "share",
                    "explanation": "'Market share' là thuật ngữ kinh doanh chỉ thị phần."
                },
                {
                    "id": 3,
                    "question": "The procurement committee decided to _____ negotiations due to unresolved licensing clauses.",
                    "options": [
                        "suspend",
                        "accelerate",
                        "rejoice",
                        "disregard"
                    ],
                    "correct": "suspend",
                    "explanation": "'Suspend negotiations' mang nghĩa tạm đình chỉ, hoãn lại cuộc đàm phán."
                },
                {
                    "id": 4,
                    "question": "We are confident that this joint venture will yield _____ returns for both organizations.",
                    "options": [
                        "substantial",
                        "meager",
                        "frivolous",
                        "negligible"
                    ],
                    "correct": "substantial",
                    "explanation": "'Yield substantial returns' mang nghĩa mang lại lợi tức to lớn, khả quan."
                },
                {
                    "id": 5,
                    "question": "Please find attached the non-disclosure agreement for your _____ and signature.",
                    "options": [
                        "perusal",
                        "leisure",
                        "hesitation",
                        "reluctance"
                    ],
                    "correct": "perusal",
                    "explanation": "'For your perusal and signature' là cụm từ trang trọng trong thư tín thương mại chỉ việc gửi văn bản để đọc kỹ và ký duyệt."
                },
                {
                    "id": 6,
                    "question": "The financial audit revealed a significant deficit in the company's _____ flow.",
                    "options": [
                        "cash",
                        "money",
                        "coin",
                        "currency"
                    ],
                    "correct": "cash",
                    "explanation": "'Cash flow' là dòng tiền trong doanh nghiệp."
                },
                {
                    "id": 7,
                    "question": "Our company has secured a _____ partnership with a leading European manufacturer.",
                    "options": [
                        "lucrative",
                        "penitent",
                        "trivial",
                        "meager"
                    ],
                    "correct": "lucrative",
                    "explanation": "'Lucrative partnership' là mối quan hệ đối tác sinh lời cao."
                },
                {
                    "id": 8,
                    "question": "The supplier offered a 5% discount on all orders placed in _____.",
                    "options": [
                        "bulk",
                        "mass",
                        "crowd",
                        "heap"
                    ],
                    "correct": "bulk",
                    "explanation": "'In bulk' nghĩa là mua với số lượng lớn (bán buôn/sỉ)."
                },
                {
                    "id": 9,
                    "question": "We must conduct thorough due _____ before finalizing the acquisition.",
                    "options": [
                        "diligence",
                        "negligence",
                        "arrogance",
                        "hesitation"
                    ],
                    "correct": "diligence",
                    "explanation": "'Due diligence' là quá trình thẩm định chi tiết trước khi mua bán, sáp nhập doanh nghiệp."
                },
                {
                    "id": 10,
                    "question": "All terms and conditions stipulated in the contract are legally _____.",
                    "options": [
                        "binding",
                        "bonding",
                        "holding",
                        "fastening"
                    ],
                    "correct": "binding",
                    "explanation": "'Legally binding' mang nghĩa có tính ràng buộc pháp lý."
                },
                {
                    "id": 11,
                    "question": "We regret to inform you that we cannot accept your _____ of delivery.",
                    "options": [
                        "terms",
                        "words",
                        "sounds",
                        "speeches"
                    ],
                    "correct": "terms",
                    "explanation": "'Terms of delivery' là các điều khoản giao hàng."
                },
                {
                    "id": 12,
                    "question": "The marketing team launched a campaign to increase customer _____.",
                    "options": [
                        "retention",
                        "rejection",
                        "evasion",
                        "omission"
                    ],
                    "correct": "retention",
                    "explanation": "'Customer retention' là tỷ lệ giữ chân khách hàng."
                },
                {
                    "id": 13,
                    "question": "Failure to fulfill the obligations will constitute a material _____ of contract.",
                    "options": [
                        "breach",
                        "gap",
                        "crack",
                        "split"
                    ],
                    "correct": "breach",
                    "explanation": "'Breach of contract' là hành vi vi phạm hợp đồng."
                },
                {
                    "id": 14,
                    "question": "The startup successfully raised $5 million in its Series A _____ round.",
                    "options": [
                        "funding",
                        "founding",
                        "find",
                        "fund"
                    ],
                    "correct": "funding",
                    "explanation": "'Funding round' là vòng gọi vốn đầu tư."
                },
                {
                    "id": 15,
                    "question": "Please ensure that the invoice is settled _____ thirty days of receipt.",
                    "options": [
                        "within",
                        "among",
                        "along",
                        "behind"
                    ],
                    "correct": "within",
                    "explanation": "'Within thirty days' nghĩa là trong vòng 30 ngày."
                }
            ]
        }
    },
    "TECH": {
        "level": "TECH",
        "title": "Tech & AI English – Tiếng Anh Chuyên Ngành CNTT & Trí Tuệ Nhân Tạo",
        "badge": "IT & AI / Kỹ thuật Công nghệ",
        "color": "#14b8a6",
        "target_audience": "Lập trình viên, kỹ sư AI, Data Scientist, Tech Lead muốn giao tiếp mượt mà trong các cuộc họp Agile/Scrum, đọc tài liệu kỹ thuật và phỏng vấn công ty công nghệ đa quốc gia.",
        "outcome": "Làm chủ 1000+ thuật ngữ IT/AI, thuyết trình giải pháp kiến trúc hệ thống (Architecture Review), viết Pull Request, và thảo luận tối ưu thuật toán LLM/Microservices.",
        "modules": [
            {
                "id": "tech-m1",
                "title": "Bài 1: Agile Standup, Architecture Review & Thảo Luận Kỹ Thuật",
                "description": "Các mẫu câu báo cáo tiến độ daily standup, thảo luận xử lý bug, tối ưu microservices và tích hợp mô hình LLM.",
                "duration_min": 35,
                "xp": 115,
                "theory": "Trong môi trường công nghệ hiện đại, khả năng mô tả ngắn gọn vấn đề kỹ thuật (Technical conciseness) là yếu tố quyết định. Cấu trúc Agile Daily Standup kinh điển: 'Yesterday I [V-ed]... Today I will [V_inf]... I am currently blocked by [Obstacle]...'.",
                "key_vocab": [
                    {
                        "word": "Scalability",
                        "ipa": "/ˌskeɪləˈbɪləti/",
                        "meaning": "Khả năng mở rộng hệ thống",
                        "example": "Our distributed cloud architecture ensures high scalability."
                    },
                    {
                        "word": "Deployment",
                        "ipa": "/dɪˈplɔɪmənt/",
                        "meaning": "Sự triển khai phần mềm",
                        "example": "The automated CI/CD pipeline streamlined production deployment."
                    },
                    {
                        "word": "Latency",
                        "ipa": "/ˈleɪtnsi/",
                        "meaning": "Độ trễ",
                        "example": "We optimized our vector database to minimize inference latency."
                    },
                    {
                        "word": "Refactor",
                        "ipa": "/ˌriːˈfæktər/",
                        "meaning": "Tái cấu trúc mã nguồn",
                        "example": "We need to refactor this legacy module to enhance maintainability."
                    },
                    {
                        "word": "Asynchronous",
                        "ipa": "/eɪˈsɪŋkrənəs/",
                        "meaning": "Bất đồng bộ",
                        "example": "We utilize asynchronous messaging queues to decouple microservices."
                    },
                    {
                        "word": "Idempotent",
                        "ipa": "/aɪˈdempətənt/",
                        "meaning": "Bất biến khi gọi lặp (API)",
                        "example": "Ensure that all payment processing endpoints are strictly idempotent."
                    }
                ],
                "grammar_point": {
                    "rule": "Mô tả nguyên nhân - kết quả kỹ thuật: Causative verbs & Consequence linkers",
                    "formula": "Due to X, the service experienced Y | By implementing X, we reduced Y by Z%",
                    "examples": [
                        "By caching frequent query responses in Redis, we reduced server load by 45%.",
                        "The memory leak was caused by an unclosed database connection pool."
                    ]
                },
                "listening_task": {
                    "audio_text": "Team, we have successfully migrated our backend services to Kubernetes clusters, which reduced our API response latency from two hundred milliseconds down to forty-five milliseconds.",
                    "question": "What is the new API response latency?",
                    "options": [
                        "200 ms",
                        "120 ms",
                        "45 ms",
                        "15 ms"
                    ],
                    "ans": "45 ms",
                    "exp": "Audio nêu rõ: 'reduced latency from 200 ms down to 45 ms'."
                },
                "speaking_prompt": {
                    "target_sentence": "Yesterday I implemented the real-time WebSocket connection, and today I am writing automated unit tests.",
                    "ipa_focus": "/aɪ ˈɪmplɪmentɪd ðə ˈriːəl taɪm/",
                    "tips": "Nói rõ ràng, tự tin các thuật ngữ kỹ thuật như WebSocket, automated unit tests."
                },
                "writing_task": {
                    "prompt": "Viết mô tả Pull Request (PR description) 3 câu tóm tắt tính năng mới bạn vừa phát triển.",
                    "hint": "This PR introduces... It resolves issue #... All unit tests have passed.",
                    "sample_answer": "This PR introduces an asynchronous caching layer using Redis to optimize vector query latency. It resolves issue #142 and improves database throughput under high traffic. All automated unit and integration tests have passed successfully."
                },
                "dialogue": [
                    {
                        "speaker": "Scrum Master",
                        "text": "Alex, how is the AI teacher integration progressing?"
                    },
                    {
                        "speaker": "Alex",
                        "text": "I have completed the backend streaming API. Today I am benchmarking token latency with Gemini 1.5 Flash."
                    },
                    {
                        "speaker": "Scrum Master",
                        "text": "Are there any blockers preventing deployment to staging?"
                    },
                    {
                        "speaker": "Alex",
                        "text": "None at the moment; everything is on track for tomorrow's demo."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "What is the standard term for improving code structure without changing its external behavior?",
                        "options": [
                            "Refactoring",
                            "Compiling",
                            "Overriding",
                            "Deprecating"
                        ],
                        "ans": "Refactoring",
                        "exp": "'Refactoring' là tái cấu trúc code giúp code sạch hơn mà không đổi logic."
                    },
                    {
                        "q": "Which data structure is optimal for semantic search in Large Language Model applications?",
                        "options": [
                            "Vector Database",
                            "Relational Table",
                            "Linked List",
                            "Binary Search Tree"
                        ],
                        "ans": "Vector Database",
                        "exp": "'Vector Database' lưu trữ embeddings cho tìm kiếm tương đồng ngữ nghĩa."
                    }
                ]
            },
            {
                "id": "tech-m2",
                "title": "Bài 2: Kiến Trúc Microservices, Cloud Infrastructure & DevOps CI/CD",
                "description": "Giao tiếp về Docker containers, Kubernetes orchestration, load balancers, database sharding và uptime SLA.",
                "duration_min": 40,
                "xp": 120,
                "theory": "Thuật ngữ kiến trúc hạ tầng: Monolith vs Microservices, Containerization, Auto-scaling, Redundancy, Zero-downtime deployment, Canary release. Các chỉ số: Latency (p99), Throughput (RPS), Uptime (99.99%).",
                "key_vocab": [
                    {
                        "word": "Orchestration",
                        "ipa": "/ˌɔːrkɪˈstreɪʃn/",
                        "meaning": "Sự điều phối hệ thống container",
                        "example": "Kubernetes simplifies container orchestration."
                    },
                    {
                        "word": "Redundancy",
                        "ipa": "/rɪˈdʌndənsi/",
                        "meaning": "Tính dư thừa dự phòng",
                        "example": "Multi-region redundancy prevents catastrophic downtime."
                    },
                    {
                        "word": "Throughput",
                        "ipa": "/ˈθruːpʊt/",
                        "meaning": "Lưu lượng xử lý",
                        "example": "Our payment gateway handles 5,000 requests per second throughput."
                    },
                    {
                        "word": "Provision",
                        "ipa": "/prəˈvɪʒn/",
                        "meaning": "Cấp phát tài nguyên",
                        "example": "Terraform scripts automate cloud resource provisioning."
                    },
                    {
                        "word": "Scalability",
                        "ipa": "/ˌskeɪləˈbɪləti/",
                        "meaning": "Khả năng mở rộng hệ thống",
                        "example": "Cloud-native architectures offer elastic scalability under heavy traffic."
                    },
                    {
                        "word": "Asynchronous",
                        "ipa": "/eɪˈsɪŋkrənəs/",
                        "meaning": "Bất đồng bộ",
                        "example": "We utilize asynchronous messaging queues to decouple microservices."
                    },
                    {
                        "word": "Idempotent",
                        "ipa": "/aɪˈdempətənt/",
                        "meaning": "Bất biến khi gọi lặp (API)",
                        "example": "Ensure that all payment processing endpoints are strictly idempotent."
                    },
                    {
                        "word": "Latency",
                        "ipa": "/ˈleɪtnsi/",
                        "meaning": "Độ trễ phản hồi mạng",
                        "example": "Edge caching reduces API response latency to under 20 milliseconds."
                    }
                ],
                "grammar_point": {
                    "rule": "Cấu trúc mô tả giải pháp kiến trúc: To ensure X, we utilize Y which enables Z",
                    "formula": "In order to mitigate X, the system architecture incorporates Y",
                    "examples": [
                        "In order to guarantee high availability, our architecture incorporates multi-zone database replicas.",
                        "To optimize cold starts, we configure provisioned concurrency for critical Lambda functions."
                    ]
                },
                "listening_task": {
                    "audio_text": "By deploying an asynchronous message broker like Apache Kafka, we decoupled the payment service from the order fulfillment pipeline.",
                    "question": "What did Apache Kafka help decouple?",
                    "options": [
                        "Payment service from order fulfillment",
                        "Frontend from CSS",
                        "Database from hard drive",
                        "Users from app"
                    ],
                    "ans": "Payment service from order fulfillment",
                    "exp": "Audio nêu rõ: 'decoupled the payment service from the order fulfillment pipeline'."
                },
                "speaking_prompt": {
                    "target_sentence": "We migrated our monolithic backend to a distributed Kubernetes cluster to achieve zero-downtime deployments.",
                    "ipa_focus": "/wɪ maɪˈɡreɪtɪd aʊər ˌmɑːnəˈlɪθɪk/",
                    "tips": "Nói rõ 'monolithic backend' và 'Kubernetes cluster'."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu mô tả kiến trúc kỹ thuật của hệ thống thanh toán có khả năng chịu tải 10,000 giao dịch/giây.",
                    "hint": "Our payment infrastructure employs... To handle high throughput, we implement...",
                    "sample_answer": "Our payment infrastructure employs a distributed event-driven architecture powered by Apache Kafka. To sustain a throughput of 10,000 transactions per second, we implement automated horizontal pod autoscaling across multi-region cloud clusters."
                },
                "dialogue": [
                    {
                        "speaker": "Tech Lead",
                        "text": "How do we handle failover if the primary database cluster goes down?"
                    },
                    {
                        "speaker": "DevOps Engineer",
                        "text": "Our automated health check triggers an instant DNS switch to the standby replica in under three seconds."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "What term describes decoupling services so they communicate via asynchronous messages?",
                        "options": [
                            "Event-driven architecture",
                            "Monolithic structure",
                            "Hardcoded linkage",
                            "Waterfall lifecycle"
                        ],
                        "ans": "Event-driven architecture",
                        "exp": "Event-driven architecture cho phép các microservices giao tiếp bất đồng bộ qua message queues."
                    },
                    {
                        "q": "What does a 99.99% (four nines) SLA guarantee?",
                        "options": [
                            "Extremely minimal annual downtime (~52 minutes)",
                            "Zero bugs in software",
                            "Free cloud hosting",
                            "Instant salary raise"
                        ],
                        "ans": "Extremely minimal annual downtime (~52 minutes)",
                        "exp": "Four nines (99.99% uptime) tương đương thời gian gián đoạn tối đa khoảng 52 phút mỗi năm."
                    }
                ]
            },
            {
                "id": "tech-m3",
                "title": "Bài 3: Trí Tuệ Nhân Tạo, Mô Hình LLM & Kỹ Thuật Prompt Engineering",
                "description": "Thảo luận về RAG, Vector Embeddings, Fine-tuning, Tokenomics, và đánh giá an toàn AI (Red Teaming).",
                "duration_min": 40,
                "xp": 125,
                "theory": "Hệ sinh thái LLM: Retrieval-Augmented Generation (RAG), Semantic Search qua Cosine Similarity, Context Window, Temperature parameter, Hallucination mitigation, Guardrails và AI Alignment.",
                "key_vocab": [
                    {
                        "word": "Hallucination",
                        "ipa": "/həˌluːsɪˈneɪʃn/",
                        "meaning": "Hiện tượng ảo giác AI (trả lời bịa)",
                        "example": "RAG architecture drastically minimizes model hallucination."
                    },
                    {
                        "word": "Embedding",
                        "ipa": "/ɪmˈbedɪŋ/",
                        "meaning": "Biểu diễn vector của văn bản",
                        "example": "Text embeddings capture rich semantic relationships."
                    },
                    {
                        "word": "Alignment",
                        "ipa": "/əˈlaɪnmənt/",
                        "meaning": "Sự tương thích an toàn với con người",
                        "example": "AI alignment ensures models adhere to ethical principles."
                    },
                    {
                        "word": "Inference",
                        "ipa": "/ˈɪnfərəns/",
                        "meaning": "Quá trình suy luận / sinh kết quả",
                        "example": "We quantized the model weights to accelerate GPU inference."
                    },
                    {
                        "word": "Scalability",
                        "ipa": "/ˌskeɪləˈbɪləti/",
                        "meaning": "Khả năng mở rộng hệ thống",
                        "example": "Cloud-native architectures offer elastic scalability under heavy traffic."
                    },
                    {
                        "word": "Asynchronous",
                        "ipa": "/eɪˈsɪŋkrənəs/",
                        "meaning": "Bất đồng bộ",
                        "example": "We utilize asynchronous messaging queues to decouple microservices."
                    },
                    {
                        "word": "Idempotent",
                        "ipa": "/aɪˈdempətənt/",
                        "meaning": "Bất biến khi gọi lặp (API)",
                        "example": "Ensure that all payment processing endpoints are strictly idempotent."
                    },
                    {
                        "word": "Latency",
                        "ipa": "/ˈleɪtnsi/",
                        "meaning": "Độ trễ phản hồi mạng",
                        "example": "Edge caching reduces API response latency to under 20 milliseconds."
                    }
                ],
                "grammar_point": {
                    "rule": "Technical causality & Quantitative comparison in AI benchmarks",
                    "formula": "By quantizing the weights to 4-bit, inference throughput increased by X% while memory footprint dropped by Y%",
                    "examples": [
                        "By indexing domain documents into a vector database, retrieval accuracy improved from 65% to 94%."
                    ]
                },
                "listening_task": {
                    "audio_text": "To mitigate hallucinations in our AI English tutor, we integrated a RAG pipeline that grounds all grammar explanations in certified CEFR textbooks.",
                    "question": "Why did the engineering team integrate RAG?",
                    "options": [
                        "To increase price",
                        "To mitigate hallucinations and ground explanations",
                        "To delete the database",
                        "To stop using AI"
                    ],
                    "ans": "To mitigate hallucinations and ground explanations",
                    "exp": "Audio nêu rõ: 'To mitigate hallucinations in our AI English tutor, we integrated a RAG pipeline'."
                },
                "speaking_prompt": {
                    "target_sentence": "We implemented a Retrieval-Augmented Generation architecture to guarantee high factual accuracy in our AI responses.",
                    "ipa_focus": "/rɪˈtriːvl ɔːɡˈmentɪd ˌdʒenəˈreɪʃn/",
                    "tips": "Nói rõ 'Retrieval-Augmented Generation' và 'factual accuracy'."
                },
                "writing_task": {
                    "prompt": "Viết 2 câu phân tích lý do tại sao RAG vượt trội hơn so với việc chỉ dựa vào kiến thức huấn luyện sẵn của LLM.",
                    "hint": "Standard LLMs suffer from knowledge cutoffs... By contrast, RAG retrieves real-time proprietary data...",
                    "sample_answer": "Standard Large Language Models frequently suffer from knowledge cutoffs and hallucinations. By contrast, a RAG pipeline dynamically retrieves verified domain knowledge from vector databases, ensuring deterministic and factual AI outputs."
                },
                "dialogue": [
                    {
                        "speaker": "AI Lead",
                        "text": "Are we observing significant latency spikes during vector similarity retrieval?"
                    },
                    {
                        "speaker": "Data Engineer",
                        "text": "Not at all. With HNSW indexing in our Milvus cluster, p95 query latency remains under 15 milliseconds."
                    }
                ],
                "practice_quiz": [
                    {
                        "q": "What is the primary objective of Retrieval-Augmented Generation (RAG)?",
                        "options": [
                            "Grounding model outputs in external factual data",
                            "Increasing electricity consumption",
                            "Deleting vector indices",
                            "Training models from scratch"
                        ],
                        "ans": "Grounding model outputs in external factual data",
                        "exp": "RAG cung cấp dữ liệu thực tế đã xác thực cho LLM để loại bỏ ảo giác (hallucinations)."
                    },
                    {
                        "q": "Which metric measures the similarity between two normalized embedding vectors?",
                        "options": [
                            "Cosine similarity",
                            "Random guessing",
                            "Alphabetical order",
                            "File size"
                        ],
                        "ans": "Cosine similarity",
                        "exp": "Cosine similarity đo góc giữa 2 vector để xác định độ tương đồng ngữ nghĩa."
                    }
                ]
            }
        ],
        "exam": {
            "title": "Bài Đánh Giá Tiếng Anh Chuyên Ngành IT & Trí Tuệ Nhân Tạo",
            "time_min": 30,
            "pass_score": 75,
            "questions": [
                {
                    "id": 1,
                    "question": "The database query was slow because the table was missing an appropriate _____ on the foreign key.",
                    "options": [
                        "index",
                        "pointer",
                        "syntax",
                        "variable"
                    ],
                    "correct": "index",
                    "explanation": "Trong cơ sở dữ liệu, việc thiếu 'index' (chỉ mục) sẽ làm câu truy vấn bị chậm."
                },
                {
                    "id": 2,
                    "question": "Our microservices architecture ensures high availability, _____ if one pod crashes, traffic is rerouted automatically.",
                    "options": [
                        "so that",
                        "in order to",
                        "because of",
                        "despite"
                    ],
                    "correct": "so that",
                    "explanation": "'So that' (để cho / nhờ đó mà) chỉ kết quả, mục đích logic của kiến trúc."
                },
                {
                    "id": 3,
                    "question": "To prevent unauthorized access, all RESTful API endpoints are protected by OAuth 2.0 _____ tokens.",
                    "options": [
                        "bearer",
                        "carrier",
                        "porter",
                        "messenger"
                    ],
                    "correct": "bearer",
                    "explanation": "'Bearer tokens' là thuật ngữ kỹ thuật chuẩn mực trong chuẩn xác thực OAuth 2.0."
                },
                {
                    "id": 4,
                    "question": "The machine learning team achieved a _____ accuracy rate of 98.4% on the validation dataset.",
                    "options": [
                        "remarkable",
                        "marginal",
                        "dubious",
                        "negligible"
                    ],
                    "correct": "remarkable",
                    "explanation": "'Remarkable accuracy rate' mang nghĩa tỷ lệ chính xác ấn tượng, vượt trội."
                },
                {
                    "id": 5,
                    "question": "Before merging the feature branch into main, developers must ensure all CI/CD pipeline checks _____.",
                    "options": [
                        "have passed",
                        "passing",
                        "passed had",
                        "were fail"
                    ],
                    "correct": "have passed",
                    "explanation": "'Ensure all checks have passed' (Đảm bảo mọi kiểm tra đã vượt qua thành công)."
                },
                {
                    "id": 6,
                    "question": "To scale our backend horizontally, we deployed containerized services managed by a _____ cluster.",
                    "options": [
                        "Kubernetes",
                        "Monolith",
                        "Waterfall",
                        "Spreadsheet"
                    ],
                    "correct": "Kubernetes",
                    "explanation": "Kubernetes là nền tảng điều phối container phổ biến để mở rộng hệ thống theo chiều ngang."
                },
                {
                    "id": 7,
                    "question": "A memory leak occurred because the asynchronous thread pool was not properly _____ upon shutdown.",
                    "options": [
                        "terminated",
                        "inflated",
                        "duplicated",
                        "compiled"
                    ],
                    "correct": "terminated",
                    "explanation": "'Terminated' nghĩa là được giải phóng, đóng kết thúc đúng cách."
                },
                {
                    "id": 8,
                    "question": "The development team decided to _____ the legacy API endpoint in favor of GraphQL.",
                    "options": [
                        "deprecate",
                        "appreciate",
                        "replicate",
                        "accelerate"
                    ],
                    "correct": "deprecate",
                    "explanation": "'Deprecate' là khai tử, không còn hỗ trợ một API hay hàm cũ."
                },
                {
                    "id": 9,
                    "question": "Our deep neural network model is vulnerable to _____ attacks if input embeddings are maliciously perturbed.",
                    "options": [
                        "adversarial",
                        "benevolent",
                        "complimentary",
                        "fictitious"
                    ],
                    "correct": "adversarial",
                    "explanation": "'Adversarial attacks' là kiểu tấn công đối kháng trong học máy."
                },
                {
                    "id": 10,
                    "question": "To minimize cold start latency, serverless functions are configured with _____ concurrency.",
                    "options": [
                        "provisioned",
                        "improvised",
                        "abandoned",
                        "relinquished"
                    ],
                    "correct": "provisioned",
                    "explanation": "'Provisioned concurrency' là tài nguyên được cấp phát sẵn để tránh độ trễ khởi động nguội."
                },
                {
                    "id": 11,
                    "question": "The security team identified a cross-site scripting (XSS) _____ in the user comments section.",
                    "options": [
                        "vulnerability",
                        "immunity",
                        "robustness",
                        "encryption"
                    ],
                    "correct": "vulnerability",
                    "explanation": "'Vulnerability' là lỗ hổng bảo mật."
                },
                {
                    "id": 12,
                    "question": "In our Agile workflow, sprint planning occurs _____ every two weeks.",
                    "options": [
                        "biweekly",
                        "bimonthly",
                        "biannually",
                        "biennially"
                    ],
                    "correct": "biweekly",
                    "explanation": "'Biweekly' mang nghĩa định kỳ 2 tuần một lần."
                },
                {
                    "id": 13,
                    "question": "The Retrieval-Augmented Generation (RAG) pipeline indexes documents into a _____ database for similarity search.",
                    "options": [
                        "vector",
                        "relational",
                        "flat-file",
                        "binary"
                    ],
                    "correct": "vector",
                    "explanation": "'Vector database' là cơ sở dữ liệu vector dùng cho tìm kiếm tương đồng ngữ nghĩa trong hệ thống RAG."
                },
                {
                    "id": 14,
                    "question": "All software releases must undergo thorough regression testing to prevent unexpected _____ in existing features.",
                    "options": [
                        "breakages",
                        "enhancements",
                        "innovations",
                        "boosts"
                    ],
                    "correct": "breakages",
                    "explanation": "'Breakages' chỉ các lỗi hỏng hóc phát sinh ngoài ý muốn trên tính năng sẵn có."
                },
                {
                    "id": 15,
                    "question": "The system utilizes an event-driven architecture powered by Kafka for real-time data _____.",
                    "options": [
                        "streaming",
                        "stagnation",
                        "freezing",
                        "halting"
                    ],
                    "correct": "streaming",
                    "explanation": "'Data streaming' là luồng truyền phát dữ liệu thời gian thực."
                }
            ]
        }
    }
}

# ══════════════════════════════════════════════════════════════════════════════
# ── MERGE EXTENDED 30 MODULES FOR A1, A2, B1, B2, C1, C2, TOEIC & IELTS ────────
# ══════════════════════════════════════════════════════════════════════════════
try:
    from backend.seed_extended_curriculum_data import (
        A1_EXTENDED_MODULES, A2_EXTENDED_MODULES,
        B1_EXTENDED_MODULES, B2_EXTENDED_MODULES,
        C1_EXTENDED_MODULES, C2_EXTENDED_MODULES,
        TOEIC_EXTENDED_MODULES, IELTS_EXTENDED_MODULES
    )
    if "A1" in LEVEL_CURRICULUM_DATA:
        LEVEL_CURRICULUM_DATA["A1"]["modules"] = A1_EXTENDED_MODULES
    if "A2" in LEVEL_CURRICULUM_DATA:
        LEVEL_CURRICULUM_DATA["A2"]["modules"] = A2_EXTENDED_MODULES
    if "B1" in LEVEL_CURRICULUM_DATA:
        LEVEL_CURRICULUM_DATA["B1"]["modules"] = B1_EXTENDED_MODULES
    if "B2" in LEVEL_CURRICULUM_DATA:
        LEVEL_CURRICULUM_DATA["B2"]["modules"] = B2_EXTENDED_MODULES
    if "C1" in LEVEL_CURRICULUM_DATA:
        LEVEL_CURRICULUM_DATA["C1"]["modules"] = C1_EXTENDED_MODULES
    if "C2" in LEVEL_CURRICULUM_DATA:
        LEVEL_CURRICULUM_DATA["C2"]["modules"] = C2_EXTENDED_MODULES
    if "TOEIC" in LEVEL_CURRICULUM_DATA:
        LEVEL_CURRICULUM_DATA["TOEIC"]["modules"] = TOEIC_EXTENDED_MODULES
    try:
        from backend.seed_business_tech_full_curriculum import (
            BUSINESS_EXTENDED_MODULES, TECH_EXTENDED_MODULES
        )
        if "BUSINESS" in LEVEL_CURRICULUM_DATA:
            LEVEL_CURRICULUM_DATA["BUSINESS"]["modules"] = BUSINESS_EXTENDED_MODULES
        if "TECH" in LEVEL_CURRICULUM_DATA:
            LEVEL_CURRICULUM_DATA["TECH"]["modules"] = TECH_EXTENDED_MODULES
    except Exception as _e_biz:
        pass
except Exception as _e:
    pass

