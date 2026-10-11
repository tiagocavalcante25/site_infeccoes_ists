# -*- coding: utf-8 -*-
"""
scripts/update_responsiveness.py
Atualiza index.html do site_infeccoes_ists com:
1. Meta tags de viewport para iPhone/Android e PWA
2. Tailwind com unidades fluidas responsivas clamp()
3. Header fixo no topo da tela com tipografia adaptada para mobile
4. Remoção total do menu lateral redundante (mobile-menu-drawer)
5. 10 Imagens clínicas encapsuladas com img-fluid-container, fluid-img, max-width: 100% e dimensões proporcionais
6. Botão FAB voltar ao topo (fab-back-to-top)
"""

import os
import re

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_PATH = os.path.join(SITE_DIR, "index.html")

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. ATUALIZAR HEAD
head_old_pattern = r'<meta name="viewport" content="width=device-width, initial-scale=1\.0">.*?</script>\s*<!-- Tailwind CSS CDN -->'
head_new = """<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
  <title>Infecções Ginecológicas & ISTs | Portal Médico Interativo</title>
  <meta name="description" content="Guia Completo e Interativo de Infecções Ginecológicas e ISTs (Parte 6). USMLE Step 2 CK, Residência Médica, FEBRASGO, Ministério da Saúde / SUS, CDC, ACOG, ASCCP e INCA.">

  <!-- Configurações Mobile Web App para iOS e Android -->
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="apple-mobile-web-app-title" content="Infecções ISTs">
  <meta name="theme-color" content="#e11d48" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0f172a" media="(prefers-color-scheme: dark)">
  <meta name="format-detection" content="telephone=no">

  <!-- Previne Flash of Unstyled Content (FOUC) ao carregar tema escuro e tamanho de fonte -->
  <script>
    (function() {
      try {
        const saved = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (saved === 'dark' || (!saved && prefersDark)) {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }

        const savedFont = localStorage.getItem('fontSizePreference');
        if (savedFont) {
          document.documentElement.setAttribute('data-font-size', savedFont);
        }
      } catch (e) {}
    })();
  </script>

  <!-- Tailwind CSS CDN -->"""

html, n = re.subn(head_old_pattern, head_new, html, flags=re.DOTALL)
print(f"[HEAD METAS] Substituições: {n}")

# 2. ATUALIZAR TAILWIND CONFIG COM CLAMP() FLUIDO
tailwind_old = r'tailwind\.config = \{.*?\n  \}'
tailwind_new = """tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          screens: {
            'xs': '480px'
          },
          fontSize: {
            '9px': ['clamp(0.68rem, 0.64rem + 0.12vw, 0.74rem)', { lineHeight: '1.3' }],
            '10px': ['clamp(0.72rem, 0.68rem + 0.16vw, 0.8rem)', { lineHeight: '1.35' }],
            '11px': ['clamp(0.76rem, 0.71rem + 0.2vw, 0.86rem)', { lineHeight: '1.4' }],
            'xs': ['clamp(0.8rem, 0.75rem + 0.25vw, 0.9rem)', { lineHeight: '1.5' }],
            'sm': ['clamp(0.88rem, 0.82rem + 0.3vw, 0.98rem)', { lineHeight: '1.58' }],
            'base': ['clamp(0.96rem, 0.9rem + 0.4vw, 1.08rem)', { lineHeight: '1.65' }],
            'lg': ['clamp(1.06rem, 0.96rem + 0.6vw, 1.22rem)', { lineHeight: '1.55' }],
            'xl': ['clamp(1.16rem, 1.02rem + 0.8vw, 1.38rem)', { lineHeight: '1.45' }],
            '2xl': ['clamp(1.28rem, 1.12rem + 1.1vw, 1.65rem)', { lineHeight: '1.35' }],
            '3xl': ['clamp(1.42rem, 1.2rem + 1.6vw, 1.95rem)', { lineHeight: '1.25' }],
            '4xl': ['clamp(1.6rem, 1.32rem + 2.2vw, 2.35rem)', { lineHeight: '1.2' }],
            '5xl': ['clamp(1.8rem, 1.42rem + 2.8vw, 2.85rem)', { lineHeight: '1.15' }],
          },
          colors: {
            brand: {
              rose: '#e11d48',
              emerald: '#059669',
              amber: '#d97706',
              indigo: '#4f46e5',
              cyan: '#0891b2',
              purple: '#9333ea'
            }
          }
        }
      }
    }"""

html, n = re.subn(tailwind_old, tailwind_new, html, flags=re.DOTALL)
print(f"[TAILWIND FONTES FLUIDAS] Substituições: {n}")

# 3. REFAZER O HEADER FIXO E REMOVER O MENU LATERAL REDUNDANTE
nav_drawer_old_pattern = r'<!-- ======================================================================\s*HEADER / NAVBAR.*?<!-- ======================================================================\s*HERO BANNER'

nav_fixed_new = """<!-- ======================================================================
       HEADER / NAVBAR FIXO NO TOPO (POSITION: FIXED, 100% RESPONSIVO, SEM GAVETA REDUNDANTE)
       ====================================================================== -->
  <header class="fixed top-0 left-0 right-0 w-full z-50 glass-nav border-b border-slate-200/80 dark:border-slate-800/80 transition-colors">
    <!-- Nível 1: Barra Principal -->
    <div class="w-full max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-14 sm:h-16 gap-2 sm:gap-3">
        
        <!-- Logo e Título com Identidade Visual SUS / PCDT / FEBRASGO -->
        <a href="#" class="flex items-center gap-2 sm:gap-2.5 min-w-0 flex-shrink group" title="Infecções & ISTs - Início">
          <div class="w-8 h-8 sm:w-9 sm:h-9 rounded-xl bg-gradient-to-tr from-rose-600 via-pink-600 to-indigo-600 flex items-center justify-center text-white shadow-md shadow-rose-500/20 group-hover:scale-105 transition-transform flex-shrink-0">
            <i data-lucide="shield-alert" class="w-4 h-4"></i>
          </div>
          <div class="min-w-0">
            <div class="flex items-center gap-1.5">
              <span class="nav-brand-title font-extrabold text-xs sm:text-base tracking-tight text-slate-900 dark:text-white truncate">Infecções & ISTs</span>
              <span class="text-[9px] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 border border-rose-200 dark:border-rose-800 hidden xs:inline-block flex-shrink-0">PCDT / SUS</span>
            </div>
          </div>
        </a>

        <!-- Barra de Busca Global Inteligente (Desktop & Tablet) -->
        <div class="hidden md:flex items-center flex-1 max-w-sm lg:max-w-md mx-2 lg:mx-4">
          <div class="relative w-full">
            <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
            <input type="text" id="global-search" placeholder="Buscar módulos, condutas (Amsel, EPT, Hager, HPV...)" 
              class="w-full pl-9 pr-14 py-2 text-xs rounded-xl bg-slate-100/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 focus:outline-none focus:ring-2 focus:ring-rose-500 text-slate-800 dark:text-slate-200 placeholder-slate-400 transition-all">
            <kbd class="hidden lg:inline-flex items-center absolute right-2.5 top-1/2 -translate-y-1/2 px-1.5 py-0.5 text-[10px] font-semibold text-slate-400 dark:text-slate-500 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded shadow-sm">Ctrl K</kbd>
          </div>
        </div>

        <!-- Ações Rápidas: Motores, Cards, Simulado, Font Size e Tema (Adaptados para Mobile) -->
        <div class="flex items-center gap-1 sm:gap-2 flex-shrink-0">
          
          <!-- Hubs de Treinamento Rápido -->
          <nav class="flex items-center gap-1 sm:gap-1.5">
            <a href="#ferramentas-clinicas" class="nav-pill-btn inline-flex items-center gap-1 px-2 py-1 sm:px-2.5 sm:py-1.5 rounded-lg font-bold text-rose-700 dark:text-rose-300 bg-rose-50 hover:bg-rose-100 dark:bg-rose-950/40 dark:hover:bg-rose-900/40 border border-rose-200/80 dark:border-rose-800/60 transition-colors" title="Motores Clínicos Interativos">
              <i data-lucide="calculator" class="w-3.5 h-3.5 text-rose-500"></i>
              <span class="hidden sm:inline">Motores</span>
            </a>
            <a href="#estudo-ativo" class="nav-pill-btn inline-flex items-center gap-1 px-2 py-1 sm:px-2.5 sm:py-1.5 rounded-lg font-bold text-indigo-700 dark:text-indigo-300 bg-indigo-50 hover:bg-indigo-100 dark:bg-indigo-950/40 dark:hover:bg-indigo-900/40 border border-indigo-200/80 dark:border-indigo-800/60 transition-colors" title="Flashcards 3D">
              <i data-lucide="layers" class="w-3.5 h-3.5 text-indigo-500"></i>
              <span class="hidden sm:inline">Cards</span>
            </a>
            <a href="#simulado-clinico" class="nav-pill-btn inline-flex items-center gap-1 px-2 py-1 sm:px-2.5 sm:py-1.5 rounded-lg font-bold text-emerald-700 dark:text-emerald-300 bg-emerald-50 hover:bg-emerald-100 dark:bg-emerald-950/40 dark:hover:bg-emerald-900/40 border border-emerald-200/80 dark:border-emerald-800/60 transition-colors" title="Simulado USMLE / PCDT">
              <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i>
              <span class="hidden sm:inline">Simulado</span>
            </a>
          </nav>

          <!-- Controle de Tamanho da Fonte (A / A+ / A++) Direto na Barra Fixa -->
          <div class="inline-flex items-center bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg p-0.5" title="Ajustar tamanho da fonte para leitura confortável">
            <button type="button" data-font-size-set="normal" aria-label="Tamanho de fonte normal" title="Fonte padrão" class="font-size-btn px-1.5 py-0.5 font-bold rounded transition-colors">A</button>
            <button type="button" data-font-size-set="large" aria-label="Tamanho de fonte grande" title="Fonte ampliada" class="font-size-btn px-1.5 py-0.5 font-bold rounded transition-colors">A+</button>
            <button type="button" data-font-size-set="xlarge" aria-label="Tamanho de fonte máximo" title="Fonte máxima" class="font-size-btn px-1.5 py-0.5 font-black rounded transition-colors">A++</button>
          </div>

          <!-- Botão de Alternância de Tema Claro/Escuro -->
          <button id="theme-toggle" type="button" aria-label="Alternar modo claro/escuro" title="Alternar modo claro/escuro" 
            class="theme-toggle-btn p-1.5 sm:p-2 rounded-xl text-slate-600 hover:text-slate-900 dark:text-slate-300 dark:hover:text-white bg-slate-100 hover:bg-slate-200 dark:bg-slate-900 hover:dark:bg-slate-800 border border-slate-200 dark:border-slate-800 transition-colors flex items-center justify-center focus:outline-none focus:ring-2 focus:ring-rose-500">
            <i data-lucide="sun" class="w-3.5 h-3.5 sm:w-4 sm:h-4 icon-sun text-amber-500"></i>
            <i data-lucide="moon" class="w-3.5 h-3.5 sm:w-4 sm:h-4 icon-moon text-slate-700 dark:text-slate-300"></i>
          </button>

        </div>

      </div>
    </div>

    <!-- Nível 2: Faixa Subnav Contínua de Módulos Clínicos & Ferramentas Rápidas (Acesso Direto em Celulares, Tablets e Desktops) -->
    <div class="w-full border-t border-slate-200/70 dark:border-slate-800/70 bg-slate-50/80 dark:bg-slate-950/80 backdrop-blur-md">
      <div class="w-full max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
        <div class="flex items-center gap-1 sm:gap-1.5 overflow-x-auto no-scrollbar py-1.5 text-xs font-semibold whitespace-nowrap">
          <span class="text-[10px] uppercase font-bold text-slate-400 dark:text-slate-500 mr-0.5 flex items-center gap-1 flex-shrink-0">
            <i data-lucide="layers" class="w-3 h-3 text-rose-500"></i> Módulos:
          </span>
          <a href="#modulo-50" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">50</span>
            Fresco
          </a>
          <a href="#modulo-51" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-pink-100 dark:bg-pink-950 text-pink-700 dark:text-pink-300 text-[10px] font-bold flex items-center justify-center">51</span>
            Vulvovaginites
          </a>
          <a href="#modulo-52" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-amber-100 dark:bg-amber-950 text-amber-700 dark:text-amber-300 text-[10px] font-bold flex items-center justify-center">52</span>
            Cervicites
          </a>
          <a href="#modulo-53" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">53</span>
            DIP & ATO
          </a>
          <a href="#modulo-54" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-purple-100 dark:bg-purple-950 text-purple-700 dark:text-purple-300 text-[10px] font-bold flex items-center justify-center">54</span>
            Fitz-Hugh-Curtis
          </a>
          <a href="#modulo-55" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-indigo-100 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300 text-[10px] font-bold flex items-center justify-center">55</span>
            Sífilis
          </a>
          <a href="#modulo-56" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">56</span>
            Úlceras
          </a>
          <a href="#modulo-57" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-cyan-100 dark:bg-cyan-950 text-cyan-700 dark:text-cyan-300 text-[10px] font-bold flex items-center justify-center">57</span>
            Herpes
          </a>
          <a href="#modulo-58" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 text-[10px] font-bold flex items-center justify-center">58</span>
            HPV & Bethesda
          </a>
          <a href="#modulo-59" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-red-100 dark:bg-red-950 text-red-700 dark:text-red-300 text-[10px] font-bold flex items-center justify-center">59</span>
            HIV & PEP
          </a>
          <a href="#modulo-60" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-[10px] font-bold flex items-center justify-center">60</span>
            Matriz & Casos
          </a>

          <!-- Separador -->
          <span class="h-3.5 w-px bg-slate-300 dark:bg-slate-700 mx-1 flex-shrink-0"></span>

          <!-- Ferramentas Clínicas Diretas -->
          <span class="text-[10px] uppercase font-bold text-slate-400 dark:text-slate-500 mr-0.5 flex items-center gap-1 flex-shrink-0">
            <i data-lucide="zap" class="w-3 h-3 text-amber-500"></i> Motores:
          </span>
          <a href="#ferramentas-clinicas" class="subnav-pill px-2 py-0.5 rounded-md text-rose-700 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/40 transition-colors flex items-center gap-1 flex-shrink-0">
            <i data-lucide="calculator" class="w-3 h-3"></i>
            Amsel / Nugent
          </a>
          <a href="#ferramentas-clinicas" class="subnav-pill px-2 py-0.5 rounded-md text-amber-700 dark:text-amber-400 hover:bg-amber-50 dark:hover:bg-amber-950/40 transition-colors flex items-center gap-1 flex-shrink-0">
            <i data-lucide="shield" class="w-3 h-3"></i>
            EPT Dose
          </a>
          <a href="#ferramentas-clinicas" class="subnav-pill px-2 py-0.5 rounded-md text-indigo-700 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-950/40 transition-colors flex items-center gap-1 flex-shrink-0">
            <i data-lucide="activity" class="w-3 h-3"></i>
            Hager DIP
          </a>
          <a href="#ferramentas-clinicas" class="subnav-pill px-2 py-0.5 rounded-md text-emerald-700 dark:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-950/40 transition-colors flex items-center gap-1 flex-shrink-0">
            <i data-lucide="file-check-2" class="w-3 h-3"></i>
            Bethesda
          </a>
          <a href="#ferramentas-clinicas" class="subnav-pill px-2 py-0.5 rounded-md text-purple-700 dark:text-purple-400 hover:bg-purple-50 dark:hover:bg-purple-950/40 transition-colors flex items-center gap-1 flex-shrink-0">
            <i data-lucide="heart-pulse" class="w-3 h-3"></i>
            HIV / PEP
          </a>
        </div>
      </div>
    </div>

    <!-- Barra de Progresso de Leitura Contínua -->
    <div id="reading-progress" class="h-1 bg-gradient-to-r from-rose-500 via-pink-500 to-indigo-500 w-0 transition-all duration-150 ease-out" role="progressbar" aria-label="Progresso de leitura"></div>
  </header>

  <!-- ======================================================================
       HERO BANNER"""

html, n = re.subn(nav_drawer_old_pattern, nav_fixed_new, html, flags=re.DOTALL)
print(f"[NAV & DRAWER REMOVAL] Substituições: {n}")

# 4. ATUALIZAR AS 10 IMAGENS CLÍNICAS
image_specs = [
    ("ecossistema_vaginal_exame_a_fresco.jpg", 1350, 900),
    ("vulvovaginites_matriz_comparativa.jpg", 1400, 900),
    ("cervicites_gonococo_clamidia_ept.jpg", 1350, 900),
    ("dip_fisiopatologia_hager_ato.jpg", 1350, 900),
    ("sindrome_fitz_hugh_curtis_sequelas.jpg", 1300, 880),
    ("sifilis_estadiamento_sorologia_gestacao.jpg", 1400, 900),
    ("ulceras_genitais_matriz_diferencial.jpg", 1400, 900),
    ("herpes_genital_profilaxia_parto.jpg", 1300, 880),
    ("hpv_oncogenese_rastreamento_bethesda.jpg", 1400, 900),
    ("hiv_prevencao_transmissao_vertical_pep.jpg", 1350, 900)
]

for img_name, w, h in image_specs:
    # Atualizar o contêiner para ter img-fluid-container
    container_pattern = rf'<div class="relative group rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md bg-slate-900">\s*<img src="assets/img/{img_name}"([^>]+)>'
    
    def replacer(match, name=img_name, width=w, height=h):
        rest = match.group(1)
        # Extrair alt
        alt_match = re.search(r'alt=["\']([^"\']+)["\']', rest)
        alt = alt_match.group(1) if alt_match else name
        return f'<div class="img-fluid-container relative group rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md bg-slate-900">\n            <img src="assets/img/{name}" alt="{alt}" width="{width}" height="{height}" class="zoomable-image fluid-img w-full max-w-full h-auto object-cover cursor-zoom-in transition-transform duration-300 group-hover:scale-[1.02]">'
    
    html, n = re.subn(container_pattern, replacer, html)
    print(f"[IMAGEM FLUIDA] {img_name}: {n}")

# 5. ADICIONAR BOTÃO FLUTUANTE (FAB) VOLTAR AO TOPO SE NÃO ESTIVER PRESENTE
if 'id="fab-back-to-top"' not in html:
    fab_html = """
  <!-- Botão Flutuante Voltar ao Topo (FAB) -->
  <button id="fab-back-to-top" type="button" aria-label="Voltar ao topo da página" title="Voltar ao topo" class="fab-hidden p-3 rounded-full bg-rose-600 hover:bg-rose-700 text-white shadow-xl shadow-rose-600/30 flex items-center justify-center focus:outline-none focus:ring-4 focus:ring-rose-500/30">
    <i data-lucide="arrow-up" class="w-5 h-5"></i>
  </button>
</body>"""
    html = html.replace('</body>', fab_html)
    print("[FAB ADICIONADO]")

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print(">>> ATUALIZAÇÃO DO index.html CONCLUÍDA COM SUCESSO! <<<")
