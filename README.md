# 🏥 Infecções Ginecológicas e ISTs — Portal Médico Interativo (Parte 6)
### USMLE Step 2 CK / Step 3 • Residência Médica • FEBRASGO • Ministério da Saúde / SUS • CDC 2021/2024 • ACOG • ASCCP • INCA

Este repositório contém a aplicação web completa, dinâmica e interativa desenvolvida a partir do artefato **Guia de Obstetrícia e Ginecologia — Parte 6: Infecções Ginecológicas e ISTs (Módulos 50 ao 60)**.

O portal foi construído com arquitetura 100% *client-side* (HTML5, Tailwind CSS, JavaScript Vanilla e Lucide Icons), garantindo **zero dependências de servidor**, carregamento ultrarrápido e compatibilidade nativa com o **GitHub Pages**.

---

## 🚀 Como Fazer o Deploy no GitHub Pages

O portal já contém o arquivo `.nojekyll` na raiz e todos os caminhos relativos devidamente configurados.

### Opção 1: Via Terminal (Git CLI)
1. Abra o terminal na pasta do projeto:
   ```bash
   cd "c:\Users\Admin\Downloads\INTERNATO GO\site_infeccoes_ists"
   ```
2. Inicialize o repositório Git (caso ainda não tenha feito):
   ```bash
   git init
   git add .
   git commit -m "feat: Portal Interativo de Infecções Ginecológicas e ISTs (Parte 6)"
   ```
3. Crie um novo repositório no seu GitHub (exemplo: `site-infeccoes-ists`) e vincule o *remote*:
   ```bash
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/site-infeccoes-ists.git
   git push -u origin main
   ```
4. No GitHub, vá em **Settings** > **Pages**:
   - Em **Source**, selecione a branch `main` e a pasta `/ (root)`.
   - Clique em **Save**.
   - O seu site estará no ar em poucos segundos em: `https://SEU_USUARIO.github.io/site-infeccoes-ists/`.

### Opção 2: Via Upload no GitHub (Interface Web)
1. Crie um novo repositório no GitHub.
2. Arraste e solte todos os arquivos da pasta `site_infeccoes_ists` (incluindo o arquivo `.nojekyll`, `index.html` e a pasta `assets/`).
3. Confirme o commit e ative o GitHub Pages em **Settings** > **Pages** selecionando a branch `main` / `root`.

---

## 🔬 Conteúdo dos Módulos Clínicos (50 ao 60)

- **Módulo 50: O Ecossistema Vaginal Normal e o Exame a Fresco**
  - Flora de Döderlein (*Lactobacillus crispatus*, *L. jensenii*), produção de glicogênio e ácido lático (pH fisiológico 3.8 a 4.5).
  - Procedimento passo a passo do exame a fresco (*Wet Mount*): lâmina com salina 0.9%, KOH 10% (Whiff test) e fita reativa de pH.
- **Módulo 51: As Grandes Vulvovaginites**
  - Matriz diferencial completa: Vaginose Bacteriana (Critérios de Amsel & Nugent), Candidíase Vulvovaginal e Tricomoníase Vaginal.
  - Atualização CDC 2021: Metronidazol 500 mg 12/12h por 7 dias para tricomoníase (superior à dose única de 2g).
  - Proscrição de fluconazol oral na gestação (risco teratogênico; uso estrito de azólicos tópicos por 7 dias).
  - Manejo de *Candida glabrata* com ácido bórico e vaginites atípicas (DIV, vaginose citolítica e atrofia).
- **Módulo 52: Cervicites, Gonorreia, Clamídia e Expedited Partner Therapy (EPT)**
  - Tropismo colunar endocervical, biologia do *Neisseria gonorrhoeae* e *Chlamydia trachomatis*.
  - Protocolo duplo: Ceftriaxona 500 mg IM (ajuste para **1 g IM se peso maternal &ge; 150 kg**) + Doxiciclina 100 mg 12/12h por 7 dias (ou Azitromicina 1g na gestante).
  - Regras de EPT cobrindo parceiros dos últimos 60 dias e abstinência por 7 dias.
- **Módulo 53: Doença Inflamatória Pélvica (DIP) e Abscesso Tubo-Ovariano (ATO)**
  - Patogênese polimicrobiana e Critérios de Hager (dor à mobilização do colo / *chandelier sign*).
  - Critérios mandatórios de internação hospitalar e regimes parenterais (Cefoxitina + Doxiciclina vs Clindamicina + Gentamicina).
  - Manejo de ATO íntegro (resposta clínica em 70-80% vs drenagem percutânea) e ATO roto (laparotomia exploradora de urgência).
- **Módulo 54: Síndrome de Fitz-Hugh-Curtis e Sequelas Reprodutivas**
  - Peri-hepatite transperitoneal, dor em hipocôndrio direito, transaminases normais e aderências em "cordas de violino".
  - Riscos cumulativos de infertilidade tubária permanente e gravidez ectópica.
- **Módulo 55: Sífilis na Prática Ginecológica e Obstétrica**
  - Estadiamento (primária, secundária, latente precoce/tardia e neurossífilis).
  - Testes treponêmicos e não treponêmicos, controle de cura por queda de 2 diluições no VDRL e efeito prozona.
  - **Dessensibilização hospitalar à penicilina oral obrigatória** em gestantes com alergia grave (a penicilina é o único tratamento fetal comprovado).
  - Reação de Jarisch-Herxheimer: suporte sintomático não alérgico.
- **Módulo 56: Matriz Diagnóstica Diferencial de Úlceras Genitais**
  - Algoritmo diferencial: Sífilis primária, Herpes simples genital, Cancro mole (*H. ducreyi*), Linfogranuloma venéreo e Donovanose.
- **Módulo 57: Herpes Genital na Gestação e Conduta no Parto**
  - Latência sacral S2-S4 e profilaxia antiviral com aciclovir a partir de 36 semanas.
  - Regra periparto ACOG/FEBRASGO: lesão ativa ou pródromo = **Cesariana Imediata Mandatória**; ausência de lesões = parto vaginal autorizado.
- **Módulo 58: HPV, Oncogênese e Rastreamento Cervical (ASCCP vs INCA)**
  - Mecanismos moleculares das oncoproteínas E6 (degradação de p53) e E7 (inativação de pRb).
  - Rastreamento cervical comparado (EUA 21-65 anos vs Brasil 25-64 anos).
  - Algoritmo Bethesda (ASC-US, LSIL, ASC-H, HSIL, AGC), colposcopia com ácido acético/Schiller e conduta com ATA em condilomas gestacionais.
- **Módulo 59: HIV na Mulher, Prevenção da Transmissão Vertical, PEP e PrEP**
  - Limiar de Carga Viral às 34-36 semanas (&lt; 1.000 vs &ge; 1.000 cópias/mL) para definição da via de parto e infusão de AZT venoso.
  - Contraindicação absoluta da amamentação materna no Brasil/EUA e inibição com cabergolina 1.0 mg.
  - Janela de ouro da PEP (&le; 72 horas por 28 dias com TDF + 3TC + DTG) e PrEP diária.
- **Módulo 60: High-Yield Master Matrix, Comunicação OSCE e Simulado com 15 Casos**
  - Roteiros OSCE para comunicação compassiva de diagnóstico de IST e HIV na gestação.
  - Simulado com 15 Vinhetas Clínicas completas estilo USMLE Step 2 CK / Residência Médica com gabarito comentado em tempo real.

---

## 📊 Suíte de 10 Infográficos Médicos em Alta Resolução

Localizados em `assets/img/`:
1. `ecossistema_vaginal_exame_a_fresco.jpg`: Microbiota normal, ácido lático e fluxograma do exame a fresco.
2. `vulvovaginites_matriz_comparativa.jpg`: Síndromes comparativas de VB, Candidíase e Tricomoníase.
3. `cervicites_gonococo_clamidia_ept.jpg`: Fisiopatologia endocervical, NAAT, ajuste ponderal e EPT.
4. `dip_fisiopatologia_hager_ato.jpg`: Ascensão polimicrobiana, critérios de Hager e manejo do ATO.
5. `sindrome_fitz_hugh_curtis_sequelas.jpg`: Rota transcelômica peritoneal, cordas de violino e riscos reprodutivos.
6. `sifilis_estadiamento_sorologia_gestacao.jpg`: Fases clínicas da sífilis, algoritmos diagnósticos e dessensibilização na gestação.
7. `ulceras_genitais_matriz_diferencial.jpg`: Diferenciação sindrômica de úlceras e bubões inguinais.
8. `herpes_genital_profilaxia_parto.jpg`: Latência sacral, profilaxia com 36 semanas e algoritmo periparto.
9. `hpv_oncogenese_rastreamento_bethesda.jpg`: Oncogênese E6/E7, diretrizes de rastreamento ASCCP/INCA e conduta em NIC.
10. `hiv_prevencao_transmissao_vertical_pep.jpg`: Limiar de carga viral no periparto, AZT venoso e janela de eficácia da PEP.

---

## 🛠️ Ferramentas Interativas e Motores Clínicos
1. **Simulador de Exame a Fresco**: Integra pH vaginal, Whiff test e microscopia óptica com retorno diagnóstico imediato.
2. **Calculadora de Critérios de Amsel e Nugent**: Diagnóstico objetivo de Vaginose Bacteriana.
3. **Estratificador de Candidíase**: Casos esporádicos vs recorrentes vs *C. glabrata* vs gestação (alerta de contraindicação do fluconazol oral).
4. **Calculadora de Cervicite & EPT**: Ajuste da dose de ceftriaxona por peso maternal (&ge; 150 kg) e regras de convocação de contatos.
5. **Escore de Internação em Doença Inflamatória Pélvica**: Identificação automática de critérios de gravidade e seleção de esquemas parenterais.
6. **Manejo de Sífilis & Dessensibilização**: Prescrição de penicilina benzatina e detecção de urgência obstétrica em gestantes alérgicas.
7. **Diferenciador de Úlceras Genitais**: Cruzamento de dor, número de lesões e fistulização de linfonodos.
8. **Conduta Bethesda / HPV**: Resolução de ASC-US, LSIL, ASC-H, HSIL e AGC com base nas diretrizes da ASCCP e do INCA.
9. **Calculadora de Transmissão Vertical do HIV no Parto**: Conduta imediata na via de parto e protocolo de AZT venoso conforme a carga viral.
10. **Rastreador de PEP e PrEP**: Validação da janela temporal de 72 horas para profilaxia pós-exposição.
11. **15 Flashcards 3D Interativos**: Repetição espaçada com efeito tridimensional de virada.
12. **Simulado Clínico Interativo**: 15 questões de nível USMLE Step 2 CK com pontuação dinâmica e gabarito detalhado.
13. **Lightbox HD**: Visualizador de imagens com zoom in/out, arrasto (pan) e tecla ESC.
