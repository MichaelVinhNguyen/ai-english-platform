# -*- coding: utf-8 -*-
"""
backend/exams/c2_exam.py – Ngân Hàng Đề Thi Khảo Thí Bậc Thầy CEFR C2 / Cambridge CPE / VSTEP Bậc 6
Format Khảo Thí Thực Tế:
1. Kỹ Năng Nghe (Listening): 35 câu hỏi – 40 phút (Part 1: 8 câu, Part 2: 12 câu, Part 3: 15 câu)
2. Kỹ Năng Đọc (Reading): 40 câu hỏi – 60 phút (4 Passages x 10 câu)
3. Kỹ Năng Viết (Writing): 2 Tasks – 60 phút (Task 1: Comparative Synthesis 250 từ, Task 2: Scholarly Critique 350-400 từ)
4. Kỹ Năng Nói (Speaking): 3 Parts – 16 phút (Part 1: Spontaneous Discourse, Part 2: Academic Monologue, Part 3: Dialectical Debate)
"""

C2_STANDARDIZED_EXAM_DATA = {
    "exam_id": "c2-cpe-vstep-cefr-2026-01",
    "title": "Đề Thi Khảo Thí Bậc Thầy Tiếng Anh CEFR C2 / Cambridge CPE / VSTEP Bậc 6 Thực Chiến 2026",
    "level": "C2",
    "standard": "CEFR C2 Grand Mastery / Cambridge CPE / VSTEP Bậc 6 Format 2026",
    "total_time_min": 176,
    "pass_gpa": 7.0,

    # ══════════════════════════════════════════════════════════════════════════
    # 1. KỸ NĂNG NGHE (LISTENING) – 35 CÂU HỎI – 40 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "listening": {
        "title": "Kỹ Năng Nghe – CEFR C2 (Mastery & Scholarly Listening)",
        "total_questions": 35,
        "time_min": 40,
        "instructions": "Đề thi Nghe C2 kiểm tra khả năng thẩm thấu ngôn ngữ đỉnh cao, ngữ điệu tinh tế, ẩn dụ học thuật và đàm thoại tốc độ tự nhiên. Lắng nghe và chọn đáp án chính xác nhất.",
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Đàm Thoại Tự Nhiên & Châm Biếm Triết Học (8 câu)",
                "description": "Nghe 8 mẩu đối thoại ngắn chứa đựng các sắc thái khẩu ngữ tinh tế, châm biếm, hoán dụ và tư duy phản biện đỉnh cao.",
                "audio_script": "This is Part 1 of the CEFR C2 Listening Examination. You will hear eight authentic extracts. Choose the best answer from A, B, C, or D.",
                "questions": [
                    {
                        "id": "C2_L1",
                        "audio_text": "Philosopher: To claim that quantitative empiricism is the sole arbiter of epistemological validity is itself an unprovable metaphysical postulate, fundamentally undermining the positivistic dogma it purports to defend.",
                        "question": "What paradox in extreme positivism does the philosopher expose?",
                        "options": [
                            "A. Empiricism can calculate all mathematical equations",
                            "B. The assertion that only empirical proof is valid is itself an unprovable metaphysical claim",
                            "C. Quantitative science requires no funding",
                            "D. Positivism is identical to ancient mythology"
                        ],
                        "correct": "B. The assertion that only empirical proof is valid is itself an unprovable metaphysical claim",
                        "explanation": "Triết gia chỉ ra nghịch lý tự hủy của chủ nghĩa thực chứng: tuyên bố chỉ có thực nghiệm mới có giá trị lại chính là một tiên đề siêu hình học không thể chứng minh bằng thực nghiệm."
                    },
                    {
                        "id": "C2_L2",
                        "audio_text": "Diplomat: The treaty's deliberate syntactic ambiguity was not an oversight by the drafting committee; rather, it was the indispensable diplomatic sleight of hand that allowed irreconcilable sovereign factions to claim domestic victory.",
                        "question": "Why was intentional ambiguity embedded in the diplomatic treaty?",
                        "options": [
                            "A. Due to poor translation quality",
                            "B. As a necessary diplomatic compromise enabling competing factions to claim victory",
                            "C. To violate international maritime laws secretly",
                            "D. Because the treaty had no legal importance"
                        ],
                        "correct": "B. As a necessary diplomatic compromise enabling competing factions to claim victory",
                        "explanation": "Nhà ngoại giao giải thích sự mơ hồ có chủ đích là thủ pháp ngoại giao cốt lõi để các phe phái đối lập cùng chấp nhận ký kết."
                    },
                    {
                        "id": "C2_L3",
                        "audio_text": "Art historian: The painter's deliberate juxtaposition of classical chiaroscuro with jagged cubist fractures subverts the spectator's yearning for spatial coherence, exposing the alienated psyche of interwar European modernity.",
                        "question": "What is the intended psychological impact of the painter's aesthetic technique?",
                        "options": [
                            "A. To provide a soothing decorative pastoral portrait",
                            "B. To subvert spatial coherence and reflect the alienated psyche of interwar Europe",
                            "C. To demonstrate photographic precision",
                            "D. To teach basic color wheel harmony to children"
                        ],
                        "correct": "B. To subvert spatial coherence and reflect the alienated psyche of interwar Europe",
                        "explanation": "Sự kết hợp giữa sáng tối cổ điển và các mảng lập thể sắc nhọn nhằm phá vỡ cảm giác không gian và phản ánh tâm thức tha hóa của châu Âu giữa hai thế chiến."
                    },
                    {
                        "id": "C2_L4",
                        "audio_text": "Sociologist: The digital panopticon does not coerce compliance through physical coercion; rather, it operates through voluntary algorithmic hyper-visibility, where subjects enthusiastically commodify their own privacy for transient dopamine rewards.",
                        "question": "How does the modern digital panopticon maintain societal compliance?",
                        "options": [
                            "A. Through physical imprisonment and military force",
                            "B. Through voluntary self-commodification of privacy in exchange for dopamine rewards",
                            "C. By shutting off electricity worldwide",
                            "D. By forcing citizens to write long essays"
                        ],
                        "correct": "B. Through voluntary self-commodification of privacy in exchange for dopamine rewards",
                        "explanation": "Audio khẳng định cơ chế kiểm soát số vận hành qua sự tự nguyện trao đổi quyền riêng tư để nhận kích thích dopamine."
                    },
                    {
                        "id": "C2_L5",
                        "audio_text": "Bioethicist: The philosophical peril of de-extinction biotechnology is not merely ecological disruption, but the profound hubris of treating evolutionary history as a malleable consumer playground subordinate to human aesthetic whims.",
                        "question": "What fundamental ethical critique is leveled against de-extinction technology?",
                        "options": [
                            "A. It requires too few electricity resources",
                            "B. It embodies dangerous human hubris by treating evolution as a consumer playground",
                            "C. It immediately creates giant predatory monsters",
                            "D. It cures all known infectious diseases"
                        ],
                        "correct": "B. It embodies dangerous human hubris by treating evolution as a consumer playground",
                        "explanation": "Audio: 'profound hubris of treating evolutionary history as a malleable consumer playground subordinate to human aesthetic whims'."
                    },
                    {
                        "id": "C2_L6",
                        "audio_text": "Linguistic anthropologist: When an indigenous oral language disappears, humanity does not merely lose a set of phonemes; we lose an irreplaceable taxonomic conceptualization of biodiversity honed over millennia of empirical observation.",
                        "question": "What profound loss accompanies the extinction of an indigenous language?",
                        "options": [
                            "A. A temporary reduction in dictionary sales",
                            "B. An irreplaceable taxonomic conceptualization of biodiversity developed over millennia",
                            "C. The physical destruction of ancient stone monuments",
                            "D. Loss of computer keyboard fonts"
                        ],
                        "correct": "B. An irreplaceable taxonomic conceptualization of biodiversity developed over millennia",
                        "explanation": "Mất đi một ngôn ngữ bản địa đồng nghĩa với việc mất đi cả một hệ thống phân loại và tri thức về đa dạng sinh học được tích lũy hàng nghìn năm."
                    },
                    {
                        "id": "C2_L7",
                        "audio_text": "Legal scholar: In constitutional jurisprudence, textualism often disguises subjective ideological outcomes under the veneer of neutral historical semantics, freezing democratic evolution within eighteenth-century conceptual paradigms.",
                        "question": "What critical flaw in strict textualism does the scholar argue?",
                        "options": [
                            "A. It writes laws in confusing modern slang",
                            "B. It conceals ideological bias under historical semantics while stifling democratic evolution",
                            "C. It gives too much power to jury members",
                            "D. It abolishes the supreme court completely"
                        ],
                        "correct": "B. It conceals ideological bias under historical semantics while stifling democratic evolution",
                        "explanation": "Audio: 'disguises subjective ideological outcomes under the veneer of neutral historical semantics, freezing democratic evolution'."
                    },
                    {
                        "id": "C2_L8",
                        "audio_text": "Economist: The prevailing obsession with gross domestic product as the paramount metric of national success conflates transactional economic velocity with genuine societal flourishing, ignoring environmental degradation and systemic inequality.",
                        "question": "Why is GDP criticized as the sole metric of national progress?",
                        "options": [
                            "A. Because it is impossible to calculate with calculators",
                            "B. It conflates transaction velocity with genuine flourishing while ignoring ecology and inequality",
                            "C. It only measures agricultural farming output",
                            "D. It causes foreign exchange currency wars"
                        ],
                        "correct": "B. It conflates transaction velocity with genuine flourishing while ignoring ecology and inequality",
                        "explanation": "Audio: 'conflates transactional economic velocity with genuine societal flourishing, ignoring environmental degradation and systemic inequality'."
                    }
                ]
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Tọa Đàm Chuyên Gia Đa Ngành & Tranh Luận Học Thuật Đỉnh Cao (12 câu)",
                "description": "Nghe 3 cuộc hội thảo chuyên đề (mỗi cuộc 4 câu) về Triết học Nhận thức, Lý thuyết Lượng tử và Kinh tế học Thể chế.",
                "audio_script": "This is Part 2. You will hear three expert interdisciplinary symposia. Choose the best answer for each question.",
                "conversations": [
                    {
                        "conv_id": "c2-conv-1",
                        "context": "Hội thoại 1 (Câu 9 - 12): Tọa đàm về Bản chất của Ý thức và Vấn Đề 'Hard Problem' của David Chalmers.",
                        "audio_text": "Professor Hawthorne: The reductionist paradigm in neurobiology assumes that mapping every action potential in the connectome will spontaneously dissolve the 'Hard Problem' of consciousness. Yet, explaining functional informational processing leaves the qualitative richness of subjective experience—the 'qualia' of what it is like to see redness or feel grief—entirely unaddressed.\nDr. Laurent: While I appreciate the phenomenological perspective, appealing to non-physical panpsychism or dualism is an explanatory surrender. Neural correlate mapping combined with predictive processing frameworks is progressively narrowing the explanatory gap.\nProfessor Hawthorne: Merely bridging structural correlations does not constitute an ontological explanation of how subjective interiority emerges from objective physical mass. We require an entirely revolutionary epistemological framework that redefines the ontological status of subjective observation.\nDr. Laurent: Unless that framework generates testable empirical hypotheses in quantum biology or cognitive fMRI paradigms, it remains fascinating speculative metaphysics rather than rigorous science.",
                        "questions": [
                            {
                                "id": "C2_L9",
                                "question": "What is the core essence of the 'Hard Problem' of consciousness discussed by Professor Hawthorne?",
                                "options": [
                                    "A. The speed of electrical signals in human nerves",
                                    "B. Why and how physical neurological processes give rise to subjective qualitative experiences (qualia)",
                                    "C. How to cure memory loss in elderly patients",
                                    "D. The cost of brain surgery equipment"
                                ],
                                "correct": "B. Why and how physical neurological processes give rise to subjective qualitative experiences (qualia)",
                                "explanation": "Hawthorne chỉ rõ: giải thích quá trình xử lý thông tin chức năng vẫn không lý giải được tại sao lại xuất hiện cảm giác chủ quan sống động (qualia)."
                            },
                            {
                                "id": "C2_L10",
                                "question": "Why does Dr. Laurent criticize non-physical theories like dualism or panpsychism?",
                                "options": [
                                    "A. Because they are too expensive to study",
                                    "B. Because he considers them an explanatory surrender that abandons scientific investigation",
                                    "C. Because they were invented by ancient kings",
                                    "D. Because they require learning Greek grammar"
                                ],
                                "correct": "B. Because he considers them an explanatory surrender that abandons scientific investigation",
                                "explanation": "Dr. Laurent: 'appealing to non-physical panpsychism or dualism is an explanatory surrender'."
                            },
                            {
                                "id": "C2_L11",
                                "question": "What fundamental limitation in neural correlation mapping does Professor Hawthorne point out?",
                                "options": [
                                    "A. Brain scanners are not fast enough",
                                    "B. Structural correlation does not equal an ontological explanation of how subjectivity emerges from physical matter",
                                    "C. Computers cannot store brain scan images",
                                    "D. All neurons look identical under microscopes"
                                ],
                                "correct": "B. Structural correlation does not equal an ontological explanation of how subjectivity emerges from physical matter",
                                "explanation": "Hawthorne: 'Merely bridging structural correlations does not constitute an ontological explanation of how subjective interiority emerges from objective physical mass'."
                            },
                            {
                                "id": "C2_L12",
                                "question": "What strict criterion does Dr. Laurent demand for any proposed new framework?",
                                "options": [
                                    "A. It must be written in poetic verse",
                                    "B. It must generate testable empirical hypotheses in cognitive paradigms",
                                    "C. It must be approved by religious authorities",
                                    "D. It must completely reject all mathematical physics"
                                ],
                                "correct": "B. It must generate testable empirical hypotheses in cognitive paradigms",
                                "explanation": "Dr. Laurent: 'Unless that framework generates testable empirical hypotheses in quantum biology or cognitive fMRI paradigms, it remains fascinating speculative metaphysics'."
                            }
                        ]
                    },
                    {
                        "conv_id": "c2-conv-2",
                        "context": "Hội thoại 2 (Câu 13 - 16): Tranh biện về Cơ học Lượng tử và Bản chất Hiện thực Khách quan.",
                        "audio_text": "Dr. Thorne: The Copenhagen interpretation's assertion that physical reality remains in an indeterminate probabilistic superposition until an act of measurement occurs is philosophically unpalatable. The Many-Worlds interpretation mathematically preserves determinism by postulating continuous universal wave function branching without arbitrary observer-induced collapse.\nProfessor Klein: Yet, postulating an unobservable infinity of branching parallel universes violates Occam's razor far more egregiously than accepting wavefunction collapse as an objective physical decoherence threshold.\nDr. Thorne: Occam's razor applies to theoretical postulates, not physical ontologies. Many-Worlds requires zero extra mathematical ad hoc axioms—the Schrödinger equation applies universally and unceasingly.\nProfessor Klein: But without an empirically verifiable mechanism to test cross-branch decoherence, Many-Worlds teeters precariously between mathematical elegance and unfalsifiable theoretical dogma.",
                        "questions": [
                            {
                                "id": "C2_L13",
                                "question": "What core feature makes the Many-Worlds interpretation attractive to Dr. Thorne?",
                                "options": [
                                    "A. It disproves the existence of atoms",
                                    "B. It preserves mathematical determinism through continuous wave function branching without arbitrary collapse",
                                    "C. It requires no mathematical equations",
                                    "D. It explains the origin of human speech"
                                ],
                                "correct": "B. It preserves mathematical determinism through continuous wave function branching without arbitrary collapse",
                                "explanation": "Dr. Thorne: 'mathematically preserves determinism by postulating continuous universal wave function branching without arbitrary observer-induced collapse'."
                            },
                            {
                                "id": "C2_L14",
                                "question": "What philosophical objection does Professor Klein raise against Many-Worlds?",
                                "options": [
                                    "A. It is too easy to understand",
                                    "B. Postulating an unobservable infinity of parallel universes violates Occam's razor egregiously",
                                    "C. It contradicts classical algebra",
                                    "D. It costs too much electricity to simulate"
                                ],
                                "correct": "B. Postulating an unobservable infinity of parallel universes violates Occam's razor egregiously",
                                "explanation": "Professor Klein: 'postulating an unobservable infinity of branching parallel universes violates Occam's razor far more egregiously'."
                            },
                            {
                                "id": "C2_L15",
                                "question": "How does Dr. Thorne defend the mathematical simplicity of Many-Worlds?",
                                "options": [
                                    "A. By stating it requires zero ad hoc collapse axioms; the Schrödinger equation applies universally",
                                    "B. By claiming it was discovered by ancient philosophers",
                                    "C. By asserting that parallel worlds can be visited using rockets",
                                    "D. By ignoring all mathematical criticism"
                                ],
                                "correct": "A. By stating it requires zero ad hoc collapse axioms; the Schrödinger equation applies universally",
                                "explanation": "Dr. Thorne: 'Many-Worlds requires zero extra mathematical ad hoc axioms—the Schrödinger equation applies universally and unceasingly'."
                            },
                            {
                                "id": "C2_L16",
                                "question": "What epistemological warning does Professor Klein articulate in conclusion?",
                                "options": [
                                    "A. All physics experiments should be cancelled",
                                    "B. Without empirical falsifiability across branches, it risks becoming unfalsifiable dogma",
                                    "C. Quantum computers can never be built",
                                    "D. Light travels faster in glass than in vacuum"
                                ],
                                "correct": "B. Without empirical falsifiability across branches, it risks becoming unfalsifiable dogma",
                                "explanation": "Professor Klein: 'without an empirically verifiable mechanism... Many-Worlds teeters precariously between mathematical elegance and unfalsifiable theoretical dogma'."
                            }
                        ]
                    },
                    {
                        "conv_id": "c2-conv-3",
                        "context": "Hội thoại 3 (Câu 17 - 20): Bàn tròn về Kinh tế học Thể chế và Sự Sụp Đổ của Các Định Chế Tài Chính Phức Tạp.",
                        "audio_text": "Economist Vance: Financial contagion in hyper-connected algorithmic derivatives markets cannot be modeled using standard Gaussian normal distributions. Extreme tail risks—often dismissed as five-sigma statistical anomalies—occur with systemic frequency due to positive feedback loops and pro-cyclical leverage cascades.\nDr. Lindqvist: Exactly. When high-frequency trading algorithms execute synchronized liquidation protocols during market volatility, liquidity evaporates instantaneously. What appears micro-prudentially rational for an individual fund creates catastrophic macro-prudential systemic insolvency.\nEconomist Vance: That is why regulatory frameworks like Basel Accords must abandon static value-at-risk (VaR) models in favor of dynamic multi-agent systemic network stress testing and mandatory countercyclical capital buffers.\nDr. Lindqvist: Provided international regulators enforce strict cross-border jurisdiction over shadow banking conduits, otherwise risk merely migrates to unregulated opaque entities.",
                        "questions": [
                            {
                                "id": "C2_L17",
                                "question": "Why are standard Gaussian normal distributions inadequate for modeling derivatives contagion?",
                                "options": [
                                    "A. Because computers cannot calculate bell curves",
                                    "B. Extreme tail risks occur with systemic frequency due to positive feedback loops and pro-cyclical leverage",
                                    "C. Because interest rates are always negative",
                                    "D. Stock markets only operate during daytime hours"
                                ],
                                "correct": "B. Extreme tail risks occur with systemic frequency due to positive feedback loops and pro-cyclical leverage",
                                "explanation": "Vance: 'Extreme tail risks... occur with systemic frequency due to positive feedback loops and pro-cyclical leverage cascades'."
                            },
                            {
                                "id": "C2_L18",
                                "question": "What paradox between micro-rationality and macro-solvency is highlighted by Dr. Lindqvist?",
                                "options": [
                                    "A. Individual funds saving money causes banks to become richer",
                                    "B. Micro-prudentially rational actions for one fund (synchronized liquidation) create catastrophic macro-systemic insolvency",
                                    "C. Printing money makes all citizens wealthy",
                                    "D. Algorithms trade slower than human traders"
                                ],
                                "correct": "B. Micro-prudentially rational actions for one fund (synchronized liquidation) create catastrophic macro-systemic insolvency",
                                "explanation": "Lindqvist: 'What appears micro-prudentially rational for an individual fund creates catastrophic macro-prudential systemic insolvency'."
                            },
                            {
                                "id": "C2_L19",
                                "question": "What regulatory reform does Economist Vance advocate over static VaR models?",
                                "options": [
                                    "A. Complete deregulation of all hedge funds",
                                    "B. Dynamic multi-agent network stress testing and mandatory countercyclical capital buffers",
                                    "C. Closing stock exchanges whenever markets drop by 1%",
                                    "D. Banning all computer trading permanently"
                                ],
                                "correct": "B. Dynamic multi-agent network stress testing and mandatory countercyclical capital buffers",
                                "explanation": "Vance: 'abandon static value-at-risk (VaR) models in favor of dynamic multi-agent systemic network stress testing and mandatory countercyclical capital buffers'."
                            },
                            {
                                "id": "C2_L20",
                                "question": "What condition must be met to prevent risk migration according to Dr. Lindqvist?",
                                "options": [
                                    "A. Imposing strict cross-border regulatory jurisdiction over shadow banking conduits",
                                    "B. Giving shadow banks complete tax exemption",
                                    "C. Eliminating all commercial banking licenses",
                                    "D. Banning all foreign direct investment"
                                ],
                                "correct": "A. Imposing strict cross-border regulatory jurisdiction over shadow banking conduits",
                                "explanation": "Lindqvist: 'enforce strict cross-border jurisdiction over shadow banking conduits, otherwise risk merely migrates to unregulated opaque entities'."
                            }
                        ]
                    }
                ]
            },
            {
                "part_id": 3,
                "part_title": "Part 3: Bài Giảng Chuyên Khảo Bậc Thầy (15 câu)",
                "description": "Nghe 3 bài giảng chuyên khảo đỉnh cao (mỗi bài 5 câu) về Triết học Ngôn ngữ của Wittgenstein, Vật lý Thiên văn Lỗ đen và Mỹ học Hậu hiện đại.",
                "audio_script": "This is Part 3. You will hear three master scholarly lectures. Choose the best answer for each question.",
                "talks": [
                    {
                        "talk_id": "c2-talk-1",
                        "context": "Bài giảng 1 (Câu 21 - 25): Triết Học Ngôn Ngữ Của Ludwig Wittgenstein và Trò Chơi Ngôn Ngữ.",
                        "audio_text": "In his revolutionary later work, 'Philosophical Investigations', Ludwig Wittgenstein definitively repudiated his earlier picture theory of language articulated in the Tractatus. He demonstrated that language does not function as a static, crystalline mirror of empirical reality, but rather as an organic constellation of dynamic 'language-games' inextricably embedded within distinct 'forms of life'. The semantic meaning of a word is not an abstract metaphysical object to which it points, but rather its situated pragmatic usage within an agreed-upon rule-governed social practice. Consequently, traditional philosophical dilemmas regarding the nature of being, time, or truth are revealed not as profound ontological enigmas, but as linguistic pathologies arising when words are extracted from their functional everyday language-games and abstracted into metaphysical vacuums—what Wittgenstein famously described as language 'going on holiday'.",
                        "questions": [
                            {
                                "id": "C2_L21",
                                "question": "What core shift occurred in Wittgenstein's transition from the Tractatus to Philosophical Investigations?",
                                "options": [
                                    "A. He abandoned philosophy to study biology",
                                    "B. He rejected the picture theory of language in favor of dynamic language-games embedded in forms of life",
                                    "C. He argued that language should only be written in mathematical symbols",
                                    "D. He asserted that words have zero meaning in society"
                                ],
                                "correct": "B. He rejected the picture theory of language in favor of dynamic language-games embedded in forms of life",
                                "explanation": "Bài giảng: 'repudiated his earlier picture theory of language... in favor of dynamic language-games inextricably embedded within distinct forms of life'."
                            },
                            {
                                "id": "C2_L22",
                                "question": "According to later Wittgenstein, where does the semantic meaning of a word reside?",
                                "options": [
                                    "A. In an immutable Platonic ideal in heaven",
                                    "B. In its situated pragmatic usage within rule-governed social practices",
                                    "C. In the physical length of the word in syllables",
                                    "D. In the subjective mood of the speaker"
                                ],
                                "correct": "B. In its situated pragmatic usage within rule-governed social practices",
                                "explanation": "Bài giảng: 'The semantic meaning of a word is not an abstract metaphysical object... but rather its situated pragmatic usage within an agreed-upon rule-governed social practice'."
                            },
                            {
                                "id": "C2_L23",
                                "question": "How does Wittgenstein reframe classic metaphysical dilemmas in philosophy?",
                                "options": [
                                    "A. As mathematical equations waiting to be solved",
                                    "B. As linguistic pathologies arising when words are divorced from their everyday language-games",
                                    "C. As divine revelations of the cosmos",
                                    "D. As chemical reactions in the temporal lobe"
                                ],
                                "correct": "B. As linguistic pathologies arising when words are divorced from their everyday language-games",
                                "explanation": "Bài giảng: 'revealed not as profound ontological enigmas, but as linguistic pathologies arising when words are extracted from their functional everyday language-games'."
                            },
                            {
                                "id": "C2_L24",
                                "question": "What metaphor did Wittgenstein use to describe words abstracted into metaphysical confusion?",
                                "options": ["A. Language entering a black hole", "B. Language going on holiday", "C. Language breaking its spine", "D. Language running out of ink"],
                                "correct": "B. Language going on holiday",
                                "explanation": "Bài giảng: 'what Wittgenstein famously described as language going on holiday'."
                            },
                            {
                                "id": "C2_L25",
                                "question": "What is the primary therapeutic aim of Wittgensteinian linguistic philosophy?",
                                "options": [
                                    "A. To construct a universal super-language",
                                    "B. To dissolve pseudo-philosophical confusion by returning words to their practical communicative contexts",
                                    "C. To memorize all historical dictionaries",
                                    "D. To ban the use of metaphors in poetry"
                                ],
                                "correct": "B. To dissolve pseudo-philosophical confusion by returning words to their practical communicative contexts",
                                "explanation": "Mục tiêu trị liệu của triết học Wittgenstein là hóa giải các ảo tưởng triết học giả tạo bằng cách đưa từ ngữ trở về ngữ cảnh sử dụng đời thường."
                            }
                        ]
                    },
                    {
                        "talk_id": "c2-talk-2",
                        "context": "Bài giảng 2 (Câu 26 - 30): Vật Lý Thiên Văn Lượng Tử và Nghịch Lý Thông Tin Lỗ Đen của Hawking.",
                        "audio_text": "In 1974, Stephen Hawking demonstrated that quantum vacuum fluctuations near an event horizon cause black holes to emit thermal radiation, leading to their eventual complete evaporation. This discovery precipitated the acute 'Black Hole Information Paradox', striking at the very heart of theoretical physics. In quantum mechanics, the fundamental principle of unitarity mandates that the quantum state information of a closed system is strictly conserved and reversible across time. However, if a collapsing star composed of complex quantum information evaporates into purely random thermal Hawking radiation, that initial information is irrevocably destroyed—a catastrophic violation of quantum unitary determinism. Solutions like the Holographic Principle and ER=EPR wormhole entanglement suggest that information is preserved on the two-dimensional boundary horizon, effectively resolving the paradox through gravitational-quantum duality.",
                        "questions": [
                            {
                                "id": "C2_L26",
                                "question": "What discovery by Stephen Hawking triggered the Black Hole Information Paradox?",
                                "options": [
                                    "A. Black holes are infinite in size",
                                    "B. Black holes emit thermal radiation via quantum fluctuations and eventually evaporate",
                                    "C. Black holes reflect visible light like mirrors",
                                    "D. Gravity does not exist in outer space"
                                ],
                                "correct": "B. Black holes emit thermal radiation via quantum fluctuations and eventually evaporate",
                                "explanation": "Bài giảng: 'quantum vacuum fluctuations near an event horizon cause black holes to emit thermal radiation, leading to their eventual complete evaporation'."
                            },
                            {
                                "id": "C2_L27",
                                "question": "What foundational quantum mechanical principle is threatened if black hole information is destroyed?",
                                "options": [
                                    "A. The law of thermal expansion",
                                    "B. The principle of unitarity (conservation of quantum information and reversibility over time)",
                                    "C. Classical Newtonian momentum",
                                    "D. Chemical stoichiometry"
                                ],
                                "correct": "B. The principle of unitarity (conservation of quantum information and reversibility over time)",
                                "explanation": "Bài giảng: 'the fundamental principle of unitarity mandates that the quantum state information of a closed system is strictly conserved and reversible across time'."
                            },
                            {
                                "id": "C2_L28",
                                "question": "Why is the destruction of quantum information described as a catastrophic theoretical crisis?",
                                "options": [
                                    "A. Because it breaks quantum unitary determinism upon which modern physics is built",
                                    "B. Because it ruins astronomical telescopes",
                                    "C. Because black holes would swallow the entire universe in five minutes",
                                    "D. Because it makes mathematics illegal"
                                ],
                                "correct": "A. Because it breaks quantum unitary determinism upon which modern physics is built",
                                "explanation": "Bài giảng: 'irrevocably destroyed—a catastrophic violation of quantum unitary determinism'."
                            },
                            {
                                "id": "C2_L29",
                                "question": "What theoretical framework suggests information is encoded on the event horizon boundary?",
                                "options": ["A. Classical phlogiston theory", "B. The Holographic Principle and gravitational-quantum duality", "C. Kinetic gas theory", "D. Steady state cosmology"],
                                "correct": "B. The Holographic Principle and gravitational-quantum duality",
                                "explanation": "Bài giảng: 'Solutions like the Holographic Principle... suggest that information is preserved on the two-dimensional boundary horizon'."
                            },
                            {
                                "id": "C2_L30",
                                "question": "What does the ER=EPR conjecture establish a connection between?",
                                "options": [
                                    "A. Einstein-Rosen bridge wormholes and quantum entanglement",
                                    "B. Radio telescopes and submarine sonar",
                                    "C. Chemical batteries and solar flares",
                                    "D. Sound waves and visual colors"
                                ],
                                "correct": "A. Einstein-Rosen bridge wormholes and quantum entanglement",
                                "explanation": "Bài giảng: 'ER=EPR wormhole entanglement'."
                            }
                        ]
                    },
                    {
                        "talk_id": "c2-talk-3",
                        "context": "Bài giảng 3 (Câu 31 - 35): Mỹ Học Hậu Hiện Đại và Thuyết Mô Phỏng Simulacra của Jean Baudrillard.",
                        "audio_text": "French philosopher Jean Baudrillard's seminal treatise 'Simulacra and Simulation' delineates the successive historical phases through which human culture has detached representation from material reality. In the pre-modern era, the image functioned as a faithful reflection of a profound reality. In the second industrial phase, mass production created copies that mask and pervert reality. In the third phase, the image masks the absence of a profound reality, playing at being an appearance. In the hyperreal fourth phase—characteristic of contemporary algorithmic media—the simulacrum bears zero relation to any physical reality whatsoever; it becomes its own pure simulacrum. In this hyperreality of synthetic virtuality, media representations no longer mirror the world; rather, the simulation precedes and generates the real—a phenomenon Baudrillard famously designated as 'the precession of simulacra'.",
                        "questions": [
                            {
                                "id": "C2_L31",
                                "question": "What is the overarching subject of Jean Baudrillard's 'Simulacra and Simulation'?",
                                "options": [
                                    "A. How to build fast digital computers",
                                    "B. The historical detachment of cultural representation and media simulation from material reality",
                                    "C. The economic history of French banking",
                                    "D. Painting techniques during the Renaissance"
                                ],
                                "correct": "B. The historical detachment of cultural representation and media simulation from material reality",
                                "explanation": "Bài giảng: 'delineates the successive historical phases through which human culture has detached representation from material reality'."
                            },
                            {
                                "id": "C2_L32",
                                "question": "What characterizes the fourth, hyperreal phase of the image in Baudrillard's taxonomy?",
                                "options": [
                                    "A. It perfectly reproduces biological nature",
                                    "B. The simulacrum bears zero relation to any physical reality and becomes pure simulation",
                                    "C. It destroys all television networks",
                                    "D. It restores pre-modern religious faith"
                                ],
                                "correct": "B. The simulacrum bears zero relation to any physical reality and becomes pure simulation",
                                "explanation": "Bài giảng: 'In the hyperreal fourth phase... the simulacrum bears zero relation to any physical reality whatsoever; it becomes its own pure simulacrum'."
                            },
                            {
                                "id": "C2_L33",
                                "question": "What is meant by the famous phrase 'the precession of simulacra'?",
                                "options": [
                                    "A. The simulation precedes and actively generates what is perceived as real",
                                    "B. Physical nature destroys all artificial technology",
                                    "C. Time travels backwards in dreams",
                                    "D. Books are always printed before paintings are made"
                                ],
                                "correct": "A. The simulation precedes and actively generates what is perceived as real",
                                "explanation": "Bài giảng: 'the simulation precedes and generates the real—a phenomenon Baudrillard famously designated as the precession of simulacra'."
                            },
                            {
                                "id": "C2_L34",
                                "question": "How did images function in the pre-modern era according to Baudrillard?",
                                "options": [
                                    "A. As pure digital computer code",
                                    "B. As a faithful reflection of a profound underlying reality",
                                    "C. As mass-manufactured commercial advertisements",
                                    "D. As unreadable abstract shapes"
                                ],
                                "correct": "B. As a faithful reflection of a profound underlying reality",
                                "explanation": "Bài giảng: 'In the pre-modern era, the image functioned as a faithful reflection of a profound reality'."
                            },
                            {
                                "id": "C2_L35",
                                "question": "What is the critical implication of hyperreality for modern society?",
                                "options": [
                                    "A. Humanity has completely abandoned all technology",
                                    "B. Synthetic media representations supersede authentic physical experience, blurring truth and simulation",
                                    "C. Physical reality becomes more powerful than digital text",
                                    "D. All human communication becomes telepathic"
                                ],
                                "correct": "B. Synthetic media representations supersede authentic physical experience, blurring truth and simulation",
                                "explanation": "Bài giảng nhấn mạnh rằng trong kỷ nguyên siêu thực (hyperreality), các biểu tượng mô phỏng số chiếm lĩnh và định hình nhận thức thay thế hiện thực vật lý."
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
        "title": "Kỹ Năng Đọc – CEFR C2 (Mastery Scholarly Reading)",
        "total_questions": 40,
        "time_min": 60,
        "instructions": "Đề thi Đọc C2 gồm 4 bài chuyên khảo học thuật đỉnh cao (mỗi bài 10 câu hỏi) về Triết học Nhận thức, Vũ trụ học Lượng tử, Lý thuyết Trò chơi Vi mô và Mỹ học Hậu hiện đại.",
        "passages": [
            {
                "passage_id": "c2-p1",
                "title": "Passage 1: Epistemic Injustice and the Hermeneutical Architecture of Knowledge",
                "topic": "Epistemology & Political Philosophy",
                "content": "In her pioneering philosophical treatise, Miranda Fricker formulated the taxonomy of 'epistemic injustice'—a systemic ethical wrong committed against a person specifically in their capacity as a knower and transmitter of truth. Epistemic injustice operates primarily through two distinct yet mutually reinforcing modalities: 'testimonial injustice' and 'hermeneutical injustice'. Testimonial injustice occurs when prejudice causes a hearer to assign a deflated level of credibility to a speaker's word—such as when institutional juries discount the testimony of racial minorities or marginalized socioeconomic groups due to pervasive implicit stereotyping.\n\nHermeneutical injustice, by contrast, operates at a deeper, structural level. It occurs at a prior stage when a society suffers from a structural deficit in its collective interpretive resources, rendering a marginalized group unable to make sense of their own lived experiences or articulate their social reality to others. A quintessential historical manifestation was the pre-1970s conceptual vacuum surrounding 'sexual harassment'. Before feminist legal theorists coined this precise terminology, women experiencing workplace harassment endured profound psychological distress, yet were hermeneutically incapacitated from naming, legally protesting, or intellectually categorizing their grievance because the collective discursive lexicon possessed no conceptual category for it.\n\nOvercoming epistemic injustice requires cultivating collective 'epistemic virtue' and democratizing discursive power. Institutional epistemologies must actively decenter exclusionary paradigms, recognizing that marginalized standpoints provide unique, epistemically privileged vantage points capable of exposing structural blind spots in dominant paradigms. True democratic deliberation demands not merely equal political franchise, but the profound structural democratization of meaning-making itself.",
                "questions": [
                    {
                        "id": "C2_R1",
                        "question": "What is the core definition of 'epistemic injustice' formulated by Miranda Fricker?",
                        "options": [
                            "A. Physical violence against intellectual scholars",
                            "B. An ethical wrong committed against a person specifically in their capacity as a knower and truth-bearer",
                            "C. The theft of proprietary computer software",
                            "D. Refusing to purchase academic textbooks"
                        ],
                        "correct": "B. An ethical wrong committed against a person specifically in their capacity as a knower and truth-bearer",
                        "explanation": "Đoạn 1: 'systemic ethical wrong committed against a person specifically in their capacity as a knower and transmitter of truth'."
                    },
                    {
                        "id": "C2_R2",
                        "question": "What defines 'testimonial injustice' according to paragraph 1?",
                        "options": [
                            "A. Forbidding witnesses from speaking in court",
                            "B. Assigning deflated credibility to a speaker's word due to implicit prejudice or bias",
                            "C. Making all legal trials secret",
                            "D. Paying witnesses for false statements"
                        ],
                        "correct": "B. Assigning deflated credibility to a speaker's word due to implicit prejudice or bias",
                        "explanation": "Đoạn 1: 'when prejudice causes a hearer to assign a deflated level of credibility to a speaker's word'."
                    },
                    {
                        "id": "C2_R3",
                        "question": "How does 'hermeneutical injustice' fundamentally differ from testimonial injustice?",
                        "options": [
                            "A. It operates at an individual legal level only",
                            "B. It arises from a structural deficit in collective interpretive resources to articulate lived experiences",
                            "C. It is caused by foreign language translation software",
                            "D. It only applies to written poetry"
                        ],
                        "correct": "B. It arises from a structural deficit in collective interpretive resources to articulate lived experiences",
                        "explanation": "Đoạn 2: 'society suffers from a structural deficit in its collective interpretive resources, rendering a marginalized group unable to make sense of their own lived experiences'."
                    },
                    {
                        "id": "C2_R4",
                        "question": "What historical example illustrates hermeneutical injustice in paragraph 2?",
                        "options": [
                            "A. The invention of the printing press",
                            "B. The lack of the term 'sexual harassment' prior to the 1970s, which left victims unable to conceptualize their experience",
                            "C. The fall of the Roman Empire",
                            "D. The discovery of penicillin"
                        ],
                        "correct": "B. The lack of the term 'sexual harassment' prior to the 1970s, which left victims unable to conceptualize their experience",
                        "explanation": "Đoạn 2 nêu ví dụ lịch sử: việc thiếu vắng khái niệm 'quấy rối tình dục' trước thập niên 1970 khiến nạn nhân không có công cụ ngôn ngữ để gọi tên và đấu tranh pháp lý."
                    },
                    {
                        "id": "C2_R5",
                        "question": "The word 'deflated' in paragraph 1 is closest in meaning to:",
                        "options": ["A. Artificially elevated", "B. Diminished, lowered, or unfairly reduced", "C. Completely eliminated", "D. Mathematically multiplied"],
                        "correct": "B. Diminished, lowered, or unfairly reduced",
                        "explanation": "'Deflated' trong ngữ cảnh chỉ mức độ uy tín bị hạ thấp, giảm sút bất công do định kiến."
                    },
                    {
                        "id": "C2_R6",
                        "question": "The word 'incapacitated' in paragraph 2 suggests that individuals were:",
                        "options": ["A. Rendered unable or deprived of the conceptual capacity to act", "B. Highly motivated and energized", "C. Physically paralyzed in hospital", "D. Legally executed"],
                        "correct": "A. Rendered unable or deprived of the conceptual capacity to act",
                        "explanation": "'Incapacitated' nghĩa là bị tước đoạt khả năng, bị bất lực về mặt công cụ tư duy."
                    },
                    {
                        "id": "C2_R7",
                        "question": "What is the concept of 'standpoint epistemology' referenced in paragraph 3?",
                        "options": [
                            "A. Dominant social classes know all scientific truths perfectly",
                            "B. Marginalized standpoints offer unique epistemically privileged vantage points that expose systemic blind spots",
                            "C. No human can ever know anything with certainty",
                            "D. Only mathematical physicists have valid knowledge"
                        ],
                        "correct": "B. Marginalized standpoints offer unique epistemically privileged vantage points that expose systemic blind spots",
                        "explanation": "Đoạn 3: 'marginalized standpoints provide unique, epistemically privileged vantage points capable of exposing structural blind spots in dominant paradigms'."
                    },
                    {
                        "id": "C2_R8",
                        "question": "What is required to dismantle systemic epistemic injustice according to the conclusion?",
                        "options": [
                            "A. Banning all public debates in universities",
                            "B. Cultivating collective epistemic virtue and structural democratization of meaning-making",
                            "C. Replacing human judges with automated algorithms",
                            "D. Restricting university degrees to the political elite"
                        ],
                        "correct": "B. Cultivating collective epistemic virtue and structural democratization of meaning-making",
                        "explanation": "Đoạn 3: 'cultivating collective epistemic virtue and democratizing discursive power... profound structural democratization of meaning-making itself'."
                    },
                    {
                        "id": "C2_R9",
                        "question": "The tone of this passage can best be described as:",
                        "options": ["A. Sarcastic and colloquial", "B. Rigorously analytical, scholarly, and normative", "C. Nostalgic and sentimental", "D. Dismissive and aggressive"],
                        "correct": "B. Rigorously analytical, scholarly, and normative",
                        "explanation": "Văn phong bài viết mang tính học thuật phân tích triết học chuẩn mực và sắc bén."
                    },
                    {
                        "id": "C2_R10",
                        "question": "Which field of academic philosophy does this passage primarily contribute to?",
                        "options": ["A. Classical Epistemology and Social Political Philosophy", "B. Quantum Electro-dynamics", "C. Organic Synthetic Chemistry", "D. Applied Structural Geology"],
                        "correct": "A. Classical Epistemology and Social Political Philosophy",
                        "explanation": "Chủ đề bài viết thuộc về Nhận thức luận xã hội và Triết học chính trị."
                    }
                ]
            },
            {
                "passage_id": "c2-p2",
                "title": "Passage 2: Quantum Decoherence and the Emergence of Classical Reality",
                "topic": "Quantum Physics & Epistemological Ontology",
                "content": "One of the profoundest enigmas in foundational physics is the measurement problem: how does the deterministic, continuous linear evolution of the quantum wave function (governed by the unitary Schrödinger equation) transition into the discrete, non-linear, and definite macroscopic reality of classical observation? For decades, orthodox Copenhagen quantum mechanics relied on the ad hoc postulate of 'wave function collapse' triggered by an undefined 'observer'—an unscientific dualism that arbitrarily divided the universe into a quantum microscopic domain and a classical macroscopic apparatus.\n\nThe modern resolution of this conundrum is found in the theory of 'quantum decoherence', pioneered by physicists Heinz-Dieter Zeh and Wojciech Zurek. Decoherence demonstrates that isolated quantum systems do not exist in the physical universe; every quantum entity is inexorably coupled to its surrounding thermodynamic environment—a sea of photons, atmospheric air molecules, and thermal vibrations. Through continuous unitary quantum entanglement between the system and its environmental degrees of freedom, the system's off-diagonal phase interference terms are dispersed into the vast environment in fractions of a femtosecond ($10^{-15}$ seconds).\n\nCrucially, quantum decoherence does not modify the Schrödinger equation, nor does it require mysterious conscious observers. Instead, it dynamically selects stable 'pointer states' through an environmental selection mechanism termed 'Quantum Darwinism'. These robust pointer states—such as definite spatial positions—survive environmental monitoring and become redundantly imprinted across billions of environmental photons, allowing multiple independent macroscopic observers to agree on an objective, classical consensus reality.",
                "questions": [
                    {
                        "id": "C2_R11",
                        "question": "What fundamental enigma defines the 'measurement problem' in quantum mechanics?",
                        "options": [
                            "A. Measuring the weight of the sun accurately",
                            "B. How unitary quantum wave function superpositions transition into definite classical macroscopic observations",
                            "C. Designing digital clocks that do not lose seconds",
                            "D. Calculating the speed of sound underwater"
                        ],
                        "correct": "B. How unitary quantum wave function superpositions transition into definite classical macroscopic observations",
                        "explanation": "Đoạn 1: 'how does the deterministic, continuous linear evolution of the quantum wave function... transition into the discrete, non-linear, and definite macroscopic reality of classical observation?'."
                    },
                    {
                        "id": "C2_R12",
                        "question": "What critical flaw characterized the orthodox Copenhagen postulate of wave function collapse?",
                        "options": [
                            "A. It was too cheap to compute on computers",
                            "B. It relied on an ad hoc, unscientific dualism dividing the universe based on an undefined 'observer'",
                            "C. It required zero mathematical symbols",
                            "D. It was disproved by Isaac Newton"
                        ],
                        "correct": "B. It relied on an ad hoc, unscientific dualism dividing the universe based on an undefined 'observer'",
                        "explanation": "Đoạn 1: 'ad hoc postulate of wave function collapse triggered by an undefined observer—an unscientific dualism'."
                    },
                    {
                        "id": "C2_R13",
                        "question": "Which pioneering physicists formulated the modern theory of quantum decoherence?",
                        "options": [
                            "A. Charles Darwin and Gregor Mendel",
                            "B. Heinz-Dieter Zeh and Wojciech Zurek",
                            "C. Galileo Galilei and Johannes Kepler",
                            "D. Sigmund Freud and B.F. Skinner"
                        ],
                        "correct": "B. Heinz-Dieter Zeh and Wojciech Zurek",
                        "explanation": "Đoạn 2: 'pioneered by physicists Heinz-Dieter Zeh and Wojciech Zurek'."
                    },
                    {
                        "id": "C2_R14",
                        "question": "According to decoherence theory, why are quantum superpositions invisible in macroscopic life?",
                        "options": [
                            "A. Because human eyes are too small",
                            "B. Because quantum systems are inexorably entangled with environmental degrees of freedom, dispersing phase interference in femtoseconds",
                            "C. Because macroscopic objects move faster than light",
                            "D. Because quantum mechanics only applies to electricity"
                        ],
                        "correct": "B. Because quantum systems are inexorably entangled with environmental degrees of freedom, dispersing phase interference in femtoseconds",
                        "explanation": "Đoạn 2: 'continuous unitary quantum entanglement between the system and its environmental degrees of freedom... dispersed into the vast environment in fractions of a femtosecond'."
                    },
                    {
                        "id": "C2_R15",
                        "question": "What is the time scale of environmental decoherence mentioned in paragraph 2?",
                        "options": ["A. Several hours", "B. Fractions of a femtosecond (10^-15 seconds)", "C. Decades", "D. Thousands of years"],
                        "correct": "B. Fractions of a femtosecond (10^-15 seconds)",
                        "explanation": "Đoạn 2: 'in fractions of a femtosecond (10^-15 seconds)'."
                    },
                    {
                        "id": "C2_R16",
                        "question": "What is 'Quantum Darwinism' as described in paragraph 3?",
                        "options": [
                            "A. The biological evolution of bacteria in radioactive soil",
                            "B. Environmental selection of robust, stable pointer states that survive monitoring and replicate information",
                            "C. Survival of the strongest animal species in quantum labs",
                            "D. A philosophical proof of mechanical determinism"
                        ],
                        "correct": "B. Environmental selection of robust, stable pointer states that survive monitoring and replicate information",
                        "explanation": "Đoạn 3: 'dynamically selects stable pointer states through an environmental selection mechanism termed Quantum Darwinism'."
                    },
                    {
                        "id": "C2_R17",
                        "question": "How does Quantum Darwinism explain the existence of an objective classical consensus reality?",
                        "options": [
                            "A. By forcing all scientists to sign an agreement",
                            "B. Pointer state information is redundantly imprinted across billions of environmental photons for independent observers to record",
                            "C. By eliminating all quantum wave equations",
                            "D. Through brain telepathy between observers"
                        ],
                        "correct": "B. Pointer state information is redundantly imprinted across billions of environmental photons for independent observers to record",
                        "explanation": "Đoạn 3: 'redundantly imprinted across billions of environmental photons, allowing multiple independent macroscopic observers to agree on an objective, classical consensus reality'."
                    },
                    {
                        "id": "C2_R18",
                        "question": "The word 'conundrum' in paragraph 2 is closest in meaning to:",
                        "options": ["A. Intricate puzzle or difficult problem", "B. Financial bankruptcy", "C. Physical chemical explosion", "D. Minor mechanical friction"],
                        "correct": "A. Intricate puzzle or difficult problem",
                        "explanation": "'Conundrum' là câu đố hóc búa, bài toán nan giải."
                    },
                    {
                        "id": "C2_R19",
                        "question": "The word 'inexorably' in paragraph 2 reinforces the idea that environmental coupling is:",
                        "options": ["A. Completely avoidable with rubber gloves", "B. Unavoidable, relentless, and physically inescapable", "C. Highly dangerous and toxic", "D. Random and unpredictable"],
                        "correct": "B. Unavoidable, relentless, and physically inescapable",
                        "explanation": "'Inexorably' diễn tả sự gắn kết không thể tránh khỏi và diễn ra tất yếu trong tự nhiên."
                    },
                    {
                        "id": "C2_R20",
                        "question": "What is the primary conceptual breakthrough achieved by decoherence theory?",
                        "options": [
                            "A. It proved that classical physics is 100% false",
                            "B. It explains the emergence of classical reality entirely within unitary quantum mechanics without ad hoc observers",
                            "C. It built the first commercial fusion reactor",
                            "D. It unified general relativity with electromagnetism"
                        ],
                        "correct": "B. It explains the emergence of classical reality entirely within unitary quantum mechanics without ad hoc observers",
                        "explanation": "Decoherence giải thích sự hình thành hiện thực cổ điển hoàn toàn dựa trên cơ học lượng tử thuần nhất mà không cần đến giả định tùy tiện về người quan sát."
                    }
                ]
            },
            {
                "passage_id": "c2-p3",
                "title": "Passage 3: Algorithmic Game Theory, Mechanism Design, and Decentralized Market Equilibrium",
                "topic": "Microeconomics & Algorithmic Game Theory",
                "content": "Classical microeconomic general equilibrium theory, formalised in the Arrow-Debreu model, demonstrates that under conditions of complete competitive markets, perfect consumer information, and convex preferences, a Pareto-optimal price equilibrium universally exists. However, Arrow-Debreu's foundational architecture treats computation as instantaneous and costless, entirely ignoring computational complexity constraints. In modern high-frequency electronic financial exchanges and automated decentralized networks, the emergence of 'Algorithmic Game Theory' (AGT) has superseded classical equilibrium models by embedding computational complexity directly into strategic microeconomic formulations.\n\nA central breakthrough of AGT is the rigorous quantification of the 'Price of Anarchy' (PoA)—the mathematical ratio measuring how much collective societal welfare degrades when autonomous selfish agents optimize their personal utility in decentralized Nash equilibrium compared to an omniscient centralized social planner. In decentralized routing networks and algorithmic market auctions, selfish routing choices frequently induce structural congestion cascades, degrading overall network efficiency by significant factors. To mitigate this efficiency degradation, mechanism designers deploy algorithmic 'incentive engineering'—such as Vickrey-Clarke-Groves (VCG) dominant-strategy truthful auctions and algorithmic dynamic congestion pricing.\n\nFurthermore, in decentralized cryptoeconomic protocols, mechanism design must withstand not merely classical rational defection, but malicious Byzantine adversaries, Sybil attacks, and systemic front-running (Maximal Extractable Value, or MEV). Designing robust market protocols therefore requires proving both economic game-theoretic incentive compatibility and cryptographic Byzantine fault tolerance simultaneously. As automated algorithms increasingly negotiate global resource allocation, algorithmic mechanism design serves as the indispensable mathematical architecture preventing systemic market failure in the computational economy.",
                "questions": [
                    {
                        "id": "C2_R21",
                        "question": "What critical real-world constraint did the classical Arrow-Debreu equilibrium model completely ignore?",
                        "options": [
                            "A. The existence of money",
                            "B. Computational complexity and the time/energy costs of algorithmic computation",
                            "C. International border shipping tariffs",
                            "D. The laws of gravity"
                        ],
                        "correct": "B. Computational complexity and the time/energy costs of algorithmic computation",
                        "explanation": "Đoạn 1: 'treats computation as instantaneous and costless, entirely ignoring computational complexity constraints'."
                    },
                    {
                        "id": "C2_R22",
                        "question": "What mathematical metric does the 'Price of Anarchy' (PoA) quantify?",
                        "options": [
                            "A. The price of police defense equipment",
                            "B. The ratio of societal welfare degradation in selfish decentralized Nash equilibrium compared to an optimal social planner",
                            "C. The inflation rate during political revolutions",
                            "D. The cost of computer software piracy"
                        ],
                        "correct": "B. The ratio of societal welfare degradation in selfish decentralized Nash equilibrium compared to an optimal social planner",
                        "explanation": "Đoạn 2: 'mathematical ratio measuring how much collective societal welfare degrades when autonomous selfish agents optimize their personal utility in decentralized Nash equilibrium compared to an omniscient centralized social planner'."
                    },
                    {
                        "id": "C2_R23",
                        "question": "What occurs when autonomous selfish agents route traffic in decentralized networks without coordination?",
                        "options": [
                            "A. Traffic speeds increase to infinity",
                            "B. Selfish routing choices induce structural congestion cascades, degrading network efficiency",
                            "C. All network cables physically melt",
                            "D. Network costs drop to zero"
                        ],
                        "correct": "B. Selfish routing choices induce structural congestion cascades, degrading network efficiency",
                        "explanation": "Đoạn 2: 'selfish routing choices frequently induce structural congestion cascades, degrading overall network efficiency'."
                    },
                    {
                        "id": "C2_R24",
                        "question": "Which mechanism ensures that truthful bidding is a dominant strategy for rational participants?",
                        "options": [
                            "A. Lottery drawings",
                            "B. Vickrey-Clarke-Groves (VCG) truthful auction mechanisms",
                            "C. First-price sealed-bid auctions exclusively",
                            "D. Fixed government rationing quotas"
                        ],
                        "correct": "B. Vickrey-Clarke-Groves (VCG) truthful auction mechanisms",
                        "explanation": "Đoạn 2: 'Vickrey-Clarke-Groves (VCG) dominant-strategy truthful auctions'."
                    },
                    {
                        "id": "C2_R25",
                        "question": "What unique threats must decentralized cryptoeconomic mechanism design withstand?",
                        "options": [
                            "A. Paper document water damage",
                            "B. Byzantine adversaries, Sybil identity proliferation attacks, and Maximal Extractable Value (MEV) front-running",
                            "C. Shortage of physical metal coins",
                            "D. Telephone wire disconnections"
                        ],
                        "correct": "B. Byzantine adversaries, Sybil identity proliferation attacks, and Maximal Extractable Value (MEV) front-running",
                        "explanation": "Đoạn 3: 'withstand not merely classical rational defection, but malicious Byzantine adversaries, Sybil attacks, and systemic front-running (Maximal Extractable Value, or MEV)'."
                    },
                    {
                        "id": "C2_R26",
                        "question": "What dual theoretical proofs are mandatory for designing robust computational market protocols?",
                        "options": [
                            "A. High marketing budget and legal trademark registration",
                            "B. Economic incentive compatibility and cryptographic Byzantine fault tolerance simultaneously",
                            "C. Low electricity usage and simple visual interface",
                            "D. Approval by domestic banking associations exclusively"
                        ],
                        "correct": "B. Economic incentive compatibility and cryptographic Byzantine fault tolerance simultaneously",
                        "explanation": "Đoạn 3: 'proving both economic game-theoretic incentive compatibility and cryptographic Byzantine fault tolerance simultaneously'."
                    },
                    {
                        "id": "C2_R27",
                        "question": "The word 'superseded' in paragraph 1 means:",
                        "options": ["A. Reinforced and preserved", "B. Replaced, outmoded, and transcended by a more advanced paradigm", "C. Destroyed illegally", "D. Translated into Latin"],
                        "correct": "B. Replaced, outmoded, and transcended by a more advanced paradigm",
                        "explanation": "'Superseded' nghĩa là thay thế, vượt qua và nâng cấp lên một cấp độ cao hơn."
                    },
                    {
                        "id": "C2_R28",
                        "question": "The word 'omniscient' in paragraph 2 describes an entity that is:",
                        "options": ["A. All-knowing and possessing complete information", "B. Extremely greedy and selfish", "C. Slow and inefficient", "D. Invisible to radar"],
                        "correct": "A. All-knowing and possessing complete information",
                        "explanation": "'Omniscient' là toàn tri, thấu suốt toàn bộ thông tin."
                    },
                    {
                        "id": "C2_R29",
                        "question": "The term 'Byzantine fault tolerance' originates from computer science to describe systems that:",
                        "options": [
                            "A. Crash whenever one computer disconnects",
                            "B. Correctly reach consensus even when arbitrary components fail or act maliciously",
                            "C. Only operate inside Byzantine historical museums",
                            "D. Require manual human signature verification"
                        ],
                        "correct": "B. Correctly reach consensus even when arbitrary components fail or act maliciously",
                        "explanation": "Đồng thuận chống lỗi Byzantine là năng lực duy trì tính đúng đắn của mạng lưới ngay cả khi có nút bị lỗi hoặc cố tình phá hoại."
                    },
                    {
                        "id": "C2_R30",
                        "question": "What is the primary conclusion regarding algorithmic mechanism design in the modern economy?",
                        "options": [
                            "A. Markets should return to 19th-century gold coins",
                            "B. It constitutes the essential mathematical foundation preventing systemic market collapse in algorithmic resource allocation",
                            "C. All algorithms will be banned by international law",
                            "D. Game theory is irrelevant in computer science"
                        ],
                        "correct": "B. It constitutes the essential mathematical foundation preventing systemic market collapse in algorithmic resource allocation",
                        "explanation": "Đoạn 3 kết luận: 'algorithmic mechanism design serves as the indispensable mathematical architecture preventing systemic market failure in the computational economy'."
                    }
                ]
            },
            {
                "passage_id": "c2-p4",
                "title": "Passage 4: Postmodern Literary Hermeneutics and the Deconstruction of Textual Authority",
                "topic": "Literary Theory & Philosophical Hermeneutics",
                "content": "The post-structuralist revolution in literary hermeneutics, spearheaded by Jacques Derrida and Roland Barthes, permanently dismantled the longstanding Western metaphysical illusion of the 'authorial center'. For centuries, classical literary criticism operated under the theological presumption that a literary text possessed a singular, fixed, and transcendent 'original meaning' authoritatively implanted by its historical creator. In his incendiary 1967 essay, 'The Death of the Author', Barthes subverted this authorial hegemony, declaring that a text is not an enclosed theological message, but a multidimensional semiotic fabric composed of multiple citations, intertextual dialogues, and cultural codes, none of which are original.\n\nDerridean 'deconstruction' extended this radical critique by exposing the inherent instability and self-contradictions embedded within language itself. Through his signature conceptual coinage 'différance'—a neologism deliberately collapsing the French verbs for 'to defer' and 'to differ'—Derrida demonstrated that linguistic signifiers never achieve direct presence with their signified concepts. Instead, meaning is perpetually deferred along an endless chain of contextual trace substitutions. Every text, when scrutinized with rigorous deconstructive close-reading, contains internal aporias—points of insoluble structural impasse where the text's explicit rhetorical assertions are systematically undermined by its own linguistic subtext.\n\nFar from degenerating into nihilistic anti-intellectualism, post-structuralist hermeneutics performs a vital emancipatory and democratic function. By liberating the reader from subservience to the authorial patriarch, deconstruction relocates the locus of textual meaning to the active, interpretive engagement of the reading subject. It reveals that literature is an infinite, democratic space of pluralistic interpretation, where marginalized voices, silenced counter-narratives, and suppressed subtexts can be continuously unearthed and critically re-interrogated.",
                "questions": [
                    {
                        "id": "C2_R31",
                        "question": "What traditional metaphysical assumption in literary criticism was dismantled by post-structuralism?",
                        "options": [
                            "A. The belief that poems must always rhyme",
                            "B. The illusion that a text has a singular, fixed, transcendent meaning implanted by an authorial creator",
                            "C. The idea that books should be printed with black ink",
                            "D. The concept that paper is made from wood"
                        ],
                        "correct": "B. The illusion that a text has a singular, fixed, transcendent meaning implanted by an authorial creator",
                        "explanation": "Đoạn 1: 'dismantled the longstanding Western metaphysical illusion of the authorial center... singular, fixed, and transcendent original meaning'."
                    },
                    {
                        "id": "C2_R32",
                        "question": "How did Roland Barthes define a literary text in 'The Death of the Author'?",
                        "options": [
                            "A. As a strict legal document",
                            "B. As a multidimensional semiotic fabric composed of multiple citations, dialogues, and cultural codes",
                            "C. As an unreadable collection of random letters",
                            "D. As a proprietary commercial asset owned exclusively by publishers"
                        ],
                        "correct": "B. As a multidimensional semiotic fabric composed of multiple citations, dialogues, and cultural codes",
                        "explanation": "Đoạn 1: 'multidimensional semiotic fabric composed of multiple citations, intertextual dialogues, and cultural codes, none of which are original'."
                    },
                    {
                        "id": "C2_R33",
                        "question": "What dual linguistic meanings are fused in Jacques Derrida's neologism 'différance'?",
                        "options": [
                            "A. 'To destroy' and 'to create'",
                            "B. 'To defer' (postpone in time) and 'to differ' (distinguish in space/concept)",
                            "C. 'To write' and 'to speak'",
                            "D. 'To question' and 'to answer'"
                        ],
                        "correct": "B. 'To defer' (postpone in time) and 'to differ' (distinguish in space/concept)",
                        "explanation": "Đoạn 2: 'neologism deliberately collapsing the French verbs for to defer and to differ'."
                    },
                    {
                        "id": "C2_R34",
                        "question": "Why can linguistic signifiers never achieve 'direct presence' with signified concepts in deconstruction?",
                        "options": [
                            "A. Because ink fades over time",
                            "B. Meaning is perpetually deferred along an endless chain of contextual trace substitutions",
                            "C. Because dictionaries are too short",
                            "D. Because human vocal cords cannot produce perfect sounds"
                        ],
                        "correct": "B. Meaning is perpetually deferred along an endless chain of contextual trace substitutions",
                        "explanation": "Đoạn 2: 'signifiers never achieve direct presence with their signified concepts... meaning is perpetually deferred along an endless chain of contextual trace substitutions'."
                    },
                    {
                        "id": "C2_R35",
                        "question": "What is an 'aporia' in deconstructive literary analysis?",
                        "options": [
                            "A. A rhyming couplet at the end of a sonnet",
                            "B. A point of insoluble structural impasse where a text's rhetoric is undermined by its own subtext",
                            "C. The signature of the author on the title page",
                            "D. A blank page left accidentally by the printer"
                        ],
                        "correct": "B. A point of insoluble structural impasse where a text's rhetoric is undermined by its own subtext",
                        "explanation": "Đoạn 2: 'internal aporias—points of insoluble structural impasse where the text's explicit rhetorical assertions are systematically undermined by its own linguistic subtext'."
                    },
                    {
                        "id": "C2_R36",
                        "question": "Where does deconstruction relocate the primary locus of textual meaning?",
                        "options": [
                            "A. In the author's personal diary",
                            "B. In the active, interpretive engagement of the reading subject",
                            "C. In government censorship boards",
                            "D. In the physical price of the paperback book"
                        ],
                        "correct": "B. In the active, interpretive engagement of the reading subject",
                        "explanation": "Đoạn 3: 'relocates the locus of textual meaning to the active, interpretive engagement of the reading subject'."
                    },
                    {
                        "id": "C2_R37",
                        "question": "What vital democratic function does post-structuralist hermeneutics serve according to paragraph 3?",
                        "options": [
                            "A. It forces all citizens to vote for the same political party",
                            "B. It creates an infinite democratic space where marginalized voices and counter-narratives can be unearthed",
                            "C. It bans the study of classical ancient literature",
                            "D. It replaces human language with computer binary"
                        ],
                        "correct": "B. It creates an infinite democratic space where marginalized voices and counter-narratives can be unearthed",
                        "explanation": "Đoạn 3: 'literature is an infinite, democratic space of pluralistic interpretation, where marginalized voices, silenced counter-narratives, and suppressed subtexts can be continuously unearthed'."
                    },
                    {
                        "id": "C2_R38",
                        "question": "The word 'hegemony' in paragraph 1 refers to:",
                        "options": ["A. Dominant leadership, control, or authoritarian supremacy", "B. A peaceful artistic friendship", "C. Complete mathematical accuracy", "D. Financial debt"],
                        "correct": "A. Dominant leadership, control, or authoritarian supremacy",
                        "explanation": "'Hegemony' là quyền bá chủ, sự thống trị áp đặt độc quyền."
                    },
                    {
                        "id": "C2_R39",
                        "question": "The word 'emancipatory' in paragraph 3 is closest in meaning to:",
                        "options": ["A. Liberating and freeing from oppression or constraints", "B. Extremely complicated and boring", "C. Highly profitable commercially", "D. Strictly forbidden"],
                        "correct": "A. Liberating and freeing from oppression or constraints",
                        "explanation": "'Emancipatory' mang ý nghĩa giải phóng, giải phóng tư tưởng khỏi sự ràng buộc giáo điều."
                    },
                    {
                        "id": "C2_R40",
                        "question": "What is the author's primary attitude toward deconstruction in this text?",
                        "options": [
                            "A. Hostile and dismissive of all literary theory",
                            "B. Appreciative of its profound philosophical rigor and liberating democratic potential",
                            "C. Indifferent and bored",
                            "D. Demanding that all literature be written by artificial intelligence"
                        ],
                        "correct": "B. Appreciative of its profound philosophical rigor and liberating democratic potential",
                        "explanation": "Tác giả đánh giá cao chiều sâu triết học và tiềm năng dân chủ hóa giải phóng tư duy của giải cấu trúc."
                    }
                ]
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 3. KỸ NĂNG VIẾT (WRITING) – 2 TASKS – 60 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "writing": {
        "title": "Kỹ Năng Viết – CEFR C2 (Mastery Scholarly Writing)",
        "time_min": 60,
        "tasks": [
            {
                "task_id": "C2_W1",
                "task_title": "Task 1: Comparative Critical Synthesis / Tổng Hợp Phê Bình Đa Nguồn (250 từ)",
                "prompt": "Read the two contrasting academic perspectives below regarding the ethical governance of cognitive-enhancing biotechnology (nootropics and neural interfaces).\n\nText A argues that cognitive enhancement is an individual libertarian right that enhances human problem-solving capacity against existential global crises.\nText B contends that cognitive enhancement commodifies human intellect, exacerbates systemic socio-economic inequality, and undermines authentic human achievement.\n\nWrite an academic comparative synthesis (250 words) synthesizing the core arguments of both texts, critically evaluating their underlying assumptions, and articulating a coherent, substantiated thesis.",
                "min_words": 250,
                "time_min": 25,
                "instructions": "Tổng hợp, so sánh, phản biện và đưa ra luận đề học thuật sắc bén (Scholarly Synthesis).",
                "sample_high_score_answer": "The bioethical discourse surrounding cognitive enhancement biotechnology encapsulates a profound dialectical tension between libertarian individual autonomy and egalitarian social justice. Text A champions a transhumanist paradigm, positing that cognitive enhancement is an inalienable individual right that amplifies collective problem-solving capacity to combat existential planetary threats, such as climate destabilization and geopolitical volatility. Conversely, Text B articulates a trenchant egalitarian critique, warning that commodifying cognitive faculties will entrench a hereditary biological caste system, while eroding the intrinsic authenticity of unenhanced human striving.\n\nUpon rigorous critical appraisal, both perspectives exhibit salient epistemological insights yet harbor unresolved ideological blind spots. While Text A rightly identifies the imperative for cognitive augmentation in navigating hyper-complex modern systems, its uncritical reliance on free-market distribution naively ignores systemic wealth concentration, which would inevitably transform neural technologies into exclusive oligarchic monopolies. Meanwhile, although Text B validly defends egalitarian dignity, its defensive stance risks stifling therapeutic neuro-interventions that could alleviate catastrophic cognitive decline.\n\nTherefore, a synthesized bioethical framework must transcend this binary stalemate by adopting a 'democratic transhumanism'. Under this paradigm, sovereign states must guarantee universal, non-market access to safe cognitive therapeutics as fundamental public health goods, accompanied by strict democratic prohibitions against coercive corporate optimization. By decoupling cognitive enhancement from capitalist commodification, humanity can harness transformative neuro-technologies to elevate universal human flourishing while steadfastly safeguarding democratic equality.",
                "rubric": {
                    "task_achievement": "Tổng hợp trọn vẹn 2 văn bản, chỉ ra điểm mù triết học của cả 2 phía và đề xuất giải pháp 'democratic transhumanism' xuất sắc.",
                    "lexical_resource": "Vốn từ C2 đỉnh cao (dialectical tension, transhumanist paradigm, trenchant egalitarian critique, oligarchic monopolies, democratic transhumanism).",
                    "cohesion_coherence": "Lập luận triết học chặt chẽ, mạch lạc, kết nối tinh tế."
                }
            },
            {
                "task_id": "C2_W2",
                "task_title": "Task 2: Discursive Scholarly Dissertation / Khảo Cứu Học Thuật Chuyên Sâu (350 - 400 từ)",
                "prompt": "Throughout philosophical history, the dialectic between individual liberty and collective societal security has served as the foundational axis of political theory. In our contemporary era of algorithmic surveillance, biopolitical governance, and catastrophic global existential risks, this tension has acquired acute urgency.\n\nWrite a scholarly discursive essay (350-400 words) critically analyzing whether modern democratic nation-states are philosophically justified in curtailing individual civil liberties in the pursuit of collective biosecurity, technological safety, and social cohesion. Support your philosophical analysis with historical, legal, and sociopolitical frameworks.",
                "min_words": 350,
                "time_min": 35,
                "instructions": "Khảo cứu học thuật chuyên sâu 4-5 đoạn, vận dụng các trường phái triết học chính trị (Hobbes, Locke, Foucault, Habermas) và dẫn chứng đương đại.",
                "sample_high_score_answer": "The dialectical tension between individual liberty and collective security constitutes the perennial crucible of political philosophy. From Thomas Hobbes’ Leviathan—which posited absolute state sovereignty as the sole bulwark against the brutal anarchy of the state of nature—to John Locke’s defense of inalienable natural rights, political legitimacy has perpetually hinged on this delicate equilibrium. In our contemporary era, marked by asymmetric biosecurity threats, planetary ecological crises, and algorithmic disinformation, modern democratic states face unprecedented pressure to expand biopolitical surveillance. A critical appraisal reveals that while circumscribed, transparent emergency interventions may be procedurally justified to preserve the biological preconditions of society, permanent curtailments of civil liberties dismantle the very constitutional legitimacy the state purports to defend.\n\nProponents of state expansion invoke the utilitarian calculus of the 'harm principle' formulated by John Stuart Mill, arguing that sovereign power must intervene whenever individual actions generate catastrophic existential externalities. In scenarios involving weaponized synthetic pathogens or critical cyber-infrastructure sabotage, unfettered individual autonomy could precipitate irreversible systemic collapse. Under such acute existential imperatives, temporary biopolitical mandates—such as targeted contact tracing or mandatory vaccination regimes—serve as morally justifiable instruments to protect the foundational right to life, without which all other civil liberties become vacuous abstractions.\n\nHowever, the profound danger lies in the institutionalization of what Giorgio Agamben terms the 'state of exception'—wherein provisional emergency decrees metastasize into permanent architectures of digital panopticism. Michel Foucault’s critique of biopolitics demonstrates that sovereign power perpetually exploits crisis rhetoric to normalize invasive surveillance and suppress political dissent. When algorithmic monitoring and warrantless data interception become structural fixtures of governance, the democratic state ceases to be a contractarian protector of autonomous citizens; instead, it degenerates into a technocratic Leviathan that reduces human subjects to mere docile bodies.\n\nIn conclusion, modern democratic states are justified in curtailing civil liberties only under extraordinary, existential emergencies that satisfy the rigorous criteria of democratic proportionality, strict temporal sunset clauses, and independent judicial review. To permit unconstrained state intrusion under the amorphous guise of collective security is to commit a fatal category error: sacrificing the intrinsic moral essence of democratic freedom in the futile pursuit of an illusory, risk-free utopia.",
                "rubric": {
                    "task_response": "Luận văn khảo cứu học thuật xuất sắc, kết hợp nhuần nhuyễn tư tưởng Hobbes, Locke, Mill, Agamben và Foucault vào bài toán đương đại.",
                    "lexical_resource": "Kho từ vựng C2 đỉnh cao (perennial crucible, biopolitical surveillance, existential externalities, state of exception, technocratic Leviathan, temporal sunset clauses).",
                    "grammatical_range": "Cú pháp tiếng Anh học thuật thượng thừa, đảo ngữ, mệnh đề tuyệt đối và cấu trúc tu từ chuẩn xác."
                }
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # 4. KỸ NĂNG NÓI (SPEAKING) – 3 PARTS – 16 PHÚT
    # ══════════════════════════════════════════════════════════════════════════
    "speaking": {
        "title": "Kỹ Năng Nói – CEFR C2 (Mastery Speaking Interview)",
        "time_min": 16,
        "parts": [
            {
                "part_id": 1,
                "part_title": "Part 1: Phản Xạ Ngôn Ngữ Học Thuật Đỉnh Cao (4 - 5 phút)",
                "description": "Giám khảo đàm thoại tự nhiên với thí sinh về các vấn đề triết học, bản thể luận và đạo đức học thuật.",
                "questions": [
                    {
                        "id": "C2_S1",
                        "question": "How do you evaluate the philosophical assertion that absolute artistic freedom must remain unconstrained by societal moral conventions?",
                        "audio_prompt": "Should artistic expression remain absolute and unconstrained, or does art have an inherent ethical responsibility toward societal well-being?",
                        "sample_answer": "Artistic expression occupies an essential transgressive space in human culture. Historically, authentic artistic breakthroughs—from the subversive tragedies of Euripides to the radical aesthetics of Modernism—frequently provoked moral outrage by exposing the hypocrisies of dominant social conventions. To subordinate artistic creation to contemporary moral orthodoxy is to neuter its prophetic capacity to challenge institutional hegemony. While direct incitement to violence rightly falls under legal sanction, artistic expression must preserve its autonomous freedom to confront, disturb, and intellectually elevate human consciousness."
                    },
                    {
                        "id": "C2_S2",
                        "question": "In what ways does language shape, constrain, or expand the boundaries of human thought and philosophical conceptualization?",
                        "audio_prompt": "To what extent do the structural boundaries of our language determine the limits of our philosophical thought?",
                        "sample_answer": "Language is not merely a transparent medium for communicating pre-existing cognitive thoughts; rather, it is the constitutive architecture of thought itself. As Ludwig Wittgenstein famously posited, 'the limits of my language mean the limits of my world.' Grammatical structures and lexical richness provide the cognitive scaffolding through which we parse temporal sequence, moral agency, and ontological categorization. When our vocabulary expands, our capacity for nuanced conceptual discrimination and empathetic imagination deepens proportionally."
                    }
                ]
            },
            {
                "part_id": 2,
                "part_title": "Part 2: Độc Thoại Diễn Thuyết Chuyên Sâu Đa Chiều (5 - 6 phút)",
                "description": "Thí sinh nhận một chủ đề triết học/khoa học trừu tượng và thực hiện bài diễn thuyết học thuật không ngắt quãng kèm phân tích phản đề.",
                "questions": [
                    {
                        "id": "C2_S3",
                        "topic": "The Epistemological Limits of Scientific Reductionism",
                        "question": "Deliver an academic address examining the limits of scientific reductionism. Can complex emergent phenomena—such as consciousness, subjective morality, and artistic aesthetic value—ever be completely explained by fundamental physics?",
                        "audio_prompt": "Can emergent phenomena like consciousness and aesthetic value be completely reduced to fundamental physics? Present your comprehensive philosophical analysis.",
                        "sample_answer": "The triumph of scientific reductionism in unraveling the mechanistic laws of physics and chemistry has fostered an overambitious ontological assumption: that all macroscopic reality can be exhaustively reduced to the interactions of subatomic particles. However, this reductionist paradigm encounters insurmountable epistemological boundaries when confronted with strong emergent phenomena. In complex adaptive systems—from ecological balance to human consciousness—the collective behavior of the whole exhibits qualitative properties that are fundamentally non-deducible from the isolated properties of individual components. Subjective qualitative experience, aesthetic appreciation, and moral normativity possess their own autonomous ontological domains that cannot be collapsed into mere neurological firings without committing a profound category mistake. Therefore, a mature epistemology must embrace an ontological pluralism that honors the distinctive explanatory frameworks of both physical mechanisms and subjective interiority."
                    }
                ]
            },
            {
                "part_id": 3,
                "part_title": "Part 3: Tranh Biện Triết Học & Biện Luận Phản Đề (6 - 7 phút)",
                "description": "Giám khảo đưa ra các phản biện triết học cực kỳ phức tạp và thí sinh bảo vệ luận điểm bằng tư duy biện chứng đỉnh cao.",
                "questions": [
                    {
                        "id": "C2_S4",
                        "topic": "Existential Risk, Transhumanism, and Human Flourishing",
                        "question": "Is the transhumanist aspiration to transcend biological human limitations an inevitable triumph of evolutionary intelligence, or does it represent an existential negation of what makes human existence intrinsically meaningful?",
                        "audio_prompt": "Does the transhumanist goal to technologically transcend biological limits fulfill human potential, or does it destroy the intrinsic meaning of human existence?",
                        "sample_answer": "The transhumanist quest to overcome biological vulnerability and mortality touches upon the core existential paradox of human identity. On one hand, humanity has perpetually utilized technology—from fire and agriculture to vaccines and artificial intelligence—to transcend our raw evolutionary constraints. In this sense, cognitive and genetic augmentation represents the logical continuation of our innate species drive toward self-transcendence. However, philosophical existentialism reminds us that much of what endows human existence with profound beauty, ethical virtue, and artistic depth—such as empathy, courage, and unconditional love—is inextricably tethered to our biological finitude and shared vulnerability. If we engineered a post-human entity devoid of vulnerability, suffering, and mortality, we might not achieve the perfection of humanity, but rather its complete ontological erasure. The true challenge of wisdom is not escaping our mortal humanity, but cultivating its ethical and spiritual zenith."
                    }
                ]
            }
        ]
    }
}
