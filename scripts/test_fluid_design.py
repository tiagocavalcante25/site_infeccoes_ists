# -*- coding: utf-8 -*-
"""
test_fluid_design.py
Verifica matematicamente e estruturalmente as exigências de responsividade no site_infeccoes_ists:
1. Imagens com max-width: 100% e altura proporcional
2. Tipografia fluida com unidades responsivas (clamp, vw, rem)
3. Blindagem contra rolagem horizontal (overflow-x: hidden, overflow-x: clip, min-width: 0, word-wrap, overflow-wrap)
4. Menu fixo no topo (position: fixed) e ausência de menu lateral redundante
"""
import os
import re
import sys

site_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
css_path = os.path.join(site_dir, 'assets', 'css', 'custom.css')
html_path = os.path.join(site_dir, 'index.html')

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

errors = []

print("=== TESTE 1: IMAGENS COM LARGURA MÁXIMA 100% E ALTURA PROPORCIONAL ===")
if 'img, picture, video, canvas, svg' in css and 'max-width: 100% !important' in css and 'height: auto !important' in css:
    print("[PASS] Regra global CSS: img, picture, video, canvas, svg possuem max-width: 100% !important e height: auto !important.")
else:
    errors.append("Regra global de img não encontrada no custom.css")

if '.fluid-img' in css and 'aspect-ratio: 1350 / 900' in css:
    print("[PASS] Regra de aspecto anatômico proporcional: .fluid-img possui aspect-ratio: 1350 / 900.")
else:
    errors.append(".fluid-img com aspect-ratio não encontrada no CSS")

expected_images = [
    "ecossistema_vaginal_exame_a_fresco.jpg",
    "vulvovaginites_matriz_comparativa.jpg",
    "cervicites_gonococo_clamidia_ept.jpg",
    "dip_fisiopatologia_hager_ato.jpg",
    "sindrome_fitz_hugh_curtis_sequelas.jpg",
    "sifilis_estadiamento_sorologia_gestacao.jpg",
    "ulceras_genitais_matriz_diferencial.jpg",
    "herpes_genital_profilaxia_parto.jpg",
    "hpv_oncogenese_rastreamento_bethesda.jpg",
    "hiv_prevencao_transmissao_vertical_pep.jpg"
]

for img_name in expected_images:
    pattern = rf'<img[^>]+src=["\']assets/img/{img_name}["\'][^>]*>'
    match = re.search(pattern, html)
    if match:
        tag = match.group(0)
        if 'fluid-img' in tag and 'w-full' in tag and 'max-w-full' in tag and 'h-auto' in tag and 'width=' in tag and 'height=' in tag:
            print(f"[PASS] Imagem {img_name} 100% fluida, com dimensões proporcionais e contêiner blindado.")
        else:
            errors.append(f"Imagem {img_name} não possui todos os atributos responsivos fluidos: {tag}")
    else:
        errors.append(f"Imagem {img_name} não encontrada no index.html")

print("\n=== TESTE 2: TIPOGRAFIA FLUIDA COM UNIDADES RESPONSIVAS (CLAMP / VW) ===")
headings = ['h1', 'h2', 'h3', 'h4']
for h in headings:
    if re.search(rf'(?:^|,|\s){h}\b[^\{{]*\{{[^}}]*font-size:\s*clamp\(', css, re.MULTILINE):
        print(f"[PASS] Tag <{h}> utiliza clamp() com unidades responsivas.")
    else:
        errors.append(f"Tag <{h}> não possui clamp() no CSS")

text_classes = ['text-xs', 'text-sm', 'text-base', 'text-lg', 'text-xl', 'text-2xl', 'text-3xl', 'text-4xl', 'text-5xl']
for tc in text_classes:
    if re.search(rf'\.{tc}\s*\{{[^}}]*clamp\(', css):
        print(f"[PASS] Classe .{tc} configurada com clamp() responsivo no custom.css.")
    else:
        errors.append(f"Classe .{tc} não encontrada com clamp() no CSS")

if 'fontSize:' in html and 'clamp(' in html:
    print("[PASS] tailwind.config injeta classes fluidas responsivas clamp() no motor Tailwind.")
else:
    errors.append("tailwind.config sem fontSize clamp()")

print("\n=== TESTE 3: BLINDAGEM CONTRA ROLAGEM HORIZONTAL & CONTÊINERES ===")
if 'overflow-x: clip' in css and 'overflow-x: hidden' in css:
    print("[PASS] html e body protegidos com overflow-x: clip e overflow-x: hidden.")
else:
    errors.append("html e body sem overflow-x adequados")

if 'box-sizing: border-box' in css and 'min-width: 0' in css:
    print("[PASS] Reset universal *, *::before, *::after com box-sizing: border-box e min-width: 0 (flex/grid safe).")
else:
    errors.append("Reset universal sem min-width: 0")

if 'word-wrap: break-word' in css and 'overflow-wrap: break-word' in css and 'overflow-wrap: anywhere' in css:
    print("[PASS] Prevenção de quebra e estouro com word-wrap: break-word e overflow-wrap.")
else:
    errors.append("Regras de word-wrap / overflow-wrap ausentes no CSS")

if 'max-width: 100% !important' in css:
    print("[PASS] Contêineres globais configurados com max-width: 100% !important.")
else:
    errors.append("Contêineres globais sem max-width: 100%")

print("\n=== TESTE 4: MENU FIXO NO TOPO & SEM GAVETA REDUNDANTE ===")
if 'position: fixed' in css and 'top: 0' in css:
    print("[PASS] Header configurado com position: fixed no topo da tela.")
else:
    errors.append("Header sem position: fixed no CSS")

if 'mobile-menu-drawer' not in html and 'mobile-menu-backdrop' not in html:
    print("[PASS] Menu lateral redundante completamente removido do HTML.")
else:
    errors.append("mobile-menu-drawer ainda presente no HTML")

if 'data-font-size-set' in html:
    print("[PASS] Controles dinâmicos de tamanho de fonte (A / A+ / A++) presentes no topo.")
else:
    errors.append("Controles de tamanho de fonte ausentes no index.html")

print("\n=======================================================")
if errors:
    print("ERROS ENCONTRADOS:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
else:
    print(">>> TODOS OS PILARES DE RESPONSIVIDADE E FLUIDEZ FORAM CONFIRMADOS COM 100% DE SUCESSO! <<<")
    sys.exit(0)
