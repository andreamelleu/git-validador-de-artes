import streamlit as st
import datetime
import os
from regras import carregar_regras
from regras import verificar_arte # Adicionei a importação da sua função

st.set_page_config(page_title="GIT Validador de Artes", layout="wide")

def main():
    # ===== SIDEBAR =====
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

    st.sidebar.image("logo_mywork.png") # Removido o 'use_container_width' desnecessário

    st.sidebar.title("Painel de Validação")

    teatro = st.sidebar.selectbox(
        "Selecione o Teatro:",
        ["Teatro dos Grandes Atores", "Teatro das Artes"]
    )

    regras = carregar_regras(teatro)
    gabarito_opcoes = [v["descricao"] for v in regras.values()]
    escolha_gabarito = st.sidebar.selectbox("Selecione o Gabarito:", gabarito_opcoes)
    chave_gabarito = list(regras.keys())[gabarito_opcoes.index(escolha_gabarito)]
    regra = regras[chave_gabarito]

    st.sidebar.markdown("#### Suba a sua Arte:")
    arquivo = st.sidebar.file_uploader("Arraste e solte o arquivo aqui", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    
    # CORREÇÃO 2: Salvar o resultado do botão
    validar_button = st.sidebar.button("Validar Arte")

    hoje = datetime.date.today().strftime("%d/%m/%Y")
    st.sidebar.markdown(f"**Rio de Janeiro, {hoje}.**")

    # ===== CABEÇALHO =====
    st.markdown("<div class='titulo-principal'>GIT Validador de Artes</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='texto-intro'>Olá, produtor Teatrali, verifique se todas as suas artes estão aprovadas para subir no drive.<br>"
        "Para abertura de vendas e divulgação, elas devem estar conforme orientações do checklist recebido.</div>",
        unsafe_allow_html=True
    )
    st.divider()

    # ===== ÁREA DE VISUALIZAÇÃO =====
    col_gabarito, col_arte = st.columns(2)

    with col_gabarito:
        st.subheader(f"Gabarito: {regra['descricao']}")
        # CORREÇÃO 3: Adicionei a lógica para mostrar a imagem do gabarito
        caminho_gabarito = regra.get("gabarito_img", "assets/default.png")
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

    # ===== ÁREA DE RESULTADOS (Lógica do placeholder está correta) =====
    placeholder_resultados = st.empty()

    if validar_button and arquivo:
        aprovado, mensagem = verificar_arte(arquivo, regra) 
        with placeholder_resultados.container():
            if aprovado:
                st.success(f"✅ ARTE APROVADA! {mensagem}")
            else:
                st.error(f"❌ ARTE REPROVADA! {mensagem}")
    elif validar_button and not arquivo:
        with placeholder_resultados.container():
            st.warning("Por favor, faça o upload de uma arte antes de validar.")

if __name__ == "__main__":
    main()
