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
                max-width: 100% !important;
                object-fit: contain !important;
            }
            
            [data-testid="stMain"] .stImage {
                width: 100% !important;
            }

            html, body {
                overflow: auto !important;
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

            /* Remove top white bar and header */
            header[data-testid="stHeader"] {
                display: none !important;
            }
            
            /* Remove standard padding to use full 100% space */
            .main .block-container {
                padding-top: 1rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                max-width: 100% !important;
            }

            /* Fix styles from previous step */
            .stMarkdown, .stText, .stSelectbox label, .stFileUploader label, h1, h2, h3, p {
                color: #ffffff !important;
            }

            /* Ensure input text remains visible (usually black on white) */
            div[data-baseweb="select"] span {
                color: #31333F !important;
            }
            
            /* Fix for the selected value in the dropdown */
            div[data-testid="stSelectbox"] div[data-baseweb="select"] div {
                color: #31333F !important;
            }

            [data-testid="stMain"] {
                overflow: auto !important;
                height: 100vh !important;
                background-color: #1a1a1a !important;
            }
            
            /* Remove gap at top of sidebar and fix width */
             section[data-testid="stSidebar"] {
                top: 0 !important; 
                margin-top: 0 !important;
                width: 400px !important;
                min-width: 400px !important;
            }
            
            /* Hide Sidebar Toggle (arrows) and Toolbar */
            [data-testid="collapsedControl"] {
                display: none !important;
            }
            [data-testid="stToolbar"] {
                display: none !important;
            }
            
            /* Hide Footer with source code link */
            footer {
                display: none !important;
            }
            [data-testid="stStatusWidget"] {
                display: none !important;
            }

            /* Hide Scrollbar in Sidebar */
            section[data-testid="stSidebar"] > div {
                scrollbar-width: none; /* Firefox */
                -ms-overflow-style: none;  /* IE 10+ */
            }
            section[data-testid="stSidebar"] > div::-webkit-scrollbar {
                display: none; /* Chrome/Safari/Webkit */
                width: 0px;
                background: transparent;
            }

            /* Limit image size in main area to avoid huge posters */
            [data-testid="stMain"] [data-testid="stImage"] img {
                max-height: 350px !important;
                width: auto !important;
                object-fit: contain !important;
            }
            [data-testid="stMain"] [data-testid="stImage"] {
                display: flex !important;
                justify-content: center !important;
            }
            
            /* Fix visibility of filenames in sidebar file uploader */
            [data-testid="stFileUploader"] div[role="listitem"] div,
            [data-testid="stFileUploader"] div[role="listitem"] span {
                color: #ffffff !important;
            }
            [data-testid="stFileUploader"] div[role="listitem"] small {
                 color: #cccccc !important;
            }
            
            /* Fix "Browse files" button text (Secondary button needs dark text) */
            [data-testid="stFileUploader"] button[kind="secondary"] {
                color: #31333F !important;
            }
            [data-testid="stFileUploader"] button[kind="secondary"] * {
                color: #31333F !important;
            }

            /* Fix UPLOADED FILENAMES - Target everything in the list items (ul/li usually) */
            [data-testid="stFileUploader"] ul,
            [data-testid="stFileUploader"] li,
            [data-testid="stFileUploader"] li div,
            [data-testid="stFileUploader"] li span,
            [data-testid="stFileUploader"] li small {
                color: #ffffff !important;
            }
            
            /* Fallback: If not ul/li, target the second main div (usually the list) */
            [data-testid="stFileUploader"] > div:nth-child(2) * {
                 color: #ffffff !important;
            }

            /* Specific fix for "X" (Delete) button inside list item */
            [data-testid="stFileUploader"] button[kind="tertiary"], /* Delete is often tertiary */
            [data-testid="stFileUploader"] button[kind="header"]    /* Or header style? */
            {
                 color: #ff4b4b !important;
                 border: none !important;
            }
            /* Explicit delete button ID again */
            button[data-testid="stFileUploaderDeleteBtn"] {
                 color: #ff4b4b !important;
            }
            button[data-testid="stFileUploaderDeleteBtn"] svg {
                fill: #ff4b4b !important;
                stroke: #ff4b4b !important;
            }

            /* Fix Expanders - FORCE DARK THEME STYLE (Background Dark + Text White) */
            
            /* Header (Summary) */
            [data-testid="stExpander"] {
                background-color: transparent !important;
                border: none !important;
            }
            [data-testid="stExpander"] summary {
                background-color: #ffffff !important;
                color: #000000 !important; /* Forces Black Text */
                border: 1px solid #cccccc !important;
                border-radius: 5px;
            }
            [data-testid="stExpander"] summary p, 
            [data-testid="stExpander"] summary span,
            [data-testid="stExpander"] summary div {
                color: #000000 !important;
            }
            [data-testid="stExpander"] summary:hover {
                color: #ffffff !important;
                background-color: #000000 !important;
            }

            /* Content Body (Details) */
            [data-testid="stExpanderDetails"] {
                background-color: transparent !important; /* Inherit main dark bg */
                color: #ffffff !important;
            }
            [data-testid="stExpanderDetails"] p,
            [data-testid="stExpanderDetails"] div, 
            [data-testid="stExpanderDetails"] span,
            [data-testid="stExpanderDetails"] ul,
            [data-testid="stExpanderDetails"] li {
                color: #ffffff !important;
            }
            
            /* Ensure Alerts (Error/Success) keep their readable text colors */
            [data-testid="stAlert"] p, [data-testid="stAlert"] div {
                 color: inherit !important;
            }

            /* HOVER STYLES - "Hover Preto Letras Brancas Sempre" */
            
            /* Buttons Standard (Normal State) - Includes Download Button */
            div.stButton > button, div.stDownloadButton > button {
                color: #ffffff !important; /* White Text */
                background-color: #000000 !important; /* Black Background */
                border-color: #ffffff !important; /* White Border */
            }
            div.stButton > button *, div.stDownloadButton > button * {
                color: #ffffff !important;
            }
            /* Specifically target the text inside the download button */
            div.stDownloadButton > button p {
                color: #ffffff !important;
            }

            /* Buttons Hover - Includes Download Button */
            div.stButton > button:hover, div.stDownloadButton > button:hover {
                background-color: #ffffff !important;
                color: #000000 !important;
                border-color: #000000 !important;
            }
            div.stButton > button:hover *, div.stDownloadButton > button:hover * {
                color: #000000 !important;
            }
            div.stDownloadButton > button:hover p {
                color: #000000 !important;
            }
            
            /* Expander Header Hover */
            [data-testid="stExpander"] summary:hover {
                background-color: #000000 !important;
                color: #ffffff !important;
            }
            [data-testid="stExpander"] summary:hover p,
            [data-testid="stExpander"] summary:hover span,
            [data-testid="stExpander"] summary:hover svg {
                color: #ffffff !important;
                fill: #ffffff !important;
            }


        </style>
    """
    st.markdown(estilos_css, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="GIT Validador de Artes",
        page_icon="favicon.ico",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    aplicar_estilos_customizados()

    teatro, regra, arquivos_raw, validar_button = renderizar_sidebar_painel()
    
    # Inicializa conjunto de arquivos removidos se ainda não existir
    if "removed_files" not in st.session_state:
        st.session_state["removed_files"] = set()
        
    # Filtra os arquivos (remove os que estão na "lixeira" temporária)
    arquivos = [a for a in arquivos_raw if (a.name, a.size) not in st.session_state["removed_files"]]
    
    renderizar_area_visualizacao(regra, arquivos)
    renderizar_resultados(validar_button, arquivos, regra)

if __name__ == "__main__":
    main()
