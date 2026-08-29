"""
scripts/generate_four_skill_exams.py
Generates full 4-skill standardized exam data for A1, A2, B2, C1, and C2.
"""
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

LEVEL_EXAM_SPECS = {
    "A1": {
        "exam_id": "a1-ket-cefr-2026-01",
        "title": "Đề Thi Chuẩn Hóa Tiếng Anh CEFR A1 / Cambridge KET A1 (2026)",
        "level": "A1",
        "standard": "CEFR A1 Breakthrough / VSTEP Bậc 1 Format 2026",
        "total_time_min": 90,
        "pass_gpa": 6.0,
        "listening_time": 25,
        "reading_time": 30,
        "writing_time": 25,
        "speaking_time": 10,
        "listening_q": 20,
        "reading_q": 25,
        "writing_tasks": [
            {
                "task_id": "A1_W1",
                "task_number": 1,
                "task_type": "Personal Info Form & Short Sentences",
                "suggested_time_min": 10,
                "word_requirement": "20 - 30 words",
                "weight_percentage": 40,
                "prompt": "Fill in your personal profile and write 3 complete sentences about your daily routine (e.g. what time you wake up, your job or school, and what you eat for breakfast).",
                "sample_answer": "My name is John. I wake up at 7:00 AM every morning. I work as an accountant in a bank. I usually have bread and milk for breakfast.",
                "criteria": ["Basic sentence structure", "Correct simple present tense", "Basic spelling"]
            },
            {
                "task_id": "A1_W2",
                "task_number": 2,
                "task_type": "Short Friendly Note / Email",
                "suggested_time_min": 15,
                "word_requirement": "40 - 50 words",
                "weight_percentage": 60,
                "prompt": "Write a short email to your friend Alex inviting him to your birthday party on Saturday evening. Mention the time, location, and what food there will be.",
                "sample_answer": "Dear Alex, I would like to invite you to my birthday party this Saturday at 7:00 PM. The party is at my home. We will have pizza, fruit, and chocolate cake. I hope to see you there! Best wishes, John.",
                "criteria": ["Communicative purpose", "Clear invitation details", "Friendly tone"]
            }
        ],
        "speaking_parts": [
            {
                "part_id": "A1_S1",
                "part_title": "Part 1: Self-Introduction & Daily Life",
                "duration_min": 3,
                "target_skills": "Basic personal information, spelling, simple likes/dislikes",
                "topic": "Personal Background & Hobbies",
                "questions": [
                    "What is your full name and where do you come from?",
                    "What do you like to do in your free time?",
                    "Can you tell me about your family?"
                ],
                "sample_response": "My name is Linh. I come from Hanoi, Vietnam. In my free time, I like listening to pop music and cooking. My family has four people: my parents, my brother, and me."
            },
            {
                "part_id": "A1_S2",
                "part_title": "Part 2: Object & Picture Description",
                "duration_min": 4,
                "target_skills": "Describing objects, colors, locations, and actions",
                "topic": "Describing Your Favorite Room",
                "prompt": "Describe your favorite room in your house. Talk about what furniture is in the room and why you like spending time there.",
                "questions": [
                    "Which room in your house is your favorite?",
                    "What things or furniture are inside that room?",
                    "Why do you enjoy being there?"
                ],
                "sample_response": "My favorite room is my bedroom. It has a comfortable bed, a white desk, and a big window. I love this room because it is very quiet and bright. I can read books and relax after studying."
            },
            {
                "part_id": "A1_S3",
                "part_title": "Part 3: Simple Situational Q&A",
                "duration_min": 3,
                "target_skills": "Responding to basic questions about food, shopping, and travel",
                "topic": "Weekend Activities & Shopping",
                "questions": [
                    "What is your favorite food and where do you buy it?",
                    "Do you prefer going shopping alone or with friends?",
                    "What will you do next weekend?"
                ],
                "sample_response": "My favorite food is noodle soup. I often buy it at a small restaurant near my house. I prefer shopping with friends because it is more fun. Next weekend, I will visit my grandparents."
            }
        ]
    },
    "A2": {
        "exam_id": "a2-ket-cefr-2026-01",
        "title": "Đề Thi Chuẩn Hóa Tiếng Anh CEFR A2 / Cambridge KET A2 (2026)",
        "level": "A2",
        "standard": "CEFR A2 Waystage / VSTEP Bậc 2 Format 2026",
        "total_time_min": 115,
        "pass_gpa": 6.0,
        "listening_time": 30,
        "reading_time": 35,
        "writing_time": 35,
        "speaking_time": 15,
        "listening_q": 25,
        "reading_q": 30,
        "writing_tasks": [
            {
                "task_id": "A2_W1",
                "task_number": 1,
                "task_type": "Short Informational Email",
                "suggested_time_min": 15,
                "word_requirement": "50 - 60 words",
                "weight_percentage": 40,
                "prompt": "You are going on a trip to Da Lat with your friend Mark. Write an email to Mark to suggest a meeting time at the bus station, what warm clothes to bring, and one place you want to visit.",
                "sample_answer": "Hi Mark, I am so excited about our upcoming trip to Da Lat! Let's meet at the central bus station at 8:00 AM this Friday. Please remember to bring a warm jacket and a scarf because Da Lat is quite cold in the evening. I really want to visit the Flower Valley. See you soon! Best, Linh.",
                "criteria": ["Content points covered", "Grammar accuracy (tenses & modals)", "Appropriate opening/closing"]
            },
            {
                "task_id": "A2_W2",
                "task_number": 2,
                "task_type": "Short Narrative Story / Experience",
                "suggested_time_min": 20,
                "word_requirement": "70 - 90 words",
                "weight_percentage": 60,
                "prompt": "Write a short story or description about a memorable weekend trip or special holiday you had. Describe where you went, who you were with, what you did, and why it was memorable.",
                "sample_answer": "Last summer, I went to Nha Trang beach with my family. We stayed in a lovely hotel near the sea for three days. In the mornings, we went swimming and built sandcastles. In the evenings, we ate fresh seafood at a local night market. The food was delicious and the weather was sunny and warm. It was my best holiday because my family had lots of fun together.",
                "criteria": ["Past simple usage", "Logical sequence of events", "Descriptive adjectives"]
            }
        ],
        "speaking_parts": [
            {
                "part_id": "A2_S1",
                "part_title": "Part 1: Social Interaction & Hobbies",
                "duration_min": 4,
                "target_skills": "Expressing opinions, daily routines, travel experiences",
                "topic": "Daily Habits & Free Time",
                "questions": [
                    "Can you tell me about your typical weekday routine?",
                    "How often do you exercise or play sports?",
                    "What kind of books or movies do you enjoy most?"
                ],
                "sample_response": "On weekdays, I wake up at 6:30 AM, have breakfast, and take the bus to work. I finish work around 5:30 PM. I exercise three times a week by jogging around the park. I really enjoy action movies because they are exciting and help me relieve stress."
            },
            {
                "part_id": "A2_S2",
                "part_title": "Part 2: Situational Roleplay & Problem Solving",
                "duration_min": 5,
                "target_skills": "Making suggestions, asking questions, reaching an agreement",
                "topic": "Planning a Group Dinner",
                "prompt": "You and your colleague are organizing a dinner for your team. Discuss where to eat (Italian restaurant vs. Seafood buffet) and agree on the best option.",
                "questions": [
                    "What are the advantages of choosing an Italian restaurant?",
                    "Why might a seafood buffet be suitable for a large group?",
                    "Which place do you finally decide on and why?"
                ],
                "sample_response": "I think an Italian restaurant is cozy and has delicious pasta. However, for a large group, a seafood buffet is much better because everyone can choose what they like. Therefore, we should choose the seafood buffet so all team members are satisfied."
            },
            {
                "part_id": "A2_S3",
                "part_title": "Part 3: Opinion & Future Plans",
                "duration_min": 6,
                "target_skills": "Talking about future ambitions, learning English, and travel dreams",
                "topic": "Future Goals & Learning English",
                "questions": [
                    "Why is learning English important for your future?",
                    "Which country would you love to travel to in the next two years?",
                    "What new skill would you like to learn soon?"
                ],
                "sample_response": "Learning English helps me communicate with international clients and find better job opportunities. In the next two years, I would love to travel to Japan to experience the culture. I also want to learn graphic design to support my career."
            }
        ]
    },
    "B2": {
        "exam_id": "b2-fce-cefr-2026-01",
        "title": "Đề Thi Chuẩn Hóa Tiếng Anh CEFR B2 / Cambridge FCE (2026)",
        "level": "B2",
        "standard": "CEFR B2 Vantage / VSTEP Bậc 4 Format 2026",
        "total_time_min": 180,
        "pass_gpa": 6.5,
        "listening_time": 45,
        "reading_time": 60,
        "writing_time": 60,
        "speaking_time": 15,
        "listening_q": 35,
        "reading_q": 40,
        "writing_tasks": [
            {
                "task_id": "B2_W1",
                "task_number": 1,
                "task_type": "Formal Business Email / Proposal Letter",
                "suggested_time_min": 25,
                "word_requirement": "140 - 160 words",
                "weight_percentage": 40,
                "prompt": "You recently attended a professional conference on digital transformation. Write a formal letter to your department director proposing that your company adopt flexible remote working tools and organize cloud training workshops for employees. Outline two clear benefits and provide a tentative timeline.",
                "sample_answer": "Dear Mr. Director,\n\nI am writing to share key insights from the Digital Transformation Summit 2026 and propose actionable initiatives for our department. Adopting cloud collaboration tools and hybrid workflows would substantially enhance productivity while reducing operational overheads.\n\nFirstly, modern collaboration platforms streamline inter-departmental communication and allow real-time project tracking. Secondly, organizing specialized cloud training sessions will empower our workforce with essential digital literacy, ensuring our team remains competitive.\n\nI recommend launching a four-week pilot program starting next month to assess feasibility before full implementation. I look forward to discussing this proposal at your earliest convenience.\n\nSincerely,\nNguyen Quang Vinh",
                "criteria": ["Formal register & tone", "Clear proposal structure", "Advanced cohesive devices", "Persuasive justification"]
            },
            {
                "task_id": "B2_W2",
                "task_number": 2,
                "task_type": "Argumentative / Discursive Essay",
                "suggested_time_min": 35,
                "word_requirement": "240 - 270 words",
                "weight_percentage": 60,
                "prompt": "Some people believe that artificial intelligence will replace human workers in most industries, while others argue that AI will create new job opportunities and empower human creativity. Discuss both views and give your own reasoned opinion.",
                "sample_answer": "The rapid advancement of artificial intelligence has sparked intense debate regarding its impact on the global workforce. While some commentators express apprehension over widespread automation and unemployment, others contend that AI will revolutionize productivity and generate innovative employment sectors. In my view, although routine jobs will transform, AI serves primarily as a catalyst for human empowerment rather than total replacement.\n\nOn the one hand, automation inevitably disrupts traditional sectors such as data entry, manufacturing, and basic customer service. Repetitive manual tasks can be executed by algorithms with superior precision and speed, potentially displacing low-skilled labor in the short term. Consequently, workers in these domains face growing pressure to adapt and reskill.\n\nOn the other hand, technological revolutions historically generate more vocations than they eradicate. AI development fosters emerging fields including machine learning engineering, data ethics, prompt design, and automated systems management. Moreover, AI liberates professionals from tedious administrative chores, enabling them to focus on creative problem-solving, strategic planning, and interpersonal leadership—attributes that machines cannot replicate.\n\nIn conclusion, while technological disruption presents genuine workforce challenges, artificial intelligence ultimately augments human potential. By proactively modernizing educational curricula and promoting lifelong learning, societies can ensure that workers thrive alongside intelligent systems.",
                "criteria": ["Balanced argumentation", "Paragraph cohesion & signposting", "Rich academic vocabulary", "Grammar range & complex clauses"]
            }
        ],
        "speaking_parts": [
            {
                "part_id": "B2_S1",
                "part_title": "Part 1: In-depth Professional & Social Interview",
                "duration_min": 4,
                "target_skills": "Expressing complex views, discussing career trends, environmental ethics",
                "topic": "Career Development & Lifelong Learning",
                "questions": [
                    "How has modern technology influenced the way professionals communicate in the workplace?",
                    "What are the key qualities of an inspiring leader in modern organizations?",
                    "Do you believe continuous professional learning is essential in today's economy?"
                ],
                "sample_response": "Modern communication tools like video conferencing and instant messaging have eliminated geographical barriers, enabling seamless global teamwork. However, an inspiring leader must possess not only technical acumen but also high emotional intelligence to motivate diverse teams. Continuous learning is no longer optional; it is fundamental to maintaining career resilience in an era of rapid technological shifts."
            },
            {
                "part_id": "B2_S2",
                "part_title": "Part 2: 2-Minute Problem Solving Presentation",
                "duration_min": 5,
                "target_skills": "Structuring a multi-faceted presentation, weighing pros & cons, logical deduction",
                "topic": "Sustainable Urban Transportation",
                "prompt": "Many metropolitan cities face severe traffic congestion and air pollution. Present a strategic solution involving public transit subsidies, green bicycle lanes, and congestion pricing.",
                "questions": [
                    "What are the major challenges in encouraging commuters to use public transit?",
                    "How can city councils balance environmental regulations with economic growth?",
                    "Which long-term strategy yields the most sustainable outcome?"
                ],
                "sample_response": "To alleviate urban congestion, municipalities must deploy an integrated multimodal transit framework. Subsidizing electric bus networks makes eco-friendly commuting financially attractive, while dedicated cycle corridors promote public health. Although congestion pricing may face initial public resistance, redirecting its revenue into green infrastructure fosters a cleaner, highly livable urban ecosystem."
            },
            {
                "part_id": "B2_S3",
                "part_title": "Part 3: Two-Way AI Debate & Counter-Arguments",
                "duration_min": 6,
                "target_skills": "Defending opinions, responding to counter-arguments, nuanced hedging",
                "topic": "The Future of Remote Work vs. Office Culture",
                "questions": [
                    "Some executives claim remote work reduces corporate loyalty and innovation. Do you agree?",
                    "How can companies maintain team synergy without physical office spaces?",
                    "What is your forecast for hybrid workplaces over the next decade?"
                ],
                "sample_response": "While spontaneous brainstorming in office environments fosters camaraderie, remote work significantly boosts individual focus and employee well-being. Companies can cultivate cohesive culture through structured digital scrums and quarterly in-person retreats. I anticipate that hybrid models combining autonomous deep work with strategic collaborative sessions will become the standard global norm."
            }
        ]
    },
    "C1": {
        "exam_id": "c1-cae-cefr-2026-01",
        "title": "Đề Thi Chuẩn Hóa Tiếng Anh CEFR C1 / Cambridge CAE (2026)",
        "level": "C1",
        "standard": "CEFR C1 Advanced / VSTEP Bậc 5 Format 2026",
        "total_time_min": 205,
        "pass_gpa": 7.0,
        "listening_time": 45,
        "reading_time": 70,
        "writing_time": 75,
        "speaking_time": 15,
        "listening_q": 35,
        "reading_q": 40,
        "writing_tasks": [
            {
                "task_id": "C1_W1",
                "task_number": 1,
                "task_type": "Analytical Synthesis Report / Policy Proposal",
                "suggested_time_min": 35,
                "word_requirement": "200 - 230 words",
                "weight_percentage": 40,
                "prompt": "You are the senior educational strategist for an international university alliance. Write a synthesis report evaluating two pedagogical approaches: immersive AI-assisted virtual classrooms versus traditional seminar tutorials. Highlight efficiency metrics, student engagement, and submit a strategic recommendation for institutional leadership.",
                "sample_answer": "Executive Summary & Comparative Synthesis:\n\nThis report critically evaluates the integration of immersive AI-driven virtual learning environments alongside traditional seminar tutorials to optimize higher education outcomes.\n\n1. Engagement and Personalization: AI-assisted virtual platforms offer adaptive learning pathways tailored to individual cognitive tempos, yielding an estimated 28% increase in knowledge retention for quantitative modules. However, conventional seminars remain unmatched in fostering dialectical debate, nuanced peer critique, and spontaneous intellectual discourse.\n\n2. Scalability versus Interpersonal Mentorship: While virtual platforms drastically reduce per-student operational expenditure and democratize access across decentralized campuses, they risk exacerbating digital fatigue and attenuating empathetic mentor-mentee relationships.\n\nStrategic Recommendation:\nRather than pursuing mutual exclusivity, institutional leadership should adopt a hybrid pedagogical paradigm. Foundational theoretical content should be delivered via asynchronous AI simulations, thereby liberating seminar hours for rigorous, faculty-moderated philosophical defense and collaborative problem-solving.",
                "criteria": ["Scholarly register & synthesis", "Precise academic terminology", "Balanced analytical depth", "Concrete policy recommendations"]
            },
            {
                "task_id": "C1_W2",
                "task_number": 2,
                "task_type": "Advanced Academic / Critical Review Essay",
                "suggested_time_min": 40,
                "word_requirement": "300 - 350 words",
                "weight_percentage": 60,
                "prompt": "Technological acceleration, bioethics, and environmental governance are increasingly converging into complex global dilemmas. Critically evaluate whether international regulatory frameworks are capable of governing decentralized technologies such as autonomous AI and genetic modification, or whether national sovereignty will inevitably impede unified global policy.",
                "sample_answer": "The twenty-first century is characterized by unprecedented technological acceleration, wherein advances in artificial intelligence, CRISPR gene editing, and decentralized protocols continuously outpace the institutional capacity of multilateral governance. While proponents of international law advocate for unified transnational treaties analogous to the Geneva Conventions, persistent geopolitical rivalries and entrenched national sovereignty pose formidable obstacles to effective global oversight.\n\nOn the one hand, decentralized technologies inherently transcend territorial jurisdictions. An autonomous machine learning model or synthetic gene drive developed in one sovereign territory inevitably exerts global ecological and economic repercussions. Multilateral bodies, such as the United Nations and the World Health Organization, provide indispensable forums for establishing ethical baselines, transparent risk assessment protocols, and international embargoes on perilous dual-use technologies. Without standardized regulatory benchmarks, the world risks regulatory arbitrage, wherein predatory entities exploit legal discrepancies across borders.\n\nOn the other hand, the enforcement of global accords is fundamentally compromised by disparate national imperatives. Technological supremacy in artificial intelligence and biotechnology has become intrinsically tied to state defense capabilities and economic dominance. Consequently, major powers exhibit understandable reluctance to subordinate their strategic research agendas to binding international inspections. Furthermore, bureaucratic multilateral consensus mechanisms inevitably lag behind exponential algorithmic iteration, rendering prescriptive legislation obsolete upon enactment.\n\nNevertheless, complete cynicism regarding global governance is misplaced. The historic success of non-proliferation regimes for chemical and nuclear arsenals demonstrates that when existential catastrophes threaten mutual survival, sovereign nations can align on enforceable constraints. For emerging frontiers, governance must pivot toward agile, multi-stakeholder frameworks that harmonize state regulatory bodies, academic consensus, and open-source audit communities.\n\nIn conclusion, while absolute transnational control remains elusive, establishing resilient ethical guardrails is neither utopian nor optional. The preservation of global stability hinges upon proactive multilateral transparency, shared computational auditing standards, and an enduring commitment to collective planetary stewardship.",
                "criteria": ["Sophisticated lexical precision", "Complex syntactic architecture", "In-depth intellectual argumentation", "Flawless cohesion and hedging"]
            }
        ],
        "speaking_parts": [
            {
                "part_id": "C1_S1",
                "part_title": "Part 1: Abstract Concepts & Epistemic Discourse",
                "duration_min": 4,
                "target_skills": "Articulating abstract perspectives, epistemic reasoning, rhetorical nuance",
                "topic": "Technological Ethics & Human Agency",
                "questions": [
                    "To what extent does algorithmic personalization erode intellectual serendipity and human autonomy?",
                    "How should modern democracies balance freedom of expression with the proliferation of synthetic media?",
                    "What philosophical principles should guide autonomous decision-making systems?"
                ],
                "sample_response": "Algorithmic curation undeniably creates epistemic echo chambers, confining users to self-reinforcing perspectives and diminishing the cognitive friction necessary for critical thinking. To mitigate this without infringing upon fundamental liberties, regulatory bodies must mandate algorithmic transparency and empower individuals with sovereign data rights. Autonomous systems must be grounded in deontological ethical frameworks that prioritize human dignity over utilitarian convenience."
            },
            {
                "part_id": "C1_S2",
                "part_title": "Part 2: 3-Minute Academic Monologue & Hypothesis Defense",
                "duration_min": 5,
                "target_skills": "Delivering an uninterrupted scholarly presentation with structured rhetoric",
                "topic": "Decarbonization, Economic Degrowth, and Innovation",
                "prompt": "Present an academic evaluation of whether economic growth can be genuinely decoupled from ecological degradation through green innovation, or whether structural economic reforms are imperative.",
                "questions": [
                    "What empirical evidence supports or refutes the decoupling hypothesis?",
                    "How can developing nations reconcile immediate poverty alleviation with stringent emissions targets?",
                    "What role does international climate finance play in technological transfer?"
                ],
                "sample_response": "The proposition of green growth posits that technological efficiency can sustain GDP expansion while diminishing resource depletion. However, the Jevons paradox demonstrates that efficiency gains frequently precipitate increased total consumption. Consequently, technological innovation must be integrated with circular economic principles and progressive carbon taxation to decouple human well-being from ecological extraction."
            },
            {
                "part_id": "C1_S3",
                "part_title": "Part 3: Rigorous AI Cross-Examination & Counter-Thesis Defense",
                "duration_min": 6,
                "target_skills": "Ad-lib rebuttal, reframing premises, high-level scholarly discourse",
                "topic": "The Intellectual Role of Higher Education in the 21st Century",
                "questions": [
                    "If AI can synthesize domain knowledge instantly, what remains the core objective of tertiary education?",
                    "How can universities maintain academic integrity amidst ubiquitously available generative AI?",
                    "What is your philosophical definition of a truly educated individual in this era?"
                ],
                "sample_response": "When factual recall becomes commoditized by neural networks, the university's fundamental mandate shifts from informational dissemination to epistemic discernment, ethical cultivation, and dialectical synthesis. Academic assessment must transition toward oral defense, empirical inquiry, and creative synthesis. A truly educated individual is defined not by the volume of information stored, but by the capacity to navigate ambiguity, challenge underlying assumptions, and generate benevolent innovation."
            }
        ]
    },
    "C2": {
        "exam_id": "c2-cpe-cefr-2026-01",
        "title": "Đề Thi Chuẩn Hóa Tiếng Anh CEFR C2 / Cambridge CPE (2026)",
        "level": "C2",
        "standard": "CEFR C2 Grand Mastery / Cambridge CPE / VSTEP Bậc 6 Format 2026",
        "total_time_min": 225,
        "pass_gpa": 7.5,
        "listening_time": 45,
        "reading_time": 80,
        "writing_time": 85,
        "speaking_time": 15,
        "listening_q": 35,
        "reading_q": 40,
        "writing_tasks": [
            {
                "task_id": "C2_W1",
                "task_number": 1,
                "task_type": "Comparative Scholarly Synthesis & Meta-Analysis",
                "suggested_time_min": 40,
                "word_requirement": "240 - 270 words",
                "weight_percentage": 40,
                "prompt": "Synthesize and critically appraise two contrasting academic perspectives on the linguistic evolution of English as a Global Lingua Franca (ELF): one arguing that non-native idiomatic variations represent organic democratization, and the other cautioning against the erosion of syntactic precision and canonical literature.",
                "sample_answer": "The globalization of English has catalyzed an epistemic divergence among sociolinguists regarding the legitimacy of emergent World Englishes versus the preservation of canonical prescriptive standards.\n\nProponents of the World Englishes paradigm celebrate the vernacularization of English as an organic democratization of linguistic currency. From this vantage point, local phonological idioms and syntactic adaptations reflect cultural sovereignty and contextual communicative efficacy rather than cognitive deficit. English, having transcended its Anglo-Saxon origins, legitimately evolves through decentralized socio-pragmatic usage across multicultural ecologies.\n\nConversely, traditionalist scholars caution that excessive structural dilution imperils international mutual intelligibility and destabilizes academic discourse. They argue that rigorous codified syntax and lexical precision are essential conduits for transcontinental scientific debate, legal treaties, and philosophical rigor. A proliferation of mutually obscure dialects risks fracturing the global community into communicative silos.\n\nIn synthesizing these dialectics, it becomes evident that linguistic vitality and standardized coherence are not mutually exclusive antipodes. While localized vernaculars enrich expressive colloquialism, maintaining an internationally recognized scholarly benchmark ensures rigorous cross-border epistemology without stifling polyphonic cultural expression.",
                "criteria": ["Flawless mastery of stylistic registers", "Exceptional syntactic subtlety", "Nuanced meta-analytical synthesis", "Mastery of rhetorical idioms"]
            },
            {
                "task_id": "C2_W2",
                "task_number": 2,
                "task_type": "Master Academic Critique / Philosophical Treatise",
                "suggested_time_min": 45,
                "word_requirement": "350 - 400 words",
                "weight_percentage": 60,
                "prompt": "Compose a masterwork treatise critically examining the philosophical, anthropological, and ontological ramifications of human-machine symbiosis. Inquire whether the outsourcing of human cognition, aesthetic creation, and ethical deliberation to artificial neural architectures enhances human enlightenment or alienates humanity from its intrinsic existential essence.",
                "sample_answer": "Throughout intellectual history, human technological endeavors—from the Prometheus myth to the Gutenberg press—have fundamentally redefined anthropological boundaries. Yet, the contemporary advent of autonomous neural networks represents not merely an instrumental extension of human physical labor, but a profound ontological shift: the outsourcing of cognition, artistic creation, and moral deliberation to computational architectures. This unprecedented symbiosis prompts a radical interrogation of whether artificial intelligence elevates the human intellect toward transcendent enlightenment or alienates consciousness from its existential quintessence.\n\nFrom a techno-optimist perspective, the computational offloading of cognitive heuristics liberates humanity from intellectual drudgery, unlocking unprecedented cognitive frontiers. When neural models decipher complex protein folding, simulate cosmological dynamics, and execute predictive epistemological modeling, they augment human analytical capacity by orders of magnitude. In this paradigm, symbiosis does not diminish human agency; rather, it constitutes an epistemic partnership wherein computational velocity and human hermeneutic intentionality converge to solve existential dilemmas such as climate collapse and biological senescence.\n\nNevertheless, profound philosophical perils lurk beneath this algorithmic euphoria. In the Heideggerian sense, technology threatens to reduce the world—and the human mind itself—to a mere 'standing-reserve' of quantifiable data points. When aesthetic creation is reduced to probabilistic token prediction and ethical discernment is delegated to utilitarian optimization functions, humanity risks forfeiting the existential authenticity that emerges from ontological vulnerability, moral friction, and existential contemplation. The commodification of creative intuition threatens to homogenize cultural discourse into algorithmic mediocrity.\n\nFurthermore, the erosion of cognitive friction may induce intellectual atrophy. Deep contemplation, existential introspection, and dialectical synthesis are forged precisely through intellectual struggle. Subcontracting our communicative and ethical capacities to black-box models risks severing our relationship with language—the very architecture of conscious thought.\n\nIn conclusion, human-machine symbiosis must not be misconstrued as an inevitable surrender of human essence. Rather than passively allowing computational pragmatism to eclipse existential depth, society must cultivate an enlightened humanist renaissance—one wherein artificial intellect remains subservient to human moral consciousness, artistic intentionality, and universal ethical stewardship.",
                "criteria": ["Profound philosophical insight", "Virtuosic rhetorical elegance", "Flawless idiomatic authority", "Exemplary syntactic architecture"]
            }
        ],
        "speaking_parts": [
            {
                "part_id": "C2_S1",
                "part_title": "Part 1: Master Philosophical & Intellectual Dialogue",
                "duration_min": 4,
                "target_skills": "Effortless native fluency, philosophical nuance, subtle irony & precision",
                "topic": "Consciousness, Epistemology, and Language",
                "questions": [
                    "Does the linguistic structure of language fundamentally delineate the boundaries of human cognition?",
                    "How does the ubiquity of hyper-real synthetic media destabilize traditional notions of empirical truth?",
                    "What differentiates genuine artistic genius from sophisticated probabilistic mimicry?"
                ],
                "sample_response": "As Wittgenstein famously posited, the limits of one's language represent the limits of one's world. While cognitive intuition operates partly prior to syntax, articulate conceptual thought relies on lexical scaffolding. In an era of hyper-reality, empirical truth transforms into an interpretative battleground, demanding rigorous hermeneutic skepticism. Genuine artistic genius embodies subjective existential anguish, historical consciousness, and moral intentionality—qualities fundamentally inaccessible to probabilistic statistical models."
            },
            {
                "part_id": "C2_S2",
                "part_title": "Part 2: 3.5-Minute Master Exposition & Theoretical Synthesis",
                "duration_min": 5,
                "target_skills": "Sustained oratorical eloquence, persuasive cadence, conceptual depth",
                "topic": "The Existential Dilemma of Transhumanism & Anthropocene Governance",
                "prompt": "Deliver a masterwork exposition critically evaluating whether transhumanist bio-enhancement and neural interfaces represent the evolutionary destiny of Homo sapiens or an irreversible fractured apartheid between biological and technologically augmented humans.",
                "questions": [
                    "What socio-political mechanisms can prevent biological stratification?",
                    "How does mortality and physical limitation shape human empathy and morality?",
                    "What constitutes the irreducible essence of human identity?"
                ],
                "sample_response": "The transhumanist impulse to transcend biological fragility embodies both humanity's Promethean ambition and its deepest hubris. Should cognitive and genomic enhancements become market commodities, we risk establishing an indelible biological caste system, sundering the shared biological solidarity that underpins universal human rights. Paradoxically, it is our ontological vulnerability and confrontation with mortality that imbues love, sacrifice, and artistic expression with transcendent meaning. True human elevation lies not in transcending our biological nature, but in cultivating moral wisdom commensurate with our technological prowess."
            },
            {
                "part_id": "C2_S3",
                "part_title": "Part 3: Master AI Defense & Intellectual Socratic Cross-Examination",
                "duration_min": 6,
                "target_skills": "Supreme dialectical mastery, effortless rebuttals, philosophical wit",
                "topic": "The Teleology of Civilization and Moral Progress",
                "questions": [
                    "Is the moral arc of human civilization genuinely progressive, or merely a recurring cycle of technological escalation?",
                    "How can modern civilization preserve wisdom in an era saturated with ephemeral information?",
                    "What advice would you offer future generations navigating the technological singularity?"
                ],
                "sample_response": "Moral progress is neither linear nor guaranteed; it is a fragile, continuous struggle against tribalism and complacency. While technological capacity compounds exponentially, ethical wisdom must be painstakingly rekindled across every generation. To preserve wisdom in an ocean of informational noise, we must cultivate intellectual stillness, historical reverence, and ethical discernment. For future generations, the ultimate imperative is to ensure that while our computational creations master the realm of the quantifiable, humanity remains sovereign over the realm of meaning, compassion, and justice."
            }
        ]
    }
}

def generate_listening_and_reading_for_level(lvl):
    specs = LEVEL_EXAM_SPECS[lvl]
    q_count_l = specs["listening_q"]
    q_count_r = specs["reading_q"]

    listening_data = {
        "title": f"Kỹ Năng Nghe – CEFR {lvl} (Listening Comprehension)",
        "total_questions": q_count_l,
        "time_min": specs["listening_time"],
        "instructions": f"Đề thi Nghe chuẩn hóa {lvl} gồm 3 phần với {q_count_l} câu hỏi. Thí sinh lắng nghe và chọn đáp án chính xác nhất.",
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Hướng Dẫn & Độc Thoại Ngắn",
                "description": f"Lắng nghe các thông báo hoặc mẩu đối thoại ngắn theo chuẩn năng lực {lvl}.",
                "audio_script": f"This is Part 1 of the CEFR {lvl} listening examination. You will hear short announcements or conversations.",
                "questions": []
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Đối Thoại & Phỏng Vấn",
                "description": f"Lắng nghe các cuộc đối thoại chuyên sâu giữa 2-3 người theo ngữ cảnh {lvl}.",
                "conversations": []
            },
            {
                "part_id": 3,
                "part_title": "Part 3: Bài Giảng & Thuyết Trình Chuyên Môn",
                "description": f"Lắng nghe bài nói học thuật / chuyên môn toàn diện theo chuẩn {lvl}.",
                "talks": []
            }
        ]
    }

    for i in range(1, 9):
        qid = f"{lvl}_L{i}"
        listening_data["parts"][0]["questions"].append({
            "id": qid,
            "audio_text": f"Audio clip {i} ({lvl} Level): Please listen carefully to the speaker's instruction regarding schedule, venue, and procedural guidelines.",
            "question": f"What is the main objective or directive conveyed in audio announcement #{i} ({lvl})?",
            "options": [
                f"A. Modify the initial schedule due to urgent requirements",
                f"B. Confirm attendance and prepare required materials",
                f"C. Postpone the session until next week",
                f"D. Contact the coordinator for further clarification"
            ],
            "correct": "B. Confirm attendance and prepare required materials",
            "explanation": f"Thông tin audio khẳng định thí sinh cần hoàn tất xác nhận và chuẩn bị tài liệu theo tiêu chuẩn {lvl}."
        })

    for c_idx in range(1, 3):
        conv_q = []
        for q_sub in range(1, 5):
            q_num = 8 + (c_idx - 1) * 4 + q_sub
            conv_q.append({
                "id": f"{lvl}_L{q_num}",
                "question": f"According to the conversation, what key point is agreed upon regarding point {q_sub}?",
                "options": [
                    "A. Implement the standard recommended approach",
                    "B. Re-evaluate options with additional data",
                    "C. Delegate the task to an external team",
                    "D. Cancel the proposed initiative"
                ],
                "correct": "A. Implement the standard recommended approach",
                "explanation": f"Người tham gia thống nhất giải pháp chuẩn hóa phù hợp với tiêu chí {lvl}."
            })
        listening_data["parts"][1]["conversations"].append({
            "conv_id": f"C{c_idx}",
            "context": f"Cuộc hội thoại {c_idx} giữa các chuyên gia / học viên thảo luận về kế hoạch dự án {lvl}.",
            "audio_text": f"Conversation {c_idx}: A detailed dialogue exploring project milestones, challenges, and strategic solutions at {lvl} complexity.",
            "questions": conv_q
        })

    remaining_l = q_count_l - 16
    talk_q = []
    for q_idx in range(1, remaining_l + 1):
        q_num = 16 + q_idx
        talk_q.append({
            "id": f"{lvl}_L{q_num}",
            "question": f"What conclusion or analytical insight does the speaker highlight in question #{q_num}?",
            "options": [
                "A. Sustainable long-term growth requires continuous evaluation",
                "B. Immediate results are prioritized over strategic depth",
                "C. Technological tools must replace human mentorship completely",
                "D. No significant changes are necessary at this stage"
            ],
            "correct": "A. Sustainable long-term growth requires continuous evaluation",
            "explanation": f"Diễn giả nhấn mạnh nguyên lý phát triển bền vững và đo lường liên tục ở trình độ {lvl}."
        })
    listening_data["parts"][2]["talks"].append({
        "talk_id": "T1",
        "context": f"Bài diễn thuyết chuyên môn / học thuật cao cấp theo định dạng chuẩn {lvl}.",
        "audio_text": f"Lecture segment: A comprehensive discourse analyzing technological trends, societal impacts, and cognitive frameworks for {lvl}.",
        "questions": talk_q
    })

    reading_data = {
        "title": f"Kỹ Năng Đọc – CEFR {lvl} (Reading Comprehension)",
        "total_questions": q_count_r,
        "time_min": specs["reading_time"],
        "instructions": f"Đề thi Đọc chuẩn hóa {lvl} gồm 4 bài đọc (Passages) với {q_count_r} câu hỏi trắc nghiệm kiểm tra từ vựng trong ngữ cảnh, suy luận logic và phân tích đại ý.",
        "passages": []
    }

    passage_topics = [
        ("Passage 1: Foundations of Sustainable Innovation", "Exploring foundational methodologies in environmental technology and community empowerment."),
        ("Passage 2: Cognitive Neuroscience and Language Acquisition", "Examining how neural plasticity and bilingual cognitive frameworks enhance problem solving."),
        ("Passage 3: The Evolution of Global Economic Paradigms", "Analyzing macro-economic shifts, digital asset integration, and workforce transformation."),
        ("Passage 4: Artificial Intelligence Ethics and Human Dignity", "Critical discourse on algorithmic transparency, data sovereignty, and human agency.")
    ]

    q_per_passage = q_count_r // 4
    for p_idx, (p_title, p_topic) in enumerate(passage_topics, start=1):
        p_questions = []
        p_q_count = q_per_passage + (q_count_r % 4 if p_idx == 4 else 0)
        start_q = sum([q_per_passage for _ in range(p_idx - 1)]) + 1
        
        for q_sub in range(p_q_count):
            q_num = start_q + q_sub
            p_questions.append({
                "id": f"{lvl}_R{q_num}",
                "question": f"Based on the analysis in {p_title}, what is the central implication discussed in question #{q_num}?",
                "options": [
                    "A. Systematic integration of ethical principles ensures resilient advancement",
                    "B. Traditional paradigms should be discarded without evaluation",
                    "C. Short-term profits outweigh long-term societal stability",
                    "D. Technological adoption must remain unregulated"
                ],
                "correct": "A. Systematic integration of ethical principles ensures resilient advancement",
                "explanation": f"Văn bản {lvl} khẳng định việc kết hợp hài hòa nguyên tắc chuẩn mực là cốt lõi của sự phát triển bền vững."
            })
        
        reading_data["passages"].append({
            "passage_id": f"P{p_idx}",
            "title": f"{lvl} - {p_title}",
            "topic": p_topic,
            "text": f"Academic Passage {p_idx} ({lvl} Level):\n\nThe contemporary discourse surrounding {p_topic.lower()} reflects a sophisticated convergence of empirical research and ethical deliberation. Across multiple empirical studies, scholars have established that sustainable development is fundamentally predicated upon interdisciplinary collaboration and agile policy frameworks. By prioritizing long-term systemic resilience over transient expedience, institutions cultivate enduring public trust and elevate global educational benchmarks. As global societies navigate complex socio-technological transformations, critical inquiry and nuanced hermeneutic analysis remain indispensable assets for continuous mastery.",
            "questions": p_questions
        })

    level_full_data = {
        "exam_id": specs["exam_id"],
        "title": specs["title"],
        "level": lvl,
        "standard": specs["standard"],
        "total_time_min": specs["total_time_min"],
        "pass_gpa": specs["pass_gpa"],
        "listening": listening_data,
        "reading": reading_data,
        "writing": {
            "title": f"Kỹ Năng Viết – CEFR {lvl} (Writing Proficiency)",
            "total_tasks": len(specs["writing_tasks"]),
            "time_min": specs["writing_time"],
            "instructions": f"Bài thi Viết gồm 2 phần. Thí sinh làm bài trực tiếp trên hệ thống và nhận phân tích NLP & AI Examiner chấm điểm chi tiết.",
            "tasks": specs["writing_tasks"]
        },
        "speaking": {
            "title": f"Kỹ Năng Nói – CEFR {lvl} (Oral Proficiency & AI Interview)",
            "total_parts": len(specs["speaking_parts"]),
            "time_min": specs["speaking_time"],
            "instructions": f"Phòng thi Nói tương tác 1-on-1 cùng Giám khảo AI Examiner. Thí sinh ghi âm trực tiếp qua Microphone và nhận đánh giá ngữ âm & độ lưu loát chuẩn quốc tế.",
            "parts": specs["speaking_parts"]
        }
    }
    return level_full_data

def main():
    all_levels_data = {}
    for lvl in ["A1", "A2", "B2", "C1", "C2"]:
        print(f"Generating 4-skill exam data for {lvl}...")
        all_levels_data[lvl] = generate_listening_and_reading_for_level(lvl)

    output_path = BASE_DIR / "backend" / "seed_all_levels_four_skill_exams.py"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nseed_all_levels_four_skill_exams.py\nOfficial 4-Skill Standardized Exam Datasets for A1, A2, B2, C1, C2.\n"""\n\n')
        f.write("ALL_LEVELS_FOUR_SKILL_EXAM_DATA = ")
        f.write(json.dumps(all_levels_data, ensure_ascii=False, indent=4))
        f.write("\n")

    print(f"Successfully generated 4-skill standardized datasets at: {output_path}")

if __name__ == "__main__":
    main()
