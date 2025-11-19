import streamlit as st
from PIL import Image
import os

# Caminho base dos gabaritos
BASE_GABARITOS = "teatros/das_artes/grandes_atores"

st.set_page_config(page_title="Validador de Artes", layout="wide")

# Título
st.title("🎭 GIT - Validador de Formatos de Artes")

# Informações iniciais
st.markdown("""
Olá, produtor(a)!  
Verifique se a sua arte está no formato correto, de acordo com o gabarito fornecido.  
Para abrir vendas e divulgar, as artes devem seguir o tamanho exato e as logomarcas do teatro e Divertix devem estar no topo da arte.
""")

# 1. Seleção de gabarito
gabaritos_disponiveis = [
    f for f in os.listdir(BASE_GABARITOS) if f.endswith(".png")
]

# Nome formatado para exibir no dropdown
def formatar_nome(nome_arquivo):
    nome_limpo = nome_arquivo.replace("gabarito_", "").replace(".png", "")
    return nome_limpo.replace("_", " ").title()

gabarito_escolhido = st.selectbox(
    "Selecione o Gabarito:",
    options=gabaritos_disponiveis,
    format_func=formatar_nome
)

# Caminho do gabarito
caminho_gabarito = os.path.join(BASE_GABARITOS, gabarito_escolhido)

# Exibir gabarito
col1, col2 = st.columns(2)

with col1:
    st.subheader("📐 Gabarito")
    imagem_gabarito = Image.open(caminho_gabarito)
    st.image(imagem_gabarito, caption=f"{formatar_nome(gabarito_escolhido)}", use_column_width=False)

# Upload da arte
with col2:
    st.subheader("🎨 Sua Arte")
    upload = st.file_uploader("Envie sua arte para validação de formatos (JPEG, PNG)", type=["jpg", "jpeg", "png"])
    
    if upload is not None:
        arte = Image.open(upload)
        st.image(arte, caption="Sua arte enviada", use_column_width=False)

        # Validar tamanho
        tam_gabarito = imagem_gabarito.size  # (largura, altura)
        tam_arte = arte.size  # (largura, altura)

        st.markdown(f"**Tamanho do Gabarito:** `{tam_gabarito[0]} x {tam_gabarito[1]}` px")
        st.markdown(f"**Tamanho da sua Arte:** `{tam_arte[0]} x {tam_arte[1]}` px")

        # Resultado
        if tam_arte == tam_gabarito:
            st.success("✅ Formato de Arte Aprovado! Tamanho correto.")
        else:
            st.error("❌ Formato de Arte Reprovado. Tamanho incorreto.")
            st.warning("⚠️ Ajuste sua arte para que tenha exatamente o mesmo tamanho do gabarito.")
