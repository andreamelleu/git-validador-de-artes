# main.py
"""
Aplicação principal do GIT Validador de Artes
Layout horizontal exato conforme layout horizontal.png
"""
import os
from dotenv import load_dotenv
import streamlit as st
from streamlit_components import renderizar_sidebar_painel, renderizar_area_visualizacao, renderizar_resultados

# Carrega variáveis de ambiente do arquivo .env (Supabase credentials)
load_dotenv()

def aplicar_estilos_customizados():
    estilos_css = """
        <style>
            [data-testid="stSidebar"] [data-testid="stImage"] img {
                width: 160px !important;
            }

            [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
                font-size: 1.1rem !important;
                color: #ffffff !important;
            }

            [data-testid="stSidebar"] h1,
            [data-testid="stSidebar"] h2,
            [data-testid="stSidebar"] h3,
            [data-testid="stSidebar"] h4,
            [data-testid="stSidebar"] h5,
            [data-testid="stSidebar"] h6 {
                color: #ffffff !important;
            }

            [data-testid="stSidebar"] .stMarkdown p {
                font-size: 1.1rem !important;
                line-height: 1.5 !important;
                color: #ffffff !important;
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

            /* RESTORE CLEAN LOOK (Transparent Header) */
            header[data-testid="stHeader"] {
                background: transparent !important;
            }
            header[data-testid="stHeader"] > div {
                 background: transparent !important;
            }
            
            /* Remove standard padding to use full 100% space */
            .main .block-container {
                padding-top: 1rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                max-width: 100% !important;
            }

            /* FORCE SIDEBAR TOGGLE VISIBILITY (Custom Style) */
            [data-testid="collapsedControl"] {
                display: block !important;
                color: #ffffff !important;
                position: fixed !important;
                top: 0.5rem !important;
                left: 0.5rem !important;
                z-index: 1000002 !important;
                background-color: #333333 !important;
                border-radius: 8px !important;
                padding: 0.4rem !important;
                width: 3rem !important;
                height: 3rem !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3) !important;
                transition: transform 0.2s !important;
            }
            [data-testid="collapsedControl"]:hover {
                background-color: #555555 !important;
                transform: scale(1.1);
            }
            
            [data-testid="collapsedControl"] svg {
                fill: #ffffff !important;
                width: 1.5rem !important;
                height: 1.5rem !important;
            }

            /* FORCE EXPAND BUTTON VISIBILITY */
            [data-testid="stExpandSidebarButton"] {
                display: block !important;
                position: fixed !important;
                top: 0.5rem !important;
                left: 0.5rem !important;
                z-index: 1000002 !important;
                background-color: #333333 !important;
                border-radius: 8px !important;
                padding: 0.6rem !important;
                width: auto !important;
                height: auto !important;
                min-width: 3rem !important;
                min-height: 3rem !important;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3) !important;
            }
            
            [data-testid="stExpandSidebarButton"]:hover {
                background-color: #555555 !important;
            }
            
            [data-testid="stExpandSidebarButton"] svg {
                fill: #ffffff !important;
                width: 1.5rem !important;
                height: 1.5rem !important;
            }

            /* FORCE ALL MAIN AREA TEXT TO WHITE */
            [data-testid="stMain"] h1,
            [data-testid="stMain"] h2,
            [data-testid="stMain"] h3,
            [data-testid="stMain"] h4,
            [data-testid="stMain"] h5,
            [data-testid="stMain"] h6,
            [data-testid="stMain"] p,
            [data-testid="stMain"] span,
            [data-testid="stMain"] div,
            [data-testid="stMain"] label,
            [data-testid="stMain"] .stMarkdown,
            [data-testid="stMain"] [data-testid="stMarkdownContainer"],
            [data-testid="stMain"] [data-testid="stText"] {
                color: #ffffff !important;
            }

            /* Hide Scrollbar in Sidebar */
            section[data-testid="stSidebar"] > div {
                scrollbar-width: none;
                -ms-overflow-style: none;
            }
            section[data-testid="stSidebar"] > div::-webkit-scrollbar {
                display: none;
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

            /* Header and Sidebar hacks removed to ensure stability */
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
            
            /* Hide "Manage app" menu (Streamlit Cloud) */
            [data-testid="manage-app-button"] {
                display: none !important;
            }
            /* button[kind="header"] {
                display: none !important;
            } REMOVED TO FIX SIDEBAR TOGGLE VISIBILITY */

            /* Disable collapsing by dragging (if applicable in some versions) */
            [data-testid="stSidebar"] {
                 min-width: 336px !important;
                 max-width: 336px !important;
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

            /* HACK: Translate "Drag and drop files here" to Portuguese */
            /* Hide the original text span ("Drag and drop files here") */
            [data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"] > div > div > span {
                display: none !important;
            }
            
            /* REMOVED injected text "Arraste seus arquivos..." as requested */
            /* File uploader is now handled by custom HTML button in streamlit_components.py */

            /* FORCE BLACK TEXT ON WHITE BUTTONS IN SIDEBAR */
            [data-testid="stSidebar"] [data-testid="stLinkButton"] a,
            [data-testid="stSidebar"] button[kind="secondary"] {
                background-color: #ffffff !important;
                border: 1px solid #cccccc !important;
            }

            [data-testid="stSidebar"] [data-testid="stLinkButton"] a *,
            [data-testid="stSidebar"] [data-testid="stLinkButton"] a, 
            [data-testid="stSidebar"] button[kind="secondary"] *,
            [data-testid="stSidebar"] button[kind="secondary"] {
                 color: #000000 !important; /* Black Text */
            }
            
            /* Tooltip Fix (in case invisible) */
            div[data-baseweb="tooltip"], div[role="tooltip"] {
                background-color: #333333 !important;
                color: #ffffff !important; 
            }

            /* Ensure the limit text (Small) inside the box is also visible/dark */
            [data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"] small {
                color: #555555 !important;
            }

            /* Fix Caption text in Sidebar (below uploader) - Must be WHITE and LARGER */
            [data-testid="stSidebar"] [data-testid="stCaption"],
            [data-testid="stSidebar"] div[data-testid="caption"],
            [data-testid="stSidebar"] .stCaption {
                color: #ffffff !important;
                font-size: 1.1em !important;
                opacity: 1 !important;
                line-height: 1.4 !important;
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

    try:
        teatro, regra, arquivos_raw, validar_button = renderizar_sidebar_painel()
    except Exception as e:
        st.error(f"Erro Crítico ao renderizar sidebar: {e}")
        import traceback
        st.code(traceback.format_exc())
        st.stop()
    
    # Inicializa conjunto de arquivos removidos se ainda não existir
    if "removed_files" not in st.session_state:
        st.session_state["removed_files"] = set()
        
    # Filtra os arquivos (remove os que estão na "lixeira" temporária)
    arquivos = [a for a in arquivos_raw if (a.name, a.size) not in st.session_state["removed_files"]]
    
    
    renderizar_area_visualizacao(regra, arquivos)
    renderizar_resultados(validar_button, arquivos, regra)

if __name__ == "__main__":
    main()
