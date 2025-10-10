import os
import zipfile
import io
import pandas as pd
import datetime
from regras import verificar_arte
from PIL import Image

def processar_arquivo(arquivo):
    logs = []

    if arquivo.name.endswith(".zip"):
        # Processa arquivos ZIP com imagens dentro
        with zipfile.ZipFile(arquivo, 'r') as zip_ref:
            for file_name in zip_ref.namelist():
                if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
                    with zip_ref.open(file_name) as file:
                        try:
                            resultado = verificar_arte(file)
                            logs.append({"arquivo": file_name, "resultado": resultado})
                        except Exception as e:
                            logs.append({"arquivo": file_name, "resultado": f"Erro ao processar: {str(e)}"})
    else:
        # Processa imagem individual
        try:
            resultado = verificar_arte(arquivo)
            logs.append({"arquivo": arquivo.name, "resultado": resultado})
        except Exception as e:
            logs.append({"arquivo": arquivo.name, "resultado": f"Erro ao processar: {str(e)}"})

    return logs

def salvar_log(logs):
    # Cria DataFrame
    df = pd.DataFrame(logs)

    # Gera nome do arquivo com timestamp
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"logs_validacao_{data_hora}.csv"

    # Salva como CSV em memória (para download no Streamlit)
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    return nome_arquivo, csv_buffer
