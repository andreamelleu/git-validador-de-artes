# streamlit_components.py
import os
from typing import Dict, Any, Tuple, Optional

import streamlit as st
from regras import carregar_regras, TEATROS_CONFIG

TIPOS_ARQUIVO_PERMITIDOS = ["jpg", "jpeg", "png"]
LOGO_MYWORK = "assets/comuns/logo_mywork_white.png"

MESSAGES = {
    "titulo_principal": "GIT Validador de Artes",
    "texto_intro": """
        <div style='font-size: 0.95em; line-height: 1.6;'>
            Olá, produtor Teatrali, verifique se todas as suas artes estão aprovadas para subir no drive.<br>
            Qualquer dúvida, fale com o Procópio e solicite para ele enviar o que precisar!
        </div>
    """,
    "selecione_teatro": "Selecione o Teatro:",
    "selecione_gabarito": "Selecione o Gabarito:",
    "suba_arte": "Suba a sua Arte:",
    "aguardando_upload": "Aguardando upload...",
    "validar_arte": "Validar Arte",
    "gabarito_nao_encontrado": "Imagem de gabarito não encontrada em:",
    "nenhuma_regra": "Nenhuma regra encontrada para este teatro",
    "upload_antes_validar": "Por favor, faça o upload de uma arte antes de validar.",
    "arte_aprovada": "✅ ARTE APROVADA!",
    "arte_reprovada": "❌ ARTE REPROVADA!",
}

def renderizar_sidebar_painel() -> Tuple[str, Dict[str, Any], Optional[Any], bool]:
    with st.sidebar:
        st.markdown("""
            <style>
                [data-testid="stSidebar"] [data-testid="stImage"] {
                    margin-top: -40px;
                }
                [data-testid="stSidebar"] [data-testid="stImage"] img {
                    width: 200px !important;
                }
            </style>
        """, unsafe_allow_html=True)

        st.image(LOGO_MYWORK)
        st.header(MESSAGES["titulo_principal"])
        st.markdown(MESSAGES["texto_intro"], unsafe_allow_html=True)

        teatros_disponiveis = list(TEATROS_CONFIG.keys())
        teatro_selecionado = st.selectbox(
            MESSAGES["selecione_teatro"],
            options=teatros_disponiveis
        )

        regras_teatro = carregar_regras(teatro_selecionado)
        regra_selecionada: Dict[str, Any] = {}

        if not regras_teatro:
            st.error(MESSAGES["nenhuma_regra"])
        else:
            opcoes_gabarito = {v["descricao"]: k for k, v in regras_teatro.items()}
            descricao_escolhida = st.selectbox(
                MESSAGES["selecione_gabarito"],
                options=opcoes_gabarito.keys()
            )
            if descricao_escolhida:
                chave_regra = opcoes_gabarito[descricao_escolhida]
                regra_selecionada = regras_teatro[chave_regra]

        arquivo_carregado = st.file_uploader(
            MESSAGES["suba_arte"],
            type=TIPOS_ARQUIVO_PERMITIDOS
        )

        botao_validar_clicado = st.button(MESSAGES["validar_arte"], use_container_width=True)

        st.link_button("Fale com o Procópio", "https://wa.me/5521968815522", use_container_width=True)

    return teatro_selecionado, regra_selecionada, arquivo_carregado, botao_validar_clicado

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

def renderizar_area_visualizacao(regra: Dict[str, Any], arquivo: Optional[Any]) -> None:
    if not regra:
        st.info("Selecione um teatro e um gabarito no painel à esquerda para começar.")
        return

    orientacao = regra.get("orientacao", "vertical")

    if orientacao == "horizontal":
        _renderizar_bloco_imagem("Gabarito", regra.get("descricao", ""), regra.get("gabarito_path"), "Gabarito não encontrado")
        st.header("")  # separador visual leve
        _renderizar_bloco_imagem("Sua Arte", f"Arquivo: {arquivo.name}" if arquivo else "", arquivo, MESSAGES["aguardando_upload"])
    else:
        col1, col2 = st.columns(2)
        with col1:
            _renderizar_bloco_imagem("Gabarito", regra.get("descricao", ""), regra.get("gabarito_path"), "Gabarito não encontrado")
        with col2:
            _renderizar_bloco_imagem("Sua Arte", f"Arquivo: {arquivo.name}" if arquivo else "", arquivo, MESSAGES["aguardando_upload"])

def renderizar_resultados(validar_button: bool, arquivo: Optional[Any], regra: Dict[str, Any]) -> None:
    if not validar_button:
        return
    if not arquivo:
        st.warning(MESSAGES["upload_antes_validar"])
        return
    if not regra:
        st.error("Selecione um gabarito antes de validar.")
        return
    try:
        from common_utils import verificar_arte
        aprovado, mensagem = verificar_arte(arquivo, regra)
        if aprovado:
            st.success(f"{MESSAGES['arte_aprovada']} {mensagem}")
        else:
            st.error(f"{MESSAGES['arte_reprovada']}")
            st.info(mensagem)
    except Exception as e:
        st.error(f"Ocorreu um erro inesperado durante a validação: {e}")
