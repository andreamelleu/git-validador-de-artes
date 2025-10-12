import streamlit as st
from regras import carregar_regras
from streamlit_components import (
    renderizar_cabecalho,
    renderizar_sidebar_painel,
    renderizar_area_visualizacao,
    renderizar_resultados
)


# === CONFIGURAÇÕES GERAIS DO APP ===
st.set_page_config(
    page_title="GIT Validador de Artes",
    layout="wide",
    page_icon="generated-icon-black.svg",  # ícone SVG (favicon)
)


def main():
    """Função principal da aplicação GIT Validador de Artes"""

    # Renderiza cabeçalho com logo automática e texto introdutório
    renderizar_cabecalho()

    # Renderiza painel lateral e coleta seleções
    teatro, regra, arquivo, validar_button = renderizar_sidebar_painel(
        teatro_inicial="Teatro dos Grandes Atores",
        regras={},
        arquivo=None
    )

    # Área de visualização principal
    renderizar_area_visualizacao(regra, arquivo, teatro)

    # Resultados da validação
    renderizar_resultados(validar_button, arquivo, regra)


if __name__ == "__main__":
    main()
