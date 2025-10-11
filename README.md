# 🎭 GIT Validador de Artes

Sistema de validação de artes para teatros, desenvolvido com Streamlit e seguindo princípios de código limpo e reutilização (DRY).

## 📋 Funcionalidades

- ✅ **Validação de Imagens**: Verifica dimensões, formato, modo de cor e resolução DPI
- ✅ **Múltiplos Teatros**: Suporte para Teatro dos Grandes Atores e Teatro das Artes
- ✅ **Interface Intuitiva**: Interface responsiva e fácil de usar
- ✅ **Processamento em Lote**: Suporte para arquivos ZIP com múltiplas imagens
- ✅ **Logs de Validação**: Geração de relatórios em CSV
- ✅ **Gabaritos Visuais**: Exibição de gabaritos para comparação

## 🏗️ Estrutura do Projeto

```
git-validador-de-artes/
├── main.py                    # Aplicação principal Streamlit
├── common_utils.py           # Utilitários centralizados
├── regras.py                 # Sistema de regras de validação
├── utils.py                  # Utilitários de processamento
├── streamlit_components.py   # Componentes reutilizáveis UI
├── config.py                 # Configurações centralizadas
├── requirements.txt          # Dependências Python
├── Procfile                  # Configuração para deploy
└── assets/                   # Recursos estáticos
    ├── comuns/              # Imagens comuns (classificações)
    └── teatros/             # Imagens específicas por teatro
        ├── grandes_atores/  # Gabaritos do Teatro dos Grandes Atores
        └── das_artes/       # Gabaritos do Teatro das Artes
```

## 🚀 Instalação e Execução

### Pré-requisitos

- Python 3.8+
- pip

### Instalação

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd git-validador-de-artes
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação**:
   ```bash
   streamlit run main.py
   ```

4. **Acesse no navegador**:
   ```
   http://localhost:8501
   ```

## 📚 Arquitetura

### Princípios Aplicados

- **DRY (Don't Repeat Yourself)**: Eliminação de código duplicado
- **Separation of Concerns**: Responsabilidades bem definidas
- **Single Responsibility**: Cada módulo tem uma função específica
- **Type Hints**: Documentação de tipos para melhor manutenibilidade

### Módulos Principais

#### `common_utils.py`
Utilitários centralizados com funções reutilizáveis:
- `formatar_data_brasileira()`: Formatação de data no padrão brasileiro
- `formatar_data_timestamp()`: Formatação para timestamps
- `verificar_arte()`: Validação completa de imagens
- `processar_arquivo_com_erro()`: Tratamento padronizado de erros
- `verificar_existencia_imagem()`: Verificação de caminhos de imagens

#### `regras.py`
Sistema de regras de validação com classes:
- `RegraValidacao`: Dataclass para representar regras
- `TeatroRegras`: Factory para criar regras por teatro
- `carregar_regras()`: Carregamento dinâmico de regras

#### `streamlit_components.py`
Componentes reutilizáveis de interface:
- `renderizar_sidebar_estilo()`: Estilos CSS da sidebar
- `renderizar_cabecalho()`: Cabeçalho principal
- `renderizar_sidebar_painel()`: Controles da sidebar
- `renderizar_area_visualizacao()`: Área de imagens
- `renderizar_resultados()`: Área de resultados

#### `utils.py`
Utilitários de processamento:
- `processar_arquivo()`: Processamento de arquivos individuais e ZIP
- `salvar_log()`: Geração de logs em CSV

## 🎯 Regras de Validação

### Teatro dos Grandes Atores

#### Divertix Home do Site
- **Dimensões**: 370 x 550 px
- **Formato**: JPEG, PNG
- **Modo de Cor**: RGB
- **Orientação**: Vertical

#### Banner Divertix
- **Dimensões**: 15059 x 14173 px (255 x 240 cm)
- **Resolução**: 150 DPI
- **Formato**: JPEG
- **Modo de Cor**: CMYK
- **Orientação**: Horizontal

### Teatro das Artes

#### Home do Site
- **Dimensões**: 768 x 1024 px
- **Formato**: JPEG, PNG
- **Modo de Cor**: RGB
- **Orientação**: Vertical

#### TV Teatro Externa
- **Dimensões**: 2160 x 3840 px
- **Formato**: JPEG, PNG
- **Modo de Cor**: RGB
- **Orientação**: Vertical

## 🔧 Configuração

### Arquivo `config.py`

Centraliza todas as configurações do sistema:

```python
# Limites de validação
VALIDATION_CONFIG = {
    "MAX_FILE_SIZE_MB": 10,
    "SUPPORTED_FORMATS": [".jpg", ".jpeg", ".png"],
    "DPI_TOLERANCE": 5
}

# Configurações de interface
UI_CONFIG = {
    "SIDEBAR_BG_COLOR": "#2c2c34",
    "PAGE_TITLE": "GIT Validador de Artes"
}
```

## 📊 Logs e Relatórios

O sistema gera logs de validação em formato CSV com:
- Nome do arquivo
- Resultado da validação (aprovado/reprovado)
- Mensagem de erro (se aplicável)
- Timestamp da validação

## 🚀 Deploy

### Heroku

1. **Configure o Procfile**:
   ```
   web: streamlit run main.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Deploy**:
   ```bash
   git push heroku main
   ```

### Docker

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]
```

## 🧪 Testes

Para executar os testes:

```bash
# Instalar dependências de teste
pip install pytest pytest-cov

# Executar testes
pytest

# Com cobertura
pytest --cov=.
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Changelog

### v1.0.0
- ✅ Implementação inicial do validador
- ✅ Suporte para múltiplos teatros
- ✅ Interface Streamlit responsiva
- ✅ Sistema de regras configurável
- ✅ Processamento em lote (ZIP)
- ✅ Geração de logs CSV
- ✅ Refatoração seguindo princípio DRY

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Equipe

- **Desenvolvimento**: Equipe de Desenvolvimento
- **Design**: Equipe de Design
- **Testes**: Equipe de QA

## 📞 Suporte

Para suporte ou dúvidas, entre em contato:
- Email: suporte@exemplo.com
- Issues: [GitHub Issues](https://github.com/exemplo/validador-artes/issues)

---

*Desenvolvido com ❤️ para facilitar a validação de artes teatrais*
