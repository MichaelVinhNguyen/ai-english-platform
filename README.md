# 🎓 VIHTECH AI ENGLISH LEARNING ACADEMY 2026

> **Nền tảng đào tạo tiếng Anh thông minh toàn diện chuẩn quốc tế (CEFR A1–C2, TOEIC 850+, IELTS 8.0+) tích hợp Trợ lý Trí tuệ Nhân tạo Đa phương thức (AI Gemini & Real-time Voice AI).**

---

## 🌟 Tổng Quan Dự Án

**AI English Learning Platform** là hệ sinh thái học ngoại ngữ hoàn chỉnh thế hệ mới, kết hợp phương pháp học đa giác quan **Omni-Method Studio** (8 chặng học sâu: Lý thuyết, Từ vựng IPA Flashcard, Ngữ pháp, Nghe hiểu, Luyện nói AI Mic 🎤, Luyện viết AI, Roleplay đối thoại và Mini-Quiz) cùng hệ thống khảo thí tự động chuẩn ETS & Cambridge.

---

## 🚀 Các Tính Năng Nổi Bật

### 1. 🎯 Lộ Trình Học & Khảo Thí 10 Tracks Toàn Diện (CEFR A1 – C2)
- **CEFR A1:** Mất gốc & Nhập môn căn bản (Breakthrough).
- **CEFR A2:** Giao tiếp sơ cấp & Sinh hoạt đời thường (Waystage).
- **CEFR B1:** Giao tiếp trung cấp vững vàng (Threshold) + Bộ 4 kỹ năng chuẩn B1.
- **CEFR B2:** Tiếng Anh học thuật & Đàm phán chuyên nghiệp (Vantage).
- **CEFR C1:** Sử dụng ngôn ngữ linh hoạt, chuyên sâu (Effective Operational).
- **CEFR C2:** Bậc thầy ngoại ngữ, phân tích sắc thái bản ngữ (Mastery).
- **TOEIC 850+:** Bộ luyện đề chuẩn ETS 2026 (Part 1 - Part 7) kèm giải thích chi tiết.
- **IELTS 8.0+ Academic:** Luyện thi 4 kỹ năng, chấm bài luận Task 1 & Task 2 bằng AI và phỏng vấn Speaking 3 phần.
- **Business English:** Tiếng Anh thương mại FAANG & Đàm phán quốc tế.
- **Phonetic IPA Studio:** Luyện ngữ âm chuyên sâu 44 âm IPA với biểu đồ âm học.

### 2. 🤖 Gia Sư AI 3D Đa Giác Quan (AI Teacher Studio)
- 3 Persona chuyên gia:
  - **Ms. Emma:** Chuyên gia ngữ âm Oxford RP & chiến lược C1/C2.
  - **Mr. Alex:** Chuyên gia đàm phán thương mại Silicon Valley & phỏng vấn FAANG.
  - **Ms. Chloe:** Phản xạ tự nhiên Anh-Mỹ & Idioms / Daily Slang.
- Tích hợp nhận diện giọng nói chuẩn xác và hệ thống Voice AI chống gián đoạn.

### 3. 📚 Kho Từ Vựng Khổng Lồ (13,973+ Từ Vựng & Thuật Toán SM-2)
- Tra cứu nhanh từ vựng A-Z theo chủ đề và cấp độ CEFR.
- Thuật toán lặp lại ngắt quãng (Spaced Repetition System - SM-2).
- Flashcards Anki tương tác 3D lật thẻ mượt mà.

### 4. 🎯 Ngân Hàng 30 Đề Quiz Đa Dạng & Khảo Thí Độc Lập
- 30 bộ đề thi trắc nghiệm phân tích điểm mạnh / điểm yếu theo từng kỹ năng.
- Chấm điểm tức thì kèm giải thích chi tiết đáp án.

### 5. 🛡️ Cổng Quản Trị Doanh Nghiệp (Enterprise CMS Admin)
- Thống kê học tập, người dùng, doanh thu và gói học.
- Quản lý kho từ vựng, tài khoản học viên và phân quyền vai trò.
- Cấu hình linh hoạt các mô hình AI (Gemini, OpenAI, Claude, DeepSeek, Local Ollama).

---

## 🛠️ Kiến Trúc Công Nghệ

```
AI English Platform
├── 🌐 Frontend: Vanilla HTML5, Modern CSS3 (Glassmorphism, High Contrast), Vanilla JS ES6+
├── ⚡ Backend API: FastAPI (Python 3.10+ / 3.11 / 3.12), SQLAlchemy 2.0 Async, aiosqlite
├── 🤖 AI Engine: Google Gemini API (gemini-2.5-flash), SpeechSynthesis & Web Speech API
├── 🗄️ Database: SQLite3 (app.db) với 29 bảng dữ liệu và 13,973+ từ vựng nạp sẵn
└── 🚀 Deployment: Vercel Serverless (@vercel/python), Render, Docker, Local Uvicorn
```

---

## 💻 Hướng Dẫn Cài Đặt & Chạy Cục Bộ (Local)

### 1. Yêu Cầu Môi Trường
- Python 3.10 trở lên
- Node.js (tùy chọn để kiểm tra script)

### 2. Cài Đặt Thư Viện
```bash
git clone https://github.com/MichaelVinhNguyen/ai-english-platform.git
cd ai-english-platform
pip install -r requirements.txt
```

### 3. Khởi Chạy Ứng Dụng
```bash
# Cách 1: Chạy trực tiếp qua file run.py
python run.py

# Hoặc Cách 2: Chạy qua uvicorn
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Truy cập trình duyệt: **`http://localhost:8000`**

### 4. Tài Khoản Quản Trị Mặc Định
- **Email:** `admin@vihtech.com` hoặc `VihTech` | **Mật khẩu:** `vihtech2026`
- **Email phụ:** `admin@example.com` hoặc `admin` | **Mật khẩu:** `admin123`
- **Học viên:** Chỉ cần nhập bất kỳ Email nào để vào học ngay lập tức!

---

## ☁️ Hướng Dẫn Triển Khai Lên Cloud (Deploy)

### 🚀 Triển Khai Trên Vercel
1. Kết nối repository GitHub `ai-english-platform` với Vercel.
2. Vercel sẽ tự động nhận diện tệp `vercel.json`, build backend serverless qua `api/index.py` và serve giao diện tĩnh từ thư mục `public/`.
3. Cấu hình biến môi trường (Environment Variables) trên Vercel nếu cần:
   - `GEMINI_API_KEY`: `AIzaSy...`

### 🐳 Triển Khai Bằng Docker
```bash
docker build -t ai-english-platform .
docker run -p 8000:8000 ai-english-platform
```

---

## 📜 Bản Quyền & Tác Giả

- **Đơn vị phát triển:** VihTech Global Academy 2026
- **Tác giả:** QuangVinh Nguyen
- **Giấy phép:** MIT License
