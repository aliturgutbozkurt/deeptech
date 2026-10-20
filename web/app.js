/**
 * Deeptech Masterclass - Interactive Web Companion Application
 * High-performance, reactive architecture for 500 lessons across 50 modules.
 */

(function () {
  'use strict';

  // State
  let allModules = [];
  let allLessons = [];
  let lessonsByNum = new Map();
  let currentLessonNum = 1;
  let currentFilterModule = 'all';
  let currentSearchQuery = '';
  let currentLang = 'both'; // 'tr', 'en', 'both'

  // DOM Elements
  const searchInput = document.getElementById('searchInput');
  const clearSearchBtn = document.getElementById('clearSearchBtn');
  const moduleSelect = document.getElementById('moduleSelect');
  const lessonNavList = document.getElementById('lessonNavList');
  const lessonContainer = document.getElementById('lessonContainer');
  const contentViewport = document.getElementById('contentViewport');
  const langButtons = document.querySelectorAll('.lang-btn');
  const openPdfModalBtn = document.getElementById('openPdfModalBtn');
  const closePdfModalBtn = document.getElementById('closePdfModalBtn');
  const pdfModal = document.getElementById('pdfModal');
  const modalModulesGrid = document.getElementById('modalModulesGrid');
  const sidebar = document.getElementById('sidebar');
  const collapseSidebarBtn = document.getElementById('collapseSidebarBtn');
  const toast = document.getElementById('toast');

  // Initialization
  function init() {
    if (window.LESSONS_DATA && window.LESSONS_DATA.modules) {
      allModules = window.LESSONS_DATA.modules;
      allLessons = [];
      lessonsByNum.clear();

      allModules.forEach(m => {
        m.lessons.forEach(l => {
          const item = {
            ...l,
            moduleId: m.id,
            moduleTitleTr: m.title_tr,
            moduleTitleEn: m.title_en
          };
          allLessons.push(item);
          lessonsByNum.set(l.num, item);
        });
      });
    }

    populateModuleDropdown();
    populateModalModules();
    setupEventListeners();

    // Parse initial URL hash
    parseHashAndLoad();
    renderNav();
    renderActiveLesson();
  }

  // Parse URL hash (#lesson-42 or #lesson-042)
  function parseHashAndLoad() {
    const hash = window.location.hash;
    if (hash) {
      const match = hash.match(/#lesson[-_]?(\d+)/i);
      if (match && match[1]) {
        const num = parseInt(match[1], 10);
        if (num >= 1 && num <= allLessons.length) {
          currentLessonNum = num;
          return;
        }
      }
    }
    currentLessonNum = 1;
  }

  // Populate Dropdown
  function populateModuleDropdown() {
    allModules.forEach(m => {
      const opt = document.createElement('option');
      opt.value = m.id;
      opt.textContent = `Bölüm ${m.id}: ${m.title_tr}`;
      moduleSelect.appendChild(opt);
    });
  }

  // Populate Modal Module Links
  function populateModalModules() {
    modalModulesGrid.innerHTML = '';
    allModules.forEach(m => {
      const paddedId = String(m.id).padStart(2, '0');
      const item = document.createElement('a');
      item.className = 'module-download-item';
      item.href = `../output/modules/module_${paddedId}.pdf`;
      item.download = `Deeptech_Module_${paddedId}.pdf`;
      item.innerHTML = `
        <div class="mod-dl-title">Bölüm ${m.id}: ${escapeHtml(m.title_tr)}</div>
        <div class="mod-dl-badge">PDF ⬇</div>
      `;
      modalModulesGrid.appendChild(item);
    });
  }

  // Event Listeners
  function setupEventListeners() {
    // Hash change event (native back/forward and anchor link navigation)
    window.addEventListener('hashchange', () => {
      parseHashAndLoad();
      updateActiveSidebarItem();
      renderActiveLesson();
      contentViewport.scrollTo({ top: 0, behavior: 'instant' });
    });

    // Search with debounce
    let searchTimeout;
    searchInput.addEventListener('input', (e) => {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => {
        currentSearchQuery = e.target.value.trim().toLowerCase();
        clearSearchBtn.style.display = currentSearchQuery ? 'block' : 'none';
        renderNav();
      }, 120);
    });

    clearSearchBtn.addEventListener('click', () => {
      searchInput.value = '';
      currentSearchQuery = '';
      clearSearchBtn.style.display = 'none';
      renderNav();
    });

    // Module Select
    moduleSelect.addEventListener('change', (e) => {
      currentFilterModule = e.target.value;
      renderNav();
    });

    // Language Toggle
    langButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        langButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentLang = btn.dataset.lang;
        document.body.className = `lang-${currentLang}`;
        showToast(`Dil modu: ${btn.textContent}`);
      });
    });

    // PDF Modal
    openPdfModalBtn.addEventListener('click', () => {
      pdfModal.classList.remove('hidden');
    });

    closePdfModalBtn.addEventListener('click', () => {
      pdfModal.classList.add('hidden');
    });

    pdfModal.addEventListener('click', (e) => {
      if (e.target === pdfModal) {
        pdfModal.classList.add('hidden');
      }
    });

    // Collapse Sidebar
    collapseSidebarBtn.addEventListener('click', () => {
      sidebar.classList.toggle('collapsed');
      collapseSidebarBtn.textContent = sidebar.classList.contains('collapsed') ? '▶' : '◀';
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        pdfModal.classList.add('hidden');
      } else if (e.key === 'ArrowRight' && !e.target.matches('input, textarea')) {
        if (currentLessonNum < allLessons.length) {
          window.location.hash = `#lesson-${currentLessonNum + 1}`;
        }
      } else if (e.key === 'ArrowLeft' && !e.target.matches('input, textarea')) {
        if (currentLessonNum > 1) {
          window.location.hash = `#lesson-${currentLessonNum - 1}`;
        }
      }
    });
  }

  // Filter lessons
  function getFilteredLessons() {
    return allLessons.filter(l => {
      if (currentFilterModule !== 'all' && l.moduleId !== parseInt(currentFilterModule, 10)) {
        return false;
      }
      if (currentSearchQuery) {
        const q = currentSearchQuery;
        const inNum = String(l.num) === q;
        const inTitleTr = l.title_tr.toLowerCase().includes(q);
        const inTitleEn = l.title_en.toLowerCase().includes(q);
        const inEli5Tr = l.eli5_tr.toLowerCase().includes(q);
        const inEli5En = l.eli5_en.toLowerCase().includes(q);
        const inDeepTr = l.deep_tr.toLowerCase().includes(q);
        const inDeepEn = l.deep_en.toLowerCase().includes(q);
        const inModule = l.moduleTitleTr.toLowerCase().includes(q) || l.moduleTitleEn.toLowerCase().includes(q);
        return inNum || inTitleTr || inTitleEn || inEli5Tr || inEli5En || inDeepTr || inDeepEn || inModule;
      }
      return true;
    });
  }

  // Render Sidebar Navigation
  function renderNav() {
    const filtered = getFilteredLessons();
    lessonNavList.innerHTML = '';

    if (filtered.length === 0) {
      lessonNavList.innerHTML = `
        <div style="padding: 24px; text-align: center; color: var(--text-dim); font-size: 13px;">
          🔍 Aradığınız kriterlere uygun ders bulunamadı.
        </div>
      `;
      return;
    }

    // Group by module
    const grouped = new Map();
    filtered.forEach(l => {
      if (!grouped.has(l.moduleId)) {
        grouped.set(l.moduleId, []);
      }
      grouped.get(l.moduleId).push(l);
    });

    const frag = document.createDocumentFragment();

    grouped.forEach((lessons, modId) => {
      const mod = allModules.find(m => m.id === modId);
      if (!mod) return;

      const groupDiv = document.createElement('div');
      groupDiv.className = 'nav-module-group';

      const titleDiv = document.createElement('div');
      titleDiv.className = 'nav-module-title';
      titleDiv.innerHTML = `
        <span>Bölüm ${mod.id}: ${escapeHtml(mod.title_tr)}</span>
        <span style="opacity: 0.6; font-size: 10px;">${lessons.length} ders</span>
      `;
      groupDiv.appendChild(titleDiv);

      lessons.forEach(l => {
        const item = document.createElement('a');
        item.href = `#lesson-${l.num}`;
        item.className = `nav-lesson-item ${l.num === currentLessonNum ? 'active' : ''}`;
        item.setAttribute('data-lesson-num', l.num);
        item.innerHTML = `
          <span class="nav-lesson-num">#${l.num}</span>
          <div class="nav-lesson-text">${escapeHtml(l.title_tr)}</div>
        `;
        groupDiv.appendChild(item);
      });

      frag.appendChild(groupDiv);
    });

    lessonNavList.appendChild(frag);
    updateActiveSidebarItem();
  }

  // Efficient active item update without DOM re-render
  function updateActiveSidebarItem() {
    const prev = lessonNavList.querySelector('.nav-lesson-item.active');
    if (prev) {
      prev.classList.remove('active');
    }
    const current = lessonNavList.querySelector(`.nav-lesson-item[data-lesson-num="${currentLessonNum}"]`);
    if (current) {
      current.classList.add('active');
      current.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    }
  }

  // Render Active Lesson in Main Viewport
  function renderActiveLesson() {
    const lesson = lessonsByNum.get(currentLessonNum);
    if (!lesson) return;

    const paddedNum = String(lesson.num).padStart(3, '0');
    const paddedMod = String(lesson.moduleId).padStart(2, '0');

    // Build Takeaways List HTML
    let takeawaysHtml = '';
    if (lesson.takeaways && lesson.takeaways.length > 0) {
      takeawaysHtml = lesson.takeaways.map(t => `
        <li class="takeaway-item">
          <span class="takeaway-dot">✓</span>
          <div>
            <div class="takeaway-text-tr col-tr">${escapeHtml(t[0])}</div>
            <div class="takeaway-text-en col-en">${escapeHtml(t[1])}</div>
          </div>
        </li>
      `).join('');
    }

    lessonContainer.innerHTML = `
      <!-- Header -->
      <div class="lesson-card-header">
        <div class="lesson-top-meta">
          <span class="lesson-badge">DERS #${lesson.num}</span>
          <span class="module-pill">Bölüm ${lesson.moduleId}: ${escapeHtml(lesson.moduleTitleTr)}</span>
        </div>
        <h2 class="lesson-title-tr col-tr">${escapeHtml(lesson.title_tr)}</h2>
        <div class="lesson-title-en col-en">${escapeHtml(lesson.title_en)}</div>

        <div class="lesson-header-actions">
          <a href="../output/individual/lesson_${paddedNum}.pdf" download="Deeptech_Lesson_${paddedNum}.pdf" class="btn btn-subtle">
            📄 Bu Dersin PDF'ini İndir
          </a>
          <a href="../output/modules/module_${paddedMod}.pdf" download="Deeptech_Module_${paddedMod}.pdf" class="btn btn-subtle">
            📦 Bölüm Kitapçığını İndir
          </a>
        </div>
      </div>

      <!-- Diagram Card -->
      <div class="section-card card-diagram">
        <div class="section-header">
          <div class="section-title">
            <span>⚡</span>
            <span>Derin Teknoloji & Fiziksel Süreç Mimari Şeması</span>
          </div>
          <span class="section-subtitle">Frontier Architecture & Physics Schematic</span>
        </div>
        <pre class="diagram-pre">${escapeHtml(lesson.diagram)}</pre>
      </div>

      <!-- ELI5 Metaphor Card -->
      <div class="section-card card-eli5">
        <div class="section-header">
          <div class="section-title">
            <span>💡</span>
            <span>Aptala Anlatım (ELI5 Metaforu)</span>
          </div>
          <span class="section-subtitle">Explain Like I'm 5 Real-Life Metaphor</span>
        </div>
        <div class="bilingual-grid">
          <div class="lang-column col-tr">
            <span class="lang-col-badge badge-tr">Türkçe ELI5</span>
            <p>${escapeHtml(lesson.eli5_tr)}</p>
          </div>
          <div class="lang-column col-en">
            <span class="lang-col-badge badge-en">English ELI5</span>
            <p class="lang-en-text">${escapeHtml(lesson.eli5_en)}</p>
          </div>
        </div>
      </div>

      <!-- Deep Dive Card -->
      <div class="section-card card-deepdive">
        <div class="section-header">
          <div class="section-title">
            <span>🔬</span>
            <span>Deeptech & Mühendislik Düzleminde Teknik Derinlik</span>
          </div>
          <span class="section-subtitle">Frontier Engineering Technical Deep-Dive</span>
        </div>
        <div class="bilingual-grid">
          <div class="lang-column col-tr">
            <span class="lang-col-badge badge-tr">Mühendislik Analizi</span>
            <p>${escapeHtml(lesson.deep_tr)}</p>
          </div>
          <div class="lang-column col-en">
            <span class="lang-col-badge badge-en">Technical Deep-Dive</span>
            <p class="lang-en-text">${escapeHtml(lesson.deep_en)}</p>
          </div>
        </div>
      </div>

      <!-- Code Card -->
      <div class="section-card card-code">
        <div class="section-header">
          <div class="section-title">
            <span>💻</span>
            <span>Uygulamalı Kod & Fiziksel Simülasyon</span>
          </div>
          <span class="section-subtitle">Python / Rust / Qiskit / CUDA / BioPython</span>
        </div>
        <div class="code-wrap">
          <button class="copy-btn" id="copyCodeBtn">Kopyala</button>
          <pre class="code-pre"><code id="lessonCodeSnippet">${escapeHtml(lesson.code)}</code></pre>
        </div>
      </div>

      <!-- Warning Card -->
      <div class="section-card card-warning">
        <div class="section-header">
          <div class="section-title">
            <span>⚠️</span>
            <span>Fiziksel Darboğaz & Ticarileşme Tuzağı</span>
          </div>
          <span class="section-subtitle">Hard Physical Limit & Commercialization Trap</span>
        </div>
        <div class="bilingual-grid">
          <div class="lang-column col-tr">
            <span class="lang-col-badge badge-tr">Aman Dikkat</span>
            <p>${escapeHtml(lesson.warning_tr)}</p>
          </div>
          <div class="lang-column col-en">
            <span class="lang-col-badge badge-en">Watch Out</span>
            <p class="lang-en-text">${escapeHtml(lesson.warning_en)}</p>
          </div>
        </div>
      </div>

      <!-- Takeaways Card -->
      <div class="section-card card-takeaways">
        <div class="section-header">
          <div class="section-title">
            <span>🎯</span>
            <span>Deeptech Mühendisinin Altın Çıkarımları</span>
          </div>
          <span class="section-subtitle">Core Takeaways</span>
        </div>
        <ul class="takeaways-list">
          ${takeawaysHtml}
        </ul>
      </div>

      <!-- Footer Navigation Buttons -->
      <div class="lesson-footer-nav">
        ${lesson.num > 1 
          ? `<a href="#lesson-${lesson.num - 1}" class="btn btn-subtle">◀ Önceki Ders (#${lesson.num - 1})</a>` 
          : `<span class="btn btn-subtle" style="opacity: 0.4; cursor: not-allowed;">◀ İlk Ders</span>`}
        <span style="font-size: 13px; color: var(--text-dim);">Ders ${lesson.num} / ${allLessons.length}</span>
        ${lesson.num < allLessons.length 
          ? `<a href="#lesson-${lesson.num + 1}" class="btn btn-primary">Sonraki Ders (#${lesson.num + 1}) ▶</a>` 
          : `<span class="btn btn-primary" style="opacity: 0.4; cursor: not-allowed;">Son Ders ▶</span>`}
      </div>
    `;

    // Bind copy button
    const copyBtn = document.getElementById('copyCodeBtn');
    if (copyBtn) {
      copyBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(lesson.code).then(() => {
          showToast('Kod panoya kopyalandı! 📋');
        });
      });
    }
  }

  // Toast Notification
  function showToast(msg) {
    toast.textContent = msg;
    toast.classList.remove('hidden');
    setTimeout(() => {
      toast.classList.add('hidden');
    }, 2400);
  }

  // Helper Escape HTML
  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Start app
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
