"""
Componentes reutilizáveis para Streamlit
Centraliza componentes de UI que são usados em múltiplos lugares
"""

import streamlit as st
from common_utils import formatar_data_brasileira


def aplicar_estilo_global():
    """Aplica tema light/dark automaticamente + rodapé customizado"""
    st.markdown(
        """
        <style>
        /* Tema claro (light) */
        @media (prefers-color-scheme: light) {
            .stApp { background-color: #f2f2f2 !important; color: #000 !important; }
            h1, h2, h3, .stSubheader, label, p, span, div { color: #000 !important; }
            .stButton > button {
                background-color: #e0e0e0 !important;
                color: #000 !important;
                border-radius: 6px;
            }
            [data-testid="stSidebar"] { background-color: #f5f5f5 !important; }
        }

        /* Tema escuro (dark) */
        @media (prefers-color-scheme: dark) {
            .stApp { background-color: #1e1e1e !important; color: #fff !important; }
            h1, h2, h3, .stSubheader, label, p, span, div { color: #fff !important; }
            .stButton > button {
                background-color: #333 !important;
                color: #fff !important;
                border-radius: 6px;
            }
            [data-testid="stSidebar"] { background-color: #2c2c34 !important; }
        }

        /* Tamanho de fontes */
        h1 { font-size: 26px !important; }
        h2 { font-size: 20px !important; }
        h3, label, p, span, div, .stMarkdown { font-size: 14px !important; }

        /* Rodapé customizado */
        #MainMenu {visibility: hidden;}
        footer > div:first-child {visibility: hidden;}
        footer:after {
            content: "mywork.digital startup";
            visibility: visible;
            display: block;
            position: relative;
            color: #777;
            padding: 10px;
            font-size: 13px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def _logo_por_tema():
    """Exibe logo conforme tema do usuário"""
    st.markdown(
        """
        <style>
        @media (prefers-color-scheme: light) {
            .logo-light { display: block; }
            .logo-dark { display: none; }
        }
        @media (prefers-color-scheme: dark) {
            .logo-light { display: none; }
            .logo-dark { display: block; }
        }
        </style>

        <img src="logo_mywork_black.png" class="logo-light" width="220">
        <img src="logo_mywork_white.png" class="logo-dark" width="220">
        """,
        unsafe_allow_html=True
    )


def renderizar_cabecalho():
    """Renderiza o cabeçalho principal da aplicação"""
    aplicar_estilo_global()
    _logo_por_tema()
    st.markdown("<h1>GIT Validador de Artes</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p>Olá, produtor Teatrali, verifique se todas as suas artes estão aprovadas para subir no drive.<br>"
        "Para abertura de vendas e divulgação, elas devem estar conforme orientações do checklist recebido.</p>",
        unsafe_allow_html=True
    )
    st.divider()


def renderizar_sidebar_painel(teatro_inicial, regras, arquivo):
    """Renderiza o painel lateral com controles"""
    from regras import carregar_regras

    _logo_por_tema()
    st.sidebar.title("Painel de Validação")

    teatro = st.sidebar.selectbox(
        "Selecione o Teatro:",
        ["Teatro dos Grandes Atores", "Teatro das Artes"],
        index=0 if teatro_inicial == "Teatro dos Grandes Atores" else 1
    )

    regras_teatro = carregar_regras(teatro)
    if regras_teatro:
        gabarito_opcoes = [v["descricao"] for v in regras_teatro.values()]
        escolha_gabarito = st.sidebar.selectbox("Selecione o Gabarito:", gabarito_opcoes)
        chave_gabarito = list(regras_teatro.keys())[gabarito_opcoes.index(escolha_gabarito)]
        regra = regras_teatro[chave_gabarito]
    else:
        st.sidebar.error("Nenhuma regra encontrada para este teatro")
        regra = {}

    st.sidebar.markdown("#### Suba a sua Arte:")
    arquivo = st.sidebar.file_uploader("Arraste e solte o arquivo aqui", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    validar_button = st.sidebar.button("Validar Arte")

    hoje = formatar_data_brasileira()
    st.sidebar.markdown(f"**Rio de Janeiro, {hoje}.**")

    return teatro, regra, arquivo, validar_button


def renderizar_area_visualizacao(regra, arquivo, teatro):
    """Renderiza a área de visualização com gabarito e arte"""
    from common_utils import verificar_existencia_imagem
    import os

    col_gabarito, col_arte = st.columns(2)

    with col_gabarito:
        st.subheader(f"Gabarito: {regra.get('descricao', '')}")
        diretorio_teatro = "grandes_atores" if "Grandes Atores" in teatro else "das_artes"
        caminho_gabarito = verificar_existencia_imagem(diretorio_teatro, regra.get("gabarito_img", "default.png"))

        if os.path.exists(caminho_gabarito):
            st.image(caminho_gabarito, use_container_width=True)
        else:
            st.warning(f"Imagem de gabarito não encontrada em: {caminho_gabarito}")

    with col_arte:
        st.subheader("Sua Arte")
        if arquivo:
            st.image(arquivo, use_container_width=True)
        else:
            st.info("Aguardando upload...")

    st.divider()


def renderizar_resultados(validar_button, arquivo, regra):
    """Renderiza a área de resultados da validação"""
    placeholder_resultados = st.empty()

    if validar_button and arquivo:
        from common_utils import verificar_arte
        aprovado, mensagem = verificar_arte(arquivo, regra)
        with placeholder_resultados.container():
            if aprovado:
                st.success(f"ARTE APROVADA! {mensagem}")
            else:
                st.error(f"ARTE REPROVADA! {mensagem}")
    elif validar_button and not arquivo:
        with placeholder_resultados.container():
            st.warning("Por favor, faça o upload de uma arte antes de validar.")
