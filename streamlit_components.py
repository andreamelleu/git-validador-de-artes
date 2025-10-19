"""
Componentes reutilizáveis para Streamlit
Centraliza componentes de UI que são usados em múltiplos lugares
"""
import streamlit as st
from common_utils import formatar_data_brasileira


def renderizar_sidebar_estilo():
    """Renderiza o estilo CSS para a sidebar"""
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-color: #2c2c34;
        }
        [data-testid="stSidebar"] img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 240px;
            image-rendering: -webkit-optimize-contrast;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def renderizar_cabecalho():
    """Renderiza o cabeçalho principal da aplicação"""
    st.markdown("<div class='titulo-principal'>GIT Validador de Artes</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='texto-intro'>Olá, produtor Teatrali, verifique se todas as suas artes estão aprovadas para subir no drive.<br>"
        "Para abertura de vendas e divulgação, elas devem estar conforme orientações do checklist recebido.</div>",
        unsafe_allow_html=True
    )
    st.divider()


def renderizar_sidebar_painel(teatro_inicial, regras, arquivo):
    """
    Renderiza o painel lateral com controles de seleção
    
    Args:
        teatro_inicial: Teatro inicial selecionado
        regras: Dicionário de regras disponíveis
        arquivo: Arquivo carregado
        
    Returns:
        tuple: (teatro, regra, arquivo, validar_button)
    """
    from regras import carregar_regras
    
    renderizar_sidebar_estilo()
    
    st.sidebar.image("logo_mywork.png")
    st.sidebar.title("Painel de Validação")

    teatro = st.sidebar.selectbox(
        "Selecione o Teatro:",
        ["Teatro dos Grandes Atores", "Teatro das Artes"],
        index=0 if teatro_inicial == "Teatro dos Grandes Atores" else 1
    )

    # Carrega regras baseadas no teatro selecionado
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
    """
    Renderiza a área de visualização com gabarito e arte
    """
    import os
    import streamlit as st
    from config import DIRECTORY_CONFIG

    col_gabarito, col_arte = st.columns(2)

    with col_gabarito:
        st.subheader(f"Gabarito: {regra['descricao']}")

        # Determina diretório base (mantendo a estrutura existente)
        diretorio_teatro = (
            DIRECTORY_CONFIG["GRANDES_ATORES_PATH"]
            if "Grandes Atores" in teatro
            else DIRECTORY_CONFIG["DAS_ARTES_PATH"]
        )

        caminho_gabarito = os.path.join(diretorio_teatro, regra.get("gabarito_img", "default.png"))

        if os.path.exists(caminho_gabarito):
            st.image(caminho_gabarito, use_container_width=True)
        else:
            st.warning(f"⚠️ Gabarito não encontrado: {caminho_gabarito}")

    with col_arte:
        st.subheader("Sua Arte")
        if arquivo:
            st.image(arquivo, use_container_width=True)
        else:
            st.info("Aguardando upload...")

    st.divider()

def renderizar_resultados(validar_button, arquivo, regra):
    """
    Renderiza a área de resultados da validação
    
    Args:
        validar_button: Estado do botão de validação
        arquivo: Arquivo carregado
        regra: Regra de validação
    """
    placeholder_resultados = st.empty()

    if validar_button and arquivo:
        from common_utils import verificar_arte
        aprovado, mensagem = verificar_arte(arquivo, regra) 
        with placeholder_resultados.container():
            if aprovado:
                st.success(f"✅ ARTE APROVADA! {mensagem}")
            else:
                st.error(f"❌ ARTE REPROVADA! {mensagem}")
    elif validar_button and not arquivo:
        with placeholder_resultados.container():
            st.warning("Por favor, faça o upload de uma arte antes de validar.")
