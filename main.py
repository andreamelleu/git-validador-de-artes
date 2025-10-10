import streamlit as st

try:
    from regras import verificar_arte
    from PIL import Image
    import pandas as pd
    import io
    import os
    import base64
    import datetime
    import zipfile
    import shutil
    from utils import processar_arquivo, salvar_log
except Exception as e:
    st.error(f"Erro de importação: {e}")
    raise

import streamlit as st
import datetime
import os
from regras import carregar_regras

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

    # logo limpa e nítida
    st.sidebar.image("logo_mywork.png")

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
    arquivo = st.sidebar.file_uploader("Drag and drop file here", type=["jpg", "jpeg", "png"])
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.button("Validar Arte")

    hoje = datetime.date.today().strftime("%d/%m/%Y")
    st.sidebar.markdown(f"**Rio de Janeiro, {hoje}.**")

    # ===== CABEÇALHO =====
    st.markdown(
        """
        <style>
        .titulo-principal {
            font-size: 2.2rem;
            font-weight: 700;
        }
        .texto-intro {
            font-size: 1.05rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

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
        caminho = regra["gabarito_img"]
        if not os.path.exists(caminho):
            caminho = os.path.join("assets", "teatros", "grandes_atores", caminho)
        if os.path.exists(caminho):
            st.image(caminho, use_container_width=True)
        else:
            st.warning("Imagem de gabarito não encontrada.")

    with col_arte:
        st.subheader("Sua Arte")
        if arquivo:
            st.image(arquivo, use_container_width=True)
        else:
            st.info("Aguardando upload...")

if __name__ == "__main__":
    main()
