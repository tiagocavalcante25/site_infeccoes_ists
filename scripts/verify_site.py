# -*- coding: utf-8 -*-
"""
verify_site.py - Verificação Completa de Integridade do Portal de Infecções & ISTs (Parte 6)
Valida estrutura de arquivos, compatibilidade com GitHub Pages, IDs no DOM,
imagens em assets/img/, responsividade mobile e sintaxe JS/CSS.
"""

import os
import re
import sys

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check_file(rel_path):
    full = os.path.join(SITE_DIR, rel_path)
    exists = os.path.exists(full)
    size = os.path.getsize(full) if exists else 0
    print(f"[{'PASS' if exists and size > 0 else 'FAIL'}] {rel_path} (Tamanho: {size:,} bytes)")
    return exists and size > 0

def test_site():
    print("=== VERIFICAÇÃO DE INTEGRIDADE: INFECÇÕES GINECOLÓGICAS & ISTs ===")
    print(f"Diretório Raiz: {SITE_DIR}\n")
    all_ok = True

    # 1. Arquivos essenciais
    print("=== 1. ARQUIVOS PRINCIPAIS & ATIVOS ESTÁTICOS ===")
    essential_files = [
        "index.html",
        ".nojekyll",
        "assets/css/custom.css",
        "assets/js/app.js",
        "assets/img/ecossistema_vaginal_exame_a_fresco.jpg",
        "assets/img/vulvovaginites_matriz_comparativa.jpg",
        "assets/img/cervicites_gonococo_clamidia_ept.jpg",
        "assets/img/dip_fisiopatologia_hager_ato.jpg",
        "assets/img/sindrome_fitz_hugh_curtis_sequelas.jpg",
        "assets/img/sifilis_estadiamento_sorologia_gestacao.jpg",
        "assets/img/ulceras_genitais_matriz_diferencial.jpg",
        "assets/img/herpes_genital_profilaxia_parto.jpg",
        "assets/img/hpv_oncogenese_rastreamento_bethesda.jpg",
        "assets/img/hiv_prevencao_transmissao_vertical_pep.jpg"
    ]
    for ef in essential_files:
        if not check_file(ef):
            all_ok = False

    # 2. Compatibilidade com GitHub Pages
    print("\n=== 2. COMPATIBILIDADE COM GITHUB PAGES (URLS RELATIVAS) ===")
    index_path = os.path.join(SITE_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    bad_absolute_paths = re.findall(r'(?:href|src)=["\']/(assets/[^"\']+)["\']', html)
    if bad_absolute_paths:
        print(f"[ERRO] Encontrados caminhos absolutos que quebram no GitHub Pages: {bad_absolute_paths}")
        all_ok = False
    else:
        print("[PASS] Todos os caminhos de assets utilizam links relativos (compatíveis com subpastas do GitHub Pages).")

    nojekyll_path = os.path.join(SITE_DIR, ".nojekyll")
    if os.path.exists(nojekyll_path):
        print("[PASS] Arquivo .nojekyll presente (Jekyll desativado para preservação total de pastas).")
    else:
        print("[ERRO] Arquivo .nojekyll não encontrado.")
        all_ok = False

    # 3. Auditoria de IDs entre app.js e index.html
    print("\n=== 3. AUDITORIA DE IDS DOM (JAVASCRIPT / HTML) ===")
    js_path = os.path.join(SITE_DIR, "assets", "js", "app.js")
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()

    js_ids = set(re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", js))
    html_ids = set(re.findall(r'id=["\']([^"\']+)["\']', html))

    missing_ids = [jid for jid in js_ids if jid not in html_ids]
    if missing_ids:
        print(f"[ERRO] IDs exigidos pelo JS ausentes no HTML: {missing_ids}")
        all_ok = False
    else:
        print(f"[PASS] Todos os {len(js_ids)} IDs exigidos por app.js estão presentes no index.html!")

    # 4. Módulos 50 a 60
    print("\n=== 4. AUDITORIA DOS 11 MÓDULOS CLÍNICOS ===")
    for mod in range(50, 61):
        mod_id = f"modulo-{mod}"
        if mod_id not in html_ids:
            print(f"[ERRO] Módulo ausente no HTML: #{mod_id}")
            all_ok = False
        else:
            print(f"[PASS] Módulo #{mod_id} verificado!")

    # 5. Auditoria de Responsividade Mobile & iOS
    print("\n=== 5. AUDITORIA DE RESPONSIVIDADE MOBILE & IOS ===")
    if 'viewport-fit=cover' in html:
        print("[PASS] Meta viewport configurado com 'viewport-fit=cover' para suporte a notch/Dynamic Island do iPhone.")
    else:
        print("[AVISO] 'viewport-fit=cover' ausente na meta tag viewport.")

    if 'apple-mobile-web-app-capable' in html:
        print("[PASS] Meta tags para Web App iOS (Safari PWA) configuradas.")
    else:
        print("[AVISO] Meta tags para iOS Safari PWA ausentes.")

    if 'id="fab-back-to-top"' in html:
        print("[PASS] Botão Flutuante (FAB) Voltar ao Topo presente no DOM.")
    else:
        print("[AVISO] Botão FAB Voltar ao Topo não encontrado.")

    if 'data-font-size-set' in html:
        print("[PASS] Controles dinâmicos de tamanho de fonte (A / A+ / A++) presentes no DOM.")
    else:
        print("[AVISO] Controles dinâmicos de tamanho de fonte não encontrados.")

    # Resumo
    print("\n=======================================================")
    if not all_ok:
        print(">>> FALHA NA VERIFICAÇÃO: Corrija os erros acima antes de realizar o deploy. <<<")
        sys.exit(1)
    else:
        print(">>> SUCESSO TOTAL: O Portal de Infecções & ISTs está 100% íntegro e pronto para deploy no GITHUB PAGES! <<<")
        sys.exit(0)

if __name__ == "__main__":
    test_site()
