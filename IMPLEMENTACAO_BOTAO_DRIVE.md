# Implementação do Botão "Acessar Drive de Artes"

## ✅ O que foi implementado

### 1. **Botão de Acesso ao Drive** (`streamlit_components.py` linhas 173-206)
- Botão "📁 Acessar Drive de Artes" que aparece na sidebar
- Funciona de **duas formas**:
  - **Via URL**: Recebe `link_drive` como parâmetro na URL (prioritário)
  - **Via Supabase**: Busca automaticamente do banco de dados usando `processo_id`

### 2. **Função de Busca no Supabase** (`supabase_utils.py` linhas 45-108)
- Função `buscar_link_drive_artes(espetaculo, teatro, processo_id=None)`
- Busca o campo `link_drive` na tabela `processos`
- Suporta busca por ID do processo (mais precisa e confiável)
- Logs detalhados para debug

### 3. **Mensagens de Debug**
- Expander "ℹ️ Debug - Link do Drive" quando o link não é encontrado
- Expander "⚠️ Erro ao buscar Drive" quando há erro de conexão
- Dicas para o usuário sobre como melhorar a precisão

## 🎯 Como funciona

### Cenário 1: Acesso via Sistema Teatrali (RECOMENDADO)
O usuário clica no botão "Acessar Git Validador de Formatos" no sistema Teatrali, que monta a URL:

```
https://git-validador-de-artes.streamlit.app/?teatro=DAS_ARTES&espetaculo=A+Arca+dos+Bichos&processo_id=abc123&link_drive=https://drive.google.com/...
```

**Parâmetros da URL:**
- `teatro`: Nome do teatro (ex: `DAS_ARTES`, `GRANDES_ATORES`)
- `espetaculo`: Nome do espetáculo (ex: `A Arca dos Bichos`)
- `processo_id`: **ID do processo no Supabase** (NOVO - recomendado)
- `link_drive`: Link direto do Drive (opcional, tem prioridade se fornecido)

### Cenário 2: Acesso Direto (sem link_drive na URL)
Se o usuário acessar sem o parâmetro `link_drive`, o sistema:
1. Tenta buscar no Supabase usando o `processo_id` (se fornecido)
2. Busca o campo `link_drive` na tabela `processos`
3. Se encontrar, mostra o botão
4. Se não encontrar, mostra mensagem de debug

## 📋 Estrutura do Banco de Dados Supabase

### Tabela: `processos`
- **Campo do link**: `link_drive` (tipo: text)
- **Chave primária**: `id` (UUID)

**Exemplo de registro:**
```json
{
  "id": "abc123-def456-...",
  "link_drive": "https://drive.google.com/drive/folders/1e7dNbdMUKuOU1GDYcJgZW7Lvs3ViXgk3",
  ...
}
```

## 🔧 Próximos Passos - O QUE VOCÊ PRECISA FAZER

### 1. **Atualizar o Sistema Teatrali** ⚠️ IMPORTANTE
No arquivo onde você monta o botão "Acessar Git Validador de Formatos", você precisa:

**OPÇÃO A (Recomendada): Passar o processo_id**
```javascript
const url = `https://git-validador-de-artes.streamlit.app/?teatro=${teatro}&espetaculo=${encodeURIComponent(espetaculo)}&processo_id=${processoId}`;
```

**OPÇÃO B (Alternativa): Passar o link_drive diretamente**
```javascript
const linkDrive = processo.link_drive; // Busca do banco
const url = `https://git-validador-de-artes.streamlit.app/?teatro=${teatro}&espetaculo=${encodeURIComponent(espetaculo)}&link_drive=${encodeURIComponent(linkDrive)}`;
```

### 2. **Verificar o Campo no Supabase**
- Confirme que a coluna se chama exatamente `link_drive` (sem espaços)
- Verifique se os processos têm esse campo preenchido
- Exemplo de query SQL para verificar:
```sql
SELECT id, link_drive FROM processos WHERE link_drive IS NOT NULL LIMIT 10;
```

### 3. **Configurar Credenciais no Streamlit Cloud**
No painel do Streamlit Cloud, adicione as variáveis de ambiente:
- `SUPABASE_URL`: URL do seu projeto Supabase
- `SUPABASE_KEY`: Chave anon/public do Supabase

### 4. **Testar o Fluxo Completo**
1. Acesse um processo no sistema Teatrali
2. Clique no botão "Acessar Git Validador de Formatos"
3. Verifique se o botão "📁 Acessar Drive de Artes" aparece
4. Clique no botão e confirme que abre a pasta correta do Drive

## 🐛 Troubleshooting

### Botão não aparece
1. **Verifique os logs do terminal** - procure por mensagens começando com "🔍 Buscando link do Drive"
2. **Verifique se o processo_id está sendo passado** - olhe a URL no navegador
3. **Verifique se o campo link_drive está preenchido** no Supabase

### Erro "Cliente Supabase não configurado"
- As credenciais `SUPABASE_URL` e `SUPABASE_KEY` não estão configuradas no Streamlit Cloud

### Erro "Processo não encontrado"
- O `processo_id` passado na URL não existe na tabela `processos`
- Verifique se o ID está correto

### Campo link_drive vazio
- O processo existe mas o campo `link_drive` está NULL ou vazio
- Preencha o campo no Supabase

## 📝 Arquivos Modificados

1. `streamlit_components.py` - Linhas 173-206
2. `supabase_utils.py` - Linhas 45-108
3. `pyiceberg/` - Mocks criados para evitar conflitos de import

## 🚀 Deploy

O código está pronto para deploy. Quando fizer push para o GitHub, o Streamlit Cloud vai atualizar automaticamente.

**Comando para commit:**
```bash
git add .
git commit -m "feat: Implementado botão de acesso direto ao Drive com suporte a processo_id"
git push origin main
```
