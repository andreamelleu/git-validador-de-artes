# main.py
"""
Aplicação principal do GIT Validador de Artes
Layout horizontal exato conforme layout horizontal.png
"""
import streamlit as st
from streamlit_components import renderizar_sidebar_painel, renderizar_area_visualizacao, renderizar_resultados

def aplicar_estilos_customizados():
    estilos_css = """
        <style>
            [data-testid="stSidebar"] [data-testid="stImage"] img {
                width: 160px !important;
            }

            [data-testid="stSidebar"] p:last-of-type {
                font-size: 0.8em !important;
                color: #A0A0A0 !important;
            }

            [data-testid="stSidebar"] .stLinkButton a {
                background-color: #4F4F5A;
                text-align: center;
                width: 100%;
                border-radius: 6px;
                padding-top: 12px;
                padding-bottom: 12px;
            }

            [data-testid="stMain"] .stBlock {
                gap: 2rem;
            }

            [data-testid="stMain"] .stColumns {
                display: flex !important;
                flex-direction: row !important;
                gap: 2rem !important;
            }

            [data-testid="stMain"] .stColumn {
                flex: 1 !important;
                min-width: 0 !important;
            }

            [data-testid="stImage"] img {
                width: 100% !important;
                height: auto !important;
                max-height: 350px !important;
                object-fit: contain !important;
            }

            html, body {
                overflow: hidden !important;
                height: 100vh !important;
            }

            .stApp {
                background-color: #1a1a1a !important;
            }

            .main .block-container {
                background-color: #1a1a1a !important;
            }

            [data-testid="stSidebar"] {
                background-color: #2c2c34 !important;
            }

            .stMarkdown, .stText, .stSelectbox label, .stFileUploader label {
                color: #ffffff !important;
            }

            [data-testid="stMain"] {
                overflow: hidden !important;
                height: 100vh !important;
            }

            [data-testid="stMain"] .main .block-container {
                padding: 1rem !important;
                max-width: none !important;
                height: 100vh !important;
                display: flex !important;
                flex-direction: column !important;
            }

            [data-testid="stMain"] .stColumns {
                flex: 0 0 auto !important;
                margin-bottom: 1rem !important;
                max-height: 70vh !important;
            }

            .art-placeholder {
                width: 100% !important;
                height: 400px !important;
                background-color: #3a3a3a !important;
                border: 2px dashed #666666 !important;
                border-radius: 8px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                color: #cccccc !important;
                font-size: 1.1em !important;
            }

            .upload-status {
                background-color: #1e3a8a !important;
                color: white !important;
                padding: 15px !important;
                border-radius: 8px !important;
                text-align: center !important;
                font-weight: 500 !important;
                margin-bottom: 15px !important;
            }
        </style>
    """
    st.markdown(estilos_css, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="GIT Validador de Artes",
        page_icon="🎭",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    aplicar_estilos_customizados()

    teatro, regra, arquivo, validar_button = renderizar_sidebar_painel()
    renderizar_area_visualizacao(regra, arquivo)
    renderizar_resultados(validar_button, arquivo, regra)

if __name__ == "__main__":
    main()
