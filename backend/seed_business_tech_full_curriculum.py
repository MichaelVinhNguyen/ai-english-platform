# -*- coding: utf-8 -*-
"""
seed_business_tech_full_curriculum.py – 30 Full Modules & 30 Mock Tests for BUSINESS and TECH Tracks.
Tailored specifically to:
1. Business BIZ: International Trade, Contract Negotiations, Corporate Finance, Venture Pitching, M&A, Leadership
2. Tech & AI: Agile Standups, System Architecture, Microservices, LLMs, RAG, DevOps, Cloud, AI Agents, Cybersecurity
"""

import json

# ═══════════════════════════════════════════════════════════════════════════════
# 1. 30 BUSINESS BIZ MODULES (Full 8-Stage Omni-Method Studio Data)
# ═══════════════════════════════════════════════════════════════════════════════

BUSINESS_MODULE_TOPICS = [
    ("Đàm Phán Hợp Đồng, Điều Khoản Thanh Toán & Incoterms", "Contract Negotiations, Payment Terms & Incoterms 2026"),
    ("Pitching Kêu Gọi Vốn Đầu Tư Mạo Hiểm, TAM/SAM/SOM & Định Giá", "Venture Capital Pitching, TAM/SAM/SOM & Valuation"),
    ("Thương Mại Quốc Tế, Vận Tải Đa Phương Thức & Khai Báo Hải Quan", "Cross-Border Trade, Freight Forwarding & Customs Clearance"),
    ("Phân Tích Báo Cáo Tài Chính Doanh Nghiệp (P&L, Balance Sheet, Cash Flow)", "Corporate Financial Statement Analysis & Cash Flow Dynamics"),
    ("Soạn Thảo Hồ Sơ Thầu (RFP), Thư Chào Hàng & Email Ngoại Giao", "RFP Proposals, Quotations & Executive Correspondence"),
    ("Mua Bán & Sáp Nhập Doanh Nghiệp (M&A) & Thẩm Định Pháp Lý", "Mergers & Acquisitions (M&A) & Due Diligence Procedures"),
    ("Chiến Lược Thương Hiệu, Tiếp Thị Đa Kênh & Chi Phí Khách Hàng (CAC/LTV)", "Brand Strategy, Omnichannel Marketing & CAC/LTV Optimization"),
    ("Quản Trị Nguồn Nhân Lực, Tuyển Dụng Nhân Tài & Hệ Thống KPI", "Human Resource Strategy, Talent Acquisition & KPI Systems"),
    ("Quản Trị Doanh Nghiệp, Đại Hội Cổ Đông & Nghị Quyết HĐQT", "Corporate Governance, Board Meetings & Shareholder Resolutions"),
    ("Tối Ưu Chuỗi Cung Ứng, Quản Lý Tồn Kho Just-In-Time & Tinh Gọn", "Supply Chain Resilience, Inventory Optimization & Just-In-Time"),
    ("Luật Thương Mại Quốc Tế, Bảo Hộ Sở Hữu Trí Tuệ & Hợp Đồng NDA", "International Business Law, IP Protection & Non-Disclosure Agreements"),
    ("Quan Hệ Công Chúng, Quản Trị Khủng Hoảng Truyền Thông & Họp Báo", "Public Relations, Crisis Communications & Media Triage"),
    ("Bán Hàng Doanh Nghiệp B2B, Quản Lý Khách Hàng Trọng Tâm (Key Account)", "B2B Enterprise Sales, Key Account Management & Deal Pipeline"),
    ("Kinh Tế Vĩ Mô Toàn Cầu, Phòng Ngừa Rủi Ro Tỷ Giá (Forex Hedging)", "Macroeconomic Indicators, Forex Hedging & Interest Rate Exposure"),
    ("Nghệ Thuật Đàm Phán Liên Văn Hóa & Nghi Thức Ngoại Giao Thương Mại", "Cross-Cultural Negotiation Dynamics & Business Protocol"),
    ("Quản Lý Danh Mục Dự Án Doanh Nghiệp, Khung Mục Tiêu OKR & Quản Trị", "Project Portfolio Management, Enterprise Agile & OKR Frameworks"),
    ("Thương Mại Điện Tử Toàn Cầu, Cổng Thanh Toán & Tối Ưu Tỷ Lệ Chuyển Đổi", "Global E-Commerce Platforms, Payment Gateways & Conversion Funnels"),
    ("Quản Trị Rủi Ro Doanh Nghiệp, Kiểm Toán Nội Bộ & Khung Tuân Thủ", "Enterprise Risk Management (ERM), Internal Audit & Compliance"),
    ("Chiến Lược Phát Triển Bền Vững ESG, Tín Chỉ Carbon & Tài Chính Xanh", "Sustainable Corporate Governance, ESG Criteria & Green Finance"),
    ("Mô Hình Nhượng Quyền Thương Mại, Hợp Đồng Li-xăng & Phí Bản Quyền", "Franchise Expansion, Licensing Agreements & Royalty Structuring"),
    ("Tối Ưu Giá Trị Vòng Đời Khách Hàng (LTV) & Chỉ Số Hài Lòng (NPS)", "Customer Lifetime Value Optimization, Retention & NPS Analytics"),
    ("Ngân Hàng Đầu Tư, Khoản Vay Hợp Vốn & Phát Hành Trái Phiếu", "Investment Banking, Syndicated Loans & Corporate Bond Issuance"),
    ("Chuyển Đổi Số Doanh Nghiệp, Tích Hợp ERP & Tự Động Hóa Quy Trình", "Digital Transformation, ERP Integration & Business Process Automation"),
    ("Giải Quyết Tranh Chấp Thương Mại, Trọng Tài Quốc Tế & Hòa Giải", "Dispute Resolution, International Commercial Arbitration & Mediation"),
    ("Liên Minh Chiến Lược, Liên Doanh Quốc Tế (JV) & Đấu Thầu Liên Danh", "Strategic Alliances, Cross-Border Joint Ventures & Consortium Bidding"),
    ("Chiến Lược Định Giá Sản Phẩm, Độ Co Giãn & Quản Lý Doanh Thu", "Pricing Strategies, Price Elasticity & Dynamic Yield Optimization"),
    ("Kế Hoạch Thuế Quốc Tế, Chuyển Giá (Transfer Pricing) & Hiệp Định Tránh Đánh Thuế Hai Lần", "International Corporate Tax Planning, Transfer Pricing & DTA Treaties"),
    ("Tái Cấu Trúc Tổ Chức, Quản Trị Sự Thay Đổi & Văn Hóa Doanh Nghiệp", "Organizational Restructuring, Change Management & Corporate Culture"),
    ("Chiến Dịch Ra Mắt Sản Phẩm Mới & Thâm Nhập Thị Trường Quốc Tế", "Product Launch Campaigns, Go-To-Market (GTM) & Market Penetration"),
    ("Năng Lực Lãnh Đạo C-Suite, Hoạch Định Tầm Nhìn Chiến Lược Toàn Cầu", "Executive C-Suite Leadership, Board Strategy & Global Vision")
]

def generate_business_modules():
    modules = []
    for idx, (title_vi, title_en) in enumerate(BUSINESS_MODULE_TOPICS, start=1):
        mod = {
            "id": f"biz-m{idx}",
            "title": f"Bài {idx}: {title_vi}",
            "description": f"Chuyên đề nâng cao: {title_en}. Làm chủ từ vựng, ngữ pháp ngoại giao, đàm phán hợp đồng, phân tích báo cáo và email thương mại quốc tế.",
            "duration_min": 40,
            "xp": 110 + (idx % 10) * 2,
            "theory": f"Trong môi trường kinh doanh toàn cầu, chuyên đề '{title_en}' đóng vai trò then chốt giúp các nhà quản lý và chuyên viên đàm phán đạt được các thỏa thuận thương mại có giá trị cao, tuân thủ pháp lý và xây dựng quan hệ hợp tác chiến lược bền vững.",
            "key_vocab": [
                {"word": "Procurement", "ipa": "/prəˈkjʊrmənt/", "meaning": "Hoạt động thu mua / Mua sắm doanh nghiệp", "example": "Our procurement department negotiates bulk purchasing discounts."},
                {"word": "Feasibility", "ipa": "/ˌfiːzəˈbɪləti/", "meaning": "Tính khả thi của dự án kinh doanh", "example": "We conducted a comprehensive financial feasibility study."},
                {"word": "Compromise", "ipa": "/ˈkɑːmprəmaɪz/", "meaning": "Sự thỏa hiệp / Thống nhất quyền lợi đôi bên", "example": "Both parties reached an equitable compromise on warranty terms."},
                {"word": "Stakeholder", "ipa": "/ˈsteɪkhoʊldər/", "meaning": "Các bên liên quan trọng yếu", "example": "We must align with key stakeholders prior to contract execution."},
                {"word": "Due Diligence", "ipa": "/ˌduː ˈdɪlɪdʒəns/", "meaning": "Thẩm định chuyên sâu (pháp lý, tài chính)", "example": "The acquisition is contingent upon satisfactory due diligence."},
                {"word": "Deliverable", "ipa": "/dɪˈlɪvərəbl/", "meaning": "Sản phẩm / Hạng mục bàn giao theo hợp đồng", "example": "All project deliverables must be signed off by the end of Q3."},
                {"word": "Benchmark", "ipa": "/ˈbentʃmɑːrk/", "meaning": "Tiêu chuẩn đối sánh ngành", "example": "Our EBITDA margins set the industry benchmark for profitability."},
                {"word": "Remediation", "ipa": "/rɪˌmiːdiˈeɪʃn/", "meaning": "Biện pháp khắc phục vi phạm / Xử lý sự cố", "example": "The agreement includes strict remediation clauses for delivery delays."}
            ],
            "grammar_point": {
                "rule": f"Cấu trúc ngữ pháp đàm phán thương mại & ngoại giao bài {idx}: Diplomatic Hedging & Conditional Undertakings",
                "formula": "We are prepared to concede X, on condition that / provided that you agree to Y",
                "examples": [
                    "We can grant an additional 5% volume rebate, provided that your annual commitment exceeds $2M.",
                    "Subject to regulatory clearance, the transaction will close before the fiscal year-end."
                ]
            },
            "listening_task": {
                "audio_text": f"During our board consultation regarding {title_en.lower()}, the directors unanimously approved the allocation of three million dollars to accelerate market expansion, provided that performance metrics are reviewed quarterly.",
                "question": f"What did the board approve regarding {title_en.lower()}?",
                "options": [
                    "Allocation of $3 million for market expansion",
                    "Complete closure of the department",
                    "Immediate salary cuts for all staff",
                    "Postponing all international projects"
                ],
                "ans": "Allocation of $3 million for market expansion",
                "exp": "Audio nêu rõ: 'unanimously approved the allocation of three million dollars to accelerate market expansion'."
            },
            "speaking_prompt": {
                "target_sentence": f"We are prepared to finalize the commercial terms for {title_en.lower()}, provided that our mutual exclusivity rights are upheld.",
                "ipa_focus": "/prəˈpaɪəd tuː ˈfaɪnəlaɪz ðə kəˈmɜːrʃl tɜːrmz/",
                "tips": "Giữ phong thái đĩnh đạc, tự tin; ngắt nghỉ rõ ràng giữa các vế điều kiện thương mại."
            },
            "writing_task": {
                "prompt": f"Viết email thương mại trang trọng (3 câu) gửi đối tác liên quan đến chuyên đề: {title_vi}.",
                "hint": "I would like to formalize our agreement regarding... Could you please confirm the terms of... Looking forward to a mutually beneficial partnership.",
                "sample_answer": f"I am writing to formalize our discussion regarding {title_en.lower()} and confirm the agreed delivery milestones. Please review the attached contract draft and let us know if any clauses require further alignment. We look forward to our mutually beneficial collaboration."
            },
            "dialogue": [
                {"speaker": "Executive VP", "text": f"Have we finalized the strategic risk assessment for our {title_en.lower()} initiative?"},
                {"speaker": "Commercial Director", "text": "Yes, all legal clauses and financial due diligence checks have been thoroughly verified."},
                {"speaker": "Executive VP", "text": "Excellent. Let us proceed with signing the definitive agreement this Friday."}
            ],
            "practice_quiz": [
                {
                    "q": f"Which term best describes the process of evaluating risks and financial health in {title_en.lower()}?",
                    "options": ["Due Diligence", "Casual Chat", "Random Guessing", "Unregulated Trading"],
                    "ans": "Due Diligence",
                    "exp": "'Due Diligence' (thẩm định chuyên sâu) là bước bắt buộc để đánh giá mọi rủi ro tài chính và pháp lý."
                },
                {
                    "q": "Which expression demonstrates the most polite and diplomatic tone in business correspondence?",
                    "options": [
                        "We would be grateful if you could confirm your availability at your earliest convenience.",
                        "Reply to my email right now.",
                        "Why haven't you signed the contract yet?",
                        "Hurry up with the paperwork."
                    ],
                    "ans": "We would be grateful if you could confirm your availability at your earliest convenience.",
                    "exp": "Mẫu câu 'We would be grateful if you could...' thể hiện văn phong ngoại giao chuẩn mực trong giao dịch quốc tế."
                }
            ]
        }
        modules.append(mod)
    return modules


# ═══════════════════════════════════════════════════════════════════════════════
# 2. 30 TECH & AI MODULES (Full 8-Stage Omni-Method Studio Data)
# ═══════════════════════════════════════════════════════════════════════════════

TECH_MODULE_TOPICS = [
    ("Họp Agile Daily Standup, Sprint Planning & Quy Trình Jira", "Agile Standups, Sprint Ceremonies & Jira Backlog Grooming"),
    ("Thiết Kế Kiến Trúc Hệ Thống Phân Tán, High Availability & Scalability", "Distributed System Architecture, High Availability & Scalability"),
    ("Kiến Trúc Microservices, API Gateway, RESTful & GraphQL Protocols", "Microservices Design, API Gateways, RESTful & GraphQL Protocols"),
    ("Mô Hình Ngôn Ngữ Lớn (LLMs), Transformer Architecture & Cơ Chế Attention", "Large Language Models (LLMs), Transformer Architecture & Self-Attention"),
    ("Kỹ Nghệ Câu Lệnh Prompt Engineering, In-Context Learning & CoT", "Prompt Engineering Techniques, Few-Shot & Chain-of-Thought Reasoning"),
    ("Kiến Trúc RAG (Retrieval-Augmented Generation) & Cơ Sở Dữ Liệu Vector", "RAG Pipelines, Semantic Embeddings & Vector Database Indexing"),
    ("Quy Trình Tự Động Hóa CI/CD Pipelines, GitHub Actions & Testing TDD", "CI/CD Automation Pipelines, GitHub Actions & Test-Driven Development"),
    ("Docker Containerization, Kubernetes Orchestration & Helm Charts", "Docker Containerization, Kubernetes Cluster Management & Helm Charts"),
    ("Cơ Sở Dữ Liệu Quan Hệ vs NoSQL, Sharding, Replicas & Tối Ưu Truy Vấn", "Relational vs NoSQL Databases, Database Sharding & Query Optimization"),
    ("Hàng Đợi Thông Điệp Bất Đồng Bộ, Kafka Streams & Event-Driven Systems", "Asynchronous Messaging, Apache Kafka Streams & Event-Driven Architectures"),
    ("Điện Toán Đám Mây AWS/GCP/Azure, Serverless & Infrastructure as Code (IaC)", "Cloud Computing (AWS/GCP), Serverless Lambda & Terraform IaC"),
    ("An Ninh Mạng, Mô Hình Zero-Trust, Mã Hóa & Kiểm Thử Xâm Nhập (Pentest)", "Cybersecurity Architecture, Zero-Trust Frameworks & Penetration Testing"),
    ("Giao Thức Xác Thực OAuth 2.0, JWT Tokens, RBAC & Single Sign-On (SSO)", "OAuth 2.0 Authorization, JWT Tokens, RBAC Security & Enterprise SSO"),
    ("Quy Trình MLOps, Huấn Luyện Mô Hình, Model Drift & Feature Stores", "MLOps Pipelines, Model Training, Data Drift & Enterprise Feature Stores"),
    ("Mạng Nơ-ron Học Sâu (Deep Learning), CNN, RNN & Diffusion Models", "Deep Learning Architectures, Computer Vision CNNs & Diffusion Models"),
    ("Văn Hóa Review Mã Nguồn (Code Review), Chiến Lược Git Branch & Pull Requests", "Code Review Etiquette, Git Flow Strategies & Pull Request Collaboration"),
    ("Xử Lý Sự Cố Production (Incident Triage), RCA & Họp Rút Kinh Nghiệm", "Production Incident Triage, Blameless Postmortems & Root Cause Analysis"),
    ("Khả Năng Quan Sát Hệ Thống (Observability), OpenTelemetry & Prometheus/Grafana", "System Observability, Distributed Tracing (OpenTelemetry) & Grafana"),
    ("Giao Thức Truyền Phát Thời Gian Thực: WebSockets, WebRTC & gRPC Streaming", "Real-Time Streaming Protocols: WebSockets, WebRTC & gRPC Services"),
    ("Kỹ Thuật Dữ Liệu Lớn (Data Engineering), ETL Pipelines, Spark & Snowflake", "Big Data Engineering, Distributed ETL Pipelines, Apache Spark & Snowflake"),
    ("Kiến Trúc Ứng Dụng Di Động Đa Nền Tảng (React Native, Flutter) & Mobile SDKs", "Cross-Platform Mobile Architecture (React Native/Flutter) & Native SDKs"),
    ("Tối Ưu Hiệu Năng Frontend, Core Web Vitals, SSR & React Server Components", "Frontend Performance Engineering, Core Web Vitals & Server Components"),
    ("Căn Chỉnh Mô Hình AI An Toàn (AI Safety), RLHF & Direct Preference Optimization", "AI Safety Alignment, Reinforcement Learning from Human Feedback (RLHF)"),
    ("Tìm Kiếm Ngữ Nghĩa (Vector Search), Cosine Similarity, HNSW & Reranking", "Semantic Search Algorithms, Cosine Similarity, HNSW & Cross-Encoder Reranking"),
    ("Điện Toán Biên (Edge Computing), Thiết Bị Nhúng IoT & Tối Ưu TensorRT", "Edge AI Computing, Embedded IoT Systems & TensorRT Model Quantization"),
    ("Giao Thức Chuỗi Khối (Blockchain), Hợp Đồng Thông Minh Solidity & Web3 Security", "Blockchain Architecture, Smart Contract Security & Decentralized Protocols"),
    ("Kỹ Thuật Hỗn Loạn (Chaos Engineering), Cơ Chế Circuit Breakers & Chịu Lỗi", "Chaos Engineering, Circuit Breaker Resilience & Fault Tolerance"),
    ("Quản Lý Nợ Kỹ Thuật (Technical Debt), Tái Cấu Trúc & Clean Code Principles", "Technical Debt Remediation, Legacy Code Refactoring & Clean Architecture"),
    ("Hệ Thống Tác Nhân Tự Trị (Autonomous AI Agents), LangChain, AutoGen & MCP", "Autonomous AI Agents, Tool Calling Protocols, LangChain & AutoGen"),
    ("Năng Lực Lãnh Đạo Kỹ Thuật (Tech Lead), RFCs & Quyết Định Kiến Trúc Phần Mềm", "Tech Lead Leadership, Architecture RFCs & Engineering Roadmaps")
]

def generate_tech_modules():
    modules = []
    for idx, (title_vi, title_en) in enumerate(TECH_MODULE_TOPICS, start=1):
        mod = {
            "id": f"tech-m{idx}",
            "title": f"Bài {idx}: {title_vi}",
            "description": f"Chuyên đề kỹ thuật chuyên sâu: {title_en}. Làm chủ thuật ngữ IT/AI, kiến trúc hệ thống, báo cáo kỹ thuật, PR description và giải pháp tối ưu hóa.",
            "duration_min": 35,
            "xp": 115 + (idx % 10) * 2,
            "theory": f"Trong kỷ nguyên AI và điện toán phân tán, làm chủ chuyên đề '{title_en}' giúp các kỹ sư phần mềm, AI researcher và Tech Lead truyền đạt giải pháp kỹ thuật chính xác, súc tích và thuyết phục trong các diễn đàn kiến trúc quốc tế.",
            "key_vocab": [
                {"word": "Scalability", "ipa": "/ˌskeɪləˈbɪləti/", "meaning": "Khả năng mở rộng tải của hệ thống", "example": "Our microservices architecture ensures horizontal scalability under high concurrency."},
                {"word": "Latency", "ipa": "/ˈleɪtnsi/", "meaning": "Độ trễ phản hồi của mạng / API", "example": "We optimized our vector database indexing to reduce search latency to under 15ms."},
                {"word": "Deployment", "ipa": "/dɪˈplɔɪmənt/", "meaning": "Sự triển khai phần mềm lên máy chủ", "example": "The automated CI/CD pipeline enables zero-downtime production deployments."},
                {"word": "Idempotent", "ipa": "/aɪˈdempətənt/", "meaning": "Tính bất biến khi thực thi lặp (API)", "example": "All financial transaction endpoints must be strictly idempotent to prevent duplicate charges."},
                {"word": "Asynchronous", "ipa": "/eɪˈsɪŋkrənəs/", "meaning": "Xử lý bất đồng bộ không chặn luồng", "example": "We use asynchronous task workers with Redis queues to process background jobs."},
                {"word": "Refactor", "ipa": "/ˌriːˈfæktər/", "meaning": "Tái cấu trúc mã nguồn nâng cao độ sạch", "example": "We plan to refactor this legacy monolith into modular microservices."},
                {"word": "Quantization", "ipa": "/ˌkwɑːntɪˈzeɪʃn/", "meaning": "Lượng tử hóa giảm dung lượng mô hình AI", "example": "Model quantization from FP16 to INT8 reduces GPU VRAM consumption by 50%."},
                {"word": "Throughput", "ipa": "/ˈθruːpʊt/", "meaning": "Băng thông / Lưu lượng xử lý đồng thời", "example": "The distributed Kafka broker increased overall event throughput to 100k requests/sec."}
            ],
            "grammar_point": {
                "rule": f"Cấu trúc diễn đạt nguyên nhân & hiệu quả kỹ thuật bài {idx}: Causative & Optimization Patterns",
                "formula": "By implementing X, we reduced / improved Y by Z% | The root cause was identified as X, leading to Y",
                "examples": [
                    "By deploying an asynchronous caching layer with Redis, we reduced database query latency by 65%.",
                    "The intermittent service degradation was caused by a memory leak in the WebSocket connection pool."
                ]
            },
            "listening_task": {
                "audio_text": f"In our architectural review of {title_en.lower()}, we benchmarked our distributed service across three cloud regions and observed that response latency dropped from one hundred twenty milliseconds to thirty-five milliseconds after enabling HTTP/3 and edge caching.",
                "question": f"What was the observed latency improvement in the review?",
                "options": [
                    "Dropped from 120ms to 35ms",
                    "Increased to over 500ms",
                    "Remained completely unchanged",
                    "All servers crashed during testing"
                ],
                "ans": "Dropped from 120ms to 35ms",
                "exp": "Audio nêu rõ: 'latency dropped from one hundred twenty milliseconds to thirty-five milliseconds'."
            },
            "speaking_prompt": {
                "target_sentence": f"Yesterday I completed the backend implementation for {title_en.lower()}, and today I am writing automated integration tests before deploying to staging.",
                "ipa_focus": "/ˈkəmpiːtɪd ðə ˌbækˈend ˌɪmplɪmenˈteɪʃn/",
                "tips": "Phát âm dứt khoát các thuật ngữ chuyên ngành công nghệ (integration tests, staging environment)."
            },
            "writing_task": {
                "prompt": f"Viết mô tả Pull Request (PR Description - 3 câu) tóm tắt tính năng bạn vừa phát triển cho chuyên đề: {title_vi}.",
                "hint": "This PR implements... It addresses issue #... All unit and end-to-end tests have passed successfully.",
                "sample_answer": f"This PR implements the core functionality for {title_en.lower()} by introducing an optimized async pipeline. It resolves issue #284 and reduces memory overhead by 40% under peak load. All automated unit and end-to-end tests have passed with 100% code coverage."
            },
            "dialogue": [
                {"speaker": "Lead Architect", "text": f"How is the performance benchmarking for our {title_en.lower()} pipeline?"},
                {"speaker": "Senior Engineer", "text": "We successfully deployed the canary build, and inference throughput has increased by nearly 3x with zero errors."},
                {"speaker": "Lead Architect", "text": "Outstanding work! Let us schedule the full production rollout for tonight's maintenance window."}
            ],
            "practice_quiz": [
                {
                    "q": f"What is the primary benefit of applying optimization techniques in {title_en.lower()}?",
                    "options": ["Minimizing latency and maximizing system throughput", "Increasing server cost needlessly", "Stopping all unit testing", "Making code impossible to maintain"],
                    "ans": "Minimizing latency and maximizing system throughput",
                    "exp": "Mục tiêu tối thượng của tối ưu hóa kỹ thuật là giảm thiểu độ trễ (latency) và tối đa hóa năng lực xử lý đồng thời (throughput)."
                },
                {
                    "q": "What does the term 'Idempotency' guarantee in API architecture?",
                    "options": [
                        "Making multiple identical requests has the same effect as making a single request",
                        "The server restarts on every request",
                        "The database deletes all records",
                        "The user password is changed"
                    ],
                    "ans": "Making multiple identical requests has the same effect as making a single request",
                    "exp": "'Idempotency' (tính bất biến) đảm bảo việc gọi lặp lại cùng một request không gây ra tác dụng phụ ngoài ý muốn (ví dụ trừ tiền hai lần)."
                }
            ]
        }
        modules.append(mod)
    return modules


# ═══════════════════════════════════════════════════════════════════════════════
# 3. GENERATE 30 EXAM BANK TESTS FOR BUSINESS AND TECH
# ═══════════════════════════════════════════════════════════════════════════════

def generate_business_30_tests():
    tests = []
    for t_idx in range(1, 31):
        questions = []
        for q_idx in range(1, 31):
            topic_pair = BUSINESS_MODULE_TOPICS[(t_idx + q_idx) % len(BUSINESS_MODULE_TOPICS)]
            topic_title = topic_pair[0]
            questions.append({
                "id": f"BIZ_{t_idx}_Q{q_idx}",
                "question": f"[Business BIZ Test {t_idx} • Q{q_idx}]\nRegarding {topic_title.lower()}: The board decided to _____ the supplier contract due to consistent delivery delays.",
                "options": [
                    "terminate",
                    "celebrate",
                    "decorate",
                    "vacate"
                ],
                "correct": "terminate",
                "explanation": "'Terminate a contract' là thuật ngữ chuẩn mang nghĩa chấm dứt/hủy hợp đồng."
            })
        tests.append({
            "test_id": f"biz-test-{t_idx}",
            "test_number": t_idx,
            "title": f"Đề Thi {t_idx}: Đề Thi Chuẩn Hóa Tiếng Anh Thương Mại Quốc Tế (Business Practice Test {t_idx})",
            "level": "BUSINESS",
            "time_min": 35,
            "pass_score": 75,
            "total_questions": 30,
            "questions": questions
        })
    return tests

def generate_tech_30_tests():
    tests = []
    for t_idx in range(1, 31):
        questions = []
        for q_idx in range(1, 31):
            topic_pair = TECH_MODULE_TOPICS[(t_idx + q_idx) % len(TECH_MODULE_TOPICS)]
            topic_title = topic_pair[0]
            questions.append({
                "id": f"TECH_{t_idx}_Q{q_idx}",
                "question": f"[Tech & AI Test {t_idx} • Q{q_idx}]\nRegarding {topic_title.lower()}: We must configure the API gateway to _____ incoming traffic when the backend service reaches 90% CPU utilization.",
                "options": [
                    "throttle",
                    "inflate",
                    "disregard",
                    "delete"
                ],
                "correct": "throttle",
                "explanation": "'Throttle traffic' là thuật ngữ kỹ thuật chỉ việc điều tiết/giới hạn lưu lượng truy cập để bảo vệ hệ thống."
            })
        tests.append({
            "test_id": f"tech-test-{t_idx}",
            "test_number": t_idx,
            "title": f"Đề Thi {t_idx}: Đề Thi Chuẩn Hóa Tiếng Anh Chuyên Ngành CNTT & AI (Tech & AI Practice Test {t_idx})",
            "level": "TECH",
            "time_min": 35,
            "pass_score": 75,
            "total_questions": 30,
            "questions": questions
        })
    return tests

BUSINESS_EXTENDED_MODULES = generate_business_modules()
TECH_EXTENDED_MODULES = generate_tech_modules()
BUSINESS_EXAM_BANK_30 = generate_business_30_tests()
TECH_EXAM_BANK_30 = generate_tech_30_tests()
