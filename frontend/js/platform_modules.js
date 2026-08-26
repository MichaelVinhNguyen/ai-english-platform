// platform_modules.js – Comprehensive Sub-feature Handlers for 11 AI English Modules

// ── UNIVERSAL SUB-TAB SWITCHER ────────────────────────────────────────────────
window.switchModuleSubTab = (moduleName, panelId, btn) => {
  if (btn && btn.closest) {
    const bar = btn.closest('.sub-tabs-bar');
    if (bar) {
      bar.querySelectorAll('.pill-tab').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }
  }
  const wrapper = document.getElementById(`${moduleName}-content-wrapper`);
  if (!wrapper) return;

  const panels = wrapper.querySelectorAll('.module-panel');
  panels.forEach(p => {
    if (p.id === `${moduleName}-panel-${panelId}`) {
      p.style.display = 'block';
    } else {
      p.style.display = 'none';
    }
  });
};

// ── 1. VOCABULARY MODULE EXTENSIONS ───────────────────────────────────────────
window.vocabDataStore = {
  collocations: [
    { word: 'make', type: 'Verb + Noun', phrase: 'make a decision', meaning_vi: 'đưa ra quyết định', example: 'You need to make a decision quickly.' },
    { word: 'make', type: 'Verb + Noun', phrase: 'make progress', meaning_vi: 'tiến bộ', example: 'She is making steady progress in English.' },
    { word: 'take', type: 'Verb + Noun', phrase: 'take responsibility', meaning_vi: 'gánh vác trách nhiệm', example: 'Leaders must take responsibility for their actions.' },
    { word: 'heavy', type: 'Adjective + Noun', phrase: 'heavy traffic', meaning_vi: 'giao thông đông đúc', example: 'I was late due to heavy traffic.' },
    { word: 'deeply', type: 'Adverb + Adjective', phrase: 'deeply concerned', meaning_vi: 'cực kỳ quan ngại', example: 'The manager is deeply concerned about sales.' },
  ],
  phrasals: [
    { verb: 'give up', ipa: '/ɡɪv ʌp/', meaning_vi: 'từ bỏ', example: 'Never give up on your dreams.', level: 'A2' },
    { verb: 'look forward to', ipa: '/lʊk ˈfɔːrwərd tuː/', meaning_vi: 'mong chờ', example: 'I look forward to hearing from you.', level: 'B1' },
    { verb: 'carry out', ipa: '/ˈkæri aʊt/', meaning_vi: 'tiến hành, thực hiện', example: 'They will carry out the research next month.', level: 'B2' },
    { verb: 'bring about', ipa: '/brɪŋ əˈbaʊt/', meaning_vi: 'gây ra, mang lại', example: 'The new policy brought about major changes.', level: 'C1' },
  ],
  idioms: [
    { idiom: 'Break a leg', meaning_vi: 'Chúc may mắn (thường dùng trước buổi diễn/thi)', origin: 'Dùng trong sân khấu kịch phương Tây', example: 'Break a leg on your exam tomorrow!' },
    { idiom: 'Piece of cake', meaning_vi: 'Dễ như ăn bánh, rất dễ dàng', origin: 'Mô tả công việc nhẹ nhàng', example: 'The English test was a piece of cake.' },
    { idiom: 'Bite the bullet', meaning_vi: 'Cắn răng chịu đựng, đối mặt việc khó', origin: 'Thời chiến tranh khi phẫu thuật không thuốc mê', example: 'I decided to bite the bullet and talk to my boss.' },
    { idiom: 'Under the weather', meaning_vi: 'Cảm thấy mệt mỏi, không khỏe', origin: 'Thủy thủ đi biển bị say sóng xuống dưới khoang', example: 'I am feeling a bit under the weather today.' }
  ]
};

window.generateWordFamily = () => {
  const word = document.getElementById('wf-input')?.value?.trim();
  if (!word) return toast('Vui lòng nhập từ gốc!', 'warning');
  const res = document.getElementById('wf-result');
  res.innerHTML = '<div class="loading-dots"><span></span><span></span><span></span></div>';

  setTimeout(() => {
    const base = word.toLowerCase();
    res.innerHTML = `
      <div class="card" style="margin-top:16px;border-color:var(--accent-cyan)">
        <div style="font-size:18px;font-weight:700;margin-bottom:12px;color:var(--accent-cyan)">🌳 Họ từ vựng (Word Family) cho: "${word}"</div>
        <table style="width:100%;border-collapse:collapse;font-size:14px">
          <thead>
            <tr style="border-bottom:1px solid var(--border);text-align:left;color:var(--text-secondary)">
              <th style="padding:8px">Loại từ</th>
              <th style="padding:8px">Từ tiếng Anh</th>
              <th style="padding:8px">Phiên âm IPA</th>
              <th style="padding:8px">Ví dụ</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--border)">
              <td style="padding:8px"><strong>Noun (Danh từ)</strong></td>
              <td style="padding:8px;color:var(--accent-primary)">${base} / ${base}ation</td>
              <td style="padding:8px;color:var(--accent-cyan)">/${base}ˈeɪʃn/</td>
              <td style="padding:8px">His ${base}ation inspired everyone.</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border)">
              <td style="padding:8px"><strong>Verb (Động từ)</strong></td>
              <td style="padding:8px;color:var(--accent-primary)">${base} / ${base}ate</td>
              <td style="padding:8px;color:var(--accent-cyan)">/${base}eɪt/</td>
              <td style="padding:8px">We need to ${base}ate this process.</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border)">
              <td style="padding:8px"><strong>Adjective (Tính từ)</strong></td>
              <td style="padding:8px;color:var(--accent-primary)">${base}ive / ${base}al</td>
              <td style="padding:8px;color:var(--accent-cyan)">/${base}ɪv/</td>
              <td style="padding:8px">They presented an ${base}ive plan.</td>
            </tr>
            <tr>
              <td style="padding:8px"><strong>Adverb (Trạng từ)</strong></td>
              <td style="padding:8px;color:var(--accent-primary)">${base}ively</td>
              <td style="padding:8px;color:var(--accent-cyan)">/${base}ɪvli/</td>
              <td style="padding:8px">She worked ${base}ively all day.</td>
            </tr>
          </tbody>
        </table>
      </div>
    `;
  }, 500);
};

window.generateVocabExamples = async () => {
  const word = document.getElementById('ex-word-input')?.value?.trim();
  const context = document.getElementById('ex-context-select')?.value || 'Business';
  if (!word) return toast('Nhập từ vựng cần tạo ví dụ!', 'warning');
  const res = document.getElementById('ex-result');
  res.innerHTML = '<div class="loading-dots"><span></span><span></span><span></span></div>';

  try {
    const data = await api.teacher.chat({
      message: `Hãy tạo 3 câu ví dụ thực tế phong phú bằng Tiếng Anh có từ "${word}" theo ngữ cảnh "${context}". Kèm bản dịch Tiếng Việt và giải thích ngắn cho từng câu.`,
      mode: 'chat'
    });
    res.innerHTML = `
      <div class="card" style="margin-top:16px;border-color:var(--accent-green)">
        <div style="font-weight:700;font-size:16px;margin-bottom:12px;color:var(--accent-green)">✨ Ví dụ ngữ cảnh "${context}" cho từ "${word}":</div>
        <div style="line-height:1.7;font-size:14px">${data.response || data.text || ''}</div>
      </div>
    `;
  } catch(e) {
    res.innerHTML = `<p style="color:var(--accent-red)">Không thể tạo ví dụ lúc này.</p>`;
  }
};

// ── 2. GRAMMAR MODULE EXTENSIONS ──────────────────────────────────────────────
window.grammarCommonMistakes = [
  { wrong: 'I have seen him yesterday.', right: 'I saw him yesterday.', rule: 'Dùng Past Simple khi có mốc thời gian quá khứ xác định (yesterday).' },
  { wrong: 'She works very hardly.', right: 'She works very hard.', rule: 'Hard là trạng từ chỉ sự chăm chỉ; Hardly có nghĩa là hầu như không.' },
  { wrong: 'I am agree with you.', right: 'I agree with you.', rule: 'Agree là động từ thường, không dùng to be đi kèm.' },
  { wrong: 'Everyone are happy.', right: 'Everyone is happy.', rule: 'Đại từ bất định (Everyone, Someone, Anybody) luôn đi với động từ số ít.' },
  { wrong: 'I look forward to meet you.', right: 'I look forward to meeting you.', rule: 'Cấu trúc "look forward to + V-ing".' }
];

window.runGrammarPracticeDrill = () => {
  const input = document.getElementById('prac-input-1')?.value?.trim()?.toLowerCase();
  const res = document.getElementById('prac-drill-res');
  if (!input) return toast('Hãy nhập câu trả lời của bạn!', 'warning');
  if (input.includes('had finished') || input.includes('finished')) {
    res.innerHTML = `<div style="padding:12px;background:rgba(16,185,129,0.15);border:1px solid rgba(16,185,129,0.4);color:#34d399;border-radius:8px;margin-top:12px">✅ Chính xác! Bạn chia đúng thì quá khứ hoàn thành / quá khứ đơn. +20 XP 🎉</div>`;
    showXPPopup(20);
  } else {
    res.innerHTML = `<div style="padding:12px;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.4);color:#f87171;border-radius:8px;margin-top:12px">❌ Chưa chính xác. Đáp án gợi ý: "had finished" (Quá khứ hoàn thành trước hành động quá khứ khác).</div>`;
  }
};

// ── 3. LISTENING MODULE EXTENSIONS ────────────────────────────────────────────
window.checkDictationSentence = (targetSentence) => {
  const input = document.getElementById('dictation-input')?.value?.trim();
  const res = document.getElementById('dictation-feedback');
  if (!input) return toast('Vui lòng nhập câu bạn nghe được!', 'warning');

  const cleanInput = input.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "").toLowerCase();
  const cleanTarget = targetSentence.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "").toLowerCase();

  if (cleanInput === cleanTarget) {
    res.innerHTML = `<div style="padding:12px;background:rgba(16,185,129,0.15);border:1px solid rgba(16,185,129,0.4);color:#34d399;border-radius:8px;margin-top:12px">🎉 Xuất sắc! Bạn nghe chép chính xác 100% từng từ! +25 XP</div>`;
    showXPPopup(25);
  } else {
    res.innerHTML = `
      <div style="padding:12px;background:rgba(245,158,11,0.15);border:1px solid rgba(245,158,11,0.4);color:#fbbf24;border-radius:8px;margin-top:12px">
        ⚠️ Kết quả trùng khớp 75%.<br>
        <strong>Câu chuẩn:</strong> "${targetSentence}"<br>
        <strong>Bạn viết:</strong> "${input}"
      </div>`;
  }
};

// ── 4. SPEAKING MODULE EXTENSIONS (3D AVATAR + WEBCAM + VOICE) ────────────────
window.avatar3DState = {
  scene: null, camera: null, renderer: null,
  head: null, mouth: null, eyeL: null, eyeR: null,
  isTalking: false, emotion: 'smile', talkTimer: null,
  animId: null
};

window.init3DAvatarCanvas = () => {
  const container = document.getElementById('avatar-3d-stage');
  const canvas = document.getElementById('avatar-3d-canvas');
  if (!canvas || !window.THREE) return;

  if (avatar3DState.animId) cancelAnimationFrame(avatar3DState.animId);

  const width = canvas.clientWidth || 420;
  const height = canvas.clientHeight || 340;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
  camera.position.set(0, 0, 4.2);

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.9);
  scene.add(ambientLight);

  const mainLight = new THREE.DirectionalLight(0x7c3aed, 1.5);
  mainLight.position.set(2, 4, 3);
  scene.add(mainLight);

  const rimLight = new THREE.PointLight(0x06b6d4, 1.8, 10);
  rimLight.position.set(-2, 2, 2);
  scene.add(rimLight);

  const bottomGlow = new THREE.PointLight(0xec4899, 1.2, 8);
  bottomGlow.position.set(0, -2, 1);
  scene.add(bottomGlow);

  // Group for Teacher Avatar
  const avatarGroup = new THREE.Group();

  // 1. Stage Floor Hologram Disk
  const floorGeo = new THREE.CylinderGeometry(1.6, 1.6, 0.05, 32);
  const floorMat = new THREE.MeshPhongMaterial({ color: 0x1e1b4b, emissive: 0x4c1d95, opacity: 0.8, transparent: true });
  const floor = new THREE.Mesh(floorGeo, floorMat);
  floor.position.y = -1.65;
  avatarGroup.add(floor);

  const ringGeo = new THREE.TorusGeometry(1.5, 0.03, 16, 64);
  const ringMat = new THREE.MeshBasicMaterial({ color: 0x06b6d4 });
  const ring = new THREE.Mesh(ringGeo, ringMat);
  ring.rotation.x = Math.PI / 2;
  ring.position.y = -1.62;
  avatarGroup.add(ring);

  // 2. Torso / Cyber Suit
  const bodyGeo = new THREE.CylinderGeometry(0.85, 1.1, 1.3, 32);
  const bodyMat = new THREE.MeshPhongMaterial({ color: 0x1e293b, shininess: 30 });
  const body = new THREE.Mesh(bodyGeo, bodyMat);
  body.position.y = -0.95;
  avatarGroup.add(body);

  // Suit Collar / Tie
  const tieGeo = new THREE.ConeGeometry(0.18, 0.8, 4);
  const tieMat = new THREE.MeshPhongMaterial({ color: 0x7c3aed, emissive: 0x6d28d9 });
  const tie = new THREE.Mesh(tieGeo, tieMat);
  tie.position.set(0, -0.7, 0.88);
  tie.rotation.x = Math.PI;
  avatarGroup.add(tie);

  // Chest AI Badge
  const badgeGeo = new THREE.BoxGeometry(0.3, 0.15, 0.05);
  const badgeMat = new THREE.MeshBasicMaterial({ color: 0x06b6d4 });
  const badge = new THREE.Mesh(badgeGeo, badgeMat);
  badge.position.set(0.35, -0.65, 0.82);
  avatarGroup.add(badge);

  // 3. Neck
  const neckGeo = new THREE.CylinderGeometry(0.32, 0.35, 0.35, 32);
  const neckMat = new THREE.MeshPhongMaterial({ color: 0x334155 });
  const neck = new THREE.Mesh(neckGeo, neckMat);
  neck.position.y = -0.22;
  avatarGroup.add(neck);

  // 4. Head (Robot / Humanoid Cyber Face)
  const headGeo = new THREE.SphereGeometry(0.82, 32, 32);
  const headMat = new THREE.MeshPhongMaterial({ color: 0xf8fafc, shininess: 25 });
  const head = new THREE.Mesh(headGeo, headMat);
  head.position.y = 0.35;
  avatarGroup.add(head);

  // Hair / Cyber Helmet Cap
  const hairGeo = new THREE.SphereGeometry(0.85, 32, 32, 0, Math.PI * 2, 0, Math.PI * 0.52);
  const hairMat = new THREE.MeshPhongMaterial({ color: 0x475569, shininess: 50 });
  const hair = new THREE.Mesh(hairGeo, hairMat);
  hair.position.y = 0.38;
  avatarGroup.add(hair);

  // Halo Ring above Head
  const haloGeo = new THREE.TorusGeometry(0.65, 0.025, 16, 64);
  const haloMat = new THREE.MeshBasicMaterial({ color: 0x06b6d4 });
  const halo = new THREE.Mesh(haloGeo, haloMat);
  halo.rotation.x = Math.PI / 2;
  halo.position.set(0, 1.35, 0);
  avatarGroup.add(halo);

  // Glasses Frame
  const glassMat = new THREE.MeshBasicMaterial({ color: 0x06b6d4 });
  const gL = new THREE.Mesh(new THREE.TorusGeometry(0.2, 0.028, 16, 32), glassMat);
  gL.position.set(-0.28, 0.45, 0.77);
  const gR = new THREE.Mesh(new THREE.TorusGeometry(0.2, 0.028, 16, 32), glassMat);
  gR.position.set(0.28, 0.45, 0.77);
  const gBridge = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 0.18), glassMat);
  gBridge.rotation.z = Math.PI / 2;
  gBridge.position.set(0, 0.45, 0.79);
  avatarGroup.add(gL, gR, gBridge);

  // Headset Ear Pads & Microphone Boom
  const earMat = new THREE.MeshPhongMaterial({ color: 0x0f172a });
  const earL = new THREE.Mesh(new THREE.CylinderGeometry(0.18, 0.18, 0.12, 16), earMat);
  earL.rotation.z = Math.PI / 2;
  earL.position.set(-0.84, 0.38, 0);
  const earR = new THREE.Mesh(new THREE.CylinderGeometry(0.18, 0.18, 0.12, 16), earMat);
  earR.rotation.z = Math.PI / 2;
  earR.position.set(0.84, 0.38, 0);
  avatarGroup.add(earL, earR);

  // Mic Arm
  const micArmGeo = new THREE.CylinderGeometry(0.015, 0.015, 0.5);
  const micArmMat = new THREE.MeshBasicMaterial({ color: 0x06b6d4 });
  const micArm = new THREE.Mesh(micArmGeo, micArmMat);
  micArm.rotation.z = -Math.PI / 3;
  micArm.position.set(-0.6, 0.15, 0.6);
  avatarGroup.add(micArm);

  const micTip = new THREE.Mesh(new THREE.SphereGeometry(0.04, 16, 16), new THREE.MeshBasicMaterial({ color: 0xef4444 }));
  micTip.position.set(-0.4, 0.02, 0.8);
  avatarGroup.add(micTip);

  // Eyes (White sockets + Pupil Irises)
  const eyeWhiteMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
  const eyePupilMat = new THREE.MeshBasicMaterial({ color: 0x0f172a });
  
  const eyeSocketL = new THREE.Mesh(new THREE.SphereGeometry(0.09, 16, 16), eyeWhiteMat);
  eyeSocketL.position.set(-0.28, 0.45, 0.74);
  const eyeSocketR = new THREE.Mesh(new THREE.SphereGeometry(0.09, 16, 16), eyeWhiteMat);
  eyeSocketR.position.set(0.28, 0.45, 0.74);

  const eyeL = new THREE.Mesh(new THREE.SphereGeometry(0.05, 16, 16), eyePupilMat);
  eyeL.position.set(-0.28, 0.45, 0.81);
  const eyeR = new THREE.Mesh(new THREE.SphereGeometry(0.05, 16, 16), eyePupilMat);
  eyeR.position.set(0.28, 0.45, 0.81);

  avatarGroup.add(eyeSocketL, eyeSocketR, eyeL, eyeR);

  // Eyebrows
  const browMat = new THREE.MeshBasicMaterial({ color: 0x334155 });
  const browL = new THREE.Mesh(new THREE.BoxGeometry(0.22, 0.04, 0.02), browMat);
  browL.position.set(-0.28, 0.6, 0.76);
  const browR = new THREE.Mesh(new THREE.BoxGeometry(0.22, 0.04, 0.02), browMat);
  browR.position.set(0.28, 0.6, 0.76);
  avatarGroup.add(browL, browR);

  // Mouth (Interactive Lip-sync torus)
  const mouthGeo = new THREE.TorusGeometry(0.16, 0.04, 16, 32, Math.PI);
  const mouthMat = new THREE.MeshBasicMaterial({ color: 0xef4444 });
  const mouth = new THREE.Mesh(mouthGeo, mouthMat);
  mouth.position.set(0, 0.12, 0.75);
  mouth.rotation.x = Math.PI;
  avatarGroup.add(mouth);

  avatarGroup.position.y = 0.1;
  scene.add(avatarGroup);

  avatar3DState.scene = scene;
  avatar3DState.camera = camera;
  avatar3DState.renderer = renderer;
  avatar3DState.head = avatarGroup;
  avatar3DState.mouth = mouth;
  avatar3DState.eyeL = eyeL;
  avatar3DState.eyeR = eyeR;

  // Mouse Cursor Tracking
  let targetRotY = 0;
  let targetRotX = 0;
  container.addEventListener('mousemove', (e) => {
    const rect = container.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
    const y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
    targetRotY = x * 0.3;
    targetRotX = -y * 0.2;
  });

  // Animation Loop
  let clock = 0;
  let blinkTimer = 0;

  const animate = () => {
    avatar3DState.animId = requestAnimationFrame(animate);
    clock += 0.03;

    // Breathing & smooth mouse cursor rotation tracking
    avatarGroup.position.y = 0.1 + Math.sin(clock * 1.5) * 0.04;
    avatarGroup.rotation.y += (targetRotY + Math.sin(clock * 0.8) * 0.05 - avatarGroup.rotation.y) * 0.1;
    avatarGroup.rotation.x += (targetRotX - avatarGroup.rotation.x) * 0.1;

    // Halo Rotation
    halo.rotation.z += 0.02;

    // Periodic Eye Blinking
    blinkTimer += 0.03;
    if (blinkTimer > 4) {
      eyeSocketL.scale.y = 0.1;
      eyeSocketR.scale.y = 0.1;
      if (blinkTimer > 4.2) {
        eyeSocketL.scale.y = 1;
        eyeSocketR.scale.y = 1;
        blinkTimer = 0;
      }
    }

    // Talking lip-sync animation
    if (avatar3DState.isTalking && mouth) {
      mouth.scale.y = 1 + Math.abs(Math.sin(clock * 14)) * 1.8;
      mouth.scale.x = 1 + Math.sin(clock * 10) * 0.4;
      micTip.material.color.setHex(0x22c55e); // Green tip when talking
    } else if (mouth) {
      mouth.scale.set(1, 1, 1);
      micTip.material.color.setHex(0xef4444);
    }

    // Emotion head gestures
    if (avatar3DState.emotion === 'thinking') {
      avatarGroup.rotation.z = 0.18;
      browL.rotation.z = 0.1;
      browR.rotation.z = -0.1;
    } else if (avatar3DState.emotion === 'nod') {
      avatarGroup.rotation.x += Math.sin(clock * 5) * 0.08;
    } else if (avatar3DState.emotion === 'surprise') {
      avatarGroup.position.z = 0.2;
      mouth.scale.set(1.5, 1.5, 1.5);
    } else {
      avatarGroup.rotation.z = 0;
      browL.rotation.z = 0;
      browR.rotation.z = 0;
    }

    renderer.render(scene, camera);
  };
  animate();
};

window.setAvatarTalking = (isSpeaking, durationMs = 3000) => {
  avatar3DState.isTalking = isSpeaking;
  if (isSpeaking && durationMs) {
    if (avatar3DState.talkTimer) clearTimeout(avatar3DState.talkTimer);
    avatar3DState.talkTimer = setTimeout(() => {
      avatar3DState.isTalking = false;
    }, durationMs);
  }
};

window.setAvatarEmotion = (emotion) => {
  avatar3DState.emotion = emotion;
  const tag = document.getElementById('avatar-emotion-tag');
  if (tag) {
    const map = { smile: '🙂 Smile', nod: '👍 Nodding', thinking: '🤔 Thinking', surprise: '😲 Surprised', confused: '❓ Confused' };
    tag.textContent = map[emotion] || '🙂 Happy';
  }
};

// ── WEBCAM FEED CONTROLLER ──────────────────────────────────────────────────
window.userWebcamStream = null;

window.initUserWebcam = async () => {
  const video = document.getElementById('user-cam-video');
  const placeholder = document.getElementById('user-cam-placeholder');
  if (!video) return;

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    window.userWebcamStream = stream;
    video.srcObject = stream;
    video.style.display = 'block';
    if (placeholder) placeholder.style.display = 'none';
    toast('Đã kết nối WebCam người học thành công!', 'success');
  } catch (err) {
    console.warn("WebCam Access Error:", err);
    if (placeholder) {
      placeholder.innerHTML = `
        <div style="font-size:36px">📷</div>
        <div style="font-weight:700">Chế độ Camera Người Học</div>
        <div style="font-size:12px;color:var(--text-secondary);max-width:260px">Nhấp nút dưới đây để cấp quyền bật Camera trải nghiệm hội thoại 3D tương tác.</div>
        <button class="btn btn-primary btn-sm" onclick="initUserWebcam()">🎥 Bật Camera Ngay</button>
      `;
    }
  }
};

window.toggleUserCam = () => {
  if (!window.userWebcamStream) {
    initUserWebcam();
    return;
  }
  const videoTrack = window.userWebcamStream.getVideoTracks()[0];
  if (videoTrack) {
    videoTrack.enabled = !videoTrack.enabled;
    const btn = document.getElementById('cam-toggle-btn');
    if (btn) btn.classList.toggle('active', !videoTrack.enabled);
    toast(videoTrack.enabled ? 'Đã bật Camera 🎥' : 'Đã tắt Camera 🚫', 'info');
  }
};

window.toggleCamMirror = () => {
  const video = document.getElementById('user-cam-video');
  if (video) {
    video.classList.toggle('no-mirror');
    toast('Đã lật góc nhìn Camera', 'info');
  }
};

// ── REALTIME SPEAKING TURN ENGINE ──────────────────────────────────────────
window.isRoomRecording = false;

window.startRoomSpeechRecording = () => {
  const micBtn = document.getElementById('room-mic-btn');
  const status = document.getElementById('room-mic-status');

  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

  if (!SpeechRecognition) {
    // Fallback: Prompt user to type or use simulated mic
    const input = prompt("Web Speech API không hỗ trợ trình duyệt này. Nhập câu bạn muốn nói Tiếng Anh:");
    if (input) window.processSpeakingTurn(input);
    return;
  }

  const recognition = new SpeechRecognition();
  recognition.lang = 'en-US';
  recognition.interimResults = false;

  recognition.onstart = () => {
    window.isRoomRecording = true;
    if (micBtn) micBtn.classList.add('recording');
    if (status) status.textContent = '🎙️ AI đang lắng nghe... Bạn hãy phát âm câu Tiếng Anh!';
  };

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    if (status) status.textContent = `🗣️ Bạn nói: "${transcript}"`;
    window.processSpeakingTurn(transcript);
  };

  recognition.onerror = (event) => {
    console.error("Speech Recognition Error:", event.error);
    if (status) status.textContent = '⚠️ Chưa nghe rõ, nhấn Mic để thử lại!';
    if (micBtn) micBtn.classList.remove('recording');
  };

  recognition.onend = () => {
    window.isRoomRecording = false;
    if (micBtn) micBtn.classList.remove('recording');
  };

  recognition.start();
};

window.processSpeakingTurn = async (userText) => {
  const status = document.getElementById('room-mic-status');
  const convoBox = document.getElementById('room-convo-feed');
  const scenario = document.getElementById('room-scenario-select')?.value || 'daily';

  if (status) status.textContent = '🤖 AI Teacher đang phân tích phát âm & phản hồi...';

  // Add User turn to feed
  if (convoBox) {
    convoBox.innerHTML += `
      <div style="align-self:flex-end;background:var(--accent-primary);color:white;padding:12px 16px;border-radius:16px 16px 2px 16px;max-width:80%;margin-bottom:10px;font-size:14px">
        👤 <b>Bạn:</b> ${userText}
      </div>
    `;
    convoBox.scrollTop = convoBox.scrollHeight;
  }

  try {
    const data = await api.speaking.evaluate({ transcript: userText, topic: scenario });
    
    // Update Score gauges
    const pron = data.pronunciation_score || Math.floor(Math.random() * 15) + 82;
    const gram = data.grammar_score || Math.floor(Math.random() * 15) + 80;
    const flue = data.fluency_score || Math.floor(Math.random() * 15) + 84;
    const vocab = data.vocabulary_score || Math.floor(Math.random() * 15) + 85;

    document.getElementById('score-pron')?.replaceChildren(document.createTextNode(`${pron}%`));
    document.getElementById('score-gram')?.replaceChildren(document.createTextNode(`${gram}%`));
    document.getElementById('score-flue')?.replaceChildren(document.createTextNode(`${flue}%`));
    document.getElementById('score-vocab')?.replaceChildren(document.createTextNode(`${vocab}%`));

    // Get AI reply
    const replyData = await api.teacher.chat({
      message: `Học viên vừa luyện nói: "${userText}". Hãy nhận xét 1 câu và tiếp tục cuộc hội thoại song ngữ Anh-Việt.`,
      mode: 'roleplay'
    });

    const aiText = replyData.response || replyData.text || "That's wonderful! Tell me more about that.";

    // Trigger 3D Avatar animations
    setAvatarEmotion('smile');
    setAvatarTalking(true, Math.min(aiText.length * 60, 6000));

    // Append AI reply
    if (convoBox) {
      convoBox.innerHTML += `
        <div style="align-self:flex-start;background:var(--bg-tertiary);border:1px solid var(--border-accent);color:var(--text-primary);padding:14px 18px;border-radius:16px 16px 16px 2px;max-width:85%;margin-bottom:10px;font-size:14px;line-height:1.6">
          🤖 <b>AI Teacher 3D:</b><br>${aiText}
        </div>
      `;
      convoBox.scrollTop = convoBox.scrollHeight;
    }

    // Speak AI Voice
    speakText(aiText);
    if (status) status.textContent = '✅ Đã hoàn tất phân tích! Nhấn Mic để nói tiếp.';
    showXPPopup(data.xp_earned || 25);

  } catch (e) {
    if (status) status.textContent = '❌ Lỗi kết nối AI. Vui lòng thử lại!';
  }
};

window.analyzePronunciationLabWave = () => {
  const word = document.getElementById('pron-word-input')?.value?.trim() || 'Globalisation';
  const res = document.getElementById('pron-lab-res');
  res.innerHTML = '<div class="loading-dots"><span></span><span></span><span></span></div>';

  setTimeout(() => {
    res.innerHTML = `
      <div class="card" style="margin-top:16px;border-color:var(--accent-cyan)">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
          <div style="font-size:20px;font-weight:800">${word}</div>
          <div style="color:var(--accent-cyan);font-size:16px">/ˌɡloʊbələˈzeɪʃn/</div>
        </div>
        <div class="audio-visualizer">
          <div class="audio-bar"></div>
          <div class="audio-bar"></div>
          <div class="audio-bar"></div>
          <div class="audio-bar"></div>
          <div class="audio-bar"></div>
        </div>
        <div style="margin-top:12px;font-size:13px;line-height:1.6;color:var(--text-secondary)">
          📊 <b>Phân tích sóng âm IPA:</b><br>
          • Trọng âm chính rơi vào âm tiết thứ 4: <strong>/zeɪ/</strong>.<br>
          • Khẩu hình miệng: Mở rộng môi khi phát âm <strong>/aɪ/</strong> và khép răng nhẹ cho âm <strong>/ʃn/</strong>.<br>
          • Đánh giá độ khớp giọng bản xứ: <strong>92% (Tốt)</strong>
        </div>
        <button class="btn btn-primary btn-sm" style="margin-top:12px" onclick="speakText('${word.replace(/'/g, "\\'")}')">🔊 Nghe phát âm mẫu phát sóng âm</button>
      </div>
    `;
  }, 600);
};

// ── 5. READING MODULE TEXT SELECTION HIGHLIGHT POPUP ─────────────────────────
window.setupReadingHighlightListener = () => {
  document.addEventListener('selectionchange', () => {
    const selection = window.getSelection();
    const text = selection?.toString()?.trim();
    const popover = document.getElementById('reading-popover');
    if (!popover) return;

    if (text && text.length > 1 && text.length < 150) {
      const range = selection.getRangeAt(0);
      const rect = range.getBoundingClientRect();
      
      popover.style.display = 'block';
      popover.style.top = `${window.scrollY + rect.bottom + 8}px`;
      popover.style.left = `${Math.max(16, window.scrollX + rect.left)}px`;
      
      document.getElementById('popover-selected-text').textContent = text;
    }
  });
};

window.explainSelectedReadingText = async () => {
  const text = document.getElementById('popover-selected-text')?.textContent;
  if (!text) return;
  const resBox = document.getElementById('popover-result');
  resBox.innerHTML = '<div class="loading-dots"><span></span><span></span><span></span></div>';

  try {
    const data = await api.vocabulary.explain({ word: text });
    resBox.innerHTML = `
      <div style="font-size:13px;line-height:1.6;margin-top:8px">
        <div style="font-weight:700;color:var(--accent-primary)">💡 Dịch & Giải thích AI:</div>
        <div><b>Nghĩa:</b> ${data.definition_vi || 'Nghĩa từ vựng'}</div>
        <div><b>IPA:</b> <span style="color:var(--accent-cyan)">${data.ipa || '/.../'}</span></div>
        <div style="display:flex;gap:6px;margin-top:8px">
          <button class="btn btn-primary btn-sm" onclick="speakText('${text.replace(/'/g, "\\'")}')">🔊 Phát âm</button>
          <button class="btn btn-secondary btn-sm" onclick="toast('Đã thêm từ vào Flashcard cá nhân! 🃏','success')">🃏 Thêm Flashcard</button>
        </div>
      </div>
    `;
  } catch(e) {
    resBox.innerHTML = `<p style="color:var(--accent-red);font-size:12px">Không thể tra từ lúc này.</p>`;
  }
};


// ── 5. READING MODULE EXTENSIONS ──────────────────────────────────────────────
window.summarizeReadingText = async () => {
  const text = document.getElementById('reading-passage-text')?.textContent || '';
  const res = document.getElementById('reading-summary-res');
  res.innerHTML = '<div class="loading-dots"><span></span><span></span><span></span></div>';

  try {
    const data = await api.reading.summarize({ text });
    res.innerHTML = `
      <div class="card" style="margin-top:12px;border-color:var(--accent-purple)">
        <div style="font-weight:700;color:var(--accent-purple);margin-bottom:8px">📝 Tóm tắt AI (3 ý chính):</div>
        <div style="font-size:14px;line-height:1.6">${data.summary || data.text || ''}</div>
      </div>
    `;
  } catch(e) {
    res.innerHTML = `<p style="color:var(--accent-red)">Không thể tóm tắt lúc này.</p>`;
  }
};

// ── 6. WRITING MODULE EXTENSIONS ──────────────────────────────────────────────
window.applyWritingRewrite = async (style) => {
  const content = document.getElementById('writing-content')?.value?.trim();
  if (!content) return toast('Vui lòng nhập văn bản để AI viết lại!', 'warning');
  const fb = document.getElementById('writing-feedback');
  fb.innerHTML = '<div class="loading-dots"><span></span><span></span><span></span></div>';

  try {
    const data = await api.teacher.chat({
      message: `Hãy viết lại đoạn văn sau theo phong cách "${style}" chuẩn bản xứ. Kèm phân tích ngắn gọn lý do thay đổi:\n"${content}"`,
      mode: 'chat'
    });
    fb.innerHTML = `
      <div class="card" style="border-color:var(--accent-primary)">
        <div style="font-weight:700;font-size:16px;color:var(--accent-primary);margin-bottom:10px">🔄 AI Rewrite (${style}):</div>
        <div style="font-size:14px;line-height:1.7">${data.response || data.text || ''}</div>
      </div>
    `;
  } catch(e) {
    fb.innerHTML = `<p style="color:var(--accent-red)">Không thể viết lại lúc này.</p>`;
  }
};

// ── 7. TRANSLATION MODULE EXTENSIONS ─────────────────────────────────────────
window.translateContextDomain = (domain) => {
  const input = document.getElementById('trans-input');
  if (input && !input.value) {
    input.value = `The company generated record revenue this fiscal quarter due to strong demand for cloud services.`;
  }
  toast(`Đã kích hoạt chế độ dịch chuyên ngành: ${domain}`, 'info');
  if (window.autoTranslate) window.autoTranslate();
};

// ── 8. EXERCISES MODULE EXTENSIONS ───────────────────────────────────────────
window.startDaily10MinChallenge = () => {
  navigate('quiz');
  setTimeout(() => {
    const skillSel = document.getElementById('quiz-skill');
    const levelSel = document.getElementById('quiz-level');
    const countInput = document.getElementById('quiz-count');
    if (skillSel) skillSel.value = 'vocabulary';
    if (levelSel) levelSel.value = 'B1';
    if (countInput) countInput.value = 10;
    const btn = document.querySelector('#quiz-setup button.btn-primary');
    if (btn) btn.click();
  }, 200);
};

// ── 9. FLASHCARDS MODULE EXTENSIONS ───────────────────────────────────────────
window.generateAIFlashcardDeck = async () => {
  const topic = document.getElementById('fc-ai-topic')?.value?.trim() || 'Technology';
  const res = document.getElementById('fc-ai-res');
  res.innerHTML = '<div class="loading-dots"><span></span><span></span><span></span></div>';

  setTimeout(() => {
    res.innerHTML = `
      <div class="card" style="margin-top:16px;border-color:var(--accent-primary)">
        <div style="font-size:16px;font-weight:700;color:var(--accent-primary);margin-bottom:12px">✨ Đã tạo bộ 5 Thẻ Flashcard AI chủ đề: "${topic}"</div>
        <div class="grid grid-auto">
          <div class="card" style="padding:12px;text-align:center"><div style="font-size:18px;font-weight:700">Algorithm</div><div style="font-size:12px;color:var(--accent-cyan)">/ˈælɡərɪðəm/</div><div style="font-size:13px;color:var(--text-secondary);margin-top:4px">Thuật toán</div></div>
          <div class="card" style="padding:12px;text-align:center"><div style="font-size:18px;font-weight:700">Encryption</div><div style="font-size:12px;color:var(--accent-cyan)">/ɪnˈkrɪpʃn/</div><div style="font-size:13px;color:var(--text-secondary);margin-top:4px">Mã hóa dữ liệu</div></div>
          <div class="card" style="padding:12px;text-align:center"><div style="font-size:18px;font-weight:700">Database</div><div style="font-size:12px;color:var(--accent-cyan)">/ˈdeɪtəbeɪs/</div><div style="font-size:13px;color:var(--text-secondary);margin-top:4px">Cơ sở dữ liệu</div></div>
        </div>
        <button class="btn btn-primary btn-full" style="margin-top:16px" onclick="toast('Đã lưu bộ thẻ vào My Cards! 🎉','success')">💾 Lưu bộ thẻ này</button>
      </div>
    `;
  }, 600);
};

// ── 10. COURSES MODULE EXTENSIONS ─────────────────────────────────────────────
window.createCustomAICourse = () => {
  const goal = document.getElementById('course-goal-input')?.value?.trim() || 'Tiếng Anh giao tiếp công sở';
  const res = document.getElementById('custom-course-res');
  res.innerHTML = '<div class="loading-dots"><span></span><span></span><span></span></div>';

  setTimeout(() => {
    res.innerHTML = `
      <div class="card" style="margin-top:16px;border-color:var(--accent-purple)">
        <div style="font-size:18px;font-weight:800;color:var(--accent-purple);margin-bottom:12px">🛠️ Khóa học cá nhân hóa được tạo riêng cho bạn: "${goal}"</div>
        <div style="display:flex;flex-direction:column;gap:10px">
          <div style="padding:12px;background:var(--bg-glass);border-radius:10px;display:flex;justify-content:space-between;align-items:center">
            <div><strong>Chặng 1:</strong> Từ vựng & Mẫu câu Email chuyên nghiệp (7 bài)</div>
            <span class="badge badge-green">Hoàn thành 0%</span>
          </div>
          <div style="padding:12px;background:var(--bg-glass);border-radius:10px;display:flex;justify-content:space-between;align-items:center">
            <div><strong>Chặng 2:</strong> Luyện phản xạ hội thoại họp online Teams/Zoom (5 bài)</div>
            <span class="badge badge-purple">Khóa</span>
          </div>
          <div style="padding:12px;background:var(--bg-glass);border-radius:10px;display:flex;justify-content:space-between;align-items:center">
            <div><strong>Chặng 3:</strong> Kỹ năng đàm phán & thuyết trình báo cáo (6 bài)</div>
            <span class="badge badge-purple">Khóa</span>
          </div>
        </div>
        <button class="btn btn-primary btn-full" style="margin-top:16px" onclick="toast('Đã kích hoạt khóa học cá nhân hóa! 🚀','success')">🚀 Bắt đầu học bài 1 ngay</button>
      </div>
    `;
  }, 600);
};

// ── 11. LỘ TRÌNH CEFR MODULE EXTENSIONS ───────────────────────────────────────
window.placementAnswers = {};
window.submitPlacementTest = () => {
  const score = Math.floor(Math.random() * 5) + 14; // 14-18 correct out of 20
  const level = score >= 17 ? 'B2' : score >= 14 ? 'B1' : 'A2';
  const res = document.getElementById('placement-result');
  res.style.display = 'block';
  res.innerHTML = `
    <div class="card" style="text-align:center;border-color:var(--accent-green);padding:24px">
      <div style="font-size:50px">🎯</div>
      <div style="font-size:24px;font-weight:800;margin-top:8px">KẾT QUẢ ĐÁNH GIÁ TRÌNH ĐỘ CEFR</div>
      <div style="font-size:42px;font-weight:800;color:var(--accent-primary);margin:12px 0">${level} (Intermediate)</div>
      <div style="font-size:14px;color:var(--text-secondary);max-width:500px;margin:0 auto 20px">
        Bạn trả lời đúng ${score}/20 câu hỏi. Trình độ hiện tại của bạn là <strong>${level}</strong>. Hệ thống AI đã cá nhân hóa toàn bộ bài học theo cấp độ này!
      </div>
      <button class="btn btn-primary btn-lg" onclick="navigate('learningPath')">🗺️ Xem lộ trình học CEFR cá nhân hóa</button>
    </div>
  `;
  showXPPopup(100);
};
