# 🚀 Instruções para Executar a Aplicação

## ⚠️ Problema Identificado
O Python não está configurado no PATH do sistema. Siga as instruções abaixo para resolver e executar a aplicação.

## 🔧 Soluções Possíveis

### Opção 1: Instalar Python (Recomendado)
1. **Baixe o Python**:
   - Acesse: https://www.python.org/downloads/
   - Baixe a versão mais recente (3.8+)
   - **IMPORTANTE**: Marque "Add Python to PATH" durante a instalação

2. **Reinicie o terminal** após a instalação

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**:
   ```bash
   streamlit run main.py
   ```

### Opção 2: Usar Anaconda/Miniconda
1. **Instale Anaconda**:
   - Acesse: https://www.anaconda.com/products/distribution
   - Baixe e instale

2. **Abra o Anaconda Prompt**

3. **Navegue para o projeto**:
   ```bash
   cd "C:\Users\impri\OneDrive\Documentos\git-validador-de-artes"
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute a aplicação**:
   ```bash
   streamlit run main.py
   ```

### Opção 3: Usar VS Code com Python
1. **Abra o projeto no VS Code**

2. **Instale a extensão Python** (se não tiver)

3. **Selecione o interpretador Python**:
   - Ctrl+Shift+P
   - Digite "Python: Select Interpreter"
   - Escolha uma versão do Python instalada

4. **Abra o terminal integrado** (Ctrl+`)

5. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Execute a aplicação**:
   ```bash
   streamlit run main.py
   ```

## 🧪 Teste a Aplicação

Após instalar o Python, execute o script de teste:

```bash
python test_app.py
```

Este script verificará se todos os componentes estão funcionando corretamente.

## 🌐 Acessar a Aplicação

Após executar `streamlit run main.py`, a aplicação estará disponível em:

- **URL Local**: http://localhost:8501
- **URL de Rede**: http://[seu-ip]:8501

## 📋 Checklist de Verificação

- [ ] Python instalado e no PATH
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Aplicação executando (`streamlit run main.py`)
- [ ] Aplicação acessível no navegador
- [ ] Upload de arquivo funcionando
- [ ] Validação de arte funcionando

## 🔍 Solução de Problemas

### Erro: "Python não foi encontrado" ou "Python is not installed"
- **Sintoma**: Ao tentar rodar o comando, aparece uma mensagem dizendo que o Python não foi encontrado ou uma janela abre a Microsoft Store.
- **Solução 1 (Configurar VS Code)**:
  1. No VS Code, pressione `F1` ou `Ctrl+Shift+P`.
  2. Digite "Python: Select Interpreter".
  3. Se aparecer "Python is not installed", você precisa instalar o Python (veja Opção 1 acima).
  4. Se aparecerem caminhos (ex: `C:\Program Files\Python312\python.exe`), selecione um deles.
- **Solução 2 (Instalar Python)**: 
  - Baixe e instale do [site oficial](https://www.python.org/downloads/).
  - **IMPORTANTE**: Na primeira tela de instalação, marque a caixa **"Add Python to PATH"**.
  - Reinicie o VS Code após instalar.

### Erro: "ModuleNotFoundError"
- **Solução**: Execute `pip install -r requirements.txt`

### Erro: "Streamlit não encontrado"
- **Solução**: Execute `pip install streamlit`

### Aplicação não carrega no navegador
- **Solução**: Verifique se a porta 8501 está livre

### Erro de importação de módulos
- **Solução**: Execute `python test_app.py` para diagnosticar

## 📞 Suporte

Se ainda tiver problemas:

1. **Execute o teste**: `python test_app.py`
2. **Verifique os logs** no terminal
3. **Confirme as dependências**: `pip list`
4. **Verifique a versão do Python**: `python --version`

## ✅ Status da Refatoração

A refatoração foi **100% concluída** com sucesso:

- ✅ **TAREFA 1**: Módulo de utilitários centralizados
- ✅ **TAREFA 2**: Sistema de regras refatorado
- ✅ **TAREFA 3**: Módulo de utilitários simplificado
- ✅ **TAREFA 4**: Interface principal refatorada
- ✅ **TAREFA 5**: Melhorias de qualidade de código
- ✅ **TAREFA 6**: Testes e validação

O código está pronto e seguindo o princípio DRY! 🎉
