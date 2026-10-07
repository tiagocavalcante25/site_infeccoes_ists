/**
 * app.js - Lógica Interativa do Portal de Infecções Ginecológicas e ISTs (Parte 6)
 * Baseado no Guia Obstetrícia e Ginecologia Parte 6 (USMLE Step 2 CK / FEBRASGO / SUS / CDC / ACOG / ASCCP / INCA)
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initMobileNav();
  initSearch();
  initVulvovaginitisSimulator();
  initAmselNugentCalculator();
  initCandidaRiskStratifier();
  initCervicitisEPTCalculator();
  initPidHospitalizationScore();
  initSyphilisStagingManager();
  initGenitalUlcerDifferentiator();
  initHpvBethesdaGuide();
  initHivVerticalTransmissionCalculator();
  initPepPrepTracker();
  initFlashcards();
  initQuiz();
  initLightbox();
});

/* ==========================================================================
   1. GERENCIAMENTO DE TEMA (DARK / LIGHT)
   ========================================================================== */
function initTheme() {
  const themeToggles = document.querySelectorAll('.theme-toggle-btn, #theme-toggle, #mobile-theme-toggle');
  const html = document.documentElement;

  function updateThemeUI() {
    const isDark = html.classList.contains('dark');
    themeToggles.forEach(btn => {
      btn.setAttribute('aria-label', isDark ? 'Ativar modo claro' : 'Ativar modo escuro');
      btn.setAttribute('title', isDark ? 'Ativar modo claro' : 'Ativar modo escuro');
    });
  }

  function toggleTheme() {
    const isDark = html.classList.contains('dark');
    if (isDark) {
      html.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    } else {
      html.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    }
    updateThemeUI();
  }

  themeToggles.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      toggleTheme();
    });
  });

  updateThemeUI();
}

/* ==========================================================================
   2. MENU MOBILE E GAVETA RESPONSIVA
   ========================================================================== */
function initMobileNav() {
  const toggleBtn = document.getElementById('mobile-menu-toggle');
  const drawer = document.getElementById('mobile-menu-drawer');
  const menuIcon = document.getElementById('mobile-menu-icon');
  if (!toggleBtn || !drawer) return;

  function setOpen(isOpen) {
    if (isOpen) {
      drawer.classList.remove('hidden');
      toggleBtn.setAttribute('aria-expanded', 'true');
      if (menuIcon && window.lucide) {
        menuIcon.setAttribute('data-lucide', 'x');
        lucide.createIcons();
      }
    } else {
      drawer.classList.add('hidden');
      toggleBtn.setAttribute('aria-expanded', 'false');
      if (menuIcon && window.lucide) {
        menuIcon.setAttribute('data-lucide', 'menu');
        lucide.createIcons();
      }
    }
  }

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isHidden = drawer.classList.contains('hidden');
    setOpen(isHidden);
  });

  drawer.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => setOpen(false));
  });

  document.addEventListener('click', (e) => {
    if (!drawer.contains(e.target) && !toggleBtn.contains(e.target) && !drawer.classList.contains('hidden')) {
      setOpen(false);
    }
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !drawer.classList.contains('hidden')) {
      setOpen(false);
    }
  });
}

/* ==========================================================================
   3. BUSCA GLOBAL INTELIGENTE (CTRL + K)
   ========================================================================== */
function initSearch() {
  const searchInputs = [
    document.getElementById('global-search'),
    document.getElementById('mobile-search')
  ].filter(Boolean);

  if (searchInputs.length === 0) return;

  function handleSearch(query) {
    const q = query.toLowerCase().trim();
    const modules = document.querySelectorAll('.module-card');

    searchInputs.forEach(input => {
      if (input.value !== query) input.value = query;
    });

    let matchCount = 0;
    modules.forEach((mod) => {
      const text = mod.textContent.toLowerCase();
      if (!q || text.includes(q)) {
        mod.style.display = '';
        matchCount++;
      } else {
        mod.style.display = 'none';
      }
    });

    const noResults = document.getElementById('search-no-results');
    if (noResults) {
      if (matchCount === 0 && q) {
        noResults.classList.remove('hidden');
      } else {
        noResults.classList.add('hidden');
      }
    }
  }

  searchInputs.forEach(input => {
    input.addEventListener('input', (e) => handleSearch(e.target.value));
  });

  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      const firstInput = searchInputs[0];
      if (firstInput) {
        firstInput.focus();
        firstInput.select();
      }
    }
  });
}

/* ==========================================================================
   4. SIMULADOR INTERATIVO DE EXAME A FRESCO & VULVOVAGINITES
   ========================================================================== */
function initVulvovaginitisSimulator() {
  const phSelect = document.getElementById('sim-ph');
  const whiffCheck = document.getElementById('sim-whiff');
  const microSelect = document.getElementById('sim-micro');
  const resultBox = document.getElementById('sim-result');

  if (!phSelect || !microSelect || !resultBox) return;

  function evaluateWetMount() {
    const ph = phSelect.value; // 'normal' (<= 4.5) ou 'elevado' (> 4.5)
    const whiffPos = whiffCheck ? whiffCheck.checked : false;
    const micro = microSelect.value; // 'lacto', 'clue', 'tricho', 'hyphae', 'parabasal'

    let title = "";
    let badgeClass = "";
    let desc = "";
    let tx = "";
    let partner = "";

    if (ph === 'normal' && micro === 'hyphae') {
      title = "Candidíase Vulvovaginal (CVV)";
      badgeClass = "bg-rose-100 text-rose-900 dark:bg-rose-950 dark:text-rose-300";
      desc = "pH ácido preservado (<= 4.5), Whiff test negativo e presença marcante de hifas e blastoconídios pós-KOH 10%. Prurido intenso e corrimento em 'nata de leite'.";
      tx = "Fluconazol 150 mg VO dose única (SE GESTANTE: estritamente Clotrimazol ou Miconazol creme vaginal por 7 noites; fluconazol é contraindicado na gravidez!).";
      partner = "NÃO tratar parceiro assintomático. Tratar apenas se apresentar balanite por cândida com antifúngico tópico.";
    } else if (ph === 'elevado' && (micro === 'clue' || (whiffPos && micro !== 'tricho'))) {
      title = "Vaginose Bacteriana (VB)";
      badgeClass = "bg-amber-100 text-amber-900 dark:bg-amber-950 dark:text-amber-300";
      desc = "pH elevado (> 4.5), teste das aminas positivo (odor a peixe) e Clue Cells (células-alvo) em lâmina salina cobrindo > 20% das bordas citoplasmáticas, sem leucócitos.";
      tx = "Metronidazol 500 mg VO de 12/12h por 7 dias (ou Metronidazol gel vaginal por 5 noites). Evitar álcool durante e até 48h pós-tratamento (efeito antabuse).";
      partner = "NÃO tratar parceiro masculino de rotina (não reduz recidiva). Tratar parceira em mulheres que fazem sexo com mulheres (WMSW).";
    } else if (ph === 'elevado' && micro === 'tricho') {
      title = "Tricomoníase Vaginal";
      badgeClass = "bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-300";
      desc = "Protozoários flagelados móveis ovais com motilidade ondulante ativa em meio a intensos neutrófilos, pH > 4.5 e colpite macular ('colo em morango').";
      tx = "Metronidazol 500 mg VO 12/12h por 7 dias (CDC comprovou superioridade à antiga dose única de 2g). Seguro na gestação.";
      partner = "TRATAMENTO OBRIGATÓRIO DE TODOS OS PARCEIROS SEXUAIS! Abstinência sexual por 7 dias até término da terapia.";
    } else if (ph === 'elevado' && micro === 'parabasal') {
      title = "Vaginite Atrófica (GSM - Síndrome Geniturinária da Menopausa)";
      badgeClass = "bg-indigo-100 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-300";
      desc = "Hipoestrogenismo pós-menopausa causando adelgaçamento epitelial, perda de glicogênio e de lactobacilos, com predomínio de células parabasais/intermediárias e pH > 5.5.";
      tx = "Estrogênio tópico vaginal (Estriol ou Promestrieno creme) e hidratantes vaginais de uso contínuo.";
      partner = "Condição não infecciosa; sem indicação de manejo do parceiro.";
    } else if (ph === 'normal' && micro === 'lacto' && !whiffPos) {
      title = "Secreção Fisiológica Normal ou Vaginose Citolítica";
      badgeClass = "bg-blue-100 text-blue-900 dark:bg-blue-950 dark:text-blue-300";
      desc = "Predomínio protetor de lactobacilos de Döderlein, ausência de aminas voláteis, células escamosas límpidas e pH fisiológico (3.8 a 4.5).";
      tx = "Se assintomática: Nenhuma conduta necessária. Se prurido cíclico lúteo com citólise celular intensa: duchas com bicarbonato de sódio para elevar o pH.";
      partner = "Flora fisiológica normal.";
    } else {
      title = "Padrão Misto ou Indeterminado";
      badgeClass = "bg-slate-100 text-slate-800 dark:bg-slate-800 dark:text-slate-200";
      desc = "Os parâmetros indicam possível associação mista (ex: VB + Tricomoníase) ou fase inicial. Recomenda-se colposcopia e coleta de NAAT molecular.";
      tx = "Avaliar cultura fúngica se suspeita de Candida não-albicans (C. glabrata) ou NAAT para Trichomonas.";
      partner = "Reavaliar conforme confirmação etiológica.";
    }

    resultBox.innerHTML = `
      <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 space-y-3">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <span class="px-2.5 py-1 text-xs font-black rounded-lg ${badgeClass}">${title}</span>
          <span class="text-xs font-bold text-slate-500">Exame a Fresco / Wet Mount</span>
        </div>
        <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed"><strong>Fisiopatologia:</strong> ${desc}</p>
        <div class="p-3 rounded-lg bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 text-xs space-y-1">
          <div><strong class="text-rose-600 dark:text-rose-400">Prescrição de 1ª Linha:</strong> ${tx}</div>
          <div><strong class="text-indigo-600 dark:text-indigo-400">Conduta com o Parceiro:</strong> ${partner}</div>
        </div>
      </div>
    `;

    if (window.lucide) lucide.createIcons();
  }

  phSelect.addEventListener('change', evaluateWetMount);
  microSelect.addEventListener('change', evaluateWetMount);
  if (whiffCheck) whiffCheck.addEventListener('change', evaluateWetMount);

  evaluateWetMount();
}

/* ==========================================================================
   5. CALCULADORA DE ESCORE DE NUGENT & CRITÉRIOS DE AMSEL (VB)
   ========================================================================== */
function initAmselNugentCalculator() {
  const amselDischarge = document.getElementById('amsel-discharge');
  const amselPh = document.getElementById('amsel-ph');
  const amselWhiff = document.getElementById('amsel-whiff');
  const amselClue = document.getElementById('amsel-clue');
  const amselResult = document.getElementById('amsel-result');

  if (!amselDischarge || !amselResult) return;

  function evaluateAmsel() {
    let score = 0;
    if (amselDischarge.checked) score++;
    if (amselPh.checked) score++;
    if (amselWhiff.checked) score++;
    if (amselClue.checked) score++;

    const isPositive = score >= 3;

    if (isPositive) {
      amselResult.className = "p-4 rounded-xl border-2 bg-amber-50 dark:bg-amber-950/40 border-amber-500 text-amber-900 dark:text-amber-200 space-y-2";
      amselResult.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-amber-700 dark:text-amber-400">
          <i data-lucide="check-circle" class="w-5 h-5"></i> DIAGNÓSTICO POSITIVO DE VAGINOSE BACTERIANA (${score}/4 CRITÉRIOS DE AMSEL)
        </div>
        <p class="text-xs leading-relaxed">
          A presença de &ge; 3 critérios fecha o diagnóstico clínico formal de Vaginose Bacteriana.<br>
          <strong>Conduta:</strong> Metronidazol 500 mg VO 12/12h por 7 dias. Na gestante, tratar sempre para reduzir riscos de RPMO e parto prematuro extremo.
        </p>
      `;
    } else {
      amselResult.className = "p-4 rounded-xl border-2 bg-slate-100 dark:bg-slate-800 border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 space-y-2";
      amselResult.innerHTML = `
        <div class="flex items-center gap-2 font-bold text-sm">
          <i data-lucide="info" class="w-5 h-5"></i> CRITÉRIOS DE AMSEL INSUFICIENTES (${score}/4)
        </div>
        <p class="text-xs">
          São necessários pelo menos 3 dos 4 critérios de Amsel para o diagnóstico de Vaginose Bacteriana.
        </p>
      `;
    }

    if (window.lucide) lucide.createIcons();
  }

  [amselDischarge, amselPh, amselWhiff, amselClue].forEach(el => {
    if (el) el.addEventListener('change', evaluateAmsel);
  });

  evaluateAmsel();
}

/* ==========================================================================
   6. ESTRATIFICADOR DE CANDIDÍASE (SIMPLES VS COMPLICADA VS GESTANTE)
   ========================================================================== */
function initCandidaRiskStratifier() {
  const typeSelect = document.getElementById('candida-type');
  const pregCheck = document.getElementById('candida-preg');
  const glabrataCheck = document.getElementById('candida-glabrata');
  const resultBox = document.getElementById('candida-result');

  if (!typeSelect || !resultBox) return;

  function evaluateCandida() {
    const isPreg = pregCheck ? pregCheck.checked : false;
    const isGlabrata = glabrataCheck ? glabrataCheck.checked : false;
    const type = typeSelect.value;

    let plan = "";

    if (isPreg) {
      plan = `
        <strong class="text-rose-700 dark:text-rose-400">⚠️ REGRA MANDATÓRIA NA GESTAÇÃO:</strong><br>
        • <strong>FLUCONAZOL ORAL É FORMALMENTE CONTRAINDICADO!</strong> Associado a abortamento espontâneo e malformações craniofaciais.<br>
        • <strong>Tratamento de Escolha:</strong> Antifúngico TÓPICO azólico: <strong>Clotrimazol creme 1%</strong> ou <strong>Miconazol creme 2%</strong>, 1 aplicador vaginal ao deitar por <strong>7 noites consecutivas</strong>.
      `;
    } else if (isGlabrata) {
      plan = `
        <strong class="text-amber-700 dark:text-amber-400">Espécie Não-Albicans (*Candida glabrata*):</strong><br>
        • *C. glabrata* é naturalmente resistente aos azólicos orais convencionais.<br>
        • <strong>Tratamento de 1ª Linha:</strong> <strong>Ácido Bórico intravaginal 600 mg em cápsula gelatinosa</strong> ao deitar por 14 a 21 dias consecutivos.<br>
        • Alternativa: Nistatina óvulos 100.000 UI por 14 noites.
      `;
    } else if (type === 'recurrent') {
      plan = `
        <strong class="text-purple-700 dark:text-purple-400">Candidíase Vulvovaginal Recorrente (&ge; 4 episódios/ano):</strong><br>
        • <strong>Fase de Indução:</strong> Fluconazol 150 mg VO a cada 72 horas por 3 doses (Dias 1, 4 e 7).<br>
        • <strong>Fase de Manutenção Supressiva:</strong> <strong>Fluconazol 150 mg VO 1 vez por semana durante 6 meses contínuos</strong>.<br>
        • Rastrear diabetes oculto (glicemia de jejum/HbA1c) e imunossupressão.
      `;
    } else {
      plan = `
        <strong class="text-emerald-700 dark:text-emerald-400">Candidíase Esporádica Não Complicada (*C. albicans*):</strong><br>
        • <strong>1ª Linha Oral:</strong> <strong>Fluconazol 150 mg VO em dose única</strong>.<br>
        • Alternativa tópica: Clotrimazol creme vaginal 1% por 7 noites ou dose única de clotrimazol 500 mg óvulo vaginal.
      `;
    }

    resultBox.innerHTML = `
      <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs sm:text-sm leading-relaxed">
        ${plan}
      </div>
    `;
  }

  typeSelect.addEventListener('change', evaluateCandida);
  if (pregCheck) pregCheck.addEventListener('change', evaluateCandida);
  if (glabrataCheck) glabrataCheck.addEventListener('change', evaluateCandida);

  evaluateCandida();
}

/* ==========================================================================
   7. CALCULADORA DE CERVICITES & EXPEDITED PARTNER THERAPY (EPT)
   ========================================================================== */
function initCervicitisEPTCalculator() {
  const weightInput = document.getElementById('cerv-weight');
  const pregCheck = document.getElementById('cerv-preg');
  const resultBox = document.getElementById('cerv-result');

  if (!weightInput || !resultBox) return;

  function evaluateCervicitis() {
    const weight = parseFloat(weightInput.value) || 60;
    const isPreg = pregCheck ? pregCheck.checked : false;

    const ceftriaxoneDose = weight >= 150 ? "1 g IM" : "500 mg IM";
    const chlamydiaDrug = isPreg 
      ? "Azitromicina 1 g VO em dose única (Doxiciclina é contraindicada no 2º e 3º trimestres por toxicidade óssea/dentária)"
      : "Doxiciclina 100 mg VO de 12/12h por 7 dias (CDC 2021: eficácia superior à azitromicina em infecções retais/assintomáticas)";

    resultBox.innerHTML = `
      <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs sm:text-sm leading-relaxed space-y-2">
        <div class="font-bold text-rose-600 dark:text-rose-400 flex items-center gap-1.5">
          <i data-lucide="pill" class="w-4 h-4"></i> Esquema Terapêutico Duplo Empírico (Gonococo + Clamídia):
        </div>
        <div>• <strong>Cobertura de Gonococo:</strong> Ceftriaxona <strong>${ceftriaxoneDose}</strong> dose única profunda.</div>
        <div>• <strong>Cobertura de Clamídia:</strong> ${chlamydiaDrug}.</div>
        <div class="p-3 bg-slate-50 dark:bg-slate-900/60 rounded-lg text-xs space-y-1">
          <strong>Regras de Ouro de Manejo de Parceiros (EPT):</strong><br>
          • Notificar e tratar TODOS os parceiros sexuais dos <strong>últimos 60 dias</strong>.<br>
          • <strong>Abstinência sexual estrita por 7 dias</strong> após o início do tratamento de ambos.<br>
          • Teste de cura (NAAT) após 3 meses para detectar reinfecções frequentes.
        </div>
      </div>
    `;

    if (window.lucide) lucide.createIcons();
  }

  weightInput.addEventListener('input', evaluateCervicitis);
  if (pregCheck) pregCheck.addEventListener('change', evaluateCervicitis);

  evaluateCervicitis();
}

/* ==========================================================================
   8. ESCORE DE INTERNAÇÃO HOSPITALAR EM DIP (HAGER / CDC)
   ========================================================================== */
function initPidHospitalizationScore() {
  const criteriaInputs = document.querySelectorAll('.pid-crit');
  const resultBox = document.getElementById('pid-result');
  if (!resultBox || criteriaInputs.length === 0) return;

  function evaluatePID() {
    let checkedCount = 0;
    criteriaInputs.forEach(i => { if (i.checked) checkedCount++; });

    if (checkedCount > 0) {
      resultBox.className = "p-4 rounded-xl border-2 bg-rose-50 dark:bg-rose-950/40 border-rose-500 text-rose-900 dark:text-rose-200 space-y-2";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-rose-700 dark:text-rose-400">
          <i data-lucide="alert-triangle" class="w-5 h-5"></i> INTERNAÇÃO HOSPITALAR MANDATÓRIA (CRITÉRIO DE GRAVIDADE DETECTADO)
        </div>
        <div class="text-xs leading-relaxed">
          A presença de qualquer critério de internação exige antibioticoterapia parenteral endovenosa imediata.<br>
          <strong>Esquemas Hospitalares de 1ª Linha:</strong><br>
          • <em>Opção A (Padrão Ouro USMLE):</em> <strong>Cefoxitina 2g IV 6/6h + Doxiciclina 100 mg VO/IV 12/12h</strong>.<br>
          • <em>Opção B (Excelente para Abscesso Tubo-Ovariano ou Alergia a Cefalosporinas):</em> <strong>Clindamicina 900 mg IV 8/8h + Gentamicina IV</strong> (ataque 2 mg/kg, manutenção 1.5 mg/kg 8/8h).<br>
          • Transição para VO após 24-48h afebril até completar <strong>14 dias totais</strong>.
        </div>
      `;
    } else {
      resultBox.className = "p-4 rounded-xl border-2 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200 space-y-2";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm text-emerald-700 dark:text-emerald-400">
          <i data-lucide="check-circle" class="w-5 h-5"></i> TRATAMENTO AMBULATORIAL AUTORIZADO (CASO LEVE A MODERADO)
        </div>
        <div class="text-xs leading-relaxed">
          Paciente sem critérios de alarme, tolerando via oral e com suporte para retorno.<br>
          <strong>Esquema Ambulatorial Tríplice:</strong><br>
          • <strong>Ceftriaxona 500 mg IM dose única</strong> + <strong>Doxiciclina 100 mg VO 12/12h por 14 dias</strong> + <strong>Metronidazol 500 mg VO 12/12h por 14 dias</strong>.<br>
          • ⚠️ <strong>Reavaliação clínica obrigatória em 48 a 72 horas</strong>: se não houver melhora, internar para esquema endovenoso!
        </div>
      `;
    }

    if (window.lucide) lucide.createIcons();
  }

  criteriaInputs.forEach(i => i.addEventListener('change', evaluatePID));
  evaluatePID();
}

/* ==========================================================================
   9. CALCULADORA DE SÍFILIS & DESSENSIBILIZAÇÃO NA GESTAÇÃO
   ========================================================================== */
function initSyphilisStagingManager() {
  const stageSelect = document.getElementById('syph-stage');
  const pregCheck = document.getElementById('syph-preg');
  const allergyCheck = document.getElementById('syph-allergy');
  const resultBox = document.getElementById('syph-result');

  if (!stageSelect || !resultBox) return;

  function evaluateSyphilis() {
    const stage = stageSelect.value;
    const isPreg = pregCheck ? pregCheck.checked : false;
    const hasAllergy = allergyCheck ? allergyCheck.checked : false;

    if (isPreg && hasAllergy) {
      resultBox.className = "p-4 rounded-xl border-2 bg-rose-600 text-white space-y-2";
      resultBox.innerHTML = `
        <div class="flex items-center gap-2 font-black text-sm">
          <i data-lucide="alert-octagon" class="w-5 h-5"></i> EMERGÊNCIA OBSTÉTRICA: DESSENSIBILIZAÇÃO À PENICILINA OBRIGATÓRIA!
        </div>
        <p class="text-xs leading-relaxed">
          <strong>A Penicilina G Benzatina é o ÚNICO fármaco que atravessa a placenta e trata o concepto prevenindo a sífilis congênita!</strong><br>
          • NÃO USAR Doxiciclina (contraindicada na gestação) e NÃO USAR Azitromicina (alta taxa de resistência treponêmica e falha transplacentária).<br>
          • <strong>Conduta Mandatória:</strong> Internação em ambiente hospitalar monitorizado e realização de <strong>DESSENSIBILIZAÇÃO ORAL À PENICILINA</strong>, seguida imediatamente pela administração da dose plena de Penicilina Benzatina!<br>
          • A primeira dose deve ocorrer com conclusão de todas as doses <strong>pelo menos 30 dias antes do parto</strong>.
        </p>
      `;
      if (window.lucide) lucide.createIcons();
      return;
    }

    let dose = "";
    if (stage === 'early') {
      dose = "Penicilina G Benzatina 2.4 milhões de UI IM em DOSE ÚNICA (1.2 mi UI em cada glúteo).";
    } else if (stage === 'late') {
      dose = "Penicilina G Benzatina 2.4 milhões de UI IM por semana durante 3 SEMANAS CONSECUTIVAS (Dose total: 7.2 milhões de UI).";
    } else {
      dose = "Penicilina G Cristalina / Potássica 18 a 24 milhões de UI/dia IV (3 a 4 mi UI IV a cada 4 horas ou infusão contínua) por 10 a 14 dias.";
    }

    resultBox.className = "p-4 rounded-xl border-2 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200 space-y-2";
    resultBox.innerHTML = `
      <div class="flex items-center gap-2 font-black text-sm text-emerald-700 dark:text-emerald-400">
        <i data-lucide="shield-check" class="w-5 h-5"></i> ESQUEMA PADRÃO OURO DE PENICILINA
      </div>
      <p class="text-xs leading-relaxed">
        <strong>Prescrição:</strong> ${dose}<br>
        <strong>Controle de Cura:</strong> VDRL quantitativo a cada 3 meses (mensal na gestante). Sucesso definido por queda de &ge; 4 vezes (2 diluições) no título.<br>
        <em>Reação de Jarisch-Herxheimer:</em> Febre e calafrios nas primeiras 24h pós-dose por lise treponêmica. Conduta: Suporte sintomático. Não é alergia!
      </p>
    `;

    if (window.lucide) lucide.createIcons();
  }

  stageSelect.addEventListener('change', evaluateSyphilis);
  if (pregCheck) pregCheck.addEventListener('change', evaluateSyphilis);
  if (allergyCheck) allergyCheck.addEventListener('change', evaluateSyphilis);

  evaluateSyphilis();
}

/* ==========================================================================
   10. DIAGNÓSTICO DIFERENCIAL INTERATIVO DE ÚLCERAS GENITAIS
   ========================================================================== */
function initGenitalUlcerDifferentiator() {
  const painSelect = document.getElementById('ulcer-pain');
  const countSelect = document.getElementById('ulcer-count');
  const buboSelect = document.getElementById('ulcer-bubo');
  const resultBox = document.getElementById('ulcer-result');

  if (!painSelect || !resultBox) return;

  function evaluateUlcer() {
    const isPainful = painSelect.value === 'painful';
    const isMultiple = countSelect.value === 'multiple';
    const buboType = buboSelect.value; // 'none', 'single', 'multi', 'bilateral'

    let disease = "";
    let agent = "";
    let tx = "";

    if (!isPainful && !isMultiple) {
      disease = "Sífilis Primária (Cancro Duro)";
      agent = "Treponema pallidum";
      tx = "Penicilina G Benzatina 2.4 milhões de UI IM dose única.";
    } else if (isPainful && isMultiple && buboType === 'bilateral') {
      disease = "Herpes Genital (HSV-1 / HSV-2)";
      agent = "Herpes Simplex Virus";
      tx = "Valaciclovir 1g VO 12/12h por 7-10 dias (Aciclovir 400 mg 3x/dia).";
    } else if (isPainful && buboType === 'single') {
      disease = "Cancro Mole";
      agent = "Haemophilus ducreyi";
      tx = "Azitromicina 1g VO dose única (ou Ceftriaxona 250 mg IM).";
    } else if (!isPainful && buboType === 'multi') {
      disease = "Linfogranuloma Venéreo (LGV)";
      agent = "Chlamydia trachomatis (L1-L3)";
      tx = "Doxiciclina 100 mg VO 12/12h por 21 dias.";
    } else if (!isPainful && buboType === 'none') {
      disease = "Donovanose (Granuloma Inguinale)";
      agent = "Klebsiella granulomatis";
      tx = "Azitromicina 1g VO 1x/semana por >= 3 semanas (até cicatrização).";
    } else {
      disease = "Herpes Genital ou Cancro Mole";
      agent = "Investigar com PCR viral e coloração de Gram";
      tx = "Terapia empírica antiviral ou azitromicina conforme gravidade.";
    }

    resultBox.innerHTML = `
      <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 space-y-2">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <span class="text-sm font-black text-rose-600 dark:text-rose-400">${disease}</span>
          <span class="text-xs font-bold text-slate-500">${agent}</span>
        </div>
        <p class="text-xs text-slate-600 dark:text-slate-300"><strong>Conduta Farmacológica:</strong> ${tx}</p>
      </div>
    `;
  }

  [painSelect, countSelect, buboSelect].forEach(el => {
    if (el) el.addEventListener('change', evaluateUlcer);
  });

  evaluateUlcer();
}

/* ==========================================================================
   11. RASTREAMENTO CERVICAL & CONDUTA BETHESDA (ASCCP vs INCA)
   ========================================================================== */
function initHpvBethesdaGuide() {
  const bethesdaSelect = document.getElementById('hpv-bethesda');
  const ageSelect = document.getElementById('hpv-age');
  const hpvPosCheck = document.getElementById('hpv-positive');
  const resultBox = document.getElementById('hpv-result');

  if (!bethesdaSelect || !resultBox) return;

  function evaluateBethesda() {
    const lesion = bethesdaSelect.value;
    const age = parseInt(ageSelect.value) || 28;
    const hasHPV = hpvPosCheck ? hpvPosCheck.checked : false;

    let action = "";

    if (lesion === 'ascus') {
      if (hasHPV || age >= 30) {
        action = "COLPOSCOPIA IMEDIATA (ASC-US com teste de HPV de alto risco positivo ou idade >= 30 anos).";
      } else {
        action = "Repetir citologia em 12 meses (ou em 3 anos se < 25 anos segundo INCA). Baixo risco de NIC 3 imediata.";
      }
    } else if (lesion === 'lsil') {
      action = "Repetir citologia em 6 meses (Diretriz INCA/Brasil) OU Colposcopia direta se >= 25 anos com HPV+ (Diretriz ASCCP/EUA). Lesão de baixo grau com alta taxa de regressão espontânea.";
    } else if (lesion === 'asch' || lesion === 'hsil') {
      action = "COLPOSCOPIA IMEDIATA COM BIÓPSIA DIRIGIDA OBRIGATÓRIA! Risco expressivo de NIC 2/3 oculta (opção 'ver e tratar' com CAF/LEEP em > 25 anos nos EUA).";
    } else if (lesion === 'agc') {
      action = "COLPOSCOPIA COM AVALIAÇÃO ENDOCERVICAL E BIÓPSIA DE ENDOMÉTRIO (se >= 35 anos ou com risco de neoplasia endometrial).";
    }

    resultBox.innerHTML = `
      <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs sm:text-sm font-semibold text-slate-800 dark:text-slate-100">
        <strong class="text-rose-600 dark:text-rose-400 block mb-1">Conduta Baseada nas Diretrizes ASCCP / INCA:</strong>
        ${action}
      </div>
    `;
  }

  [bethesdaSelect, ageSelect].forEach(el => el.addEventListener('change', evaluateBethesda));
  if (hpvPosCheck) hpvPosCheck.addEventListener('change', evaluateBethesda);

  evaluateBethesda();
}

/* ==========================================================================
   12. TRANSMISSÃO VERTICAL DO HIV NO PARTO
   ========================================================================== */
function initHivVerticalTransmissionCalculator() {
  const vlInput = document.getElementById('hiv-vl');
  const resultBox = document.getElementById('hiv-result');

  if (!vlInput || !resultBox) return;

  function evaluateHIVDelivery() {
    const vl = parseFloat(vlInput.value) || 0;

    let route = "";
    let azt = "";
    let badgeClass = "";

    if (vl < 1000) {
      route = "PARTO VAGINAL PERMITIDO (Se condições obstétricas favoráveis)";
      azt = vl < 50 ? "Não necessita AZT venoso se carga viral indetectável (< 50 cópias)" : "AZT endovenoso contínuo durante o trabalho de parto";
      badgeClass = "bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-300";
    } else {
      route = "CESARIANA ELETIVA PROGRAMADA COM 38 SEMANAS (Antes do início do TP e com bolsa íntegra)";
      azt = "Zidovudina (AZT) Endovenoso Contínuo obrigatório, iniciado 3 horas antes da incisão cirúrgica até clampeamento do cordão";
      badgeClass = "bg-rose-600 text-white";
    }

    resultBox.innerHTML = `
      <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 space-y-2">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <span class="px-2.5 py-1 text-xs font-black rounded-lg ${badgeClass}">${route}</span>
          <span class="text-xs font-bold text-slate-500">Carga Viral: ${vl.toLocaleString()} cópias/mL</span>
        </div>
        <p class="text-xs text-slate-600 dark:text-slate-300"><strong>Protocolo de Zidovudina (AZT):</strong> ${azt}</p>
        <div class="p-3 bg-rose-50 dark:bg-rose-950/40 rounded-lg text-xs text-rose-900 dark:text-rose-200 font-semibold">
          🚨 AMAMENTAÇÃO ABSOLUTAMENTE CONTRAINDICADA! Prescrever Cabergolina 1.0 mg VO em dose única nas primeiras 24h pós-parto para inibir lactação e fornecer fórmula láctea infantil exclusiva.
        </div>
      </div>
    `;
  }

  vlInput.addEventListener('input', evaluateHIVDelivery);
  evaluateHIVDelivery();
}

/* ==========================================================================
   13. RASTREADOR DE PEP E PREP
   ========================================================================== */
function initPepPrepTracker() {
  const hoursInput = document.getElementById('pep-hours');
  const resultBox = document.getElementById('pep-result');

  if (!hoursInput || !resultBox) return;

  function evaluatePEP() {
    const hours = parseFloat(hoursInput.value) || 12;

    if (hours <= 72) {
      resultBox.className = "p-4 rounded-xl border-2 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-200 text-xs leading-relaxed space-y-1";
      resultBox.innerHTML = `
        <strong class="font-bold text-emerald-700 dark:text-emerald-400 block text-sm">DENTRO DA JANELA DE EFICÁCIA DA PEP (&le; 72 HORAS)!</strong>
        • Iniciar o mais rápido possível (ideal nas primeiras 2 horas).<br>
        • <strong>Esquema Tríplice por 28 Dias Ininterruptos:</strong> Tenofovir (TDF 300 mg) + Lamivudina (3TC 300 mg) + Dolutegravir (DTG 50 mg) 1x/dia.<br>
        • Testagem rápida tempo zero para HIV, Sífilis, Hepatites B e C; controle sorológico com 30 e 90 dias.
      `;
    } else {
      resultBox.className = "p-4 rounded-xl border-2 bg-rose-50 dark:bg-rose-950/40 border-rose-500 text-rose-900 dark:text-rose-200 text-xs leading-relaxed space-y-1";
      resultBox.innerHTML = `
        <strong class="font-bold text-rose-700 dark:text-rose-400 block text-sm">FORA DA JANELA TEMPORAL DA PEP (> 72 HORAS)!</strong>
        • A eficácia profilática após 72 horas é nula segundo ensaios clínicos.<br>
        • Não iniciar antirretrovirais como profilaxia; realizar testagem basal e acompanhamento sorológico com 30 e 90 dias para detecção de infecção precoce.
      `;
    }
  }

  hoursInput.addEventListener('input', evaluatePEP);
  evaluatePEP();
}

/* ==========================================================================
   14. FLASHCARDS 3D INTERATIVOS (15 CARDS HIGH-YIELD)
   ========================================================================== */
const FLASHCARDS_DATA = [
  {
    category: "Módulo 50: Ecossistema Vaginal",
    q: "Qual o principal mecanismo pelo qual os lactobacilos mantêm o pH vaginal ácido (3.8 a 4.5)?",
    a: "Eles hidrolisam e fermentam o glicogênio intracelular das células escamosas em ácido lático, além de produzirem peróxido de hidrogênio (H2O2) e bacteriocinas protetoras."
  },
  {
    category: "Módulo 51: Vaginose Bacteriana",
    q: "Por que NÃO se recomenda o tratamento rotineiro do parceiro sexual masculino na Vaginose Bacteriana?",
    a: "Ensaios clínicos randomizados provaram que o tratamento de parceiros masculinos não reduz a taxa de recorrência da VB em mulheres heterossexuais, pois a VB é uma disbiose e não uma IST clássica."
  },
  {
    category: "Módulo 51: Candidíase na Gestação",
    q: "Por que o Fluconazol oral é formalmente contraindicado no tratamento da candidíase na gravidez?",
    a: "Porque está associado a risco aumentado de abortamento espontâneo no 1º trimestre e malformações craniofaciais e cardíacas congênitas. Na gestação, usar EXCLUSIVAMENTE antifúngicos tópicos azólicos por 7 dias."
  },
  {
    category: "Módulo 51: Tricomoníase Vaginal",
    q: "Qual a atualização posológica crucial do CDC para o tratamento da Tricomoníase em mulheres?",
    a: "O CDC preconiza Metronidazol 500 mg VO 12/12h por 7 dias, esquema comprovadamente superior à antiga dose única de 2g (reduz taxa de falha em 50%). Tratar obrigatoriamente o parceiro!"
  },
  {
    category: "Módulo 52: Cervicites",
    q: "Qual o tratamento empírico de primeira linha para cervicite cobrindo Gonococo e Clamídia simultaneamente?",
    a: "Ceftriaxona 500 mg IM em dose única (1g se peso >= 150 kg) associada a Doxiciclina 100 mg VO 12/12h por 7 dias (ou Azitromicina 1g VO dose única na gestante)."
  },
  {
    category: "Módulo 53: Doença Inflamatória Pélvica",
    q: "O que é o Chandelier Sign (sinal do lustre/rastelo) observado no toque bimanual na DIP?",
    a: "É a dor excruciante à mobilização do colo uterino, que faz a paciente quase saltar da maca devido ao estiramento dos ligamentos e reflexo de irritação peritoneal pélvica."
  },
  {
    category: "Módulo 53: Síndrome de Fitz-Hugh-Curtis",
    q: "Quais os achados laboratoriais de transaminases e o achado laparoscópico clássico em Fitz-Hugh-Curtis?",
    a: "As transaminases hepáticas (AST/ALT) estão normais ou discretamente elevadas (inflama apenas a cápsula de Glisson), e a laparoscopia revela aderências em 'cordas de violino' entre o fígado e a parede diafragmática."
  },
  {
    category: "Módulo 53: Abscesso Tubo-Ovariano",
    q: "Qual a conduta indicada diante de um Abscesso Tubo-Ovariano estável que falha após 48-72h de ATB venoso?",
    a: "Drenagem percutânea guiada por imagem (Ultrassonografia ou Tomografia Computadorizada), procedimento minimamente invasivo que preserva a fertilidade e evita laparotomia."
  },
  {
    category: "Módulo 54: Sífilis na Gestação",
    q: "Qual a conduta mandatória diante de gestante com sífilis e histórico de anafilaxia confirmada à penicilina?",
    a: "DESSENSIBILIZAÇÃO HOSPITALAR À PENICILINA ORAL seguida imediatamente de Penicilina Benzatina plena. A penicilina é o único antibiótico que trata o feto e previne sífilis congênita!"
  },
  {
    category: "Módulo 54: Reação de Jarisch-Herxheimer",
    q: "O que é a Reação de Jarisch-Herxheimer e qual sua conduta?",
    a: "Reação inflamatória aguda febril com calafrios nas primeiras 24h pós-penicilina devido à lise massiva de espiroquetas. É autolimitada. Conduta: suporte com antitérmicos. NÃO é alergia e não contraindica penicilina!"
  },
  {
    category: "Módulo 55: Úlceras Genitais",
    q: "Como diferenciar clinicamente o Cancro Duro (Sífilis) do Cancro Mole (Haemophilus ducreyi)?",
    a: "O Cancro Duro é único, INDOLOR, de base limpa endurecida e adenopatia sem supuração. O Cancro Mole é composto por múltiplas úlceras EXTREMAMENTE DOLOROSAS, base purulenta suja e bubão que fistuliza por orifício único."
  },
  {
    category: "Módulo 55: Herpes Genital e Parto",
    q: "Qual a conduta obstétrica formal diante de gestante em trabalho de parto com lesão ativa de herpes genital?",
    a: "CESARIANA IMEDIATA MANDATÓRIA! O parto vaginal é formalmente contraindicado devido ao risco altíssimo de transmissão vertical de herpes neonatal disseminado com encefalite."
  },
  {
    category: "Módulo 56: Biologia do HPV",
    q: "Como as oncoproteínas E6 e E7 do HPV de alto risco (16 e 18) induzem a carcinogênese?",
    a: "A oncoproteína E6 liga-se e degrada a proteína supressora p53 (bloqueando a apoptose), enquanto a E7 inativa a proteína pRb, liberando o fator E2F e forçando a proliferação celular mitótica contínua."
  },
  {
    category: "Módulo 57: HIV e Via de Parto",
    q: "Qual o ponto de corte da Carga Viral do HIV com 34 a 36 semanas que autoriza o parto vaginal?",
    a: "Carga Viral < 1.000 cópias/mL (idealmente indetectável < 50 cópias). Se Carga Viral >= 1.000 cópias/mL ou desconhecida: Cesariana eletiva programada com 38 semanas + AZT venoso 3h antes."
  },
  {
    category: "Módulo 57: Amamentação e HIV",
    q: "Por que a amamentação é contraindicada em puérperas com HIV no Brasil e nos EUA?",
    a: "Porque o aleitamento materno adiciona um risco de 15 a 20% de transmissão vertical do HIV. O SUS e os serviços de saúde fornecem fórmula láctea infantil gratuita e prescreve-se Cabergolina 1.0 mg para inibir lactação."
  }
];

function initFlashcards() {
  let currentIndex = 0;
  const card = document.getElementById('flashcard');
  const catOut = document.getElementById('fc-category');
  const qOut = document.getElementById('fc-question');
  const aOut = document.getElementById('fc-answer');
  const countOut = document.getElementById('fc-counter');
  const prevBtn = document.getElementById('fc-prev');
  const nextBtn = document.getElementById('fc-next');
  const flipBtn = document.getElementById('fc-flip');

  if (!card || !qOut || !aOut) return;

  function renderCard() {
    card.classList.remove('card-flipped');
    const item = FLASHCARDS_DATA[currentIndex];
    catOut.textContent = item.category;
    qOut.textContent = item.q;
    aOut.innerHTML = item.a.replace(/\n/g, '<br>');
    if (countOut) countOut.textContent = `${currentIndex + 1} de ${FLASHCARDS_DATA.length}`;
  }

  card.addEventListener('click', () => {
    card.classList.toggle('card-flipped');
  });

  if (flipBtn) {
    flipBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      card.classList.toggle('card-flipped');
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (currentIndex > 0) {
        currentIndex--;
        renderCard();
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (currentIndex < FLASHCARDS_DATA.length - 1) {
        currentIndex++;
        renderCard();
      }
    });
  }

  renderCard();
}

/* ==========================================================================
   15. SIMULADO CLÍNICO INTERATIVO (15 VINHETAS ESTILO USMLE STEP 2 CK)
   ========================================================================== */
const QUIZ_DATA = [
  {
    id: 1,
    stem: "Uma mulher de 26 anos comparece ao ambulatório com queixa de corrimento vaginal com odor desagradável há 1 semana, que piora significativamente após relações sexuais desprotegidas. Nega febre, dor pélvica ou prurido vulvar. Ao exame especular, observa-se secreção homogênea, fina, branco-acinzentada, aderente às paredes vaginais, sem hiperemia vulvovaginal. O pH vaginal é 5.3. A adição de KOH 10% a uma gota da secreção em lâmina libera odor fétido pronunciado. Qual dos seguintes achados é mais provável de ser encontrado na microscopia óptica com solução salina?",
    options: [
      "Estruturas ovais birrefringentes com brotamento e hifas verdadeiras",
      "Organismos unicelulares flagelados com movimento ondulatório ativo e miríades de leucócitos",
      "Células epiteliais escamosas com citoplasma recoberto por cocobacilos obscurecendo as margens celulares (Clue Cells)",
      "Células parabasais abundantes com ausência completa de bactérias",
      "Diplococos Gram-negativos intracelulares em neutrófilos polimorfonucleares"
    ],
    correct: 2,
    explanation: "Trata-se de Vaginose Bacteriana (VB) preenchendo todos os 4 critérios de Amsel. Na microscopia salina, o achado patognomônico são as Clue Cells (células-alvo/células-guia), caracterizadas por células escamosas cobertas por bactérias aderidas (Gardnerella/Atopobium) com perda da nitidez das margens celulares."
  },
  {
    id: 2,
    stem: "Uma primigesta de 28 anos, na 10ª semana de gestação, apresenta prurido vulvar intenso, disúria externa e corrimento branco espesso semelhante a grumos de nata de leite. Ao exame físico, a vulva está intensamente eritematosa, com escoriações por coçadura e fissuras labiais. O exame especular revela placas brancas aderentes à mucosa vaginal; colo sem secreção purulenta. O pH vaginal é 4.2. O exame a fresco com KOH 10% revela hifas e esporos. Qual é o tratamento de primeira linha mais apropriado para esta paciente?",
    options: [
      "Fluconazol 150 mg VO em dose única",
      "Clotrimazol creme vaginal 1% por 7 noites consecutivas",
      "Metronidazol gel vaginal 0.75% por 5 noites",
      "Ácido bórico intravaginal 600 mg por 14 dias",
      "Fluconazol 150 mg VO a cada 72 horas por 3 doses"
    ],
    correct: 1,
    explanation: "Gestantes com candidíase vulvovaginal DEVEM ser tratadas EXCLUSIVAMENTE com antifúngicos tópicos azólicos (clotrimazol ou miconazol creme vaginal por 7 dias). O fluconazol oral está associado a risco de abortamento espontâneo no 1º trimestre e anomalias congênitas craniofaciais e cardíacas em doses cumulativas, sendo contraindicado."
  },
  {
    id: 3,
    stem: "Uma mulher de 32 anos apresenta corrimento vaginal profuso amarelo-esverdeado e fétido há 5 dias. O exame especular revela mucosa vaginal hiperemiada com petéquias difusas no colo uterino ('colo em morango') e secreção espumosa em fundo de saco posterior. A microscopia salina imediata demonstra protozoários móveis com flagelos e numerosos leucócitos. A paciente não é gestante e tem um parceiro fixo assintomático. De acordo com as diretrizes mais recentes do CDC, qual é a conduta farmacológica mais adequada para a paciente e seu parceiro?",
    options: [
      "Paciente: Metronidazol 2g VO dose única; Parceiro: não necessita de tratamento por ser assintomático",
      "Paciente: Metronidazol 500 mg VO 12/12h por 7 dias; Parceiro: Metronidazol 500 mg VO 12/12h por 7 dias (ou 2g dose única)",
      "Paciente: Doxiciclina 100 mg VO 12/12h por 7 dias; Parceiro: Doxiciclina 100 mg VO 12/12h por 7 dias",
      "Paciente: Metronidazol gel vaginal 0.75% por 5 dias; Parceiro: Metronidazol 2g VO dose única",
      "Paciente: Ceftriaxona 500 mg IM dose única; Parceiro: Ceftriaxona 500 mg IM dose única"
    ],
    correct: 1,
    explanation: "O CDC atualizou a diretriz de tricomoníase em mulheres: o esquema de Metronidazol 500 mg VO 12/12h por 7 dias é comprovadamente superior à antiga dose única de 2g (reduz em 50% as taxas de falha). O tratamento do parceiro sexual é mandatório para interromper a reinfecção."
  },
  {
    id: 4,
    stem: "Uma mulher de 21 anos, nuligesta, procura a emergência com dor no baixo ventre há 3 dias. Refere febre não aferida e náuseas, sem vômitos. Ao exame: temperatura axilar de 38.4 °C, PA 115/70 mmHg, FC 92 bpm. Ao toque vaginal bimanual, há dor excruciante à mobilização do colo uterino e espessamento doloroso anexial bilateral, sem massas. O teste de gravidez é negativo. A ultrassonografia transvaginal mostra líquido livre laminar na pelve e espessamento tubário, sem coleções císticas ou abscessos. A paciente tolera via oral e tem fácil acesso ao hospital. Qual é o plano de manejo inicial mais adequado?",
    options: [
      "Internação hospitalar para Laparotomia exploradora imediata",
      "Internação hospitalar para antibioticoterapia endovenosa com Cefoxitina e Doxiciclina",
      "Tratamento ambulatorial com Ceftriaxona 500 mg IM dose única + Doxiciclina 100 mg VO 12/12h por 14 dias + Metronidazol 500 mg VO 12/12h por 14 dias, com reavaliação em 48 a 72 horas",
      "Tratamento ambulatorial com Azitromicina 1g VO em dose única e analgesia",
      "Internação hospitalar para Drenagem percutânea transvaginal"
    ],
    correct: 2,
    explanation: "A paciente tem critérios inequívocos de DIP (dor à mobilização cervical + febre > 38.3 °C). No entanto, NÃO preenche critérios de internação hospitalar (sem ATO, não é gestante, sem peritonite difusa, tolera via oral). Logo, o esquema ambulatorial tríplice (Ceftriaxona + Doxiciclina + Metronidazol) com reavaliação obrigatória em 48-72h é o preconizado."
  },
  {
    id: 5,
    stem: "Uma paciente de 34 anos está internada há 72 horas recebendo Ampicilina/Sulbactam IV e Doxiciclina IV para tratamento de abscesso tubo-ovariano (ATO) medindo 7 cm em anexo direito. Apesar do tratamento antimicrobiano, a paciente mantém picos febris diários de 38.8 °C, leucocitose persistente (18.000/mcL) e dor abdominal progressiva em fossa ilíaca direita, sem sinais de choque ou peritonite difusa. A tomografia de pelve confirma abscesso de 7.5 cm uniloculado sem ar livre. Qual é a próxima etapa mais adequada no manejo?",
    options: [
      "Trocar a antibioticoterapia para Ciprofloxacino oral e dar alta",
      "Histerectomia abdominal total com salpingo-ooforectomia bilateral de urgência",
      "Drenagem percutânea do abscesso guiada por imagem (TC ou USG) e manutenção dos antibióticos parenterais",
      "Manter o mesmo esquema medicamentoso por mais 7 dias antes de qualquer intervenção",
      "Laparotomia exploradora com ooforoplastia parcial"
    ],
    correct: 2,
    explanation: "Em pacientes com abscesso tubo-ovariano que apresentam falha do tratamento clínico após 48 a 72 horas e permanecem hemodinamicamente estáveis sem ruptura, a conduta padrão ouro é a Drenagem Percutânea guiada por TC ou USG, que esvazia a loja infecciosa e preserva os órgãos reprodutivos."
  },
  {
    id: 6,
    stem: "Uma primigesta de 24 anos com 14 semanas de gestação apresenta VDRL reagente (1:32) e teste treponêmico reagente. Ela é assintomática e relata história prévia bem documentada de anafilaxia à penicilina na infância (edema de glote e hipotensão). Qual é a conduta mandatória imediata para o tratamento desta paciente?",
    options: [
      "Prescrever Doxiciclina 100 mg VO 12/12h por 14 dias",
      "Prescrever Ceftriaxona 1g IV diário por 10 dias",
      "Prescrever Azitromicina 2g VO em dose única",
      "Internação hospitalar para protocolo de dessensibilização oral à penicilina, seguida de Penicilina G Benzatina plena",
      "Aguardar o terceiro trimestre para iniciar o tratamento fetal"
    ],
    correct: 3,
    explanation: "A Penicilina G Benzatina é o ÚNICO antimicrobiano comprovadamente eficaz para tratar a gestante e prevenir a sífilis congênita no feto. Gestante alérgica à penicilina DEVE OBRIGATORIAMENTE ser submetida à DESSENSIBILIZAÇÃO À PENICILINA em ambiente hospitalar, recebendo a dose correta de penicilina logo em seguida."
  },
  {
    id: 7,
    stem: "Uma gestante de 20 semanas recebeu sua primeira injeção de 2.4 milhões de UI de Penicilina G Benzatina para sífilis secundária. Oito horas após a injeção, procura a emergência com calafrios intensos, febre de 38.6 °C, cefaleia e mialgia difusa. Os batimentos fetais estão normais (155 bpm) e o útero está normotônico. Qual é o diagnóstico e o manejo apropriado?",
    options: [
      "Reação anafilática tardia à penicilina; administrar adrenalina IM e suspender penicilina",
      "Reação de Jarisch-Herxheimer; suporte clínico com antitérmicos e hidratação oral, tranquilizando a paciente",
      "Corioamnionite aguda por infecção bacteriana ascendente; indicar cesariana de emergência",
      "Descolamento prematuro de placenta; realizar amniotomia imediata",
      "Falha terapêutica do treponema; iniciar Vancomicina IV"
    ],
    correct: 1,
    explanation: "Trata-se da clássica Reação de Jarisch-Herxheimer, resposta febril aguda autolimitada desencadeada pela lise massiva de espiroquetas nas primeiras horas pós-penicilina com liberação de endotoxinas. O manejo é suporte clínico com antitérmicos. NÃO é reação alérgica e não contraindica doses futuras."
  },
  {
    id: 8,
    stem: "Uma mulher de 23 anos comparece com dor vulvar intensa há 4 dias. Ao exame, observam-se quatro úlceras profundas e extremamente dolorosas no introito vaginal com exsudato purulento amarelado e bordas irregulares descoladas que sangram com facilidade. Na região inguinal esquerda, palpa-se linfonodomegalia volumosa de 4 cm dolorosa e flutuante. O VDRL e o PCR para herpes são negativos. Qual o agente etiológico mais provável e o tratamento recomendado?",
    options: [
      "Treponema pallidum; Penicilina G Benzatina 2.4 mi UI IM",
      "Haemophilus ducreyi; Azitromicina 1g VO dose única (ou Ceftriaxona 250 mg IM)",
      "Chlamydia trachomatis sorotipos L1-L3; Doxiciclina 100 mg VO 12/12h por 21 dias",
      "Klebsiella granulomatis; Ciprofloxacino 500 mg VO 12/12h por 14 dias",
      "Vírus Herpes Simples tipo 2; Valaciclovir 1g VO 12/12h por 10 dias"
    ],
    correct: 1,
    explanation: "Úlceras genitais múltiplas, extremamente dolorosas, de base suja e purulenta, que sangram com facilidade, associadas a linfonodomegalia unilateral inflamatória que amolece e flutua (bubão venéreo com orifício único) é o quadro patognomônico de Cancro Mole, causado pelo Haemophilus ducreyi. Tratamento: Azitromicina 1g VO dose única."
  },
  {
    id: 9,
    stem: "Uma gestante de 39 semanas entra em trabalho de parto ativo em 5 cm de dilatação. Possui diagnóstico prévio de herpes genital recorrente e fez profilaxia com aciclovir a partir de 36 semanas. Ao exame na admissão, observam-se três vesículas intactas agrupadas sobre base eritematosa no grande lábio direito com ardência local. A vitalidade fetal é categoria 1. Qual é a conduta obstétrica mandatória?",
    options: [
      "Realizar amniotomia precoce e prosseguir com parto vaginal com proteção de campo estéril",
      "Realizar cesariana imediata",
      "Aplicar gel de aciclovir tópico na lesão e prosseguir com parto vaginal",
      "Coletar swab para PCR de herpes e aguardar o resultado do teste rápido",
      "Administrar dose de ataque de Aciclovir 10 mg/kg IV e aguardar parto normal"
    ],
    correct: 1,
    explanation: "A presença de qualquer lesão ativa de herpes genital (vesículas ou úlceras) ou sintomas prodrômicos no momento do trabalho de parto ou rotura de membranas é INDICAÇÃO FORMAL E ABSOLUTA DE CESARIANA IMEDIATA, evitando contato do feto com vírus infectante no canal de parto e prevenindo o herpes neonatal letal."
  },
  {
    id: 10,
    stem: "Uma mulher de 32 anos apresenta citologia em meio líquido revelando: Células escamosas atípicas de significado indeterminado (ASC-US). O teste molecular reflexo de DNA-HPV de alto risco oncogênico resultou POSITIVO. Pelas diretrizes baseadas em risco da ASCCP, qual é a conduta imediata indicada?",
    options: [
      "Repetir a citologia oncótica em 1 ano",
      "Encaminhar para Colposcopia imediata",
      "Realizar conização cervical por CAF/LEEP imediatamente ('ver e tratar')",
      "Repetir o teste de HPV em 6 meses",
      "Tranquilizar a paciente e agendar retorno de rotina em 3 anos"
    ],
    correct: 1,
    explanation: "Pelas diretrizes da ASCCP, uma paciente com ASC-US cujo teste de HPV de alto risco seja POSITIVO apresenta risco imediato de NIC 3+ de aproximadamente 4.5%, ultrapassando o limiar clínico que exige Colposcopia Imediata."
  },
  {
    id: 11,
    stem: "Mulher de 38 anos tem citologia com Lesão Intraepitelial Escamosa de Alto Grau (HSIL). A colposcopia revela Zona de Transformação não visualizada penetrando profundamente no canal endocervical (ZT Tipo 3). A biópsia revela NIC 2 com margens endocervicais não avaliáveis. A paciente tem prole constituída. Qual o tratamento de escolha?",
    options: [
      "Crioterapia com nitrogênio líquido do colo uterino",
      "Procedimento excisional tipo conização (cone a frio ou CAF/LEEP profundo com avaliação de margens)",
      "Histerectomia total abdominal imediata sem estudo prévio do cone",
      "Acompanhamento citológico e colposcópico a cada 6 meses",
      "Aplicação de Imiquimode intravaginal semanal"
    ],
    correct: 1,
    explanation: "Em pacientes com NIC 2/3 e Zona de Transformação tipo 3 (endocervical), métodos ablativos (crioterapia) são contraindicados porque não fornecem peça cirúrgica para afastar carcinoma invasor oculto. O padrão ouro é a Conização cirúrgica para avaliação diagnóstica e terapêutica completa das margens."
  },
  {
    id: 12,
    stem: "Uma médica residente sofreu acidente perfurocortante profundo com agulha com sangue visível de paciente com HIV reagente há 1 hora. O teste rápido da residente é não reagente e a função renal é normal. Qual é a conduta profilática recomendada?",
    options: [
      "Iniciar Tenofovir + Lamivudina + Dolutegravir por 28 dias ininterruptos, idealmente nas primeiras horas",
      "Coletar carga viral da residente e aguardar o resultado em 48 horas antes de prescrever qualquer medicação",
      "Prescrever Zidovudina em monoterapia por 14 dias",
      "Iniciar Tenofovir + Entricitabina por 7 dias associado a reforço de vacina de hepatite B",
      "Nenhuma medicação é necessária, apenas acompanhamento sorológico aos 30 e 90 dias"
    ],
    correct: 0,
    explanation: "A Profilaxia Pós-Exposição (PEP) de risco para o HIV deve ser iniciada o mais rápido possível (idealmente nas primeiras 2h, máximo 72h) e mantida por 28 dias consecutivos com o esquema tríplice padrão: Tenofovir (TDF) + Lamivudina (3TC) + Dolutegravir (DTG)."
  },
  {
    id: 13,
    stem: "Mulher vivendo com HIV na 35ª semana de gestação recebe resultado de Carga Viral coletada na 34ª semana de 4.800 cópias/mL. O feto está hígido em apresentação cefálica. Qual é a conduta preconizada para a via de parto?",
    options: [
      "Indicar cesariana eletiva programada na 38ª semana de gestação com infusão intraparto de Zidovudina (AZT) endovenosa",
      "Aguardar o início espontâneo do trabalho de parto para permitir parto vaginal com fórceps",
      "Induzir o parto vaginal com ocitocina com 37 semanas e rotura artificial da bolsa",
      "Indicar parto vaginal e autorizar amamentação se a carga viral zerar no pós-parto",
      "Suspender a TARV imediatamente para evitar toxicidade fetal"
    ],
    correct: 0,
    explanation: "Em gestantes com Carga Viral de HIV >= 1.000 cópias/mL entre 34 e 36 semanas, a indicação formal é Cesariana Eletiva Programada na 38ª semana (com bolsa íntegra e antes do trabalho de parto) associada à infusão contínua de Zidovudina (AZT) endovenosa iniciada 3 horas antes da cirurgia."
  },
  {
    id: 14,
    stem: "Jovem de 20 anos apresenta úlcera única no pênis há 10 dias, medindo 1.2 cm, indolor, de bordas endurecidas e fundo limpo. Teste rápido treponêmico é reagente, porém o VDRL retorna Não Reagente. Qual a explicação e conduta correta?",
    options: [
      "Trata-se de falso-positivo do teste rápido; tranquilizar o paciente e não tratar",
      "O teste treponêmico positiva mais precocemente que os testes não treponêmicos na sífilis primária; o paciente tem cancro duro e deve receber Penicilina G Benzatina 2.4 milhões de UI IM",
      "Trata-se de cancro mole com reação cruzada; prescrever ciprofloxacino",
      "O resultado indica cicatriz sorológica de infecção no passado; não tratar",
      "O paciente apresenta fenômeno de prozona; deve-se diluir a amostra para confirmar sífilis terciária"
    ],
    correct: 1,
    explanation: "Na Sífilis Primária (Cancro Duro), os testes treponêmicos são os primeiros a positivar, enquanto o VDRL pode ser falso-negativo em até 20 a 30% das lesões iniciais por ainda não ter atingido títulos detectáveis. Diante de úlcera típica com teste treponêmico reagente, o diagnóstico é sífilis primária e trata-se imediatamente com Penicilina Benzatina."
  },
  {
    id: 15,
    stem: "Mulher de 19 anos tem NAAT positivo para Chlamydia trachomatis. Mantém relacionamento monogâmico há 4 meses com parceiro assintomático que tem dificuldade de acesso a consultas médicas. Em uma jurisdição com regulamentação de Expedited Partner Therapy (EPT), qual é a recomendação do CDC?",
    options: [
      "Tratar a paciente e fornecer prescrição/medicação de Doxiciclina 100 mg 12/12h por 7 dias em nome do parceiro sem consulta médica prévia presencial",
      "Tratar apenas a paciente e proibir qualquer comunicação ao parceiro para preservar sigilo",
      "Tratar a paciente e orientar o parceiro a realizar sorologia para clamídia antes de tomar antibióticos",
      "Internar a paciente para tratamento parenteral profilático",
      "Dispensar o tratamento do parceiro, uma vez que ele permanece assintomático"
    ],
    correct: 0,
    explanation: "A Expedited Partner Therapy (EPT) é uma estratégia de saúde pública endossada pelo CDC e ACOG que autoriza a prescrição/dispensação de antibióticos para o parceiro sexual do caso-índice sem a necessidade de avaliação médica presencial prévia do parceiro, quebrando a cadeia de transmissão e prevenindo reinfecção."
  }
];

function initQuiz() {
  const container = document.getElementById('quiz-container');
  const scoreDisplay = document.getElementById('quiz-score-display');
  const resetBtn = document.getElementById('quiz-reset-btn');

  if (!container) return;

  let userAnswers = {};

  function renderQuiz() {
    container.innerHTML = "";
    userAnswers = {};
    if (scoreDisplay) scoreDisplay.textContent = "Pontuação: 0 de 15 respondidas";

    QUIZ_DATA.forEach((q, idx) => {
      const qCard = document.createElement('div');
      qCard.className = "p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/80 shadow-sm space-y-3 transition-all";
      qCard.id = `quiz-card-${q.id}`;

      let optionsHTML = q.options.map((opt, optIdx) => `
        <button type="button" data-qid="${q.id}" data-opt="${optIdx}" 
          class="quiz-opt-btn w-full text-left p-3 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 text-xs sm:text-sm font-medium transition-all text-slate-800 dark:text-slate-200 flex items-start gap-2.5">
          <span class="w-5 h-5 rounded-full border border-slate-400 flex items-center justify-center text-xs font-bold shrink-0 mt-0.5">${String.fromCharCode(65 + optIdx)}</span>
          <span class="leading-relaxed">${opt}</span>
        </button>
      `).join('');

      qCard.innerHTML = `
        <div class="flex items-center justify-between gap-2">
          <span class="px-2.5 py-0.5 text-xs font-extrabold rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300">Questão ${idx + 1} de ${QUIZ_DATA.length}</span>
          <span class="text-xs font-semibold text-slate-400">USMLE Step 2 CK / Residência</span>
        </div>
        <p class="text-xs sm:text-sm text-slate-800 dark:text-slate-200 font-medium leading-relaxed">${q.stem}</p>
        <div class="space-y-2 pt-1" id="quiz-options-${q.id}">
          ${optionsHTML}
        </div>
        <div id="quiz-feedback-${q.id}" class="hidden p-3.5 rounded-xl text-xs sm:text-sm leading-relaxed mt-2 transition-all"></div>
      `;

      container.appendChild(qCard);
    });

    attachOptionListeners();
  }

  function attachOptionListeners() {
    document.querySelectorAll('.quiz-opt-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const qid = parseInt(btn.dataset.qid);
        const selected = parseInt(btn.dataset.opt);
        if (userAnswers[qid] !== undefined) return;

        userAnswers[qid] = selected;
        const qData = QUIZ_DATA.find(item => item.id === qid);
        const isCorrect = selected === qData.correct;

        const parentOptions = document.getElementById(`quiz-options-${qid}`);
        parentOptions.querySelectorAll('.quiz-opt-btn').forEach((b, idx) => {
          b.disabled = true;
          if (idx === qData.correct) {
            b.classList.add('border-emerald-500', 'bg-emerald-50', 'dark:bg-emerald-950/60', 'text-emerald-900', 'dark:text-emerald-200', 'font-bold');
            b.querySelector('span').classList.add('bg-emerald-600', 'text-white', 'border-emerald-600');
          } else if (idx === selected && !isCorrect) {
            b.classList.add('border-rose-500', 'bg-rose-50', 'dark:bg-rose-950/60', 'text-rose-900', 'dark:text-rose-200');
            b.querySelector('span').classList.add('bg-rose-600', 'text-white', 'border-rose-600');
          }
        });

        const fb = document.getElementById(`quiz-feedback-${qid}`);
        fb.classList.remove('hidden');
        if (isCorrect) {
          fb.className = "p-3.5 rounded-xl text-xs sm:text-sm leading-relaxed mt-2 bg-emerald-50 dark:bg-emerald-950/50 border border-emerald-300 dark:border-emerald-800 text-emerald-900 dark:text-emerald-200";
          fb.innerHTML = `<strong>Correto!</strong> ${qData.explanation}`;
        } else {
          fb.className = "p-3.5 rounded-xl text-xs sm:text-sm leading-relaxed mt-2 bg-rose-50 dark:bg-rose-950/50 border border-rose-300 dark:border-rose-800 text-rose-900 dark:text-rose-200";
          fb.innerHTML = `<strong>Incorreto.</strong> A alternativa correta é a letra <strong>${String.fromCharCode(65 + qData.correct)}</strong>.<br>${qData.explanation}`;
        }

        updateScore();
      });
    });
  }

  function updateScore() {
    let answered = Object.keys(userAnswers).length;
    let correctCount = 0;
    Object.keys(userAnswers).forEach(qid => {
      const q = QUIZ_DATA.find(x => x.id === parseInt(qid));
      if (q && userAnswers[qid] === q.correct) correctCount++;
    });

    if (scoreDisplay) {
      scoreDisplay.textContent = `Pontuação: ${correctCount} acertos de ${answered} respondidas (${Math.round((correctCount / (answered || 1)) * 100)}%)`;
    }
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', renderQuiz);
  }

  renderQuiz();
}

/* ==========================================================================
   16. HD LIGHTBOX MODAL (COM ZOOM E ARRASTAR)
   ========================================================================== */
function initLightbox() {
  const modal = document.getElementById('lightbox-modal');
  const img = document.getElementById('lightbox-img');
  const caption = document.getElementById('lightbox-caption');
  const closeBtn = document.getElementById('lightbox-close');
  const zoomInBtn = document.getElementById('lightbox-zoom-in');
  const zoomOutBtn = document.getElementById('lightbox-zoom-out');
  const resetBtn = document.getElementById('lightbox-reset');

  if (!modal || !img) return;

  let scale = 1;
  let isDragging = false;
  let startX = 0, startY = 0, translateX = 0, translateY = 0;

  function updateTransform() {
    img.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;
  }

  function openLightbox(src, alt) {
    img.src = src;
    caption.textContent = alt || "";
    scale = 1;
    translateX = 0;
    translateY = 0;
    updateTransform();
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('.zoomable-image').forEach(el => {
    el.addEventListener('click', () => {
      openLightbox(el.src, el.alt || el.getAttribute('title') || "");
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeLightbox();
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeLightbox();
    }
  });

  if (zoomInBtn) {
    zoomInBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      scale = Math.min(scale + 0.3, 3.5);
      updateTransform();
    });
  }

  if (zoomOutBtn) {
    zoomOutBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      scale = Math.max(scale - 0.3, 0.7);
      updateTransform();
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      scale = 1;
      translateX = 0;
      translateY = 0;
      updateTransform();
    });
  }

  // Arrastar com mouse
  img.addEventListener('mousedown', (e) => {
    if (scale <= 1) return;
    isDragging = true;
    startX = e.clientX - translateX;
    startY = e.clientY - translateY;
    e.preventDefault();
  });

  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    translateX = e.clientX - startX;
    translateY = e.clientY - startY;
    updateTransform();
  });

  window.addEventListener('mouseup', () => {
    isDragging = false;
  });
}
