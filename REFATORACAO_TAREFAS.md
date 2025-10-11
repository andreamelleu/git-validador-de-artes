# 🚀 Plano de Refatoração - GIT Validador de Artes

## 📋 Visão Geral
Este documento contém todas as tarefas necessárias para refatorar o projeto seguindo o princípio DRY (Don't Repeat Yourself) e melhorar a estrutura do código.

---

## 🎯 TAREFA 1: Criar Módulo de Utilitários Centralizados

### 1.1 Criar arquivo `common_utils.py`
- [ ] **1.1.1** Criar função `formatar_data_brasileira()` para data no formato dd/mm/yyyy
- [ ] **1.1.2** Criar função `formatar_data_timestamp()` para timestamp yyyy-mm-dd_hh-mm-ss
- [ ] **1.1.3** Criar função `verificar_arte(arquivo, regra)` com validação completa:
  - [ ] Verificar dimensões (largura x altura)
  - [ ] Verificar formato de arquivo (JPEG, PNG)
  - [ ] Verificar modo de cor (RGB, CMYK)
  - [ ] Verificar resolução DPI (se especificada)
  - [ ] Retornar tupla (aprovado: bool, mensagem: str)
- [ ] **1.1.4** Criar função `processar_arquivo_com_erro()` para tratamento padronizado de erros
- [ ] **1.1.5** Criar função `verificar_existencia_imagem()` para verificar caminhos de imagens
- [ ] **1.1.6** Adicionar type hints e docstrings completas

### 1.2 Testar funções utilitárias
- [ ] **1.2.1** Testar formatação de datas
- [ ] **1.2.2** Testar validação de imagens com diferentes formatos
- [ ] **1.2.3** Testar tratamento de erros

---

## 🎯 TAREFA 2: Refatorar Sistema de Regras

### 2.1 Criar estrutura de classes para regras
- [ ] **2.1.1** Criar dataclass `RegraValidacao` com campos:
  - [ ] descricao: str
  - [ ] largura: int
  - [ ] altura: int
  - [ ] formato_final: Tuple[str, ...]
  - [ ] modo_cor: str
  - [ ] gabarito_img: str
  - [ ] orientacao: str
  - [ ] resolucao_dpi: Optional[int] = None
- [ ] **2.1.2** Adicionar método `to_dict()` na classe `RegraValidacao`
- [ ] **2.1.3** Criar classe `TeatroRegras` com métodos estáticos para criar regras
- [ ] **2.1.4** Implementar métodos para cada tipo de regra:
  - [ ] `criar_regra_divertix_home()`
  - [ ] `criar_regra_banner_divertix()`
  - [ ] `criar_regra_site_teatro_home()`
  - [ ] `criar_regra_tv_teatro_externa()`

### 2.2 Refatorar função `carregar_regras()`
- [ ] **2.2.1** Modificar para usar as novas classes
- [ ] **2.2.2** Manter compatibilidade com interface existente
- [ ] **2.2.3** Adicionar type hints
- [ ] **2.2.4** Adicionar docstring

### 2.3 Testar sistema de regras
- [ ] **2.3.1** Testar carregamento de regras para cada teatro
- [ ] **2.3.2** Verificar compatibilidade com código existente
- [ ] **2.3.3** Testar conversão para dicionário

---

## 🎯 TAREFA 3: Refatorar Módulo de Utilitários

### 3.1 Simplificar `utils.py`
- [ ] **3.1.1** Remover imports duplicados (datetime)
- [ ] **3.1.2** Importar funções de `common_utils.py`
- [ ] **3.1.3** Refatorar `processar_arquivo()` para usar funções centralizadas
- [ ] **3.1.4** Refatorar `salvar_log()` para usar `formatar_data_timestamp()`
- [ ] **3.1.5** Adicionar parâmetro `regra` opcional em `processar_arquivo()`
- [ ] **3.1.6** Adicionar docstrings e type hints

### 3.2 Testar funcionalidades de processamento
- [ ] **3.2.1** Testar processamento de arquivos individuais
- [ ] **3.2.2** Testar processamento de arquivos ZIP
- [ ] **3.2.3** Testar geração de logs
- [ ] **3.2.4** Testar tratamento de erros

---

## 🎯 TAREFA 4: Refatorar Interface Principal

### 4.1 Criar componentes Streamlit reutilizáveis
- [ ] **4.1.1** Criar arquivo `streamlit_components.py`
- [ ] **4.1.2** Implementar `renderizar_sidebar_estilo()` para CSS da sidebar
- [ ] **4.1.3** Implementar `renderizar_cabecalho()` para cabeçalho principal
- [ ] **4.1.4** Implementar `renderizar_sidebar_painel()` para controles da sidebar
- [ ] **4.1.5** Implementar `renderizar_area_visualizacao()` para área de imagens
- [ ] **4.1.6** Implementar `renderizar_resultados()` para área de resultados

### 4.2 Refatorar `main.py`
- [ ] **4.2.1** Remover imports duplicados (datetime)
- [ ] **4.2.2** Importar funções de `common_utils.py` e `streamlit_components.py`
- [ ] **4.2.3** Substituir formatação de data por `formatar_data_brasileira()`
- [ ] **4.2.4** Substituir lógica de verificação de imagem por `verificar_existencia_imagem()`
- [ ] **4.2.5** Refatorar função `main()` para usar componentes reutilizáveis
- [ ] **4.2.6** Adicionar type hints e docstrings

### 4.3 Testar interface refatorada
- [ ] **4.3.1** Testar carregamento da aplicação
- [ ] **4.3.2** Testar seleção de teatro e gabarito
- [ ] **4.3.3** Testar upload e validação de arquivos
- [ ] **4.3.4** Testar exibição de resultados
- [ ] **4.3.5** Testar responsividade da interface

---

## 🎯 TAREFA 5: Melhorias de Qualidade de Código

### 5.1 Adicionar validações e tratamento de erros
- [ ] **5.1.1** Adicionar validação de entrada em todas as funções
- [ ] **5.1.2** Implementar logging estruturado
- [ ] **5.1.3** Adicionar tratamento de exceções específicas
- [ ] **5.1.4** Implementar fallbacks para casos de erro

### 5.2 Melhorar documentação
- [ ] **5.2.1** Adicionar docstrings completas em todas as funções
- [ ] **5.2.2** Adicionar comentários explicativos em código complexo
- [ ] **5.2.3** Criar README.md com instruções de uso
- [ ] **5.2.4** Documentar estrutura de arquivos e responsabilidades

### 5.3 Otimizações de performance
- [ ] **5.3.1** Otimizar carregamento de imagens
- [ ] **5.3.2** Implementar cache para regras carregadas
- [ ] **5.3.3** Otimizar processamento de arquivos ZIP
- [ ] **5.3.4** Adicionar validação de tamanho de arquivo

---

## 🎯 TAREFA 6: Testes e Validação

### 6.1 Criar testes unitários
- [ ] **6.1.1** Criar arquivo `test_common_utils.py`
- [ ] **6.1.2** Criar arquivo `test_regras.py`
- [ ] **6.1.3** Criar arquivo `test_utils.py`
- [ ] **6.1.4** Implementar testes para todas as funções principais
- [ ] **6.1.5** Adicionar testes de casos extremos

### 6.2 Testes de integração
- [ ] **6.2.1** Testar fluxo completo de validação
- [ ] **6.2.2** Testar com diferentes tipos de arquivo
- [ ] **6.2.3** Testar com arquivos corrompidos ou inválidos
- [ ] **6.2.4** Testar performance com arquivos grandes

### 6.3 Validação final
- [ ] **6.3.1** Executar todos os testes
- [ ] **6.3.2** Verificar se não há regressões
- [ ] **6.3.3** Validar funcionamento em produção
- [ ] **6.3.4** Documentar mudanças e melhorias

---

## 📊 Critérios de Sucesso

### ✅ Funcionalidade
- [ ] Todas as funcionalidades existentes continuam funcionando
- [ ] Nova função `verificar_arte` implementada e funcional
- [ ] Interface responsiva e intuitiva

### ✅ Qualidade de Código
- [ ] Zero duplicação de código (princípio DRY)
- [ ] Type hints em todas as funções
- [ ] Docstrings completas
- [ ] Código modular e reutilizável

### ✅ Manutenibilidade
- [ ] Estrutura clara e organizada
- [ ] Responsabilidades bem definidas
- [ ] Fácil adição de novas regras
- [ ] Código autodocumentado

### ✅ Performance
- [ ] Tempo de carregamento otimizado
- [ ] Processamento eficiente de arquivos
- [ ] Uso adequado de memória

---

## 🚨 Notas Importantes

1. **Backup**: Sempre faça backup do código original antes de iniciar
2. **Testes**: Execute testes após cada tarefa principal
3. **Compatibilidade**: Mantenha compatibilidade com interface existente
4. **Documentação**: Atualize documentação conforme necessário
5. **Versionamento**: Use commits pequenos e descritivos

---

## 📅 Cronograma Sugerido

- **Semana 1**: Tarefas 1 e 2 (Utilitários e Regras)
- **Semana 2**: Tarefas 3 e 4 (Interface e Componentes)
- **Semana 3**: Tarefas 5 e 6 (Qualidade e Testes)

---

*Documento criado em: $(date)*
*Versão: 1.0*
