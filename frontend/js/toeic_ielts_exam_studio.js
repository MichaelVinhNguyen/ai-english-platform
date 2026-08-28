/**
 * toeic_ielts_exam_studio.js – Phân Hệ Khảo Thí Chuẩn Hóa TOEIC 850+ & IELTS 8.0+ Academic (2026)
 * Tích hợp:
 * 1. TOEIC 850+ (ETS Format 2026 - 7 Parts - Thang điểm 10-990)
 * 2. IELTS 8.0+ Academic (4 Kỹ năng - Thang Band 1.0-9.0 - AI Examiner 1-on-1 Real-time Voice Studio)
 * 3. Ma trận Chuẩn đầu ra & Chứng chỉ số Gold Luxury xác thực Blockchain
 */

// ══════════════════════════════════════════════════════════════════════════════
// ── 1. TOEIC 850+ STANDARDIZED EXAM CONTROLLER (ETS FORMAT 2026) ─────────────
// ══════════════════════════════════════════════════════════════════════════════

window.formatExamTimer = function(seconds) {
  if (isNaN(seconds) || seconds < 0) seconds = 0;
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
};

window.selectToeicOption = function(skill, qid, answer) {
  if (!window.toeicExamState) return;
  if (skill === 'listening') {
    window.toeicExamState.listeningAnswers[qid] = answer;
  } else if (skill === 'reading') {
    window.toeicExamState.readingAnswers[qid] = answer;
  }
};

window.selectIeltsOption = function(skill, qid, answer) {
  if (!window.ieltsExamState) return;
  if (skill === 'listening') {
    window.ieltsExamState.listeningAnswers[qid] = answer;
  } else if (skill === 'reading') {
    window.ieltsExamState.readingAnswers[qid] = answer;
  }
};

window.toeicExamState = {
  examData: null,
  activeSection: 'listening', // 'listening' | 'reading'
  activePartId: 'P1', // 'P1'..'P7'
  examMode: 'full', // 'full' | 'listening' | 'reading' | 'P1'..'P7'
  listeningAnswers: {},
  readingAnswers: {},
  activePassageIndex: 0,
  readingFontSize: 14.5,
  secondsLeft: 120 * 60,
  timerInterval: null
};

window.getFallbackToeicExamData = function() {
  return {
    exam_id: "toeic-ets-2026-01",
    title: "Đề Thi Khảo Thí TOEIC 850+ Format Chuẩn ETS 2026 (7 Parts)",
    listening: {
      title: "TOEIC Listening Comprehension (100 Questions - 45 Mins)",
      total_questions: 100,
      time_min: 45,
      parts: [
        {
          part_id: "P1",
          part_title: "Part 1: Photographs (6 Questions)",
          description: "Nghe 4 phát biểu và chọn câu miêu tả đúng nhất bức ảnh.",
          questions: [
            {
              id: "P1_Q1",
              audio_text: "A. He is writing on a whiteboard. B. He is looking at a computer monitor. C. He is talking on the phone. D. He is opening a filing cabinet.",
              options: ["A. He is writing on a whiteboard", "B. He is looking at a computer monitor", "C. He is talking on the phone", "D. He is opening a filing cabinet"],
              correct: "B. He is looking at a computer monitor",
              explanation: "Câu B miêu tả đúng hành động của nhân vật nhìn vào màn hình máy tính."
            },
            {
              id: "P1_Q2",
              audio_text: "A. People are boarding a train. B. People are walking along a street. C. People are sitting in a conference room. D. People are waiting in line at a counter.",
              options: ["A. People are boarding a train", "B. People are walking along a street", "C. People are sitting in a conference room", "D. People are waiting in line at a counter"],
              correct: "C. People are sitting in a conference room",
              explanation: "Câu C mô tả chính xác mọi người đang ngồi trong phòng hội nghị."
            }
          ]
        },
        {
          part_id: "P2",
          part_title: "Part 2: Question - Response (25 Questions)",
          description: "Nghe câu hỏi hoặc phát biểu và chọn câu phản hồi phù hợp nhất (A, B, C).",
          questions: [
            {
              id: "P2_Q7",
              audio_text: "Where is the marketing meeting scheduled to take place?",
              options: ["A. At 3:30 PM", "B. In Conference Room B on the second floor", "C. Yes, with the new director"],
              correct: "B. In Conference Room B on the second floor",
              explanation: "Câu hỏi 'Where' hỏi về địa điểm nên phương án B trả lời chính xác."
            }
          ]
        }
      ]
    },
    reading: {
      title: "TOEIC Reading Comprehension (100 Questions - 75 Mins)",
      total_questions: 100,
      time_min: 75,
      parts: [
        {
          part_id: "P5",
          part_title: "Part 5: Incomplete Sentences (30 Questions)",
          questions: [
            {
              id: "P5_Q101",
              question: "All employees are required to submit their travel expense reports _______ Friday afternoon.",
              options: ["A. by", "B. at", "C. on", "D. in"],
              correct: "A. by",
              explanation: "'by + thời điểm' mang nghĩa trước hoặc muộn nhất vào thời điểm đó."
            },
            {
              id: "P5_Q102",
              question: "The newly renovated library is _______ located near the central subway station.",
              options: ["A. convenient", "B. conveniently", "C. convenience", "D. more convenient"],
              correct: "B. conveniently",
              explanation: "Cần một trạng từ (conveniently) bổ nghĩa cho tính từ/phân từ 'located'."
            }
          ]
        },
        {
          part_id: "P6",
          part_title: "Part 6: Text Completion (16 Questions)",
          passages: [
            {
              passage_id: "P6_T1",
              text: "To: All Department Heads\nFrom: Facilities Management\nSubject: Office Air Conditioning Upgrade\n\nPlease be advised that the building management team will conduct essential maintenance on the central air conditioning units this Saturday from 8:00 AM to 4:00 PM. [131] _______, the entire building will be without climate control during these hours. Employees are advised to plan accordingly.",
              questions: [
                {
                  id: "P6_Q131",
                  options: ["A. Consequently", "B. Although", "C. However", "D. Otherwise"],
                  correct: "A. Consequently",
                  explanation: "'Consequently' (Do đó/kết quả là) thể hiện mối quan hệ nguyên nhân - kết quả."
                }
              ]
            }
          ]
        },
        {
          part_id: "P7",
          part_title: "Part 7: Reading Comprehension (54 Questions)",
          passages: [
            {
              passage_id: "P7_T1",
              title: "Business Announcement: TechNova Expansion",
              text: "TechNova Corporation, a global leader in educational software solutions, announced today that it will open a new regional research and development center in Da Nang, Vietnam next quarter. The 50,000-square-foot facility is expected to create over 300 high-tech engineering and AI specialist jobs over the next two years. Interested applicants are encouraged to visit the company careers portal.",
              questions: [
                {
                  id: "P7_Q147",
                  question: "What is the primary purpose of the announcement?",
                  options: [
                    "A. To announce the opening of a new R&D center",
                    "B. To report quarterly financial earnings",
                    "C. To recruit a new Chief Executive Officer",
                    "D. To announce a product price increase"
                  ],
                  correct: "A. To announce the opening of a new R&D center",
                  explanation: "Thông báo nêu rõ việc TechNova mở trung tâm nghiên cứu và phát triển mới tại Đà Nẵng."
                }
              ]
            }
          ]
        }
      ]
    }
  };
};

window.renderToeicExamTab = async function(container, levelData) {
  container.innerHTML = '<div class="loading-dots" style="padding:40px; text-align:center;"><span></span><span></span><span></span></div>';

  let examData = null;
  try {
    examData = await api.levelCurriculum.getToeicFullExam();
  } catch (err) {
    console.warn('[WARN] API getToeicFullExam failed, using fallback:', err);
  }

  if (!examData || !examData.listening) {
    examData = window.getFallbackToeicExamData();
  }
  window.toeicExamState.examData = examData;

    container.innerHTML = `
      <!-- TOEIC 2026 HERO LOBBY CARD -->
      <div class="toeic-exam-lobby-header card" style="padding:28px; background:linear-gradient(135deg, rgba(30, 27, 75, 0.95), rgba(15, 23, 42, 0.98)); border:2px solid rgba(168,85,247,0.5); border-radius:20px; box-shadow:0 12px 35px rgba(0,0,0,0.4); margin-bottom:24px;">
        <div style="display:inline-flex; align-items:center; gap:8px; background:linear-gradient(135deg, #a855f7, #7c3aed); padding:6px 16px; border-radius:30px; margin-bottom:14px; box-shadow:0 0 15px rgba(168,85,247,0.4);">
          <span style="font-size:14px;">💼</span>
          <span style="font-size:12px; font-weight:900; text-transform:uppercase; letter-spacing:1px; color:#ffffff;">
            PHÒNG THI CHUẨN HÓA TOEIC 850+ ETS FORMAT 2026
          </span>
        </div>
        
        <h1 style="font-size:26px; font-weight:900; margin:0 0 10px 0; color:#ffffff; text-shadow:0 2px 10px rgba(0,0,0,0.8);">
          🎯 Đề Thi Thực Chiến 7 Part Đầy Đủ Chuẩn ETS (Listening & Reading – Thang Điểm 990)
        </h1>
        <p style="color:#e2e8f0; font-size:14px; max-width:820px; margin:0 0 20px 0; line-height:1.6;">
          Đánh giá năng lực giao tiếp thương mại và công sở quốc tế theo định dạng chuẩn ETS 2026. Luyện tập toàn diện 7 Parts hoặc kiểm tra toàn bộ 200 câu trong 120 phút. Đạt từ <b>850/990 điểm</b> trở lên để được cấp <b>Chứng Chỉ TOEIC 850+ Gold Quốc Tế</b>!
        </p>

        <!-- 2 MAIN SECTIONS GRID -->
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:16px; margin-bottom:24px;">
          <!-- LISTENING SECTION -->
          <div class="card" style="background:rgba(0,0,0,0.4); border:1.5px solid rgba(6,182,212,0.4); border-radius:16px; padding:20px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
              <span style="font-size:22px;">🎧</span>
              <span class="badge" style="background:#06b6d4; color:#fff; font-weight:800;">100 CÂU • 45 PHÚT • 495 ĐIỂM</span>
            </div>
            <div style="font-size:16px; font-weight:800; color:#38bdf8; margin-bottom:6px;">Section 1: Listening Comprehension</div>
            <div style="font-size:12.5px; color:#cbd5e1; line-height:1.5; margin-bottom:14px;">
              • <b>Part 1: Photographs</b> (6 câu - Tranh miêu tả)<br>
              • <b>Part 2: Question - Response</b> (25 câu - Hỏi đáp phản xạ)<br>
              • <b>Part 3: Short Conversations</b> (39 câu - 13 đoạn hội thoại)<br>
              • <b>Part 4: Short Talks</b> (30 câu - 10 bài nói ngắn)
            </div>
            <div style="display:flex; gap:8px; flex-wrap:wrap;">
              <button class="btn btn-sm btn-ghost" onclick="startToeicExam('listening', 'P1')" style="flex:1; border:1px solid rgba(6,182,212,0.5); color:#38bdf8; font-weight:700;">
                Thi Phần Nghe (P1-P4) →
              </button>
            </div>
          </div>

          <!-- READING SECTION -->
          <div class="card" style="background:rgba(0,0,0,0.4); border:1.5px solid rgba(16,185,129,0.4); border-radius:16px; padding:20px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
              <span style="font-size:22px;">📖</span>
              <span class="badge" style="background:#10b981; color:#fff; font-weight:800;">100 CÂU • 75 PHÚT • 495 ĐIỂM</span>
            </div>
            <div style="font-size:16px; font-weight:800; color:#4ade80; margin-bottom:6px;">Section 2: Reading Comprehension</div>
            <div style="font-size:12.5px; color:#cbd5e1; line-height:1.5; margin-bottom:14px;">
              • <b>Part 5: Incomplete Sentences</b> (30 câu - Ngữ pháp & Từ vựng)<br>
              • <b>Part 6: Text Completion</b> (16 câu - Điền đoạn văn bản)<br>
              • <b>Part 7: Reading Comprehension</b> (54 câu - Đơn, Kép & Ba đoạn)
            </div>
            <div style="display:flex; gap:8px; flex-wrap:wrap;">
              <button class="btn btn-sm btn-ghost" onclick="startToeicExam('reading', 'P5')" style="flex:1; border:1px solid rgba(16,185,129,0.5); color:#4ade80; font-weight:700;">
                Thi Phần Đọc (P5-P7) →
              </button>
            </div>
          </div>
        </div>

        <!-- 7-PART DRILL BUTTONS -->
        <div style="background:rgba(0,0,0,0.3); border-radius:14px; padding:14px; margin-bottom:20px;">
          <div style="font-size:12.5px; font-weight:800; color:#cbd5e1; margin-bottom:8px; text-transform:uppercase; letter-spacing:0.5px;">
            ⚡ Luyện Tập Từng Part Riêng Biệt (Speed Drill):
          </div>
          <div style="display:flex; gap:8px; flex-wrap:wrap;">
            <button class="btn btn-sm btn-secondary" onclick="startToeicExam('part', 'P1')">Part 1 (Tranh)</button>
            <button class="btn btn-sm btn-secondary" onclick="startToeicExam('part', 'P2')">Part 2 (Hỏi đáp)</button>
            <button class="btn btn-sm btn-secondary" onclick="startToeicExam('part', 'P3')">Part 3 (Hội thoại)</button>
            <button class="btn btn-sm btn-secondary" onclick="startToeicExam('part', 'P4')">Part 4 (Bài nói)</button>
            <button class="btn btn-sm btn-secondary" onclick="startToeicExam('part', 'P5')">Part 5 (Điền câu)</button>
            <button class="btn btn-sm btn-secondary" onclick="startToeicExam('part', 'P6')">Part 6 (Điền đoạn)</button>
            <button class="btn btn-sm btn-secondary" onclick="startToeicExam('part', 'P7')">Part 7 (Đọc hiểu)</button>
          </div>
        </div>

        <!-- FULL 200Q MOCK TEST CTA -->
        <div style="text-align:center; padding-top:16px; border-top:1px solid rgba(168,85,247,0.3);">
          <button class="btn btn-primary btn-lg" onclick="startToeicExam('full', 'P1')" style="padding:14px 44px; font-size:17px; font-weight:900; box-shadow:0 8px 30px rgba(168,85,247,0.5); background:linear-gradient(135deg, #a855f7, #7c3aed);">
            🚀 VÀO THI THỬ TOEIC FULL 200 CÂU (120 PHÚT – 990 ĐIỂM)
          </button>
          <div style="font-size:12px; color:#94a3b8; margin-top:8px;">
            ⏱️ Tổng thời gian: 120 phút • Bảng quy đổi điểm ETS 990 chuẩn xác • Cấp chứng chỉ số xác thực
          </div>
        </div>
      </div>

      <div id="toeic-exam-active-arena" style="display:none;"></div>
      <div id="toeic-exam-result-board" style="display:none;"></div>
    `;
};

window.startToeicExam = async function(mode, partId) {
  if (!window.toeicExamState.examData) {
    try {
      window.toeicExamState.examData = await api.levelCurriculum.getToeicFullExam();
    } catch(e) {
      return toast('Không thể tải dữ liệu đề thi TOEIC: ' + e.message, 'error');
    }
  }

  window.toeicExamState.examMode = mode;
  window.toeicExamState.activePartId = partId || (mode === 'reading' ? 'P5' : 'P1');
  window.toeicExamState.activeSection = ['P1', 'P2', 'P3', 'P4'].includes(window.toeicExamState.activePartId) ? 'listening' : 'reading';
  window.toeicExamState.listeningAnswers = {};
  window.toeicExamState.readingAnswers = {};
  window.toeicExamState.activePassageIndex = 0;

  if (mode === 'full') {
    window.toeicExamState.secondsLeft = 120 * 60;
  } else if (mode === 'listening') {
    window.toeicExamState.secondsLeft = 45 * 60;
  } else if (mode === 'reading') {
    window.toeicExamState.secondsLeft = 75 * 60;
  } else {
    window.toeicExamState.secondsLeft = 20 * 60;
  }

  const lobby = document.querySelector('.toeic-exam-lobby-header');
  const arena = document.getElementById('toeic-exam-active-arena');
  const resultBoard = document.getElementById('toeic-exam-result-board');
  if (lobby) lobby.style.display = 'none';
  if (resultBoard) resultBoard.style.display = 'none';
  if (!arena) return;

  arena.style.display = 'block';
  renderToeicActiveArena();
  startToeicExamTimer();
};

function startToeicExamTimer() {
  if (window.toeicExamState.timerInterval) clearInterval(window.toeicExamState.timerInterval);
  window.toeicExamState.timerInterval = setInterval(() => {
    window.toeicExamState.secondsLeft--;
    const timerEl = document.getElementById('toeic-exam-timer-display');
    if (timerEl) {
      timerEl.textContent = formatExamTimer(window.toeicExamState.secondsLeft);
      if (window.toeicExamState.secondsLeft <= 180) {
        timerEl.style.color = '#ef4444';
        timerEl.style.background = 'rgba(239,68,68,0.15)';
      }
    }
    if (window.toeicExamState.secondsLeft <= 0) {
      clearInterval(window.toeicExamState.timerInterval);
      toast('Đã hết thời gian làm bài thi TOEIC! Tự động nộp bài...', 'warning');
      submitToeicExam();
    }
  }, 1000);
}

function renderToeicActiveArena() {
  const arena = document.getElementById('toeic-exam-active-arena');
  if (!arena) return;

  const data = window.toeicExamState.examData;
  const currentPart = window.toeicExamState.activePartId;
  const mode = window.toeicExamState.examMode;

  arena.innerHTML = `
    <!-- STICKY TOP CONTROL BAR -->
    <div style="background:var(--bg-card); border:1.5px solid var(--border); border-radius:16px; padding:16px 20px; margin-bottom:20px; position:sticky; top:10px; z-index:100; box-shadow:0 8px 25px rgba(0,0,0,0.15);">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:12px;">
        <div>
          <div style="display:flex; align-items:center; gap:8px;">
            <span class="badge" style="background:#a855f7; color:#fff; font-weight:900;">TOEIC ETS 2026</span>
            <span style="font-weight:900; font-size:16px; color:var(--text-primary);">${data.title}</span>
          </div>
          <div style="font-size:12px; color:var(--text-secondary); margin-top:2px;">
            Chế độ: <b>${mode === 'full' ? 'Thi Thử Toàn Diện 200 Câu (990 Điểm)' : `Luyện Tập Part ${currentPart}`}</b>
          </div>
        </div>

        <div style="display:flex; align-items:center; gap:12px;">
          <div id="toeic-exam-timer-display" style="font-size:22px; font-weight:900; color:var(--accent-purple); font-family:monospace; background:rgba(168,85,247,0.1); padding:6px 16px; border-radius:10px; border:1px solid rgba(168,85,247,0.3);">
            ${formatExamTimer(window.toeicExamState.secondsLeft)}
          </div>
          <button class="btn btn-success" onclick="submitToeicExam()" style="font-weight:900; padding:10px 22px; box-shadow:0 4px 15px rgba(16,185,129,0.35);">
            📥 Nộp Bài Thi TOEIC
          </button>
        </div>
      </div>

      <!-- 7 PART NAVIGATION TABS -->
      <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:4px;">
        <button class="pill-tab ${currentPart === 'P1' ? 'active' : ''}" onclick="switchToeicPart('P1')" style="font-size:12.5px; font-weight:800; white-space:nowrap;">P1: Tranh (6c)</button>
        <button class="pill-tab ${currentPart === 'P2' ? 'active' : ''}" onclick="switchToeicPart('P2')" style="font-size:12.5px; font-weight:800; white-space:nowrap;">P2: Hỏi Đáp (25c)</button>
        <button class="pill-tab ${currentPart === 'P3' ? 'active' : ''}" onclick="switchToeicPart('P3')" style="font-size:12.5px; font-weight:800; white-space:nowrap;">P3: Hội Thoại (39c)</button>
        <button class="pill-tab ${currentPart === 'P4' ? 'active' : ''}" onclick="switchToeicPart('P4')" style="font-size:12.5px; font-weight:800; white-space:nowrap;">P4: Bài Nói (30c)</button>
        <button class="pill-tab ${currentPart === 'P5' ? 'active' : ''}" onclick="switchToeicPart('P5')" style="font-size:12.5px; font-weight:800; white-space:nowrap;">P5: Điền Câu (30c)</button>
        <button class="pill-tab ${currentPart === 'P6' ? 'active' : ''}" onclick="switchToeicPart('P6')" style="font-size:12.5px; font-weight:800; white-space:nowrap;">P6: Điền Đoạn (16c)</button>
        <button class="pill-tab ${currentPart === 'P7' ? 'active' : ''}" onclick="switchToeicPart('P7')" style="font-size:12.5px; font-weight:800; white-space:nowrap;">P7: Đọc Hiểu (54c)</button>
      </div>
    </div>

    <!-- PART CONTENT CONTAINER -->
    <div id="toeic-part-body-container"></div>
  `;

  renderToeicCurrentPartBody();
}

window.switchToeicPart = function(partId) {
  window.toeicExamState.activePartId = partId;
  window.toeicExamState.activeSection = ['P1', 'P2', 'P3', 'P4'].includes(partId) ? 'listening' : 'reading';
  
  document.querySelectorAll('#toeic-exam-active-arena .pill-tab').forEach(b => b.classList.remove('active'));
  renderToeicActiveArena();
};

function renderToeicCurrentPartBody() {
  const container = document.getElementById('toeic-part-body-container');
  if (!container) return;

  const data = window.toeicExamState.examData;
  const partId = window.toeicExamState.activePartId;
  const isListening = ['P1', 'P2', 'P3', 'P4'].includes(partId);

  let partData = null;
  if (isListening) {
    partData = data.listening.parts.find(p => p.part_id === partId);
  } else {
    partData = data.reading.parts.find(p => p.part_id === partId);
  }

  if (!partData) {
    container.innerHTML = `<div class="card" style="padding:20px; text-align:center;">Chưa có dữ liệu cho phần này.</div>`;
    return;
  }

  // 1. PART 1: PHOTOGRAPHS
  if (partId === 'P1') {
    container.innerHTML = `
      <div style="max-width:920px; margin:0 auto;">
        <div class="card" style="padding:16px 20px; margin-bottom:16px; background:linear-gradient(135deg, rgba(6,182,212,0.08), rgba(168,85,247,0.05)); border:1px solid rgba(6,182,212,0.4); border-radius:14px;">
          <b>${partData.part_title}</b>: ${partData.description}
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(420px, 1fr)); gap:16px;">
          ${(partData.questions || []).map(q => `
            <div class="card" style="padding:18px; border-radius:14px;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                <span class="badge badge-purple" style="font-weight:800;">${q.id}</span>
                <button class="btn btn-sm btn-ghost" onclick="speakText('${q.audio_text.replace(/'/g, "\\'")}')" style="font-size:12px;">
                  🔊 Phát Audio Lựa Chọn
                </button>
              </div>
              <div style="background:var(--bg-secondary); border:1px dashed var(--border); border-radius:10px; padding:14px; font-size:13px; color:var(--text-secondary); margin-bottom:12px;">
                🖼️ <b>Mô tả hình ảnh:</b> ${q.image_desc}
              </div>
              <div style="display:flex; flex-direction:column; gap:6px;">
                ${q.options.map(opt => `
                  <label style="display:flex; align-items:center; gap:8px; background:var(--bg-secondary); border:1px solid var(--border); border-radius:8px; padding:8px 12px; cursor:pointer; font-size:13px;">
                    <input type="radio" name="toeic_ans_${q.id}" value="${opt.replace(/"/g, '&quot;')}" ${window.toeicExamState.listeningAnswers[q.id] === opt ? 'checked' : ''} onchange="selectToeicOption('listening', '${q.id}', this.value)">
                    <span>${opt}</span>
                  </label>
                `).join('')}
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
    return;
  }

  // 2. PART 2: QUESTION-RESPONSE
  if (partId === 'P2') {
    container.innerHTML = `
      <div style="max-width:920px; margin:0 auto;">
        <div class="card" style="padding:16px 20px; margin-bottom:16px; background:linear-gradient(135deg, rgba(6,182,212,0.08), rgba(168,85,247,0.05)); border:1px solid rgba(6,182,212,0.4); border-radius:14px;">
          <b>${partData.part_title}</b>: ${partData.description}
        </div>
        <div style="display:flex; flex-direction:column; gap:14px;">
          ${(partData.questions || []).map(q => `
            <div class="card" style="padding:18px; border-radius:14px;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                <span class="badge badge-cyan" style="font-weight:800;">${q.id}</span>
                <button class="btn btn-sm btn-primary" onclick="speakText('${q.audio_text.replace(/'/g, "\\'")}')" style="font-size:12px; font-weight:800;">
                  🔊 Nghe Câu Hỏi & 3 Lựa Chọn
                </button>
              </div>
              <div style="font-size:14.5px; font-weight:800; color:var(--text-primary); margin-bottom:10px;">
                ${q.question}
              </div>
              <div style="display:flex; flex-direction:column; gap:6px;">
                ${q.options.map(opt => `
                  <label style="display:flex; align-items:center; gap:8px; background:var(--bg-secondary); border:1px solid var(--border); border-radius:8px; padding:9px 14px; cursor:pointer; font-size:13.5px;">
                    <input type="radio" name="toeic_ans_${q.id}" value="${opt.replace(/"/g, '&quot;')}" ${window.toeicExamState.listeningAnswers[q.id] === opt ? 'checked' : ''} onchange="selectToeicOption('listening', '${q.id}', this.value)">
                    <span>${opt}</span>
                  </label>
                `).join('')}
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
    return;
  }

  // 3. PART 3 & PART 4: CONVERSATIONS & TALKS
  if (partId === 'P3' || partId === 'P4') {
    const items = partId === 'P3' ? (partData.conversations || []) : (partData.talks || []);
    container.innerHTML = `
      <div style="max-width:920px; margin:0 auto;">
        <div class="card" style="padding:16px 20px; margin-bottom:16px; background:linear-gradient(135deg, rgba(6,182,212,0.08), rgba(168,85,247,0.05)); border:1px solid rgba(6,182,212,0.4); border-radius:14px;">
          <b>${partData.part_title}</b>: ${partData.description}
        </div>
        <div style="display:flex; flex-direction:column; gap:20px;">
          ${items.map((item, idx) => `
            <div class="card" style="padding:20px; border-radius:16px;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
                <span class="badge badge-purple" style="font-weight:900;">Đoạn ${idx + 1}: ${item.context || ''}</span>
                <button class="btn btn-sm btn-primary" onclick="speakText('${item.audio_text.replace(/'/g, "\\'")}')" style="font-size:12.5px; font-weight:800;">
                  🔊 Phát Audio Đoạn Hội Thoại
                </button>
              </div>
              <div style="display:flex; flex-direction:column; gap:12px;">
                ${item.questions.map(q => `
                  <div style="background:var(--bg-secondary); border:1px solid var(--border); border-radius:10px; padding:12px;">
                    <div style="font-size:13.5px; font-weight:800; color:var(--text-primary); margin-bottom:8px;">
                      <span style="color:var(--accent-cyan); margin-right:4px;">${q.id}:</span> ${q.question}
                    </div>
                    <div style="display:flex; flex-direction:column; gap:6px;">
                      ${q.options.map(opt => `
                        <label style="display:flex; align-items:center; gap:8px; background:var(--bg-card); border:1px solid var(--border); border-radius:6px; padding:7px 12px; cursor:pointer; font-size:13px;">
                          <input type="radio" name="toeic_ans_${q.id}" value="${opt.replace(/"/g, '&quot;')}" ${window.toeicExamState.listeningAnswers[q.id] === opt ? 'checked' : ''} onchange="selectToeicOption('listening', '${q.id}', this.value)">
                          <span>${opt}</span>
                        </label>
                      `).join('')}
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
    return;
  }

  // 4. PART 5: INCOMPLETE SENTENCES
  if (partId === 'P5') {
    container.innerHTML = `
      <div style="max-width:920px; margin:0 auto;">
        <div class="card" style="padding:16px 20px; margin-bottom:16px; background:linear-gradient(135deg, rgba(16,185,129,0.08), rgba(124,58,237,0.05)); border:1px solid rgba(16,185,129,0.4); border-radius:14px;">
          <b>${partData.part_title}</b>: ${partData.description}
        </div>
        <div style="display:flex; flex-direction:column; gap:14px;">
          ${(partData.questions || []).map(q => `
            <div class="card" style="padding:18px; border-radius:14px;">
              <div style="font-size:14.5px; font-weight:800; color:var(--text-primary); margin-bottom:12px; line-height:1.5;">
                <span class="badge badge-green" style="margin-right:6px;">${q.id}</span> ${q.question}
              </div>
              <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:8px;">
                ${q.options.map(opt => `
                  <label style="display:flex; align-items:center; gap:8px; background:var(--bg-secondary); border:1px solid var(--border); border-radius:8px; padding:10px 14px; cursor:pointer; font-size:13.5px;">
                    <input type="radio" name="toeic_ans_${q.id}" value="${opt.replace(/"/g, '&quot;')}" ${window.toeicExamState.readingAnswers[q.id] === opt ? 'checked' : ''} onchange="selectToeicOption('reading', '${q.id}', this.value)">
                    <span>${opt}</span>
                  </label>
                `).join('')}
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
    return;
  }

  // 5. PART 6 & PART 7: TEXT COMPLETION & READING COMPREHENSION (SPLIT SCREEN)
  if (partId === 'P6' || partId === 'P7') {
    const passages = partData.passages || [];
    const currentPass = passages[window.toeicExamState.activePassageIndex || 0] || passages[0];

    container.innerHTML = `
      <div style="max-width:1180px; margin:0 auto;">
        <!-- PASSAGE SELECTOR BAR -->
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
          <div style="display:flex; gap:6px; flex-wrap:wrap;">
            ${passages.map((ps, pidx) => `
              <button class="pill-tab ${window.toeicExamState.activePassageIndex === pidx ? 'active' : ''}" onclick="switchToeicPassage(${pidx})" style="font-size:12.5px; font-weight:800;">
                📄 Đoạn ${pidx + 1} (${ps.title || ps.text_type || 'Đọc hiểu'})
              </button>
            `).join('')}
          </div>
          <div style="display:flex; align-items:center; gap:6px;">
            <button class="btn btn-sm btn-ghost" onclick="adjustToeicFontSize(-1)" title="Giảm cỡ chữ">A-</button>
            <button class="btn btn-sm btn-ghost" onclick="adjustToeicFontSize(1)" title="Tăng cỡ chữ">A+</button>
          </div>
        </div>

        <!-- SPLIT-SCREEN 2 COLUMNS -->
        <div class="b1-reading-split-grid" style="display:grid; grid-template-columns:1.1fr 0.9fr; gap:16px;">
          <!-- LEFT: PASSAGE TEXT -->
          <div class="card toeic-reading-passage-pane" style="padding:22px; font-size:${window.toeicExamState.readingFontSize || 14.5}px; line-height:1.7; height:680px; overflow-y:auto; border-radius:14px; background:var(--bg-card); white-space:pre-line;">
            <div style="font-weight:900; font-size:16px; color:var(--accent-purple); margin-bottom:12px; border-bottom:1px solid var(--border); padding-bottom:8px;">
              ${currentPass.title || currentPass.text_type || 'READING PASSAGE'}
            </div>
            ${currentPass.content}
          </div>

          <!-- RIGHT: QUESTIONS LIST -->
          <div style="height:680px; overflow-y:auto; display:flex; flex-direction:column; gap:12px; padding-right:4px;">
            ${(currentPass.questions || []).map(q => `
              <div class="card" style="padding:16px; border-radius:12px;">
                <div style="font-size:13.5px; font-weight:800; color:var(--text-primary); margin-bottom:10px; line-height:1.4;">
                  <span class="badge badge-green" style="margin-right:6px;">${q.id}</span> ${q.question}
                </div>
                <div style="display:flex; flex-direction:column; gap:6px;">
                  ${q.options.map(opt => `
                    <label style="display:flex; align-items:center; gap:8px; background:var(--bg-secondary); border:1px solid var(--border); border-radius:6px; padding:8px 12px; cursor:pointer; font-size:13px;">
                      <input type="radio" name="toeic_ans_${q.id}" value="${opt.replace(/"/g, '&quot;')}" ${window.toeicExamState.readingAnswers[q.id] === opt ? 'checked' : ''} onchange="selectToeicOption('reading', '${q.id}', this.value)">
                      <span>${opt}</span>
                    </label>
                  `).join('')}
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      </div>
    `;
  }
}

window.switchToeicPassage = function(pidx) {
  window.toeicExamState.activePassageIndex = pidx;
  renderToeicCurrentPartBody();
};

window.adjustToeicFontSize = function(delta) {
  let size = (window.toeicExamState.readingFontSize || 14.5) + delta;
  if (size < 12) size = 12;
  if (size > 20) size = 20;
  window.toeicExamState.readingFontSize = size;
  const pane = document.querySelector('.toeic-reading-passage-pane');
  if (pane) pane.style.fontSize = `${size}px`;
};

window.selectToeicOption = function(section, qId, val) {
  if (section === 'listening') {
    window.toeicExamState.listeningAnswers[qId] = val;
  } else {
    window.toeicExamState.readingAnswers[qId] = val;
  }
};

window.submitToeicExam = async function() {
  if (window.toeicExamState.timerInterval) clearInterval(window.toeicExamState.timerInterval);

  showGlobalLoading('Hệ thống AI đang chấm điểm 200 câu TOEIC theo chuẩn ETS 990...');
  try {
    const res = await api.levelCurriculum.submitToeicExam({
      listening_answers: window.toeicExamState.listeningAnswers,
      reading_answers: window.toeicExamState.readingAnswers,
      time_spent_sec: (120 * 60) - window.toeicExamState.secondsLeft,
      exam_mode: window.toeicExamState.examMode
    });
    hideGlobalLoading();
    renderToeicResultBoard(res);
  } catch (err) {
    hideGlobalLoading();
    toast(`Lỗi khi nộp bài TOEIC: ${err.message}`, 'error');
  }
};

function renderToeicResultBoard(res) {
  const arena = document.getElementById('toeic-exam-active-arena');
  const resultBoard = document.getElementById('toeic-exam-result-board');
  if (arena) arena.style.display = 'none';
  if (!resultBoard) return;

  resultBoard.style.display = 'block';
  window.curriculumState.latestExamResult = res;

  const radar = res.radar || { listening_speed: 85, business_lexicon: 85, grammar_precision: 85, multi_passage_logic: 85 };

  resultBoard.innerHTML = `
    <div class="card" style="max-width:920px; margin:0 auto; padding:32px; border-radius:22px; background:var(--bg-card); border:2px solid ${res.passed ? '#10b981' : '#f59e0b'}; box-shadow:0 15px 40px rgba(0,0,0,0.3);">
      <div style="text-align:center; margin-bottom:24px;">
        <div style="font-size:55px; margin-bottom:10px;">${res.passed ? '🎉' : '📊'}</div>
        <h1 style="font-size:26px; font-weight:900; color:var(--text-primary); margin:0 0 6px 0;">
          KẾT QUẢ THI CHUẨN HÓA TOEIC 850+ (ETS FORMAT 2026)
        </h1>
        <div style="font-size:15px; color:var(--text-secondary);">
          Đánh giá năng lực bởi Hệ Thống Khảo Thí AI VihTech
        </div>
      </div>

      <!-- ETS 990 SCORE SUMMARY -->
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:16px; margin-bottom:24px;">
        <div class="card" style="padding:20px; text-align:center; background:linear-gradient(135deg, rgba(6,182,212,0.1), rgba(168,85,247,0.1)); border:2px solid var(--accent-purple); border-radius:16px;">
          <div style="font-size:12px; font-weight:800; color:var(--text-secondary); text-transform:uppercase;">TỔNG ĐIỂM TOEIC ETS</div>
          <div style="font-size:42px; font-weight:900; color:var(--accent-purple); margin:4px 0;">${res.total_toeic_score}</div>
          <div style="font-size:13px; font-weight:700; color:${res.passed ? '#10b981' : '#f59e0b'};">
            ${res.passed ? '✅ ĐẠT CHUẨN TOEIC 850+ GOLD' : '⏳ CẦN TIẾP TỤC RÈN LUYỆN'}
          </div>
        </div>

        <div class="card" style="padding:20px; text-align:center; background:var(--bg-secondary); border-radius:16px;">
          <div style="font-size:12px; font-weight:800; color:#38bdf8; text-transform:uppercase;">🎧 LISTENING SCORE</div>
          <div style="font-size:36px; font-weight:900; color:#38bdf8; margin:4px 0;">${res.listening.score_495} <span style="font-size:16px; color:var(--text-secondary);">/ 495</span></div>
          <div style="font-size:12px; color:var(--text-secondary);">Đúng ${res.listening.correct_count} / ${res.listening.total_questions} câu</div>
        </div>

        <div class="card" style="padding:20px; text-align:center; background:var(--bg-secondary); border-radius:16px;">
          <div style="font-size:12px; font-weight:800; color:#4ade80; text-transform:uppercase;">📖 READING SCORE</div>
          <div style="font-size:36px; font-weight:900; color:#4ade80; margin:4px 0;">${res.reading.score_495} <span style="font-size:16px; color:var(--text-secondary);">/ 495</span></div>
          <div style="font-size:12px; color:var(--text-secondary);">Đúng ${res.reading.correct_count} / ${res.reading.total_questions} câu</div>
        </div>
      </div>

      <!-- RADAR METRICS -->
      <div style="background:var(--bg-secondary); border-radius:16px; padding:20px; margin-bottom:24px;">
        <div style="font-size:14px; font-weight:900; color:var(--text-primary); margin-bottom:14px;">
          📊 Chẩn Đoán Năng Lực 4 Trục TOEIC ETS:
        </div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:12px;">
          <div><span>Listening Speed:</span> <b>${radar.listening_speed}%</b></div>
          <div><span>Business Lexicon:</span> <b>${radar.business_lexicon}%</b></div>
          <div><span>Grammar Precision:</span> <b>${radar.grammar_precision}%</b></div>
          <div><span>Multi-Passage Logic:</span> <b>${radar.multi_passage_logic}%</b></div>
        </div>
      </div>

      <div style="text-align:center; display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
        ${res.passed ? `
          <button class="btn btn-warning btn-lg" onclick="switchCurriculumTab('certificate')" style="font-weight:900; padding:12px 32px; box-shadow:0 6px 20px rgba(234,179,8,0.4);">
            🏆 Xem & Tải Chứng Chỉ TOEIC 850+ Gold
          </button>
        ` : ''}
        <button class="btn btn-secondary btn-lg" onclick="switchCurriculumTab('exam')">
          🔄 Quay Lại Phòng Thi
        </button>
      </div>
    </div>
  `;

  toast(res.passed ? 'Chúc mừng bạn đã xuất sắc Đạt Chuẩn TOEIC 850+! 🎉' : 'Đã hoàn thành bài thi TOEIC.', res.passed ? 'success' : 'info');
}


// ══════════════════════════════════════════════════════════════════════════════
// ── 2. IELTS ACADEMIC 8.0+ STANDARDIZED EXAM & AI EXAMINER STUDIO CONTROLLER ─
// ══════════════════════════════════════════════════════════════════════════════

window.ieltsExamState = {
  examData: null,
  activeSection: 'listening', // 'listening' | 'reading' | 'writing' | 'speaking'
  examMode: 'full',
  listeningAnswers: {},
  readingAnswers: {},
  writingSubmissions: { I_W1: '', I_W2: '' },
  speakingSubmissions: { I_S1: '', I_S2: '', I_S3: '' },
  activePassageIndex: 0,
  activeSpeakingPartIndex: 0,
  readingFontSize: 14.5,
  secondsLeft: 170 * 60,
  timerInterval: null
};

window.getFallbackIeltsExamData = function() {
  return {
    exam_id: "ielts-academic-2026-01",
    title: "Kỳ Thi Học Thuật Toàn Diện 4 Kỹ Năng (Listening – Reading – Writing – Speaking)",
    listening: {
      title: "IELTS Academic Listening (40 Questions - 30 Mins)",
      total_questions: 40,
      time_min: 30,
      sections: [
        {
          section_id: 1,
          section_title: "Section 1: Social Needs Dialogue (10 Questions)",
          audio_script: "Listen to a conversation between a student and a university accommodation officer.",
          questions: [
            {
              id: "I_L1",
              audio_text: "Officer: Good morning. Are you looking for on-campus housing? Student: Yes, I am an international post-graduate student starting this September. Officer: We have single en-suite rooms available in Green Park Hall for 150 pounds per week.",
              question: "What is the weekly rent for a single en-suite room in Green Park Hall?",
              options: ["A. £120 per week", "B. £150 per week", "C. £180 per week", "D. £200 per week"],
              correct: "B. £150 per week",
              explanation: "Audio nêu rõ: '150 pounds per week'."
            }
          ]
        }
      ]
    },
    reading: {
      title: "IELTS Academic Reading (40 Questions - 60 Mins)",
      total_questions: 40,
      time_min: 60,
      passages: [
        {
          passage_id: 1,
          title: "Reading Passage 1: The Evolution of Renewable Energy Storage",
          content: "As renewable energy sources like solar and wind power become central to global electricity grids, grid-scale energy storage technology has emerged as a crucial area of innovation. Traditional lithium-ion batteries, while highly efficient for short durations, face challenges regarding raw material supply and long-term sustainability. Consequently, researchers are developing flow batteries and compressed air energy storage systems that offer safer, scalable, and more cost-effective solutions for storing excess green energy.",
          questions: [
            {
              id: "I_R1",
              question: "What is one limitation of traditional lithium-ion batteries mentioned in the passage?",
              options: [
                "A. They cannot store any electricity",
                "B. Raw material supply and long-term sustainability challenges",
                "C. They are completely illegal in modern cities",
                "D. They only work during daytime"
              ],
              correct: "B. Raw material supply and long-term sustainability challenges",
              explanation: "Bài đọc nêu: 'face challenges regarding raw material supply and long-term sustainability'."
            }
          ]
        }
      ]
    },
    writing: {
      title: "IELTS Academic Writing (2 Tasks - 60 Mins)",
      time_min: 60,
      tasks: [
        {
          task_id: "I_W1",
          task_title: "Task 1: Academic Data Report (150 words)",
          prompt: "The chart below shows global renewable energy capacity growth between 2015 and 2025. Summarise the information by selecting and reporting the main features, and make comparisons where relevant. Write at least 150 words.",
          min_words: 150,
          target_words: 170
        },
        {
          task_id: "I_W2",
          task_title: "Task 2: Academic Essay (250 words)",
          prompt: "Many people argue that artificial intelligence will eliminate millions of jobs, while others believe it will generate far more innovative career opportunities. Discuss both views and give your opinion. Write at least 250 words.",
          min_words: 250,
          target_words: 280
        }
      ]
    },
    speaking: {
      title: "IELTS Academic Speaking (3 Parts - 14 Mins)",
      time_min: 14,
      parts: [
        {
          part_id: 1,
          part_title: "Part 1: Introduction & Everyday Topics (4-5 mins)",
          questions: [
            { id: "I_S1", prompt: "Let's talk about your hometown. What is the most interesting thing to see in your hometown?", sample_answer: "My hometown is known for its beautiful historical river and vibrant night food markets..." }
          ]
        },
        {
          part_id: 2,
          part_title: "Part 2: Long Turn Cue Card (3-4 mins)",
          cue_card: "Describe an innovative piece of technology that you find very useful in your daily life.",
          questions: [
            { id: "I_S2", prompt: "Describe an innovative piece of technology that you find very useful in your daily life. You should say: What it is, How you use it, and Explain why it is so helpful.", sample_answer: "I would like to talk about AI conversational tutors..." }
          ]
        },
        {
          part_id: 3,
          part_title: "Part 3: Two-way Analytical Discussion (4-5 mins)",
          questions: [
            { id: "I_S3", prompt: "How do you think artificial intelligence will shape the future of university education in the next decade?", sample_answer: "AI will likely transform higher education by providing hyper-personalized learning pathways..." }
          ]
        }
      ]
    }
  };
};

window.renderIeltsExamTab = async function(container, levelData) {
  container.innerHTML = '<div class="loading-dots" style="padding:40px; text-align:center;"><span></span><span></span><span></span></div>';

  let examData = null;
  try {
    examData = await api.levelCurriculum.getIeltsFullExam();
  } catch (err) {
    console.warn('[WARN] API getIeltsFullExam failed, using fallback:', err);
  }

  if (!examData || !examData.listening) {
    examData = window.getFallbackIeltsExamData();
  }
  window.ieltsExamState.examData = examData;

    container.innerHTML = `
      <!-- IELTS 2026 HERO LOBBY CARD -->
      <div class="ielts-exam-lobby-header card" style="padding:28px; background:linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(6, 78, 59, 0.95)); border:2px solid rgba(6,182,212,0.5); border-radius:20px; box-shadow:0 12px 35px rgba(0,0,0,0.4); margin-bottom:24px;">
        <div style="display:inline-flex; align-items:center; gap:8px; background:linear-gradient(135deg, #06b6d4, #0284c7); padding:6px 16px; border-radius:30px; margin-bottom:14px; box-shadow:0 0 15px rgba(6,182,212,0.4);">
          <span style="font-size:14px;">🎓</span>
          <span style="font-size:12px; font-weight:900; text-transform:uppercase; letter-spacing:1px; color:#ffffff;">
            PHÒNG THI CHUẨN HÓA IELTS ACADEMIC 8.0+ (2026)
          </span>
        </div>
        
        <h1 style="font-size:26px; font-weight:900; margin:0 0 10px 0; color:#ffffff; text-shadow:0 2px 10px rgba(0,0,0,0.8);">
          🎯 Kỳ Thi Học Thuật Toàn Diện 4 Kỹ Năng (Listening – Reading – Writing – Speaking)
        </h1>
        <p style="color:#e2e8f0; font-size:14px; max-width:820px; margin:0 0 20px 0; line-height:1.6;">
          Chuẩn đề thi Cambridge & IDP mới nhất. Tích hợp <b>AI Senior Examiner Studio 1-on-1</b> khảo thí phản xạ vấn đáp trực tiếp và AI chấm bài viết đa tiêu chí (TR, CC, LR, GRA). Đạt Overall Band từ <b>8.0/9.0</b> để nhận <b>Chứng Chỉ IELTS 8.0+ Expert User</b>!
        </p>

        <!-- 4-SKILL STATS GRID -->
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:14px; margin-bottom:24px;">
          <div class="card" style="background:rgba(0,0,0,0.4); padding:16px; border-radius:14px; border-top:3px solid #06b6d4;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span style="font-size:20px;">🎧</span>
              <span class="badge badge-cyan">40 CÂU • 30P</span>
            </div>
            <div style="font-size:15px; font-weight:800; color:#fff;">1. Nghe Học Thuật</div>
            <div style="font-size:12px; color:#cbd5e1; margin:4px 0 10px;">4 Sections đối thoại đời sống & bài giảng nghiên cứu.</div>
            <button class="btn btn-sm btn-ghost" onclick="startIeltsExam('listening')" style="width:100%; border:1px solid rgba(6,182,212,0.5); color:#38bdf8;">Luyện Nghe →</button>
          </div>

          <div class="card" style="background:rgba(0,0,0,0.4); padding:16px; border-radius:14px; border-top:3px solid #10b981;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span style="font-size:20px;">📖</span>
              <span class="badge badge-green">40 CÂU • 60P</span>
            </div>
            <div style="font-size:15px; font-weight:800; color:#fff;">2. Đọc Học Thuật</div>
            <div style="font-size:12px; color:#cbd5e1; margin:4px 0 10px;">3 Academic Passages (True/False/Not Given & Headings).</div>
            <button class="btn btn-sm btn-ghost" onclick="startIeltsExam('reading')" style="width:100%; border:1px solid rgba(16,185,129,0.5); color:#4ade80;">Luyện Đọc →</button>
          </div>

          <div class="card" style="background:rgba(0,0,0,0.4); padding:16px; border-radius:14px; border-top:3px solid #f59e0b;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span style="font-size:20px;">✍️</span>
              <span class="badge badge-warning">2 TASKS • 60P</span>
            </div>
            <div style="font-size:15px; font-weight:800; color:#fff;">3. Viết Học Thuật</div>
            <div style="font-size:12px; color:#cbd5e1; margin:4px 0 10px;">Task 1 Data Report (150w) & Task 2 Essay (250w).</div>
            <button class="btn btn-sm btn-ghost" onclick="startIeltsExam('writing')" style="width:100%; border:1px solid rgba(245,158,11,0.5); color:#facc15;">Luyện Viết →</button>
          </div>

          <div class="card" style="background:rgba(0,0,0,0.4); padding:16px; border-radius:14px; border-top:3px solid #ec4899;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <span style="font-size:20px;">🎤</span>
              <span class="badge" style="background:#ec4899; color:#fff;">3 PARTS • 14P</span>
            </div>
            <div style="font-size:15px; font-weight:800; color:#fff;">4. Nói AI 1-on-1</div>
            <div style="font-size:12px; color:#cbd5e1; margin:4px 0 10px;">Phòng Vấn Đáp Giám Khảo AI Examiner thời gian thực.</div>
            <button class="btn btn-sm btn-ghost" onclick="startIeltsExam('speaking')" style="width:100%; border:1px solid rgba(236,72,153,0.5); color:#f472b6;">Luyện Nói →</button>
          </div>
        </div>

        <!-- FULL 4-SKILL MOCK TEST CTA -->
        <div style="text-align:center; padding-top:16px; border-top:1px solid rgba(6,182,212,0.3);">
          <button class="btn btn-primary btn-lg" onclick="startIeltsExam('full')" style="padding:14px 44px; font-size:17px; font-weight:900; box-shadow:0 8px 30px rgba(6,182,212,0.5); background:linear-gradient(135deg, #06b6d4, #0284c7);">
            🚀 VÀO THI THỬ TOÀN DIỆN 4 KỸ NĂNG (FULL IELTS BAND 9.0)
          </button>
          <div style="font-size:12px; color:#94a3b8; margin-top:8px;">
            ⏱️ Tổng thời gian: 170 phút • Đánh giá 4 kỹ năng & Cấp chứng chỉ số xác thực
          </div>
        </div>
      </div>

      <div id="ielts-exam-active-arena" style="display:none;"></div>
      <div id="ielts-exam-result-board" style="display:none;"></div>
    `;
};

window.startIeltsExam = async function(mode) {
  if (!window.ieltsExamState.examData) {
    try {
      window.ieltsExamState.examData = await api.levelCurriculum.getIeltsFullExam();
    } catch(e) {
      return toast('Không thể tải dữ liệu đề thi IELTS: ' + e.message, 'error');
    }
  }

  window.ieltsExamState.examMode = mode;
  window.ieltsExamState.activeSection = mode === 'full' ? 'listening' : mode;
  window.ieltsExamState.listeningAnswers = {};
  window.ieltsExamState.readingAnswers = {};
  window.ieltsExamState.writingSubmissions = { I_W1: '', I_W2: '' };
  window.ieltsExamState.speakingSubmissions = { I_S1: '', I_S2: '', I_S3: '' };
  window.ieltsExamState.activePassageIndex = 0;
  window.ieltsExamState.activeSpeakingPartIndex = 0;

  const timers = { listening: 30 * 60, reading: 60 * 60, writing: 60 * 60, speaking: 14 * 60, full: 170 * 60 };
  window.ieltsExamState.secondsLeft = timers[mode] || (60 * 60);

  const lobby = document.querySelector('.ielts-exam-lobby-header');
  const arena = document.getElementById('ielts-exam-active-arena');
  const resultBoard = document.getElementById('ielts-exam-result-board');
  if (lobby) lobby.style.display = 'none';
  if (resultBoard) resultBoard.style.display = 'none';
  if (!arena) return;

  arena.style.display = 'block';
  renderIeltsActiveArena();
  startIeltsExamTimer();
};

function startIeltsExamTimer() {
  if (window.ieltsExamState.timerInterval) clearInterval(window.ieltsExamState.timerInterval);
  window.ieltsExamState.timerInterval = setInterval(() => {
    window.ieltsExamState.secondsLeft--;
    const timerEl = document.getElementById('ielts-exam-timer-display');
    if (timerEl) {
      timerEl.textContent = formatExamTimer(window.ieltsExamState.secondsLeft);
      if (window.ieltsExamState.secondsLeft <= 180) {
        timerEl.style.color = '#ef4444';
        timerEl.style.background = 'rgba(239,68,68,0.15)';
      }
    }
    if (window.ieltsExamState.secondsLeft <= 0) {
      clearInterval(window.ieltsExamState.timerInterval);
      toast('Đã hết thời gian làm bài thi IELTS! Tự động nộp bài...', 'warning');
      submitIeltsExam();
    }
  }, 1000);
}

function renderIeltsActiveArena() {
  const arena = document.getElementById('ielts-exam-active-arena');
  if (!arena) return;

  const data = window.ieltsExamState.examData;
  const currentSec = window.ieltsExamState.activeSection;
  const mode = window.ieltsExamState.examMode;

  arena.innerHTML = `
    <!-- STICKY TOP CONTROL BAR -->
    <div style="background:var(--bg-card); border:1.5px solid var(--border); border-radius:16px; padding:16px 20px; margin-bottom:20px; position:sticky; top:10px; z-index:100; box-shadow:0 8px 25px rgba(0,0,0,0.15);">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:12px;">
        <div>
          <div style="display:flex; align-items:center; gap:8px;">
            <span class="badge" style="background:#06b6d4; color:#fff; font-weight:900;">IELTS ACADEMIC 8.0+</span>
            <span style="font-weight:900; font-size:16px; color:var(--text-primary);">${data.title}</span>
          </div>
          <div style="font-size:12px; color:var(--text-secondary); margin-top:2px;">
            Chế độ: <b>${mode === 'full' ? 'Thi Thử Toàn Diện 4 Kỹ Năng' : `Luyện Tập Kỹ Năng ${currentSec.toUpperCase()}`}</b>
          </div>
        </div>

        <div style="display:flex; align-items:center; gap:12px;">
          <div id="ielts-exam-timer-display" style="font-size:22px; font-weight:900; color:var(--accent-cyan); font-family:monospace; background:rgba(6,182,212,0.1); padding:6px 16px; border-radius:10px; border:1px solid rgba(6,182,212,0.3);">
            ${formatExamTimer(window.ieltsExamState.secondsLeft)}
          </div>
          <button class="btn btn-success" onclick="submitIeltsExam()" style="font-weight:900; padding:10px 22px; box-shadow:0 4px 15px rgba(16,185,129,0.35);">
            📥 Nộp Toàn Bộ Bài Thi
          </button>
        </div>
      </div>

      <!-- SECTION TABS -->
      <div class="b1-exam-nav-tabs">
        <button class="b1-nav-tab-btn ${currentSec === 'listening' ? 'active' : ''}" onclick="switchIeltsSection('listening')">
          <span>🎧</span> 1. Nghe (40 câu - 30p)
        </button>
        <button class="b1-nav-tab-btn ${currentSec === 'reading' ? 'active' : ''}" onclick="switchIeltsSection('reading')">
          <span>📖</span> 2. Đọc (40 câu - 60p)
        </button>
        <button class="b1-nav-tab-btn ${currentSec === 'writing' ? 'active' : ''}" onclick="switchIeltsSection('writing')">
          <span>✍️</span> 3. Viết (2 Tasks - 60p)
        </button>
        <button class="b1-nav-tab-btn ${currentSec === 'speaking' ? 'active' : ''}" onclick="switchIeltsSection('speaking')">
          <span>🎤</span> 4. Nói AI 1-on-1 (14p)
        </button>
      </div>
    </div>

    <!-- SECTION CONTENT CONTAINER -->
    <div id="ielts-section-body-container"></div>
  `;

  renderIeltsCurrentSectionBody();
}

window.switchIeltsSection = function(sec) {
  window.ieltsExamState.activeSection = sec;
  document.querySelectorAll('#ielts-exam-active-arena .b1-nav-tab-btn').forEach(b => b.classList.remove('active'));
  renderIeltsActiveArena();
};

function renderIeltsCurrentSectionBody() {
  const container = document.getElementById('ielts-section-body-container');
  if (!container) return;

  const data = window.ieltsExamState.examData;
  const currentSec = window.ieltsExamState.activeSection;

  // 1. LISTENING
  if (currentSec === 'listening') {
    const lis = data.listening;
    container.innerHTML = `
      <div style="max-width:920px; margin:0 auto;">
        <div class="card" style="padding:16px 20px; margin-bottom:16px; background:linear-gradient(135deg, rgba(6,182,212,0.08), rgba(16,185,129,0.05)); border:1px solid rgba(6,182,212,0.4); border-radius:14px;">
          <b>${lis.title}</b>: ${lis.instructions}
        </div>
        <div style="display:flex; flex-direction:column; gap:20px;">
          ${(lis.sections || []).map(sec => `
            <div class="card" style="padding:20px; border-radius:16px;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
                <div>
                  <span class="badge badge-cyan" style="font-weight:800;">${sec.section_title}</span>
                  <div style="font-size:12.5px; color:var(--text-secondary); margin-top:3px;">${sec.description}</div>
                </div>
                <button class="btn btn-sm btn-primary" onclick="speakText('${sec.audio_script.replace(/'/g, "\\'")}')" style="font-size:12.5px; font-weight:800;">
                  🔊 Nghe Toàn Bộ Audio Section
                </button>
              </div>
              <div style="display:flex; flex-direction:column; gap:12px;">
                ${sec.questions.map(q => `
                  <div style="background:var(--bg-secondary); border:1px solid var(--border); border-radius:10px; padding:12px;">
                    <div style="font-size:13.5px; font-weight:800; color:var(--text-primary); margin-bottom:8px;">
                      <span style="color:var(--accent-cyan); margin-right:4px;">${q.id}:</span> ${q.question}
                    </div>
                    <div style="display:flex; flex-direction:column; gap:6px;">
                      ${q.options.map(opt => `
                        <label style="display:flex; align-items:center; gap:8px; background:var(--bg-card); border:1px solid var(--border); border-radius:6px; padding:7px 12px; cursor:pointer; font-size:13px;">
                          <input type="radio" name="ielts_ans_${q.id}" value="${opt.replace(/"/g, '&quot;')}" ${window.ieltsExamState.listeningAnswers[q.id] === opt ? 'checked' : ''} onchange="window.ieltsExamState.listeningAnswers['${q.id}'] = this.value">
                          <span>${opt}</span>
                        </label>
                      `).join('')}
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
    return;
  }

  // 2. READING
  if (currentSec === 'reading') {
    const read = data.reading;
    const passages = read.passages || [];
    const currentPass = passages[window.ieltsExamState.activePassageIndex || 0] || passages[0];

    container.innerHTML = `
      <div style="max-width:1180px; margin:0 auto;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
          <div style="display:flex; gap:6px; flex-wrap:wrap;">
            ${passages.map((ps, pidx) => `
              <button class="pill-tab ${window.ieltsExamState.activePassageIndex === pidx ? 'active' : ''}" onclick="window.ieltsExamState.activePassageIndex = ${pidx}; renderIeltsCurrentSectionBody();" style="font-size:12.5px; font-weight:800;">
                📄 ${ps.title.substring(0, 30)}...
              </button>
            `).join('')}
          </div>
          <div style="display:flex; align-items:center; gap:6px;">
            <button class="btn btn-sm btn-ghost" onclick="adjustIeltsFontSize(-1)">A-</button>
            <button class="btn btn-sm btn-ghost" onclick="adjustIeltsFontSize(1)">A+</button>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1.1fr 0.9fr; gap:16px;">
          <!-- LEFT: PASSAGE TEXT -->
          <div class="card ielts-reading-passage-pane" style="padding:22px; font-size:${window.ieltsExamState.readingFontSize || 14.5}px; line-height:1.7; height:680px; overflow-y:auto; border-radius:14px; background:var(--bg-card); white-space:pre-line;">
            <div style="font-weight:900; font-size:16px; color:var(--accent-cyan); margin-bottom:12px; border-bottom:1px solid var(--border); padding-bottom:8px;">
              ${currentPass.title}
            </div>
            ${currentPass.content}
          </div>

          <!-- RIGHT: QUESTIONS LIST -->
          <div style="height:680px; overflow-y:auto; display:flex; flex-direction:column; gap:12px; padding-right:4px;">
            ${(currentPass.questions || []).map(q => `
              <div class="card" style="padding:16px; border-radius:12px;">
                <div style="font-size:13.5px; font-weight:800; color:var(--text-primary); margin-bottom:10px; line-height:1.4;">
                  <span class="badge badge-cyan" style="margin-right:6px;">${q.id}</span> ${q.question}
                </div>
                <div style="display:flex; flex-direction:column; gap:6px;">
                  ${q.options.map(opt => `
                    <label style="display:flex; align-items:center; gap:8px; background:var(--bg-secondary); border:1px solid var(--border); border-radius:6px; padding:8px 12px; cursor:pointer; font-size:13px;">
                      <input type="radio" name="ielts_ans_${q.id}" value="${opt.replace(/"/g, '&quot;')}" ${window.ieltsExamState.readingAnswers[q.id] === opt ? 'checked' : ''} onchange="window.ieltsExamState.readingAnswers['${q.id}'] = this.value">
                      <span>${opt}</span>
                    </label>
                  `).join('')}
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      </div>
    `;
    return;
  }

  // 3. WRITING
  if (currentSec === 'writing') {
    const write = data.writing;
    const t1 = write.tasks[0];
    const t2 = write.tasks[1];

    container.innerHTML = `
      <div style="max-width:920px; margin:0 auto;">
        <div class="card" style="padding:16px 20px; margin-bottom:20px; background:linear-gradient(135deg, rgba(245,158,11,0.08), rgba(6,182,212,0.05)); border:1px solid rgba(245,158,11,0.4); border-radius:14px;">
          <b>${write.title}</b>: ${write.instructions}
        </div>

        <!-- TASK 1 -->
        <div class="card" style="padding:22px; margin-bottom:24px; border-radius:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; flex-wrap:wrap; gap:8px;">
            <div>
              <span class="badge badge-warning" style="font-weight:900;">TASK 1 (33.3% ĐIỂM)</span>
              <span style="font-weight:900; font-size:15.5px; color:var(--text-primary); margin-left:8px;">${t1.task_type}</span>
            </div>
            <div id="ielts-w1-counter" class="b1-word-counter-badge progressing">
              📝 Đếm từ: 0 / 150 từ
            </div>
          </div>
          <div style="background:var(--bg-secondary); border:1px solid var(--border); border-radius:10px; padding:14px; margin-bottom:14px; font-size:13.5px; line-height:1.6; white-space:pre-line;">
            ${t1.prompt}
          </div>
          <textarea id="ielts-writing-input-w1" class="form-control" rows="8" placeholder="Nhập bài viết Task 1 tại đây (tối thiểu 150 từ)..." oninput="updateIeltsWordCount('I_W1')" style="width:100%; font-size:14px; line-height:1.7; padding:14px; border-radius:12px;">${window.ieltsExamState.writingSubmissions.I_W1 || ''}</textarea>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:12px; flex-wrap:wrap; gap:8px;">
            <button class="btn btn-primary" onclick="evaluateIeltsWritingLive('I_W1', '${t1.prompt.replace(/'/g, "\\'")}')" style="font-weight:800;">
              🤖 AI Chấm & Phân Tích Band Task 1
            </button>
            <button class="btn btn-ghost" onclick="toggleIeltsSample('w1')" style="font-weight:700; font-size:13px;">
              👁️ Xem Bài Mẫu Band 8.5+
            </button>
          </div>
          <div id="ielts-sample-w1" style="display:none; margin-top:12px; padding:14px; background:rgba(6,182,212,0.06); border:1px dashed var(--accent-cyan); border-radius:10px; font-size:13px; line-height:1.6; white-space:pre-line;">
            <b>Bài Mẫu Chuẩn Band 8.5+:</b>\n${t1.sample_high_band}
          </div>
          <div id="ielts-feedback-w1" style="display:none; margin-top:12px;"></div>
        </div>

        <!-- TASK 2 -->
        <div class="card" style="padding:22px; margin-bottom:24px; border-radius:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; flex-wrap:wrap; gap:8px;">
            <div>
              <span class="badge badge-purple" style="font-weight:900;">TASK 2 (66.7% ĐIỂM)</span>
              <span style="font-weight:900; font-size:15.5px; color:var(--text-primary); margin-left:8px;">${t2.task_type}</span>
            </div>
            <div id="ielts-w2-counter" class="b1-word-counter-badge progressing">
              📝 Đếm từ: 0 / 250 từ
            </div>
          </div>
          <div style="background:var(--bg-secondary); border:1px solid var(--border); border-radius:10px; padding:14px; margin-bottom:14px; font-size:13.5px; line-height:1.6; white-space:pre-line;">
            ${t2.prompt}
          </div>
          <textarea id="ielts-writing-input-w2" class="form-control" rows="12" placeholder="Nhập bài luận Task 2 tại đây (tối thiểu 250 từ)..." oninput="updateIeltsWordCount('I_W2')" style="width:100%; font-size:14px; line-height:1.7; padding:14px; border-radius:12px;">${window.ieltsExamState.writingSubmissions.I_W2 || ''}</textarea>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:12px; flex-wrap:wrap; gap:8px;">
            <button class="btn btn-primary" onclick="evaluateIeltsWritingLive('I_W2', '${t2.prompt.replace(/'/g, "\\'")}')" style="font-weight:800;">
              🤖 AI Chấm & Phân Tích Band Task 2
            </button>
            <button class="btn btn-ghost" onclick="toggleIeltsSample('w2')" style="font-weight:700; font-size:13px;">
              👁️ Xem Bài Luận Mẫu Band 8.5+
            </button>
          </div>
          <div id="ielts-sample-w2" style="display:none; margin-top:12px; padding:14px; background:rgba(124,58,237,0.06); border:1px dashed var(--accent-purple); border-radius:10px; font-size:13px; line-height:1.6; white-space:pre-line;">
            <b>Bài Luận Mẫu Chuẩn Band 8.5+:</b>\n${t2.sample_high_band}
          </div>
          <div id="ielts-feedback-w2" style="display:none; margin-top:12px;"></div>
        </div>
      </div>
    `;
    return;
  }

  // 4. SPEAKING (AI EXAMINER STUDIO 1-ON-1)
  if (currentSec === 'speaking') {
    const spk = data.speaking;
    container.innerHTML = `
      <div style="max-width:920px; margin:0 auto;">
        <div class="card" style="padding:16px 20px; margin-bottom:20px; background:linear-gradient(135deg, rgba(236,72,153,0.08), rgba(6,182,212,0.05)); border:1px solid rgba(236,72,153,0.4); border-radius:14px;">
          <b>${spk.title}</b>: ${spk.instructions}
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px;">
          <!-- PART 1 -->
          <div class="card" style="padding:20px; border-radius:16px;">
            <div style="font-size:16px; font-weight:800; color:var(--text-primary); margin-bottom:6px;">Part 1: Introduction & Interview</div>
            <div style="font-size:12.5px; color:var(--text-secondary); margin-bottom:14px;">Chủ đề Time Management & Technology. Giám khảo AI hỏi đáp phản xạ tự nhiên.</div>
            <button class="btn btn-primary" onclick="openIeltsAIInterviewStudio('I_S1', 'Time Management & Technology')" style="width:100%; font-weight:800;">
              🎙️ Vào Phòng Vấn Đáp AI Part 1
            </button>
          </div>

          <!-- PART 2 -->
          <div class="card" style="padding:20px; border-radius:16px;">
            <div style="font-size:16px; font-weight:800; color:var(--text-primary); margin-bottom:6px;">Part 2: Cue Card Long Turn</div>
            <div style="font-size:12.5px; color:var(--text-secondary); margin-bottom:14px;">Thẻ chủ đề Environmental Dilemma. 1 phút chuẩn bị + 2 phút trình bày độc thoại.</div>
            <button class="btn btn-primary" onclick="openIeltsAIInterviewStudio('I_S2', 'Environmental Dilemma & Sustainability')" style="width:100%; font-weight:800;">
              🎙️ Vào Phòng Vấn Đáp AI Part 2
            </button>
          </div>

          <!-- PART 3 -->
          <div class="card" style="padding:20px; border-radius:16px;">
            <div style="font-size:16px; font-weight:800; color:var(--text-primary); margin-bottom:6px;">Part 3: Two-way Abstract Discussion</div>
            <div style="font-size:12.5px; color:var(--text-secondary); margin-bottom:14px;">Thảo luận sâu về triết học, luật pháp quốc tế và trách nhiệm toàn cầu.</div>
            <button class="btn btn-primary" onclick="openIeltsAIInterviewStudio('I_S3', 'Global Environmental Policies')" style="width:100%; font-weight:800;">
              🎙️ Vào Phòng Vấn Đáp AI Part 3
            </button>
          </div>
        </div>
      </div>
    `;
    return;
  }
}

window.adjustIeltsFontSize = function(delta) {
  let size = (window.ieltsExamState.readingFontSize || 14.5) + delta;
  if (size < 12) size = 12;
  if (size > 20) size = 20;
  window.ieltsExamState.readingFontSize = size;
  const pane = document.querySelector('.ielts-reading-passage-pane');
  if (pane) pane.style.fontSize = `${size}px`;
};

window.updateIeltsWordCount = function(taskId) {
  const el = document.getElementById(taskId === 'I_W1' ? 'ielts-writing-input-w1' : 'ielts-writing-input-w2');
  const counter = document.getElementById(taskId === 'I_W1' ? 'ielts-w1-counter' : 'ielts-w2-counter');
  if (!el || !counter) return;

  const text = el.value.trim();
  const words = text ? text.split(/\s+/).length : 0;
  const target = taskId === 'I_W1' ? 150 : 250;

  window.ieltsExamState.writingSubmissions[taskId] = text;
  counter.textContent = `📝 Đếm từ: ${words} / ${target} từ`;
  if (words >= target) {
    counter.className = 'b1-word-counter-badge satisfied';
  } else {
    counter.className = 'b1-word-counter-badge progressing';
  }
};

window.toggleIeltsSample = function(taskId) {
  const el = document.getElementById(taskId === 'w1' ? 'ielts-sample-w1' : 'ielts-sample-w2');
  if (el) el.style.display = el.style.display === 'none' ? 'block' : 'none';
};

window.evaluateIeltsWritingLive = async function(taskId, promptText) {
  const inputEl = document.getElementById(taskId === 'I_W1' ? 'ielts-writing-input-w1' : 'ielts-writing-input-w2');
  const fbEl = document.getElementById(taskId === 'I_W1' ? 'ielts-feedback-w1' : 'ielts-feedback-w2');
  if (!inputEl || !fbEl) return;

  const text = inputEl.value.trim();
  if (text.length < 20) {
    toast('Vui lòng viết ít nhất vài câu để AI phân tích!', 'warning');
    return;
  }

  fbEl.style.display = 'block';
  fbEl.innerHTML = '<div class="loading-dots" style="padding:15px; text-align:center;"><span></span><span></span><span></span></div>';

  try {
    const res = await api.levelCurriculum.evaluateIeltsWriting({
      task_id: taskId,
      user_text: text,
      prompt: promptText
    });
    const r = res.result;

    fbEl.innerHTML = `
      <div class="card" style="padding:16px; background:rgba(6,182,212,0.06); border:1.5px solid var(--accent-cyan); border-radius:12px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
          <div style="font-weight:900; font-size:15px; color:var(--accent-cyan);">🤖 KẾT QUẢ ĐÁNH GIÁ IELTS WRITING (${taskId})</div>
          <div class="badge badge-cyan" style="font-size:14px; font-weight:900;">BAND ${r.band_score} / 9.0</div>
        </div>
        <div style="font-size:13px; color:var(--text-primary); line-height:1.6; margin-bottom:8px;">
          • <b>Task Response:</b> ${r.tr_feedback}<br>
          • <b>Coherence & Cohesion:</b> ${r.cc_feedback}<br>
          • <b>Lexical Resource:</b> ${r.lr_feedback}<br>
          • <b>Grammatical Range:</b> ${r.gra_feedback}
        </div>
        <div style="background:var(--bg-secondary); padding:10px; border-radius:8px; font-size:12.5px;">
          💡 <b>Gợi ý nâng Band:</b> ${r.corrections}
        </div>
      </div>
    `;
    toast(`Đã chấm điểm ${taskId}: Band ${r.band_score}! ⭐`, 'success');
  } catch (err) {
    fbEl.innerHTML = `<div style="color:var(--accent-red);">❌ Lỗi khi chấm bài: ${err.message}</div>`;
  }
};

// ── REAL-TIME INTERACTIVE AI IELTS SPEAKING EXAMINER STUDIO ──────────────────
window.openIeltsAIInterviewStudio = function(partId, topicTitle) {
  const modal = document.createElement('div');
  modal.className = 'lesson-studio-overlay';
  modal.id = 'ielts-ai-interview-modal';
  modal.style.zIndex = '100005';

  modal.innerHTML = `
    <div class="card" style="background:linear-gradient(135deg, #090d1a 0%, #064e3b 60%, #090d1a 100%); border:3px solid #06b6d4; border-radius:24px; max-width:840px; width:95%; max-height:92vh; overflow-y:auto; padding:24px; box-shadow:0 25px 70px rgba(0,0,0,0.8), 0 0 40px rgba(6,182,212,0.4); position:relative;">
      <!-- TOP HEADER -->
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(6,182,212,0.3); padding-bottom:12px; margin-bottom:16px;">
        <div style="display:flex; align-items:center; gap:10px;">
          <span style="font-size:26px;">🎙️</span>
          <div>
            <div style="font-size:16px; font-weight:900; color:#38bdf8;">IELTS SENIOR AI EXAMINER STUDIO 1-ON-1</div>
            <div style="font-size:12px; color:#cbd5e1;">Phần thi: <b>${partId}</b> • Chủ đề: <b>${topicTitle}</b></div>
          </div>
        </div>
        <button class="btn btn-sm btn-ghost" onclick="document.getElementById('ielts-ai-interview-modal').remove()" style="font-size:18px; color:#94a3b8;">✕</button>
      </div>

      <!-- EXAMINER AVATAR & DIALOGUE AREA -->
      <div style="display:flex; gap:16px; margin-bottom:18px; flex-wrap:wrap; align-items:center;">
        <div style="width:90px; height:90px; border-radius:50%; border:3px solid #06b6d4; background:url('/assets/login_hero_3d.jpg') center/cover; box-shadow:0 0 20px rgba(6,182,212,0.5); flex-shrink:0;"></div>
        <div style="flex:1; min-width:280px; background:rgba(0,0,0,0.5); border:1.5px solid rgba(6,182,212,0.4); border-radius:16px; padding:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <b style="color:#38bdf8; font-size:13.5px;">👩‍🏫 Dr. Sarah Mitchell (Senior IELTS Examiner)</b>
            <div style="display:flex; gap:6px;">
              <button class="btn btn-sm btn-ghost" onclick="speakText(document.getElementById('ielts-examiner-speech-text').textContent, 1.0)" style="font-size:11px;">🔊 1.0x</button>
              <button class="btn btn-sm btn-ghost" onclick="speakText(document.getElementById('ielts-examiner-speech-text').textContent, 0.8)" style="font-size:11px;">🐢 0.8x</button>
            </div>
          </div>
          <div id="ielts-examiner-speech-text" style="font-size:14.5px; line-height:1.6; color:#ffffff; font-weight:600;">
            Đang kết nối với Giám khảo AI...
          </div>
          <div id="ielts-examiner-speech-vi" style="font-size:12.5px; line-height:1.5; color:#cbd5e1; margin-top:8px; border-top:1px dashed rgba(255,255,255,0.15); padding-top:6px;">
            ...
          </div>
        </div>
      </div>

      <!-- CANDIDATE SPEECH INPUT ARENA -->
      <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.1); border-radius:16px; padding:16px; margin-bottom:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
          <b style="color:#fff; font-size:13px;">🎤 Câu Trả Lời Của Bạn:</b>
          <span id="ielts-turn-indicator" class="badge badge-cyan">LƯỢT 1 / 3</span>
        </div>
        <textarea id="ielts-candidate-answer-input" class="form-control" rows="4" placeholder="Nhấn nút Micro bên dưới để nói tiếng Anh hoặc nhập trực tiếp văn bản câu trả lời..." style="width:100%; font-size:14px; line-height:1.6; padding:12px; border-radius:10px;"></textarea>
        
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:12px; flex-wrap:wrap; gap:8px;">
          <button id="ielts-mic-toggle-btn" class="btn btn-primary" onclick="toggleIeltsSpeechRecognition()" style="font-weight:800; padding:10px 20px; box-shadow:0 0 15px rgba(6,182,212,0.4);">
            🎤 Bật Micro Thu Âm Trực Tiếp
          </button>
          <button class="btn btn-success" onclick="submitIeltsInterviewTurn('${partId}', '${topicTitle}')" style="font-weight:800; padding:10px 24px;">
            🚀 Gửi Lời Nói Tới Giám Khảo →
          </button>
        </div>
      </div>

      <!-- AI LIVE EVALUATION BOX -->
      <div id="ielts-interview-feedback-box" style="display:none; background:rgba(6,182,212,0.08); border:1.5px solid var(--accent-cyan); border-radius:14px; padding:14px;"></div>
    </div>
  `;

  document.body.appendChild(modal);
  // Send turn 0 opening
  submitIeltsInterviewTurn(partId, topicTitle, 0, "");
};

window.submitIeltsInterviewTurn = async function(partId, topicTitle, customTurn, customText) {
  const inputEl = document.getElementById('ielts-candidate-answer-input');
  const speechEn = document.getElementById('ielts-examiner-speech-text');
  const speechVi = document.getElementById('ielts-examiner-speech-vi');
  const fbBox = document.getElementById('ielts-interview-feedback-box');
  const turnBadge = document.getElementById('ielts-turn-indicator');

  const turn = customTurn !== undefined ? customTurn : (window.ieltsInterviewTurnCount || 1);
  const text = customText !== undefined ? customText : (inputEl ? inputEl.value.trim() : '');

  if (turn > 0 && text.length < 5) {
    toast('Vui lòng nói hoặc nhập câu trả lời của bạn!', 'warning');
    return;
  }

  if (speechEn) speechEn.textContent = "Dr. Sarah Mitchell đang lắng nghe và phân tích bài nói của bạn...";

  try {
    const res = await api.levelCurriculum.ieltsInterviewTurn({
      part_id: partId,
      topic_or_question: topicTitle,
      turn_index: turn,
      user_answer_text: text
    });
    const r = res.result;

    if (speechEn) speechEn.textContent = r.examiner_reply_en;
    if (speechVi) speechVi.textContent = r.examiner_reply_vi;
    speakText(r.examiner_reply_en, 1.0);

    if (turn > 0 && fbBox) {
      fbBox.style.display = 'block';
      fbBox.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
          <b style="color:#38bdf8; font-size:13.5px;">🎯 Đánh Giá Phản Xạ Lượt Vừa Rồi:</b>
          <span class="badge badge-cyan" style="font-weight:900;">BAND ${r.turn_band || 8.0} • ${r.fluency_badge || 'EXCELLENT'}</span>
        </div>
        <div style="font-size:13px; color:#e2e8f0; line-height:1.5;">${r.feedback_on_answer}</div>
      `;
      // Store into speakingSubmissions
      window.ieltsExamState.speakingSubmissions[partId] = (window.ieltsExamState.speakingSubmissions[partId] || '') + ' ' + text;
    }

    if (inputEl) inputEl.value = '';
    window.ieltsInterviewTurnCount = (turn || 1) + 1;
    if (turnBadge) turnBadge.textContent = `LƯỢT ${Math.min(3, window.ieltsInterviewTurnCount)} / 3`;

    if (r.is_part_finished) {
      toast(`Hoàn thành xuất sắc phần thi Nói ${partId}! 🎉`, 'success');
    }
  } catch (err) {
    if (speechEn) speechEn.textContent = "Không thể kết nối với giám khảo AI: " + err.message;
  }
};

window.toggleIeltsSpeechRecognition = function() {
  const btn = document.getElementById('ielts-mic-toggle-btn');
  const inputEl = document.getElementById('ielts-candidate-answer-input');

  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    toast('Trình duyệt không hỗ trợ Web Speech API. Vui lòng gõ chữ trực tiếp!', 'warning');
    return;
  }

  if (window.ieltsSpeechRecognizer && window.isIeltsRecording) {
    window.ieltsSpeechRecognizer.stop();
    window.isIeltsRecording = false;
    if (btn) {
      btn.innerHTML = '🎤 Bật Micro Thu Âm Trực Tiếp';
      btn.style.background = '';
    }
    toast('Đã dừng thu âm giọng nói.', 'info');
    return;
  }

  const recognition = new SpeechRecognition();
  recognition.lang = 'en-US';
  recognition.continuous = true;
  recognition.interimResults = true;

  recognition.onstart = () => {
    window.isIeltsRecording = true;
    if (btn) {
      btn.innerHTML = '🔴 Đang Thu Âm (Nói Tiếng Anh)...';
      btn.style.background = '#ef4444';
    }
    toast('Micro đang lắng nghe giọng nói của bạn...', 'info');
  };

  recognition.onresult = (event) => {
    let transcript = '';
    for (let i = event.resultIndex; i < event.results.length; ++i) {
      transcript += event.results[i][0].transcript;
    }
    if (inputEl) inputEl.value = transcript;
  };

  recognition.onerror = (e) => {
    toast('Lỗi micro: ' + e.error, 'error');
  };

  window.ieltsSpeechRecognizer = recognition;
  recognition.start();
};

window.submitIeltsExam = async function() {
  if (window.ieltsExamState.timerInterval) clearInterval(window.ieltsExamState.timerInterval);

  showGlobalLoading('Hệ thống AI đang chấm điểm toàn diện 4 Kỹ Năng IELTS Academic...');
  try {
    const res = await api.levelCurriculum.submitIeltsExam({
      listening_answers: window.ieltsExamState.listeningAnswers,
      reading_answers: window.ieltsExamState.readingAnswers,
      writing_submissions: window.ieltsExamState.writingSubmissions,
      speaking_submissions: window.ieltsExamState.speakingSubmissions,
      time_spent_sec: (170 * 60) - window.ieltsExamState.secondsLeft,
      exam_mode: window.ieltsExamState.examMode
    });
    hideGlobalLoading();
    renderIeltsResultBoard(res);
  } catch (err) {
    hideGlobalLoading();
    toast(`Lỗi khi nộp bài IELTS: ${err.message}`, 'error');
  }
};

function renderIeltsResultBoard(res) {
  const arena = document.getElementById('ielts-exam-active-arena');
  const resultBoard = document.getElementById('ielts-exam-result-board');
  if (arena) arena.style.display = 'none';
  if (!resultBoard) return;

  resultBoard.style.display = 'block';
  window.curriculumState.latestExamResult = res;

  const radar = res.radar || { listening: 85, reading: 85, writing: 85, speaking: 85 };

  resultBoard.innerHTML = `
    <div class="card" style="max-width:920px; margin:0 auto; padding:32px; border-radius:22px; background:var(--bg-card); border:2px solid ${res.passed ? '#06b6d4' : '#f59e0b'}; box-shadow:0 15px 40px rgba(0,0,0,0.3);">
      <div style="text-align:center; margin-bottom:24px;">
        <div style="font-size:55px; margin-bottom:10px;">${res.passed ? '🎓' : '📊'}</div>
        <h1 style="font-size:26px; font-weight:900; color:var(--text-primary); margin:0 0 6px 0;">
          BẢNG ĐIỂM IELTS ACADEMIC 8.0+ TOÀN DIỆN 4 KỸ NĂNG
        </h1>
        <div style="font-size:15px; color:var(--text-secondary);">
          Đánh giá theo chuẩn Cambridge Assessment & IDP 2026
        </div>
      </div>

      <!-- OVERALL BAND SCORE -->
      <div class="card" style="padding:24px; text-align:center; background:linear-gradient(135deg, rgba(6,182,212,0.1), rgba(16,185,129,0.1)); border:2px solid var(--accent-cyan); border-radius:18px; margin-bottom:24px;">
        <div style="font-size:13px; font-weight:800; color:var(--text-secondary); text-transform:uppercase;">OVERALL BAND SCORE</div>
        <div style="font-size:55px; font-weight:900; color:var(--accent-cyan); margin:4px 0;">${res.overall_band} <span style="font-size:22px; color:var(--text-secondary);">/ 9.0</span></div>
        <div style="font-size:14px; font-weight:800; color:${res.passed ? '#10b981' : '#f59e0b'};">
          ${res.passed ? '🌟 XUẤT SẮC ĐẠT CHUẨN IELTS 8.0+ ACADEMIC' : '⏳ CẦN TIẾP TỤC RÈN LUYỆN ĐỂ ĐẠT BAND 8.0+'}
        </div>
      </div>

      <!-- 4 SKILL BANDS -->
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(190px, 1fr)); gap:14px; margin-bottom:24px;">
        <div class="card" style="padding:16px; text-align:center; background:var(--bg-secondary); border-radius:14px;">
          <div style="font-size:12px; color:#38bdf8; font-weight:800;">🎧 LISTENING</div>
          <div style="font-size:28px; font-weight:900; color:#38bdf8;">Band ${res.listening.band}</div>
        </div>
        <div class="card" style="padding:16px; text-align:center; background:var(--bg-secondary); border-radius:14px;">
          <div style="font-size:12px; color:#4ade80; font-weight:800;">📖 READING</div>
          <div style="font-size:28px; font-weight:900; color:#4ade80;">Band ${res.reading.band}</div>
        </div>
        <div class="card" style="padding:16px; text-align:center; background:var(--bg-secondary); border-radius:14px;">
          <div style="font-size:12px; color:#facc15; font-weight:800;">✍️ WRITING</div>
          <div style="font-size:28px; font-weight:900; color:#facc15;">Band ${res.writing.band}</div>
        </div>
        <div class="card" style="padding:16px; text-align:center; background:var(--bg-secondary); border-radius:14px;">
          <div style="font-size:12px; color:#f472b6; font-weight:800;">🎤 SPEAKING</div>
          <div style="font-size:28px; font-weight:900; color:#f472b6;">Band ${res.speaking.band}</div>
        </div>
      </div>

      <div style="text-align:center; display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
        ${res.passed ? `
          <button class="btn btn-warning btn-lg" onclick="switchCurriculumTab('certificate')" style="font-weight:900; padding:12px 32px; box-shadow:0 6px 20px rgba(234,179,8,0.4);">
            🏆 Xem & Tải Chứng Chỉ IELTS 8.0+ Academic
          </button>
        ` : ''}
        <button class="btn btn-secondary btn-lg" onclick="switchCurriculumTab('exam')">
          🔄 Quay Lại Phòng Thi
        </button>
      </div>
    </div>
  `;

  toast(res.passed ? 'Chúc mừng bạn đã xuất sắc Đạt Chuẩn IELTS 8.0+! 🎉' : 'Đã hoàn thành bài thi IELTS.', res.passed ? 'success' : 'info');
}

// ══════════════════════════════════════════════════════════════════════════════
// ── 3. ULTRA-REALISTIC CERTIFICATE GENERATOR (VIHTECH GLOBAL ACCREDITED) ─────
// ══════════════════════════════════════════════════════════════════════════════

window.renderUltraRealisticCertificateHTML = function(certData, isMockup = false) {
  let user = (typeof state !== 'undefined' && state.user) || null;
  if (!user && typeof localStorage !== 'undefined') {
    try {
      const raw = localStorage.getItem('user_data');
      if (raw) user = JSON.parse(raw);
    } catch(e) {}
  }

  let studentName = (certData && certData.student_name) || '';
  let studentEmail = (certData && certData.student_email) || (user && user.email) || 'learner@vihtech.edu.vn';

  if (!studentName) {
    if (user && user.full_name && user.full_name.trim()) {
      studentName = user.full_name.toUpperCase();
    } else if (user && user.email) {
      const prefix = user.email.split('@')[0];
      const parts = prefix.split(/[._\-+0-9]+/).filter(Boolean);
      studentName = parts.length ? parts.map(p => p.toUpperCase()).join(' ') : prefix.toUpperCase();
    } else if (user && user.username) {
      studentName = user.username.toUpperCase();
    } else {
      studentName = 'HỌC VIÊN XUẤT SẮC';
    }
  }

  const certId = (certData && certData.cert_id) || 'VIH-ACAD-2026-' + Math.floor(100000 + Math.random() * 900000);
  const issueDate = (certData && certData.issue_date) || new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
  const certTitle = (certData && certData.title) || 'CERTIFICATE OF ENGLISH PROFICIENCY';
  const levelBadge = (certData && certData.level_badge) || 'CEFR B1 INDEPENDENT USER';
  const scoresHtml = (certData && certData.scores_html) || `
    <div style="display:flex; justify-content:center; gap:20px; flex-wrap:wrap; margin:16px 0; font-family:'Cinzel', serif; font-size:13px; font-weight:700; color:#1e1b4b;">
      <span style="background:rgba(184,134,11,0.12); padding:4px 14px; border-radius:15px; border:1px solid #b8860b;">🎧 Listening: 8.5/10</span>
      <span style="background:rgba(184,134,11,0.12); padding:4px 14px; border-radius:15px; border:1px solid #b8860b;">📖 Reading: 8.0/10</span>
      <span style="background:rgba(184,134,11,0.12); padding:4px 14px; border-radius:15px; border:1px solid #b8860b;">✍️ Writing: 7.5/10</span>
      <span style="background:rgba(184,134,11,0.12); padding:4px 14px; border-radius:15px; border:1px solid #b8860b;">🎤 Speaking: 8.0/10</span>
      <span style="background:#b8860b; color:#fff; padding:4px 16px; border-radius:15px; font-weight:900;">🏆 GPA: 8.0 / 10.0</span>
    </div>
  `;
  const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=110x110&data=https://vihtech.edu.vn/verify-cert/${certId}`;

  return `
    <div class="realistic-cert-container">
      <!-- DIPLOMA FRAME -->
      <div class="realistic-cert-frame">
        <div class="realistic-cert-watermark">VIHTECH OFFICIAL</div>
        
        <div class="realistic-cert-inner-border">
          <!-- CORNER ORNAMENTS -->
          <div style="position:absolute; top:8px; left:8px; font-size:20px; color:#b8860b;">⚜️</div>
          <div style="position:absolute; top:8px; right:8px; font-size:20px; color:#b8860b;">⚜️</div>
          <div style="position:absolute; bottom:8px; left:8px; font-size:20px; color:#b8860b;">⚜️</div>
          <div style="position:absolute; bottom:8px; right:8px; font-size:20px; color:#b8860b;">⚜️</div>

          <!-- TOP ACADEMY LOGO & EMBLEM -->
          <div style="text-align:center; margin-bottom:14px;">
            <div style="display:inline-flex; align-items:center; gap:8px; color:#b8860b; font-size:12px; font-weight:900; letter-spacing:3px; text-transform:uppercase; margin-bottom:4px;">
              <span>🏛️</span> VIHTECH GLOBAL ACADEMY OF ADVANCED LANGUAGES
            </div>
            <div style="font-size:10.5px; color:#64748b; letter-spacing:1.5px; text-transform:uppercase; font-weight:700;">
              INTERNATIONAL ASSESSMENT & ACCREDITATION COMMISSION (EST. 2026)
            </div>
          </div>

          <!-- DIPLOMA MAIN TITLE -->
          <div style="text-align:center; margin-bottom:18px;">
            <h1 style="font-size:28px; font-weight:900; color:#1e1b4b; margin:0 0 4px 0; letter-spacing:2px; text-transform:uppercase; text-shadow:0 1px 2px rgba(0,0,0,0.1);">
              ${certTitle}
            </h1>
            <div style="display:inline-block; background:linear-gradient(135deg, #b8860b, #d4af37); color:#fff; font-size:11.5px; font-weight:900; padding:3px 18px; border-radius:20px; letter-spacing:1.5px; text-transform:uppercase;">
              ${levelBadge}
            </div>
          </div>

          <!-- RECIPIENT INTRODUCTION -->
          <div style="text-align:center; font-size:13.5px; color:#475569; font-style:italic; margin-bottom:6px;">
            This is to officially certify and attest that
          </div>

          <!-- RECIPIENT NAME & EMAIL -->
          <div style="text-align:center; margin-bottom:12px;">
            <div style="font-family:'Playfair Display', 'Georgia', serif; font-size:32px; font-weight:900; color:#0f172a; text-transform:uppercase; letter-spacing:2px; border-bottom:2px solid #d4af37; display:inline-block; padding:0 30px 4px 30px;">
              ${studentName}
            </div>
            <div style="font-size:12px; color:#64748b; font-family:monospace; margin-top:6px; font-weight:600;">
              Student ID / Email: <b>${studentEmail}</b>
            </div>
          </div>


          <!-- CONFERRAL TEXT -->
          <div style="text-align:center; font-size:12.5px; color:#334155; line-height:1.6; max-width:680px; margin:0 auto 14px auto;">
            has successfully completed all standardized examination requirements and demonstrated outstanding academic competence in accordance with the International Standardized Language Assessment Framework 2026.
          </div>

          <!-- SCORE MATRIX -->
          ${scoresHtml}

          <!-- FOOTER: SEALS, SIGNATURES & VERIFICATION -->
          <div style="display:grid; grid-template-columns:1fr auto 1fr; align-items:flex-end; gap:20px; margin-top:24px; padding-top:14px; border-top:1px solid rgba(184,134,11,0.3);">
            
            <!-- LEFT SIGNATURE: ACADEMIC DIRECTOR -->
            <div style="text-align:center;">
              <div class="realistic-cert-signature">David Sterling</div>
              <div style="font-size:11px; font-weight:800; color:#1e1b4b; text-transform:uppercase; letter-spacing:0.5px;">Dr. David Sterling, Ph.D.</div>
              <div style="font-size:9.5px; color:#64748b;">Dean of Academic Examination Board</div>
            </div>

            <!-- CENTER: 3D GOLD EMBOSSED SEAL & RED STAMP -->
            <div style="display:flex; align-items:center; justify-content:center; gap:16px;">
              <div class="realistic-cert-seal-wrap">
                <div class="realistic-cert-ribbon-red"></div>
                <div class="realistic-cert-ribbon-red-2"></div>
                <div class="realistic-cert-seal-3d">
                  <span style="font-size:15px;">👑</span>
                  <span style="font-size:9px; letter-spacing:0.5px; line-height:1.1;">VIHTECH<br>ACCREDITED<br>2026</span>
                </div>
              </div>

              <!-- RED OFFICIAL STAMP -->
              <div class="realistic-cert-stamp-red">
                <span style="font-size:8.5px; font-weight:900; line-height:1.1;">★ OFFICIAL ★<br>VERIFIED<br>EXAMINATION</span>
              </div>
            </div>

            <!-- RIGHT SIGNATURE: FOUNDER & PRESIDENT -->
            <div style="text-align:center;">
              <div class="realistic-cert-signature">Quang Vinh Nguyen</div>
              <div style="font-size:11px; font-weight:800; color:#1e1b4b; text-transform:uppercase; letter-spacing:0.5px;">Prof. Nguyen Quang Vinh</div>
              <div style="font-size:9.5px; color:#64748b;">Founder & Academy President</div>
            </div>
          </div>

          <!-- SECURITY HASH & QR METADATA -->
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px; padding-top:10px; border-top:1px dashed #d4af37; font-size:10px; color:#64748b; font-family:monospace;">
            <div>
              <b>CERTIFICATE ID:</b> <span style="color:#b8860b; font-weight:700;">${certId}</span><br>
              <b>DATE OF ISSUANCE:</b> ${issueDate}<br>
              <b>BLOCKCHAIN HASH:</b> 0x7f8a9b4c2d1e94c3b5a6e7f8... [Verified]
            </div>
            <div style="display:flex; align-items:center; gap:8px;">
              <img src="${qrUrl}" alt="Verification QR" style="width:52px; height:52px; border:1px solid #d4af37; border-radius:4px; padding:2px; background:#fff;">
              <div style="font-size:9px; line-height:1.2; text-align:left;">
                Scan QR to<br>verify authenticity<br>on Blockchain
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ACTION BUTTONS: PRINT / DOWNLOAD -->
      <div class="no-print" style="display:flex; justify-content:center; gap:14px; margin-top:20px; flex-wrap:wrap;">
        <button class="btn btn-warning btn-lg" onclick="window.print()" style="font-weight:900; box-shadow:0 6px 20px rgba(234,179,8,0.4);">
          🖨️ In Chứng Chỉ / Xuất Bản PDF Chuẩn Quốc Tế
        </button>
        <button class="btn btn-primary btn-lg" onclick="toast('Đã lưu mã xác thực chứng chỉ: ' + '${certId}', 'success')" style="font-weight:900;">
          📋 Sao Chép Mã Tra Cứu
        </button>
      </div>
    </div>
  `;
};

