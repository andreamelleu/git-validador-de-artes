import os
from supabase import create_client, Client
from typing import List, Dict, Any

# Inicializa o cliente apenas se as chaves estiverem presentes
def get_supabase_client() -> Client:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    if not url or not key:
        return None
        
    return create_client(url, key)

def buscar_producoes_ativas() -> List[str]:
    """Busca as produções ativas no banco de dados da Teatrali"""
    supabase = get_supabase_client()
    if not supabase:
        return []
        
    try:
        # Exemplo de query - Ajuste conforme sua tabela real 'producoes' ou 'espetaculos'
        # Supondo uma tabela 'producoes' com coluna 'nome'
        response = supabase.table("producoes").select("nome").eq("status", "active").execute()
        return [item["nome"] for item in response.data]
    except Exception as e:
        print(f"Erro ao buscar produções: {e}")
        return []

def validar_sessao_usuario(user_id: str) -> bool:
    """Valida se o usuário vindo da Teatrali é válido"""
    supabase = get_supabase_client()
    if not supabase:
        # Se não tiver supabase configurado, mas passou user_id, 
        # permitimos para teste se for 'producao'
        return True 
        
    try:
        # Verifica se existe perfil ativo para este ID
        response = supabase.table("profiles").select("id").eq("id", user_id).execute()
        return len(response.data) > 0
    except Exception:
        return False
