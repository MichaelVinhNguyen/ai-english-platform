"""
append_common_phrases_view.py – Injects Common Phrases View and Interactive Studio into app.js
"""
import sys

NEW_CODE = r'''

// ═══════════════════════════════════════════════════════════════════════════════
// MODULE: CÂU NÓI THƯỜNG GẶP (COMMON PHRASES & SITUATIONAL DIALOGUES - 50 TOPICS)
// 2,500 Bilingual Q&A Pairs • AI Speech Audio • Cartoon Avatars • 4 Interactive Modes
// ═══════════════════════════════════════════════════════════════════════════════

const cpState = {
  topics: [],
  activeCategory: 'ALL',
  searchQuery: '',
  selectedTopic: null,
  topicPhrases: [],
  filteredPhrases: [],
  activeTab: 'dialogue', // 'dialogue' | 'flashcards' | 'reflex' | 'bookmarks'
  currentCardIdx: 0,
  cardFlipped: false,
  bookmarks: JSON.parse(localStorage.getItem('vihtech_phrase_bookmarks') || '[]'),
  reflex: {
    questions: [],
    currentIdx: 0,
    score: 0,
    streak: 0,
    selectedOption: null,
    answered: false
  },
  micActive: false,
  micPhraseId: null,
  micScore: null,
  micSpeaker: null
};

// ── REGISTER VIEW ─────────────────────────────────────────────────────────────
registerView('commonPhrases', () => `
  <div class="common-phrases-wrapper" style="padding: 10px 0 40px;">
    <div id="cp-view-container">
      <div style="display:flex;align-items:center;justify-content:center;height:240px">
        <div class="loading-dots"><span></span><span></span><span></span></div>
      </div>
    </div>
  </div>
`, async () => {
  await initCommonPhrasesView();
});

async function initCommonPhrasesView() {
  const container = document.getElementById('cp-view-container');
  if (!container) return;

  try {
    // 1. Fetch Topics
    let res = null;
    if (api && api.commonPhrases) {
      res = await api.commonPhrases.getTopics();
    }
    if (res && res.topics && res.topics.length) {
      cpState.topics = res.topics;
    } else if (window.STANDALONE_DATA && window.STANDALONE_DATA.common_phrases_topics) {
      cpState.topics = window.STANDALONE_DATA.common_phrases_topics;
    }

    // Default to main showcase
    renderCPShowcase();
  } catch (err) {
    console.error('Error loading common phrases:', err);
    if (window.STANDALONE_DATA && window.STANDALONE_DATA.common_phrases_topics) {
      cpState.topics = window.STANDALONE_DATA.common_phrases_topics;
      renderCPShowcase();
    } else {
      container.innerHTML = `
        <div class="card" style="text-align:center; padding: 40px 20px;">
          <div style="font-size: 40px; margin-bottom: 12px;">⚠️</div>
          <h3 style="margin-bottom: 8px;">Không thể tải dữ liệu Chủ đề</h3>
          <p style="color: var(--text-secondary); margin-bottom: 16px;">Vui lòng kiểm tra kết nối mạng hoặc thử lại.</p>
          <button class="btn btn-primary" onclick="initCommonPhrasesView()">🔄 Tải lại</button>
        </div>
      `;
    }
  }
}

// ── RENDER MAIN TOPIC SHOWCASE GRID ───────────────────────────────────────────
function renderCPShowcase() {
  const container = document.getElementById('cp-view-container');
  if (!container) return;

  const categories = [
    { id: 'ALL', name: '🌟 Tất cả', count: cpState.topics.length },
    { id: 'Daily Life', name: '☕ Đời sống & Hàng ngày', count: cpState.topics.filter(t => t.category === 'Daily Life').length },
    { id: 'Business & Career', name: '💼 Công sở & Kinh doanh', count: cpState.topics.filter(t => t.category === 'Business & Career').length },
    { id: 'Technology & AI', name: '💻 Công nghệ & Kỹ thuật số', count: cpState.topics.filter(t => t.category === 'Technology & AI').length },
    { id: 'Academic & Exams', name: '🎓 Học thuật & Luyện thi', count: cpState.topics.filter(t => t.category === 'Academic & Exams').length },
    { id: 'Culture & Social', name: '🎭 Văn hóa & Kỹ năng xã hội', count: cpState.topics.filter(t => t.category === 'Culture & Social').length },
  ];

  // Filter topics
  let filtered = cpState.topics;
  if (cpState.activeCategory !== 'ALL') {
    filtered = filtered.filter(t => t.category === cpState.activeCategory);
  }
  if (cpState.searchQuery.trim()) {
    const q = cpState.searchQuery.toLowerCase().trim();
    filtered = filtered.filter(t =>
      (t.title && t.title.toLowerCase().includes(q)) ||
      (t.title_vi && t.title_vi.toLowerCase().includes(q)) ||
      (t.description && t.description.toLowerCase().includes(q)) ||
      (t.description_vi && t.description_vi.toLowerCase().includes(q))
    );
  }

  container.innerHTML = `
    <!-- HERO HEADER -->
    <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.12) 0%, rgba(6, 182, 212, 0.12) 50%, rgba(124, 58, 237, 0.12) 100%); border: 1.5px solid rgba(16, 185, 129, 0.35); border-radius: 24px; padding: 28px 24px; margin-bottom: 24px; position: relative; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.04);">
      <div style="position: absolute; right: -15px; top: -15px; font-size: 110px; opacity: 0.12; user-select: none; pointer-events: none;">💬</div>
      
      <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px; position: relative; z-index: 1;">
        <div style="max-width: 680px;">
          <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4); color: #059669; padding: 4px 14px; border-radius: 20px; font-size: 12px; font-weight: 800; margin-bottom: 12px;">
            <span>✨</span> BẢN PHÁT HÀNH 2026 • 50 CHỦ ĐỀ CHUYÊN SÂU
          </div>
          <h1 style="font-size: 26px; font-weight: 900; margin: 0 0 10px; line-height: 1.3; background: linear-gradient(135deg, #059669, #0891b2, #7c3aed); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            💬 CÂU NÓI THƯỜNG GẶP & GIAO TIẾP TÌNH HUỐNG
          </h1>
          <p style="font-size: 14px; color: var(--text-secondary); margin: 0; line-height: 1.6;">
            Kho tư liệu đối thoại chuẩn quốc tế gồm <strong>50 Chủ đề</strong> và <strong>2,500 cặp câu hỏi - đáp song ngữ</strong> kèm phiên âm IPA, giải nghĩa chi tiết, phát âm AI bản ngữ và 4 chế độ luyện phản xạ thông minh!
          </p>
        </div>

        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
          <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px; padding: 12px 18px; text-align: center; min-width: 100px; box-shadow: var(--shadow-sm);">
            <div style="font-size: 22px; font-weight: 900; color: #10b981;">50</div>
            <div style="font-size: 11.5px; color: var(--text-muted); font-weight: 700;">Chủ đề</div>
          </div>
          <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px; padding: 12px 18px; text-align: center; min-width: 100px; box-shadow: var(--shadow-sm);">
            <div style="font-size: 22px; font-weight: 900; color: #06b6d4;">2,500</div>
            <div style="font-size: 11.5px; color: var(--text-muted); font-weight: 700;">Cặp Hỏi - Đáp</div>
          </div>
          <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px; padding: 12px 18px; text-align: center; min-width: 100px; box-shadow: var(--shadow-sm);">
            <div style="font-size: 22px; font-weight: 900; color: #8b5cf6;">100%</div>
            <div style="font-size: 11.5px; color: var(--text-muted); font-weight: 700;">AI Speech & IPA</div>
          </div>
        </div>
      </div>

      <!-- SEARCH & FILTER BAR -->
      <div style="margin-top: 24px; display: flex; flex-wrap: wrap; gap: 12px; align-items: center;">
        <div style="position: relative; flex: 1; min-width: 260px;">
          <span style="position: absolute; left: 14px; top: 50%; transform: translateY(-50%); font-size: 16px; color: #94a3b8;">🔍</span>
          <input type="text" id="cp-search-input" value="${escapeHtml(cpState.searchQuery)}" placeholder="Tìm kiếm câu nói, từ vựng hoặc chủ đề (Anh / Việt)..." 
                 oninput="handleCPSearch(this.value)"
                 style="width: 100%; padding: 12px 14px 12px 42px; border-radius: 14px; border: 1.5px solid var(--border); background: var(--bg-card); color: var(--text-primary); font-size: 14px; box-shadow: var(--shadow-sm); outline: none; transition: border-color 0.2s;">
          ${cpState.searchQuery ? `
            <button onclick="clearCPSearch()" style="position: absolute; right: 12px; top: 50%; transform: translateY(-50%); background: none; border: none; font-size: 14px; cursor: pointer; color: #94a3b8;">✖</button>
          ` : ''}
        </div>

        <button class="btn btn-outline" onclick="openCPGlobalSearchModal()" style="border-radius: 14px; font-weight: 700; padding: 11px 18px; display: flex; align-items: center; gap: 6px;">
          <span>⚡</span> Tra Cứu 2,500 Câu
        </button>
      </div>

      <!-- CATEGORY PILLS -->
      <div style="display: flex; gap: 8px; margin-top: 16px; overflow-x: auto; padding-bottom: 4px;" class="custom-scrollbar">
        ${categories.map(cat => `
          <button onclick="setCPCategory('${cat.id}')" 
                  style="padding: 8px 16px; border-radius: 20px; font-size: 13px; font-weight: 800; cursor: pointer; white-space: nowrap; transition: all 0.2s; border: none;
                         ${cpState.activeCategory === cat.id ?
                           'background: linear-gradient(135deg, #10b981, #06b6d4); color: #fff; box-shadow: 0 4px 12px rgba(16,185,129,0.3); transform: translateY(-2px);' :
                           'background: var(--bg-card); color: var(--text-secondary); border: 1px solid var(--border);'
                         }">
            ${cat.name} (${cat.count})
          </button>
        `).join('')}
      </div>
    </div>

    <!-- TOPICS GRID -->
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
      <div style="font-size: 15px; font-weight: 800; color: var(--text-primary);">
        📚 Danh Sách Chủ Đề (${filtered.length} / 50 Chủ đề)
      </div>
      <div style="font-size: 12.5px; color: var(--text-muted);">
        Nhấn vào bất kỳ chủ đề nào để mở Studio luyện tập
      </div>
    </div>

    ${filtered.length === 0 ? `
      <div class="card" style="text-align:center; padding: 60px 20px;">
        <div style="font-size: 48px; margin-bottom: 12px;">🔎</div>
        <h3 style="margin-bottom: 6px;">Không tìm thấy chủ đề phù hợp</h3>
        <p style="color: var(--text-secondary); margin-bottom: 16px;">Thử tìm kiếm với từ khóa khác hoặc xóa bộ lọc.</p>
        <button class="btn btn-primary" onclick="clearCPSearch()">Xem toàn bộ 50 chủ đề</button>
      </div>
    ` : `
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 18px;">
        ${filtered.map(t => renderCPTopicCard(t)).join('')}
      </div>
    `}
  `;
}

function renderCPTopicCard(topic) {
  const color = topic.color || '#10b981';
  return `
    <div class="cp-topic-card" onclick="openCPTopic(${topic.id})"
         style="background: var(--bg-card); border: 1px solid var(--border); border-radius: 20px; padding: 22px 20px; cursor: pointer; position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; min-height: 220px; box-shadow: var(--shadow-sm); transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);">
      
      <!-- Top Accent Line -->
      <div style="position: absolute; top: 0; left: 0; right: 0; height: 5px; background: ${color};"></div>
      
      <div>
        <!-- Top Row: Badges & Cartoon -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <div style="width: 44px; height: 44px; border-radius: 14px; background: ${color}18; border: 1.5px solid ${color}40; display: flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: 0 4px 10px rgba(0,0,0,0.06);">
              ${topic.cartoon || topic.icon || '💬'}
            </div>
            <div>
              <span style="font-size: 11px; font-weight: 800; color: ${color}; background: ${color}15; padding: 3px 8px; border-radius: 8px;">
                Chủ đề #${topic.id}
              </span>
            </div>
          </div>

          <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); color: #059669; font-size: 11px; font-weight: 800; padding: 4px 10px; border-radius: 20px; display: inline-flex; align-items: center; gap: 4px;">
            <span>💬</span> 50 Cặp Q&A
          </div>
        </div>

        <!-- Topic Title EN & VI -->
        <h3 style="font-size: 16.5px; font-weight: 800; margin: 0 0 4px; color: var(--text-primary); line-height: 1.35;">
          ${topic.title}
        </h3>
        <div style="font-size: 13.5px; font-weight: 700; color: #059669; margin-bottom: 10px;">
          ${topic.title_vi}
        </div>

        <!-- Description -->
        <p style="font-size: 12.5px; color: var(--text-secondary); margin: 0 0 16px; line-height: 1.5; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
          ${topic.description_vi || topic.description}
        </p>
      </div>

      <!-- Action Footer -->
      <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 14px; margin-top: 8px;">
        <span style="font-size: 12px; color: var(--text-muted); font-weight: 600;">
          ${topic.category}
        </span>
        <span style="font-size: 13px; font-weight: 800; color: ${color}; display: flex; align-items: center; gap: 4px;">
          Vào luyện tập <span>➔</span>
        </span>
      </div>
    </div>
  `;
}

// ── FILTER & SEARCH HANDLERS ──────────────────────────────────────────────────
function setCPCategory(catId) {
  cpState.activeCategory = catId;
  renderCPShowcase();
}

let cpSearchTimeout = null;
function handleCPSearch(val) {
  cpState.searchQuery = val;
  clearTimeout(cpSearchTimeout);
  cpSearchTimeout = setTimeout(() => {
    renderCPShowcase();
  }, 250);
}

function clearCPSearch() {
  cpState.searchQuery = '';
  cpState.activeCategory = 'ALL';
  renderCPShowcase();
}

// ── OPEN TOPIC STUDIO ─────────────────────────────────────────────────────────
async function openCPTopic(topicId) {
  const container = document.getElementById('cp-view-container');
  if (!container) return;

  container.innerHTML = `
    <div style="display:flex;align-items:center;justify-content:center;height:300px;flex-direction:column;gap:16px;">
      <div class="loading-dots"><span></span><span></span><span></span></div>
      <div style="font-size:14px;color:var(--text-secondary);font-weight:700;">Đang chuẩn bị 50 cặp câu đàm thoại...</div>
    </div>
  `;

  try {
    let res = null;
    if (api && api.commonPhrases) {
      res = await api.commonPhrases.getTopic(topicId);
    }

    if (res && res.topic && res.phrases) {
      cpState.selectedTopic = res.topic;
      cpState.topicPhrases = res.phrases;
    } else {
      // Fallback
      const topic = cpState.topics.find(t => String(t.id) === String(topicId)) || cpState.topics[0];
      const allPhrases = (window.STANDALONE_DATA && window.STANDALONE_DATA.common_phrases) || {};
      const phrases = allPhrases[String(topicId)] || allPhrases[String(topic.id)] || [];
      cpState.selectedTopic = topic;
      cpState.topicPhrases = phrases;
    }

    cpState.filteredPhrases = [...cpState.topicPhrases];
    cpState.activeTab = 'dialogue';
    cpState.currentCardIdx = 0;
    cpState.cardFlipped = false;

    renderCPTopicStudio();
  } catch (err) {
    console.error('Error opening topic:', err);
    toast('Không thể tải chi tiết chủ đề', 'error');
    renderCPShowcase();
  }
}

function backToCPTopics() {
  cpState.selectedTopic = null;
  cpState.topicPhrases = [];
  renderCPShowcase();
}

// ── RENDER TOPIC STUDIO (4 INTERACTIVE MODES) ─────────────────────────────────
function renderCPTopicStudio() {
  const container = document.getElementById('cp-view-container');
  if (!container || !cpState.selectedTopic) return;

  const topic = cpState.selectedTopic;
  const color = topic.color || '#10b981';

  container.innerHTML = `
    <!-- TOP BACK BAR -->
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; flex-wrap: wrap; gap: 12px;">
      <button class="btn btn-outline" onclick="backToCPTopics()" style="font-weight: 800; border-radius: 12px; display: inline-flex; align-items: center; gap: 8px; padding: 10px 18px;">
        <span>⬅️</span> Quay lại danh sách 50 Chủ đề
      </button>

      <div style="display: flex; gap: 8px; align-items: center;">
        <span style="font-size: 12px; font-weight: 800; color: ${color}; background: ${color}15; border: 1px solid ${color}40; padding: 5px 12px; border-radius: 20px;">
          ${topic.category}
        </span>
        <span style="font-size: 12px; font-weight: 800; color: #059669; background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.3); padding: 5px 12px; border-radius: 20px;">
          💬 ${cpState.topicPhrases.length} Cặp Q&A
        </span>
      </div>
    </div>

    <!-- TOPIC STUDIO HEADER -->
    <div style="background: linear-gradient(135deg, ${color}18 0%, rgba(6, 182, 212, 0.1) 100%); border: 1.5px solid ${color}40; border-radius: 24px; padding: 24px; margin-bottom: 24px; position: relative; overflow: hidden; box-shadow: var(--shadow-sm);">
      <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
        <div style="width: 72px; height: 72px; border-radius: 20px; background: ${color}25; border: 2px solid ${color}; display: flex; align-items: center; justify-content: center; font-size: 38px; box-shadow: 0 8px 20px ${color}30; flex-shrink: 0;">
          ${topic.cartoon || topic.icon || '💬'}
        </div>

        <div style="flex: 1; min-width: 260px;">
          <div style="font-size: 12px; font-weight: 800; color: ${color}; letter-spacing: 0.5px; margin-bottom: 4px;">
            CHỦ ĐỀ SỐ #${topic.id}
          </div>
          <h2 style="font-size: 22px; font-weight: 900; margin: 0 0 4px; color: var(--text-primary); line-height: 1.3;">
            ${topic.title}
          </h2>
          <div style="font-size: 16px; font-weight: 800; color: #059669; margin-bottom: 8px;">
            ${topic.title_vi}
          </div>
          <p style="font-size: 13.5px; color: var(--text-secondary); margin: 0; line-height: 1.5;">
            ${topic.description_vi || topic.description}
          </p>
        </div>
      </div>

      <!-- 4 MODE TABS -->
      <div style="display: flex; gap: 8px; margin-top: 24px; overflow-x: auto; padding-top: 16px; border-top: 1px solid rgba(0,0,0,0.06);" class="custom-scrollbar">
        <button onclick="switchCPTab('dialogue')" 
                style="padding: 10px 18px; border-radius: 14px; font-size: 13.5px; font-weight: 800; cursor: pointer; border: none; display: flex; align-items: center; gap: 8px; transition: all 0.2s; white-space: nowrap;
                       ${cpState.activeTab === 'dialogue' ?
                         'background: linear-gradient(135deg, #10b981, #06b6d4); color: #fff; box-shadow: 0 4px 14px rgba(16,185,129,0.35); transform: translateY(-2px);' :
                         'background: var(--bg-card); color: var(--text-secondary); border: 1px solid var(--border);'
                       }">
          <span>💬</span> 1. Đối thoại 1:1 (${cpState.topicPhrases.length})
        </button>

        <button onclick="switchCPTab('flashcards')" 
                style="padding: 10px 18px; border-radius: 14px; font-size: 13.5px; font-weight: 800; cursor: pointer; border: none; display: flex; align-items: center; gap: 8px; transition: all 0.2s; white-space: nowrap;
                       ${cpState.activeTab === 'flashcards' ?
                         'background: linear-gradient(135deg, #10b981, #06b6d4); color: #fff; box-shadow: 0 4px 14px rgba(16,185,129,0.35); transform: translateY(-2px);' :
                         'background: var(--bg-card); color: var(--text-secondary); border: 1px solid var(--border);'
                       }">
          <span>🃏</span> 2. Thẻ 3D Song Ngữ
        </button>

        <button onclick="switchCPTab('reflex')" 
                style="padding: 10px 18px; border-radius: 14px; font-size: 13.5px; font-weight: 800; cursor: pointer; border: none; display: flex; align-items: center; gap: 8px; transition: all 0.2s; white-space: nowrap;
                       ${cpState.activeTab === 'reflex' ?
                         'background: linear-gradient(135deg, #10b981, #06b6d4); color: #fff; box-shadow: 0 4px 14px rgba(16,185,129,0.35); transform: translateY(-2px);' :
                         'background: var(--bg-card); color: var(--text-secondary); border: 1px solid var(--border);'
                       }">
          <span>⚡</span> 3. Thử thách phản xạ
        </button>

        <button onclick="switchCPTab('bookmarks')" 
                style="padding: 10px 18px; border-radius: 14px; font-size: 13.5px; font-weight: 800; cursor: pointer; border: none; display: flex; align-items: center; gap: 8px; transition: all 0.2s; white-space: nowrap;
                       ${cpState.activeTab === 'bookmarks' ?
                         'background: linear-gradient(135deg, #10b981, #06b6d4); color: #fff; box-shadow: 0 4px 14px rgba(16,185,129,0.35); transform: translateY(-2px);' :
                         'background: var(--bg-card); color: var(--text-secondary); border: 1px solid var(--border);'
                       }">
          <span>⭐</span> 4. Đã lưu (${getTopicBookmarkCount()})
        </button>
      </div>
    </div>

    <!-- ACTIVE TAB BODY -->
    <div id="cp-tab-content">
      ${renderActiveCPTab()}
    </div>
  `;
}

function switchCPTab(tab) {
  cpState.activeTab = tab;
  renderCPTopicStudio();
}

function renderActiveCPTab() {
  if (cpState.activeTab === 'dialogue') {
    return renderCPDialogueTab();
  } else if (cpState.activeTab === 'flashcards') {
    return renderCPFlashcardsTab();
  } else if (cpState.activeTab === 'reflex') {
    return renderCPReflexTab();
  } else if (cpState.activeTab === 'bookmarks') {
    return renderCPBookmarksTab();
  }
  return '';
}

// ── 1. DIALOGUE TAB (ALL 50 PAIRS) ────────────────────────────────────────────
function renderCPDialogueTab() {
  const phrases = cpState.filteredPhrases;

  return `
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 12px;">
      <div style="display: flex; align-items: center; gap: 8px;">
        <span style="font-weight: 800; font-size: 15px;">💬 Các cặp hội thoại chuẩn tình huống (${phrases.length} câu)</span>
      </div>

      <div style="display: flex; gap: 8px; align-items: center;">
        <button class="btn btn-outline btn-sm" onclick="playAllPhrasesInTopic()" style="border-radius: 10px; font-weight: 700;">
          🔊 Tự động phát toàn bộ
        </button>
      </div>
    </div>

    <div style="display: flex; flex-direction: column; gap: 20px;">
      ${phrases.map((p, idx) => renderCPDialogueItem(p, idx)).join('')}
    </div>
  `;
}

function renderCPDialogueItem(p, idx) {
  const isBookmarked = cpState.bookmarks.includes(p.id);

  return `
    <div class="cp-dialogue-card" id="phrase-card-${p.id}"
         style="background: var(--bg-card); border: 1.5px solid var(--border); border-radius: 20px; padding: 22px 20px; box-shadow: var(--shadow-sm); transition: border-color 0.2s;">
      
      <!-- Situation & Difficulty Header -->
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 8px;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="font-size: 12px; font-weight: 900; color: #fff; background: linear-gradient(135deg, #10b981, #06b6d4); padding: 3px 10px; border-radius: 20px;">
            #${p.order_index || (idx + 1)}
          </span>
          <span style="font-size: 12.5px; font-weight: 800; color: #3b82f6; background: rgba(59, 130, 246, 0.1); padding: 3px 10px; border-radius: 8px;">
            📌 ${p.situation || 'Giao tiếp tình huống'}
          </span>
          <span style="font-size: 11px; font-weight: 700; color: #8b5cf6; background: rgba(139, 92, 246, 0.1); padding: 3px 8px; border-radius: 8px;">
            ${p.difficulty || 'Intermediate'}
          </span>
        </div>

        <button onclick="toggleCPBookmark(${p.id})" title="${isBookmarked ? 'Bỏ lưu' : 'Lưu câu này'}"
                style="background: none; border: none; cursor: pointer; font-size: 20px; color: ${isBookmarked ? '#f59e0b' : '#94a3b8'}; transition: transform 0.2s;">
          ${isBookmarked ? '★' : '☆'}
        </button>
      </div>

      <!-- QUESTION CONTAINER (Speaker 1) -->
      <div style="background: rgba(99, 102, 241, 0.05); border: 1px solid rgba(99, 102, 241, 0.2); border-radius: 16px; padding: 16px; margin-bottom: 12px; position: relative;">
        <div style="display: flex; gap: 14px; align-items: flex-start;">
          <div style="width: 42px; height: 42px; border-radius: 12px; background: #e0e7ff; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; box-shadow: 0 2px 6px rgba(0,0,0,0.06);">
            ${p.q_avatar || '🙋‍♀️'}
          </div>

          <div style="flex: 1;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
              <span style="font-size: 11.5px; font-weight: 800; color: #4f46e5; text-transform: uppercase;">
                ${p.q_speaker || 'Speaker A'} (Hỏi)
              </span>
              <div style="display: flex; gap: 4px;">
                <button class="btn-voice-mini" onclick="speakText('${escapeQuotes(p.q_text)}', 'en-US')" title="Nghe phát âm chuẩn">
                  🔊
                </button>
                <button class="btn-voice-mini" onclick="speakText('${escapeQuotes(p.q_text)}', 'en-US', 0.75)" title="Nghe chậm (0.75x)">
                  🐢
                </button>
                <button class="btn-voice-mini" onclick="startCPMicPractice(${p.id}, 'Q', '${escapeQuotes(p.q_text)}')" title="Luyện nói câu này bằng Mic">
                  🎤
                </button>
              </div>
            </div>

            <!-- English Text -->
            <div style="font-size: 15.5px; font-weight: 800; color: var(--text-primary); margin-bottom: 4px; line-height: 1.4;">
              ${p.q_text}
            </div>

            <!-- IPA -->
            <div style="font-size: 12.5px; font-family: monospace; color: #6366f1; margin-bottom: 6px;">
              ${p.q_ipa || ''}
            </div>

            <!-- Vietnamese -->
            <div style="font-size: 13.5px; font-weight: 600; color: var(--text-secondary); line-height: 1.4;">
              🇻🇳 ${p.q_vi}
            </div>

            <!-- Live Speech Recognition Feedback -->
            <div id="mic-feedback-${p.id}-Q" style="display:none; margin-top: 8px;"></div>
          </div>
        </div>
      </div>

      <!-- ANSWER CONTAINER (Speaker 2) -->
      <div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 16px; padding: 16px; margin-bottom: 12px; position: relative;">
        <div style="display: flex; gap: 14px; align-items: flex-start;">
          <div style="width: 42px; height: 42px; border-radius: 12px; background: #d1fae5; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; box-shadow: 0 2px 6px rgba(0,0,0,0.06);">
            ${p.a_avatar || '🙋‍♂️'}
          </div>

          <div style="flex: 1;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
              <span style="font-size: 11.5px; font-weight: 800; color: #059669; text-transform: uppercase;">
                ${p.a_speaker || 'Speaker B'} (Đáp)
              </span>
              <div style="display: flex; gap: 4px;">
                <button class="btn-voice-mini" onclick="speakText('${escapeQuotes(p.a_text)}', 'en-US')" title="Nghe phát âm chuẩn">
                  🔊
                </button>
                <button class="btn-voice-mini" onclick="speakText('${escapeQuotes(p.a_text)}', 'en-US', 0.75)" title="Nghe chậm (0.75x)">
                  🐢
                </button>
                <button class="btn-voice-mini" onclick="startCPMicPractice(${p.id}, 'A', '${escapeQuotes(p.a_text)}')" title="Luyện nói câu này bằng Mic">
                  🎤
                </button>
              </div>
            </div>

            <!-- English Text -->
            <div style="font-size: 15.5px; font-weight: 800; color: var(--text-primary); margin-bottom: 4px; line-height: 1.4;">
              ${p.a_text}
            </div>

            <!-- IPA -->
            <div style="font-size: 12.5px; font-family: monospace; color: #059669; margin-bottom: 6px;">
              ${p.a_ipa || ''}
            </div>

            <!-- Vietnamese -->
            <div style="font-size: 13.5px; font-weight: 600; color: var(--text-secondary); line-height: 1.4;">
              🇻🇳 ${p.a_vi}
            </div>

            <!-- Live Speech Recognition Feedback -->
            <div id="mic-feedback-${p.id}-A" style="display:none; margin-top: 8px;"></div>
          </div>
        </div>
      </div>

      <!-- TIPS & KEY VOCAB FOOTER -->
      <div style="background: rgba(245, 158, 11, 0.06); border: 1px solid rgba(245, 158, 11, 0.2); border-radius: 12px; padding: 10px 14px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 10px; font-size: 12.5px;">
        <div style="color: #b45309; display: flex; align-items: center; gap: 6px; flex: 1; min-width: 200px;">
          <span>💡</span> <strong>Mẹo giao tiếp:</strong> ${p.tips || 'Chú ý nối âm tự nhiên và hạ giọng ở cuối câu trần thuật.'}
        </div>

        <div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap;">
          <span style="color: #64748b; font-weight: 700;">🔑 Từ khóa:</span>
          ${(p.key_vocab || '').split(',').map(w => w.trim()).filter(Boolean).map(w => `
            <span style="background: rgba(255,255,255,0.8); border: 1px solid rgba(245,158,11,0.3); color: #92400e; padding: 2px 8px; border-radius: 6px; font-size: 11px; font-weight: 800;">
              ${w}
            </span>
          `).join('')}
        </div>
      </div>
    </div>
  `;
}

// ── 2. 3D FLASHCARDS TAB ──────────────────────────────────────────────────────
function renderCPFlashcardsTab() {
  const phrases = cpState.topicPhrases;
  if (!phrases || !phrases.length) return '<div class="card"><p>Chưa có dữ liệu thẻ flashcard.</p></div>';

  const idx = cpState.currentCardIdx;
  const p = phrases[idx];
  const total = phrases.length;
  const isFlipped = cpState.cardFlipped;

  return `
    <div style="max-width: 680px; margin: 0 auto; text-align: center;">
      <!-- Flashcard Controls & Counter -->
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div style="font-size: 14px; font-weight: 800; color: var(--text-primary);">
          🃏 Thẻ số: <span style="color:#10b981;">${idx + 1}</span> / ${total}
        </div>

        <div style="display: flex; gap: 8px;">
          <button class="btn btn-outline btn-sm" onclick="shuffleCPCards()" style="border-radius: 10px;">
            🔀 Trộn thẻ
          </button>
          <button class="btn btn-outline btn-sm" onclick="playCPCardAudioPair()" style="border-radius: 10px; font-weight: 700;">
            🔊 Nghe cả cặp
          </button>
        </div>
      </div>

      <!-- PROGRESS BAR -->
      <div style="width: 100%; height: 6px; background: var(--border); border-radius: 10px; margin-bottom: 24px; overflow: hidden;">
        <div style="height: 100%; width: ${((idx + 1) / total) * 100}%; background: linear-gradient(90deg, #10b981, #06b6d4); transition: width 0.3s ease;"></div>
      </div>

      <!-- 3D FLIP CARD -->
      <div class="cp-3d-card-container" onclick="flipCPCard()"
           style="perspective: 1000px; cursor: pointer; min-height: 380px; margin-bottom: 24px;">
        <div class="cp-3d-card ${isFlipped ? 'flipped' : ''}"
             style="position: relative; width: 100%; min-height: 380px; text-align: center; transition: transform 0.6s cubic-bezier(0.4, 0.2, 0.2, 1); transform-style: preserve-3d; border-radius: 24px; box-shadow: 0 16px 40px rgba(0,0,0,0.08);">
          
          <!-- FRONT: QUESTION -->
          <div style="position: absolute; width: 100%; height: 100%; backface-visibility: hidden; background: var(--bg-card); border: 2px solid rgba(99, 102, 241, 0.35); border-radius: 24px; padding: 32px 24px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box; text-align: center;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; font-weight: 800; background: rgba(99, 102, 241, 0.12); color: #4f46e5; padding: 4px 12px; border-radius: 20px;">
                MẶT TRƯỚC: CÂU HỎI / GỢI MỞ
              </span>
              <span style="font-size: 12px; color: var(--text-muted); font-weight: 700;">
                📌 ${p.situation || 'Tình huống'}
              </span>
            </div>

            <div style="margin: 24px 0;">
              <div style="font-size: 48px; margin-bottom: 12px;">${p.q_avatar || '🙋‍♀️'}</div>
              <div style="font-size: 12px; font-weight: 800; color: #4f46e5; text-transform: uppercase; margin-bottom: 6px;">
                ${p.q_speaker || 'Speaker A'}
              </div>
              <h3 style="font-size: 20px; font-weight: 900; color: var(--text-primary); margin: 0 0 8px; line-height: 1.4;">
                ${p.q_text}
              </h3>
              <div style="font-size: 14px; font-family: monospace; color: #6366f1; margin-bottom: 12px;">
                ${p.q_ipa || ''}
              </div>
              <div style="font-size: 15px; font-weight: 700; color: #059669;">
                🇻🇳 ${p.q_vi}
              </div>
            </div>

            <div style="display: flex; justify-content: center; align-items: center; gap: 8px;">
              <button class="btn btn-sm btn-outline" onclick="event.stopPropagation(); speakText('${escapeQuotes(p.q_text)}', 'en-US')" style="border-radius: 12px; font-weight: 700;">
                🔊 Nghe câu hỏi
              </button>
              <span style="font-size: 12px; color: var(--text-muted); font-weight: 600;">
                (Nhấn thẻ để lật xem câu đáp)
              </span>
            </div>
          </div>

          <!-- BACK: ANSWER -->
          <div style="position: absolute; width: 100%; height: 100%; backface-visibility: hidden; transform: rotateY(180deg); background: var(--bg-card); border: 2px solid rgba(16, 185, 129, 0.35); border-radius: 24px; padding: 32px 24px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box; text-align: center;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; font-weight: 800; background: rgba(16, 185, 129, 0.12); color: #059669; padding: 4px 12px; border-radius: 20px;">
                MẶT SAU: CÂU TRẢ LỜI CHUẨN
              </span>
              <span style="font-size: 12px; color: #b45309; font-weight: 700;">
                💡 ${p.tips ? p.tips.substring(0, 30) + '...' : 'Giao tiếp bản ngữ'}
              </span>
            </div>

            <div style="margin: 24px 0;">
              <div style="font-size: 48px; margin-bottom: 12px;">${p.a_avatar || '🙋‍♂️'}</div>
              <div style="font-size: 12px; font-weight: 800; color: #059669; text-transform: uppercase; margin-bottom: 6px;">
                ${p.a_speaker || 'Speaker B'}
              </div>
              <h3 style="font-size: 20px; font-weight: 900; color: var(--text-primary); margin: 0 0 8px; line-height: 1.4;">
                ${p.a_text}
              </h3>
              <div style="font-size: 14px; font-family: monospace; color: #059669; margin-bottom: 12px;">
                ${p.a_ipa || ''}
              </div>
              <div style="font-size: 15px; font-weight: 700; color: #059669;">
                🇻🇳 ${p.a_vi}
              </div>
            </div>

            <div style="display: flex; justify-content: center; align-items: center; gap: 8px;">
              <button class="btn btn-sm btn-outline" onclick="event.stopPropagation(); speakText('${escapeQuotes(p.a_text)}', 'en-US')" style="border-radius: 12px; font-weight: 700;">
                🔊 Nghe câu đáp
              </button>
              <span style="font-size: 12px; color: var(--text-muted); font-weight: 600;">
                (Nhấn thẻ để lật lại)
              </span>
            </div>
          </div>

        </div>
      </div>

      <!-- PREV / NEXT NAVIGATION -->
      <div style="display: flex; justify-content: center; gap: 14px;">
        <button class="btn btn-outline" onclick="prevCPCard()" ${idx === 0 ? 'disabled' : ''} style="border-radius: 14px; font-weight: 800; padding: 12px 24px;">
          ⬅️ Thẻ trước
        </button>
        <button class="btn btn-primary" onclick="flipCPCard()" style="border-radius: 14px; font-weight: 800; padding: 12px 28px; background: linear-gradient(135deg, #10b981, #06b6d4);">
          🔄 Lật thẻ
        </button>
        <button class="btn btn-outline" onclick="nextCPCard()" ${idx === total - 1 ? 'disabled' : ''} style="border-radius: 14px; font-weight: 800; padding: 12px 24px;">
          Thẻ tiếp ➡️
        </button>
      </div>
    </div>
  `;
}

function flipCPCard() {
  cpState.cardFlipped = !cpState.cardFlipped;
  const cardEl = document.querySelector('.cp-3d-card');
  if (cardEl) {
    if (cpState.cardFlipped) cardEl.classList.add('flipped');
    else cardEl.classList.remove('flipped');
  }
}

function prevCPCard() {
  if (cpState.currentCardIdx > 0) {
    cpState.currentCardIdx--;
    cpState.cardFlipped = false;
    renderCPTopicStudio();
  }
}

function nextCPCard() {
  if (cpState.currentCardIdx < cpState.topicPhrases.length - 1) {
    cpState.currentCardIdx++;
    cpState.cardFlipped = false;
    renderCPTopicStudio();
  }
}

function shuffleCPCards() {
  const arr = [...cpState.topicPhrases];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  cpState.topicPhrases = arr;
  cpState.currentCardIdx = 0;
  cpState.cardFlipped = false;
  renderCPTopicStudio();
  toast('Đã xáo trộn thứ tự các thẻ flashcard! 🔀', 'info');
}

function playCPCardAudioPair() {
  const p = cpState.topicPhrases[cpState.currentCardIdx];
  if (!p) return;
  speakText(p.q_text, 'en-US');
  setTimeout(() => {
    speakText(p.a_text, 'en-US');
  }, 3200);
}

// ── 3. REFLEX QUIZ TAB ────────────────────────────────────────────────────────
function initCPReflexQuiz() {
  const phrases = cpState.topicPhrases;
  if (!phrases || phrases.length < 4) return;

  const shuffled = [...phrases].sort(() => 0.5 - Math.random());
  const selected = shuffled.slice(0, 10);

  const questions = selected.map(target => {
    // 3 distractors
    const others = phrases.filter(p => p.id !== target.id);
    const distractors = others.sort(() => 0.5 - Math.random()).slice(0, 3).map(o => o.a_text);
    const options = [target.a_text, ...distractors].sort(() => 0.5 - Math.random());

    return {
      target,
      options,
      correctAnswer: target.a_text
    };
  });

  cpState.reflex = {
    questions,
    currentIdx: 0,
    score: 0,
    streak: 0,
    selectedOption: null,
    answered: false
  };
}

function renderCPReflexTab() {
  if (!cpState.reflex.questions.length) {
    initCPReflexQuiz();
  }

  const r = cpState.reflex;
  if (r.currentIdx >= r.questions.length) {
    // Show summary
    const pct = Math.round((r.score / r.questions.length) * 100);
    return `
      <div class="card" style="max-width: 580px; margin: 0 auto; text-align: center; padding: 40px 24px; border-radius: 24px;">
        <div style="font-size: 64px; margin-bottom: 16px;">🏆</div>
        <h2 style="font-size: 24px; font-weight: 900; margin-bottom: 8px;">Hoàn Thành Thử Thách Phản Xạ!</h2>
        <p style="color: var(--text-secondary); margin-bottom: 24px;">Bạn đã xuất sắc hoàn thành phần thử thách phản xạ giao tiếp.</p>
        
        <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(6, 182, 212, 0.12)); border: 1.5px solid rgba(16, 185, 129, 0.35); border-radius: 20px; padding: 24px; margin-bottom: 24px;">
          <div style="font-size: 44px; font-weight: 900; color: #10b981; margin-bottom: 4px;">${r.score} / ${r.questions.length}</div>
          <div style="font-size: 14px; font-weight: 800; color: var(--text-secondary);">Độ chính xác phản xạ: ${pct}%</div>
        </div>

        <div style="display: flex; justify-content: center; gap: 12px;">
          <button class="btn btn-primary" onclick="initCPReflexQuiz(); renderCPTopicStudio();" style="border-radius: 14px; font-weight: 800; padding: 12px 28px; background: linear-gradient(135deg, #10b981, #06b6d4);">
            🔄 Thử thách lượt mới
          </button>
          <button class="btn btn-outline" onclick="switchCPTab('dialogue')" style="border-radius: 14px; font-weight: 800; padding: 12px 24px;">
            💬 Quay lại xem đối thoại
          </button>
        </div>
      </div>
    `;
  }

  const cur = r.questions[r.currentIdx];
  const target = cur.target;

  return `
    <div style="max-width: 680px; margin: 0 auto;">
      <!-- Quiz Header -->
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div style="font-size: 14px; font-weight: 800; color: var(--text-primary);">
          ⚡ Câu phản xạ: <span style="color:#10b981;">${r.currentIdx + 1}</span> / ${r.questions.length}
        </div>
        <div style="display: flex; gap: 12px; align-items: center;">
          <span style="font-size: 13px; font-weight: 800; color: #ea580c;">🔥 Chuỗi: ${r.streak}</span>
          <span style="font-size: 13px; font-weight: 800; color: #10b981;">⭐ Điểm: ${r.score}</span>
        </div>
      </div>

      <!-- Progress bar -->
      <div style="width: 100%; height: 6px; background: var(--border); border-radius: 10px; margin-bottom: 24px; overflow: hidden;">
        <div style="height: 100%; width: ${((r.currentIdx + 1) / r.questions.length) * 100}%; background: linear-gradient(90deg, #10b981, #06b6d4); transition: width 0.3s ease;"></div>
      </div>

      <!-- SITUATIONAL PROMPT -->
      <div style="background: var(--bg-card); border: 2px solid rgba(99, 102, 241, 0.3); border-radius: 20px; padding: 24px; margin-bottom: 20px; box-shadow: var(--shadow-sm);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
          <span style="font-size: 12px; font-weight: 800; color: #4f46e5; background: rgba(99, 102, 241, 0.1); padding: 4px 10px; border-radius: 10px;">
            📌 Tình huống: ${target.situation || 'Giao tiếp'}
          </span>
          <button class="btn btn-sm btn-outline" onclick="speakText('${escapeQuotes(target.q_text)}', 'en-US')" style="border-radius: 10px; font-weight: 700;">
            🔊 Nghe câu hỏi
          </button>
        </div>

        <div style="display: flex; gap: 14px; align-items: center; margin-bottom: 8px;">
          <div style="font-size: 36px;">${target.q_avatar || '🙋‍♀️'}</div>
          <div>
            <div style="font-size: 12px; font-weight: 800; color: #6366f1; text-transform: uppercase;">
              ${target.q_speaker || 'Đối tác'} nói:
            </div>
            <div style="font-size: 18px; font-weight: 900; color: var(--text-primary); line-height: 1.4;">
              "${target.q_text}"
            </div>
            <div style="font-size: 13.5px; color: var(--text-secondary); margin-top: 2px;">
              🇻🇳 (${target.q_vi})
            </div>
          </div>
        </div>

        <div style="font-size: 13px; font-weight: 800; color: #059669; margin-top: 14px; border-top: 1px dashed var(--border); padding-top: 12px;">
          👉 Bạn nên phản hồi lại bằng câu nào sau đây?
        </div>
      </div>

      <!-- OPTIONS -->
      <div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px;">
        ${cur.options.map((opt, i) => {
          let btnStyle = 'background: var(--bg-card); border: 1.5px solid var(--border); color: var(--text-primary);';
          if (r.answered) {
            if (opt === cur.correctAnswer) {
              btnStyle = 'background: rgba(16, 185, 129, 0.15); border: 2px solid #10b981; color: #047857; font-weight: 800;';
            } else if (opt === r.selectedOption) {
              btnStyle = 'background: rgba(239, 68, 68, 0.12); border: 2px solid #ef4444; color: #b91c1c;';
            } else {
              btnStyle = 'background: var(--bg-card); opacity: 0.6; border: 1px solid var(--border);';
            }
          }

          return `
            <button class="cp-quiz-opt" onclick="selectCPReflexOption('${escapeQuotes(opt)}')" ${r.answered ? 'disabled' : ''}
                    style="${btnStyle} padding: 16px 20px; border-radius: 16px; font-size: 14.5px; text-align: left; cursor: ${r.answered ? 'default' : 'pointer'}; transition: all 0.2s; display: flex; align-items: center; justify-content: space-between; gap: 12px;">
              <span style="line-height: 1.4;">
                <strong style="margin-right: 8px;">${String.fromCharCode(65 + i)}.</strong> ${opt}
              </span>
              <span style="font-size: 18px;">
                ${r.answered && opt === cur.correctAnswer ? '✅' : ''}
                ${r.answered && opt === r.selectedOption && opt !== cur.correctAnswer ? '❌' : ''}
              </span>
            </button>
          `;
        }).join('')}
      </div>

      <!-- NEXT BUTTON -->
      ${r.answered ? `
        <div style="display: flex; justify-content: flex-end;">
          <button class="btn btn-primary" onclick="nextCPReflexQuestion()" style="border-radius: 14px; font-weight: 800; padding: 12px 28px; background: linear-gradient(135deg, #10b981, #06b6d4);">
            ${r.currentIdx < r.questions.length - 1 ? 'Câu tiếp theo ➔' : 'Xem kết quả tổng kết 🏆'}
          </button>
        </div>
      ` : ''}
    </div>
  `;
}

function selectCPReflexOption(opt) {
  const r = cpState.reflex;
  if (r.answered) return;

  r.selectedOption = opt;
  r.answered = true;

  const cur = r.questions[r.currentIdx];
  if (opt === cur.correctAnswer) {
    r.score++;
    r.streak++;
    toast('Chính xác! Phản xạ rất tự nhiên 🌟 (+15 XP)', 'success');
  } else {
    r.streak = 0;
    toast('Chưa chính xác, hãy quan sát đáp án đúng nhé! 💡', 'warning');
  }

  renderCPTopicStudio();
}

function nextCPReflexQuestion() {
  const r = cpState.reflex;
  r.currentIdx++;
  r.answered = false;
  r.selectedOption = null;
  renderCPTopicStudio();
}

// ── 4. BOOKMARKS TAB ──────────────────────────────────────────────────────────
function renderCPBookmarksTab() {
  const bookmarkedPhrases = cpState.topicPhrases.filter(p => cpState.bookmarks.includes(p.id));

  if (!bookmarkedPhrases.length) {
    return `
      <div class="card" style="text-align: center; padding: 60px 20px; border-radius: 20px;">
        <div style="font-size: 48px; margin-bottom: 12px;">⭐</div>
        <h3 style="margin-bottom: 8px;">Chưa có câu nào được lưu trong chủ đề này</h3>
        <p style="color: var(--text-secondary); margin-bottom: 18px;">
          Hãy bấm vào biểu tượng ngôi sao <strong>☆</strong> ở bất kỳ cặp câu nào trong tab "Đối thoại 1:1" để lưu vào danh sách học lại.
        </p>
        <button class="btn btn-primary" onclick="switchCPTab('dialogue')" style="border-radius: 12px; font-weight: 700;">
          💬 Khám phá câu nói ngay
        </button>
      </div>
    `;
  }

  return `
    <div style="margin-bottom: 16px; font-size: 14.5px; font-weight: 800;">
      ⭐ Danh sách câu quan trọng đã lưu (${bookmarkedPhrases.length} câu)
    </div>
    <div style="display: flex; flex-direction: column; gap: 20px;">
      ${bookmarkedPhrases.map((p, idx) => renderCPDialogueItem(p, idx)).join('')}
    </div>
  `;
}

function getTopicBookmarkCount() {
  if (!cpState.topicPhrases || !cpState.bookmarks) return 0;
  return cpState.topicPhrases.filter(p => cpState.bookmarks.includes(p.id)).length;
}

function toggleCPBookmark(id) {
  const idx = cpState.bookmarks.indexOf(id);
  if (idx > -1) {
    cpState.bookmarks.splice(idx, 1);
    toast('Đã bỏ lưu câu khỏi danh sách yêu thích', 'info');
  } else {
    cpState.bookmarks.push(id);
    toast('Đã lưu câu vào danh sách học tập ⭐', 'success');
  }
  localStorage.setItem('vihtech_phrase_bookmarks', JSON.stringify(cpState.bookmarks));
  renderCPTopicStudio();
}

// ── PLAY ALL PHRASES SEQUENTIALLY ─────────────────────────────────────────────
let cpAutoPlayActive = false;
let cpAutoPlayIdx = 0;

function playAllPhrasesInTopic() {
  if (cpAutoPlayActive) {
    cpAutoPlayActive = false;
    window.stopAllAudio();
    toast('Đã dừng tự động phát', 'info');
    return;
  }

  cpAutoPlayActive = true;
  cpAutoPlayIdx = 0;
  toast('Bắt đầu tự động phát các câu hội thoại... Bấm lại để dừng.', 'info');
  playNextInSequence();
}

function playNextInSequence() {
  if (!cpAutoPlayActive || cpAutoPlayIdx >= cpState.topicPhrases.length) {
    cpAutoPlayActive = false;
    toast('Đã phát xong toàn bộ các câu trong chủ đề! 🏆', 'success');
    return;
  }

  const p = cpState.topicPhrases[cpAutoPlayIdx];
  const cardEl = document.getElementById(`phrase-card-${p.id}`);
  if (cardEl) {
    cardEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
    cardEl.style.borderColor = '#10b981';
    setTimeout(() => { cardEl.style.borderColor = 'var(--border)'; }, 3000);
  }

  speakText(p.q_text, 'en-US');
  setTimeout(() => {
    if (!cpAutoPlayActive) return;
    speakText(p.a_text, 'en-US');
    setTimeout(() => {
      if (!cpAutoPlayActive) return;
      cpAutoPlayIdx++;
      playNextInSequence();
    }, 3500);
  }, 3000);
}

// ── SPEECH RECOGNITION / PRONUNCIATION PRACTICE ───────────────────────────────
function startCPMicPractice(phraseId, speaker, targetText) {
  const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRec) {
    toast('Trình duyệt của bạn chưa hỗ trợ nhận diện giọng nói Web Speech API (Hãy thử Google Chrome hoặc Microsoft Edge).', 'warning');
    return;
  }

  const feedbackEl = document.getElementById(`mic-feedback-${phraseId}-${speaker}`);
  if (feedbackEl) {
    feedbackEl.style.display = 'block';
    feedbackEl.innerHTML = `
      <div style="background: rgba(16, 185, 129, 0.1); border: 1.5px dashed #10b981; border-radius: 12px; padding: 12px; display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <div style="width: 12px; height: 12px; border-radius: 50%; background: #ef4444; animation: pulse 1.2s infinite;"></div>
          <span style="font-size: 13px; font-weight: 700; color: var(--text-primary);">Đang lắng nghe bạn đọc câu... Hãy phát âm to và rõ ràng!</span>
        </div>
        <button class="btn btn-xs btn-outline" onclick="stopCPMicPractice('${phraseId}', '${speaker}')">Dừng</button>
      </div>
    `;
  }

  try {
    const recognition = new SpeechRec();
    recognition.lang = 'en-US';
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      const score = calculateSpeechAccuracy(transcript, targetText);
      displayMicScore(phraseId, speaker, transcript, targetText, score);
    };

    recognition.onerror = (event) => {
      if (feedbackEl) {
        feedbackEl.innerHTML = `
          <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 10px; padding: 8px 12px; font-size: 12.5px; color: #dc2626;">
            ⚠️ Không nhận diện được âm thanh: ${event.error || 'Vui lòng thử lại.'}
          </div>
        `;
      }
    };

    recognition.start();
  } catch (e) {
    console.error('Mic error:', e);
  }
}

function stopCPMicPractice(phraseId, speaker) {
  const feedbackEl = document.getElementById(`mic-feedback-${phraseId}-${speaker}`);
  if (feedbackEl) feedbackEl.style.display = 'none';
}

function calculateSpeechAccuracy(spoken, target) {
  const cleanSpoken = spoken.toLowerCase().replace(/[^a-z0-9 ]/g, '').split(' ');
  const cleanTarget = target.toLowerCase().replace(/[^a-z0-9 ]/g, '').split(' ');

  let matchCount = 0;
  cleanTarget.forEach(w => {
    if (cleanSpoken.includes(w)) matchCount++;
  });

  const ratio = matchCount / Math.max(cleanTarget.length, 1);
  return Math.min(100, Math.round(ratio * 100));
}

function displayMicScore(phraseId, speaker, spoken, target, score) {
  const feedbackEl = document.getElementById(`mic-feedback-${phraseId}-${speaker}`);
  if (!feedbackEl) return;

  let color = '#10b981';
  let badgeText = '🌟 Xuất sắc!';
  if (score < 60) {
    color = '#ef4444';
    badgeText = '🔄 Cần luyện thêm!';
  } else if (score < 80) {
    color = '#f59e0b';
    badgeText = '👍 Khá tốt!';
  }

  feedbackEl.innerHTML = `
    <div style="background: ${color}12; border: 1.5px solid ${color}; border-radius: 14px; padding: 12px 16px; margin-top: 8px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <span style="font-size: 12px; font-weight: 800; color: ${color};">${badgeText}</span>
        <span style="font-size: 14px; font-weight: 900; color: ${color};">${score}% Độ chính xác</span>
      </div>
      <div style="font-size: 12.5px; color: var(--text-secondary); line-height: 1.4;">
        <strong>Bạn vừa nói:</strong> "${spoken}"
      </div>
    </div>
  `;
}

// ── GLOBAL SEARCH MODAL (SEARCH OVER 2,500 PHRASES) ───────────────────────────
function openCPGlobalSearchModal() {
  let modal = document.getElementById('cp-search-modal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'cp-search-modal';
    modal.style.position = 'fixed';
    modal.style.top = '0';
    modal.style.left = '0';
    modal.style.right = '0';
    modal.style.bottom = '0';
    modal.style.background = 'rgba(0,0,0,0.6)';
    modal.style.zIndex = '9999';
    modal.style.display = 'flex';
    modal.style.alignItems = 'center';
    modal.style.justifyContent = 'center';
    modal.style.padding = '20px';
    document.body.appendChild(modal);
  }

  modal.style.display = 'flex';
  modal.innerHTML = `
    <div style="background: var(--bg-card); width: 100%; max-width: 720px; max-height: 85vh; border-radius: 24px; border: 1px solid var(--border); box-shadow: 0 20px 50px rgba(0,0,0,0.3); display: flex; flex-direction: column; overflow: hidden;">
      <!-- Modal Header -->
      <div style="padding: 20px 24px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center;">
        <div style="font-size: 18px; font-weight: 900; color: var(--text-primary); display: flex; align-items: center; gap: 8px;">
          <span>⚡</span> Tra Cứu Toàn Diện 2,500 Câu Hội Thoại
        </div>
        <button onclick="closeCPGlobalSearchModal()" style="background: none; border: none; font-size: 20px; cursor: pointer; color: var(--text-secondary);">✖</button>
      </div>

      <!-- Search Input -->
      <div style="padding: 16px 24px; border-bottom: 1px solid var(--border); background: var(--bg-secondary);">
        <input type="text" id="cp-modal-search-input" placeholder="Nhập từ hoặc câu tiếng Anh / tiếng Việt để tra cứu..." 
               oninput="executeCPGlobalSearch(this.value)"
               style="width: 100%; padding: 12px 16px; border-radius: 12px; border: 1.5px solid var(--border); background: var(--bg-card); color: var(--text-primary); font-size: 14px; outline: none;">
      </div>

      <!-- Results Body -->
      <div id="cp-modal-results" style="padding: 20px 24px; overflow-y: auto; flex: 1;" class="custom-scrollbar">
        <div style="text-align: center; padding: 40px 0; color: var(--text-muted);">
          Gõ từ khóa để tra cứu ngay trong 2,500 câu nói tình huống...
        </div>
      </div>
    </div>
  `;

  setTimeout(() => {
    const inp = document.getElementById('cp-modal-search-input');
    if (inp) inp.focus();
  }, 100);
}

function closeCPGlobalSearchModal() {
  const modal = document.getElementById('cp-search-modal');
  if (modal) modal.style.display = 'none';
}

let cpGlobalSearchTimeout = null;
async function executeCPGlobalSearch(query) {
  clearTimeout(cpGlobalSearchTimeout);
  if (!query || query.trim().length < 2) {
    const resBox = document.getElementById('cp-modal-results');
    if (resBox) resBox.innerHTML = '<div style="text-align:center;padding:40px 0;color:var(--text-muted);">Gõ ít nhất 2 ký tự để tra cứu...</div>';
    return;
  }

  cpGlobalSearchTimeout = setTimeout(async () => {
    const resBox = document.getElementById('cp-modal-results');
    if (!resBox) return;

    resBox.innerHTML = '<div style="text-align:center;padding:30px 0;"><div class="loading-dots"><span></span><span></span><span></span></div></div>';

    try {
      let results = [];
      if (api && api.commonPhrases) {
        const res = await api.commonPhrases.search(query);
        if (res && res.results) results = res.results;
      }
      
      if (!results.length && window.STANDALONE_DATA) {
        const q = query.toLowerCase().trim();
        const allPhrases = window.STANDALONE_DATA.common_phrases || {};
        const topics = window.STANDALONE_DATA.common_phrases_topics || [];
        const tMap = {};
        topics.forEach(t => { tMap[String(t.id)] = t; });

        Object.keys(allPhrases).forEach(tid => {
          const t = tMap[tid] || {};
          (allPhrases[tid] || []).forEach(p => {
            if (
              (p.q_text && p.q_text.toLowerCase().includes(q)) ||
              (p.q_vi && p.q_vi.toLowerCase().includes(q)) ||
              (p.a_text && p.a_text.toLowerCase().includes(q)) ||
              (p.a_vi && p.a_vi.toLowerCase().includes(q))
            ) {
              results.push({
                ...p,
                topic_title: t.title,
                topic_title_vi: t.title_vi,
                topic_cartoon: t.cartoon
              });
            }
          });
        });
      }

      if (!results.length) {
        resBox.innerHTML = `
          <div style="text-align:center;padding:40px 0;color:var(--text-muted);">
            Không tìm thấy kết quả nào cho "${escapeHtml(query)}"
          </div>
        `;
        return;
      }

      resBox.innerHTML = `
        <div style="font-size:13px;font-weight:700;color:var(--text-secondary);margin-bottom:12px;">
          Tìm thấy ${results.length} câu phù hợp:
        </div>
        <div style="display:flex;flex-direction:column;gap:12px;">
          ${results.slice(0, 50).map(r => `
            <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:14px;display:flex;justify-content:space-between;align-items:center;gap:12px;">
              <div style="flex:1;">
                <div style="display:flex;align-items:center;gap:6px;margin-bottom:4px;">
                  <span style="font-size:11px;font-weight:800;color:#10b981;background:rgba(16,185,129,0.1);padding:2px 6px;border-radius:6px;">
                    ${r.topic_cartoon || '💬'} ${r.topic_title || 'Chủ đề'}
                  </span>
                </div>
                <div style="font-size:14px;font-weight:800;color:var(--text-primary);margin-bottom:2px;">
                  ❓ ${r.q_text}
                </div>
                <div style="font-size:12.5px;color:var(--text-secondary);margin-bottom:6px;">
                  🇻🇳 ${r.q_vi}
                </div>
                <div style="font-size:14px;font-weight:700;color:#059669;">
                  💬 ${r.a_text}
                </div>
              </div>
              <div style="display:flex;flex-direction:column;gap:6px;">
                <button class="btn btn-sm btn-outline" onclick="speakText('${escapeQuotes(r.q_text)}', 'en-US')" title="Nghe câu hỏi">
                  🔊 Hỏi
                </button>
                <button class="btn btn-sm btn-outline" onclick="speakText('${escapeQuotes(r.a_text)}', 'en-US')" title="Nghe câu đáp">
                  🔊 Đáp
                </button>
                <button class="btn btn-sm btn-primary" onclick="closeCPGlobalSearchModal(); openCPTopic(${r.topic_id});" style="font-size:11px;padding:4px 8px;">
                  Vào chủ đề ➔
                </button>
              </div>
            </div>
          `).join('')}
        </div>
      `;
    } catch (e) {
      console.error('Search error:', e);
      resBox.innerHTML = '<div style="text-align:center;padding:30px 0;color:#ef4444;">Lỗi khi tra cứu. Vui lòng thử lại.</div>';
    }
  }, 250);
}

// ── UTILITIES ─────────────────────────────────────────────────────────────────
function escapeQuotes(str) {
  if (!str) return '';
  return str.replace(/'/g, "\\'").replace(/"/g, '&quot;');
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// Global scope exposures
window.openCPTopic = openCPTopic;
window.backToCPTopics = backToCPTopics;
window.switchCPTab = switchCPTab;
window.setCPCategory = setCPCategory;
window.handleCPSearch = handleCPSearch;
window.clearCPSearch = clearCPSearch;
window.flipCPCard = flipCPCard;
window.prevCPCard = prevCPCard;
window.nextCPCard = nextCPCard;
window.shuffleCPCards = shuffleCPCards;
window.playCPCardAudioPair = playCPCardAudioPair;
window.selectCPReflexOption = selectCPReflexOption;
window.nextCPReflexQuestion = nextCPReflexQuestion;
window.initCPReflexQuiz = initCPReflexQuiz;
window.toggleCPBookmark = toggleCPBookmark;
window.playAllPhrasesInTopic = playAllPhrasesInTopic;
window.startCPMicPractice = startCPMicPractice;
window.stopCPMicPractice = stopCPMicPractice;
window.openCPGlobalSearchModal = openCPGlobalSearchModal;
window.closeCPGlobalSearchModal = closeCPGlobalSearchModal;
window.executeCPGlobalSearch = executeCPGlobalSearch;
'''

with open('frontend/js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Append cleanly to app.js
with open('frontend/js/app.js', 'w', encoding='utf-8') as f:
    f.write(content + "\n" + NEW_CODE)

print("Successfully injected Common Phrases module into frontend/js/app.js!")
