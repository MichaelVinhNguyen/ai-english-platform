// api.js – Centralized API client for all backend calls
const API_BASE = '/api';
let authToken = localStorage.getItem('auth_token') || null;

const api = {
  setToken(token) { authToken = token; localStorage.setItem('auth_token', token); },
  clearToken()    { authToken = null;  localStorage.removeItem('auth_token'); localStorage.removeItem('user_data'); },

  async request(method, path, data = null, isFormData = false) {
    const headers = {};
    if (authToken) headers['Authorization'] = `Bearer ${authToken}`;
    if (!isFormData && data) headers['Content-Type'] = 'application/json';

    const options = { method, headers };
    if (data) options.body = isFormData ? data : JSON.stringify(data);

    try {
      const res = await fetch(`${API_BASE}${path}`, options);
      if (res.status === 401 && path !== '/auth/login' && path !== '/auth/quick-email-login') {
        api.clearToken();
        window.location.reload();
        return null;
      }
      const rawText = await res.text();
      let json = {};
      try {
        json = rawText ? JSON.parse(rawText) : {};
      } catch (parseErr) {
        json = { detail: rawText || `Lỗi phản hồi máy chủ (${res.status})` };
      }
      if (!res.ok) throw new Error(json.detail || json.message || `Lỗi yêu cầu (${res.status})`);
      return json;
    } catch (e) {
      if (e.message === 'Failed to fetch') throw new Error('Không thể kết nối đến máy chủ');
      throw e;
    }
  },

  get:    (path)       => api.request('GET', path),
  post:   (path, data) => api.request('POST', path, data),
  put:    (path, data) => api.request('PUT', path, data),
  delete: (path)       => api.request('DELETE', path),

  // ── AUTH ───────────────────────────────────────────────────────
  auth: {
    register:        d => api.post('/auth/register', d),
    login:           d => api.post('/auth/login', d),
    quickEmailLogin: d => api.post('/auth/quick-email-login', d),
    me:              () => api.get('/auth/me'),
  },

  // ── DASHBOARD ─────────────────────────────────────────────────
  dashboard: {
    stats:         () => api.get('/dashboard/stats'),
    leaderboard:   () => api.get('/dashboard/leaderboard'),
    recommend:     () => api.get('/dashboard/recommend'),
  },

  // ── AI TEACHER ────────────────────────────────────────────────
  teacher: {
    chat:     (d) => api.post('/teacher/chat', d),
    voice:    (d) => api.post('/teacher/voice', d),
    tts:      (d) => api.post('/teacher/tts', d),
    history:  (sessionId) => api.get(`/teacher/history${sessionId ? '?session_id='+sessionId : ''}`),
    sessions: () => api.get('/teacher/sessions'),
    roleplay: (d) => api.post('/teacher/roleplay', d),
  },

  // ── VOCABULARY ────────────────────────────────────────────────
  vocabulary: {
    list:       (p) => api.get(`/vocabulary/?${new URLSearchParams(p)}`),
    explain:    (d) => api.post('/vocabulary/explain', d),
    addToList:  (id) => api.post(`/vocabulary/add-to-my-list/${id}`),
    myList:     () => api.get('/vocabulary/my-list'),
    dueCards:   (n) => api.get(`/vocabulary/flashcards/due?limit=${n||20}`),
    review:     (d) => api.post('/vocabulary/flashcards/review', d),
    topics:     () => api.get('/vocabulary/topics'),
    stats:      () => api.get('/vocabulary/stats'),
  },

  // ── GRAMMAR ───────────────────────────────────────────────────
  grammar: {
    check:   (d) => api.post('/grammar/check', d),
    explain: (topic, level) => api.post(`/grammar/explain?topic=${encodeURIComponent(topic)}&level=${level||'B1'}`),
    rules:   (p) => api.get(`/grammar/rules${p ? '?'+new URLSearchParams(p) : ''}`),
    generateExercise: topic => api.post(`/grammar/generate-exercise?topic=${encodeURIComponent(topic)}`)
  },

  // ── QUIZ ──────────────────────────────────────────────────────
  quiz: {
    generate:       (d) => api.post('/quiz/generate', d),
    submit:         (d) => api.post('/quiz/submit', d),
    submitBatch:    (d) => api.post('/quiz/submit-batch', d),
    history:        () => api.get('/quiz/history'),
    getCuratedBank: () => api.get('/quiz/curated-bank'),
    getCategory:    (id) => api.get(`/quiz/category/${id}`),
  },

  // ── WRITING ───────────────────────────────────────────────────
  writing: {
    submit:   (d) => api.post('/writing/submit', d),
    history:  () => api.get('/writing/history'),
    prompts:  (type) => api.get(`/writing/prompts?writing_type=${type||'essay'}`),
  },

  // ── TRANSLATION ───────────────────────────────────────────────
  translation: {
    translate: (d) => api.post('/translation/translate', d),
    quick:     (text) => api.post(`/translation/quick?text=${encodeURIComponent(text)}`),
  },

  // ── COURSES ───────────────────────────────────────────────────
  courses: {
    list:           (p) => api.get(`/courses/${p ? '?'+new URLSearchParams(p) : ''}`),
    get:            (id) => api.get(`/courses/${id}`),
    enroll:         (id) => api.post(`/courses/${id}/enroll`),
    lesson:         (id) => api.get(`/courses/lesson/${id}`),
    completeLesson: (id) => api.post(`/courses/lesson/${id}/complete`),
    generateLesson: (topic, skill, level) =>
      api.post(`/courses/generate-lesson?topic=${encodeURIComponent(topic)}&skill=${skill}&level=${level}`),
    startSession:   (id) => api.post(`/courses/lesson/${id}/start-session`),
    submitAnswer:   (d)  => api.post(`/courses/lesson/submit-answer`, d),
  },

  // ── GAMIFICATION ──────────────────────────────────────────────
  gamification: {
    badges:   () => api.get('/gamification/badges'),
    myBadges: () => api.get('/gamification/my-badges'),
    missions: () => api.get('/gamification/missions'),
  },

  // ── COMMUNITY ─────────────────────────────────────────────────
  community: {
    posts:      (cat) => api.get(`/community/posts${cat ? '?category='+cat : ''}`),
    createPost: (d) => api.post('/community/posts', d),
    getPost:    (id) => api.get(`/community/posts/${id}`),
    comment:    (id, d) => api.post(`/community/posts/${id}/comments`, d),
  },

  // ── SPEAKING / LISTENING / READING ────────────────────────────
  speaking: {
    evaluate: (d) => api.post('/speaking/evaluate', d),
    topics:   (lvl) => api.get(`/speaking/topics?level=${lvl||'B1'}`),
    generatePractice: (topic, level) => api.post(`/speaking/generate-practice?topic=${encodeURIComponent(topic)}&level=${level||'B1'}`),
  },
  listening: {
    exercises: (lvl) => api.get(`/listening/exercises${lvl ? '?level='+lvl : ''}`),
    checkDictation: (d) => api.post('/listening/check-dictation', d),
    generateExercise: (topic, level) => api.post(`/listening/generate-exercise?topic=${encodeURIComponent(topic)}&level=${level||'B1'}`),
  },
  reading: {
    articles:   (p) => api.get(`/reading/articles${p ? '?'+new URLSearchParams(p) : ''}`),
    getArticle: (id) => api.get(`/reading/articles/${id}`),
    summarize:  (d) => api.post('/reading/summarize', d),
    questions:  (d) => api.post('/reading/questions', d),
  },

  // ── LEARNING PATH ─────────────────────────────────────────────
  learningPath: {
    generate: (d) => api.post('/learning-path/generate', d),
    myPath: () => api.get('/learning-path/my-path'),
    updateProgress: (week) => api.post(`/learning-path/update-progress?week_completed=${week}`),
    cefrInfo: () => api.get('/learning-path/cefr-info'),
  },

  // ── LEVEL CURRICULUM & EXAM HUB ───────────────────────────────
  levelCurriculum: {
    getOverview: () => api.get('/level-curriculum/overview'),
    getDetail: (lvl) => api.get(`/level-curriculum/detail/${lvl}`),
    getExam: (lvl) => api.get(`/level-curriculum/exam/${lvl}`),
    submitExam: (d) => api.post('/level-curriculum/submit-exam', d),
    completeModule: (d) => api.post('/level-curriculum/complete-module', d),
    evaluateWriting: (d) => api.post('/level-curriculum/evaluate-writing', d),
    evaluateSpeaking: (d) => api.post('/level-curriculum/evaluate-speaking', d),
    updateSRS: (d) => api.post('/level-curriculum/srs-review', d),
    // Exam Bank (30 Practice Tests Per Level)
    getExamBank: (lvl) => api.get(`/level-curriculum/exam-bank/${lvl}`),
    getExamBankTest: (lvl, testId) => api.get(`/level-curriculum/exam-bank/${lvl}/${testId}`),
    submitExamBank: (d) => api.post('/level-curriculum/submit-exam-bank', d),
    // 4-Skill Standardized Exam Suite (A1, A2, B1, B2, C1, C2)
    getFullExam: (lvl) => api.get(`/level-curriculum/full-exam/${lvl}`),
    submitFourSkillExam: (d) => api.post('/level-curriculum/submit-four-skill-exam', d),
    evaluateLevelWriting: (d) => api.post('/level-curriculum/evaluate-level-writing', d),
    levelInterviewTurn: (d) => api.post('/level-curriculum/level-ai-interview-turn', d),
    // B1 4-Skill Standardized Exam Suite (Legacy aliases)
    getB1FullExam: () => api.get('/level-curriculum/full-exam/B1'),
    submitB1Exam: (d) => api.post('/level-curriculum/submit-four-skill-exam', { ...d, level: 'B1' }),
    evaluateB1Writing: (d) => api.post('/level-curriculum/evaluate-level-writing', { ...d, level: 'B1' }),
    evaluateB1Speaking: (d) => api.post('/level-curriculum/evaluate-speaking', d),
    interviewTurn: (d) => api.post('/level-curriculum/level-ai-interview-turn', { ...d, level: 'B1' }),
    // TOEIC 850+ Standardized Exam Suite (ETS Format 2026)
    getToeicFullExam: () => api.get('/level-curriculum/toeic-full-exam'),
    submitToeicExam: (d) => api.post('/level-curriculum/submit-toeic-exam', d),
    // IELTS Academic 8.0+ Standardized Exam Suite
    getIeltsFullExam: () => api.get('/level-curriculum/ielts-full-exam'),
    submitIeltsExam: (d) => api.post('/level-curriculum/submit-ielts-exam', d),
    evaluateIeltsWriting: (d) => api.post('/level-curriculum/evaluate-ielts-writing-task', d),
    ieltsInterviewTurn: (d) => api.post('/level-curriculum/ielts-ai-interview-turn', d),
  },

  // ── QUIZ & EXERCISES (30 CURATED TESTS SUITE) ──────────────────
  quiz: {
    generate:    (d) => api.post('/quiz/generate', d),
    submit:      (d) => api.post('/quiz/submit', d),
    submitBatch: (d) => api.post('/quiz/submit-batch', d),
    history:     () => api.get('/quiz/history'),
    categories:  () => api.get('/quiz/categories'),
    curatedBank: () => api.get('/quiz/curated-bank'),
    getCategory: (id) => api.get(`/quiz/category/${id}`),
  },

  // ── COMMERCIAL ADMIN & ENTERPRISE CMS ─────────────────────────
  admin: {
    stats:                   () => api.get('/admin/stats'),
    commercialStats:         () => api.get('/admin/commercial-stats'),
    transactions:           (limit) => api.get(`/admin/transactions${limit ? '?limit='+limit : ''}`),
    approveTransaction:     (id) => api.post(`/admin/transactions/${id}/approve`),
    createManualTransaction:(d) => api.post('/admin/transactions/create-manual', d),
    coupons:                () => api.get('/admin/coupons'),
    createCoupon:           (d) => api.post('/admin/coupons', d),
    deleteCoupon:           (code) => api.delete(`/admin/coupons/${code}`),
    users:                   () => api.get('/admin/users'),
    studyActivity:           () => api.get('/admin/study-activity'),
    toggleUser:              (id) => api.post(`/admin/users/${id}/toggle-active`),
    changeRole:              (id, role) => api.post(`/admin/users/${id}/change-role?role=${role}`),
    adjustUserFunds:         (id, d) => api.post(`/admin/users/${id}/adjust-funds`, d),
    grantVip:                (id, d) => api.post(`/admin/users/${id}/grant-vip`, d),
    resetPassword:           (id, d) => api.post(`/admin/users/${id}/reset-password`, d),
    deleteUser:              (id) => api.delete(`/admin/users/${id}`),
    vocabularies:            (p) => api.get(`/admin/vocabularies${p ? '?'+new URLSearchParams(p) : ''}`),
    addVocabulary:           (d) => api.post('/admin/vocabularies', d),
    updateVocabulary:        (id, d) => api.put(`/admin/vocabularies/${id}`, d),
    deleteVocabulary:        (id) => api.delete(`/admin/vocabularies/${id}`),
    auditLogs:               (limit) => api.get(`/admin/audit-logs${limit ? '?limit='+limit : ''}`),
    systemHealth:            () => api.get('/admin/system-health'),
    seedData:                () => api.post('/admin/seed-data'),
    getAIConfig:             () => api.get('/admin/ai-config'),
    updateAIConfig:          (d) => api.post('/admin/ai-config', d),
    getAIProfiles:           () => api.get('/admin/ai-profiles'),
    saveAIProfile:           (d) => api.post('/admin/ai-profiles', d),
    deleteAIProfile:         (id) => api.delete(`/admin/ai-profiles/${id}`),
    activateAIProfile:       (id) => api.post(`/admin/ai-profiles/${id}/activate`),
    testAIConnection:        (d) => api.post('/admin/test-ai-connection', d),
  },
};

