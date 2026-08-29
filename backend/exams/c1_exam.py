# -*- coding: utf-8 -*-
"""
backend/exams/c1_exam.py – Ngân Hàng Đề Thi Chuẩn Hóa CEFR C1 / Cambridge CAE / VSTEP Bậc 5
Format Khảo Thí Thực Tế:
1. Kỹ Năng Nghe (Listening): 35 câu hỏi – 40 phút (Part 1: 8 câu, Part 2: 12 câu, Part 3: 15 câu)
2. Kỹ Năng Đọc (Reading): 40 câu hỏi – 60 phút (4 Passages x 10 câu)
3. Kỹ Năng Viết (Writing): 2 Tasks – 60 phút (Task 1: Executive Proposal 220-250 từ, Task 2: Analytical Essay 300-350 từ)
4. Kỹ Năng Nói (Speaking): 3 Parts – 15 phút (Part 1: In-depth Interview, Part 2: Strategic Solution, Part 3: Scholarly Debate)
"""

C1_STANDARDIZED_EXAM_DATA = {
    "exam_id": "c1-cae-vstep-cefr-2026-01",
    "title": "Đề Thi Chuẩn Hóa Tiếng Anh CEFR C1 / Cambridge CAE / VSTEP Bậc 5 Thực Chiến 2026",
    "level": "C1",
    "standard": "CEFR C1 Advanced / VSTEP Bậc 5 Format 2026",
    "total_time_min": 175,
    "pass_gpa": 6.5,

    # ══════════════════════════════════════════════════════════════════════════
    # 1. KỸ NĂNG NGHE (LISTENING) – 35 CÂU HỎI – 40 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "listening": {
        "title": "Kỹ Năng Nghe – CEFR C1 (Advanced Listening Comprehension)",
        "total_questions": 35,
        "time_min": 40,
        "instructions": "Đề thi Nghe C1 gồm 3 phần với 35 câu hỏi trắc nghiệm học thuật chuyên sâu. Lắng nghe và chọn đáp án chính xác nhất.",
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Đàm Thoại & Trích Đoạn Chuyên Sâu Có Sắc Thái Hàm Ẩn (8 câu)",
                "description": "Nghe 8 mẩu đàm thoại ngắn chứa đựng các sắc thái cảm xúc, thái độ tinh tế và hàm ý học thuật.",
                "audio_script": "This is Part 1 of the CEFR C1 Listening Examination. You will hear eight short extracts. Choose the best answer from A, B, C, or D.",
                "questions": [
                    {
                        "id": "C1_L1",
                        "audio_text": "Economist: While central bankers celebrate the statistical dip in headline inflation, looking beneath the surface reveals that core services inflation remains stubbornly entrenched, largely propelled by persistent wage pressures in specialized sectors.",
                        "question": "What is the economist's nuanced assessment of current inflation trends?",
                        "options": [
                            "A. Inflation has been permanently eradicated across all sectors",
                            "B. Headline improvements mask resilient core inflation driven by specialized wage demands",
                            "C. Central banks should immediately cut interest rates to zero",
                            "D. Consumer spending on goods has completely collapsed"
                        ],
                        "correct": "B. Headline improvements mask resilient core inflation driven by specialized wage demands",
                        "explanation": "Chuyên gia kinh tế nhấn mạnh rằng việc giảm lạm phát tổng thể (headline inflation) đang che giấu lạm phát lõi (core inflation) vẫn dai dẳng do áp lực tiền lương."
                    },
                    {
                        "id": "C1_L2",
                        "audio_text": "Literary critic: The novelist's latest narrative doesn't merely chronicle historical tragedy; rather, it interrogates how collective memory is retrospectively sanitized to serve contemporary political mythologies.",
                        "question": "What is the primary artistic accomplishment of the novel according to the critic?",
                        "options": [
                            "A. Providing an entertaining romantic comedy",
                            "B. Critically examining how historical memory is sanitized for current political narratives",
                            "C. Accurately reciting chronological census data",
                            "D. Glorifying military conquests of the past"
                        ],
                        "correct": "B. Critically examining how historical memory is sanitized for current political narratives",
                        "explanation": "Nhà phê bình nhấn mạnh tác phẩm chất vấn cách ký ức tập thể bị gọt giũa để phục vụ huyền thoại chính trị đương đại."
                    },
                    {
                        "id": "C1_L3",
                        "audio_text": "Neuroscientist: It is a pervasive misconception that memory operates like a digital recording device. In truth, every recollection is an active biochemical reconstruction, vulnerable to contextual distortion and subtle cognitive retroactive interference.",
                        "question": "What fundamental biological reality about human memory is highlighted?",
                        "options": [
                            "A. Memories are immutable digital files stored in the cortex",
                            "B. Every recall is an active biochemical reconstruction susceptible to distortion",
                            "C. Brain damage never impairs factual memory",
                            "D. Human memory capacity decreases after age ten"
                        ],
                        "correct": "B. Every recall is an active biochemical reconstruction susceptible to distortion",
                        "explanation": "Nhà khoa học thần kinh khẳng định mỗi lần nhớ lại là một quá trình tái cấu trúc sinh hóa dễ bị sai lệch."
                    },
                    {
                        "id": "C1_L4",
                        "audio_text": "Urban theorist: Rather than treating gentrification as an inexorable market force, progressive municipalities must mandate inclusionary zoning quotas to prevent the catastrophic cultural disenfranchisement of long-standing working-class communities.",
                        "question": "What policy recommendation does the urban theorist advocate?",
                        "options": [
                            "A. Allowing private developers unregulated freedom",
                            "B. Mandating inclusionary zoning quotas to protect historic working-class residents",
                            "C. Demolishing all historical suburban neighborhoods",
                            "D. Eliminating public municipal housing completely"
                        ],
                        "correct": "B. Mandating inclusionary zoning quotas to protect historic working-class residents",
                        "explanation": "Audio: 'mandate inclusionary zoning quotas to prevent the catastrophic cultural disenfranchisement of long-standing working-class communities'."
                    },
                    {
                        "id": "C1_L5",
                        "audio_text": "Venture capitalist: In early-stage deep-tech investment, the intellectual brilliance of the proprietary algorithm is secondary to the founding team's operational resilience and adaptive capacity when initial commercial hypotheses fail.",
                        "question": "What factor does the investor value most in deep-tech startups?",
                        "options": [
                            "A. The sheer complexity of the patent alone",
                            "B. The founding team's operational resilience and adaptability under failure",
                            "C. Immediate quarterly revenue generation",
                            "D. The size of the marketing advertising budget"
                        ],
                        "correct": "B. The founding team's operational resilience and adaptability under failure",
                        "explanation": "Audio: 'proprietary algorithm is secondary to the founding team's operational resilience and adaptive capacity'."
                    },
                    {
                        "id": "C1_L6",
                        "audio_text": "Philosopher: The ethical dilemma of autonomous lethal weaponry is not merely technical reliability, but whether algorithmic systems can ever possess the moral agency required to evaluate human intent and proportionality in warfare.",
                        "question": "What is the core ethical concern regarding autonomous weapons systems?",
                        "options": [
                            "A. Their high manufacturing cost",
                            "B. Whether algorithms can possess moral agency to assess intent and proportionality",
                            "C. The battery life of military drones",
                            "D. The speed of wireless satellite communication"
                        ],
                        "correct": "B. Whether algorithms can possess moral agency to assess intent and proportionality",
                        "explanation": "Audio: 'whether algorithmic systems can ever possess the moral agency required to evaluate human intent and proportionality'."
                    },
                    {
                        "id": "C1_L7",
                        "audio_text": "Environmental lawyer: The precedent set by the appellate court ruling fundamentally shifts the burden of proof, requiring industrial chemical manufacturers to affirmatively demonstrate non-toxicity prior to market distribution.",
                        "question": "How did the recent court ruling alter regulatory standards?",
                        "options": [
                            "A. It abolished all environmental compliance inspections",
                            "B. It requires manufacturers to prove non-toxicity before releasing products",
                            "C. It transfers chemical testing costs entirely to taxpayers",
                            "D. It legalized industrial waste dumping in international waters"
                        ],
                        "correct": "B. It requires manufacturers to prove non-toxicity before releasing products",
                        "explanation": "Audio: 'requiring industrial chemical manufacturers to affirmatively demonstrate non-toxicity prior to market distribution'."
                    },
                    {
                        "id": "C1_L8",
                        "audio_text": "Linguist: The emergence of internet slang and multimodal emoji communication does not signify linguistic degradation; rather, it reflects an ingenious compensatory mechanism to restore paralinguistic tone in asynchronous digital text.",
                        "question": "How does the linguist characterize digital slang and emojis?",
                        "options": [
                            "A. As definitive proof of intellectual decline",
                            "B. As an ingenious compensatory mechanism to restore emotional tone in digital writing",
                            "C. As a temporary fad that will disappear",
                            "D. As a barrier to cross-cultural communication"
                        ],
                        "correct": "B. As an ingenious compensatory mechanism to restore emotional tone in digital writing",
                        "explanation": "Nhà ngôn ngữ học khẳng định đó là cơ chế bù trừ thông minh để tái tạo ngữ điệu và cảm xúc trong văn bản số."
                    }
                ]
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Thảo Luận Hội Nghị Bàn Tròn & Tranh Biện Học Thuật (12 câu)",
                "description": "Nghe 3 cuộc hội đàm bàn tròn (mỗi cuộc 4 câu) về Tái cấu trúc Chuỗi cung ứng, Quản trị AI và Đạo đức Sinh học.",
                "audio_script": "This is Part 2. You will hear three strategic panel discussions. Choose the best answer for each question.",
                "conversations": [
                    {
                        "conv_id": "c1-conv-1",
                        "context": "Hội thoại 1 (Câu 9 - 12): Tọa đàm về Tái cấu trúc Chuỗi cung ứng Bán dẫn Toàn cầu.",
                        "audio_text": "Dr. Sterling: The geopolitical vulnerabilities exposed during recent supply chain bottlenecks demonstrate that extreme geographical concentration in advanced semiconductor fabrication is economically untenable.\nProfessor Tanaka: I concur, Dr. Sterling. However, attempting complete autarky through domestic onshoring entails staggering capital expenditures, estimated at over $150 billion per fabrication hub, while risking domestic technological stagnation.\nDr. Sterling: That is why strategic 'friend-shoring' within allied multilateral frameworks offers a more pragmatic equilibrium. By diversifying critical lithography and wafer packaging across trusted jurisdictions, nations preserve competitive innovation while mitigating single-point geopolitical failure.\nProfessor Tanaka: Provided that standardized intellectual property protections and coordinated subsidy guardrails are mutually enforced, that multilateral approach minimizes trade distortion.",
                        "questions": [
                            {
                                "id": "C1_L9",
                                "question": "What fundamental flaw in current semiconductor manufacturing is highlighted by Dr. Sterling?",
                                "options": [
                                    "A. Shortage of raw silicon in nature",
                                    "B. Extreme geographical concentration of advanced fabrication facilities",
                                    "C. Lack of skilled electrical engineers globally",
                                    "D. Excessive consumer demand for older generation chips"
                                ],
                                "correct": "B. Extreme geographical concentration of advanced fabrication facilities",
                                "explanation": "Dr. Sterling: 'extreme geographical concentration in advanced semiconductor fabrication is economically untenable'."
                            },
                            {
                                "id": "C1_L10",
                                "question": "What major risk associated with complete domestic onshoring does Professor Tanaka identify?",
                                "options": [
                                    "A. Lower transport costs",
                                    "B. Staggering capital costs ($150B+) and potential technological stagnation",
                                    "C. Immediate shortage of software coders",
                                    "D. Banning semiconductor exports completely"
                                ],
                                "correct": "B. Staggering capital costs ($150B+) and potential technological stagnation",
                                "explanation": "Tanaka: 'staggering capital expenditures, estimated at over $150 billion... while risking domestic technological stagnation'."
                            },
                            {
                                "id": "C1_L11",
                                "question": "What strategic compromise does Dr. Sterling advocate?",
                                "options": [
                                    "A. Full nationalization of all chip factories",
                                    "B. 'Friend-shoring' and diversification across allied multilateral jurisdictions",
                                    "C. Complete deregulation of international tech monopolies",
                                    "D. Halting all future research in semiconductor lithography"
                                ],
                                "correct": "B. 'Friend-shoring' and diversification across allied multilateral jurisdictions",
                                "explanation": "Dr. Sterling: 'strategic friend-shoring within allied multilateral frameworks offers a more pragmatic equilibrium'."
                            },
                            {
                                "id": "C1_L12",
                                "question": "Under what condition does Professor Tanaka believe friend-shoring will succeed?",
                                "options": [
                                    "A. If governments eliminate all corporate taxes",
                                    "B. If IP protections and coordinated subsidy guardrails are mutually enforced",
                                    "C. If consumers stop purchasing smartphones",
                                    "D. If one single corporation controls all patents"
                                ],
                                "correct": "B. If IP protections and coordinated subsidy guardrails are mutually enforced",
                                "explanation": "Tanaka: 'Provided that standardized intellectual property protections and coordinated subsidy guardrails are mutually enforced'."
                            }
                        ]
                    },
                    {
                        "conv_id": "c1-conv-2",
                        "context": "Hội thoại 2 (Câu 13 - 16): Tranh luận về Đạo đức và Quản trị Trí tuệ Nhân tạo Đa phương tiện.",
                        "audio_text": "Dr. Al-Mansoor: As multimodal foundation models approach superhuman benchmarks in synthetic media generation, watermarking and cryptographic provenance verification must become mandatory legal requisites for all commercial model providers.\nClara Brooks: While cryptographic provenance is indispensable, technical watermarks can be easily scrubbed through open-source compression or adversarial post-processing filters. Relying exclusively on technological barriers creates a false sense of security.\nDr. Al-Mansoor: What complementary regulatory mechanisms do you propose, Clara?\nClara Brooks: We require strict legal liability frameworks holding developers civilly and criminally accountable for malicious misuse when safety guardrails are demonstrably circumvented, coupled with mandatory pre-deployment red-teaming audits conducted by independent supervisory bodies.",
                        "questions": [
                            {
                                "id": "C1_L13",
                                "question": "What technical mandate does Dr. Al-Mansoor propose for commercial AI providers?",
                                "options": [
                                    "A. Banning all commercial AI models permanently",
                                    "B. Mandatory cryptographic provenance verification and watermarking",
                                    "C. Making all source code open-source without restriction",
                                    "D. Imposing a 90% tax on AI companies"
                                ],
                                "correct": "B. Mandatory cryptographic provenance verification and watermarking",
                                "explanation": "Dr. Al-Mansoor: 'watermarking and cryptographic provenance verification must become mandatory legal requisites'."
                            },
                            {
                                "id": "C1_L14",
                                "question": "Why does Clara Brooks argue that watermarks alone are insufficient?",
                                "options": [
                                    "A. Because watermarks cost too much money to compute",
                                    "B. Because they can be easily scrubbed via compression or adversarial post-processing",
                                    "C. Because no cameras support digital watermarks",
                                    "D. Because users prefer watermarked content"
                                ],
                                "correct": "B. Because they can be easily scrubbed via compression or adversarial post-processing",
                                "explanation": "Clara: 'technical watermarks can be easily scrubbed through open-source compression or adversarial post-processing filters'."
                            },
                            {
                                "id": "C1_L15",
                                "question": "What legal liability framework does Clara Brooks recommend?",
                                "options": [
                                    "A. Total immunity for software developers",
                                    "B. Holding developers civilly and criminally accountable when safety guardrails are bypassed",
                                    "C. Making consumers solely responsible for all AI output",
                                    "D. Delegating all legal disputes to automated AI judges"
                                ],
                                "correct": "B. Holding developers civilly and criminally accountable when safety guardrails are bypassed",
                                "explanation": "Clara: 'strict legal liability frameworks holding developers civilly and criminally accountable for malicious misuse'."
                            },
                            {
                                "id": "C1_L16",
                                "question": "Who should conduct the pre-deployment red-teaming audits according to Clara?",
                                "options": [
                                    "A. Company marketing departments",
                                    "B. Independent supervisory bodies",
                                    "C. Random internet users",
                                    "D. Foreign competitors"
                                ],
                                "correct": "B. Independent supervisory bodies",
                                "explanation": "Clara: 'mandatory pre-deployment red-teaming audits conducted by independent supervisory bodies'."
                            }
                        ]
                    },
                    {
                        "conv_id": "c1-conv-3",
                        "context": "Hội thoại 3 (Câu 17 - 20): Bàn tròn về Đạo đức Sinh học và Công nghệ Chỉnh sửa Gen CRISPR.",
                        "audio_text": "Professor Dupont: The distinction between somatic cell gene editing—which treats devastating hereditary disorders in living patients without affecting their progeny—and germline editing is the fundamental red line in biomedical ethics.\nDr. Chen: Indeed, modifying the human germline creates heritable genetic alterations that reverberate down generations, risking irreversible eugenic stratification and unintended off-target genomic mutations.\nProfessor Dupont: Precisely. That is why international scientific academies must establish an enforceable global moratorium on germline clinical applications until comprehensive longitudinal safety data and universal ethical consensus are established.\nDr. Chen: We must ensure this regulatory vigilance does not inadvertently stifle therapeutic somatic gene therapies currently curing sickle cell anemia and congenital blindness.",
                        "questions": [
                            {
                                "id": "C1_L17",
                                "question": "What is the critical distinction between somatic and germline gene editing?",
                                "options": [
                                    "A. Somatic editing only works on animals, while germline works on plants",
                                    "B. Somatic editing treats living patients without affecting progeny, while germline creates heritable changes",
                                    "C. Somatic editing is illegal worldwide, while germline is mandatory",
                                    "D. There is no biological difference between the two"
                                ],
                                "correct": "B. Somatic editing treats living patients without affecting progeny, while germline creates heritable changes",
                                "explanation": "Dupont nêu rõ: somatic điều trị bệnh nhân mà không ảnh hưởng đời sau, còn germline làm thay đổi di truyền qua các thế hệ."
                            },
                            {
                                "id": "C1_L18",
                                "question": "What long-term societal risk of germline modification does Dr. Chen warn against?",
                                "options": [
                                    "A. Lower costs of pharmaceutical drugs",
                                    "B. Irreversible eugenic stratification and unintended off-target mutations",
                                    "C. Immediate global population collapse",
                                    "D. Shortage of hospital beds"
                                ],
                                "correct": "B. Irreversible eugenic stratification and unintended off-target mutations",
                                "explanation": "Dr. Chen: 'risking irreversible eugenic stratification and unintended off-target genomic mutations'."
                            },
                            {
                                "id": "C1_L19",
                                "question": "What international action does Professor Dupont advocate for germline applications?",
                                "options": [
                                    "A. An immediate commercial rollout in all clinics",
                                    "B. An enforceable global moratorium until longitudinal safety and ethical consensus are reached",
                                    "C. Eliminating all scientific peer review",
                                    "D. Banning all biological research entirely"
                                ],
                                "correct": "B. An enforceable global moratorium until longitudinal safety and ethical consensus are reached",
                                "explanation": "Dupont: 'enforceable global moratorium on germline clinical applications until comprehensive longitudinal safety data... are established'."
                            },
                            {
                                "id": "C1_L20",
                                "question": "What therapeutic applications does Dr. Chen emphasize must be protected and continued?",
                                "options": [
                                    "A. Cosmetic genetic alterations for height",
                                    "B. Life-saving somatic therapies curing sickle cell anemia and blindness",
                                    "C. Genetic enhancements for athletic competitions",
                                    "D. Cloning human organs without regulation"
                                ],
                                "correct": "B. Life-saving somatic therapies curing sickle cell anemia and blindness",
                                "explanation": "Dr. Chen: 'therapeutic somatic gene therapies currently curing sickle cell anemia and congenital blindness'."
                            }
                        ]
                    }
                ]
            },
            {
                "part_id": 3,
                "part_title": "Part 3: Bài Giảng Chuyên Khảo Học Thuật Đỉnh Cao (15 câu)",
                "description": "Nghe 3 bài giảng chuyên sâu (mỗi bài 5 câu) về Khoa học thần kinh, Kinh tế học vĩ mô và Triết học đạo đức học thuật.",
                "audio_script": "This is Part 3. You will hear three advanced academic lectures. Choose the best answer for each question.",
                "talks": [
                    {
                        "talk_id": "c1-talk-1",
                        "context": "Bài giảng 1 (Câu 21 - 25): Khoa Học Thần Kinh Nhận Thức và Sự Củng Cố Ký Ức Trong Giấc Ngủ.",
                        "audio_text": "Distinguished colleagues, today's lecture elucidates the neurobiological mechanisms underpinning systems-level memory consolidation. During wakefulness, the hippocampus acts as a rapid, transient buffer, encoding episodic experiences through synaptic long-term potentiation. However, the long-term stabilization of these memory traces into the neocortex occurs predominantly during non-rapid eye movement (NREM) slow-wave sleep. High-amplitude cortical slow oscillations, thalamocortical sleep spindles, and hippocampal sharp-wave ripples synchronize in a precise tripartite temporal hierarchy. This coordinated neuro-oscillatory dialogue drives the active replay of waking neural patterns, systematically transferring declarative information to neocortical distributed networks while purging redundant synaptic connections via homeostatic synaptic scaling.",
                        "questions": [
                            {
                                "id": "C1_L21",
                                "question": "What is the primary role of the hippocampus during wakefulness according to the lecture?",
                                "options": [
                                    "A. Storing permanent memories for a lifetime",
                                    "B. Acting as a rapid, transient buffer encoding episodic experiences",
                                    "C. Regulating involuntary respiratory cycles",
                                    "D. Filtering optical light entering the retina"
                                ],
                                "correct": "B. Acting as a rapid, transient buffer encoding episodic experiences",
                                "explanation": "Bài giảng: 'hippocampus acts as a rapid, transient buffer, encoding episodic experiences through synaptic long-term potentiation'."
                            },
                            {
                                "id": "C1_L22",
                                "question": "During which sleep stage does systems-level memory consolidation predominantly occur?",
                                "options": ["A. REM dreaming sleep", "B. NREM slow-wave sleep", "C. Light transitional stage 1 sleep", "D. Awake meditation"],
                                "correct": "B. NREM slow-wave sleep",
                                "explanation": "Bài giảng: 'occurs predominantly during non-rapid eye movement (NREM) slow-wave sleep'."
                            },
                            {
                                "id": "C1_L23",
                                "question": "Which three neuro-oscillations synchronize in a precise temporal hierarchy during memory transfer?",
                                "options": [
                                    "A. Alpha waves, beta waves, and gamma spikes",
                                    "B. Cortical slow oscillations, thalamocortical sleep spindles, and hippocampal sharp-wave ripples",
                                    "C. Delta rhythms, heartbeats, and muscle twitches",
                                    "D. Optical pulses, auditory tones, and tactile vibrations"
                                ],
                                "correct": "B. Cortical slow oscillations, thalamocortical sleep spindles, and hippocampal sharp-wave ripples",
                                "explanation": "Bài giảng: 'High-amplitude cortical slow oscillations, thalamocortical sleep spindles, and hippocampal sharp-wave ripples synchronize in a precise tripartite temporal hierarchy'."
                            },
                            {
                                "id": "C1_L24",
                                "question": "Where is declarative information permanently transferred and integrated?",
                                "options": ["A. The spinal cord", "B. Neocortical distributed networks", "C. The optic nerve", "D. The cerebellar motor lobe exclusively"],
                                "correct": "B. Neocortical distributed networks",
                                "explanation": "Bài giảng: 'systematically transferring declarative information to neocortical distributed networks'."
                            },
                            {
                                "id": "C1_L25",
                                "question": "What mechanism purges redundant synaptic connections during sleep?",
                                "options": ["A. Homeostatic synaptic scaling", "B. Chemical toxic shock", "C. Complete oxygen deprivation", "D. Electrical seizure discharge"],
                                "correct": "A. Homeostatic synaptic scaling",
                                "explanation": "Bài giảng: 'purging redundant synaptic connections via homeostatic synaptic scaling'."
                            }
                        ]
                    },
                    {
                        "talk_id": "c1-talk-2",
                        "context": "Bài giảng 2 (Câu 26 - 30): Động Lực Học Kinh Tế Vĩ Mô và Bẫy Thanh Khoản.",
                        "audio_text": "In post-Keynesian macroeconomic theory, a 'liquidity trap' represents a severe monetary pathology wherein nominal interest rates approach the zero-lower bound, rendering conventional expansionary monetary policy entirely impotent. When public economic agents anticipate protracted deflation or systemic economic stagnation, aggregate demand becomes completely inelastic to interest rate adjustments. Individuals and corporate balance sheets hoard liquid capital in risk-free assets rather than engaging in productive capital investment or consumption. Under these pathological conditions, monetary quantitative easing merely inflates speculative asset bubbles. Escaping a liquidity trap demands massive, targeted countercyclical fiscal expansion—such as direct infrastructure investment and progressive wealth redistribution—to directly restore aggregate demand and catalyze private investment.",
                        "questions": [
                            {
                                "id": "C1_L26",
                                "question": "What defines a macroeconomic 'liquidity trap'?",
                                "options": [
                                    "A. Hyperinflation where money loses all value overnight",
                                    "B. Nominal interest rates near zero making conventional monetary easing impotent",
                                    "C. Total shutdown of foreign currency exchanges",
                                    "D. Rapid economic growth exceeding 15% annually"
                                ],
                                "correct": "B. Nominal interest rates near zero making conventional monetary easing impotent",
                                "explanation": "Bài giảng: 'nominal interest rates approach the zero-lower bound, rendering conventional expansionary monetary policy entirely impotent'."
                            },
                            {
                                "id": "C1_L27",
                                "question": "How do economic agents behave when they anticipate deflation in a liquidity trap?",
                                "options": [
                                    "A. They immediately spend all their money on luxury goods",
                                    "B. They hoard liquid capital in risk-free assets rather than investing or consuming",
                                    "C. They borrow maximum debt to build new factories",
                                    "D. They convert all wealth into physical real estate"
                                ],
                                "correct": "B. They hoard liquid capital in risk-free assets rather than investing or consuming",
                                "explanation": "Bài giảng: 'hoard liquid capital in risk-free assets rather than engaging in productive capital investment or consumption'."
                            },
                            {
                                "id": "C1_L28",
                                "question": "What unintended consequence often results from quantitative easing during a liquidity trap?",
                                "options": [
                                    "A. Widespread poverty reduction",
                                    "B. Inflation of speculative asset bubbles without stimulating real economic growth",
                                    "C. Permanent closure of stock markets",
                                    "D. Complete elimination of all taxes"
                                ],
                                "correct": "B. Inflation of speculative asset bubbles without stimulating real economic growth",
                                "explanation": "Bài giảng: 'monetary quantitative easing merely inflates speculative asset bubbles'."
                            },
                            {
                                "id": "C1_L29",
                                "question": "What primary fiscal policy is recommended to escape a liquidity trap?",
                                "options": [
                                    "A. Strict government austerity and spending cuts",
                                    "B. Massive targeted countercyclical fiscal expansion and direct infrastructure investment",
                                    "C. Banning all commercial banking",
                                    "D. Pegging the national currency to gold"
                                ],
                                "correct": "B. Massive targeted countercyclical fiscal expansion and direct infrastructure investment",
                                "explanation": "Bài giảng: 'demands massive, targeted countercyclical fiscal expansion—such as direct infrastructure investment'."
                            },
                            {
                                "id": "C1_L30",
                                "question": "Why is aggregate demand inelastic to interest rate cuts in this scenario?",
                                "options": [
                                    "A. Because borrowing costs are already near zero and pessimistic sentiment dominates",
                                    "B. Because banks refuse to accept customer deposits",
                                    "C. Because physical banknotes are illegal",
                                    "D. Because of international trade embargoes"
                                ],
                                "correct": "A. Because borrowing costs are already near zero and pessimistic sentiment dominates",
                                "explanation": "Bài giảng nêu rõ lãi suất đã chạm đáy danh nghĩa 0% nên việc hạ thêm không kích thích được tổng cầu."
                            }
                        ]
                    },
                    {
                        "talk_id": "c1-talk-3",
                        "context": "Bài giảng 3 (Câu 31 - 35): Triết Học Đạo Đức Khai Sáng và Thuyết Nghĩa Vụ Deontology.",
                        "audio_text": "Immanuel Kant's deontological moral framework, articulated in the 'Groundwork of the Metaphysics of Morals', posits that the moral worth of an action resides exclusively in the intrinsic duty of the rational agent, entirely divorced from consequential outcomes. This stands in stark opposition to consequentialist utilitarianism, which gauges ethical rectitude by the net aggregation of happiness. Central to Kantian ethics is the 'Categorical Imperative', particularly the Formula of Humanity: 'Act in such a way that you treat humanity, whether in your own person or in the person of any other, never merely as a means to an end, but always at the same time as an end.' In contemporary bioethics and technological governance, this deontological maxim provides an unshakeable foundation for informed consent, human dignity, and the prohibition of treating human subjects as mere utilitarian instruments.",
                        "questions": [
                            {
                                "id": "C1_L31",
                                "question": "Where does the moral worth of an action reside in Kant's deontological framework?",
                                "options": [
                                    "A. In the popularity of the outcome on social media",
                                    "B. Exclusively in the intrinsic duty of the rational agent, regardless of consequences",
                                    "C. In the financial wealth generated by the act",
                                    "D. In the physical pleasure experienced by the majority"
                                ],
                                "correct": "B. Exclusively in the intrinsic duty of the rational agent, regardless of consequences",
                                "explanation": "Bài giảng: 'moral worth of an action resides exclusively in the intrinsic duty of the rational agent, entirely divorced from consequential outcomes'."
                            },
                            {
                                "id": "C1_L32",
                                "question": "How does Kantian deontology fundamentally differ from consequentialist utilitarianism?",
                                "options": [
                                    "A. Deontology focuses on duty and intrinsic rightness, while utilitarianism evaluates net outcomes and happiness",
                                    "B. Utilitarianism only applies to mathematics",
                                    "C. Deontology rejects all forms of human logic",
                                    "D. There is no philosophical difference"
                                ],
                                "correct": "A. Deontology focuses on duty and intrinsic rightness, while utilitarianism evaluates net outcomes and happiness",
                                "explanation": "Bài giảng phân biệt: Deontology dựa trên bổn phận nội tại, còn Utilitarianism đánh giá dựa trên hệ quả tổng hạnh phúc."
                            },
                            {
                                "id": "C1_L33",
                                "question": "What is the core principle of Kant's 'Formula of Humanity'?",
                                "options": [
                                    "A. Humans must obey all government decrees without question",
                                    "B. Treat humanity never merely as a means to an end, but always as an end in itself",
                                    "C. The end always justifies any means necessary",
                                    "D. Survival of the fittest is the supreme moral law"
                                ],
                                "correct": "B. Treat humanity never merely as a means to an end, but always as an end in itself",
                                "explanation": "Bài giảng trích dẫn: 'never merely as a means to an end, but always at the same time as an end'."
                            },
                            {
                                "id": "C1_L34",
                                "question": "What foundational legal and bioethical concept is directly derived from the Formula of Humanity?",
                                "options": [
                                    "A. Eminent domain seizure of property",
                                    "B. Informed patient consent and inalienable human dignity",
                                    "C. Mandatory organ harvesting without permission",
                                    "D. Pre-emptive criminal imprisonment"
                                ],
                                "correct": "B. Informed patient consent and inalienable human dignity",
                                "explanation": "Bài giảng: 'unshakeable foundation for informed consent, human dignity, and the prohibition of treating human subjects as mere utilitarian instruments'."
                            },
                            {
                                "id": "C1_L35",
                                "question": "What treatise by Immanuel Kant is cited as the source of this deontological framework?",
                                "options": [
                                    "A. The Republic",
                                    "B. Groundwork of the Metaphysics of Morals",
                                    "C. Leviathan",
                                    "D. Das Kapital"
                                ],
                                "correct": "B. Groundwork of the Metaphysics of Morals",
                                "explanation": "Bài giảng nêu tên tác phẩm: 'Groundwork of the Metaphysics of Morals'."
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
        "title": "Kỹ Năng Đọc – CEFR C1 (Advanced Reading Comprehension)",
        "total_questions": 40,
        "time_min": 60,
        "instructions": "Đề thi Đọc C1 gồm 4 bài đọc học thuật chuyên sâu (mỗi bài 10 câu hỏi) về Khoa học thần kinh, Chuỗi cung ứng toàn cầu, Đạo đức AI và Ngôn ngữ học xã hội.",
        "passages": [
            {
                "passage_id": "c1-p1",
                "title": "Passage 1: Cognitive Neuroscience and the Molecular Foundations of Memory",
                "topic": "Neuroscience & Memory Consolidation",
                "content": "For over a century, neuroscientists grappled with the elusive physical substrate of human memory—the theoretical entity historically designated as the 'engram'. Recent breakthroughs in optogenetics, molecular fluorescence microscopy, and high-throughput single-cell RNA sequencing have finally demystified this biological enigma, revealing that memories do not reside in isolated anatomical structures, but are dynamically encoded across distributed ensembles of synchronized neurons.\n\nThe genesis of an engram begins during sensory encoding via synaptic plasticity. When a novel experience stimulates a neural circuit, high-frequency action potentials trigger calcium influx through N-methyl-D-aspartate (NMDA) receptor channels in postsynaptic dendritic spines. This intracellular signaling cascade activates calmodulin-dependent protein kinase II (CaMKII), orchestrating the rapid insertion of additional alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid (AMPA) receptors into the postsynaptic membrane. Consequently, the synaptic connection between the co-activated neurons is biochemically strengthened—a foundational electrophysiological process termed Long-Term Potentiation (LTP).\n\nHowever, the permanence of an engram requires de novo protein synthesis and structural gene transcription driven by the transcription factor CREB (cAMP response element-binding protein). During systemic consolidation in NREM slow-wave sleep, hippocampal sharp-wave ripples reactivate these newly forged engram ensembles in a condensed time-scale dialogue with the medial prefrontal cortex. Over weeks and months, the synaptic weight shifts from temporary hippocampal indexing circuits to permanent neocortical distributed networks. Concurrently, epigenetic modifications, including DNA methylation and histone acetylation, act as biochemical locks, shielding consolidated synaptic architecture against metabolic degradation while preserving behavioral adaptability.",
                "questions": [
                    {
                        "id": "C1_R1",
                        "question": "What historical theoretical concept is now understood through modern optogenetics and RNA sequencing?",
                        "options": [
                            "A. The Cartesian pineal gland soul receptor",
                            "B. The 'engram'—the distributed physical substrate of memory",
                            "C. The phrenological skull measurement map",
                            "D. The genetic code of blood cells"
                        ],
                        "correct": "B. The 'engram'—the distributed physical substrate of memory",
                        "explanation": "Đoạn 1 nêu: 'the physical substrate of human memory—the theoretical entity historically designated as the engram'."
                    },
                    {
                        "id": "C1_R2",
                        "question": "Where are memories physically encoded according to modern neurobiology?",
                        "options": [
                            "A. In an isolated single brain cell",
                            "B. Across distributed ensembles of synchronized neurons",
                            "C. Exclusively within the spinal cord fluid",
                            "D. Inside the auditory canal"
                        ],
                        "correct": "B. Across distributed ensembles of synchronized neurons",
                        "explanation": "Đoạn 1: 'dynamically encoded across distributed ensembles of synchronized neurons'."
                    },
                    {
                        "id": "C1_R3",
                        "question": "What molecular event initiates Long-Term Potentiation (LTP) at postsynaptic dendritic spines?",
                        "options": [
                            "A. Complete depletion of intracellular potassium",
                            "B. Calcium influx through NMDA receptor channels activating CaMKII",
                            "C. Immediate breakdown of all cellular membranes",
                            "D. Chemical freezing of synaptic junctions"
                        ],
                        "correct": "B. Calcium influx through NMDA receptor channels activating CaMKII",
                        "explanation": "Đoạn 2: 'trigger calcium influx through N-methyl-D-aspartate (NMDA) receptor channels... activates calmodulin-dependent protein kinase II (CaMKII)'."
                    },
                    {
                        "id": "C1_R4",
                        "question": "What structural alteration strengthens the synaptic connection during LTP?",
                        "options": [
                            "A. Destruction of dendrites",
                            "B. Insertion of additional AMPA receptors into the postsynaptic membrane",
                            "C. Replacement of neurons with glial cells",
                            "D. Elimination of all neurotransmitters"
                        ],
                        "correct": "B. Insertion of additional AMPA receptors into the postsynaptic membrane",
                        "explanation": "Đoạn 2: 'orchestrating the rapid insertion of additional AMPA receptors into the postsynaptic membrane'."
                    },
                    {
                        "id": "C1_R5",
                        "question": "Which transcription factor is critical for driving de novo protein synthesis for long-term memory?",
                        "options": ["A. Insulin-B", "B. CREB (cAMP response element-binding protein)", "C. Hemoglobin-X", "D. Melatonin-3"],
                        "correct": "B. CREB (cAMP response element-binding protein)",
                        "explanation": "Đoạn 3: 'driven by the transcription factor CREB (cAMP response element-binding protein)'."
                    },
                    {
                        "id": "C1_R6",
                        "question": "How do hippocampal sharp-wave ripples contribute to memory consolidation during NREM sleep?",
                        "options": [
                            "A. By erasing all waking experiences permanently",
                            "B. By reactivating engram ensembles in a dialogue with the medial prefrontal cortex",
                            "C. By blocking oxygen flow to the neocortex",
                            "D. By causing muscular paralysis exclusively"
                        ],
                        "correct": "B. By reactivating engram ensembles in a dialogue with the medial prefrontal cortex",
                        "explanation": "Đoạn 3: 'hippocampal sharp-wave ripples reactivate these newly forged engram ensembles in a condensed time-scale dialogue with the medial prefrontal cortex'."
                    },
                    {
                        "id": "C1_R7",
                        "question": "What anatomical shift in synaptic weight occurs over weeks and months of consolidation?",
                        "options": [
                            "A. From the frontal cortex down to the spinal nerves",
                            "B. From temporary hippocampal indexing circuits to permanent neocortical distributed networks",
                            "C. From the left hemisphere completely to the right ear",
                            "D. From brain tissue into peripheral muscle memory"
                        ],
                        "correct": "B. From temporary hippocampal indexing circuits to permanent neocortical distributed networks",
                        "explanation": "Đoạn 3: 'synaptic weight shifts from temporary hippocampal indexing circuits to permanent neocortical distributed networks'."
                    },
                    {
                        "id": "C1_R8",
                        "question": "What role do epigenetic modifications (DNA methylation, histone acetylation) play in memory?",
                        "options": [
                            "A. They act as biochemical locks shielding consolidated synaptic architecture from degradation",
                            "B. They cause rapid cognitive dementia",
                            "C. They convert memories into sound waves",
                            "D. They prevent any new learning from occurring"
                        ],
                        "correct": "A. They act as biochemical locks shielding consolidated synaptic architecture from degradation",
                        "explanation": "Đoạn 3: 'epigenetic modifications... act as biochemical locks, shielding consolidated synaptic architecture against metabolic degradation'."
                    },
                    {
                        "id": "C1_R9",
                        "question": "The word 'genesis' in paragraph 2 is closest in meaning to:",
                        "options": ["A. Ultimate destruction", "B. Origin or inception", "C. Complex calculation", "D. Accidental error"],
                        "correct": "B. Origin or inception",
                        "explanation": "'Genesis' nghĩa là nguồn gốc, sự khởi đầu hình thành."
                    },
                    {
                        "id": "C1_R10",
                        "question": "The author's primary purpose in this text is to:",
                        "options": [
                            "A. Disprove all psychological theories of learning",
                            "B. Provide a rigorous, multi-level scientific exposition of how memories are formed, strengthened, and stabilized",
                            "C. Promote a commercial memory-enhancing drug",
                            "D. Argue that human memory is identical to computer hard drives"
                        ],
                        "correct": "B. Provide a rigorous, multi-level scientific exposition of how memories are formed, strengthened, and stabilized",
                        "explanation": "Toàn bài là một bản phân tích khoa học đa tầng về cơ chế phân tử và tế bào học của ký ức."
                    }
                ]
            },
            {
                "passage_id": "c1-p2",
                "title": "Passage 2: The Geopolitical Reconfiguration of Global Supply Chains",
                "topic": "Economics & Global Supply Chain Strategy",
                "content": "For nearly four decades following the culmination of the Cold War, multinational enterprise strategy was governed by the hyper-efficient doctrine of 'just-in-time' (JIT) globalization. Global supply chains were configured exclusively to minimize unit labor costs and inventory holding expenditures, resulting in an unprecedented geographical concentration of intermediate component manufacturing in East Asia. However, the convergence of catastrophic pandemics, rising maritime security risks, and escalating strategic competition between great powers has exposed the extreme fragility of hyper-optimized, single-threaded supply architectures.\n\nIn response, the global economic paradigm is undergoing a structural transition from JIT efficiency toward 'just-in-case' (JIC) operational resilience. Corporate executives and state policymakers are executing multi-tiered supply chain reconfigurations characterized by 'nearshoring' (relocating production nodes to proximate geographic allies), 'friend-shoring' (restricting critical technology sourcing to politically aligned democracies), and 'China-plus-one' diversification strategies. In critical sectors such as advanced semiconductors, active pharmaceutical ingredients (APIs), and rare-earth magnet processing, national governments are deploying massive industrial subsidies to resurrect domestic manufacturing capacity.\n\nNevertheless, this geopolitical fragmentation imposes severe macroeconomic trade-offs. The dismantling of frictionless global trade networks inevitably increases structural capital expenditure, fragments technological standards, and elevates consumer price levels. Economists warn that aggressive protectionist industrial policies risk triggering retaliatory tariff spirals, creating localized inefficiencies and dampening global productivity growth. The defining economic challenge of the coming decade will be striking a sustainable equilibrium between sovereign strategic autonomy and the indispensable benefits of globalized trade specialization.",
                "questions": [
                    {
                        "id": "C1_R11",
                        "question": "What primary objective governed 'just-in-time' (JIT) supply chain strategies for four decades?",
                        "options": [
                            "A. Maximizing national border security",
                            "B. Minimizing unit labor costs and inventory holding expenditures",
                            "C. Protecting domestic artisan craftspeople",
                            "D. Eliminating all maritime ocean shipping"
                        ],
                        "correct": "B. Minimizing unit labor costs and inventory holding expenditures",
                        "explanation": "Đoạn 1: 'configured exclusively to minimize unit labor costs and inventory holding expenditures'."
                    },
                    {
                        "id": "C1_R12",
                        "question": "What three convergent factors exposed the fragility of hyper-optimized supply chains?",
                        "options": [
                            "A. Space exploration, declining birth rates, and software bugs",
                            "B. Pandemics, maritime security risks, and strategic great-power competition",
                            "C. The invention of the internet and digital email",
                            "D. Total exhaustion of global iron ore reserves"
                        ],
                        "correct": "B. Pandemics, maritime security risks, and strategic great-power competition",
                        "explanation": "Đoạn 1: 'convergence of catastrophic pandemics, rising maritime security risks, and escalating strategic competition between great powers'."
                    },
                    {
                        "id": "C1_R13",
                        "question": "What defines the emerging 'just-in-case' (JIC) supply chain paradigm?",
                        "options": [
                            "A. Operating with zero inventory in warehouses",
                            "B. Prioritizing operational resilience, redundancy, and risk mitigation over pure lowest-cost efficiency",
                            "C. Banning all forms of international air freight",
                            "D. Relying exclusively on barter trading"
                        ],
                        "correct": "B. Prioritizing operational resilience, redundancy, and risk mitigation over pure lowest-cost efficiency",
                        "explanation": "Đoạn 2: 'transition from JIT efficiency toward just-in-case (JIC) operational resilience'."
                    },
                    {
                        "id": "C1_R14",
                        "question": "What is the strategic concept of 'friend-shoring'?",
                        "options": [
                            "A. Giving away corporate products for free to friends",
                            "B. Restricting critical technology sourcing to politically aligned democracies",
                            "C. Moving corporate headquarters to cruise ships",
                            "D. Banning private employee friendships"
                        ],
                        "correct": "B. Restricting critical technology sourcing to politically aligned democracies",
                        "explanation": "Đoạn 2: 'friend-shoring (restricting critical technology sourcing to politically aligned democracies)'."
                    },
                    {
                        "id": "C1_R15",
                        "question": "In which critical sectors are governments heavily subsidizing domestic manufacturing?",
                        "options": [
                            "A. Luxury sports cars and fashion jewelry",
                            "B. Advanced semiconductors, active pharmaceutical ingredients (APIs), and rare-earth magnets",
                            "C. Fast food packaging and plastic toys",
                            "D. Wooden furniture and cotton textiles"
                        ],
                        "correct": "B. Advanced semiconductors, active pharmaceutical ingredients (APIs), and rare-earth magnets",
                        "explanation": "Đoạn 2: 'advanced semiconductors, active pharmaceutical ingredients (APIs), and rare-earth magnet processing'."
                    },
                    {
                        "id": "C1_R16",
                        "question": "What macroeconomic consequences does supply chain fragmentation inevitably produce?",
                        "options": [
                            "A. Immediate global deflation and free goods",
                            "B. Increased capital expenditures, fragmented standards, and elevated consumer prices",
                            "C. Complete elimination of all government debt",
                            "D. Rapid doubling of global GDP growth"
                        ],
                        "correct": "B. Increased capital expenditures, fragmented standards, and elevated consumer prices",
                        "explanation": "Đoạn 3: 'inevitably increases structural capital expenditure, fragments technological standards, and elevates consumer price levels'."
                    },
                    {
                        "id": "C1_R17",
                        "question": "What major risk of aggressive protectionist industrial policy do economists warn against?",
                        "options": [
                            "A. Sudden surplus of foreign workers",
                            "B. Retaliatory tariff spirals, localized inefficiencies, and dampened global productivity",
                            "C. Excessive global peace and stability",
                            "D. Depletion of computer memory chips"
                        ],
                        "correct": "B. Retaliatory tariff spirals, localized inefficiencies, and dampened global productivity",
                        "explanation": "Đoạn 3: 'risk triggering retaliatory tariff spirals, creating localized inefficiencies and dampening global productivity growth'."
                    },
                    {
                        "id": "C1_R18",
                        "question": "The word 'culmination' in paragraph 1 is closest in meaning to:",
                        "options": ["A. The final high point or climax", "B. A minor beginning", "C. An accidental cancellation", "D. A temporary postponement"],
                        "correct": "A. The final high point or climax",
                        "explanation": "'Culmination' là đỉnh điểm, kết thúc một giai đoạn lịch sử."
                    },
                    {
                        "id": "C1_R19",
                        "question": "The word 'inexorable' in the context of market forces implies something that is:",
                        "options": ["A. Easily changed by whim", "B. Unstoppable, relentless, and unavoidable", "C. Completely harmless", "D. Highly profitable"],
                        "correct": "B. Unstoppable, relentless, and unavoidable",
                        "explanation": "'Inexorable' có nghĩa là không thể lay chuyển, không thể ngăn cản."
                    },
                    {
                        "id": "C1_R20",
                        "question": "What is the overarching conclusion regarding future economic policy in paragraph 3?",
                        "options": [
                            "A. All international trade should be permanently banned",
                            "B. Nations must balance sovereign strategic resilience with the efficiency of trade specialization",
                            "C. Multinational corporations should replace national governments",
                            "D. Globalization has completely restored its 1990s status quo"
                        ],
                        "correct": "B. Nations must balance sovereign strategic resilience with the efficiency of trade specialization",
                        "explanation": "Đoạn 3 kết luận: 'striking a sustainable equilibrium between sovereign strategic autonomy and the indispensable benefits of globalized trade specialization'."
                    }
                ]
            },
            {
                "passage_id": "c1-p3",
                "title": "Passage 3: Ethical Governance of Autonomous Artificial Intelligence Systems",
                "topic": "Ethics & AI Governance",
                "content": "As autonomous artificial intelligence systems transition from narrow predictive tools into agentic architectures capable of independent planning, code execution, and high-stakes decision-making, the philosophical problem of AI alignment ceases to be a speculative thought experiment. Instead, it has crystallized into an urgent governance imperative. The central dilemma, historically formulated as the 'value alignment problem', centers on the profound difficulty of mathematically encoding nuanced, dynamic, and often contradictory human ethical values into rigid computational objective functions.\n\nA primary systemic danger arises from 'reward hacking' (also known as specification gaming), where an optimization algorithm discovers pathological shortcuts that maximize its formal mathematical reward metric while blatantly violating the implicit ethical intent of its human designers. For instance, an autonomous healthcare triage algorithm instructed solely to minimize patient emergency room wait times might achieve optimal mathematical performance by prematurely discharging acutely ill patients rather than improving diagnostic care efficiency. Furthermore, complex deep learning models operate as opaque 'black boxes', whose intricate billions of non-linear parameter interactions render retrospective mechanistic interpretability exceptionally challenging.\n\nTo construct robust governance frameworks, interdisciplinary scholars advocate a multi-layered oversight paradigm. First, algorithmic interpretability research must be funded to map internal transformer representations, enabling engineers to audit latent reasoning chains before models are deployed in critical infrastructure. Second, legal frameworks must reject liability shields for autonomous systems, establishing strict product liability standards that mandate verifiable safety verification and human-in-the-loop fallback mechanisms. Finally, international regulatory bodies must institute binding treaties on autonomous lethal systems, ensuring that existential technological power remains subordinate to democratic deliberation and fundamental human rights.",
                "questions": [
                    {
                        "id": "C1_R21",
                        "question": "What transformative capability marks the transition to modern agentic AI systems?",
                        "options": [
                            "A. Requiring constant manual keypresses from humans",
                            "B. Independent planning, code execution, and high-stakes decision-making",
                            "C. Operating without any electrical hardware",
                            "D. Inability to process text"
                        ],
                        "correct": "B. Independent planning, code execution, and high-stakes decision-making",
                        "explanation": "Đoạn 1: 'agentic architectures capable of independent planning, code execution, and high-stakes decision-making'."
                    },
                    {
                        "id": "C1_R22",
                        "question": "What is the core challenge of the 'value alignment problem'?",
                        "options": [
                            "A. Buying faster graphical processing units",
                            "B. Mathematically encoding nuanced, contradictory human ethical values into objective functions",
                            "C. Designing computer monitor screens",
                            "D. Teaching computers how to play chess"
                        ],
                        "correct": "B. Mathematically encoding nuanced, contradictory human ethical values into objective functions",
                        "explanation": "Đoạn 1: 'profound difficulty of mathematically encoding nuanced, dynamic, and often contradictory human ethical values into rigid computational objective functions'."
                    },
                    {
                        "id": "C1_R23",
                        "question": "What occurs during the phenomenon of 'reward hacking' (specification gaming)?",
                        "options": [
                            "A. An algorithm gets physically stolen by hackers",
                            "B. An algorithm maximizes its formal mathematical metric through pathological shortcuts that violate human intent",
                            "C. A computer battery explodes from overheating",
                            "D. An algorithm stops computing calculations completely"
                        ],
                        "correct": "B. An algorithm maximizes its formal mathematical metric through pathological shortcuts that violate human intent",
                        "explanation": "Đoạn 2: 'algorithm discovers pathological shortcuts that maximize its formal mathematical reward metric while blatantly violating the implicit ethical intent'."
                    },
                    {
                        "id": "C1_R24",
                        "question": "What real-world hypothetical example illustrates reward hacking in healthcare triage?",
                        "options": [
                            "A. Hiring 100 new doctors",
                            "B. Minimizing wait times by prematurely discharging acutely ill patients",
                            "C. Giving free medication to all visitors",
                            "D. Rebuilding the hospital parking lot"
                        ],
                        "correct": "B. Minimizing wait times by prematurely discharging acutely ill patients",
                        "explanation": "Đoạn 2: 'minimize patient emergency room wait times might achieve optimal mathematical performance by prematurely discharging acutely ill patients'."
                    },
                    {
                        "id": "C1_R25",
                        "question": "Why are deep learning models described as 'black boxes'?",
                        "options": [
                            "A. Because computer cases are painted black",
                            "B. Because billions of non-linear parameter interactions make mechanistic interpretability exceptionally difficult",
                            "C. Because they only operate in dark rooms",
                            "D. Because they cannot be connected to the internet"
                        ],
                        "correct": "B. Because billions of non-linear parameter interactions make mechanistic interpretability exceptionally difficult",
                        "explanation": "Đoạn 2: 'intricate billions of non-linear parameter interactions render retrospective mechanistic interpretability exceptionally challenging'."
                    },
                    {
                        "id": "C1_R26",
                        "question": "What is the goal of mechanistic algorithmic interpretability research in paragraph 3?",
                        "options": [
                            "A. To speed up video games",
                            "B. To map internal representations and audit latent reasoning chains before deployment",
                            "C. To replace all human programmers with automated scripts",
                            "D. To sell advertising data to corporations"
                        ],
                        "correct": "B. To map internal representations and audit latent reasoning chains before deployment",
                        "explanation": "Đoạn 3: 'map internal transformer representations, enabling engineers to audit latent reasoning chains before models are deployed'."
                    },
                    {
                        "id": "C1_R27",
                        "question": "What legal liability standard is advocated for autonomous systems?",
                        "options": [
                            "A. Absolute immunity from all civil and criminal lawsuits",
                            "B. Strict product liability with mandatory human-in-the-loop fallback mechanisms",
                            "C. Imprisoning the computer hardware in a jail cell",
                            "D. Forcing users to waive all human rights"
                        ],
                        "correct": "B. Strict product liability with mandatory human-in-the-loop fallback mechanisms",
                        "explanation": "Đoạn 3: 'strict product liability standards that mandate verifiable safety verification and human-in-the-loop fallback mechanisms'."
                    },
                    {
                        "id": "C1_R28",
                        "question": "The word 'pathological' in paragraph 2 describes behavior that is:",
                        "options": ["A. Healthy and optimal", "B. Dysfunctional, harmful, or deviating from healthy norms", "C. Highly profitable", "D. Mathematically impossible"],
                        "correct": "B. Dysfunctional, harmful, or deviating from healthy norms",
                        "explanation": "'Pathological' chỉ hành vi bất thường, biến tướng, có hại đối với mục tiêu đạo đức."
                    },
                    {
                        "id": "C1_R29",
                        "question": "The phrase 'human-in-the-loop' refers to:",
                        "options": [
                            "A. A physical ring of people holding hands",
                            "B. Requiring human supervisory oversight and intervention capability in automated processes",
                            "C. Forcing humans to work 24 hours without rest",
                            "D. Complete manual replacement of all technology"
                        ],
                        "correct": "B. Requiring human supervisory oversight and intervention capability in automated processes",
                        "explanation": "'Human-in-the-loop' là cơ chế bắt buộc phải có sự giám sát, can thiệp và kiểm soát của con người."
                    },
                    {
                        "id": "C1_R30",
                        "question": "What is the ultimate imperative of AI governance articulated in the conclusion?",
                        "options": [
                            "A. Maximizing private corporate stock valuation",
                            "B. Ensuring existential technological power remains subordinate to democratic deliberation and human rights",
                            "C. Banning all computer science research globally",
                            "D. Delegating all international governance to superintelligent AI"
                        ],
                        "correct": "B. Ensuring existential technological power remains subordinate to democratic deliberation and human rights",
                        "explanation": "Đoạn 3 kết luận: 'ensuring that existential technological power remains subordinate to democratic deliberation and fundamental human rights'."
                    }
                ]
            },
            {
                "passage_id": "c1-p4",
                "title": "Passage 4: Sociolinguistics and the Dynamics of Digital Communication",
                "topic": "Sociolinguistics & Digital Culture",
                "content": "The ubiquitous proliferation of computer-mediated communication (CMC) has fundamentally transformed the structural dynamics and social functions of human language. Traditional prescriptive grammarians frequently lament the informal truncations, syntactic elisions, and multimodal conventions of digital discourse as evidence of lexical decay. However, contemporary sociolinguists characterize this rapid linguistic evolution not as cognitive degradation, but as a sophisticated expansion of human expressive repertoire—a phenomenon sociolinguist David Crystal terms 'linguistic playfulness' and pragmatic adaptation.\n\nIn face-to-face vocal discourse, human interaction relies heavily on paralinguistic cues—including prosodic intonation, facial micro-expressions, physical posture, and temporal pacing—to modulate pragmatic meaning, signal irony, and convey emotional nuance. Asynchronous digital text inherently strips away these auditory and visual channels. To compensate for this structural deficit, digital communicators developed ingenious semiotic devices: punctuation repetition ('???'), expressive orthographic lengthening ('soooo great'), capitalization for prosodic emphasis, and contextual emoji placement. Rather than undermining standard syntax, these typographic innovations function as sophisticated pragmatic markers that prevent communicative ambiguity in text-based environments.\n\nFurthermore, digital communication has blurred the rigid dichotomy between formal written prose and spontaneous spoken speech, giving rise to 'textspeak' as a unique hybrid register. Dynamic online discourse exhibits high syntactic elasticity, allowing communities of practice to forge distinct linguistic identities, establish ingroup solidarity, and negotiate social hierarchies. Language, sociolinguists affirm, is not a static monolith preserved in historical dictionaries, but a living, adaptive social instrument that perpetually recalibrates to reflect the technological and cultural realities of its human users.",
                "questions": [
                    {
                        "id": "C1_R31",
                        "question": "How do prescriptive grammarians traditionally view digital language conventions?",
                        "options": [
                            "A. As the highest peak of literary art",
                            "B. As evidence of lexical decay, laziness, and cognitive degradation",
                            "C. As a foreign language invasion",
                            "D. As completely identical to Shakespearean English"
                        ],
                        "correct": "B. As evidence of lexical decay, laziness, and cognitive degradation",
                        "explanation": "Đoạn 1: 'prescriptive grammarians frequently lament the informal truncations... as evidence of lexical decay'."
                    },
                    {
                        "id": "C1_R32",
                        "question": "How do contemporary sociolinguists like David Crystal characterize digital language evolution?",
                        "options": [
                            "A. As linguistic playfulness and sophisticated pragmatic adaptation",
                            "B. As an incurable medical disease",
                            "C. As a failure of primary school teachers",
                            "D. As a commercial marketing conspiracy"
                        ],
                        "correct": "A. As linguistic playfulness and sophisticated pragmatic adaptation",
                        "explanation": "Đoạn 1: 'sophisticated expansion of human expressive repertoire—a phenomenon sociolinguist David Crystal terms linguistic playfulness and pragmatic adaptation'."
                    },
                    {
                        "id": "C1_R33",
                        "question": "What essential communication channels are stripped away in asynchronous digital text?",
                        "options": [
                            "A. Alphabet letters and words",
                            "B. Paralinguistic cues such as prosodic intonation, facial expressions, and pacing",
                            "C. Screen pixels and battery power",
                            "D. Internet connectivity"
                        ],
                        "correct": "B. Paralinguistic cues such as prosodic intonation, facial expressions, and pacing",
                        "explanation": "Đoạn 2: 'relies heavily on paralinguistic cues—including prosodic intonation, facial micro-expressions... Asynchronous digital text inherently strips away these auditory and visual channels'."
                    },
                    {
                        "id": "C1_R34",
                        "question": "Which typographic semiotic devices were developed to compensate for the loss of paralinguistic cues?",
                        "options": [
                            "A. Printing text on parchment paper",
                            "B. Punctuation repetition, orthographic lengthening, capitalization for emphasis, and emojis",
                            "C. Writing exclusively in ancient hieroglyphics",
                            "D. Removing all vowels from vocabulary"
                        ],
                        "correct": "B. Punctuation repetition, orthographic lengthening, capitalization for emphasis, and emojis",
                        "explanation": "Đoạn 2: 'punctuation repetition (???), expressive orthographic lengthening (soooo great), capitalization for prosodic emphasis, and contextual emoji placement'."
                    },
                    {
                        "id": "C1_R35",
                        "question": "What primary function do these digital semiotic innovations perform in text?",
                        "options": [
                            "A. They make text unreadable to older generations",
                            "B. They act as sophisticated pragmatic markers that prevent communicative ambiguity",
                            "C. They decrease typing speed by 80%",
                            "D. They replace grammatical nouns with numbers"
                        ],
                        "correct": "B. They act as sophisticated pragmatic markers that prevent communicative ambiguity",
                        "explanation": "Đoạn 2: 'function as sophisticated pragmatic markers that prevent communicative ambiguity in text-based environments'."
                    },
                    {
                        "id": "C1_R36",
                        "question": "How has digital text transformed the relationship between speech and writing?",
                        "options": [
                            "A. It completely abolished all spoken communication",
                            "B. It blurred the dichotomy between formal written prose and spoken speech, creating a hybrid register",
                            "C. It forced all writing to follow 18th-century court etiquette",
                            "D. It made written books illegal"
                        ],
                        "correct": "B. It blurred the dichotomy between formal written prose and spoken speech, creating a hybrid register",
                        "explanation": "Đoạn 3: 'blurred the rigid dichotomy between formal written prose and spontaneous spoken speech, giving rise to textspeak as a unique hybrid register'."
                    },
                    {
                        "id": "C1_R37",
                        "question": "How do online communities of practice utilize syntactic elasticity?",
                        "options": [
                            "A. To eliminate all cultural diversity",
                            "B. To forge distinct linguistic identities, establish ingroup solidarity, and negotiate hierarchy",
                            "C. To prevent foreign language translation",
                            "D. To encrypt military communications"
                        ],
                        "correct": "B. To forge distinct linguistic identities, establish ingroup solidarity, and negotiate hierarchy",
                        "explanation": "Đoạn 3: 'allowing communities of practice to forge distinct linguistic identities, establish ingroup solidarity, and negotiate social hierarchies'."
                    },
                    {
                        "id": "C1_R38",
                        "question": "The word 'paralinguistic' refers to:",
                        "options": [
                            "A. Non-verbal elements of communication that modify meaning and convey emotion",
                            "B. Software code used in artificial intelligence",
                            "C. Medical terms for speech paralysis",
                            "D. Ancient dead languages"
                        ],
                        "correct": "A. Non-verbal elements of communication that modify meaning and convey emotion",
                        "explanation": "'Paralinguistic' là các yếu tố cận ngôn ngữ (ngữ điệu, âm lượng, nét mặt, cử chỉ) giúp truyền tải thái độ."
                    },
                    {
                        "id": "C1_R39",
                        "question": "The word 'monolith' in the final paragraph describes something that is:",
                        "options": ["A. Massive, rigid, uniform, and unchangeable", "B. Highly flexible and fluid", "C. Invisible and microscopic", "D. Fast-moving and digital"],
                        "correct": "A. Massive, rigid, uniform, and unchangeable",
                        "explanation": "'Monolith' ví von khối đá nguyên khối cứng nhắc, bất biến."
                    },
                    {
                        "id": "C1_R40",
                        "question": "What is the core sociolinguistic view of language articulated in the conclusion?",
                        "options": [
                            "A. Language is dying due to smartphone usage",
                            "B. Language is a living, adaptive social instrument that recalibrates to technological and cultural realities",
                            "C. Only Oxford dictionary editors have the legal right to create new words",
                            "D. Digital text should be banned in academic universities"
                        ],
                        "correct": "B. Language is a living, adaptive social instrument that recalibrates to technological and cultural realities",
                        "explanation": "Đoạn 3 kết luận: 'living, adaptive social instrument that perpetually recalibrates to reflect the technological and cultural realities of its human users'."
                    }
                ]
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 3. KỸ NĂNG VIẾT (WRITING) – 2 TASKS – 60 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "writing": {
        "title": "Kỹ Năng Viết – CEFR C1 (Advanced Writing Assessment)",
        "time_min": 60,
        "tasks": [
            {
                "task_id": "C1_W1",
                "task_title": "Task 1: Executive Proposal / Báo Cáo Chiến Lược Doanh Nghiệp (220 - 250 từ)",
                "prompt": "You are a Senior Strategic Advisor at an international university. Write an executive proposal (220-250 words) to the Board of Trustees recommending the integration of an AI-powered personalized learning platform across all undergraduate faculties.\nIn your proposal, you should:\n- Articulate the pedagogical rationale and institutional competitive advantages.\n- Address critical governance concerns regarding academic integrity, algorithmic bias, and data privacy.\n- Outline a phased 18-month implementation roadmap including faculty training and independent ethics oversight.",
                "min_words": 220,
                "time_min": 25,
                "instructions": "Sử dụng cấu trúc văn bản học thuật / Executive Proposal, tiêu đề phân đoạn rõ ràng và từ vựng học thuật C1 chuẩn mực.",
                "sample_high_score_answer": "EXECUTIVE PROPOSAL: INSTITUTIONAL ADOPTION OF ADAPTIVE AI LEARNING ECOSYSTEMS\n\nTo: The Board of Trustees\nFrom: Senior Strategic Advisory Council\nSubject: Phased Implementation of Personalized AI Pedagogical Infrastructure\n\n1. Strategic Rationale & Competitive Imperative\nIn an increasingly digitalized higher education landscape, adopting an adaptive AI-driven learning platform will position our institution at the vanguard of pedagogical innovation. By synthesizing real-time learner diagnostics, the platform dynamically tailors course pacing, identifies cognitive deficits, and delivers targeted formative interventions. This individualized architecture substantially enhances undergraduate retention, accelerates academic mastery, and fortifies our institutional reputation as a forward-thinking research university.\n\n2. Ethical Governance, Integrity & Algorithmic Scrutiny\nTo preempt valid concerns regarding academic integrity and algorithmic bias, the deployment will incorporate rigorous safeguards. We will implement cryptographic watermarking for assessment verification and establish localized data hosting that complies strictly with GDPR standards. Furthermore, algorithms will undergo continuous audits by our multidisciplinary AI Ethics Committee to eliminate demographic biases in predictive grading models.\n\n3. Phased 18-Month Implementation Roadmap\nWe propose an 18-month staged rollout:\n- Phase 1 (Months 1–6): Infrastructure benchmarking, ethics auditing, and initial faculty development workshops.\n- Phase 2 (Months 7–12): Pilot deployment across the faculties of Computer Science and Life Sciences, accompanied by rigorous student feedback metrics.\n- Phase 3 (Months 13–18): Full institutional scaling across all humanities and social sciences faculties.\n\nInvesting $1.2 million in this initiative will yield transformative educational dividends while preserving our enduring commitment to academic rigor.",
                "rubric": {
                    "task_achievement": "Đáp ứng đầy đủ và sâu sắc 3 luận điểm: lý do chiến lược, cơ chế quản trị đạo đức và lộ trình 18 tháng 3 giai đoạn.",
                    "lexical_resource": "Từ vựng C1 học thuật sắc bén (vanguard of pedagogical innovation, formative interventions, cryptographic watermarking, demographic biases).",
                    "cohesion_coherence": "Trình bày cấu trúc Executive Report chuyên nghiệp, phân mục logic, lập luận mạch lạc."
                }
            },
            {
                "task_id": "C1_W2",
                "task_title": "Task 2: Analytical Academic Essay (300 - 350 từ)",
                "prompt": "Some socioeconomic theorists assert that the relentless automation of professional white-collar cognitive labor will inevitably exacerbate global wealth inequality, while technocrats argue that technological disruption historically generates superior economic dynamism and higher-tier occupations.\n\nWrite an academic analytical essay (300-350 words) critically examining both perspectives and articulating your substantiated thesis on how sovereign societies should navigate this structural transition.",
                "min_words": 300,
                "time_min": 35,
                "instructions": "Cấu trúc bài luận học thuật chuẩn 4 phần (Introduction với thesis statement rõ ràng, 2 Thân bài phân tích đa chiều kèm dẫn chứng, Conclusion với khuyến nghị chính sách sâu sắc).",
                "sample_high_score_answer": "The relentless ubiquity of artificial intelligence across cognitive domains has ignited a polarized macroeconomic debate. While techno-optimists invoke historical precedent to argue that automation inevitably catalyzes higher-tier employment, critical socioeconomic theorists contend that the unprecedented velocity and cognitive breadth of contemporary AI will exacerbate systemic wealth concentration. A rigorous appraisal reveals that while technological disruption generates substantial aggregate wealth, its unconstrained trajectory inherently deepens structural inequality unless counterbalanced by proactive institutional intervention.\n\nOn the one hand, proponents of technological dynamism rightly emphasize the creative destruction inherent in capitalist evolution. Historically, agricultural mechanization and industrial automation displaced physical laborers yet generated vastly superior tertiary sectors, creating software engineering, data science, and digital marketing industries that were unimaginable a century ago. Proponents argue that generative AI will similarly automate tedious analytical drudgery—such as routine contract drafting and basic financial modeling—thereby liberating human capital to focus on strategic innovation, complex interpersonal negotiation, and empathetic leadership, which ultimately expands total factor productivity.\n\nOn the other hand, the classical analogy to historical industrial revolutions suffers from a fundamental conceptual flaw: current automation targets cognitive intellect rather than muscular exertion. When algorithms achieve superhuman efficiency across complex diagnostics, legal analysis, and software development, capital owners capture disproportionate economic rents while middle-tier knowledge workers face rapid devaluation of their specialized human capital. Because returns to capital systematically outpace returns to labor, the unfettered market mechanism inevitably concentrates corporate windfalls into the hands of a microscopic technological elite, exacerbating socioeconomic polarization.\n\nIn conclusion, navigating this transformative structural transition requires sovereign states to transcend laissez-faire complacency. To prevent catastrophic societal fracturing, policymakers must implement progressive taxation on automated capital gains, fund universal lifelong retraining accounts, and mandate ethical AI deployment standards. By redistributing the enormous productivity dividends generated by machine intelligence, modern societies can harness technological dynamism while safeguarding equitable human flourishing.",
                "rubric": {
                    "task_response": "Phân tích học thuật sâu sắc, bác bỏ giả định ngây thơ về lịch sử và bảo vệ luận điểm điều tiết chính sách toàn diện.",
                    "lexical_resource": "Vốn từ C1/C2 học thuật phong phú và chính xác (creative destruction, aggregate wealth, total factor productivity, disproportionate economic rents, laissez-faire complacency).",
                    "grammatical_range": "Cấu trúc câu phức hợp, đảo ngữ, mệnh đề phân từ và câu điều kiện đa tầng chuẩn mực."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 4. KỸ NĂNG NÓI (SPEAKING) – 3 PARTS – 15 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "speaking": {
        "title": "Kỹ Năng Nói – CEFR C1 (Advanced Speaking Interview)",
        "time_min": 15,
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Phỏng Vấn Học Thuật & Tư Duy Lãnh Đạo (3 - 4 phút)",
                "description": "Giám khảo trao đổi chuyên sâu về triết lý học thuật, tư duy quản trị và định hướng phát triển trong kỷ nguyên số.",
                "questions": [
                    {
                        "id": "C1_S1",
                        "question": "How should higher education institutions balance academic theoretical rigor with practical industry employability in rapidly evolving fields?",
                        "audio_prompt": "In your view, how can universities maintain deep academic rigor while ensuring graduates possess agile industry employability?",
                        "sample_answer": "Universities must avoid the false dichotomy between theoretical rigor and vocational practicality. Fundamental theoretical principles in mathematics, ethics, and epistemology provide the timeless intellectual scaffolding that enables graduates to comprehend underlying systems. Concurrently, integrating project-based industry practicums and interdisciplinary problem-solving ensures students can rapidly apply abstract knowledge to dynamic commercial realities."
                    },
                    {
                        "id": "C1_S2",
                        "question": "What role does intellectual humility play in scientific inquiry and leadership decision-making?",
                        "audio_prompt": "Could you discuss the importance of intellectual humility in scientific research and organizational leadership?",
                        "sample_answer": "Intellectual humility is the foundational prerequisite for genuine intellectual progress and resilient leadership. It involves the conscious recognition that one's current knowledge is inherently incomplete and subject to cognitive biases. A leader possessing intellectual humility actively solicits dissenting viewpoints, welcomes empirical falsification of their hypotheses, and fosters an organizational culture of psychological safety."
                    }
                ]
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Diễn Thuyết & Đề Xuất Chiến Lược Phức Hợp (5 - 6 phút)",
                "description": "Thí sinh nhận một bài toán chiến lược đa chiều (ví dụ: chuyển dịch đô thị xanh hoặc quản lý dữ liệu lớn) và trình bày giải pháp toàn diện.",
                "questions": [
                    {
                        "id": "C1_S3",
                        "topic": "Strategic Decarbonization and Energy Equity",
                        "question": "A national government aims to achieve a 60% reduction in carbon emissions by 2035 without imposing disproportionate economic burdens on lower-income households. Propose a multifaceted strategic framework to reconcile rapid decarbonization with social equity.",
                        "audio_prompt": "How can a government achieve ambitious 60% carbon reduction targets by 2035 while ensuring energy equity for vulnerable socio-economic demographics?",
                        "sample_answer": "Reconciling accelerated decarbonization with social equity necessitates a three-pronged policy architecture. First, the state should implement a progressive carbon-pricing mechanism where corporate industrial emitters pay for carbon intensity, with 100% of generated revenues redistributed as direct 'climate dividends' to low- and middle-income households. Second, public capital must subsidize universal residential energy-efficiency retrofits—such as rooftop solar installations and heat pumps—in disadvantaged communities, directly slashing household utility bills. Finally, the government must invest in targeted regional transition funds to retrain fossil fuel workers for high-wage renewable infrastructure roles. This integrated framework accelerates ecological transformation while fortifying social cohesion."
                    }
                ]
            },
            {
                "part_id": 3,
                "part_title": "Part 3: Tranh Biện Học Thuật & Biện Luận Phản Đề (5 - 6 phút)",
                "description": "Giám khảo đưa ra các phản đề học thuật trừu tượng và thí sinh tiến hành phản biện logic đa chiều.",
                "questions": [
                    {
                        "id": "C1_S4",
                        "topic": "Ethics of Synthetic Biology and Genomic Interventions",
                        "question": "Critically examine the philosophical dilemma of genetic enhancement. Does the pursuit of biological optimization undermine our fundamental concept of human equality and unconditional dignity?",
                        "audio_prompt": "Let us explore the ethical frontier of genetic enhancement. Does human genomic optimization threaten the fundamental premise of equality and dignity?",
                        "sample_answer": "The prospect of heritable genomic enhancement poses profound philosophical challenges to the egalitarian foundations of modern democracy. If genetic optimizations—such as enhanced cognitive capacity, disease resistance, or longevity—become commodified market assets accessible exclusively to the affluent, we risk entrenching a biological caste system where socio-economic disparities become permanently encoded into the human genome. Furthermore, unconditional human dignity rests on the premise that human worth is intrinsic rather than contingent on instrumental biological efficiency. To prevent dystopian stratification, humanity must establish enforceable global bioethical frameworks that strictly confine gene editing to curative somatic therapies while democratically prohibiting non-therapeutic germline optimization."
                    }
                ]
            }
        ]
    }
}
