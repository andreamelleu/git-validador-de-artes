"""
Script de teste para verificar se a aplicação está funcionando
"""
import sys
import os

def test_imports():
    """Testa se todos os imports estão funcionando"""
    try:
        print("Testando imports...")
        
        # Testa imports básicos
        import datetime
        print("OK - datetime importado")
        
        # Testa imports do projeto
        from regras import carregar_regras
        print("OK - regras importado")
        
        from common_utils import verificar_arte, formatar_data_brasileira
        print("OK - common_utils importado")
        
        from streamlit_components import renderizar_cabecalho
        print("OK - streamlit_components importado")
        
        # Testa streamlit
        import streamlit as st
        print("OK - streamlit importado")
        
        return True
        
    except Exception as e:
        print(f"ERRO ao importar: {e}")
        return False

def test_regras():
    """Testa se as regras estão funcionando"""
    try:
        print("\nTestando regras...")
        
        from regras import carregar_regras
        
        # Testa carregamento de regras
        regras_grandes_atores = carregar_regras("Teatro dos Grandes Atores")
        print(f"OK - Regras Grandes Atores: {len(regras_grandes_atores)} regras")
        
        regras_das_artes = carregar_regras("Teatro das Artes")
        print(f"OK - Regras Das Artes: {len(regras_das_artes)} regras")
        
        return True
        
    except Exception as e:
        print(f"ERRO nas regras: {e}")
        return False

def test_utils():
    """Testa se as funções utilitárias estão funcionando"""
    try:
        print("\nTestando utilitários...")
        
        from common_utils import formatar_data_brasileira, formatar_data_timestamp
        
        data_br = formatar_data_brasileira()
        print(f"OK - Data brasileira: {data_br}")
        
        timestamp = formatar_data_timestamp()
        print(f"OK - Timestamp: {timestamp}")
        
        return True
        
    except Exception as e:
        print(f"ERRO nos utilitarios: {e}")
        return False

def main():
    """Função principal de teste"""
    print("Iniciando testes da aplicacao GIT Validador de Artes\n")
    
    # Testa imports
    if not test_imports():
        print("\nERRO - Falha nos imports. Verifique as dependencias.")
        return False
    
    # Testa regras
    if not test_regras():
        print("\nERRO - Falha nas regras. Verifique o arquivo regras.py.")
        return False
    
    # Testa utilitários
    if not test_utils():
        print("\nERRO - Falha nos utilitarios. Verifique o arquivo common_utils.py.")
        return False
    
    print("\nSUCESSO - Todos os testes passaram! A aplicacao esta pronta para executar.")
    print("\nPara executar a aplicacao, use:")
    print("C:\\Users\\impri\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\streamlit.exe run main.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
