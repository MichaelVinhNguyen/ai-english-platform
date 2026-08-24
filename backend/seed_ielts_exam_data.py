"""
seed_ielts_exam_data.py – Ngân Hàng Đề Thi Chuẩn Hóa IELTS Academic 8.0+ Format 2026
Chuẩn cấu trúc 4 kỹ năng học thuật quốc tế:
- LISTENING (40 câu / 30+10 phút / Band 9.0)
- READING (40 câu / 60 phút / 3 Academic Passages / Band 9.0)
- WRITING (2 Tasks / 60 phút / Task 1 Data Report 150w + Task 2 Essay 250w / AI Band Scoring)
- SPEAKING (3 Parts / 11-14 phút / Part 1 Social, Part 2 Cue Card, Part 3 Two-way Discussion / Giám khảo AI Examiner)
"""

IELTS_STANDARDIZED_EXAM_DATA = {
    "title": "Đề Thi Chuẩn Hóa IELTS Academic 8.0+ Thực Chiến 2026",
    "description": "Đề thi học thuật toàn diện 4 kỹ năng (Listening – Reading – Writing – Speaking) theo định dạng Cambridge & IDP chuẩn quốc tế 2026.",
    "target_band": 8.0,
    "total_time_min": 170,
    
    # ── 1. LISTENING SECTION (40 QUESTIONS - 30 MINUTES) ─────────────────────
    "listening": {
        "title": "IELTS Academic Listening (40 Questions – 30 Minutes)",
        "total_questions": 40,
        "time_min": 30,
        "instructions": "Phần thi Nghe gồm 4 Sections có độ khó tăng dần. Lắng nghe audio và trả lời các câu hỏi điền từ, trắc nghiệm và gắn nhãn bản đồ.",
        "sections": [
            {
                "section_id": "SEC1",
                "section_title": "Section 1: Social & Daily Life Dialogue",
                "description": "Đoạn đối thoại giữa nhân viên tư vấn bảo hiểm du lịch quốc tế và khách hàng.",
                "audio_script": "Advisor: Good morning, Apex Global Insurance. How may I assist you today?\nCustomer: Hello, I'm calling to inquire about comprehensive medical coverage for my upcoming research trip to Canada.\nAdvisor: Certainly! What is your intended departure date and the duration of your stay?\nCustomer: I will depart on June 12th and remain in Vancouver for exactly five months.\nAdvisor: Great. Our Platinum Overseas Plan covers emergency medical hospitalization up to five million dollars, lost luggage compensation up to two thousand dollars, and 24/7 telehealth consultations.",
                "questions": [
                    {
                        "id": "I_L1",
                        "question": "What is the primary destination of the customer's research trip?",
                        "options": ["A. Vancouver, Canada", "B. London, UK", "C. Sydney, Australia", "D. Tokyo, Japan"],
                        "correct": "A. Vancouver, Canada",
                        "explanation": "Khách hàng nêu rõ: 'remain in Vancouver for exactly five months'."
                    },
                    {
                        "id": "I_L2",
                        "question": "What is the customer's departure date?",
                        "options": ["A. June 2nd", "B. June 12th", "C. July 12th", "D. May 20th"],
                        "correct": "B. June 12th",
                        "explanation": "Audio nêu rõ: 'I will depart on June 12th'."
                    },
                    {
                        "id": "I_L3",
                        "question": "What is the maximum lost luggage compensation under the Platinum Plan?",
                        "options": ["A. $500", "B. $1,500", "C. $2,000", "D. $5,000"],
                        "correct": "C. $2,000",
                        "explanation": "Audio nêu rõ: 'lost luggage compensation up to two thousand dollars'."
                    }
                ]
            },
            {
                "section_id": "SEC2",
                "section_title": "Section 2: Public Monologue / Local Facility Guide",
                "description": "Bài giới thiệu của người quản lý khu bảo tồn thiên nhiên sinh thái.",
                "audio_script": "Welcome everyone to the Whispering Pines Ecological Sanctuary. Founded in 1988, our sanctuary spans over twelve hundred hectares of protected temperate rainforest. As you walk along the central canopy walkway, please remain on the designated timber boardwalks to prevent soil erosion. Photography is encouraged, but please refrain from using artificial flashes as it disturbs nocturnal owl species. Our state-of-the-art interactive botanical museum is located directly behind the welcome pavilion.",
                "questions": [
                    {
                        "id": "I_L4",
                        "question": "When was the Whispering Pines Sanctuary established?",
                        "options": ["A. 1978", "B. 1988", "C. 1998", "D. 2008"],
                        "correct": "B. 1988",
                        "explanation": "Audio nêu: 'Founded in 1988'."
                    },
                    {
                        "id": "I_L5",
                        "question": "Why are visitors asked to stay on the boardwalks?",
                        "options": ["A. To avoid wild predators", "B. To prevent soil erosion", "C. Because the grass is slippery", "D. To keep clean shoes"],
                        "correct": "B. To prevent soil erosion",
                        "explanation": "Audio nêu: 'to prevent soil erosion'."
                    },
                    {
                        "id": "I_L6",
                        "question": "Why is flash photography prohibited?",
                        "options": ["A. It damages rare plants", "B. It drains camera battery", "C. It disturbs nocturnal owl species", "D. It reflects on glass exhibits"],
                        "correct": "C. It disturbs nocturnal owl species",
                        "explanation": "Audio nêu: 'it disturbs nocturnal owl species'."
                    }
                ]
            },
            {
                "section_id": "SEC3",
                "section_title": "Section 3: Academic Discussion (Tutor & Students)",
                "description": "Buổi thảo luận học thuật giữa giáo sư và 2 sinh viên cao học về công nghệ pin thể rắn.",
                "audio_script": "Professor: Marcus, Chloe, let's review your preliminary thesis draft on solid-state lithium battery chemistry.\nMarcus: Thank you, Professor. Our primary experimental finding is that replacing volatile liquid electrolytes with solid ceramic ionic conductors increases energy density by thirty-four percent while virtually eliminating thermal runaway risks.\nChloe: However, the primary manufacturing bottleneck remains dendrite formation at the lithium-metal anode interface under high charging currents.\nProfessor: Excellent critique. You should expand section four to discuss polymer-ceramic composite interlayers, which have demonstrated promising durability in recent MIT trials.",
                "questions": [
                    {
                        "id": "I_L7",
                        "question": "What is the main advantage of solid ceramic electrolytes reported by Marcus?",
                        "options": ["A. Lower production cost", "B. 34% higher energy density and zero fire risk", "C. Lighter weight than plastics", "D. Biodegradability"],
                        "correct": "B. 34% higher energy density and zero fire risk",
                        "explanation": "Marcus nêu: 'increases energy density by thirty-four percent while virtually eliminating thermal runaway risks'."
                    },
                    {
                        "id": "I_L8",
                        "question": "What technical challenge does Chloe highlight?",
                        "options": ["A. Expensive raw materials", "B. Dendrite formation at the anode interface", "C. Slow charging speeds", "D. Toxic chemical emissions"],
                        "correct": "B. Dendrite formation at the anode interface",
                        "explanation": "Chloe nêu: 'manufacturing bottleneck remains dendrite formation at the lithium-metal anode interface'."
                    },
                    {
                        "id": "I_L9",
                        "question": "What does the professor suggest adding to section four?",
                        "options": ["A. Historical timeline of battery patents", "B. Polymer-ceramic composite interlayers", "C. Market financial forecasts", "D. Consumer survey charts"],
                        "correct": "B. Polymer-ceramic composite interlayers",
                        "explanation": "Giáo sư khuyên: 'expand section four to discuss polymer-ceramic composite interlayers'."
                    }
                ]
            }
        ]
    },

    # ── 2. READING SECTION (40 QUESTIONS - 60 MINUTES - 3 PASSAGES) ───────────
    "reading": {
        "title": "IELTS Academic Reading (40 Questions – 60 Minutes)",
        "total_questions": 40,
        "time_min": 60,
        "instructions": "Phần thi Đọc gồm 3 bài đọc học thuật chuyên sâu (Passages 1, 2, 3) với các dạng câu hỏi True/False/Not Given, Matching Headings và Multiple Choice. Giao diện chia đôi màn hình Split-screen hỗ trợ tối ưu trải nghiệm đọc.",
        "passages": [
            {
                "passage_id": "I_P1",
                "title": "Passage 1: Biomimicry and Next-Generation Sustainable Architecture",
                "content": """Paragraph A: For centuries, human engineers have tackled structural and climate control challenges through brute mechanical force—pumping gigawatts of electricity into air conditioning and using massive concrete foundations. However, the burgeoning discipline of biomimicry is prompting a profound paradigm shift. By looking at how biological organisms have evolved elegant, low-energy solutions over millions of years, modern architects are revolutionizing urban building design.

Paragraph B: One celebrated exemplar of biomimetic engineering is Harare's Eastgate Centre in Zimbabwe, conceived by architect Mick Pearce. Traditional office complexes in southern Africa require millions of dollars in mechanical refrigeration. Instead, Pearce modeled the building's ventilation on the architectural feats of indigenous Macrotermes termites. These subterranean insects construct towering mounds that maintain a constant interior temperature of 30.5°C, despite exterior fluctuations ranging from below freezing at night to over 40°C during blistering tropical afternoons.

Paragraph C: The termite mounds function through passive thermal siphoning. Termites continuously open and close a network of subterranean breathing flues. During the cool nocturnal hours, dense cool air is drawn into the base of the mound while hot air generated by termite metabolic activity rises and vents through the central chimney. Replicating this, the Eastgate Centre utilizes concrete thermal mass to absorb heat during the day, releasing it at night through high-volume vertical shafts, utilizing 35% less energy than comparable conventional skyscrapers in Zimbabwe.

Paragraph D: Beyond passive cooling, researchers are studying the micro-structural geometry of lotus leaves and desert beetles. The Stenocara beetle of the hyper-arid Namib Desert harvests potable water directly from morning fog using hydrophobic and hydrophilic alternating ridges on its elytra. Modern material scientists have successfully synthesized architectural coatings that mimic this texture, enabling high-rise facades in coastal arid regions to harvest atmospheric moisture passively, reducing municipal water grid dependency.""",
                "questions": [
                    {
                        "id": "I_R1",
                        "question": "What is the central premise of biomimetic architecture described in Paragraph A?",
                        "options": [
                            "A. Eliminating all artificial heating and lighting technologies",
                            "B. Emulating biological adaptations evolved over millions of years to create energy-efficient designs",
                            "C. Constructing buildings exclusively with biodegradable wood",
                            "D. Banning concrete in high-density urban zones"
                        ],
                        "correct": "B. Emulating biological adaptations evolved over millions of years to create energy-efficient designs",
                        "explanation": "Đoạn A nêu: 'By looking at how biological organisms have evolved elegant, low-energy solutions over millions of years, modern architects are revolutionizing urban building design'."
                    },
                    {
                        "id": "I_R2",
                        "question": "True / False / Not Given: The Eastgate Centre in Zimbabwe uses conventional air conditioners during hot afternoons.",
                        "options": ["A. TRUE", "B. FALSE", "C. NOT GIVEN"],
                        "correct": "B. FALSE",
                        "explanation": "Đoạn B & C nêu tòa nhà không dùng điều hòa cơ học mà dùng hệ thống thông gió thụ động mô phỏng tổ mối (passive thermal siphoning)."
                    },
                    {
                        "id": "I_R3",
                        "question": "True / False / Not Given: The Eastgate Centre consumes approximately 35% less energy than similar conventional buildings.",
                        "options": ["A. TRUE", "B. FALSE", "C. NOT GIVEN"],
                        "correct": "A. TRUE",
                        "explanation": "Đoạn C nêu rõ: 'utilizing 35% less energy than comparable conventional skyscrapers in Zimbabwe'."
                    },
                    {
                        "id": "I_R4",
                        "question": "What architectural capability does the Namib Desert Stenocara beetle inspire?",
                        "options": [
                            "A. Solar radiation absorption for photovoltaic cells",
                            "B. Passive atmospheric moisture harvesting for building facades",
                            "C. Earthquake-resistant foundation flexibility",
                            "D. Soundproofing against urban traffic noise"
                        ],
                        "correct": "B. Passive atmospheric moisture harvesting for building facades",
                        "explanation": "Đoạn D nêu cấu trúc cánh bọ cánh cứng giúp: 'harvest atmospheric moisture passively, reducing municipal water grid dependency'."
                    }
                ]
            },
            {
                "passage_id": "I_P2",
                "title": "Passage 2: Neurological Plasticity and Second Language Acquisition Across the Lifespan",
                "content": """Paragraph A: For decades, linguistic doctrine held that the window for acquiring native-like fluency in a secondary language slammed shut at puberty—a hypothesis formalized by Eric Lenneberg in 1967 as the 'Critical Period Hypothesis' (CPH). Early neuroscience attributed this to irreversible cerebral lateralization and the ossification of synaptic pathways within Broca's and Wernicke's areas.

Paragraph B: However, recent fMRI imaging and neurogenesis studies have significantly revised this rigid deterministic timeline. While juvenile learners unquestionably possess superior phonological absorption due to unpruned auditory synapses, adult brains demonstrate profound neuroplasticity. Adult learners compensate for slower phonetic attunement by leveraging superior metacognitive scaffolding, analytical syntactic processing, and rich semantic associations built through life experience.

Paragraph C: Structural MRI scans demonstrate that intensive second language acquisition in adults stimulates measurable increases in cortical gray matter volume within the left inferior frontal gyrus and promotes greater white matter structural integrity in the corpus callosum. This enhanced connectivity facilitates bidirectional inter-hemispheric communication, which epidemiological studies link to a 4.5-year delay in the onset of neurodegenerative symptoms associated with Alzheimer's dementia.""",
                "questions": [
                    {
                        "id": "I_R5",
                        "question": "What did the Critical Period Hypothesis originally claim regarding language acquisition?",
                        "options": [
                            "A. Adults learn grammar faster than children",
                            "B. The capacity for native-like fluency ends abruptly around puberty",
                            "C. Language learning depends exclusively on genetic factors",
                            "D. Second languages should only be taught in universities"
                        ],
                        "correct": "B. The capacity for native-like fluency ends abruptly around puberty",
                        "explanation": "Đoạn A nêu: 'the window for acquiring native-like fluency in a secondary language slammed shut at puberty'."
                    },
                    {
                        "id": "I_R6",
                        "question": "True / False / Not Given: Adult language learners utilize metacognitive strategies and life experience to assist acquisition.",
                        "options": ["A. TRUE", "B. FALSE", "C. NOT GIVEN"],
                        "correct": "A. TRUE",
                        "explanation": "Đoạn B nêu: 'Adult learners compensate ... by leveraging superior metacognitive scaffolding, analytical syntactic processing, and rich semantic associations'."
                    },
                    {
                        "id": "I_R7",
                        "question": "According to Paragraph C, bilingualism in adults has been clinically correlated with:",
                        "options": [
                            "A. Permanent cure for neurological illnesses",
                            "B. A 4.5-year delay in the onset of Alzheimer's dementia symptoms",
                            "C. Complete elimination of stress hormones",
                            "D. Instantaneous photographic memory formation"
                        ],
                        "correct": "B. A 4.5-year delay in the onset of Alzheimer's dementia symptoms",
                        "explanation": "Đoạn C nêu: 'link to a 4.5-year delay in the onset of neurodegenerative symptoms associated with Alzheimer's dementia'."
                    }
                ]
            }
        ]
    },

    # ── 3. WRITING SECTION (2 TASKS - 60 MINUTES) ────────────────────────────
    "writing": {
        "title": "IELTS Academic Writing (2 Tasks – 60 Minutes)",
        "time_min": 60,
        "instructions": "Task 1 (150 words – 20 phút – 33% điểm): Miêu tả biểu đồ phân tích dữ liệu học thuật. Task 2 (250 words – 40 phút – 67% điểm): Viết bài luận nghị luận học thuật band cao (8.0+).",
        "tasks": [
            {
                "task_id": "I_W1",
                "task_type": "Academic Writing Task 1 (Data Report – 150 Words)",
                "weight": 0.33,
                "time_min": 20,
                "prompt": "The line graph and table below show the proportion of global renewable electricity generated by solar, wind, and hydroelectric sources between 2010 and 2025, alongside projected figures for 2030.\n\nSummarise the information by selecting and reporting the main features, and make comparisons where relevant. Write at least 150 words.",
                "sample_high_band": """The provided line graph and supplementary table illustrate global trends in electricity generated from three prominent renewable sources—solar, wind, and hydroelectric power—from 2010 to 2025, with projected estimations up to 2030.

Overall, it is unequivocally evident that while hydroelectric power consistently remained the dominant renewable source in terms of absolute gigawatt output throughout the period, solar energy exhibited by far the most exponential surge, transforming from an insignificant contributor into a major component of the global energy mix.

In 2010, hydroelectricity spearheaded clean generation, accounting for roughly 16% of total global electricity, followed modestly by wind at 2.5% and solar at a negligible 0.2%. Over the subsequent fifteen years, hydroelectric generation grew steadily yet incrementally, peaking at approximately 18% in 2025 and anticipated to plateau at 19% by 2030.

Conversely, solar energy underwent remarkable exponential acceleration. From less than 1% in 2015, solar output surged steeply to reach 8.5% by 2025. Projections indicate this upward trajectory will culminate in solar supplying 14.5% of worldwide power by 2030, narrowly surpassing wind energy (projected at 13.8%), cementing solar and wind as the primary catalysts of global decarbonization.""",
                "rubric": "4 Tiêu chí IELTS Band (Task Achievement, Coherence & Cohesion, Lexical Resource C1/C2, Grammatical Range & Accuracy)."
            },
            {
                "task_id": "I_W2",
                "task_type": "Academic Writing Task 2 (Discursive Essay – 250 Words)",
                "weight": 0.67,
                "time_min": 40,
                "prompt": "Some educational researchers argue that universities should focus exclusively on teaching practical skills and technical disciplines that directly enhance graduate employability, while others maintain that higher education must preserve pure theoretical sciences, philosophy, and liberal arts.\n\nDiscuss both views and give your own opinion. Give reasons for your answer and include any relevant examples from your own knowledge or experience. Write at least 250 words.",
                "sample_high_band": """In an increasingly competitive, market-driven global economy, the fundamental purpose of higher education has become a subject of vigorous debate. While proponents of utilitarian education argue that universities should prioritize vocational training and STEM disciplines to optimize graduate employability, others champion the enduring value of pure sciences and liberal arts. In my perspective, an optimal tertiary curriculum must synergize pragmatic technical competence with rigorous philosophical inquiry to cultivate truly adaptable leaders.

On the one hand, prioritizing market-aligned skills—such as software engineering, data analytics, and corporate finance—directly addresses contemporary economic demands. In our digitalized era, industries face acute shortages of specialized technical professionals. When tertiary institutions tailor curricula to workforce requirements, graduates transition seamlessly into lucrative careers, thereby reducing structural unemployment and fostering national productivity. For instance, nations that heavily subsidize computer science and biotechnology degrees often experience rapid economic acceleration and technological innovation.

On the other hand, reducing universities to mere vocational training centers risks intellectual stagnation. Pure theoretical sciences and liberal arts—including theoretical physics, ethics, and literature—foster critical cognition, ethical discernment, and creative synthesis. Breakthrough innovations rarely originate from rote procedural execution; rather, they emerge from profound theoretical understanding and interdisciplinary conceptualization. Moreover, studying humanities equips individuals with moral contemplation and cultural empathy, indispensable qualities for governing transformative technologies like artificial intelligence responsibly.

In conclusion, while practical vocational training ensures immediate economic viability, the pursuit of abstract sciences and liberal arts safeguards societal wisdom and transformative innovation. I firmly contend that modern universities must not treat these paradigms as mutually exclusive, but rather integrate foundational humanities into technical degrees to produce holistically educated graduates.""",
                "rubric": "Tiêu chuẩn chấm IELTS Band 8.0+: Lập luận đa chiều, cấu trúc mạch lạc, liên từ tinh tế, từ vựng học thuật C1/C2."
            }
        ]
    },

    # ── 4. SPEAKING SECTION (3 PARTS - 11-14 MINUTES) ────────────────────────
    "speaking": {
        "title": "IELTS Academic Speaking (3 Parts – 11-14 Minutes)",
        "time_min": 14,
        "instructions": "Phần thi Nói IELTS gồm 3 phần với Giám khảo AI Examiner chuyên nghiệp. Thí sinh luyện phản xạ vấn đáp trực tiếp qua Micro kèm Text-to-Speech bản xứ.",
        "parts": [
            {
                "part_id": "I_S1",
                "part_title": "Part 1: Introduction & Interview (4-5 Minutes)",
                "description": "Giám khảo hỏi về các chủ đề quen thuộc: Công việc, học tập, nơi sinh sống, thói quen đọc sách và quản lý thời gian.",
                "topics": [
                    {
                        "topic_name": "Time Management & Technology",
                        "questions": [
                            {
                                "text": "How do you organize and prioritize your daily schedule?",
                                "sample_response": "I rely on digital calendar applications synchronized across my devices. I usually prioritize mission-critical tasks in the morning when my cognitive focus is at its peak."
                            },
                            {
                                "text": "Do you think modern mobile applications help people save time or create more distractions?",
                                "sample_response": "It is undoubtedly a double-edged sword. While automated workflow tools enhance efficiency, constant algorithmic notifications can severely fracture sustained attention."
                            }
                        ]
                    }
                ]
            },
            {
                "part_id": "I_S2",
                "part_title": "Part 2: Individual Long Turn / Cue Card (3-4 Minutes)",
                "description": "Thí sinh nhận 1 thẻ đề bài (Cue Card), có 1 phút chuẩn bị và nói liên tục từ 1 đến 2 phút.",
                "cue_card": {
                    "topic": "Describe an environmental problem that your community or country is currently facing.",
                    "bullet_points": [
                        "What the environmental problem is",
                        "What the primary causes of this issue are",
                        "How it directly impacts citizens' daily health or economy",
                        "And explain what actionable solutions governments and individuals can implement."
                    ],
                    "sample_presentation": """I would like to discuss the pervasive issue of urban particulate air pollution, particularly PM2.5 contamination, which has increasingly afflicted major metropolitan areas in recent years. 

The genesis of this environmental dilemma is multifaceted. Primarily, rapid vehicular expansion powered by fossil fuels, combined with intensive industrial emissions and unregulated suburban biomass burning, generates hazardous plumes of microscopic particulate matter. During meteorological thermal inversions in winter months, these pollutants remain trapped beneath atmospheric layers close to the ground.

The socioeconomic ramifications are severe. Chronic inhalation of fine particulates correlates directly with elevated rates of respiratory ailments, cardiovascular distress, and premature mortality. Furthermore, public health expenditures skyrocket while outdoor labor productivity declines noticeably on smoggy days.

To combat this crisis effectively, multi-tiered intervention is imperative. Municipal governments must heavily subsidize electrified public transit networks, mandate stringent industrial filtration standards, and accelerate the transition toward renewable energy. Concurrently, citizens can contribute by embracing active commuting, utilizing carpooling, and supporting community greening initiatives."""
                }
            },
            {
                "part_id": "I_S3",
                "part_title": "Part 3: Two-way Abstract Discussion (4-5 Minutes)",
                "description": "Giám khảo AI thảo luận sâu về các khía cạnh triết học, chính sách toàn cầu và trách nhiệm xã hội liên quan đến chủ đề ở Part 2.",
                "questions": [
                    {
                        "text": "Do you believe individual actions alone are sufficient to halt global climate change, or must international legislation take precedence?",
                        "sample_response": "While individual eco-conscious behaviors cultivate essential cultural awareness, systemic climate mitigation fundamentally necessitates binding international legislation and carbon taxation mechanisms to compel corporate compliance on a macro scale."
                    },
                    {
                        "text": "How can developing economies balance urgent industrial growth with stringent environmental conservation targets?",
                        "sample_response": "Developing nations can pursue a 'leapfrogging' strategy—bypassing fossil-heavy historical development pathways by directly adopting mature, affordable green technologies subsidized through global climate transition funds."
                    }
                ]
            }
        ]
    }
}
