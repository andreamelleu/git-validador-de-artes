# 🚀 Como colocar o Validador no Ar (Deploy)

Para que o sistema Teatrali consiga acessar o Validador, ele precisa estar hospedado na internet. A melhor opção para aplicativos Streamlit é o **Streamlit Community Cloud**.

## Passo a Passo no Streamlit Cloud

1. **Acesse o Site:**
   - Entre em [https://share.streamlit.io/](https://share.streamlit.io/)
   - Clique em "Sign up" ou "Log in" e entre com sua conta do **GitHub**.

2. **Crie o Aplicativo:**
   - Clique no botão azul **"New app"** (canto superior direito).
   - Selecione a opção **"Use existing repo"**.

3. **Configure os Campos:**
   - **Repository:** Selecione o seu repositório: `andreamelleu/git-validador-de-artes`
   - **Branch:** Deixe como `main`
   - **Main file path:** Escreva `main.py`
   - **App URL:** Você pode escolher um nome personalizado, por exemplo: `validador-teatrali`

4. **Configurar Banco de Dados (Supabase):**
   - Antes de clicar em Deploy, clique em **"Advanced settings"**.
   - Procure a caixa de texto **"Secrets"**.
   - Cole as chaves do seu Supabase neste formato:
     ```toml
     SUPABASE_URL = "sua_url_do_supabase_aqui"
     SUPABASE_KEY = "sua_chave_anon_key_aqui"
     ```
   - *Se você não tiver as chaves agora, pode pular essa etapa, mas o histórico na nuvem e a lista automática de espetáculos não funcionarão (funcionarão apenas com input manual).*

5. **Finalizar:**
   - Clique no botão **"Deploy!"**.
   - Aguarde alguns minutos enquanto o sistema instala tudo.
   - Quando terminar, você receberá o link final (ex: `https://validador-teatrali.streamlit.app`).

## Atualizando o Teatrali

Copie o link gerado acima e atualize o código ou configuração do seu site Teatrali (no arquivo `ProcessForm.tsx` ou onde fica o botão), garantindo que os parâmetros de URL estejam corretos.

Exemplo de Link Final para o botão:
`https://validador-teatrali.streamlit.app/?user=producao&espetaculo=MAMMA+MIA&teatro=GRANDES_ATORES`
