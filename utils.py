import zipfile
import io
import pandas as pd
from common_utils import verificar_arte, processar_arquivo_com_erro, formatar_data_timestamp


def processar_arquivo(arquivo, regra=None):
    """
    Processa um arquivo (individual ou ZIP) e retorna logs de validação
    
    Args:
        arquivo: Arquivo a ser processado
        regra: Regra de validação (opcional)
        
    Returns:
        list: Lista de logs com resultados da validação
    """
    logs = []

    if arquivo.name.endswith(".zip"):
        # Processa arquivos ZIP com imagens dentro
        with zipfile.ZipFile(arquivo, 'r') as zip_ref:
            for file_name in zip_ref.namelist():
                if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
                    with zip_ref.open(file_name) as file:
                        # Usa função centralizada para processamento com erro
                        resultado = processar_arquivo_com_erro(
                            file, 
                            lambda f: verificar_arte(f, regra) if regra else verificar_arte(f, {})
                        )
                        resultado["arquivo"] = file_name
                        logs.append(resultado)
    else:
        # Processa imagem individual usando função centralizada
        resultado = processar_arquivo_com_erro(
            arquivo,
            lambda f: verificar_arte(f, regra) if regra else verificar_arte(f, {})
        )
        logs.append(resultado)

    return logs


def salvar_log(logs):
    """
    Salva logs de validação em formato CSV
    
    Args:
        logs: Lista de logs para salvar
        
    Returns:
        tuple: (nome_arquivo, buffer_csv)
    """
    # Cria DataFrame
    df = pd.DataFrame(logs)

    # Gera nome do arquivo com timestamp usando função centralizada
    data_hora = formatar_data_timestamp()
    nome_arquivo = f"logs_validacao_{data_hora}.csv"

    # Salva como CSV em memória (para download no Streamlit)
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    return nome_arquivo, csv_buffer
