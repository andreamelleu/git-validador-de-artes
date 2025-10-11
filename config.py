"""
Configurações centralizadas para o projeto GIT Validador de Artes
"""
from typing import List, Dict, Any

# Configurações de validação
VALIDATION_CONFIG = {
    "MAX_FILE_SIZE_MB": 10,
    "SUPPORTED_FORMATS": [".jpg", ".jpeg", ".png"],
    "DPI_TOLERANCE": 5,
    "DEFAULT_DPI": 72
}

# Configurações de interface
UI_CONFIG = {
    "SIDEBAR_BG_COLOR": "#2c2c34",
    "LOGO_WIDTH": "240px",
    "PAGE_TITLE": "GIT Validador de Artes",
    "PAGE_LAYOUT": "wide"
}

# Configurações de diretórios
DIRECTORY_CONFIG = {
    "ASSETS_BASE": "assets",
    "TEATROS_PATH": "assets/teatros",
    "GRANDES_ATORES_PATH": "assets/teatros/grandes_atores",
    "DAS_ARTES_PATH": "assets/teatros/das_artes",
    "DEFAULT_IMAGE": "assets/default.png"
}

# Configurações de logging
LOGGING_CONFIG = {
    "LOG_FORMAT": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "LOG_LEVEL": "INFO",
    "LOG_FILE": "logs/validador.log"
}

# Mensagens padronizadas
MESSAGES = {
    "SUCCESS": "Arte aprovada com sucesso!",
    "ERROR_NO_FILE": "Nenhum arquivo fornecido para validação",
    "ERROR_NO_RULE": "Nenhuma regra de validação fornecida",
    "ERROR_FILE_NOT_FOUND": "Arquivo não encontrado",
    "ERROR_PERMISSION": "Sem permissão para acessar o arquivo",
    "ERROR_UNSUPPORTED_FORMAT": "Formato de arquivo não suportado ou arquivo corrompido",
    "ERROR_FILE_TOO_LARGE": "Arquivo muito grande para processar",
    "ERROR_DIMENSIONS": "Dimensões incorretas. Esperado: {expected}px, Encontrado: {actual}px",
    "ERROR_FORMAT": "Formato incorreto. Esperado: {expected}, Encontrado: {actual}",
    "ERROR_COLOR_MODE": "Modo de cor incorreto. Esperado: {expected}, Encontrado: {actual}",
    "ERROR_DPI": "Resolução DPI incorreta. Esperado: {expected}, Encontrado: {actual}",
    "ERROR_FILE_SIZE": "Arquivo muito grande. Tamanho máximo permitido: {max_size}MB",
    "WARNING_NO_GABARITO": "Imagem de gabarito não encontrada em: {path}",
    "INFO_WAITING_UPLOAD": "Aguardando upload...",
    "WARNING_UPLOAD_FIRST": "Por favor, faça o upload de uma arte antes de validar."
}

# Configurações de teatros
TEATROS_CONFIG = {
    "GRANDES_ATORES": {
        "name": "Teatro dos Grandes Atores",
        "path": "grandes_atores",
        "regras": ["divertix_home", "banner_divertix"]
    },
    "DAS_ARTES": {
        "name": "Teatro das Artes", 
        "path": "das_artes",
        "regras": ["site_teatro_home", "tv_teatro_externa"]
    }
}
