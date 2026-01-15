import os
import hashlib
from typing import Dict, Any, Tuple, Optional
from PIL import Image

import streamlit as st
from regras import carregar_regras, TEATROS_CONFIG

TIPOS_ARQUIVO_PERMITIDOS = ["jpg", "jpeg", "png"]
LOGO_MYWORK = "assets/comuns/logo_mywork_white.png"

MESSAGES = {
    "titulo_principal": "GIT - Validador de Formatos de Artes",
    "texto_intro": """
        **Olá, produtor Teatrali!**  
        Após criar as suas artes conforme o checklist, suba e veja os avisos do sistema: em vermelho delete.  
        Depois valide o formato das suas artes, até finalizar todas elas.  
        **Baixe o relatório e suba tudo no drive da sua atração.**
        
        Qualquer dúvida, fale com o Procópio e solicite o que precisar!
    """,
    "selecione_teatro": "Selecione o Teatro:",
    "selecione_gabarito": "Selecione o Gabarito:",
    "suba_arte": "Suba a sua Arte:",
    "aguardando_upload": "Aguardando upload...",
    "validar_arte": "Validar Formato da Arte",
    "gabarito_nao_encontrado": "Imagem de gabarito não encontrada em:",
    "nenhuma_regra": "Nenhuma regra encontrada para este teatro",
    "upload_antes_validar": "Por favor, faça o upload de uma arte antes de validar.",
    "arte_aprovada": "✅ ARTE APROVADA!",
    "arte_reprovada": "❌ ARTE REPROVADA!",
}

def renderizar_sidebar_painel() -> Tuple[str, Dict[str, Any], list, bool]:
    with st.sidebar:
        st.markdown("""
            <style>
                [data-testid="stSidebar"] [data-testid="stImage"] {
                    margin-top: -40px;
                }
                [data-testid="stSidebar"] [data-testid="stImage"] img {
                    width: 200px !important;
                }
                /* Style for Link Buttons to ensure black text */
                [data-testid="stLinkButton"] a {
                    color: black !important;
                    background-color: white !important;
                    border: 1px solid #e0e0e0 !important;
                }
                [data-testid="stLinkButton"] a:hover {
                    color: white !important;
                    background-color: black !important;
                    border-color: black !important;
                }
                /* Force Green Color for Primary Button in Sidebar */
                [data-testid="stSidebar"] button[kind="primary"], 
                [data-testid="stSidebar"] [data-testid="stButton"] button[kind="primary"] {
                    background-color: #28a745 !important;
                    border: 1px solid #28a745 !important;
                    color: #FFFFFF !important;
                }
                /* Force text inside the button to be white */
                [data-testid="stSidebar"] button[kind="primary"] p,
                [data-testid="stSidebar"] [data-testid="stButton"] button[kind="primary"] p {
                    color: #FFFFFF !important;
                }
                
                [data-testid="stSidebar"] button[kind="primary"]:hover,
                [data-testid="stSidebar"] [data-testid="stButton"] button[kind="primary"]:hover {
                    background-color: #218838 !important;
                    border-color: #218838 !important;
                    color: #FFFFFF !important;
                }
                [data-testid="stSidebar"] button[kind="primary"]:hover p,
                [data-testid="stSidebar"] [data-testid="stButton"] button[kind="primary"]:hover p {
                    color: #FFFFFF !important;
                }

                [data-testid="stSidebar"] button[kind="primary"]:focus:not(:active) {
                    background-color: #28a745 !important;
                    color: #FFFFFF !important;
                    border-color: #28a745 !important;
                    box-shadow: none !important;
                }
            </style>
        """, unsafe_allow_html=True)

        st.image(LOGO_MYWORK)
        st.header(MESSAGES["titulo_principal"])
        st.markdown("---")

        teatros_disponiveis = list(TEATROS_CONFIG.keys())
        
        # Tenta pegar teatro da URL
        teatro_url = st.query_params.get("teatro")
        
        # Mapping de Aliases (Proteção contra nomes diferentes vindo do frontend)
        if teatro_url == "ARTES": 
            teatro_url = "DAS_ARTES"
            
        idx_teatro = 0
        if teatro_url and teatro_url in teatros_disponiveis:
             idx_teatro = teatros_disponiveis.index(teatro_url)
             
        teatro_selecionado = st.selectbox(
            "1️⃣ " + MESSAGES["selecione_teatro"],
            options=teatros_disponiveis,
            index=idx_teatro
        )

        # Tenta pegar espetáculo da URL ou do Banco
        nome_espetaculo_auto = st.query_params.get("espetaculo", "")
        
        # Tenta buscar do Supabase (se configurado)
        try:
            from supabase_utils import buscar_producoes_ativas
            lista_producoes = buscar_producoes_ativas()
        except ImportError:
            lista_producoes = []

        if lista_producoes:
            # Se tiver lista, usa Selectbox
            idx_default = 0
            if nome_espetaculo_auto in lista_producoes:
                idx_default = lista_producoes.index(nome_espetaculo_auto)
                
            espetaculo_nome = st.selectbox(
                "2️⃣ Nome do Espetáculo (Para Histórico):",
                options=lista_producoes,
                index=idx_default,
                placeholder="Selecione o espetáculo..."
            )
        else:
            # Fallback para Input Manual
            espetaculo_nome = st.text_input(
                "2️⃣ Nome do Espetáculo (Para Histórico):", 
                value=nome_espetaculo_auto,
                placeholder="Ex: Os 3 Porquinhos"
            )

        regras_teatro = carregar_regras(teatro_selecionado)
        regra_selecionada: Dict[str, Any] = {}

        if not regras_teatro:
            st.error(MESSAGES["nenhuma_regra"])
        else:
            # Exibir checklist de referência no menu
            with st.expander("📋 Ver Lista de Formatos (Checklist)"):
                st.markdown("**Obrigatórios (Divertix / Site / Telas do Shopping):**")
                for k, v in regras_teatro.items():
                    if not k.startswith("banner_"):
                        st.markdown(f"- {v['descricao']}")
                
                st.markdown("**Especiais / Banners (Opcionais):**")
                for k, v in regras_teatro.items():
                    if k.startswith("banner_"):
                        st.markdown(f"- {v['descricao']}")

            # Opção de validação inteligente
            opcoes_gabarito = {"🔍 TODOS (Validação Automática)": "SMART_MODE"}
            # Adiciona regras individuais
            opcoes_gabarito.update({v["descricao"]: k for k, v in regras_teatro.items()})
            
            descricao_escolhida = st.selectbox(
                "3️⃣ " + MESSAGES["selecione_gabarito"],
                options=opcoes_gabarito.keys()
            )
            
            if descricao_escolhida:
                chave_regra = opcoes_gabarito[descricao_escolhida]
                if chave_regra == "SMART_MODE":
                    regra_selecionada = {
                        "is_smart_mode": True,
                        "descricao": "Validação Automática de Todos os Formatos",
                        "todas_regras": regras_teatro,
                        "orientacao": "vertical", # padrão
                        "teatro": teatro_selecionado,
                        "espetaculo": espetaculo_nome
                    }
                else:
                    regra_selecionada = regras_teatro[chave_regra]
                    regra_selecionada["is_smart_mode"] = False
                    regra_selecionada["teatro"] = teatro_selecionado
                    regra_selecionada["espetaculo"] = espetaculo_nome

        # Controle de estado para reset
        if "uploader_key" not in st.session_state:
            st.session_state["uploader_key"] = 0

        # Custom upload button that matches other buttons
        st.markdown("**4️⃣ Suba suas artes:**")
        st.markdown("""
            <style>
                /* Hide the default file uploader completely */
                [data-testid="stFileUploader"] {
                    display: none !important;
                }
                
                /* Custom upload button */
                .custom-upload-btn {
                    display: block;
                    width: 100%;
                    padding: 12px 20px;
                    background-color: #ffffff;
                    color: #000000;
                    border: 1px solid #cccccc;
                    border-radius: 5px;
                    text-align: center;
                    font-size: 16px;
                    font-weight: normal;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    margin-bottom: 1rem;
                }
                
                .custom-upload-btn:hover {
                    background-color: #000000;
                    color: #ffffff;
                    border-color: #000000;
                }
            </style>
            
            <button class="custom-upload-btn" onclick="document.querySelector('[data-testid=stFileUploader] input[type=file]').click()">
                ⬆ Upload
            </button>
        """, unsafe_allow_html=True)
        
        arquivos_carregados = st.file_uploader(
            MESSAGES["suba_arte"],
            type=TIPOS_ARQUIVO_PERMITIDOS,
            accept_multiple_files=True,
            key=f"uploader_{st.session_state['uploader_key']}",
            label_visibility="collapsed"
        )

        
        # Inicializa e filtra removidos
        if "removed_files" not in st.session_state:
            st.session_state["removed_files"] = set()
            
        arquivos_validos = []
        if arquivos_carregados:
            # Filtra usando nome E tamanho para permitir re-upload de arquivos corrigidos (mesmo nome, tamanho diferente)
            arquivos_validos = [a for a in arquivos_carregados if (a.name, a.size) not in st.session_state["removed_files"]]

        # Lista completa para contornar paginação do uploader nativo
        if arquivos_validos:
            st.markdown(f"**Total de arquivos: {len(arquivos_validos)}**")
            with st.expander("📂 Ver lista completa", expanded=False):
                unique_names = sorted({a.name for a in arquivos_validos})
                for name in unique_names:
                    st.markdown(f"📄 {name}")
        st.markdown("---")
        
        # Botão para acessar Drive de Artes (recebe link via URL ou Processo ID)
        link_drive_url = st.query_params.get("link_drive", "")
        processo_id_url = st.query_params.get("processo_id", "")
        
        link_final = None
        
        # 1. Prioridade: Link direto na URL
        if link_drive_url:
            link_final = link_drive_url
            
        # 2. Se não tem link, mas tem ID do processo, busca no banco (mesmo sem nome de espetáculo)
        elif processo_id_url:
            try:
                from supabase_utils import buscar_link_drive_artes
                # Passa o ID. O nome/teatro são opcionais nesse caso.
                link_final = buscar_link_drive_artes("", "", processo_id_url)
            except Exception:
                pass
                
        # 3. Se não tem nada na URL, depende do nome digitado
        elif espetaculo_nome and espetaculo_nome.strip():
            try:
                from supabase_utils import buscar_link_drive_artes
                link_final = buscar_link_drive_artes(espetaculo_nome, teatro_selecionado)
            except Exception:
                pass

        # Se resetar a seleção, limpa também a lixeira para evitar inconsistências futuras
        if arquivos_carregados and st.button("5️⃣ 🗑️ Limpar Seleção", use_container_width=True):
            st.session_state["uploader_key"] += 1
            st.session_state["removed_files"] = set() # Reset removed files too
            st.rerun()

        botao_validar_clicado = st.button(MESSAGES["validar_arte"], use_container_width=True, type="primary")
        
        # Exibe o botão se encontrou algum link
        st.markdown("---")
        st.markdown("**🛠️ Ferramentas de Apoio:**")
        
        if link_final:
            st.link_button(
                "📂 Abre a pasta do Drive com todas as artes deste espetáculo", 
                link_final, 
                use_container_width=True
            )
        
        st.link_button("Fale com o Procópio", "https://wa.me/5521968815522", use_container_width=True)
        
        # Links de Gabaritos (Placeholder - Aguardando URLs reais)
        st.markdown("**📥 Gabaritos Photoshop:**")
        st.link_button("🎭 Teatro das Artes", "https://drive.google.com/drive/folders/1hphPn7oWtfsAH9Cp5hoHD4FIuingzlhD", use_container_width=True) 
        st.link_button("🎭 Teatro dos Grandes Atores", "/Gabaritos Teatro dos Grandes Atores.zip", use_container_width=True)

        st.link_button("← Voltar ao Sistema Teatrali", "https://teatrali.netlify.app/", use_container_width=True)
        
        # --- ÁREA DE HISTÓRICO ---
        if st.checkbox("📜 Ver Histórico Recente"):
             from history_utils import load_all_history
             history = load_all_history()
             if not history:
                 st.caption("Nenhum histórico encontrado.")
             else:
                 for key, data in history.items():
                     with st.expander(f"{data['espetaculo']} ({data['status']})"):
                         st.caption(f"Última atualização: {data['last_update']}")
                         st.markdown(f"**Teatro:** {data['teatro']}")
                         if data['missing']:
                            st.markdown("⚠️ **Pendências:**")
                            for m in data['missing']:
                                st.markdown(f"- {m}")
                         else:
                             st.success("✅ Tudo entregue!")

    # Garante que retorna uma lista, mesmo que vazia
    if arquivos_validos is None:
        arquivos_validos = []
        
    return teatro_selecionado, regra_selecionada, arquivos_validos, botao_validar_clicado

def _renderizar_bloco_imagem(titulo: str, caption: str, imagem_path: Any, placeholder_text: str):
    st.subheader(titulo)
    if caption:
        st.caption(caption)

    if imagem_path:
        if isinstance(imagem_path, str) and not os.path.exists(imagem_path):
            st.warning(f"{MESSAGES['gabarito_nao_encontrado']} {imagem_path}")
        else:
            st.image(imagem_path)
    else:
        st.markdown(f'<div class="art-placeholder" style="width:100%; height:400px; background-color:#2E2E38; border:2px dashed #555; border-radius:8px; display:flex; align-items:center; justify-content:center; color:#999; font-size:1.1em;">{placeholder_text}</div>', unsafe_allow_html=True)

def renderizar_area_visualizacao(regra: Dict[str, Any], arquivos: list) -> None:
    if not regra:
        st.info("Selecione um teatro e um gabarito no painel à esquerda para começar.")
        return

    # Inicializa estado de arquivos removidos se não existir
    if "removed_files" not in st.session_state:
        st.session_state["removed_files"] = set()

    # Filtra arquivos que foram "deletados" pelo usuário nesta sessão
    # Nota: Recebemos já filtrado do sidebar, mas mantemos redundância segura
    arquivos_visiveis = [a for a in arquivos if (a.name, a.size) not in st.session_state["removed_files"]]

    # Modo Inteligente
    if regra.get("is_smart_mode"):
        st.markdown("### 🔍 Modo de Validação Automática")
        st.markdown('<div style="font-size: 1.2em; margin-bottom: 20px; color: #e0e0e0;">O sistema identificará automaticamente o formato de cada arquivo enviado e verificará as regras correspondentes.</div>', unsafe_allow_html=True)
        
        if arquivos_visiveis:
            st.subheader(f"Artes Carregadas ({len(arquivos_visiveis)})")
            
            # --- LÓGICA DE ORDENAÇÃO (Bloqueados primeiro) ---
            from PIL import Image
            todas_regras = regra.get("todas_regras", {})
            
            arquivos_processados = []
            
            for arquivo in arquivos_visiveis:
                # Ler dimensões sem consumir o arquivo permanentemente
                arquivo.seek(0)
                img = Image.open(arquivo)
                w, h = img.size
                arquivo.seek(0) # Reset pointer
                
                valid_format = False
                for r_vals in todas_regras.values():
                    if abs(r_vals["largura"] - w) <= 1 and abs(r_vals["altura"] - h) <= 1:
                        valid_format = True
                        break
                
                # Armazena tupla (is_blocked, arquivo, width, height)
                # is_blocked = True se NÃO for válido (para aparecer primeiro na sort, True > False? Não, False < True. 
                # Queremos Blocked (Invalid) primeiro. Invalid = not valid.
                # Sort key: (is_valid, nome) -> False (0) vem antes de True (1).
                arquivos_processados.append({
                    "arquivo": arquivo,
                    "is_valid": valid_format,
                    "width": w,
                    "height": h,
                    "name": arquivo.name
                })
            
            # Ordena: Invalidos (False) primeiro, depois Válidos (True)
            arquivos_processados.sort(key=lambda x: x["is_valid"])
            
            # --- RENDERIZAÇÃO EM GRID (UX Melhorada - 3 Colunas) ---
            cols = st.columns(3)
            
            for idx, item in enumerate(arquivos_processados):
                arquivo = item["arquivo"]
                is_valid = item["is_valid"]
                w = item["width"]
                h = item["height"]
                
                with cols[idx % 3]:
                    # Card Container styling wrapper (via CSS class if possible, but st.container is logical grouping)
                    with st.container(border=True): # Use Streamlit's native border container for better defining the card
                        # 1. Image Area
                        st.image(arquivo, use_container_width=True, channels="RGB")
                        
                        # 2. Status Area
                        if is_valid:
                            st.markdown(f"**✅ {arquivo.name}**")
                            st.caption(f"Dimensões: {w}x{h}px")
                        else:
                            # Cleaner, compact error badge
                            st.markdown(f"""
                            <div style="
                                background-color: #ff4b4b; 
                                color: white; 
                                padding: 8px; 
                                border-radius: 4px; 
                                margin-top: 5px; 
                                margin-bottom: 10px; 
                                font-size: 0.9em; 
                                line-height: 1.2;
                                text-align: center;">
                                <strong>⛔ BLOQUEADO</strong><br>
                                <span style="opacity:0.9; font-size:0.85em;">{w}x{h}px • Inválido</span>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # 3. Action Area
                        if st.button("🗑️ Remover", key=f"del_{arquivo.name}_{idx}", use_container_width=True):
                            st.session_state["removed_files"].add((arquivo.name, arquivo.size))
                            st.rerun()

        else:
            if len(st.session_state["removed_files"]) > 0 and len(arquivos) > 0:
                 st.info("Todos os arquivos visíveis foram removidos. Limpe a seleção no menu lateral para reiniciar.")
            else:
                st.markdown('<div class="art-placeholder" style="height:200px; font-size: 1.5em; display:flex; align-items:center; justify-content:center; color: #cccccc;">Aguardando upload de arquivos...</div>', unsafe_allow_html=True)
        return

    # Modo Individual (comportamento original, adaptado para lista)
    # Nota: O filtro de removidos também se aplica aqui
    arquivo_principal = arquivos_visiveis[0] if arquivos_visiveis else None
    
    orientacao = regra.get("orientacao", "vertical")

    if orientacao == "horizontal":
        _renderizar_bloco_imagem("Gabarito", regra.get("descricao", ""), regra.get("gabarito_path"), "Gabarito não encontrado")
        st.header("")
        _renderizar_bloco_imagem("Sua Arte", f"Arquivo: {arquivo_principal.name}" if arquivo_principal else "", arquivo_principal, MESSAGES["aguardando_upload"])
        if len(arquivos_visiveis) > 1:
            st.caption(f"+ {len(arquivos_visiveis)-1} outros arquivos carregados")
    else:
        col1, col2 = st.columns(2)
        with col1:
            _renderizar_bloco_imagem("Gabarito", regra.get("descricao", ""), regra.get("gabarito_path"), "Gabarito não encontrado")
        with col2:
            _renderizar_bloco_imagem("Sua Arte", f"Arquivo: {arquivo_principal.name}" if arquivo_principal else "", arquivo_principal, MESSAGES["aguardando_upload"])
            if len(arquivos_visiveis) > 1:
                st.caption(f"+ {len(arquivos_visiveis)-1} outros arquivos carregados")

def renderizar_resultados(validar_button: bool, arquivos: list, regra: Dict[str, Any]) -> None:
    if not validar_button:
        return
    if not arquivos:
        st.warning(MESSAGES["upload_antes_validar"])
        return
    if not regra:
        st.error("Selecione um gabarito antes de validar.")
        return

    try:
        from common_utils import verificar_arte
        from PIL import Image

        st.divider()
        st.header("Status da Validação")

        # Lógica para Modo Inteligente
        # Lógica para Modo Inteligente
        if regra.get("is_smart_mode"):
            
            # Deduplicação Binária e por Nome Limpo
            arquivos_unicos = []
            hashes_vistos = set()
            nomes_vistos = set()
            duplicados_count = 0
            
            for arq in arquivos:
                # Check Hash
                arq.seek(0)
                file_hash = hashlib.md5(arq.read()).hexdigest()
                arq.seek(0)
                
                if file_hash not in hashes_vistos:
                    hashes_vistos.add(file_hash)
                    arquivos_unicos.append(arq)
                else:
                    duplicados_count += 1
            
            if duplicados_count > 0:
                st.toast(f"⚠️ {duplicados_count} duplicata(s) removida(s) automaticamente.", icon="🧹")
            
            # Atualiza lista para processamento
            arquivos = arquivos_unicos

            todas_regras = regra.get("todas_regras", {})
            regras_encontradas = set()
            
            # Listas para agrupamento
            lista_aprovados = []
            lista_reprovados = []
            lista_sem_formato = []
            
            # Cabeçalho do Relatório com Data e Teatro
            from datetime import datetime
            data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
            nome_teatro = regra.get("teatro", "Teatro não identificado")
            
            relatorio_texto = [
                "RELATÓRIO DE VALIDAÇÃO - TEATRALI",
                f"Teatro: {nome_teatro}",
                f"Data: {data_atual}",
                "="*40, 
                ""
            ]
            
            # Processamento
            for arquivo in arquivos:
                arquivo.seek(0)
                img = Image.open(arquivo)
                largura, altura = img.size
                
                # Identificação da regra
                regra_compativel = None
                nome_regra = "Desconhecido"
                key_regra = ""
                
                for k, r in todas_regras.items():
                    # Tolerância de 1px na identificação (opcional, mas seguro)
                    if abs(r["largura"] - largura) <= 1 and abs(r["altura"] - altura) <= 1:
                        regra_compativel = r
                        nome_regra = r["descricao"]
                        key_regra = k
                        break
                
                info_arquivo = {
                    "nome": arquivo.name,
                    "regra": nome_regra,
                    "dimensao": f"{largura}x{altura}px",
                    "msg": "",
                    "checklist": []
                }

                if regra_compativel:
                    regras_encontradas.add(nome_regra)
                    aprovado, msg = verificar_arte(arquivo, regra_compativel)
                    info_arquivo["msg"] = msg
                    info_arquivo["checklist"] = regra_compativel.get("checklist_visual", [])
                    
                    if aprovado:
                        lista_aprovados.append(info_arquivo)
                        relatorio_texto.append(f"[APROVADO] {arquivo.name} ({nome_regra})")
                    else:
                        lista_reprovados.append(info_arquivo)
                        relatorio_texto.append(f"[REPROVADO] {arquivo.name} ({nome_regra}) - Motivo: {msg}")
                else:
                    # Treat unknown formats as REJECTED
                    info_arquivo["msg"] = f"Dimensões {largura}x{altura}px não correspondem a nenhuma regra deste teatro."
                    lista_reprovados.append(info_arquivo)
                    relatorio_texto.append(f"[REPROVADO] {arquivo.name} ({largura}x{altura}px) - Motivo: Formato desconhecido")
            
            # Análise de Faltantes
            faltantes_mandatorios = []
            faltantes_opcionais = [] # Banners
            
            for k, r in todas_regras.items():
                if r["descricao"] not in regras_encontradas:
                    if k.startswith("banner_"):
                         faltantes_opcionais.append(r["descricao"])
                    else:
                         faltantes_mandatorios.append(r["descricao"])

            # ======= DASHBOARD DE RESUMO COM CORES =======
            st.markdown("### Status da Entrega")
            
            style_card = """
            <style>
                .kpi-card {
                    border-radius: 8px;
                    padding: 15px;
                    text-align: center;
                    margin-bottom: 10px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                }
                .kpi-value { font-size: 2em; font-weight: bold; margin-bottom: 5px; }
                .kpi-label { font-size: 0.9em; font-weight: 600; text-transform: uppercase; }
                
                .card-green { background-color: #28a745; color: white; }
                .card-red { background-color: #dc3545; color: white; }
                .card-blue { background-color: #007bff; color: white; }
                .card-white { background-color: #f8f9fa; color: #333; border: 1px solid #ddd; }
            </style>
            """
            st.markdown(style_card, unsafe_allow_html=True)
            
            def kpi_html(label, value, color_class):
                return f"""
                <div class="kpi-card {color_class}">
                    <div class="kpi-value">{value}</div>
                    <div class="kpi-label">{label}</div>
                </div>
                """
            
            c1, c2, c3, c4 = st.columns(4)
            c1.markdown(kpi_html("Aprovados", len(lista_aprovados), "card-green"), unsafe_allow_html=True)
            c2.markdown(kpi_html("Reprovados", len(lista_reprovados), "card-red"), unsafe_allow_html=True)
            c3.markdown(kpi_html("Faltam (Obrig.)", len(faltantes_mandatorios), "card-blue"), unsafe_allow_html=True)
            
            # Lógica Banners: Conta como 1 grupo. Se detectou algum banner (aprovado ou não), faltam=0.
            has_banners = any(k.startswith("banner_") for k in todas_regras)
            found_banner = any(v["descricao"] in regras_encontradas for k, v in todas_regras.items() if k.startswith("banner_"))
            val_banners = 1 if (has_banners and not found_banner) else 0
            
            c4.markdown(kpi_html("Banners (Opc.)", val_banners, "card-white"), unsafe_allow_html=True)
            
            st.divider()

            # ======= STATUS GERAL DO PACOTE =======
            pacote_concluido = len(faltantes_mandatorios) == 0 and len(lista_reprovados) == 0
            
            if pacote_concluido:
                st.balloons()
                st.markdown('<div class="kpi-card card-green" style="font-size:1.1em; text-align:center;">🏆 PARABÉNS! PACOTE DE ARTES OBRIGATÓRIAS CONCLUÍDO! Todas as artes foram aprovadas.</div>', unsafe_allow_html=True)
                relatorio_texto.append("\nSTATUS FINAL: ARTES CONCLUÍDAS 🏆")
            elif len(lista_reprovados) > 0:
                st.markdown(f'<div class="kpi-card card-red" style="font-size:1.1em;">Atenção: Existem {len(lista_reprovados)} artes reprovadas que precisam de correção.</div>', unsafe_allow_html=True)
                relatorio_texto.append("\nSTATUS FINAL: PENDENTE CORREÇÃO")
            else:

                st.markdown(f'<div class="kpi-card card-blue" style="font-size:1.1em;">ℹ️ O processo continua! Faltam {len(faltantes_mandatorios)} artes obrigatórias.</div>', unsafe_allow_html=True)
                relatorio_texto.append("\nSTATUS FINAL: EM ANDAMENTO")

            # ======= LISTAGEM DETALHADA =======
            
            if lista_reprovados:
                st.markdown("### ❌ Artes Reprovadas (Corrigir)")
                for item in lista_reprovados:
                    with st.status(f"{item['nome']} - {item['regra']}", expanded=True, state="error"):
                        st.error(f"Motivo: {item['msg']}")
                        st.caption("Verifique as dimensões, modo de cor (RGB/CMYK) e resolução.")

            if lista_aprovados:
                st.markdown("### ✅ Artes Aprovadas")
                for item in lista_aprovados:
                    with st.status(f"{item['nome']} - {item['regra']}", expanded=False, state="complete"):
                        st.success("Formato Técnico Correto")
                        if item['checklist']:
                            st.markdown("---")
                            st.markdown("**Checklist Visual:**")
                            for chk in item['checklist']:
                                st.markdown(f"- [ ] {chk}")

            # Sem formato removido - agora entram como reprovados.

            # ======= CHECKLIST PENDENTES =======
            st.markdown("### 📋 Checklist de Pendências")
            
            col_mand, col_opc = st.columns(2)
            
            with col_mand:
                if faltantes_mandatorios:
                    html_items = "".join([f"<li style='text-align:left;'>{fal}</li>" for fal in faltantes_mandatorios])
                    st.markdown(f"""
                    <div class="kpi-card card-red" style="text-align:left; padding:15px; margin-bottom:10px;">
                        <h4 style="margin:0 0 10px 0; color:white; font-size:1.1em;">⚠️ Artes Obrigatórias Faltantes:</h4>
                        <ul style="margin:0; padding-left:20px;">{html_items}</ul>
                    </div>
                    """, unsafe_allow_html=True)
                    for f in faltantes_mandatorios:
                        relatorio_texto.append(f"MISSING MANUAL: {f}")
                else:
                    st.markdown('<div class="kpi-card card-green" style="font-size:1.1em; text-align:center;">Todas as artes obrigatórias foram entregues!</div>', unsafe_allow_html=True)

            with col_opc:
                if faltantes_opcionais:
                    html_banners = "".join([f"<li style='text-align:left;'>{f}</li>" for f in faltantes_opcionais])
                    st.markdown(f"""
                    <div class="kpi-card card-blue" style="text-align:left; padding:15px; margin-bottom:10px;">
                        <h4 style="margin:0 0 10px 0; color:white; font-size:1.1em;">ℹ️ Banners Individuais (Opcionais):</h4>
                        <ul style="margin:0; padding-left:20px;">{html_banners}</ul>
                    </div>
                    """, unsafe_allow_html=True)
            
            # ======= SALVAMENTO AUTOMÁTICO NO HISTÓRICO =======
            nome_espetaculo_save = regra.get("espetaculo", "").strip()
            if nome_espetaculo_save:
                from history_utils import save_validation_state
                # Extrai nomes dos arquivos aprovados/reprovados
                aprovados_names = [f"{item['nome']} ({item['regra']})" for item in lista_aprovados]
                reprovados_names = [f"{item['nome']} ({item['msg']})" for item in lista_reprovados]
                
                save_validation_state(
                    espetaculo=nome_espetaculo_save,
                    teatro=nome_teatro,
                    arquivos_aprovados=aprovados_names,
                    arquivos_reprovados=reprovados_names,
                    faltantes=faltantes_mandatorios
                )
                st.toast(f"Histórico salvo para '{nome_espetaculo_save}'!", icon="💾")

            # Download
            st.download_button(
                label="📥 Baixar Relatório de Status",
                data="\n".join(relatorio_texto),
                file_name="status_validacao_artes.txt",
                mime="text/plain",
                use_container_width=True
            )
            return

        # Lógica Original (Validação Simples) - Loop para todos os arquivos
        for arquivo in arquivos:
            aprovado, mensagem = verificar_arte(arquivo, regra)
            
            with st.container():
                st.subheader(f"Arquivo: {arquivo.name}")
                if aprovado:
                    st.success(f"{MESSAGES['arte_aprovada']} {mensagem}")
                    
                    # Exibir checklist visual
                    checklist = regra.get("checklist_visual", [])
                    if checklist:
                        st.markdown("##### 📝 Checklist Visual")
                        st.info("Por favor, verifique visualmente os seguintes itens:")
                        for item in checklist:
                            st.markdown(f"- [ ] {item}")
                        st.caption("*Estes itens não podem ser validados automaticamente.*")
                        
                else:
                    st.error(f"{MESSAGES['arte_reprovada']}")
                    st.info(mensagem)
                    
                    # Também exibir checklist no erro
                    checklist = regra.get("checklist_visual", [])
                    if checklist:
                        with st.expander("Ver requisitos visuais"):
                            for item in checklist:
                                st.markdown(f"- {item}")
        
    except Exception as e:
        st.error(f"Ocorreu um erro inesperado durante a validação: {e}")
