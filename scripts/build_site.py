# -*- coding: utf-8 -*-
"""
build_site.py - Gerador do Portal Interativo de Infecções Ginecológicas e ISTs (Parte 6)
Compatível com GitHub Pages e alinhado aos padrões USMLE Step 2 CK, PCDT/SUS, CDC 2021/2024, ACOG, ASCCP e INCA.
"""

import os
import sys

OUTPUT_FILE = "index.html"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Infecções Ginecológicas & ISTs | Portal Médico Interativo</title>
  <meta name="description" content="Guia Completo e Interativo de Infecções Ginecológicas e ISTs (Parte 6). USMLE Step 2 CK, Residência Médica, FEBRASGO, Ministério da Saúde / SUS, CDC, ACOG, ASCCP e INCA.">

  <!-- Previne Flash of Unstyled Content (FOUC) ao carregar tema escuro -->
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
      } catch (e) {}
    })();
  </script>

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          screens: {
            'xs': '480px'
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
    }
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Custom CSS -->
  <link rel="stylesheet" href="assets/css/custom.css">
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-slate-100 min-h-screen flex flex-col antialiased transition-colors duration-200">

  <!-- ======================================================================
       HEADER / NAVBAR MULTI-NÍVEL RESPONSIVO & ELEGANTE
       ====================================================================== -->
  <header class="sticky top-0 z-40 glass-nav border-b border-slate-200/80 dark:border-slate-800/80 transition-colors">
    <!-- Nível 1: Barra Principal -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 gap-3 lg:gap-4">
        
        <!-- Logo e Título com Identidade Visual SUS / FEBRASGO / CDC / ACOG -->
        <a href="#" class="flex items-center gap-3 flex-shrink-0 group" title="Ir para o início">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-rose-600 via-pink-600 to-indigo-600 flex items-center justify-center text-white shadow-md shadow-rose-500/20 group-hover:scale-105 transition-transform flex-shrink-0">
            <i data-lucide="shield-alert" class="w-5 h-5"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="font-extrabold text-sm sm:text-base tracking-tight text-slate-900 dark:text-white">Infecções & ISTs</span>
              <span class="text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 border border-rose-200 dark:border-rose-800 hidden xs:inline-block">PCDT / SUS</span>
            </div>
            <span class="text-[11px] text-slate-500 dark:text-slate-400 font-medium hidden sm:block">USMLE Step 2 CK • Residência Médica • CDC • FEBRASGO • ASCCP</span>
          </div>
        </a>

        <!-- Barra de Busca Global Inteligente (Desktop & Tablet) -->
        <div class="hidden md:flex items-center flex-1 max-w-sm lg:max-w-md mx-2 lg:mx-4">
          <div class="relative w-full">
            <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
            <input type="text" id="global-search" placeholder="Buscar módulos, condutas (ex: Amsel, Penicilina, EPT, Hager, HPV, PEP...)" 
              class="w-full pl-9 pr-14 py-2 text-xs rounded-xl bg-slate-100/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 focus:outline-none focus:ring-2 focus:ring-rose-500 text-slate-800 dark:text-slate-200 placeholder-slate-400 transition-all">
            <kbd class="hidden lg:inline-flex items-center absolute right-2.5 top-1/2 -translate-y-1/2 px-1.5 py-0.5 text-[10px] font-semibold text-slate-400 dark:text-slate-500 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded shadow-sm">Ctrl K</kbd>
          </div>
        </div>

        <!-- Ações Rápidas de Estudo, Botão de Tema e Menu Mobile -->
        <div class="flex items-center gap-1.5 sm:gap-2">
          <!-- Atalho Calculadoras -->
          <a href="#ferramentas-clinicas" class="hidden xl:inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold rounded-lg text-rose-700 dark:text-rose-300 bg-rose-50 dark:bg-rose-950/60 border border-rose-200 dark:border-rose-800 hover:bg-rose-100 transition-colors">
            <i data-lucide="calculator" class="w-3.5 h-3.5"></i>
            <span>Motores Clínicos</span>
          </a>

          <!-- Atalho Flashcards -->
          <a href="#estudo-ativo" class="hidden xl:inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold rounded-lg text-indigo-700 dark:text-indigo-300 bg-indigo-50 dark:bg-indigo-950/60 border border-indigo-200 dark:border-indigo-800 hover:bg-indigo-100 transition-colors">
            <i data-lucide="layers" class="w-3.5 h-3.5"></i>
            <span>Flashcards</span>
          </a>

          <!-- Atalho Simulado -->
          <a href="#simulado-clinico" class="hidden xl:inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold rounded-lg text-emerald-700 dark:text-emerald-300 bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-200 dark:border-emerald-800 hover:bg-emerald-100 transition-colors">
            <i data-lucide="check-circle-2" class="w-3.5 h-3.5"></i>
            <span>Simulado (15Q)</span>
          </a>

          <!-- Botão Modo Claro / Escuro -->
          <button type="button" id="theme-toggle" class="p-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors border border-transparent hover:border-slate-200 dark:hover:border-slate-700 theme-toggle-btn" title="Alternar tema">
            <i data-lucide="moon" class="w-4 h-4 icon-moon"></i>
            <i data-lucide="sun" class="w-4 h-4 icon-sun"></i>
          </button>

          <!-- Botão Menu Mobile -->
          <button type="button" id="mobile-menu-toggle" class="p-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors border border-transparent md:hidden" aria-label="Abrir menu" aria-expanded="false">
            <i data-lucide="menu" id="mobile-menu-icon" class="w-5 h-5"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- Nível 2: Faixa de Navegação Rápida entre Módulos (Subnav Ribbon) -->
    <div class="border-t border-slate-200/60 dark:border-slate-800/60 bg-slate-50/70 dark:bg-slate-900/70 overflow-x-auto no-scrollbar">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <nav class="flex items-center gap-1 py-1.5 text-xs font-semibold whitespace-nowrap min-w-max">
          <a href="#modulo-50" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M50: Ecossistema & Fresco</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-51" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M51: Vulvovaginites</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-52" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M52: Cervicites & EPT</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-53" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M53: DIP & ATO</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-54" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M54: Fitz-Hugh-Curtis</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-55" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M55: Sífilis & Gestação</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-56" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M56: Úlceras Genitais</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-57" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M57: Herpes & Parto</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-58" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M58: HPV & Bethesda</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-59" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M59: HIV & Transmissão Vertical</a>
          <span class="text-slate-300 dark:text-slate-700">•</span>
          <a href="#modulo-60" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-300 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-slate-200/60 dark:hover:bg-slate-800 transition-colors">M60: Matriz & Casos</a>
        </nav>
      </div>
    </div>
  </header>

  <!-- Gaveta de Menu Mobile -->
  <div id="mobile-menu-drawer" class="hidden fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-sm md:hidden">
    <div class="fixed inset-y-0 right-0 w-full max-w-xs bg-white dark:bg-slate-900 p-6 shadow-2xl flex flex-col justify-between overflow-y-auto">
      <div class="space-y-6">
        <div class="flex items-center justify-between pb-4 border-b border-slate-200 dark:border-slate-800">
          <span class="font-extrabold text-base text-slate-900 dark:text-white">Navegação Rápida</span>
          <button type="button" id="mobile-theme-toggle" class="p-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 theme-toggle-btn">
            <i data-lucide="moon" class="w-4 h-4 icon-moon"></i>
            <i data-lucide="sun" class="w-4 h-4 icon-sun"></i>
          </button>
        </div>

        <!-- Busca Mobile -->
        <div class="relative">
          <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
          <input type="text" id="mobile-search" placeholder="Buscar módulos ou condutas..." 
            class="w-full pl-9 pr-3 py-2 text-xs rounded-xl bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200">
        </div>

        <nav class="space-y-1 text-sm font-semibold">
          <a href="#ferramentas-clinicas" class="flex items-center gap-2.5 px-3 py-2 rounded-lg text-rose-600 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/40">
            <i data-lucide="calculator" class="w-4 h-4"></i>
            <span>Motores Clínicos Interativos</span>
          </a>
          <a href="#estudo-ativo" class="flex items-center gap-2.5 px-3 py-2 rounded-lg text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-950/40">
            <i data-lucide="layers" class="w-4 h-4"></i>
            <span>Flashcards 3D (15 Cards)</span>
          </a>
          <a href="#simulado-clinico" class="flex items-center gap-2.5 px-3 py-2 rounded-lg text-emerald-600 dark:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-950/40">
            <i data-lucide="check-circle-2" class="w-4 h-4"></i>
            <span>Simulado USMLE (15 Casos)</span>
          </a>

          <div class="pt-3 pb-1 border-t border-slate-200 dark:border-slate-800 text-[11px] font-bold uppercase tracking-wider text-slate-400">Módulos Clínicos</div>
          <a href="#modulo-50" class="block px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">M50: Ecossistema Vaginal & Fresco</a>
          <a href="#modulo-51" class="block px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">M51: Grandes Vulvovaginites</a>
          <a href="#modulo-52" class="block px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">M52: Cervicites Infecciosas & EPT</a>
          <a href="#modulo-53" class="block px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">M53: DIP & Abscesso Tubo-Ovariano</a>
          <a href="#modulo-54" class="block px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">M54: Síndrome de Fitz-Hugh-Curtis</a>
          <a href="#modulo-55" class="block px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">M55: Sífilis Adquirida & Gestação</a>
          <a href="#modulo-56" class="block px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">M56: Matriz de Úlceras Genitais</a>
          <a href="#modulo-57" class="block px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">M57: Herpes Genital na Gestação</a>
          <a href="#modulo-58" class="block px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">M58: HPV, Oncogênese & Bethesda</a>
          <a href="#modulo-59" class="block px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">M59: HIV & Transmissão Vertical</a>
          <a href="#modulo-60" class="block px-3 py-1.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800">M60: OSCE, Revisão & Simulado</a>
        </nav>
      </div>

      <div class="pt-6 border-t border-slate-200 dark:border-slate-800 text-xs text-slate-500">
        PCDT / SUS • CDC 2021 • FEBRASGO
      </div>
    </div>
  </div>

  <!-- ======================================================================
       HERO BANNER & DESTAQUES CLÍNICOS
       ====================================================================== -->
  <section class="relative overflow-hidden bg-gradient-to-b from-rose-500/10 via-slate-50 dark:via-slate-950 to-slate-50 dark:to-slate-950 py-12 md:py-16 border-b border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl space-y-4">
        
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-100 dark:bg-rose-950/80 text-rose-700 dark:text-rose-300 border border-rose-200 dark:border-rose-800 text-xs font-bold">
          <i data-lucide="shield-check" class="w-3.5 h-3.5"></i>
          <span>Guia Oficial de Infecções Ginecológicas e ISTs (Parte 6)</span>
        </div>

        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-slate-900 dark:text-white leading-tight">
          Infecções Ginecológicas & <span class="bg-gradient-to-r from-rose-600 via-pink-600 to-indigo-600 bg-clip-text text-transparent">ISTs de Alta Precisão</span>
        </h1>

        <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed font-normal">
          Abordagem sindrômica e etiológica de ponta do internato à residência médica e USMLE Step 2 CK. Integração de biologia molecular (NAAT), diretrizes do PCDT/SUS, CDC 2021/2024, ACOG, ASCCP e INCA para prevenção da transmissão vertical materna, oncogênese cervical e stewardship de antimicrobianos.
        </p>

        <!-- Grade de Estatísticas Rápidas -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-4">
          <div class="p-3.5 rounded-xl bg-white/70 dark:bg-slate-900/70 border border-slate-200/80 dark:border-slate-800/80 shadow-sm">
            <div class="text-2xl font-black text-rose-600 dark:text-rose-400">11</div>
            <div class="text-xs font-bold text-slate-600 dark:text-slate-300">Módulos Especializados</div>
            <div class="text-[10px] text-slate-400">M50 ao M60 Completos</div>
          </div>
          <div class="p-3.5 rounded-xl bg-white/70 dark:bg-slate-900/70 border border-slate-200/80 dark:border-slate-800/80 shadow-sm">
            <div class="text-2xl font-black text-indigo-600 dark:text-indigo-400">10</div>
            <div class="text-xs font-bold text-slate-600 dark:text-slate-300">Motores Interativos</div>
            <div class="text-[10px] text-slate-400">Calculadoras Clínicas</div>
          </div>
          <div class="p-3.5 rounded-xl bg-white/70 dark:bg-slate-900/70 border border-slate-200/80 dark:border-slate-800/80 shadow-sm">
            <div class="text-2xl font-black text-amber-600 dark:text-amber-400">10</div>
            <div class="text-xs font-bold text-slate-600 dark:text-slate-300">Infográficos HD</div>
            <div class="text-[10px] text-slate-400">Visualizador com Zoom</div>
          </div>
          <div class="p-3.5 rounded-xl bg-white/70 dark:bg-slate-900/70 border border-slate-200/80 dark:border-slate-800/80 shadow-sm">
            <div class="text-2xl font-black text-emerald-600 dark:text-emerald-400">15</div>
            <div class="text-xs font-bold text-slate-600 dark:text-slate-300">Casos USMLE & Cards</div>
            <div class="text-[10px] text-slate-400">Gabarito em Tempo Real</div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- Mensagem de Sem Resultados na Busca -->
  <div id="search-no-results" class="hidden max-w-7xl mx-auto px-4 py-8 text-center">
    <div class="p-6 rounded-2xl bg-amber-50 dark:bg-amber-950/50 border border-amber-200 dark:border-amber-800 max-w-md mx-auto">
      <i data-lucide="search-x" class="w-8 h-8 mx-auto text-amber-600 mb-2"></i>
      <h3 class="font-bold text-sm text-amber-900 dark:text-amber-200">Nenhum módulo encontrado</h3>
      <p class="text-xs text-amber-700 dark:text-amber-300 mt-1">Tente buscar por "Amsel", "Nugent", "Ceftriaxona", "Sífilis", "Herpes" ou "HPV".</p>
    </div>
  </div>

  <!-- ======================================================================
       SEÇÃO: MOTORES CLÍNICOS E CALCULADORAS INTERATIVAS
       ====================================================================== -->
  <section id="ferramentas-clinicas" class="py-12 bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-md bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 text-xs font-bold uppercase tracking-wider mb-2">
            Tomada de Decisão Beira-Leito
          </div>
          <h2 class="text-2xl sm:text-3xl font-black tracking-tight text-slate-900 dark:text-white">
            Motores Clínicos & Calculadoras de ISTs
          </h2>
          <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1">
            Algoritmos validados conforme CDC 2021/2024, PCDT/MS e diretrizes ASCCP/INCA.
          </p>
        </div>
      </div>

      <!-- Grade dos 10 Motores Clínicos -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

        <!-- 1. Simulador de Exame a Fresco -->
        <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-800/50 space-y-4 shadow-sm flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-rose-600 dark:text-rose-400 font-bold text-sm">
              <i data-lucide="microscope" class="w-4 h-4"></i>
              <span>1. Simulador de Exame a Fresco</span>
            </div>
            <div class="space-y-2 text-xs">
              <div>
                <label class="font-semibold block mb-1">pH Vaginal (Fita de pH):</label>
                <select id="sim-ph" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 font-medium">
                  <option value="normal">pH Normal / Ácido (≤ 4.5)</option>
                  <option value="elevado">pH Elevado / Básico (&gt; 4.5)</option>
                </select>
              </div>
              <div>
                <label class="font-semibold block mb-1">Microscopia Óptica (Salina / KOH):</label>
                <select id="sim-micro" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 font-medium">
                  <option value="lacto">Lactobacilos e Células Epiteliais Limpas</option>
                  <option value="clue">Clue Cells (&gt; 20% das células)</option>
                  <option value="hyphae">Hifas, Pseudo-hifas e Blastoconídios</option>
                  <option value="tricho">Protozoários Flagelados Móveis</option>
                  <option value="parabasal">Células Parabasais (Ausência de Flora)</option>
                </select>
              </div>
              <div class="flex items-center gap-2 pt-1">
                <input type="checkbox" id="sim-whiff" class="rounded border-slate-300 text-rose-600 focus:ring-rose-500 w-4 h-4">
                <label for="sim-whiff" class="font-medium">Whiff Test Positivo (KOH 10% libera odor fétido)</label>
              </div>
            </div>
          </div>
          <div id="sim-result" class="pt-2"></div>
        </div>

        <!-- 2. Critérios de Amsel (VB) -->
        <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-800/50 space-y-4 shadow-sm flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-amber-600 dark:text-amber-400 font-bold text-sm">
              <i data-lucide="check-square" class="w-4 h-4"></i>
              <span>2. Critérios de Amsel (Vaginose Bacteriana)</span>
            </div>
            <p class="text-[11px] text-slate-500">Exige pelo menos 3 de 4 critérios clínicos para fechar diagnóstico:</p>
            <div class="space-y-2 text-xs">
              <label class="flex items-center gap-2 p-1.5 rounded hover:bg-slate-200/50 dark:hover:bg-slate-700/50 cursor-pointer">
                <input type="checkbox" id="amsel-discharge" class="rounded border-slate-300 text-amber-600 w-4 h-4">
                <span>1. Corrimento fino, homogêneo, acinzentado</span>
              </label>
              <label class="flex items-center gap-2 p-1.5 rounded hover:bg-slate-200/50 dark:hover:bg-slate-700/50 cursor-pointer">
                <input type="checkbox" id="amsel-ph" class="rounded border-slate-300 text-amber-600 w-4 h-4">
                <span>2. pH Vaginal &gt; 4.5</span>
              </label>
              <label class="flex items-center gap-2 p-1.5 rounded hover:bg-slate-200/50 dark:hover:bg-slate-700/50 cursor-pointer">
                <input type="checkbox" id="amsel-whiff" class="rounded border-slate-300 text-amber-600 w-4 h-4">
                <span>3. Whiff test positivo (odor de peixe com KOH)</span>
              </label>
              <label class="flex items-center gap-2 p-1.5 rounded hover:bg-slate-200/50 dark:hover:bg-slate-700/50 cursor-pointer">
                <input type="checkbox" id="amsel-clue" class="rounded border-slate-300 text-amber-600 w-4 h-4">
                <span>4. Clue cells presentes (&ge; 20% no fresco)</span>
              </label>
            </div>
          </div>
          <div id="amsel-result" class="pt-2"></div>
        </div>

        <!-- 3. Estratificador de Candidíase -->
        <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-800/50 space-y-4 shadow-sm flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-rose-600 dark:text-rose-400 font-bold text-sm">
              <i data-lucide="sparkles" class="w-4 h-4"></i>
              <span>3. Estratificador de Candidíase (CVV)</span>
            </div>
            <div class="space-y-2 text-xs">
              <div>
                <label class="font-semibold block mb-1">Apresentação Clínica:</label>
                <select id="candida-type" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 font-medium">
                  <option value="sporadic">Episódio Esporádico Não Complicado</option>
                  <option value="recurrent">Candidíase Recorrente (&ge; 4 episódios/ano)</option>
                </select>
              </div>
              <div class="space-y-2 pt-1">
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="candida-preg" class="rounded border-slate-300 text-rose-600 w-4 h-4">
                  <span class="font-semibold text-rose-600 dark:text-rose-400">Paciente Gestante? (Regra Crítica!)</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="candida-glabrata" class="rounded border-slate-300 text-purple-600 w-4 h-4">
                  <span>Isolada espécie não-albicans (*C. glabrata*)?</span>
                </label>
              </div>
            </div>
          </div>
          <div id="candida-result" class="pt-2"></div>
        </div>

        <!-- 4. Calculadora de Cervicite & EPT -->
        <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-800/50 space-y-4 shadow-sm flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-indigo-600 dark:text-indigo-400 font-bold text-sm">
              <i data-lucide="pill" class="w-4 h-4"></i>
              <span>4. Cervicites, Ajuste de Dose & EPT</span>
            </div>
            <div class="space-y-2 text-xs">
              <div>
                <label class="font-semibold block mb-1">Peso da Paciente (kg):</label>
                <input type="number" id="cerv-weight" value="65" min="30" max="250" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 font-medium">
                <span class="text-[10px] text-slate-400">Atenção ao limiar de ≥ 150 kg para Ceftriaxona</span>
              </div>
              <div class="pt-1">
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="cerv-preg" class="rounded border-slate-300 text-indigo-600 w-4 h-4">
                  <span class="font-semibold">Paciente Gestante (Muda esquema de Clamídia)</span>
                </label>
              </div>
            </div>
          </div>
          <div id="cerv-result" class="pt-2"></div>
        </div>

        <!-- 5. Escore de Internação em DIP (Hager) -->
        <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-800/50 space-y-4 shadow-sm flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-rose-600 dark:text-rose-400 font-bold text-sm">
              <i data-lucide="hospital" class="w-4 h-4"></i>
              <span>5. Escore de Internação em DIP (CDC)</span>
            </div>
            <p class="text-[11px] text-slate-500">Selecione quaisquer critérios de gravidade presentes:</p>
            <div class="space-y-1.5 text-xs">
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="checkbox" class="pid-crit rounded border-slate-300 text-rose-600 w-4 h-4">
                <span>Abscesso Tubo-Ovariano (ATO) diagnosticado</span>
              </label>
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="checkbox" class="pid-crit rounded border-slate-300 text-rose-600 w-4 h-4">
                <span>Paciente Gestante</span>
              </label>
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="checkbox" class="pid-crit rounded border-slate-300 text-rose-600 w-4 h-4">
                <span>Emergência cirúrgica não descartada (ex: Apendicite)</span>
              </label>
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="checkbox" class="pid-crit rounded border-slate-300 text-rose-600 w-4 h-4">
                <span>Náuseas/vômitos intensos ou peritonite generalizada</span>
              </label>
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="checkbox" class="pid-crit rounded border-slate-300 text-rose-600 w-4 h-4">
                <span>Falha terapêutica oral após 48 a 72 horas</span>
              </label>
            </div>
          </div>
          <div id="pid-result" class="pt-2"></div>
        </div>

        <!-- 6. Sífilis & Dessensibilização -->
        <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-800/50 space-y-4 shadow-sm flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-emerald-600 dark:text-emerald-400 font-bold text-sm">
              <i data-lucide="shield" class="w-4 h-4"></i>
              <span>6. Sífilis & Dessensibilização Gestacional</span>
            </div>
            <div class="space-y-2 text-xs">
              <div>
                <label class="font-semibold block mb-1">Estágio Clínico da Sífilis:</label>
                <select id="syph-stage" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 font-medium">
                  <option value="early">Primária, Secundária ou Latente Precoce (&lt; 1 ano)</option>
                  <option value="late">Latente Tardia (&gt; 1 ano) ou Duração Indeterminada</option>
                  <option value="neuro">Neurossífilis ou Sífilis Ocular/Ótica</option>
                </select>
              </div>
              <div class="space-y-1.5 pt-1">
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="syph-preg" class="rounded border-slate-300 text-rose-600 w-4 h-4">
                  <span class="font-bold text-rose-600 dark:text-rose-400">Paciente Gestante?</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="syph-allergy" class="rounded border-slate-300 text-rose-600 w-4 h-4">
                  <span class="font-bold text-rose-600 dark:text-rose-400">Histórico de Anafilaxia / Alergia Grave à Penicilina?</span>
                </label>
              </div>
            </div>
          </div>
          <div id="syph-result" class="pt-2"></div>
        </div>

        <!-- 7. Matriz de Úlceras Genitais -->
        <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-800/50 space-y-4 shadow-sm flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-rose-600 dark:text-rose-400 font-bold text-sm">
              <i data-lucide="layers-2" class="w-4 h-4"></i>
              <span>7. Seletor de Úlceras Genitais</span>
            </div>
            <div class="space-y-2 text-xs">
              <div>
                <label class="font-semibold block mb-1">Dor na Lesão:</label>
                <select id="ulcer-pain" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 font-medium">
                  <option value="painless">Totalmente INDOLOR</option>
                  <option value="painful">MUITO DOLOROSA / Queimação</option>
                </select>
              </div>
              <div>
                <label class="font-semibold block mb-1">Número de Úlceras:</label>
                <select id="ulcer-count" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 font-medium">
                  <option value="single">Úlcera ÚNICA</option>
                  <option value="multiple">Múltiplas Úlceras ou Vesículas</option>
                </select>
              </div>
              <div>
                <label class="font-semibold block mb-1">Comportamento do Bubão / Linfonodos:</label>
                <select id="ulcer-bubo" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 font-medium">
                  <option value="none">Sem adenopatia ou indolor sem supuração</option>
                  <option value="bilateral">Bilateral, doloroso, sem fistulização (Herpes)</option>
                  <option value="single">Unilateral, volumoso, fistuliza por ORIFÍCIO ÚNICO (Cancro Mole)</option>
                  <option value="multi">Sinal do sulco, fistuliza por MÚLTIPLOS ORIFÍCIOS (LGV)</option>
                </select>
              </div>
            </div>
          </div>
          <div id="ulcer-result" class="pt-2"></div>
        </div>

        <!-- 8. HPV & Bethesda -->
        <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-800/50 space-y-4 shadow-sm flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-purple-600 dark:text-purple-400 font-bold text-sm">
              <i data-lucide="dna" class="w-4 h-4"></i>
              <span>8. Conduta Bethesda & HPV (ASCCP / INCA)</span>
            </div>
            <div class="space-y-2 text-xs">
              <div>
                <label class="font-semibold block mb-1">Resultado Citopatológico:</label>
                <select id="hpv-bethesda" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 font-medium">
                  <option value="ascus">ASC-US (Significado Indeterminado)</option>
                  <option value="lsil">LSIL (Lesão de Baixo Grau / NIC 1)</option>
                  <option value="asch">ASC-H (Não exclui Alto Grau)</option>
                  <option value="hsil">HSIL (Lesão de Alto Grau / NIC 2/3)</option>
                  <option value="agc">AGC (Células Glandulares Atípicas)</option>
                </select>
              </div>
              <div class="grid grid-cols-2 gap-2">
                <div>
                  <label class="font-semibold block mb-1">Idade da Paciente:</label>
                  <select id="hpv-age" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 font-medium">
                    <option value="22">&lt; 25 anos (Jovem)</option>
                    <option value="28" selected>25 a 29 anos</option>
                    <option value="35">&ge; 30 anos</option>
                  </select>
                </div>
                <div class="flex items-center pt-5">
                  <label class="flex items-center gap-1.5 cursor-pointer">
                    <input type="checkbox" id="hpv-positive" class="rounded border-slate-300 text-purple-600 w-4 h-4">
                    <span class="font-semibold">HPV Alto Risco +</span>
                  </label>
                </div>
              </div>
            </div>
          </div>
          <div id="hpv-result" class="pt-2"></div>
        </div>

        <!-- 9. Transmissão Vertical do HIV no Parto -->
        <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-800/50 space-y-4 shadow-sm flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-rose-600 dark:text-rose-400 font-bold text-sm">
              <i data-lucide="baby" class="w-4 h-4"></i>
              <span>9. HIV Periparto & Via de Parto</span>
            </div>
            <div class="space-y-2 text-xs">
              <div>
                <label class="font-semibold block mb-1">Carga Viral com 34 a 36 semanas (cópias/mL):</label>
                <input type="number" id="hiv-vl" value="4800" min="0" step="10" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 font-medium">
                <span class="text-[10px] text-slate-400">Limiar decisivo: &lt; 1.000 vs &ge; 1.000 cópias/mL</span>
              </div>
            </div>
          </div>
          <div id="hiv-result" class="pt-2"></div>
        </div>

        <!-- 10. Rastreador de PEP -->
        <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-800/50 space-y-4 shadow-sm flex flex-col justify-between md:col-span-2 lg:col-span-3">
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-emerald-600 dark:text-emerald-400 font-bold text-sm">
              <i data-lucide="clock" class="w-4 h-4"></i>
              <span>10. Janela Crítica de Profilaxia Pós-Exposição (PEP ao HIV)</span>
            </div>
            <div class="max-w-md space-y-2 text-xs">
              <div>
                <label class="font-semibold block mb-1">Tempo Transcorrido desde a Exposição Sexual ou Acidente (Horas):</label>
                <input type="number" id="pep-hours" value="14" min="0" max="168" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 font-medium">
                <span class="text-[10px] text-slate-400">Janela de Ouro: &le; 2 horas • Janela Limite Absoluta: &le; 72 horas</span>
              </div>
            </div>
          </div>
          <div id="pep-result" class="pt-2"></div>
        </div>

      </div>

    </div>
  </section>

  <!-- ======================================================================
       SEÇÃO: MÓDULOS DE CONTEÚDO CLÍNICO (M50 AO M60)
       ====================================================================== -->
  <main id="modulos-clinicos" class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-16">

    <!-- MÓDULO 50 -->
    <article id="modulo-50" class="module-card p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 shadow-sm space-y-6">
      <div class="flex items-center justify-between flex-wrap gap-2 pb-4 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-3">
          <span class="w-9 h-9 rounded-xl bg-rose-100 dark:bg-rose-950 text-rose-600 dark:text-rose-400 font-black flex items-center justify-center text-sm">50</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Ecossistema Vaginal Normal e o Exame a Fresco</h2>
            <p class="text-xs text-slate-500">Lactobacilos de Döderlein, glicogênio celular, barreira ácida e Wet Mount</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Padrão Ouro Ambulatorial</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <div class="space-y-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
          <div class="p-4 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900/60">
            <h4 class="font-bold text-rose-900 dark:text-rose-200 mb-1 flex items-center gap-1.5">
              <i data-lucide="heart" class="w-4 h-4"></i> Didática & Linha de Defesa Fisiológica
            </h4>
            <p>
              Na menacme, os altos níveis de estrogênio estimulam a maturação das células escamosas vaginais, acumulando reservas de <strong>glicogênio</strong>. Os lactobacilos (*Lactobacillus crispatus*, *L. jensenii*) hidrolisam o glicogênio e produzem <strong>ácido lático</strong>, mantendo o pH vaginal ácido entre <strong>3.8 e 4.5</strong>. Além disso, sintetizam peróxido de hidrogênio (\(H_2O_2\)) e bacteriocinas, impedindo a proliferação de patógenos anaeróbios e leveduras.
            </p>
          </div>

          <div class="space-y-2">
            <h4 class="font-bold text-slate-900 dark:text-white">Passo a Passo do Exame a Fresco (Wet Mount):</h4>
            <ul class="list-disc pl-5 space-y-1">
              <li><strong>Inspeção Especular:</strong> Coleta de secreção em parede vaginal lateral (evitar muco cervical e sangue).</li>
              <li><strong>Fita de pH:</strong> pH normal &le; 4.5; pH &gt; 4.5 indica quebra da barreira (VB ou Tricomoníase).</li>
              <li><strong>Lâmina com Salina 0.9%:</strong> Avaliação de células-guia (clue cells), motilidade de flagelados e leucócitos.</li>
              <li><strong>Lâmina com KOH 10% (Whiff Test):</strong> Lise de células escamosas e volatilização de diaminas pútridas (odor positivo na VB). Permite visualização imediata de pseudo-hifas de cândida.</li>
            </ul>
          </div>
        </div>

        <!-- Imagem 1: Ecossistema Vaginal -->
        <div class="space-y-2">
          <div class="relative group rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md bg-slate-900">
            <img src="assets/img/ecossistema_vaginal_exame_a_fresco.jpg" alt="Ecossistema Vaginal Normal e Exame a Fresco" class="zoomable-image w-full h-auto object-cover cursor-zoom-in transition-transform duration-300 group-hover:scale-[1.02]">
            <div class="absolute bottom-2 right-2 px-2.5 py-1 rounded bg-black/70 backdrop-blur-sm text-white text-[11px] font-bold flex items-center gap-1">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para Ampliar HD
            </div>
          </div>
          <p class="text-[11px] text-center text-slate-500">Diagrama 1: Flora fisiológica, produção de ácido lático e fluxograma do Wet Mount.</p>
        </div>
      </div>
    </article>

    <!-- MÓDULO 51 -->
    <article id="modulo-51" class="module-card p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 shadow-sm space-y-6">
      <div class="flex items-center justify-between flex-wrap gap-2 pb-4 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-3">
          <span class="w-9 h-9 rounded-xl bg-amber-100 dark:bg-amber-950 text-amber-600 dark:text-amber-400 font-black flex items-center justify-center text-sm">51</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">As Grandes Vulvovaginites</h2>
            <p class="text-xs text-slate-500">Vaginose Bacteriana, Candidíase Vulvovaginal e Tricomoníase</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300">CDC 2021 Update</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <!-- Imagem 2: Matriz Vulvovaginites -->
        <div class="space-y-2 order-2 lg:order-1">
          <div class="relative group rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md bg-slate-900">
            <img src="assets/img/vulvovaginites_matriz_comparativa.jpg" alt="Matriz Comparativa das Vulvovaginites" class="zoomable-image w-full h-auto object-cover cursor-zoom-in transition-transform duration-300 group-hover:scale-[1.02]">
            <div class="absolute bottom-2 right-2 px-2.5 py-1 rounded bg-black/70 backdrop-blur-sm text-white text-[11px] font-bold flex items-center gap-1">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para Ampliar HD
            </div>
          </div>
          <p class="text-[11px] text-center text-slate-500">Diagrama 2: Síndromes vaginais, critérios de Amsel, Nugent e esquemas antimicrobianos.</p>
        </div>

        <div class="space-y-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed order-1 lg:order-2">
          <div class="p-3.5 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-900/60 space-y-1">
            <h4 class="font-bold text-amber-900 dark:text-amber-300">Vaginose Bacteriana (VB)</h4>
            <p>
              Disbiose com colapso de lactobacilos e proliferação exponencial de *Gardnerella vaginalis*, *Atopobium vaginae* e anaeróbios estritos. Critérios de Amsel (3 de 4): corrimento fino acinzentado, pH &gt; 4.5, Whiff positivo e &ge; 20% de Clue Cells. <strong>Tratamento:</strong> Metronidazol 500 mg VO 12/12h por 7 dias. Na gestante, tratar sempre para prevenir RPMO e parto prematuro. <em>Parceiro masculino não é tratado rotineiramente.</em>
            </p>
          </div>

          <div class="p-3.5 rounded-xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-900/60 space-y-1">
            <h4 class="font-bold text-rose-900 dark:text-rose-300">Candidíase Vulvovaginal (CVV)</h4>
            <p>
              Proliferação de *C. albicans* com hifas invadindo o epitélio. Corrimento em nata de leite/queijo cottage, prurido excruciante e pH &le; 4.5 preservado. <strong>Tratamento:</strong> Fluconazol 150 mg VO dose única. <strong>Na gestante:</strong> Fluconazol oral é formalmente contraindicado; prescrever estritamente azólicos tópicos por 7 dias!
            </p>
          </div>

          <div class="p-3.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-900/60 space-y-1">
            <h4 class="font-bold text-emerald-900 dark:text-emerald-300">Tricomoníase Vaginal</h4>
            <p>
              IST causada pelo *Trichomonas vaginalis*. Corrimento bolhoso amarelo-esverdeado, colo em morango, protozoários móveis flagelados. <strong>Atualização CDC:</strong> Metronidazol 500 mg VO 12/12h por 7 dias (superior à dose única de 2g). <strong>Tratamento do parceiro é mandatório!</strong>
            </p>
          </div>
        </div>
      </div>
    </article>

    <!-- MÓDULO 52 -->
    <article id="modulo-52" class="module-card p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 shadow-sm space-y-6">
      <div class="flex items-center justify-between flex-wrap gap-2 pb-4 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-3">
          <span class="w-9 h-9 rounded-xl bg-indigo-100 dark:bg-indigo-950 text-indigo-600 dark:text-indigo-400 font-black flex items-center justify-center text-sm">52</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Cervicites, Gonorreia, Clamídia & EPT</h2>
            <p class="text-xs text-slate-500">Tropismo colunar, NAAT molecular, ajuste por peso e Expedited Partner Therapy</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-indigo-100 dark:bg-indigo-950 text-indigo-800 dark:text-indigo-300">Ajuste de Dose &ge; 150 kg</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <div class="space-y-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
          <p>
            *Neisseria gonorrhoeae* e *Chlamydia trachomatis* invadem seletivamente o epitélio colunar simples da endocérvice, poupando a ectocérvice escamosa. Até 80% das infecções por clamídia são assintomáticas, constituindo o grande reservatório silencioso para doença inflamatória pélvica e infertilidade por fator tubário.
          </p>

          <div class="p-4 rounded-xl bg-indigo-50 dark:bg-indigo-950/40 border border-indigo-200 dark:border-indigo-900/60 space-y-2">
            <h4 class="font-bold text-indigo-900 dark:text-indigo-300 flex items-center gap-1.5">
              <i data-lucide="shield-alert" class="w-4 h-4"></i> Diretrizes Farmacológicas Atualizadas
            </h4>
            <div class="space-y-1">
              <div>• <strong>Gonorreia Não Complicada:</strong> Ceftriaxona 500 mg IM dose única (<strong>1 g IM se peso materno &ge; 150 kg</strong>). Infecção faríngea exige compulsoriamente Ceftriaxona.</div>
              <div>• <strong>Clamídia Não Complicada:</strong> Doxiciclina 100 mg VO 12/12h por 7 dias. Na gestante: Azitromicina 1g VO em dose única (doxiciclina contraindicada).</div>
              <div>• <strong>Expedited Partner Therapy (EPT):</strong> Notificar e tratar contatos dos últimos 60 dias. Abstinência sexual por 7 dias e teste de cura aos 3 meses.</div>
            </div>
          </div>
        </div>

        <!-- Imagem 3: Cervicites e EPT -->
        <div class="space-y-2">
          <div class="relative group rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md bg-slate-900">
            <img src="assets/img/cervicites_gonococo_clamidia_ept.jpg" alt="Cervicites, Gonorreia, Clamídia e EPT" class="zoomable-image w-full h-auto object-cover cursor-zoom-in transition-transform duration-300 group-hover:scale-[1.02]">
            <div class="absolute bottom-2 right-2 px-2.5 py-1 rounded bg-black/70 backdrop-blur-sm text-white text-[11px] font-bold flex items-center gap-1">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para Ampliar HD
            </div>
          </div>
          <p class="text-[11px] text-center text-slate-500">Diagrama 3: Fisiopatologia endocervical, biologia molecular e conduta em parceiros.</p>
        </div>
      </div>
    </article>

    <!-- MÓDULO 53 -->
    <article id="modulo-53" class="module-card p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 shadow-sm space-y-6">
      <div class="flex items-center justify-between flex-wrap gap-2 pb-4 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-3">
          <span class="w-9 h-9 rounded-xl bg-rose-100 dark:bg-rose-950 text-rose-600 dark:text-rose-400 font-black flex items-center justify-center text-sm">53</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Doença Inflamatória Pélvica & Abscesso Tubo-Ovariano</h2>
            <p class="text-xs text-slate-500">Critérios de Hager, Chandelier Sign, estratificação de internação e ATO</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-300">Emergência Ginecológica</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <!-- Imagem 4: DIP e Hager -->
        <div class="space-y-2 order-2 lg:order-1">
          <div class="relative group rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md bg-slate-900">
            <img src="assets/img/dip_fisiopatologia_hager_ato.jpg" alt="DIP, Critérios de Hager e Abscesso Tubo-Ovariano" class="zoomable-image w-full h-auto object-cover cursor-zoom-in transition-transform duration-300 group-hover:scale-[1.02]">
            <div class="absolute bottom-2 right-2 px-2.5 py-1 rounded bg-black/70 backdrop-blur-sm text-white text-[11px] font-bold flex items-center gap-1">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para Ampliar HD
            </div>
          </div>
          <p class="text-[11px] text-center text-slate-500">Diagrama 4: Critérios de Hager, esquemas parenterais e fluxograma de ATO estável vs roto.</p>
        </div>

        <div class="space-y-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed order-1 lg:order-2">
          <p>
            A DIP resulta da ascensão polimicrobiana de patógenos cervicais e anaeróbios para tubas uterinas, ovários e peritônio. O limiar de tratamento é intencionalmente baixo para evitar o bloqueio tubário e a infertilidade.
          </p>

          <div class="p-3.5 rounded-xl bg-slate-100 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 space-y-1">
            <h4 class="font-bold text-slate-900 dark:text-white">Critérios Mínimos de Hager (Basta 1 para iniciar ATB empírico):</h4>
            <div>1. Dor à mobilização do colo uterino (<em>Chandelier sign</em>).</div>
            <div>2. Dor à palpação do corpo uterino.</div>
            <div>3. Dor à palpação anexial uni ou bilateral.</div>
          </div>

          <div class="p-3.5 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900/60 space-y-1">
            <h4 class="font-bold text-rose-900 dark:text-rose-300">Abscesso Tubo-Ovariano (ATO):</h4>
            <p>
              Coleção purulenta encapsulada envolvendo anexo. <strong>ATO Estável:</strong> internação para ATB venoso (Cefoxitina + Doxiciclina ou Clindamicina + Gentamicina). Se falha após 48-72h: <strong>drenagem percutânea por imagem</strong>. <strong>ATO Roto:</strong> abdome cirúrgico em tábua, choque séptico; exige laparotomia de urgência imediata!
            </p>
          </div>
        </div>
      </div>
    </article>

    <!-- MÓDULO 54 -->
    <article id="modulo-54" class="module-card p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 shadow-sm space-y-6">
      <div class="flex items-center justify-between flex-wrap gap-2 pb-4 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-3">
          <span class="w-9 h-9 rounded-xl bg-cyan-100 dark:bg-cyan-950 text-cyan-600 dark:text-cyan-400 font-black flex items-center justify-center text-sm">54</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Síndrome de Fitz-Hugh-Curtis e Sequelas Crônicas</h2>
            <p class="text-xs text-slate-500">Peri-hepatite em cordas de violino, transaminases normais e infertilidade tubária</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-cyan-100 dark:bg-cyan-950 text-cyan-800 dark:text-cyan-300">USMLE High-Yield</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <div class="space-y-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
          <p>
            A Síndrome de Fitz-Hugh-Curtis ocorre em 5 a 15% das pacientes com DIP devido à disseminação transperitoneal ascendente de *C. trachomatis* ou *N. gonorrhoeae* até a goteira parietocólica direita e cápsula de Glisson hepática.
          </p>

          <div class="p-4 rounded-xl bg-cyan-50 dark:bg-cyan-950/40 border border-cyan-200 dark:border-cyan-900/60 space-y-2">
            <h4 class="font-bold text-cyan-900 dark:text-cyan-200 flex items-center gap-1.5">
              <i data-lucide="alert-circle" class="w-4 h-4"></i> Pegadinha Clássica de Prova (USMLE & Residência):
            </h4>
            <p>
              A paciente apresenta dor pleurítica em hipocôndrio direito que simula colecistite aguda. No entanto, <strong>as enzimas hepáticas (AST/ALT e bilirrubinas) estão normais ou minimamente elevadas</strong>, pois a infecção é uma peri-hepatite restrita à serosa peritoneal hepática, sem invasão ou necrose do parênquima hepatocitário.
            </p>
            <p class="text-[11px] font-semibold text-cyan-800 dark:text-cyan-300">
              Laparoscopia revela finas aderências fibrosas entre o fígado e a cúpula diafragmática em <strong>"cordas de violino" (violin-string adhesions)</strong>.
            </p>
          </div>

          <div class="space-y-1 text-xs">
            <h4 class="font-bold text-slate-900 dark:text-white">Sequelas Reprodutivas Cumulativas:</h4>
            <div>• 1º episódio de DIP: ~8% de infertilidade por fator tubário.</div>
            <div>• 2º episódio: ~20% de infertilidade.</div>
            <div>• 3º episódio: &gt; 40% de infertilidade e elevação de 6 a 10 vezes no risco de gravidez ectópica.</div>
          </div>
        </div>

        <!-- Imagem 5: Fitz-Hugh-Curtis -->
        <div class="space-y-2">
          <div class="relative group rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md bg-slate-900">
            <img src="assets/img/sindrome_fitz_hugh_curtis_sequelas.jpg" alt="Síndrome de Fitz-Hugh-Curtis e Sequelas Reprodutivas" class="zoomable-image w-full h-auto object-cover cursor-zoom-in transition-transform duration-300 group-hover:scale-[1.02]">
            <div class="absolute bottom-2 right-2 px-2.5 py-1 rounded bg-black/70 backdrop-blur-sm text-white text-[11px] font-bold flex items-center gap-1">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para Ampliar HD
            </div>
          </div>
          <p class="text-[11px] text-center text-slate-500">Diagrama 5: Rota transcelômica de peri-hepatite, cordas de violino e impacto reprodutivo.</p>
        </div>
      </div>
    </article>

    <!-- MÓDULO 55 -->
    <article id="modulo-55" class="module-card p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 shadow-sm space-y-6">
      <div class="flex items-center justify-between flex-wrap gap-2 pb-4 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-3">
          <span class="w-9 h-9 rounded-xl bg-emerald-100 dark:bg-emerald-950 text-emerald-600 dark:text-emerald-400 font-black flex items-center justify-center text-sm">55</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Sífilis Adquirida, Gestacional e Congênita</h2>
            <p class="text-xs text-slate-500">Treponema pallidum, sorologia, efeito prozona e protocolo mandatório de dessensibilização</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300">Regra de Ouro Obstétrica</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <!-- Imagem 6: Sífilis -->
        <div class="space-y-2 order-2 lg:order-1">
          <div class="relative group rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md bg-slate-900">
            <img src="assets/img/sifilis_estadiamento_sorologia_gestacao.jpg" alt="Sífilis Estadiamento, Sorologia e Gestação" class="zoomable-image w-full h-auto object-cover cursor-zoom-in transition-transform duration-300 group-hover:scale-[1.02]">
            <div class="absolute bottom-2 right-2 px-2.5 py-1 rounded bg-black/70 backdrop-blur-sm text-white text-[11px] font-bold flex items-center gap-1">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para Ampliar HD
            </div>
          </div>
          <p class="text-[11px] text-center text-slate-500">Diagrama 6: Estágios clínicos, algoritmos tradicionais/reversos e dessensibilização oral.</p>
        </div>

        <div class="space-y-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed order-1 lg:order-2">
          <div class="p-3.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-900/60 space-y-1">
            <h4 class="font-bold text-emerald-900 dark:text-emerald-300">Estadiamento e Tratamento com Penicilina G Benzatina:</h4>
            <div>• <strong>Primária, Secundária ou Latente Precoce (&lt; 1 ano):</strong> 2.4 milhões de UI IM em dose única.</div>
            <div>• <strong>Latente Tardia (&gt; 1 ano) ou Duração Desconhecida:</strong> 2.4 milhões de UI IM por semana por 3 semanas (total 7.2 milhões de UI).</div>
            <div>• <strong>Neurossífilis / Ocular:</strong> Penicilina Cristalina IV 18 a 24 mi UI/dia por 10 a 14 dias.</div>
          </div>

          <div class="p-3.5 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900/60 space-y-2">
            <h4 class="font-bold text-rose-900 dark:text-rose-300 flex items-center gap-1.5">
              <i data-lucide="alert-octagon" class="w-4 h-4"></i> Dessensibilização Mandatória na Gestante Alérgica
            </h4>
            <p>
              A Penicilina Benzatina é o <strong>único fármaco que atravessa a placenta e trata o feto</strong>, prevenindo sífilis congênita e óbito fetal. Em gestantes com anafilaxia à penicilina, a conduta mandatória é internação hospitalar para <strong>dessensibilização à penicilina oral</strong> em doses crescentes, seguida imediatamente de penicilina benzatina. Doxiciclina e macrolídeos são proscritos!
            </p>
          </div>

          <p class="text-[11px] text-slate-500">
            <strong>Reação de Jarisch-Herxheimer:</strong> Febre, calafrios e taquicardia em 2 a 24h pós-dose por lise de espiroquetas. Não é alergia! Manter suporte com antitérmicos.
          </p>
        </div>
      </div>
    </article>

    <!-- MÓDULO 56 -->
    <article id="modulo-56" class="module-card p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 shadow-sm space-y-6">
      <div class="flex items-center justify-between flex-wrap gap-2 pb-4 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-3">
          <span class="w-9 h-9 rounded-xl bg-rose-100 dark:bg-rose-950 text-rose-600 dark:text-rose-400 font-black flex items-center justify-center text-sm">56</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Matriz Diagnóstica Diferencial de Úlceras Genitais</h2>
            <p class="text-xs text-slate-500">Sífilis, Herpes, Cancro Mole, Linfogranuloma Venéreo e Donovanose</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-300">Diagnóstico Diferencial</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <div class="space-y-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
          <p>
            O diagnóstico sindrômico e etiológico das úlceras genitais apoia-se em quatro pilares fundamentais: <strong>presença de dor</strong>, <strong>número de lesões</strong>, <strong>aspecto do fundo/bordas</strong> e o <strong>comportamento do bubão inguinal</strong>.
          </p>

          <div class="space-y-2 text-xs">
            <div class="p-2.5 rounded-lg bg-slate-100 dark:bg-slate-800/80">
              <strong class="text-rose-600 dark:text-rose-400">Cancro Mole (*Haemophilus ducreyi*):</strong> Múltiplas úlceras extremamente dolorosas, purulentas e com sangramento fácil; bubão que amolece e fistuliza por orifício único. Tratamento: Azitromicina 1g VO dose única.
            </div>
            <div class="p-2.5 rounded-lg bg-slate-100 dark:bg-slate-800/80">
              <strong class="text-indigo-600 dark:text-indigo-400">Linfogranuloma Venéreo (*C. trachomatis* L1-L3):</strong> Úlcera fugaz indolor que passa despercebida; bubão exuberante separado pelo ligamento inguinal (sinal do sulco) que fistuliza por múltiplos orifícios ("bico de regador"). Tratamento: Doxiciclina 100 mg 12/12h por 21 dias.
            </div>
            <div class="p-2.5 rounded-lg bg-slate-100 dark:bg-slate-800/80">
              <strong class="text-emerald-600 dark:text-emerald-400">Donovanose (*Klebsiella granulomatis*):</strong> Úlcera vegetante indolor em "carne viva", bordas em rolete, sem adenopatia verdadeira; biópsia com corpúsculos de Donovan. Tratamento: Azitromicina 1g VO 1x/semana por &ge; 3 semanas.
            </div>
          </div>
        </div>

        <!-- Imagem 7: Úlceras Genitais -->
        <div class="space-y-2">
          <div class="relative group rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md bg-slate-900">
            <img src="assets/img/ulceras_genitais_matriz_diferencial.jpg" alt="Matriz Comparativa das Úlceras Genitais" class="zoomable-image w-full h-auto object-cover cursor-zoom-in transition-transform duration-300 group-hover:scale-[1.02]">
            <div class="absolute bottom-2 right-2 px-2.5 py-1 rounded bg-black/70 backdrop-blur-sm text-white text-[11px] font-bold flex items-center gap-1">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para Ampliar HD
            </div>
          </div>
          <p class="text-[11px] text-center text-slate-500">Diagrama 7: Matriz clínica comparativa de úlceras, fistulização de bubões e terapêutica.</p>
        </div>
      </div>
    </article>

    <!-- MÓDULO 57 -->
    <article id="modulo-57" class="module-card p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 shadow-sm space-y-6">
      <div class="flex items-center justify-between flex-wrap gap-2 pb-4 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-3">
          <span class="w-9 h-9 rounded-xl bg-indigo-100 dark:bg-indigo-950 text-indigo-600 dark:text-indigo-400 font-black flex items-center justify-center text-sm">57</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Herpes Genital na Gestação e Decisão da Via de Parto</h2>
            <p class="text-xs text-slate-500">HSV-1 e HSV-2, profilaxia com 36 semanas, lesão ativa e cesariana imediata</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-indigo-100 dark:bg-indigo-950 text-indigo-800 dark:text-indigo-300">Conduta Periparto ACOG</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <!-- Imagem 8: Herpes Genital -->
        <div class="space-y-2 order-2 lg:order-1">
          <div class="relative group rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md bg-slate-900">
            <img src="assets/img/herpes_genital_profilaxia_parto.jpg" alt="Herpes Genital Profilaxia e Parto" class="zoomable-image w-full h-auto object-cover cursor-zoom-in transition-transform duration-300 group-hover:scale-[1.02]">
            <div class="absolute bottom-2 right-2 px-2.5 py-1 rounded bg-black/70 backdrop-blur-sm text-white text-[11px] font-bold flex items-center gap-1">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para Ampliar HD
            </div>
          </div>
          <p class="text-[11px] text-center text-slate-500">Diagrama 8: Latência sacral, algoritmo periparto e prevenção do herpes neonatal letal.</p>
        </div>

        <div class="space-y-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed order-1 lg:order-2">
          <p>
            O HSV migra pelos axônios sensitivos e aloja-se nos gânglios da raiz dorsal sacral (S2-S4). A primoinfecção é exuberante com vesículas agrupadas dolorosas. Recorrências são mais brandas e precedidas de pródromos neurais (queimação ou parestesia).
          </p>

          <div class="p-4 rounded-xl bg-indigo-50 dark:bg-indigo-950/40 border border-indigo-200 dark:border-indigo-900/60 space-y-2">
            <h4 class="font-bold text-indigo-900 dark:text-indigo-300 flex items-center gap-1.5">
              <i data-lucide="check-circle" class="w-4 h-4"></i> Protocolo Periparto Rigoroso (ACOG / FEBRASGO):
            </h4>
            <div class="space-y-1">
              <div>1. <strong>Gestante com história prévia de Herpes:</strong> Iniciar profilaxia supressiva com Aciclovir 400 mg 3x/dia ou Valaciclovir 500 mg 2x/dia a partir de <strong>36 semanas de gestação</strong> até o parto.</div>
              <div>2. <strong>No momento do trabalho de parto:</strong></div>
              <div class="pl-3 text-rose-700 dark:text-rose-400 font-bold">• Lesão ativa presente (vesícula/úlcera) ou PRÓDROMO: CESARIANA IMEDIATA MANDATÓRIA!</div>
              <div class="pl-3 text-emerald-700 dark:text-emerald-400 font-bold">• Ausência de lesões e sem sintomas prodrômicos: PARTO VAGINAL TOTALMENTE AUTORIZADO!</div>
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- MÓDULO 58 -->
    <article id="modulo-58" class="module-card p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 shadow-sm space-y-6">
      <div class="flex items-center justify-between flex-wrap gap-2 pb-4 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-3">
          <span class="w-9 h-9 rounded-xl bg-purple-100 dark:bg-purple-950 text-purple-600 dark:text-purple-400 font-black flex items-center justify-center text-sm">58</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">HPV, Oncogênese e Rastreamento Bethesda</h2>
            <p class="text-xs text-slate-500">Oncoproteínas E6/E7, condilomas, vacinação e diretrizes comparadas ASCCP vs INCA</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-purple-100 dark:bg-purple-950 text-purple-800 dark:text-purple-300">ASCCP 2019/2023 & INCA</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <div class="space-y-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
          <p>
            O HPV de alto risco (especialmente 16 e 18) produz duas oncoproteínas cruciais: <strong>E6</strong> (que induz ubiquitinação e degradação proteassômica de p53, inibindo apoptose) e <strong>E7</strong> (que inativa pRb, liberando o fator de transcrição E2F e promovendo proliferação celular contínua).
          </p>

          <div class="p-3.5 rounded-xl bg-purple-50 dark:bg-purple-950/40 border border-purple-200 dark:border-purple-900/60 space-y-1">
            <h4 class="font-bold text-purple-900 dark:text-purple-300">Diretrizes Comparadas de Rastreamento Cervical:</h4>
            <div>• <strong>Estados Unidos (USPSTF/ASCCP):</strong> Início aos 21 anos. 21-29 anos com citologia trienal. 30-65 anos preferencialmente Teste de HPV primário a cada 5 anos. Encerramento aos 65 anos.</div>
            <div>• <strong>Brasil (INCA/MS):</strong> Início aos 25 anos. Citologia trienal após 2 anuais negativos. Encerramento aos 64 anos. Incorporação progressiva de DNA-HPV iniciada em 2024.</div>
          </div>

          <div class="space-y-1 text-xs">
            <h4 class="font-bold text-slate-900 dark:text-white">Condutas Chave nas Anormalidades (Bethesda):</h4>
            <div>• <strong>ASC-US:</strong> Repetir em 12 meses se jovem; Colposcopia imediata se HPV+ ou &ge; 30 anos.</div>
            <div>• <strong>ASC-H / HSIL:</strong> Colposcopia imediata com biópsia dirigida mandatória.</div>
            <div>• <strong>Condiloma Acuminado na Gestante:</strong> Tratar com Ácido Tricloroacético (ATA 80-90%). Imiquimode e podofilina são contraindicados. Cesariana indicada apenas se obstrução mecânica volumosa.</div>
          </div>
        </div>

        <!-- Imagem 9: HPV e Bethesda -->
        <div class="space-y-2">
          <div class="relative group rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md bg-slate-900">
            <img src="assets/img/hpv_oncogenese_rastreamento_bethesda.jpg" alt="HPV Oncogênese e Diretrizes de Rastreamento Bethesda" class="zoomable-image w-full h-auto object-cover cursor-zoom-in transition-transform duration-300 group-hover:scale-[1.02]">
            <div class="absolute bottom-2 right-2 px-2.5 py-1 rounded bg-black/70 backdrop-blur-sm text-white text-[11px] font-bold flex items-center gap-1">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para Ampliar HD
            </div>
          </div>
          <p class="text-[11px] text-center text-slate-500">Diagrama 9: Oncogênese viral E6/p53 e E7/pRb, rastreamento comparado e manejo de NIC.</p>
        </div>
      </div>
    </article>

    <!-- MÓDULO 59 -->
    <article id="modulo-59" class="module-card p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 shadow-sm space-y-6">
      <div class="flex items-center justify-between flex-wrap gap-2 pb-4 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-3">
          <span class="w-9 h-9 rounded-xl bg-rose-100 dark:bg-rose-950 text-rose-600 dark:text-rose-400 font-black flex items-center justify-center text-sm">59</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">HIV na Mulher, Transmissão Vertical, PEP e PrEP</h2>
            <p class="text-xs text-slate-500">Carga viral de 34-36 semanas, protocolo de AZT, inibição da lactação e profilaxias</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-300">PCDT / SUS & CDC</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <!-- Imagem 10: HIV e PEP -->
        <div class="space-y-2 order-2 lg:order-1">
          <div class="relative group rounded-2xl overflow-hidden border border-slate-200 dark:border-slate-800 shadow-md bg-slate-900">
            <img src="assets/img/hiv_prevencao_transmissao_vertical_pep.jpg" alt="HIV Prevenção da Transmissão Vertical e Profilaxias" class="zoomable-image w-full h-auto object-cover cursor-zoom-in transition-transform duration-300 group-hover:scale-[1.02]">
            <div class="absolute bottom-2 right-2 px-2.5 py-1 rounded bg-black/70 backdrop-blur-sm text-white text-[11px] font-bold flex items-center gap-1">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5"></i> Clique para Ampliar HD
            </div>
          </div>
          <p class="text-[11px] text-center text-slate-500">Diagrama 10: Algoritmo de parto pelo limiar de 1.000 cópias, AZT venoso e janela da PEP.</p>
        </div>

        <div class="space-y-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed order-1 lg:order-2">
          <p>
            Com a TARV combinada universal iniciada no pré-natal e intervenções adequadas no parto e puerpério, a taxa de transmissão vertical do HIV cai de até 40% para <strong>menos de 1%</strong>.
          </p>

          <div class="p-3.5 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900/60 space-y-1">
            <h4 class="font-bold text-rose-900 dark:text-rose-300">Decisão da Via de Parto (Carga Viral às 34-36 semanas):</h4>
            <div>• <strong>CV &lt; 1.000 cópias/mL:</strong> Parto vaginal autorizado (se condições favoráveis). Sem necessidade de AZT se CV &lt; 50 cópias.</div>
            <div>• <strong>CV &ge; 1.000 cópias/mL ou desconhecida:</strong> <strong>Cesariana eletiva programada com 38 semanas</strong> (bolsa íntegra e sem TP) + <strong>AZT venoso contínuo 3h antes</strong> da incisão até o clampeamento imediato.</div>
          </div>

          <div class="p-3.5 rounded-xl bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 space-y-1">
            <h4 class="font-bold text-slate-900 dark:text-white">Aleitamento Materno e PEP:</h4>
            <div>• <strong>Amamentação:</strong> Formalmente CONTRAINDICADA no Brasil e EUA. Prescrever Cabergolina 1.0 mg VO dose única para inibir lactação.</div>
            <div>• <strong>PEP:</strong> Início em até 72h por 28 dias ininterruptos com TDF + 3TC + Dolutegravir.</div>
          </div>
        </div>
      </div>
    </article>

    <!-- MÓDULO 60 -->
    <article id="modulo-60" class="module-card p-6 sm:p-8 rounded-3xl border border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/90 shadow-sm space-y-8">
      <div class="flex items-center justify-between flex-wrap gap-2 pb-4 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-3">
          <span class="w-9 h-9 rounded-xl bg-indigo-100 dark:bg-indigo-950 text-indigo-600 dark:text-indigo-400 font-black flex items-center justify-center text-sm">60</span>
          <div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">High-Yield Master Matrix, Comunicação OSCE & Estudo Ativo</h2>
            <p class="text-xs text-slate-500">Matriz interativa com filtro, simulação de atendimento e questões comentadas</p>
          </div>
        </div>
        <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-indigo-100 dark:bg-indigo-950 text-indigo-800 dark:text-indigo-300">Revisão Integrativa</span>
      </div>

      <!-- Scripts de Comunicação OSCE -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="p-5 rounded-2xl bg-indigo-50/70 dark:bg-indigo-950/40 border border-indigo-200 dark:border-indigo-900/60 space-y-2">
          <h4 class="font-bold text-indigo-900 dark:text-indigo-300 text-sm flex items-center gap-1.5">
            <i data-lucide="message-square" class="w-4 h-4"></i> Caso OSCE 1: Diagnóstico de Clamídia em Casada
          </h4>
          <p class="text-xs text-slate-600 dark:text-slate-300 italic">
            "Dona Mariana, a clamídia é uma infecção muito silenciosa que pode permanecer oculta por meses ou anos sem nenhum sintoma. Não é possível determinar quando ou quem adquiriu a bactéria primeiro. O mais importante é proteger a sua saúde reprodutiva e a do seu parceiro: trataremos ambos simultaneamente com abstinência por 7 dias."
          </p>
        </div>

        <div class="p-5 rounded-2xl bg-rose-50/70 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900/60 space-y-2">
          <h4 class="font-bold text-rose-900 dark:text-rose-300 text-sm flex items-center gap-1.5">
            <i data-lucide="heart-handshake" class="w-4 h-4"></i> Caso OSCE 2: Gestante em Choque com HIV Positivo
          </h4>
          <p class="text-xs text-slate-600 dark:text-slate-300 italic">
            "Fernanda, respire fundo e olhe para mim: com os antirretrovirais modernos que iniciaremos hoje, a quantidade de vírus no seu sangue cairá tanto que se tornará indetectável, e o risco de transmitir para seu bebê fica menor que 1%. Nós forneceremos gratuitamente toda a fórmula láctea infantil para que ele cresça forte e protegido."
          </p>
        </div>
      </div>

    </article>

  </main>

  <!-- ======================================================================
       SEÇÃO: ESTUDO ATIVO — FLASHCARDS 3D E SIMULADO
       ====================================================================== -->
  <section id="estudo-ativo" class="py-12 bg-slate-100/70 dark:bg-slate-900/50 border-t border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      
      <!-- Bloco de Flashcards 3D -->
      <div class="space-y-4">
        <div class="flex items-center justify-between flex-wrap gap-2">
          <div>
            <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-indigo-100 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300 text-[11px] font-bold uppercase tracking-wider">
              Repetição Espaçada
            </div>
            <h3 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Flashcards 3D de Alta Retenção (15 Cards)</h3>
          </div>
          <span id="fc-counter" class="text-xs font-bold text-slate-500">1 de 15</span>
        </div>

        <div class="max-w-xl mx-auto">
          <!-- Card 3D Container -->
          <div id="flashcard" class="flashcard-container cursor-pointer select-none">
            <div class="flashcard-inner">
              <!-- Frente do Card -->
              <div class="flashcard-front p-8 flex flex-col justify-between">
                <div class="flex items-center justify-between">
                  <span id="fc-category" class="text-[11px] font-bold uppercase tracking-wider text-rose-600 dark:text-rose-400">Módulo</span>
                  <i data-lucide="rotate-cw" class="w-4 h-4 text-slate-400"></i>
                </div>
                <div class="my-auto py-6">
                  <p id="fc-question" class="text-base sm:text-lg font-bold text-slate-900 dark:text-white leading-relaxed text-center">Pergunta...</p>
                </div>
                <div class="text-[10px] text-center text-slate-400 font-semibold uppercase tracking-wider">
                  Clique no card para virar e ver a resposta
                </div>
              </div>

              <!-- Verso do Card -->
              <div class="flashcard-back p-8 flex flex-col justify-between">
                <div class="flex items-center justify-between">
                  <span class="text-[11px] font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Resposta High-Yield</span>
                  <i data-lucide="check-circle" class="w-4 h-4 text-emerald-500"></i>
                </div>
                <div class="my-auto py-6">
                  <p id="fc-answer" class="text-xs sm:text-sm font-medium text-slate-800 dark:text-slate-200 leading-relaxed text-center">Resposta detalhada...</p>
                </div>
                <div class="text-[10px] text-center text-slate-400 font-semibold uppercase tracking-wider">
                  Clique para virar novamente
                </div>
              </div>
            </div>
          </div>

          <!-- Controles do Flashcard -->
          <div class="flex items-center justify-center gap-3 pt-4">
            <button type="button" id="fc-prev" class="px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-slate-50 dark:hover:bg-slate-700 shadow-sm transition-all flex items-center gap-1.5">
              <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> Anterior
            </button>
            <button type="button" id="fc-flip" class="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-extrabold shadow-sm shadow-indigo-500/20 transition-all flex items-center gap-1.5">
              <i data-lucide="rotate-3d" class="w-3.5 h-3.5"></i> Girar Card
            </button>
            <button type="button" id="fc-next" class="px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-slate-50 dark:hover:bg-slate-700 shadow-sm transition-all flex items-center gap-1.5">
              Próximo <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>
      </div>

      <!-- Bloco do Simulado Clínico -->
      <div id="simulado-clinico" class="space-y-6 pt-8 border-t border-slate-200 dark:border-slate-800">
        <div class="flex items-center justify-between flex-wrap gap-3">
          <div>
            <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 text-[11px] font-bold uppercase tracking-wider">
              USMLE Step 2 CK & Residência Médica
            </div>
            <h3 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Simulado Clínico (15 Vinhetas Comentadas)</h3>
          </div>
          <div class="flex items-center gap-3">
            <span id="quiz-score-display" class="px-3 py-1.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs font-extrabold text-slate-700 dark:text-slate-200 shadow-sm">
              Pontuação: 0 de 15 respondidas
            </span>
            <button type="button" id="quiz-reset-btn" class="p-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700 transition-all" title="Reiniciar Simulado">
              <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
            </button>
          </div>
        </div>

        <div id="quiz-container" class="space-y-4 max-w-3xl mx-auto">
          <!-- As questões serão injetadas via app.js -->
        </div>
      </div>

    </div>
  </section>

  <!-- ======================================================================
       MODAL DE LIGHTBOX FULLSCREEN (ZOOM & PAN)
       ====================================================================== -->
  <div id="lightbox-modal" class="hidden fixed inset-0 z-50 bg-black/95 backdrop-blur-md items-center justify-center p-4">
    <div class="absolute top-4 right-4 flex items-center gap-2 z-10">
      <button type="button" id="lightbox-zoom-in" class="p-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white transition-colors" title="Aumentar Zoom">
        <i data-lucide="zoom-in" class="w-5 h-5"></i>
      </button>
      <button type="button" id="lightbox-zoom-out" class="p-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white transition-colors" title="Diminuir Zoom">
        <i data-lucide="zoom-out" class="w-5 h-5"></i>
      </button>
      <button type="button" id="lightbox-reset" class="p-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-white transition-colors" title="Resetar Visualização">
        <i data-lucide="refresh-cw" class="w-5 h-5"></i>
      </button>
      <button type="button" id="lightbox-close" class="p-2.5 rounded-xl bg-rose-600 hover:bg-rose-700 text-white transition-colors" title="Fechar (ESC)">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>
    </div>

    <div class="relative w-full h-full flex flex-col items-center justify-center overflow-hidden">
      <img id="lightbox-img" src="" alt="" class="max-w-full max-h-[85vh] object-contain rounded-xl select-none transition-transform duration-75 cursor-grab">
      <div id="lightbox-caption" class="mt-4 px-4 py-2 rounded-xl bg-black/60 text-white text-xs sm:text-sm font-semibold max-w-2xl text-center"></div>
    </div>
  </div>

  <!-- ======================================================================
       RODAPÉ OFICIAL & DIRETRIZES
       ====================================================================== -->
  <footer class="bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 py-10 mt-auto">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6 text-center sm:text-left">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-lg bg-rose-600 flex items-center justify-center text-white font-black text-sm">
            GO
          </div>
          <div>
            <div class="font-extrabold text-sm text-slate-900 dark:text-white">Internato GO • Infecções & ISTs (Parte 6)</div>
            <div class="text-[11px] text-slate-500">Desenvolvido para estudo médico de excelência • GitHub Pages Ready</div>
          </div>
        </div>

        <div class="flex items-center gap-2 text-xs font-bold">
          <span class="px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">PCDT / SUS</span>
          <span class="px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">CDC 2021/2024</span>
          <span class="px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">FEBRASGO</span>
          <span class="px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">ASCCP</span>
          <span class="px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">INCA</span>
        </div>
      </div>

      <div class="pt-6 border-t border-slate-100 dark:border-slate-800/80 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-400">
        <div>Conteúdo puramente didático para profissionais e estudantes de medicina. Uso clínico sob responsabilidade técnica médica.</div>
        <a href="#" class="hover:text-rose-600 transition-colors flex items-center gap-1">
          <span>Voltar ao topo</span>
          <i data-lucide="arrow-up" class="w-3.5 h-3.5"></i>
        </a>
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="assets/js/app.js"></script>
  <script>
    // Inicializa ícones do Lucide
    if (window.lucide) {
      lucide.createIcons();
    }
  </script>
</body>
</html>
"""

def main():
    print(f"Escrevendo arquivo {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"[OK] {OUTPUT_FILE} gerado com sucesso ({len(HTML_CONTENT)} bytes)!")

if __name__ == "__main__":
    main()
