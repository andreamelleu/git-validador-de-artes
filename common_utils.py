"""
Módulo de utilitários comuns para o projeto GIT Validador de Artes
Centraliza funções reutilizáveis seguindo o princípio DRY
"""
import datetime
from typing import Tuple, Any
from PIL import Image
import os


def formatar_data_brasileira() -> str:
    """Retorna a data atual formatada no padrão brasileiro (dd/mm/yyyy)"""
    return datetime.date.today().strftime("%d/%m/%Y")


def formatar_data_timestamp() -> str:
    """Retorna data e hora atual formatada para timestamp (yyyy-mm-dd_hh-mm-ss)"""
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def verificar_arte(arquivo, regra: dict) -> Tuple[bool, str]:
    """
    Valida uma arte de acordo com as regras especificadas
    
    Args:
        arquivo: Arquivo de imagem a ser validado
        regra: Dicionário com as regras de validação
        
    Returns:
        Tuple[bool, str]: (aprovado, mensagem)
    """
    # Validação de entrada
    if not arquivo:
        return False, "Nenhum arquivo fornecido para validação"
    
    if not regra:
        return False, "Nenhuma regra de validação fornecida"
    
    try:
        # Abrir a imagem
        if hasattr(arquivo, 'read'):
            # Se é um arquivo upload do Streamlit
            arquivo.seek(0)
            img = Image.open(arquivo)
        else:
            # Se é um caminho de arquivo
            img = Image.open(arquivo)
        
        # Verificar se a imagem foi carregada corretamente
        if not img:
            return False, "Não foi possível carregar a imagem"
        
        # Verificar dimensões
        largura, altura = img.size
        largura_esperada = regra.get('largura')
        altura_esperada = regra.get('altura')
        
        if largura_esperada and altura_esperada:
            if largura != largura_esperada or altura != altura_esperada:
                return False, f"Dimensões incorretas. Esperado: {largura_esperada}x{altura_esperada}px, Encontrado: {largura}x{altura}px"
        
        # Verificar formato
        formato_atual = img.format
        formatos_aceitos = regra.get('formato_final', [])
        
        if formatos_aceitos and formato_atual not in formatos_aceitos:
            return False, f"Formato incorreto. Esperado: {', '.join(formatos_aceitos)}, Encontrado: {formato_atual}"
        
        # Verificar modo de cor
        modo_cor_atual = img.mode
        modo_cor_esperado = regra.get('modo_cor')
        
        if modo_cor_esperado and modo_cor_atual != modo_cor_esperado:
            return False, f"Modo de cor incorreto. Esperado: {modo_cor_esperado}, Encontrado: {modo_cor_atual}"
        
        # Verificar resolução DPI (se especificada)
        dpi_esperado = regra.get('resolucao_dpi')
        if dpi_esperado:
            dpi_atual = img.info.get('dpi', (72, 72))[0]  # DPI padrão se não especificado
            if abs(dpi_atual - dpi_esperado) > 5:  # Tolerância de 5 DPI
                return False, f"Resolução DPI incorreta. Esperado: {dpi_esperado}, Encontrado: {dpi_atual}"
        
        # Verificar tamanho do arquivo (limite de 10MB)
        if hasattr(arquivo, 'size') and arquivo.size > 10 * 1024 * 1024:
            return False, "Arquivo muito grande. Tamanho máximo permitido: 10MB"
        
        return True, "Arte aprovada com sucesso!"
        
    except FileNotFoundError:
        return False, "Arquivo não encontrado"
    except PermissionError:
        return False, "Sem permissão para acessar o arquivo"
    except Image.UnidentifiedImageError:
        return False, "Formato de arquivo não suportado ou arquivo corrompido"
    except MemoryError:
        return False, "Arquivo muito grande para processar"
    except Exception as e:
        return False, f"Erro ao processar imagem: {str(e)}"


def processar_arquivo_com_erro(arquivo, funcao_processamento) -> dict:
    """
    Processa um arquivo com tratamento de erro padronizado
    
    Args:
        arquivo: Arquivo a ser processado
        funcao_processamento: Função que processa o arquivo
        
    Returns:
        dict: Resultado do processamento com tratamento de erro
    """
    try:
        resultado = funcao_processamento(arquivo)
        return {"arquivo": getattr(arquivo, 'name', 'arquivo'), "resultado": resultado}
    except Exception as e:
        return {"arquivo": getattr(arquivo, 'name', 'arquivo'), "resultado": f"Erro ao processar: {str(e)}"}


def verificar_existencia_imagem(caminho: str, nome_arquivo: str) -> str:
    """
    Verifica se uma imagem existe e retorna o caminho correto
    
    Args:
        caminho: Caminho base da imagem
        nome_arquivo: Nome do arquivo
        
    Returns:
        str: Caminho completo se existir, senão caminho padrão
    """
    # Primeiro tenta o caminho exato
    caminho_completo = os.path.join("assets", "teatros", caminho, nome_arquivo)
    if os.path.exists(caminho_completo):
        return caminho_completo
    
    # Se não encontrar, procura por arquivos similares na pasta
    pasta_teatro = os.path.join("assets", "teatros", caminho)
    if os.path.exists(pasta_teatro):
        for arquivo in os.listdir(pasta_teatro):
            if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Remove a extensão do nome_arquivo para comparar
                nome_sem_ext = os.path.splitext(nome_arquivo)[0]
                arquivo_sem_ext = os.path.splitext(arquivo)[0]
                
                # Verifica se o nome base é similar
                if nome_sem_ext.lower() in arquivo_sem_ext.lower() or arquivo_sem_ext.lower() in nome_sem_ext.lower():
                    return os.path.join(pasta_teatro, arquivo)
    
    return f"assets/default.png"
