import streamlit as st
from datetime import datetime

# === CONFIGURAÇÕES GERAIS ===
st.set_page_config(
    page_title="GIT Validador de Artes",
    layout="wide",
    page_icon="generated-icon-black.svg"
)

# === ESTILO PERSONALIZADO (modo claro) ===
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #f2f2f2 !important;
            color: #000000 !important;
        }
        .stTextInput > div > div > input, 
        .stSelectbox > div > div > div,
        .stButton > button {
            color: #000000 !important;
        }
        footer:after {
            content:'mywork.digital startup';
            visibility: visible;
            display: block;
            position: relative;
            color: #555;
            padding: 10px;
            font-size: 14px;
            text-align: center;
        }
        footer > div:first-child {visibility: hidden;}
        #MainMenu {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# === CABEÇALHO E LOGO ===
st.image("logo_mywork_black.png", use_container_width=False)
st.title("Painel de Validação")

# === CAMPOS DE ENTRADA ===
st.subheader("Selecione o Teatro:")
teatro = st.selectbox("Selecione o Teatro:", ["Teatro dos Grandes Atores", "Teatro das Artes"])

st.subheader("Selecione o Gabarito:")
gabarito = st.selectbox("Selecione o Gabarito:", ["Divertix Home do Site – 370 x 550 px"])

st.subheader("Suba a sua Arte:")
arte = st.file_uploader("Suba a sua arte (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

# === BOTÃO DE AÇÃO ===
if st.button("Validar Arte"):
    if arte is not None:
        st.success(f"Arquivo '{arte.name}' enviado com sucesso!")
    else:
        st.warning("Por favor, envie um arquivo antes de validar.")

# === RODAPÉ ===
data_atual = datetime.now().strftime("%d/%m/%Y")
st.markdown(f"<p style='text-align:center;color:#000000;'>Rio de Janeiro, {data_atual}.</p>", unsafe_allow_html=True)
