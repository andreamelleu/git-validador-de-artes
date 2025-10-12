import streamlit as st
from regras import carregar_regras
from streamlit_components import (
    renderizar_cabecalho, 
    renderizar_sidebar_painel, 
    renderizar_area_visualizacao, 
    renderizar_resultados
)

st.set_page_config(page_title="GIT Validador de Artes", layout="wide")


def main():
    """
    Função principal da aplicação GIT Validador de Artes
    """
    # Renderiza cabeçalho
    renderizar_cabecalho()
    
    # Renderiza sidebar e obtém controles
    teatro, regra, arquivo, validar_button = renderizar_sidebar_painel("Teatro dos Grandes Atores", {}, None)
    
    # Renderiza área de visualização
    renderizar_area_visualizacao(regra, arquivo, teatro)
    
    # Renderiza resultados da validação
    renderizar_resultados(validar_button, arquivo, regra)

if __name__ == "__main__":
    main()
