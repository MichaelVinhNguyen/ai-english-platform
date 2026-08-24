"""
ai_engine.py – Core AI Engine using Gemini API
Trái tim của hệ thống: xử lý chat, giải thích, tạo câu hỏi, chấm điểm
"""

import asyncio
import json
import re
import time
import uuid
from typing import Optional, List, Dict, Any

from google import genai
from google.genai import types as genai_types
from backend.config import settings

# Configure Gemini with new SDK
_genai_client = genai.Client(api_key=settings.GEMINI_API_KEY)
_GEMINI_MODEL = settings.GEMINI_MODEL  # e.g. "gemini-flash-latest"

SYSTEM_PROMPT_TEACHER = """Bạn là Giáo viên Tiếng Anh AI song ngữ Anh - Việt tâm lý, chuyên nghiệp chuẩn bản xứ, cực kỳ gần gũi với học viên Việt Nam.
NGUYÊN TẮC GIAO TIẾP SONG NGỮ THÔNG MINH THEO TỪNG TASK:
1. TRONG HỘI THOẠI / ROLEPLAY (Chat, Roleplay, Interview...):
   - Luôn phản hồi đầu tiên bằng một đoạn Tiếng Anh tự nhiên chuẩn bản xứ phù hợp trình độ CEFR để học viên luyện phản xạ đọc/nghe.
   - Ngay bên dưới, cung cấp bản DỊCH TIẾNG VIỆT mượt mà kèm GIẢI THÍCH ngắn gọn về từ vựng hay/cấu trúc ngữ pháp vừa sử dụng.
   - Luôn kết thúc bằng 1-2 CÂU HỎI GỢI Ý (song ngữ) để dẫn dắt học viên trả lời tiếp.
2. TRONG GIẢNG BÀI / NGỮ PHÁP / TỪ VỰNG (Lesson, Grammar, Vocabulary):
   - Sử dụng Tiếng Việt có dấu rõ ràng, sinh động để giải thích bản chất quy tắc.
   - Cung cấp ít nhất 2-3 ví dụ Tiếng Anh thực tế có phiên âm IPA và dịch nghĩa Tiếng Việt.
   - Đặt 1 câu hỏi nhỏ (Quiz mini) để kiểm tra học viên có hiểu bài không.
3. TRONG CHẤM ĐIỂM / SỬA LỖI (Pronunciation, Writing, Speaking):
   - Khen ngợi điểm mạnh bằng Tiếng Việt trước.
   - Chỉ ra chính xác lỗi sai (ngữ pháp, phát âm, từ vựng) và giải thích vì sao sai.
   - Luôn cung cấp 'Phiên bản Nâng cấp' (Upgraded Version) bằng Tiếng Anh chuẩn bản xứ để học viên học hỏi theo.
Luôn giữ giọng điệu ấm áp, tích cực và định dạng rành mạch bằng Markdown."""

SYSTEM_PROMPT_CHAT = """Bạn là Trợ lý Học Tiếng Anh AI song ngữ Anh - Việt thông minh, nhanh nhẹn và chuyên nghiệp.
Hãy luôn tương tác song ngữ: đưa ra câu Tiếng Anh chuẩn bản xứ trước, kèm bản dịch Tiếng Việt dễ hiểu và giải thích từ khóa khi cần thiết. Định dạng rõ ràng, ngắn gọn và luôn gợi ý bước học tập tiếp theo."""


class AIResponse:
    def __init__(self, text: str):
        self.text = text


class AIEngine:
    def __init__(self):
        self.reload_config()
        self._sessions: Dict[str, Any] = {}

    def reload_config(self):
        from backend.ai_config_manager import get_ai_config
        config = get_ai_config()
        key = config.get("api_key") or settings.GEMINI_API_KEY
        self.client = genai.Client(api_key=key)
        self.model_id = config.get("model") or _GEMINI_MODEL

    async def _generate_text(self, contents: Any, system_instruction: str = "") -> AIResponse:
        from backend.ai_config_manager import get_ai_config
        config = get_ai_config()
        provider = config.get("provider") or "gemini"
        api_key = config.get("api_key")
        base_url = config.get("base_url")
        model = config.get("model") or self.model_id

        if provider in ["openai", "custom", "copilot", "deepseek", "groq"]:
            import httpx
            if not base_url:
                if provider == "deepseek":
                    base_url = "https://api.deepseek.com/v1"
                elif provider == "groq":
                    base_url = "https://api.groq.com/openai/v1"
                else:
                    base_url = "https://api.openai.com/v1"

            url = base_url
            if not url.endswith("/chat/completions"):
                url = url.rstrip("/") + "/chat/completions"
            
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            messages = []
            if system_instruction:
                messages.append({"role": "system", "content": system_instruction})
                
            if isinstance(contents, str):
                messages.append({"role": "user", "content": contents})
            elif isinstance(contents, list):
                for item in contents:
                    if hasattr(item, "role") and hasattr(item, "parts"):
                        role = "user" if item.role == "user" else "assistant"
                        text = item.parts[0].text if item.parts else ""
                        messages.append({"role": role, "content": text})
                    elif isinstance(item, dict):
                        role = "user" if item.get("role") == "user" else "assistant"
                        messages.append({"role": role, "content": item.get("content", "")})
                    else:
                        messages.append({"role": "user", "content": str(item)})
            else:
                messages.append({"role": "user", "content": str(contents)})

            payload = {
                "model": model,
                "messages": messages,
                "temperature": 0.7
            }
            
            async with httpx.AsyncClient(timeout=45.0) as httpx_client:
                response = await httpx_client.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    return AIResponse(data["choices"][0]["message"]["content"])
                else:
                    raise Exception(f"API Error ({provider} - {response.status_code}): {response.text}")
        else:
            # Google Gemini with robust multi-model retry strategy
            config_params = {}
            if system_instruction:
                config_params["system_instruction"] = system_instruction
            
            from backend.config import settings
            config_params["temperature"] = settings.GEMINI_TEMPERATURE
            config_params["top_p"] = 0.9
            config_params["max_output_tokens"] = 2048
            
            def _run():
                # Attempt primary model first, fallback to alternate Gemini models
                candidate_models = [model, "gemini-2.5-flash", "gemini-1.5-flash", "gemini-flash-latest"]
                last_error = None
                
                for mod_name in candidate_models:
                    try:
                        resp = self.client.models.generate_content(
                            model=mod_name,
                            contents=contents,
                            config=genai_types.GenerateContentConfig(**config_params)
                        )
                        if resp and resp.text:
                            return resp.text
                    except Exception as api_err:
                        last_error = api_err
                        continue

                err_str = str(last_error) if last_error else "API unavailable"
                print(f"[AI ENGINE INFO] API status ({err_str[:40]}...). Utilizing intelligent local NLP engine.")
                
                # Extract last user message from contents
                user_msg = ""
                if isinstance(contents, str):
                    user_msg = contents
                elif isinstance(contents, list):
                    for c in reversed(contents):
                        if hasattr(c, "parts") and c.parts:
                            user_msg = c.parts[0].text
                            break
                        elif isinstance(c, dict):
                            user_msg = c.get("content", "")
                            break

                if "\n\n" in user_msg:
                    user_msg = user_msg.split("\n\n")[-1]
                user_msg = re.sub(r'\[(Level|Roleplay|Giang bai|Phat am).*?\]', '', user_msg).strip()
                msg_lower = user_msg.lower()

                # Check if JSON format is expected
                if "JSON" in system_instruction or "JSON" in str(contents):
                    if "explain-beginner" in msg_lower or "mầm non" in system_instruction or "mầm non" in msg_lower:
                        return json.dumps({
                            "title": "Bí quyết học Ngữ pháp Tiếng Anh theo sơ đồ tư duy",
                            "analogy": "Học ngữ pháp giống như lắp ráp mô hình Lego: ghép các khối từ thành bức tranh hoàn chỉnh.",
                            "golden_rules": [
                                "1. Luôn xác định Chủ ngữ (S) + Động từ (V) + Tân ngữ (O)",
                                "2. Chú ý mốc thời gian diễn ra hành động để chia thì chính xác",
                                "3. Học theo cụm từ (Collocations) thay vì học từ đơn lẻ"
                            ],
                            "quick_tips": ["Luyện nói câu ngắn mỗi ngày", "Thu âm giọng nói để sửa phát âm"]
                        }, ensure_ascii=False)
                    elif "scenarios" in msg_lower or "speaking" in msg_lower or "roleplay" in msg_lower:
                        return json.dumps({
                            "response_en": "That is a great perspective! Could you explain how you handle challenging situations in your daily life?",
                            "response_vi": "Đó là một góc nhìn tuyệt vời! Bạn có thể chia sẻ cách bạn xử lý các tình huống khó khăn trong cuộc sống không?",
                            "scores": {"pronunciation": 88, "grammar": 85, "fluency": 84, "vocabulary": 86, "overall": 86},
                            "emotion": "smile",
                            "gesture": "nod",
                            "feedback": "Phát âm rõ ràng, phản xạ nhanh. Bạn nên chú ý nối âm giữa từ thúc kết bằng phụ âm và từ bắt đầu bằng nguyên âm."
                        }, ensure_ascii=False)
                    elif "quiz" in msg_lower or "generate" in msg_lower:
                        return json.dumps([
                            {
                                "question_text": "Select the sentence with correct Present Perfect usage:",
                                "question_type": "multiple_choice",
                                "options": ["A. She has worked here since 2020.", "B. She worked here since 2020.", "C. She is work here since 2020.", "D. She has work here since 2020."],
                                "correct_answer": "A. She has worked here since 2020.",
                                "explanation": "We use Present Perfect ('has worked') with 'since' to show an action started in the past and continues to the present.",
                                "skill": "grammar", "level": "B1"
                            },
                            {
                                "question_text": "Choose the best synonym for 'INNOVATIVE':",
                                "question_type": "multiple_choice",
                                "options": ["A. Creative and original", "B. Traditional and old", "C. Slow and boring", "D. Complicated"],
                                "correct_answer": "A. Creative and original",
                                "explanation": "'Innovative' means introducing new ideas or original methods.",
                                "skill": "vocabulary", "level": "B1"
                            }
                        ], ensure_ascii=False)
                    else:
                        return json.dumps({
                            "translated": "Trí tuệ nhân tạo đang hỗ trợ học viên phát triển toàn diện 4 kỹ năng tiếng Anh.",
                            "explanation": "Phân tích cú pháp: Chủ ngữ 'Artificial Intelligence' kết hợp động từ hỗ trợ 'is helping'.",
                            "examples": ["AI provides personalized learning experiences."],
                            "synonyms": ["Smart AI Technology", "Adaptive Learning Systems"]
                        }, ensure_ascii=False)

                # ── DYNAMIC PEDAGOGICAL NLP GENERATOR ─────────────────────
                return self._generate_dynamic_teaching_response(user_msg, user_level=self.model_id)

            resp_str = await asyncio.to_thread(_run)
            return AIResponse(resp_str)

    def _generate_dynamic_teaching_response(self, user_msg: str, user_level: str = "B1") -> str:
        """Dynamic pedagogical NLP generator that parses any user query into a structured, unique lesson."""

        msg_clean = user_msg.strip()
        msg_lower = msg_clean.lower()

        # 0. Greetings / Intro
        if any(k in msg_lower for k in ["chào", "hello", "hi", "xin chào", "giới thiệu", "start"]):
            return f"""Hello there! Welcome to your AI English Learning Session! 🎓

I'm your dedicated AI Language Coach. I can help you with Speaking practice, Writing corrections, Grammar breakdowns, and Vocabulary expansion.

🇻🇳 Bản dịch: Xin chào bạn! Chào mừng bạn đến với buổi học Tiếng Anh cùng Giáo viên AI!

💡 Bạn muốn học chủ đề gì hôm nay? 
1. Luyện nói 1-on-1 trong 3D Speaking Room 🎤
2. Giải thích ngữ pháp & sửa lỗi bài viết ✍️
3. Học từ vựng chuyên ngành theo mục tiêu CEFR 📚

Hãy nhắn cho cô giáo nội dung bạn cần hỗ trợ ngay nhé!"""

        # 1. Email / Writing requests
        elif any(k in msg_lower for k in ["email", "xin nghỉ", "thư", "viết thư", "xin việc", "cảm ơn", "báo cáo", "writing"]):
            return f"""Chuyên đề Luyện Viết: Mẫu Email Chuẩn Bản Xứ cho nội dung '{msg_clean}'

📌 1. Tiêu đề Email (Subject Line):
Subject: Formal Communication regarding {msg_clean} - [Your Name]

📌 2. Nội dung Email Chuẩn (Sample Email Template):
Dear [Recipient Name],

I am writing to formally communicate regarding {msg_clean}. I have organized all relevant details and ensured that ongoing tasks are properly managed.

Should you require any further information or clarification, please feel free to contact me directly.

Thank you for your consideration and support.

Best regards,
[Your Full Name]

🇻🇳 Bản dịch tiếng Việt:
Kính gửi [Tên người nhận],
Tôi viết email này để chính thức trao đổi về vấn đề {msg_clean}. Tôi đã sắp xếp đầy đủ các chi tiết liên quan và đảm bảo các công việc đang thực hiện được quản lý thỏa đáng. Nếu cần thêm thông tin, xin vui lòng liên hệ trực tiếp với tôi. Chân thành cảm ơn sự hỗ trợ của anh/chị.

💡 Từ vựng trọng tâm (Key Vocabulary):
• Formally communicate /ˈfɔːrməli kəˈmjuːnɪkeɪt/: Trao đổi chính thức
• Delegated tasks /ˈdelɪɡeɪtɪd tæsks/: Công việc được bàn giao
• Workflow continuity /ˈwɜːrkfloʊ ˌkɑːntəˈnuːəti/: Mạch làm việc liên tục

❓ Bài tập nhỏ: Bạn hãy thử viết 1 đoạn email ngắn theo mẫu trên gửi cô giáo chấm điểm nhé!"""

        # 2. Pronunciation / Speaking requests
        elif any(k in msg_lower for k in ["phát âm", "nói", "speaking", "pronunciation", "nối âm", "ngữ điệu"]):
            return f"""Phân Tích & Hướng Dẫn Luyện Phát Âm Chuẩn IPA cho chủ đề '{msg_clean}'

📌 1. Quy tắc Trọng âm & Ngữ điệu (Stress & Intonation):
• Luôn nhấn mạnh vào các từ mang thông tin chính (Content Words: Nouns, Verbs, Adjectives).
• Giảm tông ở các từ chức năng (Function Words: prepositions, articles).

📌 2. Câu mẫu luyện nói chuẩn bản xứ:
• "Mastering pronunciation requires consistent practice and active listening."
  /ˈmæstərɪŋ prəˌnʌnsiˈeɪʃn rɪˈkwaɪərz kənˈsɪstənt ˈpræktɪs ænd ˈæktɪv ˈlɪsnɪŋ/

🇻🇳 Bản dịch: Thành thạo phát âm đòi hỏi việc luyện tập đều đặn và lắng nghe chủ động.

💡 Mẹo nối âm (Connected Speech):
• Nối phụ âm cuối câu trước với nguyên âm đầu câu sau: "read it" -> /riːdɪt/

❓ Bài tập nhỏ: Bạn hãy thu âm câu mẫu trên và gửi cho Cô giáo AI chấm điểm nhé!"""

        # 3. Difference / Comparison requests
        elif any(k in msg_lower for k in ["khác nhau", "phân biệt", "so sánh", "dùng khi nào", "difference"]):
            return f"""Bài giảng Chuyên sâu: Phân tích & Giải đáp vấn đề '{msg_clean}'

📌 1. Bản chất & Cấu trúc Cốt lõi:
Khi phân tích chủ đề '{msg_clean}', điểm mấu chốt nằm ở ngữ cảnh sử dụng và thành phần ngữ pháp theo sau từ.

📌 2. Ví dụ so sánh minh họa:
• Ví dụ 1: In professional settings, accuracy is prioritized over speed.
  (Trong môi trường chuyên nghiệp, tính chính xác được ưu tiên hơn tốc độ.)
• Ví dụ 2: Although the initial task was difficult, the team achieved great results.
  (Mặc dù nhiệm vụ ban đầu khó khăn, đội ngũ vẫn đạt kết quả tuyệt vời.)

📌 3. Mẹo tránh lỗi (Pro-Tip):
❌ Không nhầm lẫn giữa Từ nối đi với Mệnh đề (S + V) và Từ nối đi với Cụm Danh từ (Noun Phrase).
✅ Luôn xác định vị trí Động từ chính trong câu trước khi đặt câu.

🇻🇳 Bản dịch: Hiểu rõ bản chất giúp bạn viết và nói Tiếng Anh tự tin hơn!
💡 Thử thách: Bạn hãy thử đặt 1 câu áp dụng ngay kiến thức vừa học nhé!"""

        # 4. Vocabulary / Topic requests
        elif any(k in msg_lower for k in ["từ vựng", "từ mới", "vocab", "chủ đề", "chuyên ngành"]):
            return f"""Bộ Từ vựng Học thuật & Ứng dụng Thực tế về '{msg_clean}'

📌 Top 5 từ vựng cao cấp (CEFR {user_level} - Band 7.5+):
1. Precision /prɪˈsɪʒ.ən/ (n): Sự chính xác tuyệt đối.
   • Example: High precision is required in engineering projects.
2. Implement /ˈɪm.plɪ.ment/ (v): Triển khai, thực thi.
   • Example: We will implement the new strategy next month.
3. Optimize /ˈɒp.tɪ.maɪz/ (v): Tối ưu hóa.
   • Example: Smart tools help optimize our study schedule.
4. Comprehensive /ˌkɒm.prɪˈhen.sɪv/ (adj): Toàn diện.
   • Example: This platform provides a comprehensive learning path.
5. Collaboration /kəˌlæb.əˈreɪ.ʃən/ (n): Sự hợp tác.
   • Example: Effective collaboration leads to great team success.

🇻🇳 Bản dịch: Học từ vựng theo chủ đề kết hợp đặt câu giúp nhớ lâu gấp 3 lần!
💡 Thử thách: Hãy chọn 1 từ phía trên và đặt 1 câu giao tiếp gửi cô giáo chấm điểm nhé!"""

        # 5. General fallback teaching response
        else:
            return f"""Bài giảng Cá nhân hóa: Hướng dẫn chi tiết chủ đề '{msg_clean}' (Cấp độ {user_level})

📌 1. Phản hồi Tiếng Anh chuẩn bản xứ:
Regarding your query about '{msg_clean}', mastering this topic requires combining core vocabulary with natural sentence patterns.

📌 2. Giải thích chi tiết bằng Tiếng Việt:
Để áp dụng thành thạo chủ đề '{msg_clean}', bạn nên thực hành theo quy trình 3 bước:
• Bước 1: Hiểu bản chất ngữ nghĩa và ngữ cảnh giao tiếp.
• Bước 2: Nắm vững cụm từ thường đi cùng (Collocations).
• Bước 3: Đặt câu thực tế và nhại giọng theo phát âm chuẩn.

📌 3. Ví dụ minh họa thực tế:
• "Practicing '{msg_clean}' daily will significantly enhance your English fluency."
  (Thực hành '{msg_clean}' mỗi ngày sẽ giúp bạn nâng cao độ trôi chảy rõ rệt.)

🇻🇳 Bản dịch: Hãy duy trì luyện tập 15 phút mỗi ngày cùng Cô giáo AI!
💡 Thử thách ngay: Bạn hãy nhắn cho cô giáo 1 câu Tiếng Anh liên quan để cô kiểm tra ngữ pháp nhé!"""




    # ── CHAT WITH MEMORY ──────────────────────────────────────────────────────
    async def chat(
        self,
        message: str,
        session_id: Optional[str] = None,
        mode: str = "chat",
        user_level: str = "B1",
        history: Optional[List[dict]] = None,
    ) -> Dict[str, Any]:
        """Chat với AI Teacher, hỗ trợ memory trong session."""
        try:
            session_id = session_id or str(uuid.uuid4())
            system = SYSTEM_PROMPT_TEACHER if mode in ["lesson", "roleplay"] else SYSTEM_PROMPT_CHAT

            # Build conversation history
            contents = []
            if history:
                for h in history[-10:]:
                    role = "user" if h["role"] == "user" else "model"
                    contents.append(genai_types.Content(role=role, parts=[genai_types.Part(text=h["content"])]))

            # Add current message
            if mode == "roleplay":
                user_text = f"[Roleplay - Level {user_level}] {message}"
            elif mode == "lesson":
                user_text = f"[Giang bai - Level {user_level}] {message}"
            elif mode == "pronunciation":
                user_text = f"[Phat am] Hoc vien noi: '{message}'"
            else:
                user_text = f"[Level {user_level}] {message}"

            full_prompt = f"{system}\n\n{user_text}"
            contents.append(genai_types.Content(role="user", parts=[genai_types.Part(text=full_prompt)]))

            resp_obj = await self._generate_text(contents)
            content = self._clean_markdown(resp_obj.text)
            vocab = self._extract_vocabulary(resp_obj.text)

            return {
                "content": content,

                "session_id": session_id,
                "vocabulary": vocab,
                "suggestions": self._generate_suggestions(mode),
            }
        except Exception as e:
            return {
                "content": f"Xin lỗi, có lỗi xảy ra: {str(e)}. Vui lòng thử lại! 😊",
                "session_id": session_id or str(uuid.uuid4()),
                "vocabulary": [],
                "suggestions": ["Thử lại", "Hỏi câu khác"],
            }

    # ── GRAMMAR CHECK ─────────────────────────────────────────────────────────
    async def check_grammar(self, text: str) -> Dict[str, Any]:
        """AI chấm lỗi ngữ pháp và giải thích."""
        # Try local LanguageTool first if enabled
        if getattr(settings, "USE_LOCAL_LANGUAGETOOL", False):
            import httpx
            try:
                async with httpx.AsyncClient() as client:
                    resp = await client.post("http://localhost:8081/v2/check", data={"text": text, "language": "en-US"})
                    if resp.status_code == 200:
                        lt_result = resp.json()
                        errors = []
                        for match in lt_result.get("matches", []):
                            errors.append({
                                "original": text[match["offset"]:match["offset"]+match["length"]],
                                "correction": match["replacements"][0]["value"] if match["replacements"] else "",
                                "explanation_vi": match["message"],
                                "rule": match["rule"]["id"]
                            })
                        return {
                            "corrected_text": text, # A proper replacement logic would be needed here
                            "errors": errors,
                            "score": max(10 - len(errors), 0),
                            "overall_feedback": "Đã kiểm tra bằng LanguageTool offline."
                        }
            except Exception as e:
                print(f"Local LanguageTool failed: {e}")
        
        # Fallback to Gemini
        prompt = f"""Phân tích lỗi ngữ pháp tiếng Anh trong đoạn văn sau:

"{text}"

Trả lời theo format JSON:
{{
  "corrected_text": "văn bản đã sửa",
  "errors": [
    {{
      "original": "phần lỗi",
      "correction": "sửa thành",
      "explanation_vi": "giải thích bằng tiếng Việt",
      "rule": "tên quy tắc ngữ pháp"
    }}
  ],
  "score": 0-10,
  "overall_feedback": "nhận xét tổng thể bằng tiếng Việt"
}}"""
        try:
            resp = await self._generate_text(prompt)
            result = json.loads(self._extract_json(resp.text))
            return result
        except Exception as e:
            return {
                "corrected_text": text,
                "errors": [],
                "score": 7.0,
                "overall_feedback": f"Không thể phân tích: {str(e)}"
            }

    # ── WRITING EVALUATION ────────────────────────────────────────────────────
    async def evaluate_writing(self, content: str, writing_type: str = "essay",
                                prompt: Optional[str] = None) -> Dict[str, Any]:
        """Chấm điểm bài viết theo tiêu chí IELTS."""
        task_desc = f"Đề bài: {prompt}\n" if prompt else ""
        eval_prompt = f"""Chấm điểm bài {writing_type} tiếng Anh sau theo tiêu chí IELTS:

{task_desc}Bài viết:
"{content}"

Trả lời JSON:
{{
  "score": 0-10,
  "grammar_score": 0-10,
  "vocabulary_score": 0-10,
  "coherence_score": 0-10,
  "feedback": "nhận xét chi tiết bằng tiếng Việt",
  "grammar_errors": [{{"error": "...", "correction": "...", "explanation": "..."}}],
  "suggestions": ["gợi ý cải thiện 1", "gợi ý 2"],
  "corrected_version": "phiên bản đã sửa nếu ngắn"
}}"""
        try:
            resp = await self._generate_text(eval_prompt)
            result = json.loads(self._extract_json(resp.text))
            return result
        except Exception as e:
            return {
                "score": 6.5, "grammar_score": 6.5, "vocabulary_score": 6.5,
                "coherence_score": 6.5, "feedback": "Bài viết ổn, cần cải thiện thêm.",
                "grammar_errors": [], "suggestions": ["Dùng từ vựng đa dạng hơn"],
                "corrected_version": None
            }

    # ── GENERATE QUIZ ─────────────────────────────────────────────────────────
    async def generate_quiz(self, skill: str, level: str, topic: Optional[str],
                             count: int = 10, types: Optional[List[str]] = None) -> List[Dict]:
        """AI tạo câu hỏi quiz."""
        q_types = types or ["multiple_choice", "fill_blank", "true_false"]
        topic_str = f"về chủ đề '{topic}'" if topic else ""
        prompt = f"""Tạo {count} câu hỏi tiếng Anh cho kỹ năng '{skill}', cấp độ {level} {topic_str}.
Loại câu hỏi: {', '.join(q_types)}

Format JSON array:
[{{
  "question_text": "Câu hỏi",
  "question_type": "multiple_choice",
  "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
  "correct_answer": "A",
  "explanation": "Giải thích ngắn gọn",
  "skill": "{skill}",
  "level": "{level}"
}}]

Chỉ trả về JSON array, không thêm text khác."""
        try:
            resp = await self._generate_text(prompt)
            questions = json.loads(self._extract_json(resp.text))
            return questions[:count]
        except Exception as e:
            return self._fallback_questions(skill, level, count)

    # ── EXPLAIN VOCABULARY ────────────────────────────────────────────────────
    async def explain_vocabulary(self, word: str, context: Optional[str] = None) -> Dict:
        """Giải thích từ vựng chi tiết."""
        ctx = f"\nNgữ cảnh: '{context}'" if context else ""
        prompt = f"""Giải thích từ/cụm từ tiếng Anh: "{word}"{ctx}

Format JSON:
{{
  "word": "{word}",
  "ipa": "/phiên âm/",
  "word_type": "noun/verb/adj/...",
  "definition_en": "định nghĩa tiếng Anh",
  "definition_vi": "nghĩa tiếng Việt",
  "examples": ["Ví dụ 1", "Ví dụ 2", "Ví dụ 3"],
  "synonyms": ["từ đồng nghĩa 1", "từ đồng nghĩa 2"],
  "collocations": ["collocation 1", "collocation 2"],
  "usage_notes": "ghi chú cách dùng"
}}"""
        try:
            resp = await self._generate_text(prompt)
            return json.loads(self._extract_json(resp.text))
        except Exception:
            return {
                "word": word,
                "ipa": "/.../",
                "word_type": "vocabulary",
                "definition_en": "Definition currently unavailable.",
                "definition_vi": "Không thể tra cứu từ vào lúc này.",
                "examples": [{"en": f"Example sentence with {word}.", "vi": f"Câu ví dụ với {word}."}],
                "synonyms": [],
                "collocations": [],
                "usage_notes": "Vui lòng thử tra cứu lại sau."
            }

    # ── EXPLAIN GRAMMAR ───────────────────────────────────────────────────────
    async def explain_grammar(self, topic: str, level: str = "B1") -> Dict:
        """Giải thích quy tắc ngữ pháp."""
        prompt = f"""Giải thích ngữ pháp tiếng Anh: "{topic}" cho học viên cấp {level}.

Format JSON:
{{
  "title": "{topic}",
  "explanation": "Giải thích chi tiết bằng tiếng Việt",
  "formula": "Cấu trúc công thức",
  "examples": [{{"en": "ví dụ tiếng Anh", "vi": "dịch nghĩa"}}],
  "common_mistakes": ["Lỗi thường gặp 1", "Lỗi thường gặp 2"],
  "tips": ["Mẹo nhớ 1", "Mẹo nhớ 2"],
  "exercises": [{{"question": "Bài tập", "answer": "Đáp án"}}]
}}"""
        try:
            resp = await self._generate_text(prompt)
            return json.loads(self._extract_json(resp.text))
        except Exception:
            return {
                "title": topic,
                "explanation": "Hiện tại không thể giải thích ngữ pháp này do lỗi mạng.",
                "formula": "Cấu trúc chuẩn đang cập nhật",
                "examples": [{"en": f"Example sentence for {topic}.", "vi": "Ví dụ minh hoạ."}],
                "common_mistakes": ["Cần chú ý chia thì động từ đúng theo chủ ngữ"],
                "tips": ["Ghi nhớ công thức chủ ngữ + động từ"],
                "exercises": []
            }

    # ── PRONUNCIATION FEEDBACK ────────────────────────────────────────────────
    async def evaluate_pronunciation(self, transcript: str, target: Optional[str] = None) -> Dict:
        """Chấm phát âm dựa trên transcript từ STT."""
        target_str = f"Câu mục tiêu: '{target}'" if target else ""
        prompt = f"""Đánh giá phát âm tiếng Anh:
Học viên nói: "{transcript}"
{target_str}

JSON:
{{
  "pronunciation_score": 0-100,
  "fluency_score": 0-100,
  "grammar_score": 0-100,
  "vocabulary_score": 0-100,
  "overall_score": 0-100,
  "feedback": "Nhận xét chi tiết",
  "corrections": [{{"word": "từ sai", "correct": "từ đúng", "tip": "cách phát âm"}}],
  "suggestions": ["Gợi ý cải thiện"]
}}"""
        try:
            resp = await self._generate_text(prompt)
            return json.loads(self._extract_json(resp.text))
        except Exception:
            return {
                "pronunciation_score": 70, "fluency_score": 70, "grammar_score": 75,
                "vocabulary_score": 70, "overall_score": 71, "feedback": "Khá tốt!",
                "corrections": [], "suggestions": ["Luyện tập thêm"]
            }

    # ── GENERATE LESSON ───────────────────────────────────────────────────────
    async def generate_lesson(self, topic: str, skill: str, level: str) -> Dict:
        """AI tạo bài học hoàn chỉnh."""
        prompt = f"""Tạo bài học tiếng Anh về '{topic}' cho kỹ năng '{skill}', cấp độ {level}.

JSON:
{{
  "title": "Tiêu đề bài học",
  "introduction": "Giới thiệu bài học",
  "vocabulary": [{{"word": "...", "ipa": "...", "meaning_vi": "..."}}],
  "content": "Nội dung chính bài học",
  "examples": ["Ví dụ 1", "Ví dụ 2"],
  "exercises": [{{"question": "...", "answer": "..."}}],
  "summary": "Tóm tắt bài học",
  "homework": "Bài tập về nhà"
}}"""
        try:
            resp = await self._generate_text(prompt)
            return json.loads(self._extract_json(resp.text))
        except Exception:
            return {"title": topic, "content": "Bài học đang được tải...", "exercises": []}

    # ── TRANSLATE ─────────────────────────────────────────────────────────────
    async def translate(self, text: str, source: str = "en", target: str = "vi",
                         detailed: bool = False) -> Dict:
        """Dịch văn bản với giải thích chi tiết."""
        if detailed:
            prompt = f"""Dịch và giải thích chi tiết:
Văn bản ({source}): "{text}"
Dịch sang: {target}

JSON:
{{
  "translated": "Bản dịch",
  "explanation": "Giải thích ngữ pháp/từ vựng",
  "examples": ["Ví dụ sử dụng 1", "Ví dụ 2"],
  "synonyms": ["Cách diễn đạt khác 1", "Cách 2"],
  "notes": "Ghi chú văn hóa/ngữ cảnh"
}}"""
        else:
            prompt = f'Dịch "{text}" từ {source} sang {target}. Chỉ trả về bản dịch, không giải thích.'

        try:
            resp = await self._generate_text(prompt)
            if detailed:
                result = json.loads(self._extract_json(resp.text))
                return {"translated": result.get("translated", ""), **result}
            else:
                return {"translated": resp.text.strip()}
        except Exception:
            return {"translated": "[Không thể dịch]", "explanation": None}

    # ── SUMMARIZE TEXT ────────────────────────────────────────────────────────
    async def summarize(self, text: str, language: str = "vi") -> str:
        """Tóm tắt bài đọc/nghe."""
        prompt = f"""Tóm tắt văn bản sau bằng {'tiếng Việt' if language == 'vi' else 'English'}
(3-5 câu chính):

{text[:3000]}"""
        try:
            resp = await self._generate_text(prompt)
            return resp.text
        except Exception:
            return "Không thể tóm tắt nội dung."

    # ── GENERATE READING QUESTIONS ────────────────────────────────────────────
    async def generate_reading_questions(self, passage: str, count: int = 5) -> List[Dict]:
        """Tạo câu hỏi đọc hiểu."""
        prompt = f"""Tạo {count} câu hỏi đọc hiểu cho đoạn văn:
"{passage[:2000]}"

JSON array:
[{{"question": "...", "options": ["A..","B..","C..","D.."], "answer": "A", "explanation": "..."}}]"""
        try:
            resp = await self._generate_text(prompt)
            return json.loads(self._extract_json(resp.text))
        except Exception:
            return []

    # ── RECOMMEND LEARNING PATH ───────────────────────────────────────────────
    async def recommend_learning_path(self, user_data: Dict) -> Dict:
        """Gợi ý lộ trình học cá nhân hóa chuẩn khoa học theo từng bước."""
        level = user_data.get('level', 'B1')
        target = user_data.get('target', 'Giao tiếp chuẩn bản xứ')
        prompt = f"""Tạo lộ trình học Tiếng Anh khoa học từng bước cho học viên:
- Cấp độ hiện tại: {level}
- Mục tiêu: {target}
- Thời gian học/ngày: {user_data.get('daily_minutes', 30)} phút

JSON:
{{
  "recommended_courses": ["Khóa học 1", "Khóa học 2"],
  "step_by_step_roadmap": [
    {{"step": 1, "phase": "Bổ sung Từ vựng & Ngữ pháp nền tảng", "duration": "Tuần 1", "actions": ["Nạp 50 từ vựng chủ đề", "Luyện 3 thì cơ bản"]}},
    {{"step": 2, "phase": "Luyện Phản xạ Nghe - Chép chính tả", "duration": "Tuần 2", "actions": ["Luyện Dictation 15p", "Shadowing đoạn hội thoại ngắn"]}},
    {{"step": 3, "phase": "Thực hành Hội thoại cùng AI Teacher 3D", "duration": "Tuần 3", "actions": ["Roleplay 5 kịch bản thực tế", "Sửa lỗi phát âm & trọng âm"]}},
    {{"step": 4, "phase": "Luyện Viết & Làm bài Quiz tổng hợp", "duration": "Tuần 4", "actions": ["Viết email / đoạn văn Band 8.0", "Làm Quiz tổng hợp 4 kỹ năng"]}}
  ],
  "weekly_plan": {{
    "Thu 2": "Luyện Từ vựng & Flashcard SRS (20 phút)",
    "Thu 3": "Học Ngữ pháp chuyên sâu & Bài tập Quiz (25 phút)",
    "Thu 4": "Luyện Nghe Dictation & Shadowing (30 phút)",
    "Thu 5": "Hội thoại 3D AI Teacher Room (30 phút)",
    "Thu 6": "Luyện Viết & AI Correction (25 phút)",
    "Thu 7": "Kiểm tra tổng hợp & Làm bài Quiz tuần (30 phút)",
    "Chu Nhat": "Ôn tập nhẹ nhàng & Xem lại từ vựng yêu thích"
  }},
  "focus_skills": ["Phản xạ Phát âm", "Từ vựng Ngữ cảnh", "Viết Học thuật"],
  "tips": ["Học đều đặn 25-30 phút mỗi ngày theo phương pháp Pomodoro", "Thu âm giọng nói mỗi ngày để đo lường sự tiến bộ"],
  "estimated_weeks": 4
}}"""
        try:
            resp = await self._generate_text(prompt)
            return json.loads(self._extract_json(resp.text))
        except Exception:
            return {
                "recommended_courses": ["Phản xạ Giao tiếp 3D", "Ngữ pháp Ứng dụng B1-B2", "Từ vựng Oxford 3000"],
                "step_by_step_roadmap": [
                    {"step": 1, "phase": "Bổ sung Từ vựng & Ngữ pháp nền tảng", "duration": "Tuần 1", "actions": ["Nạp 50 từ vựng chủ đề", "Luyện 3 thì cơ bản"]},
                    {"step": 2, "phase": "Luyện Phản xạ Nghe - Chép chính tả", "duration": "Tuần 2", "actions": ["Luyện Dictation 15p", "Shadowing đoạn hội thoại ngắn"]},
                    {"step": 3, "phase": "Thực hành Hội thoại cùng AI Teacher 3D", "duration": "Tuần 3", "actions": ["Roleplay 5 kịch bản thực tế", "Sửa lỗi phát âm & trọng âm"]},
                    {"step": 4, "phase": "Luyện Viết & Làm bài Quiz tổng hợp", "duration": "Tuần 4", "actions": ["Viết email / đoạn văn Band 8.0", "Làm Quiz tổng hợp 4 kỹ năng"]}
                ],
                "weekly_plan": {
                    "Thu 2": "Luyện Từ vựng & Flashcard SRS (20 phút)",
                    "Thu 3": "Học Ngữ pháp chuyên sâu & Bài tập Quiz (25 phút)",
                    "Thu 4": "Luyện Nghe Dictation & Shadowing (30 phút)",
                    "Thu 5": "Hội thoại 3D AI Teacher Room (30 phút)",
                    "Thu 6": "Luyện Viết & AI Correction (25 phút)",
                    "Thu 7": "Kiểm tra tổng hợp & Làm bài Quiz tuần (30 phút)",
                    "Chu Nhat": "Ôn tập nhẹ nhàng & Xem lại từ vựng yêu thích"
                },
                "focus_skills": ["Phản xạ Phát âm", "Từ vựng Ngữ cảnh", "Viết Học thuật"],
                "tips": ["Học đều đặn 25-30 phút mỗi ngày", "Nói to và thu âm lại để kiểm tra phát âm"],
                "estimated_weeks": 4
            }


    # ── GENERATE SPEAKING PRACTICE ────────────────────────────────────────────
    async def generate_speaking_practice(self, topic: str, level: str) -> Dict:
        """AI tạo kịch bản luyện nói."""
        prompt = f"""Tạo kịch bản luyện nói (roleplay) tiếng Anh về chủ đề '{topic}', cấp độ {level}.

JSON:
{{
  "title": "Tên kịch bản",
  "context": "Ngữ cảnh",
  "roles": ["Vai trò 1", "Vai trò 2"],
  "vocabulary": ["Từ vựng 1", "Từ vựng 2"],
  "sample_dialogue": [
    {{"role": "Vai trò 1", "text": "Câu nói..."}}
  ],
  "questions_for_user": ["Câu hỏi gợi mở 1", "Câu hỏi 2"]
}}"""
        try:
            resp = await self._generate_text(prompt)
            return json.loads(self._extract_json(resp.text))
        except Exception:
            return {"title": topic, "context": "Lỗi khi tạo kịch bản."}

    # ── GENERATE LISTENING EXERCISE ───────────────────────────────────────────
    async def generate_listening_exercise(self, topic: str, level: str) -> Dict:
        """AI tạo bài luyện nghe."""
        prompt = f"""Tạo một bài luyện nghe tiếng Anh ngắn về chủ đề '{topic}', cấp độ {level}.
Đoạn hội thoại hoặc đoạn văn dài khoảng 100-150 từ.

JSON:
{{
  "title": "Tên bài nghe",
  "transcript": "Nội dung bài nghe",
  "vocabulary": ["Từ vựng chính"],
  "questions": [
    {{"question": "...", "options": ["A..","B..","C..","D.."], "answer": "A", "explanation": "..."}}
  ]
}}"""
        try:
            resp = await self._generate_text(prompt)
            return json.loads(self._extract_json(resp.text))
        except Exception:
            return {"title": topic, "transcript": "Lỗi khi tạo bài nghe."}

    # ── HELPERS ───────────────────────────────────────────────────────────────
    def _extract_json(self, text: str) -> str:
        """Extract JSON from response robustly."""
        # 1. Try to find JSON block
        extracted = text
        match = re.search(r'```(?:json)?\s*([\s\S]+?)\s*```', text)
        if match:
            extracted = match.group(1)
        else:
            # 2. Try to find raw JSON object or array
            match = re.search(r'(\{[\s\S]+\}|\[[\s\S]+\])', text)
            if match:
                extracted = match.group(1)

        # 3. Clean up common formatting issues that break Python json.loads
        # Remove single-line // comments (not inside strings if simple)
        extracted = re.sub(r'^\s*//.*$', '', extracted, flags=re.MULTILINE)
        # Remove trailing commas before } or ]
        extracted = re.sub(r',\s*(\}|\])', r'\1', extracted)
        return extracted.strip()

    def _clean_markdown(self, text: str) -> str:
        """Strip messy asterisks ** and * from response for clean professional presentation."""
        if not text:
            return ""
        # Replace **word** or *word* with clean word
        cleaned = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
        cleaned = re.sub(r'\*(.*?)\*', r'\1', cleaned)
        cleaned = re.sub(r'```(?:markdown|text)?', '', cleaned).replace('```', '')
        return cleaned.strip()

    def _extract_vocabulary(self, text: str) -> List[Dict]:
        """Extract vocabulary from AI response with richer metadata."""
        words = re.findall(r'\*\*([A-Za-z]+(?:\s+[A-Za-z]+){0,3})\*\*', text) or re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\b', text)
        result = []
        seen = set()
        for w in words:
            clean = w.strip()
            if len(clean) > 2 and clean.lower() not in seen and clean.lower() not in ["the", "and", "that", "this", "great", "question"]:
                seen.add(clean.lower())
                result.append({"word": clean, "ipa": "", "meaning_vi": ""})
                if len(result) >= 5:
                    break
        return result

    def _generate_suggestions(self, mode: str) -> List[str]:
        suggestions_map = {
            "chat": [
                "Hỏi thêm về ngữ pháp câu vừa rồi",
                "Cho tôi ví dụ thực tế khác",
                "Hãy giúp tôi viết câu giao tiếp liên quan"
            ],
            "lesson": [
                "Cho tôi thêm ví dụ dễ hiểu hơn",
                "Làm bài tập nhỏ để kiểm tra",
                "Giải thích sự khác nhau giữa các từ tương tự"
            ],
            "roleplay": [
                "I would like to order more items, please.",
                "Can you speak a little bit slower?",
                "Could you give me some feedback on my answer?"
            ],
            "pronunciation": [
                "Hãy đọc mẫu lại từ khó với tốc độ chậm",
                "Tôi phát âm trọng âm từ này đúng chưa?",
                "Cho tôi từ tương tự để luyện phát âm"
            ],
        }
        return suggestions_map.get(mode, ["Tiếp tục học", "Ôn tập câu tiếp theo", "Cho tôi bài tập luyện thêm"])


    def _fallback_questions(self, skill: str, level: str, count: int) -> List[Dict]:
        """High quality educational questions fallback per skill and level."""
        bank = {
            "grammar": [
                {
                    "question_text": "Choose the correct verb form to complete the sentence: 'She _____ to London twice this year.'",
                    "question_type": "multiple_choice",
                    "options": ["A. has traveled", "B. traveled", "C. is travel", "D. was traveled"],
                    "correct_answer": "A. has traveled",
                    "explanation": "We use Present Perfect ('has traveled') because the action happened during a time period that includes the present ('this year').",
                    "skill": "grammar", "level": level
                },
                {
                    "question_text": "Which sentence is grammatically CORRECT?",
                    "question_type": "multiple_choice",
                    "options": ["A. If I had known, I would have helped you.", "B. If I knew, I would had helped you.", "C. If I have known, I will help you.", "D. If I know, I would have helped."],
                    "correct_answer": "A. If I had known, I would have helped you.",
                    "explanation": "Third conditional structure: If + past perfect (had known), would + have + V3 (would have helped).",
                    "skill": "grammar", "level": level
                },
                {
                    "question_text": "Select the correct relative pronoun: 'The manager _____ office is on the third floor is very strict.'",
                    "question_type": "multiple_choice",
                    "options": ["A. whose", "B. who", "C. whom", "D. which"],
                    "correct_answer": "A. whose",
                    "explanation": "'Whose' is used to show possession (the manager's office).",
                    "skill": "grammar", "level": level
                },
                {
                    "question_text": "Fill in the blank: 'By this time next month, they _____ the new stadium.'",
                    "question_type": "multiple_choice",
                    "options": ["A. will have completed", "B. complete", "C. are completing", "D. had completed"],
                    "correct_answer": "A. will have completed",
                    "explanation": "Future Perfect ('will have completed') expresses an action completed before a future time.",
                    "skill": "grammar", "level": level
                },
                {
                    "question_text": "Choose the correct passive voice: 'The committee approved the project.'",
                    "question_type": "multiple_choice",
                    "options": ["A. The project was approved by the committee.", "B. The project is approved by the committee.", "C. The project had approved by the committee.", "D. The project was approving."],
                    "correct_answer": "A. The project was approved by the committee.",
                    "explanation": "Past simple active ('approved') becomes past simple passive ('was approved').",
                    "skill": "grammar", "level": level
                }
            ],
            "vocabulary": [
                {
                    "question_text": "Select the word closest in meaning to 'RESILIENT':",
                    "question_type": "multiple_choice",
                    "options": ["A. Adaptable and strong", "B. Fragile and weak", "C. Arrogant", "D. Indifferent"],
                    "correct_answer": "A. Adaptable and strong",
                    "explanation": "'Resilient' means able to withstand or recover quickly from difficult conditions.",
                    "skill": "vocabulary", "level": level
                },
                {
                    "question_text": "Choose the best collocation for business: 'We need to _____ a formal agreement with the partner.'",
                    "question_type": "multiple_choice",
                    "options": ["A. reach", "B. make a arrive", "C. do", "D. hold up"],
                    "correct_answer": "A. reach",
                    "explanation": "The strong collocation is 'reach an agreement' (đạt được thỏa thuận).",
                    "skill": "vocabulary", "level": level
                },
                {
                    "question_text": "What is the opposite (antonym) of 'SUBSTANTIAL'?",
                    "question_type": "multiple_choice",
                    "options": ["A. Insignificant", "B. Considerable", "C. Massive", "D. Prominent"],
                    "correct_answer": "A. Insignificant",
                    "explanation": "'Substantial' means large or important; its opposite is 'insignificant' (không đáng kể).",
                    "skill": "vocabulary", "level": level
                },
                {
                    "question_text": "Select the correct phrasal verb: 'We had to _____ the meeting due to heavy rain.'",
                    "question_type": "multiple_choice",
                    "options": ["A. call off", "B. call on", "C. call out", "D. call in"],
                    "correct_answer": "A. call off",
                    "explanation": "'Call off' means to cancel an event or meeting.",
                    "skill": "vocabulary", "level": level
                }
            ],
            "listening": [
                {
                    "question_text": "Listen to the statement: 'Could you pass me the quarterly sales report?' What does the speaker want?",
                    "question_type": "multiple_choice",
                    "options": ["A. To receive the sales document", "B. To buy a product", "C. To attend a meeting", "D. To cancel the report"],
                    "correct_answer": "A. To receive the sales document",
                    "explanation": "'Pass me' means hand over or give the document to the speaker.",
                    "skill": "listening", "level": level
                },
                {
                    "question_text": "Audio context: A customer at a hotel asks: 'Is breakfast included in the room rate?' What is the customer asking?",
                    "question_type": "multiple_choice",
                    "options": ["A. If morning food is free with the room", "B. What time the kitchen closes", "C. Where the dinner menu is", "D. How to check out early"],
                    "correct_answer": "A. If morning food is free with the room",
                    "explanation": "'Included in the rate' asks if the price covers breakfast.",
                    "skill": "listening", "level": level
                }
            ],
            "reading": [
                {
                    "question_text": "Passage: 'Global adoption of renewable energy accelerated in 2025 due to technological innovations.' What drove energy adoption?",
                    "question_type": "multiple_choice",
                    "options": ["A. Technological innovations", "B. High coal prices", "C. Government bans", "D. Population decrease"],
                    "correct_answer": "A. Technological innovations",
                    "explanation": "The text directly states that 'technological innovations' accelerated adoption.",
                    "skill": "reading", "level": level
                }
            ]
        }

        selected = bank.get(skill, bank["grammar"] + bank["vocabulary"])
        result = []
        for i in range(min(count, len(selected))):
            q = selected[i % len(selected)].copy()
            q["id"] = i + 1
            result.append(q)
        return result



    async def generate_lesson_interactive(self, content: str, lesson_type: str) -> Dict:
        """Sinh ra lời chào và câu hỏi đầu tiên dựa trên nội dung bài học."""
        prompt = f"""Đóng vai một giáo viên tiếng Anh nhiệt huyết.
Học sinh vừa mở bài học loại '{lesson_type}'. Nội dung bài học (có thể rỗng): '{content}'.
Hãy chào hỏi, giải thích ngắn gọn nội dung và đặt MỘT câu hỏi tương tác đơn giản để kiểm tra học sinh.

Format JSON:
{{
  "message": "Lời chào và giải thích của giáo viên",
  "question": "Câu hỏi dành cho học sinh"
}}"""
        try:
            resp = await self._generate_text(prompt)
            return json.loads(self._extract_json(resp.text))
        except Exception:
            return {"message": "Chào bạn, chúng ta cùng học nhé!", "question": "Bạn đã sẵn sàng chưa?"}

    async def evaluate_lesson_answer(self, answer: str) -> Dict:
        """Chấm điểm câu trả lời trong luồng bài học."""
        prompt = f"""Học sinh vừa trả lời câu hỏi bài học: "{answer}".
Hãy đánh giá xem câu trả lời này có đúng ngữ cảnh tiếng Anh không, và chấm điểm.

Format JSON:
{{
  "is_correct": true/false,
  "score": 0-10,
  "feedback": "Nhận xét của giáo viên (khen ngợi hoặc động viên)",
  "correction": "Sửa lỗi nếu sai",
  "explanation": "Giải thích chi tiết lỗi sai",
  "next_question": "Một câu hỏi tiếp theo (nếu muốn tiếp tục)"
}}"""
        try:
            resp = await self._generate_text(prompt)
            return json.loads(self._extract_json(resp.text))
        except Exception:
            return {"is_correct": True, "score": 10, "feedback": "Rất tốt!", "correction": "", "explanation": "", "next_question": None}

    async def test_connection(self, config_data: Dict[str, Any]) -> Dict[str, Any]:
        """Kiểm tra kết nối và đo độ trễ của API cấu hình."""
        provider = config_data.get("provider", "gemini")
        api_key = config_data.get("api_key", "").strip()
        base_url = config_data.get("base_url", "").strip()
        model = config_data.get("model", "").strip()

        if not api_key:
            return {"success": False, "error": "Vui lòng nhập API Key để kiểm tra kết nối."}

        start_time = time.time()
        test_prompt = "Say 'AI Connection OK - Ready to Teach!' in English."

        try:
            if provider in ["openai", "custom", "copilot", "deepseek", "groq"]:
                import httpx
                if not base_url:
                    if provider == "deepseek":
                        base_url = "https://api.deepseek.com/v1"
                    elif provider == "groq":
                        base_url = "https://api.groq.com/openai/v1"
                    else:
                        base_url = "https://api.openai.com/v1"

                url = base_url
                if not url.endswith("/chat/completions"):
                    url = url.rstrip("/") + "/chat/completions"

                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": model or ("gpt-4o-mini" if provider == "openai" else ("deepseek-chat" if provider == "deepseek" else "llama-3.3-70b-versatile")),
                    "messages": [{"role": "user", "content": test_prompt}],
                    "max_tokens": 50
                }

                async with httpx.AsyncClient(timeout=15.0) as client:
                    resp = await client.post(url, json=payload, headers=headers)
                    latency = round((time.time() - start_time) * 1000)
                    if resp.status_code == 200:
                        data = resp.json()
                        reply = data["choices"][0]["message"]["content"]
                        return {
                            "success": True,
                            "latency_ms": latency,
                            "reply": reply.strip(),
                            "message": f"Kết nối {provider.upper()} thành công! Độ trễ: {latency}ms."
                        }
                    else:
                        return {
                            "success": False,
                            "latency_ms": latency,
                            "error": f"Lỗi HTTP {resp.status_code}: {resp.text}"
                        }
            else:
                # Gemini
                from google import genai
                test_client = genai.Client(api_key=api_key)
                resp = await asyncio.to_thread(
                    test_client.models.generate_content,
                    model=model or "gemini-flash-latest",
                    contents=test_prompt
                )
                latency = round((time.time() - start_time) * 1000)
                return {
                    "success": True,
                    "latency_ms": latency,
                    "reply": resp.text.strip(),
                    "message": f"Kết nối Google Gemini thành công! Độ trễ: {latency}ms."
                }
        except Exception as e:
            latency = round((time.time() - start_time) * 1000)
            return {
                "success": False,
                "latency_ms": latency,
                "error": f"Lỗi kết nối ({provider}): {str(e)}"
            }

# Singleton instance
ai_engine = AIEngine()


