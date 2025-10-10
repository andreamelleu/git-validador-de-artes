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
    st.sidebar.image("logo_mywork.png", use_container_width=False)

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
# ... todo o seu código da sidebar e do cabeçalho ...

# ===== ÁREA DE VISUALIZAÇÃO (seu código atual) =====
col_gabarito, col_arte = st.columns(2)

with col_gabarito:
    st.subheader(f"Gabarito: {regra['descricao']}")
    # ... seu código para mostrar a imagem do gabarito ...

with col_arte:
    st.subheader("Sua Arte")
    if arquivo:
        st.image(arquivo, use_container_width=True)
    else:
        st.info("Aguardando upload...")

st.divider()

# ===== ÁREA DE RESULTADOS (aqui está a correção) =====

# 1. Crie um placeholder dedicado para os resultados da validação
placeholder_resultados = st.empty()

# 2. Verifique se o botão foi clicado E se existe um arquivo
# (Note que o st.button retorna True quando é clicado)
if validar_button and arquivo:
    
    # 3. Chame sua função de validação
    # Supondo que ela retorne (True/False, "Mensagem")
    aprovado, mensagem = verificar_arte(arquivo, regra) 

    # 4. Use o placeholder para mostrar o resultado
    with placeholder_resultados.container():
        if aprovado:
            st.success(f"✅ ARTE APROVADA! {mensagem}")
        else:
            st.error(f"❌ ARTE REPROVADA! {mensagem}")

# Opcional: Mostre uma mensagem inicial no placeholder se não houver arquivo
elif not arquivo:
    with placeholder_resultados.container():
        st.info("Aguardando o upload de uma arte para iniciar a validação.")
