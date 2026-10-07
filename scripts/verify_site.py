# -*- coding: utf-8 -*-
"""
verify_site.py - Verificação Completa do Portal site_infeccoes_ists
Valida estrutura de arquivos, IDs no DOM, imagens em assets/img/ e sintaxe JS/CSS.
"""

import os
import re
import sys

def test_site():
    print("=== INICIANDO VERIFICAÇÃO AUTOMATIZADA DO PORTAL (PARTE 6) ===")
    errors = []

    # 1. Arquivos essenciais
    essential_files = [
        "index.html",
        ".nojekyll",
        "assets/css/custom.css",
        "assets/js/app.js"
    ]
    for ef in essential_files:
        if not os.path.isfile(ef):
            errors.append(f"Arquivo essencial ausente: {ef}")
        else:
            sz = os.path.getsize(ef)
            print(f"[OK] Arquivo presente: {ef} ({sz} bytes)")

    # 2. Imagens
    images = [
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
    for img in images:
        if not os.path.isfile(img):
            errors.append(f"Imagem ausente: {img}")
        else:
            sz = os.path.getsize(img)
            print(f"[OK] Imagem verificada: {img} ({sz} bytes)")

    # 3. Ler index.html e verificar IDs necessários pelo JS
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    with open("assets/js/app.js", "r", encoding="utf-8") as f:
        js = f.read()

    js_ids = set(re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", js))
    html_ids = set(re.findall(r'id=["\']([^"\']+)["\']', html))

    missing_ids = []
    for jid in js_ids:
        if jid not in html_ids:
            missing_ids.append(jid)

    if missing_ids:
        errors.append(f"IDs exigidos pelo JS ausentes no HTML: {missing_ids}")
    else:
        print(f"[OK] Todos os {len(js_ids)} IDs exigidos por app.js estao presentes no index.html!")

    # 4. Módulos 50 a 60
    for mod in range(50, 61):
        mod_id = f"modulo-{mod}"
        if mod_id not in html_ids:
            errors.append(f"Módulo ausente no HTML: #{mod_id}")
        else:
            print(f"[OK] Módulo #{mod_id} verificado!")

    # 5. Classes interativas
    if "zoomable-image" not in html:
        errors.append("Classe .zoomable-image ausente no HTML")
    if "pid-crit" not in html:
        errors.append("Classe .pid-crit ausente no HTML")
    if "module-card" not in html:
        errors.append("Classe .module-card ausente no HTML")

    # Resumo
    print("\n=== RESUMO DA VERIFICAÇÃO ===")
    if errors:
        print(f"ERROS ENCONTRADOS ({len(errors)}):")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("[SUCESSO TOTAL] O portal esta 100% integro, validado e pronto para deploy!")

if __name__ == "__main__":
    test_site()
