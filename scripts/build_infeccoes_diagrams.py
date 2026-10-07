"""
build_infeccoes_diagrams.py - Gerador de Infográficos Médicos de Alta Definição
Parte 6: Infecções Ginecológicas e ISTs • FEBRASGO / SUS / CDC / ACOG / ASCCP / INCA
"""

import os
from PIL import Image, ImageDraw, ImageFont

IMG_DIR = r"c:\Users\Admin\Downloads\INTERNATO GO\site_infeccoes_ists\assets\img"
os.makedirs(IMG_DIR, exist_ok=True)

# Fontes do Windows
FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_REG = r"C:\Windows\Fonts\segoeui.ttf"
FONT_ITALIC = r"C:\Windows\Fonts\segoeuii.ttf"

def get_font(size, bold=False, italic=False):
    path = FONT_BOLD if bold else (FONT_ITALIC if italic else FONT_REG)
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def draw_header(draw, width, title, subtitle, badge_text="FEBRASGO • SUS • CDC 2021 • ACOG • ASCCP"):
    draw.rectangle([0, 0, width, 110], fill="#0f172a")
    draw.rectangle([0, 106, width, 110], fill="#e11d48")
    
    # Badge
    f_badge = get_font(13, bold=True)
    draw.rounded_rectangle([30, 20, 320, 44], radius=6, fill="#e11d48")
    draw.text((42, 23), badge_text, fill="#ffffff", font=f_badge)
    
    # Título e Subtítulo
    f_title = get_font(26, bold=True)
    f_sub = get_font(15, italic=False)
    draw.text((30, 52), title, fill="#ffffff", font=f_title)
    draw.text((30, 84), subtitle, fill="#94a3b8", font=f_sub)

def draw_footer(draw, width, height, text="Guia Obstetrícia & Ginecologia Parte 6 — Portal Interativo de Decisão Clínica"):
    draw.rectangle([0, height - 35, width, height], fill="#0f172a")
    f = get_font(12, italic=True)
    draw.text((30, height - 25), text, fill="#94a3b8", font=f)

# ==============================================================================
# 1. ECOSSISTEMA VAGINAL & EXAME A FRESCO (M50)
# ==============================================================================
def create_diagram_ecossistema_vaginal():
    W, H = 1350, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "O ECOSSISTEMA VAGINAL NORMAL & EXAME A FRESCO (WET MOUNT)", "Microbiota Fisiológica • Fermentação de Glicogênio • Passo a Passo de Consultório")

    # Coluna 1: A Linha de Defesa
    draw.rounded_rectangle([30, 130, 430, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 430, 175], radius=10, fill="#1e293b")
    draw.text((45, 142), "1. MICROBIOTA & BARREIRA", fill="#ffffff", font=get_font(16, bold=True))

    bars = [
        ("Estrogênio & Glicogênio", "O estrogênio estimula a maturação do epitélio escamoso estratificado vaginal e o acúmulo intracelular de glicogênio nas camadas intermediária e superficial."),
        ("Bacilos de Döderlein", "Lactobacillus crispatus, L. jensenii e L. gasseri hidrolisam o glicogênio e fermentam em ÁCIDO LÁTICO (isômeros D e L), mantendo o pH vaginal ácido entre 3.8 e 4.5."),
        ("Peróxido de Hidrogênio (H2O2)", "Os lactobacilos produzem H2O2 e bacteriocinas que inibem competitivamente a adesão e proliferação de anaeróbios facultativos, leveduras e patógenos de ISTs."),
        ("Secreção Fisiológica Normal", "Composta por células escamosas maduras esfoliadas, transudato sérico e escassos leucócitos (relação leucócito:célula epitelial < 1:1). Não há odor fétido ou prurido.")
    ]
    y = 190
    for title, desc in bars:
        draw.rounded_rectangle([45, y, 415, y + 140], radius=8, fill="#eff6ff", outline="#bfdbfe")
        draw.text((55, y + 8), title, fill="#1e3a8a", font=get_font(13, bold=True))
        draw.text((55, y + 34), desc, fill="#1e40af", font=get_font(11))
        y += 152

    # Coluna 2: Passo a Passo do Exame a Fresco
    draw.rounded_rectangle([450, 130, 890, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([450, 130, 890, 175], radius=10, fill="#0284c7")
    draw.text((465, 142), "2. PASSO A PASSO NO CONSULTÓRIO", fill="#ffffff", font=get_font(16, bold=True))

    steps = [
        ("Passo 1: Coleta em Parede Lateral", "Exame especular sem lubrificante. Coleta com espátula ou swab estéril no terço médio das paredes vaginais laterais (evitar muco cervical ou sangue)."),
        ("Passo 2: Fita Reativa de pH", "Tocar a secreção diretamente na fita de pH de faixa estreita.\n• pH Normal (<= 4.5): Candidíase ou Fisiológico\n• pH Elevado (> 4.5): Vaginose Bacteriana ou Tricomoníase"),
        ("Passo 3: Lâmina 1 (Solução Salina 0.9%)", "Microscopia direta com salina:\n• Clue cells (> 20%): Vaginose Bacteriana\n• Protozoários flagelados móveis + neutrófilos: Tricomoníase\n• Células escamosas limpas com lactobacilos: Fisiológico"),
        ("Passo 4: Lâmina 2 (KOH 10% - Whiff Test)", "Adicionar 1 gota de KOH 10%:\n• Teste das Aminas Positivo (odor fétido a peixe podre): VB ou Tricomoníase\n• Microscopia pós-lise celular: Hifas e blastoconídios de Candidíase")
    ]
    y = 190
    for title, desc in steps:
        draw.rounded_rectangle([465, y, 875, y + 140], radius=8, fill="#f0f9ff", outline="#bae6fd")
        draw.text((475, y + 8), title, fill="#0369a1", font=get_font(13, bold=True))
        draw.text((475, y + 34), desc, fill="#0c4a6e", font=get_font(11))
        y += 152

    # Coluna 3: Raciocínio Rápido
    draw.rounded_rectangle([910, 130, 1320, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([910, 130, 1320, 175], radius=10, fill="#0f172a")
    draw.text((925, 142), "3. RACIOCÍNIO POR pH & AMINAS", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([925, 190, 1305, 480], radius=8, fill="#fdf2f8", outline="#fbcfe8")
    draw.text((935, 200), "Dilema do pH Vaginal de Beira do Leito", fill="#831843", font=get_font(14, bold=True))
    draw.text((935, 226), "• pH <= 4.5 (Ácido Preservado):\n  - Candidíase Vulvovaginal (CVV)\n  - Secreção Fisiológica Normal\n  - Vaginose Citolítica (pH < 4.0)\n\n• pH > 4.5 (Alcalinizado):\n  - Vaginose Bacteriana (VB: pH 5.0 - 6.0)\n  - Tricomoníase (pH 5.5 - 6.5)\n  - Vaginite Descamativa Inflamatória (VDI)\n  - Vaginite Atrófica (Menopausa: pH > 5.5)\n\n⚠️ Atenção: Sangue menstrual (pH 7.4) e sêmen (pH 7.8)\nalcalinizam a vagina e geram falsos resultados de pH!", fill="#701a75", font=get_font(12))

    draw.rounded_rectangle([925, 500, 1305, 830], radius=8, fill="#fef2f2", outline="#fecaca")
    draw.text((935, 510), "Whiff Test: A Química das Aminas", fill="#991b1b", font=get_font(14, bold=True))
    draw.text((935, 536), "As bactérias anaeróbias estritas da disbiose descarboxilam\naminoácidos e produzem diaminas voláteis:\n• Putrescina\n• Cadaverina\n• Trimetilamina\n\nEm meio ácido, essas aminas permanecem protonadas\ne sem cheiro. O KOH 10% (ou o sêmen alcalino no coito)\ndesprotona essas moléculas, liberando o odor fétido típico\nde 'peixe podre' característico da VB!", fill="#7f1d1d", font=get_font(12))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "ecossistema_vaginal_exame_a_fresco.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 2. AS GRANDES VULVOVAGINITES: MATRIZ COMPARATIVA (M51)
# ==============================================================================
def create_diagram_vulvovaginites():
    W, H = 1400, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "AS GRANDES VULVOVAGINITES: MATRIZ COMPARATIVA COMPLETA", "Vaginose Bacteriana vs Candidíase vs Tricomoníase • Critérios de Amsel • CDC 2021")

    # Tabela Comparativa em 4 Colunas
    cols = [
        ("Vaginose Bacteriana (VB)", "#be123c", "#fff1f2", "#881337", [
            ("Patógeno", "Disbiose polimicrobiana (Gardnerella, Atopobium, Prevotella, Mobiluncus)."),
            ("Sintoma Central", "Odor desagradável a peixe podre, pior pós-coito e menstruação. Sem prurido intenso."),
            ("Aspecto da Secreção", "Fluida, homogênea, cinzenta-esbranquiçada, aderente às paredes vaginais."),
            ("Epitélio / Vulva", "SEM inflamação ou eritema verdadeiro (é vaginose, não vaginite!)."),
            ("pH Vaginal", "> 4.5 (geralmente 5.0 a 6.0)."),
            ("Whiff Test", "FORTEMENTE POSITIVO (odor fétido imediato)."),
            ("Microscopia", "CLUE CELLS (> 20%), ausência de leucócitos, escassos lactobacilos."),
            ("Tratamento de 1ª Linha", "Metronidazol 500 mg VO 12/12h por 7 dias (ou gel por 5 noites). Evitar álcool!"),
            ("Manejo do Parceiro", "NÃO tratar parceiro masculino rotineiramente (não reduz recidiva).")
        ]),
        ("Candidíase Vulvovaginal (CVV)", "#701a75", "#fdf4ff", "#4a044e", [
            ("Patógeno", "Candida albicans (85-90%) ou C. glabrata (resistente a azólicos)."),
            ("Sintoma Central", "PRURIDO VULVAR INTENSO, queimação, ardor miccional externo e dispareunia."),
            ("Aspecto da Secreção", "Branca, espessa, em grumos ('nata de leite' ou 'queijo cottage')."),
            ("Epitélio / Vulva", "INTENSA VULVOVAGINITE (eritema vulvar, edema, fissuras e escoriações)."),
            ("pH Vaginal", "<= 4.5 (ÁCIDO FISIOLÓGICO PRESERVADO!)."),
            ("Whiff Test", "NEGATIVO."),
            ("Microscopia", "HIFAS, PSEUDO-HIFAS e blastoconídios em KOH 10%. Lactobacilos preservados."),
            ("Tratamento de 1ª Linha", "Fluconazol 150 mg VO dose única (SE GESTANTE: estritamente azólico tópico!)."),
            ("Manejo do Parceiro", "NÃO tratar se parceiro assintomático. Tratar apenas se balanite.")
        ]),
        ("Tricomoníase Vaginal", "#047857", "#ecfdf5", "#064e3b", [
            ("Patógeno", "Trichomonas vaginalis (protozoário anaeróbio flagelado)."),
            ("Sintoma Central", "Corrimento abundante, disúria, odor fétido e queimação genital."),
            ("Aspecto da Secreção", "Amarelo-esverdeada, abundante, BOLHOSA e fluida."),
            ("Epitélio / Vulva", "Colpite difusa com petéquias: 'COLO EM MORANGO' (strawberry cervix)."),
            ("pH Vaginal", "> 4.5 (geralmente 5.5 a 6.5)."),
            ("Whiff Test", "Frequentemente positivo."),
            ("Microscopia", "PROTOZOÁRIOS FLAGELADOS MÓVEIS com motilidade ondulante + leucocitose maciça."),
            ("Tratamento de 1ª Linha", "Metronidazol 500 mg VO 12/12h por 7 dias (CDC comprovou superioridade)."),
            ("Manejo do Parceiro", "TRATAMENTO OBRIGATÓRIO DO PARCEIRO! É uma IST clássica. Abstinência 7 dias.")
        ]),
        ("Critérios de Amsel & Gestação", "#1e293b", "#f8fafc", "#0f172a", [
            ("Critérios de Amsel (VB)", "Exige >= 3 de 4:\n1. Corrimento fino cinzento\n2. pH vaginal > 4.5\n3. Whiff test positivo\n4. Clue cells >= 20%"),
            ("Escore de Nugent", "Padrão-ouro em pesquisa (coloração de Gram: 0-3 normal, 4-6 intermediário, 7-10 VB)."),
            ("Candidíase Gestacional", "Tratamento TÓPICO OBRIGATÓRIO por 7 noites (Clotrimazol 1%). Fluconazol contraindicado."),
            ("C. glabrata", "Ácido Bórico 600 mg intravaginal por 14 a 21 dias."),
            ("Riscos Perinatais", "VB e Tricomoníase aumentam risco de RPMO, corioamnionite e prematuridade."),
            ("Vaginose Citolítica", "Lactobacilos em excesso, citólise, pH < 4.0. Tratar com banho de bicarbonato."),
            ("Vaginite Atrófica", "Hipoestrogenismo, pH > 5.5, células parabasais. Tratar com estriol tópico."),
            ("Dissulfiram-Like", "Metronidazol + etanol = vômitos incoercíveis, rubor facial e hipotensão!"),
            ("Testes Moleculares", "NAAT (PCR) é o padrão-ouro de sensibilidade para Trichomonas vaginalis.")
        ])
    ]

    col_w = 320
    x = 30
    for header_title, head_bg, card_bg, text_col, items in cols:
        draw.rounded_rectangle([x, 130, x + col_w, 850], radius=10, fill=card_bg, outline="#cbd5e1", width=2)
        draw.rounded_rectangle([x, 130, x + col_w, 175], radius=8, fill=head_bg)
        draw.text((x + 12, 144), header_title, fill="#ffffff", font=get_font(13, bold=True))

        cur_y = 190
        for item_label, item_desc in items:
            draw.text((x + 12, cur_y), item_label + ":", fill=text_col, font=get_font(11, bold=True))
            draw.text((x + 12, cur_y + 16), item_desc, fill="#334155", font=get_font(10))
            cur_y += 68

        x += col_w + 18

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "vulvovaginites_matriz_comparativa.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 3. CERVICITES: GONORREIA, CLAMÍDIA & EPT (M52)
# ==============================================================================
def create_diagram_cervicites():
    W, H = 1350, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "CERVICITES: GONORREIA, CLAMÍDIA & EXPEDITED PARTNER THERAPY", "Tropismo Endocervical • Diagnóstico por NAAT • Esquema Duplo & Manejo de Parceiros")

    # Coluna 1: O Inimigo Silencioso
    draw.rounded_rectangle([30, 130, 420, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 420, 175], radius=10, fill="#be123c")
    draw.text((45, 142), "1. OS PATÓGENOS & CLÍNICA", fill="#ffffff", font=get_font(16, bold=True))

    cerv_items = [
        ("Tropismo pelo Endocérvice", "O ectocérvice é revestido por epitélio escamoso estratificado (resistente). O endocérvice possui epitélio colunar mucossecretor, vulnerável à invasão por clamídia e gonococo."),
        ("Chlamydia trachomatis (D-K)", "Bactéria intracelular obrigatória com ciclo bifásico: Corpo Elementar (CE - infeccioso extracelular) e Corpo Reticular (CR - replicativo intracelular). 70 a 80% das mulheres são assintomáticas!"),
        ("Neisseria gonorrhoeae", "Diplococo Gram-negativo intracelular com pili e proteínas Opa que aderem ao epitélio e liberam endotoxinas (LOS), gerando exsudação purulenta intensa e friabilidade cervical."),
        ("Manifestações Típicas", "• Secreção endocervical mucopurulenta espessa\n• Friabilidade cervical (sangramento ao toque do swab)\n• Disúria estéril e sinusorragia (sangramento pós-coito)")
    ]
    y = 190
    for title, desc in cerv_items:
        draw.rounded_rectangle([45, y, 405, y + 140], radius=8, fill="#fff1f2", outline="#fecdd3")
        draw.text((55, y + 8), title, fill="#9f1239", font=get_font(13, bold=True))
        draw.text((55, y + 34), desc, fill="#4c0519", font=get_font(11))
        y += 152

    # Coluna 2: Diagnóstico e Terapêutica Dupla
    draw.rounded_rectangle([440, 130, 880, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([440, 130, 880, 175], radius=10, fill="#0f172a")
    draw.text((455, 142), "2. DIAGNÓSTICO & ESQUEMA DUPLO", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([455, 190, 865, 340], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((465, 200), "Padrão-Ouro: NAAT Molecular (PCR)", fill="#0f172a", font=get_font(14, bold=True))
    draw.text((465, 226), "• Teste de Amplificação de Ácidos Nucleicos (NAAT)\n• Sensibilidade > 95% e especificidade > 98%\n• Coleta: Swab vaginal autocoletado, swab endocervical ou\n  primeira fração de urina (primeiro jato de 20-30 mL sem urinar há 1h)\n• Não aguardar resultado para iniciar tratamento empírico!", fill="#334155", font=get_font(12))

    draw.rounded_rectangle([455, 360, 865, 590], radius=8, fill="#f0fdf4", outline="#bbf7d0")
    draw.text((465, 370), "Terapia Dupla Empírica Imediata (CDC 2021)", fill="#166534", font=get_font(14, bold=True))
    draw.text((465, 396), "1. Cobertura de Gonococo:\n   • Ceftriaxona 500 mg IM em dose única profunda\n   • Se paciente com peso >= 150 kg: Ceftriaxona 1 g IM\n   • Se faríngeo: Ceftriaxona obrigatória!\n\n2. Cobertura de Clamídia:\n   • Doxiciclina 100 mg VO 12/12h por 7 dias (1ª linha CDC)\n   • Se GESTANTE: Azitromicina 1 g VO em dose única\n     (Doxiciclina contraindicada por toxicidade dentária/óssea)", fill="#14532d", font=get_font(12))

    draw.rounded_rectangle([455, 610, 865, 830], radius=8, fill="#fefce8", outline="#fef08a")
    draw.text((465, 620), "Mycoplasma genitalium: Alerta Emergente", fill="#854d0e", font=get_font(14, bold=True))
    draw.text((465, 646), "• Causa de cervicite persistente e DIP refratária\n• Sem parede celular (resistente a beta-lactâmicos) e com mutações a macrolídeos\n• Tratamento sequencial guiado:\n  Doxiciclina 100 mg 12/12h por 7 dias seguida de Moxifloxacino 400 mg por 7 dias.", fill="#713f12", font=get_font(12))

    # Coluna 3: Manejo de Parceiros (EPT)
    draw.rounded_rectangle([900, 130, 1320, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([900, 130, 1320, 175], radius=10, fill="#1d4ed8")
    draw.text((915, 142), "3. PARCEIROS & EPT (CDC / ACOG)", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([915, 190, 1305, 520], radius=8, fill="#eff6ff", outline="#bfdbfe")
    draw.text((925, 200), "Expedited Partner Therapy (EPT)", fill="#1e3a8a", font=get_font(14, bold=True))
    draw.text((925, 226), "• Notificar e tratar TODOS os parceiros sexuais com\n  quem a paciente teve contato nos ÚLTIMOS 60 DIAS.\n\n• O médico fornece prescrição ou antibióticos diretamente\n  para a paciente entregar ao parceiro, SEM necessidade\n  de exame médico presencial prévio do parceiro!\n\n• Estratégia de alto impacto em saúde pública que quebra\n  a cadeia de transmissão e evita reinfecção na paciente.\n\n• Abstinência sexual estrita por 7 dias após o início\n  do tratamento de ambos.\n\n• Repetir NAAT após 3 meses (teste de reinfecção).", fill="#1e40af", font=get_font(12))

    draw.rounded_rectangle([915, 540, 1305, 830], radius=8, fill="#fef2f2", outline="#fecaca")
    draw.text((925, 550), "⚠️ Sequelas Graves da Falha de Tratamento", fill="#991b1b", font=get_font(14, bold=True))
    draw.text((925, 576), "A cervicite não tratada ascende em até 20% das mulheres:\n• Doença Inflamatória Pélvica (DIP)\n• Abscesso Tubo-Ovariano e Peritonite\n• Infertilidade tubária irreversível (oclusão das tubas)\n• Gestação ectópica (risco aumentado em 6 a 10 vezes)\n• Dor pélvica crônica incapacitante\n• No recém-nascido: conjuntivite neonatal hiperaguda e pneumonia", fill="#7f1d1d", font=get_font(12))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "cervicites_gonococo_clamidia_ept.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 4. DIP & ABSCESSO TUBO-OVARIANO (M53)
# ==============================================================================
def create_diagram_dip_ato():
    W, H = 1350, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "DOENÇA INFLAMATÓRIA PÉLVICA (DIP) & ABSCESSO TUBO-OVARIANO (ATO)", "Critérios de Hager • Critérios de Internação • Tratamento Parenteral vs Drenagem")

    # Coluna 1: Critérios de Hager
    draw.rounded_rectangle([30, 130, 420, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 420, 175], radius=10, fill="#be123c")
    draw.text((45, 142), "1. CRITÉRIOS DE HAGER / CDC", fill="#ffffff", font=get_font(16, bold=True))

    crit_min = [
        ("Critérios Mínimos (Basta 1)", "Em mulher jovem sexualmente ativa com dor pélvica sem outra causa evidente:\n1. Dor à mobilização do colo (Chandelier Sign)\n2. Dor à palpação uterina\n3. Dor à palpação anexial (uni ou bilateral)\n* Iniciar tratamento empírico imediatamente!"),
        ("Critérios Adicionais (Especificidade)", "• Febre axilar > 38.3 °C (oral > 38.0 °C)\n• Secreção endocervical purulenta anormal\n• Leucócitos abundantes na microscopia salina\n• VHS ou PCR elevados no sangue\n• NAAT positivo para gonococo ou clamídia"),
        ("Critérios Definitivos (Raros)", "• Biópsia de endométrio com endometrite\n• USG transvaginal com sinal da roda dentada ou ATO\n• Laparoscopia com hiperemia tubária e exsudato")
    ]
    y = 190
    for title, desc in crit_min:
        draw.rounded_rectangle([45, y, 405, y + 195], radius=8, fill="#fff1f2", outline="#fecdd3")
        draw.text((55, y + 8), title, fill="#9f1239", font=get_font(13, bold=True))
        draw.text((55, y + 36), desc, fill="#4c0519", font=get_font(11))
        y += 210

    # Coluna 2: Critérios de Internação Hospitalar
    draw.rounded_rectangle([440, 130, 880, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([440, 130, 880, 175], radius=10, fill="#0f172a")
    draw.text((455, 142), "2. CRITÉRIOS DE INTERNAÇÃO", fill="#ffffff", font=get_font(16, bold=True))

    hosp_reasons = [
        ("1. Emergência Cirúrgica Não Excluída", "Apendicite aguda, torção anexial ou gravidez ectópica não descartadas."),
        ("2. Abscesso Tubo-Ovariano (ATO)", "Presença de massa complexa inflamatória anexial ao exame ou USG."),
        ("3. Gestação", "DIP na gravidez é raríssima e associada a desfechos obstétricos catastróficos."),
        ("4. Quadro Clínico Grave / Peritonite", "Febre alta (> 38.5 °C), náuseas e vômitos incoercíveis ou irritação peritoneal."),
        ("5. Falha do Tratamento Ambulatorial", "Ausência de resposta clínica consistente após 48 a 72 horas de terapia oral."),
        ("6. Imunossupressão ou Não Adesão", "HIV com CD4 baixo, incapacidade de ingerir ou seguir medicação ambulatorial.")
    ]
    y = 190
    for title, desc in hosp_reasons:
        draw.rounded_rectangle([455, y, 865, y + 90], radius=8, fill="#f8fafc", outline="#cbd5e1")
        draw.text((465, y + 6), title, fill="#0f172a", font=get_font(13, bold=True))
        draw.text((465, y + 28), desc, fill="#334155", font=get_font(11))
        y += 102

    # Coluna 3: Tratamento e ATO
    draw.rounded_rectangle([900, 130, 1320, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([900, 130, 1320, 175], radius=10, fill="#15803d")
    draw.text((915, 142), "3. ESQUEMAS ATB & MANEJO DO ATO", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([915, 190, 1305, 410], radius=8, fill="#f0fdf4", outline="#bbf7d0")
    draw.text((925, 200), "Esquemas Antimicrobianos (14 Dias)", fill="#166534", font=get_font(14, bold=True))
    draw.text((925, 226), "Ambulatorial (Leve/Moderado):\n• Ceftriaxona 500 mg IM dose única +\n  Doxiciclina 100 mg 12/12h + Metronidazol 500 mg 12/12h 14d.\n  (Reavaliar obrigatoriamente em 48-72h!)\n\nHospitalar (Parenteral):\n• Opção A: Cefoxitina 2 g IV 6/6h + Doxiciclina 100 mg VO/IV 12/12h\n• Opção B (Excelente para ATO): Clindamicina 900 mg IV 8/8h +\n  Gentamicina IV (dose ataque 2 mg/kg, manutenção 1.5 mg/kg 8/8h)", fill="#14532d", font=get_font(11))

    draw.rounded_rectangle([915, 430, 1305, 830], radius=8, fill="#fef2f2", outline="#fecaca")
    draw.text((925, 440), "Manejo Específico do ATO", fill="#991b1b", font=get_font(14, bold=True))
    draw.text((925, 466), "• ATO Íntegro (Estável):\n  Antibioticoterapia parenteral hospitalar inicial (70-80% respondem).\n\n• Falha após 48-72h de ATB ou Tamanho > 8 cm:\n  DRENAGEM PERCUTÂNEA GUIADA POR TC OU USG!\n  Procedimento minimamente invasivo que preserva fertilidade.\n\n• ATO Roto (Choque Séptico / Abdome em Tábua):\n  EMERGÊNCIA CIRÚRGICA VITAL!\n  Laparotomia exploradora de urgência imediata com lavagem peritoneal.", fill="#7f1d1d", font=get_font(12))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "dip_fisiopatologia_hager_ato.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 5. SÍNDROME DE FITZ-HUGH-CURTIS & SEQUELAS (M53.5)
# ==============================================================================
def create_diagram_fitz_hugh_curtis():
    W, H = 1300, 880
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "SÍNDROME DE FITZ-HUGH-CURTIS & SEQUELAS REPRODUTIVAS DA DIP", "Peri-hepatite • Aderências em Cordas de Violino • Risco de Infertilidade e Ectópica")

    # Painel Esquerdo: Fitz-Hugh-Curtis
    draw.rounded_rectangle([30, 130, 630, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 630, 175], radius=10, fill="#0f172a")
    draw.text((45, 142), "SÍNDROME DE FITZ-HUGH-CURTIS (PERI-HEPATITE)", fill="#ffffff", font=get_font(16, bold=True))

    fhc_points = [
        ("Definição e Fisiopatologia", "Ocorre em 5 a 15% das mulheres com DIP por disseminação transcelômica peritoneal de Chlamydia trachomatis ou N. gonorrhoeae pela goteira parietocólica direita até a cápsula de Glisson hepática."),
        ("Quadro Clínico Típico", "Dor aguda intensa em hipocôndrio direito, pleurítica, que piora na inspiração profunda ou tosse, simulando colecistite aguda, pleurite ou abscesso subfrênico."),
        ("Laboratório (Pegadinha Clássica de Prova!)", "As enzimas hepáticas (AST/ALT) estão NORMAIS OU DISCRETAMENTE ELEVADAS! A inflamação atinge apenas a cápsula peritoneal hepática superficial, sem causar necrose de hepatócitos."),
        ("Achado Cirúrgico Patognomônico", "Na videolaparoscopia: presença de aderências fibrosas delgadas entre a face anterior do fígado e o peritônio diafragmático em 'CORDAS DE VIOLINO' (violin-string adhesions).")
    ]
    y = 190
    for title, desc in fhc_points:
        draw.rounded_rectangle([45, y, 615, y + 140], radius=8, fill="#eff6ff", outline="#bfdbfe")
        draw.text((55, y + 8), title, fill="#1e3a8a", font=get_font(13, bold=True))
        draw.text((55, y + 34), desc, fill="#1e40af", font=get_font(11))
        y += 152

    # Painel Direito: Sequelas Reprodutivas
    draw.rounded_rectangle([660, 130, 1270, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([660, 130, 1270, 175], radius=10, fill="#be123c")
    draw.text((675, 142), "SEQUELAS REPRODUTIVAS PERMANENTES DA DIP", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([675, 190, 1255, 410], radius=8, fill="#fff1f2", outline="#fecdd3")
    draw.text((685, 200), "Risco Cumulativo de Infertilidade por Fator Tubário", fill="#881337", font=get_font(14, bold=True))
    draw.text((685, 226), "A destruição inflamatória dos cílios da mucosa tubária e a formação de\nsinéquias intraluminais causam infertilidade de forma exponencial:\n\n• Após 1º episódio de DIP: ~8% de risco de infertilidade\n• Após 2º episódio de DIP: ~20% de risco de infertilidade\n• Após 3º episódio de DIP: > 40% de risco de infertilidade permanente!\n\nPor isso, o início do tratamento antimicrobiano empírico NÃO pode ser atrasado!", fill="#4c0519", font=get_font(12))

    draw.rounded_rectangle([675, 430, 1255, 620], radius=8, fill="#fdf2f8", outline="#fbcfe8")
    draw.text((685, 440), "Gravidez Ectópica Tubária", fill="#831843", font=get_font(14, bold=True))
    draw.text((685, 466), "• O risco de gestação ectópica aumenta em 6 a 10 vezes após DIP!\n• O embrião fecundado não consegue trafegar pelos cílios lesados e\n  implanta-se na parede da tuba uterina (risco de rotura e hemoperitônio).", fill="#701a75", font=get_font(12))

    draw.rounded_rectangle([675, 640, 1255, 805], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((685, 650), "Dor Pélvica Crônica (DPC)", fill="#0f172a", font=get_font(14, bold=True))
    draw.text((685, 676), "• Desenvolve-se em até 30% das pacientes após salpingite aguda.\n• Decorrente de aderências peritoneais pélvicas densas e sensibilização neural.", fill="#334155", font=get_font(12))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "sindrome_fitz_hugh_curtis_sequelas.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 6. SÍFILIS: ESTADIAMENTO, SOROLOGIA & GESTAÇÃO (M54)
# ==============================================================================
def create_diagram_sifilis():
    W, H = 1400, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "SÍFILIS: ESTADIAMENTO CLÍNICO, SOROLOGIAS & DESSENSIBILIZAÇÃO", "Treponema pallidum • Testes Treponêmicos vs VDRL • Regra de Ouro na Gestação")

    # Coluna 1: Estágios Clínicos
    draw.rounded_rectangle([30, 130, 440, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 440, 175], radius=10, fill="#0f172a")
    draw.text((45, 142), "1. ESTÁGIOS DA SÍFILIS", fill="#ffffff", font=get_font(16, bold=True))

    stages = [
        ("Sífilis Primária (10-90 dias)", "CANCRO DURO: Úlcera única, INDOLOR, base limpa cartilaginosa, bordas elevadas nítidas. Adenopatia inguinal indolor não supurativa. Cicatriza em 3-6 semanas."),
        ("Sífilis Secundária (4-10 sem pós-cancro)", "Disseminação hematogênica: Roséola sifilítica, exantema maculopapular (PALMAS E PLANTAS!), condiloma lata (lesões vegetantes úmidas highly infectantes) e micropoliadenopatia."),
        ("Sífilis Latente (Assintomática)", "• Precoce: < 1 ano de infecção (alta infectividade)\n• Tardia: > 1 ano ou duração desconhecida"),
        ("Sífilis Terciária (Anos pós-infecção)", "Gomas sifilíticas destrutivas, aneurisma de aorta ascendente e neurossífilis parenquimatosa (Tabes dorsalis, pupila de Argyll Robertson).")
    ]
    y = 190
    for title, desc in stages:
        draw.rounded_rectangle([45, y, 425, y + 140], radius=8, fill="#eff6ff", outline="#bfdbfe")
        draw.text((55, y + 8), title, fill="#1e3a8a", font=get_font(13, bold=True))
        draw.text((55, y + 34), desc, fill="#1e40af", font=get_font(11))
        y += 152

    # Coluna 2: Sorologias & Interpretação
    draw.rounded_rectangle([460, 130, 900, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([460, 130, 900, 175], radius=10, fill="#be123c")
    draw.text((475, 142), "2. SOROLOGIAS: TNT VS TREPONÊMICOS", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([475, 190, 885, 390], radius=8, fill="#fdf2f8", outline="#fbcfe8")
    draw.text((485, 200), "Testes Não Treponêmicos (VDRL / RPR)", fill="#831843", font=get_font(14, bold=True))
    draw.text((485, 226), "• Detectam anticorpos anticardiolipina\n• Semiquantitativos (títulos: 1:1, 1:2, 1:4, 1:8, 1:16, 1:32...)\n• UTILIZADOS PARA CONTROLE DE CURA: Sucesso é queda\n  de pelo menos 4 vezes (2 diluições) em 3 a 6 meses\n• Fenômeno de Prozona: excesso de anticorpos gera falso-negativo;\n  se suspeita alta, solicitar diluição da amostra!", fill="#701a75", font=get_font(11))

    draw.rounded_rectangle([475, 410, 885, 600], radius=8, fill="#f0fdf4", outline="#bbf7d0")
    draw.text((485, 420), "Testes Treponêmicos (FTA-ABS / TR / ELISA)", fill="#166534", font=get_font(14, bold=True))
    draw.text((485, 446), "• Detectam anticorpos específicos contra antígenos do T. pallidum\n• Primeiros a positivar na sífilis primária (1-2 semanas pós-contato)\n• CICATRIZ SOROLÓGICA PERENE: Permanecem reagentes pelo\n  resto da vida em ~85% dos pacientes curados (não avaliam cura!).", fill="#14532d", font=get_font(11))

    draw.rounded_rectangle([475, 620, 885, 830], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((485, 630), "Esquemas Padrão de Penicilina Benzatina", fill="#0f172a", font=get_font(14, bold=True))
    draw.text((485, 654), "• Primária, Secundária ou Latente Precoce (< 1 ano):\n  Penicilina G Benzatina 2.4 milhões de UI IM dose única\n\n• Latente Tardia (> 1 ano), Duração Desconhecida ou Terciária:\n  Penicilina G Benzatina 2.4 milhões de UI IM/semana por 3 semanas\n  (Dose cumulativa: 7.2 milhões de UI)", fill="#334155", font=get_font(11))

    # Coluna 3: Sífilis na Gestação & Alergia
    draw.rounded_rectangle([920, 130, 1370, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([920, 130, 1370, 175], radius=10, fill="#be123c")
    draw.text((935, 142), "3. REGRA DE OURO NA GESTAÇÃO", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([935, 190, 1355, 520], radius=8, fill="#fee2e2", outline="#fca5a5")
    draw.text((945, 200), "DESSENSIBILIZAÇÃO OBRIGATÓRIA!", fill="#991b1b", font=get_font(15, bold=True))
    draw.text((945, 228), "A Penicilina Benzatina é o ÚNICO medicamento capaz de\natravessar a barreira transplacentária e tratar o concepto,\nprevenindo a sífilis congênita (mortalidade fetal até 40%).\n\nSe a gestante tiver história comprovada de anafilaxia:\n• NÃO usar Doxiciclina (contraindicada na gestação!)\n• NÃO usar Azitromicina (alta taxa de resistência treponêmica\n  e falha transplacentária)\n\nCONDUTA MANDATÓRIA:\nInternação hospitalar monitorizada e DESSENSIBILIZAÇÃO\nORAL À PENICILINA com doses crescentes a cada 15 min,\nseguida imediatamente pela dose plena de Penicilina Benzatina!", fill="#7f1d1d", font=get_font(12))

    draw.rounded_rectangle([935, 540, 1355, 830], radius=8, fill="#eff6ff", outline="#bfdbfe")
    draw.text((945, 550), "Reação de Jarisch-Herxheimer", fill="#1e3a8a", font=get_font(14, bold=True))
    draw.text((945, 576), "• Reação febril aguda de 2 a 24 horas pós-dose de penicilina\n• Febre, calafrios, mialgia por lise massiva de espiroquetas\n• Na gestante: pode desencadear contrações uterinas transitórias\n• CONDUTA: Sintomáticos (paracetamol) e hidratação.\n  NÃO É ALERGIA! Não suspender nem contraindicar a penicilina.", fill="#1e40af", font=get_font(12))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "sifilis_estadiamento_sorologia_gestacao.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 7. ÚLCERAS GENITAIS: MATRIZ DIFERENCIAL (M55)
# ==============================================================================
def create_diagram_ulceras_genitais():
    W, H = 1400, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "MATRIZ DIFERENCIAL COMPLETA DAS ÚLCERAS GENITAIS", "Sífilis vs Herpes vs Cancro Mole vs Linfogranuloma Venéreo vs Donovanose")

    ulcers = [
        ("Sífilis Primária", "#1e293b", "#eff6ff", "#1e3a8a", [
            ("Patógeno", "Treponema pallidum (espiroqueta)."),
            ("Número de Lesões", "Única (geralmente)."),
            ("Dor na Úlcera?", "INDOLOR (não dói nada)."),
            ("Base e Bordas", "Base limpa avermelhada, bordas endurecidas nítidas 'cartilaginosas'."),
            ("Adenopatia Inguinal", "Bilateral, indolor, múltiplos linfonodos firmes, SEM SUPURAÇÃO."),
            ("Tratamento 1ª Linha", "Penicilina G Benzatina 2.4 mi UI IM dose única.")
        ]),
        ("Herpes Genital", "#7c2d12", "#fff7ed", "#9a3412", [
            ("Patógeno", "Herpes Simplex Virus (HSV-1 / HSV-2)."),
            ("Número de Lesões", "Múltiplas vesículas que se rompem em úlceras rasas agrupadas."),
            ("Dor na Úlcera?", "MUITO DOLOROSA (ardência/queimação excruciante)."),
            ("Base e Bordas", "Base eritematosa com crostas tardias, bordas policíclicas finas."),
            ("Adenopatia Inguinal", "Bilateral, dolorosa, firme, NÃO FISTULIZA."),
            ("Tratamento 1ª Linha", "Valaciclovir 1g VO 12/12h 7-10d (Aciclovir 400 mg 3x/dia).")
        ]),
        ("Cancro Mole", "#be123c", "#fff1f2", "#9f1239", [
            ("Patógeno", "Haemophilus ducreyi (cocobacilo Gram-negativo)."),
            ("Número de Lesões", "Múltiplas úlceras (por autoinoculação)."),
            ("Dor na Úlcera?", "EXTREMAMENTE DOLOROSA."),
            ("Base e Bordas", "Fundo sujo purulento/necrótico, friável, sangra fácil, bordas descoladas."),
            ("Adenopatia Inguinal", "Unilateral (50%), volumosa, inflamatória, FISTULIZA POR ORIFÍCIO ÚNICO."),
            ("Tratamento 1ª Linha", "Azitromicina 1g VO dose única (ou Ceftriaxona 250 mg IM).")
        ]),
        ("Linfogranuloma Venéreo", "#047857", "#ecfdf5", "#064e3b", [
            ("Patógeno", "Chlamydia trachomatis sorotipos L1, L2, L3."),
            ("Número de Lesões", "Pápula/úlcera minúscula e fugaz (passa despercebida)."),
            ("Dor na Úlcera?", "INDOLOR."),
            ("Base e Bordas", "Pequena e superficial, cicatriza rapidamente sem deixar marca."),
            ("Adenopatia Inguinal", "SINAL DO SULCO (ligamento inguinal); FISTULIZA POR ORIFÍCIOS MÚLTIPLOS ('bico de regador')."),
            ("Tratamento 1ª Linha", "Doxiciclina 100 mg VO 12/12h por 21 dias consecutivos.")
        ]),
        ("Donovanose", "#4338ca", "#eef2ff", "#312e81", [
            ("Patógeno", "Klebsiella granulomatis (bastonete intracelular)."),
            ("Número de Lesões", "Lesão ulcerada expansiva crônica."),
            ("Dor na Úlcera?", "INDOLOR."),
            ("Base e Bordas", "Úlcera vegetante granulomatosa vermelha em 'carne viva', bordas em rolete."),
            ("Adenopatia Inguinal", "SEM ADENOPATIA VERDADEIRA (pode haver 'pseudobubão' subcutâneo)."),
            ("Tratamento 1ª Linha", "Azitromicina 1g VO 1x/semana por >= 3 semanas (até cicatrização completa).")
        ])
    ]

    col_w = 250
    x = 30
    for title, head_bg, card_bg, text_col, items in ulcers:
        draw.rounded_rectangle([x, 130, x + col_w, 850], radius=10, fill=card_bg, outline="#cbd5e1", width=2)
        draw.rounded_rectangle([x, 130, x + col_w, 175], radius=8, fill=head_bg)
        draw.text((x + 10, 144), title, fill="#ffffff", font=get_font(13, bold=True))

        cur_y = 190
        for item_label, item_desc in items:
            draw.text((x + 10, cur_y), item_label + ":", fill=text_col, font=get_font(11, bold=True))
            draw.text((x + 10, cur_y + 16), item_desc, fill="#334155", font=get_font(10))
            cur_y += 105

        x += col_w + 20

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "ulceras_genitais_matriz_diferencial.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 8. HERPES GENITAL & CONDUTA NO PARTO (M55.2)
# ==============================================================================
def create_diagram_herpes_parto():
    W, H = 1300, 880
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "HERPES GENITAL: FISIOPATOLOGIA, PROFILAXIA & CONDUTA NO PARTO", "HSV-1 e HSV-2 • Latência nos Gânglios Sacrais • Algoritmo Decisório no Parto")

    # Coluna 1: Virologia e Latência
    draw.rounded_rectangle([30, 130, 630, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 630, 175], radius=10, fill="#be123c")
    draw.text((45, 142), "1. VIROLOGIA, LATÊNCIA & RECORRÊNCIA", fill="#ffffff", font=get_font(16, bold=True))

    hsv_data = [
        ("HSV-1 vs HSV-2", "• HSV-2: responsável por 70-80% das infecções genitais recorrentes\n• HSV-1: frequentemente associado a contato orogenital; crescente em primoinfecções."),
        ("Mecanismo de Latência Neural", "Após o contágio mucoso, o vírus migra por transporte retrógrado axonal até os GÂNGLIOS NERVOSOS DA RAIZ DORSAL SACRAL (S2 a S4), onde permanece em latência vitalícia dentro dos neurônios sensoriais."),
        ("Dinâmica das Recorrências", "Estresse físico/emocional, imunodepressão e radiação reativam o vírus. As crises recorrentes são precedidas por PRÓDROMOS (formigamento, queimação neural ou parestesia vulvar horas antes das vesículas)."),
        ("Terapia Supressiva Crônica", "Valaciclovir 500 mg a 1g VO 1x/dia contínuo para quem tem >= 6 surtos/ano: reduz crises em 80% e transmissão ao parceiro suscetível em 50%.")
    ]
    y = 190
    for title, desc in hsv_data:
        draw.rounded_rectangle([45, y, 615, y + 140], radius=8, fill="#fff1f2", outline="#fecdd3")
        draw.text((55, y + 8), title, fill="#9f1239", font=get_font(13, bold=True))
        draw.text((55, y + 34), desc, fill="#4c0519", font=get_font(11))
        y += 152

    # Coluna 2: Protocolo Periparto
    draw.rounded_rectangle([660, 130, 1270, 820], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([660, 130, 1270, 175], radius=10, fill="#0f172a")
    draw.text((675, 142), "2. CONDUTA OBSTÉTRICA NO PERIPARTO (ACOG)", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([675, 190, 1255, 360], radius=8, fill="#eff6ff", outline="#bfdbfe")
    draw.text((685, 200), "Profilaxia Antiviral a Partir de 36 Semanas", fill="#1e3a8a", font=get_font(14, bold=True))
    draw.text((685, 226), "Em toda gestante com HISTÓRICO PRÉVIO de herpes genital:\n• Iniciar Aciclovir 400 mg VO 3x/dia OU Valaciclovir 500 mg VO 2x/dia\n  a partir de 36 semanas de gestação até o parto.\n• Objetivo: Suprimir o shedding viral assintomático e prevenir o\n  surgimento de lesões ativas no momento do parto, viabilizando o parto normal.", fill="#1e40af", font=get_font(12))

    draw.rounded_rectangle([675, 380, 1255, 590], radius=8, fill="#fee2e2", outline="#fca5a5")
    draw.text((685, 390), "Cenário 1: Lesão Ativa ou Pródromo no Parto", fill="#991b1b", font=get_font(14, bold=True))
    draw.text((685, 416), "🚨 CESARIANA IMEDIATA MANDATÓRIA!\n• Presença de vesículas, úlceras ou sintomas prodrômicos (queimação/ardor)\n  no momento do trabalho de parto ou rotura de membranas;\n• O parto vaginal é formalmente CONTRAINDICADO;\n• Evita o contato direto do neonato com o vírus ativo no canal de parto,\n  prevenindo o Herpes Neonatal disseminado (encefalite e óbito > 60%).", fill="#7f1d1d", font=get_font(12))

    draw.rounded_rectangle([675, 610, 1255, 805], radius=8, fill="#f0fdf4", outline="#bbf7d0")
    draw.text((685, 620), "Cenário 2: Ausência de Lesões e Sem Pródromos", fill="#166534", font=get_font(14, bold=True))
    draw.text((685, 646), "✅ PARTO VAGINAL TOTALMENTE PERMITIDO!\n• Exame físico perineal e vulvar minucioso sem lesões visíveis e assintomática;\n• A história prévia de herpes NÃO obriga cesariana quando não há lesão ativa!", fill="#14532d", font=get_font(12))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "herpes_genital_profilaxia_parto.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 9. HPV, RASTREAMENTO & BETHESDA (M56)
# ==============================================================================
def create_diagram_hpv_bethesda():
    W, H = 1400, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "HPV, ONCOGÊNESE, RASTREAMENTO & CLASSIFICAÇÃO BETHESDA", "Oncoproteínas E6 e E7 • Comparativo ASCCP (EUA) vs INCA (Brasil) • Conduta nas Lesões")

    # Coluna 1: Oncogênese & Vacina
    draw.rounded_rectangle([30, 130, 440, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 440, 175], radius=10, fill="#701a75")
    draw.text((45, 142), "1. BIOLOGIA MOLECULAR DO HPV", fill="#ffffff", font=get_font(16, bold=True))

    hpv_bio = [
        ("Tipos de Baixo Risco (6 e 11)", "Causam > 90% dos Condilomas Acuminados (verrugas genitais em crista de galo) e papilomatose respiratória. Não causam câncer invasor."),
        ("Tipos de Alto Risco (16 e 18)", "HPV 16 e 18 causam ~70% dos carcinomas cervicais mundiais. Outros: 31, 33, 45, 52, 58."),
        ("Oncoproteína E6 (Degrada p53)", "E6 liga-se à proteína p53 ('guardiã do genoma') e recruta a ubiquitina-ligase, degradando a p53 e bloqueando a apoptose celular."),
        ("Oncoproteína E7 (Inativa pRb)", "E7 liga-se à proteína pRb hipofosforilada, liberando o fator de transcrição E2F, forçando proliferação celular ininterrupta da fase S."),
        ("Vacina Gardasil 9", "Protege contra 9 genótipos (6, 11, 16, 18, 31, 33, 45, 52, 58). 9 a 14 anos (dose única no BR ou 2 doses nos EUA; imunodeprimidos 3 doses até 45a).")
    ]
    y = 190
    for title, desc in hpv_bio:
        draw.rounded_rectangle([45, y, 425, y + 115], radius=8, fill="#fdf4ff", outline="#f5d0fe")
        draw.text((55, y + 8), title, fill="#86198f", font=get_font(13, bold=True))
        draw.text((55, y + 32), desc, fill="#4a044e", font=get_font(11))
        y += 128

    # Coluna 2: Rastreamento ASCCP vs INCA
    draw.rounded_rectangle([460, 130, 900, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([460, 130, 900, 175], radius=10, fill="#0f172a")
    draw.text((475, 142), "2. RASTREAMENTO: EUA VS BRASIL", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([475, 190, 885, 410], radius=8, fill="#eff6ff", outline="#bfdbfe")
    draw.text((485, 200), "Diretriz EUA (USPSTF / ASCCP)", fill="#1e3a8a", font=get_font(14, bold=True))
    draw.text((485, 226), "• Início: 21 anos (independentemente da sexarca)\n• 21 a 29 anos: Citologia a cada 3 anos (sem teste de HPV)\n• 30 a 65 anos:\n  - Teste primário de HPV de alto risco a cada 5 anos (preferível) OU\n  - Coteste (Citologia + HPV) a cada 5 anos OU\n  - Citologia isolada a cada 3 anos\n• Interrupção: 65 anos se rastreamento prévio adequado nos últimos 10 anos.", fill="#1e40af", font=get_font(11))

    draw.rounded_rectangle([475, 430, 885, 650], radius=8, fill="#f0fdf4", outline="#bbf7d0")
    draw.text((485, 440), "Diretriz Brasil (INCA / Ministério da Saúde)", fill="#166534", font=get_font(14, bold=True))
    draw.text((485, 466), "• Início: 25 anos (mulheres com atividade sexual)\n• 25 a 64 anos: Citologia anual; após 2 exames normais consecutivos,\n  passar para intervalo de 3 em 3 anos.\n• Interrupção: 64 anos com pelo menos dois exames negativos nos últimos 5 anos.\n* SUS incorporando progressivamente o teste de DNA de HPV.", fill="#14532d", font=get_font(11))

    draw.rounded_rectangle([475, 670, 885, 830], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((485, 680), "Condiloma Acuminado na Gravidez", fill="#0f172a", font=get_font(13, bold=True))
    draw.text((485, 704), "• Ácido Tricloroacético (ATA 80-90%): SEGURO e método de escolha!\n• Imiquimode e podofilotoxina são contraindicados na gravidez.\n• NÃO indica cesariana exceto se obstruir canal ou risco hemorrágico.", fill="#334155", font=get_font(11))

    # Coluna 3: Conduta em Bethesda
    draw.rounded_rectangle([920, 130, 1370, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([920, 130, 1370, 175], radius=10, fill="#be123c")
    draw.text((935, 142), "3. CONDUTA NAS ANORMALIDADES", fill="#ffffff", font=get_font(16, bold=True))

    bethesda_rules = [
        ("ASC-US (Significado Indeterminado)", "Repetir citologia em 12 meses (se jovem) OU COLPOSCOPIA IMEDIATA se >= 30 anos ou HPV de alto risco positivo."),
        ("LSIL (Baixo Grau / NIC 1)", "Conduta conservadora: Repetir citologia em 6 meses (Brasil) ou Colposcopia direta se >= 25 anos com HPV+ (EUA). Alta regressão espontânea."),
        ("ASC-H (Não Exclui Alto Grau)", "COLPOSCOPIA IMEDIATA OBRIGATÓRIA. Alto risco de lesão pré-neoplásica grave oculta (NIC 2/3)."),
        ("HSIL (Alto Grau / NIC 2/3)", "COLPOSCOPIA COM BIÓPSIA DIRIGIDA OBRIGATÓRIA (opção 'ver e tratar' com LEEP em > 25 anos nos EUA)."),
        ("AGC (Células Glandulares Atípicas)", "COLPOSCOPIA + AVALIAÇÃO ENDOCERVICAL + BIÓPSIA DE ENDOMÉTRIO (se >= 35 anos ou com risco endometrial)."),
        ("NIC 2 e NIC 3 Histológicas", "Excisão da Zona de Transformação (CAF/LEEP) ou Conização a frio (se ZT tipo 3 ou suspeita de invasão).")
    ]
    y = 190
    for title, desc in bethesda_rules:
        draw.rounded_rectangle([935, y, 1355, y + 95], radius=8, fill="#fff1f2", outline="#fecdd3")
        draw.text((945, y + 6), title, fill="#9f1239", font=get_font(12, bold=True))
        draw.text((945, y + 26), desc, fill="#4c0519", font=get_font(10))
        y += 105

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "hpv_oncogenese_rastreamento_bethesda.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

# ==============================================================================
# 10. HIV: TRANSMISSÃO VERTICAL, PEP & PREP (M57)
# ==============================================================================
def create_diagram_hiv():
    W, H = 1350, 900
    im = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(im)
    
    draw_header(draw, W, "HIV: TRANSMISSÃO VERTICAL, VIA DE PARTO, PEP & PREP", "Protocolo de Carga Viral 34-36 Semanas • Zidovudina Intraparto • Janela de Ouro PEP")

    # Coluna 1: Prevenção da Transmissão Vertical no Parto
    draw.rounded_rectangle([30, 130, 440, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([30, 130, 440, 175], radius=10, fill="#be123c")
    draw.text((45, 142), "1. VIA DE PARTO & CARGA VIRAL", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([45, 190, 425, 410], radius=8, fill="#f0fdf4", outline="#bbf7d0")
    draw.text((55, 200), "Carga Viral < 1.000 cópias/mL (34-36 sem)", fill="#166534", font=get_font(14, bold=True))
    draw.text((55, 226), "✅ PARTO VAGINAL PERMITIDO!\n• Se condições obstétricas favoráveis;\n• Se Carga Viral indetectável (< 50 cópias), não é necessário\n  AZT venoso durante o trabalho de parto;\n• Se entre 50 e 999 cópias: AZT venoso contínuo durante o trabalho de parto.", fill="#14532d", font=get_font(12))

    draw.rounded_rectangle([45, 430, 425, 680], radius=8, fill="#fee2e2", outline="#fca5a5")
    draw.text((55, 440), "Carga Viral >= 1.000 cópias ou Desconhecida", fill="#991b1b", font=get_font(14, bold=True))
    draw.text((55, 466), "🚨 CESARIANA ELETIVA PROGRAMADA!\n• Realizar na 38ª semana de gestação (com bolsa íntegra e antes do início do TP);\n• AZT (Zidovudina) Endovenoso Contínuo obrigatório, iniciado 3 HORAS ANTES DA INCISÃO cirúrgica até o clampeamento imediato do cordão umbilical.", fill="#7f1d1d", font=get_font(12))

    draw.rounded_rectangle([45, 700, 425, 830], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((55, 710), "Cuidados no Recém-Nascido", fill="#0f172a", font=get_font(13, bold=True))
    draw.text((55, 734), "• Clampeamento imediato do cordão (sem ordenha)\n• Banho imediato e aspiração delicada se necessária\n• Profilaxia antiviral oral com AZT iniciada nas primeiras 4 horas", fill="#334155", font=get_font(11))

    # Coluna 2: Amamentação & Lactação
    draw.rounded_rectangle([460, 130, 890, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([460, 130, 890, 175], radius=10, fill="#0f172a")
    draw.text((465, 142), "2. CONTRAINDICAÇÃO DE AMAMENTAÇÃO", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([475, 190, 875, 460], radius=8, fill="#fee2e2", outline="#fca5a5")
    draw.text((485, 200), "AMAMENTAÇÃO ABSOLUTAMENTE PROIBIDA!", fill="#991b1b", font=get_font(15, bold=True))
    draw.text((485, 228), "No Brasil e nos EUA, o aleitamento materno por puérpera\nvivendo com HIV é FORMALMENTE CONTRAINDICADO,\nindependentemente da carga viral ser indetectável!\n\n• O aleitamento acrescenta risco de 15 a 20% de transmissão vertical;\n• O SUS fornece gratuitamente toda a fórmula infantil necessária até pelo menos 6 meses de vida;\n• Também é proibido o aleitamento cruzado (doação de leite de outra mulher sem pasteurização).", fill="#7f1d1d", font=get_font(12))

    draw.rounded_rectangle([475, 480, 875, 680], radius=8, fill="#fdf2f8", outline="#fbcfe8")
    draw.text((485, 490), "Inibição Farmacológica da Lactação", fill="#831843", font=get_font(14, bold=True))
    draw.text((485, 516), "• Prescrever imediatamente nas primeiras 24h pós-parto:\n  Cabergolina 1.0 mg VO em dose única (2 cp de 0.5 mg)\n• Inibe a liberação de prolactina pela hipófise e interrompe\n  a apojadura láctea sem necessidade de enfaixamento doloroso.", fill="#701a75", font=get_font(12))

    draw.rounded_rectangle([475, 700, 875, 830], radius=8, fill="#f8fafc", outline="#cbd5e1")
    draw.text((485, 710), "TARV Universal na Gestação", fill="#0f172a", font=get_font(13, bold=True))
    draw.text((485, 734), "• Iniciar TARV tríplice imediatamente (TDF + 3TC + DTG) para todas as gestantes, independentemente do CD4 ou idade gestacional.", fill="#334155", font=get_font(11))

    # Coluna 3: PEP & PrEP
    draw.rounded_rectangle([910, 130, 1320, 850], radius=12, fill="#ffffff", outline="#cbd5e1", width=2)
    draw.rounded_rectangle([910, 130, 1320, 175], radius=10, fill="#15803d")
    draw.text((925, 142), "3. PROFILAXIA: PEP & PREP", fill="#ffffff", font=get_font(16, bold=True))

    draw.rounded_rectangle([925, 190, 1305, 510], radius=8, fill="#eff6ff", outline="#bfdbfe")
    draw.text((935, 200), "PEP (Profilaxia Pós-Exposição)", fill="#1e3a8a", font=get_font(14, bold=True))
    draw.text((935, 226), "• JANELA DE OURO: Iniciar o mais rápido possível,\n  idealmente em até 2 horas e MÁXIMO DE 72 HORAS\n  após a relação desprotegida ou violência sexual.\n\n• DURAÇÃO: 28 dias ininterruptos.\n\n• Esquema Padrão (Brasil e CDC):\n  Tenofovir (TDF 300 mg) + Lamivudina (3TC 300 mg) +\n  Dolutegravir (DTG 50 mg) 1 comprimido 1x/dia.\n\n• Testagem rápida tempo zero e controle sorológico com 30 e 90 dias.", fill="#1e40af", font=get_font(12))

    draw.rounded_rectangle([925, 530, 1305, 830], radius=8, fill="#f0fdf4", outline="#bbf7d0")
    draw.text((935, 540), "PrEP (Profilaxia Pré-Exposição)", fill="#166534", font=get_font(14, bold=True))
    draw.text((935, 566), "• Uso contínuo diário: TDF 300 mg + FTC 200 mg (Truvada)\n• Indicada para populações com risco substancial de HIV\n• Pré-requisitos mandatórios antes do início:\n  - Documentação de HIV negativo recente\n  - Clearance de Creatinina > 60 mL/min\n  - Status sorológico de Hepatite B verificado\n• Proteção > 99% na via sexual quando tomada com adesão.", fill="#14532d", font=get_font(12))

    draw_footer(draw, W, H)
    out_path = os.path.join(IMG_DIR, "hiv_prevencao_transmissao_vertical_pep.jpg")
    im.save(out_path, quality=95)
    print(f"[OK] Gerado: {out_path}")

def build_all():
    print("=== INICIANDO GERAÇÃO DOS 10 INFOGRÁFICOS DE INFECÇÕES GINECOLÓGICAS E ISTs ===")
    create_diagram_ecossistema_vaginal()
    create_diagram_vulvovaginites()
    create_diagram_cervicites()
    create_diagram_dip_ato()
    create_diagram_fitz_hugh_curtis()
    create_diagram_sifilis()
    create_diagram_ulceras_genitais()
    create_diagram_herpes_parto()
    create_diagram_hpv_bethesda()
    create_diagram_hiv()
    print("=== TODOS OS 10 INFOGRÁFICOS FORAM GERADOS COM SUCESSO! ===")

if __name__ == "__main__":
    build_all()
