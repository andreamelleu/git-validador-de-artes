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

def buscar_link_drive_artes(espetaculo: str, teatro: str, processo_id: str = None) -> str:
    """Busca o link do Drive de artes do processo específico
    
    Args:
        espetaculo: Nome do espetáculo (não usado se processo_id for fornecido)
        teatro: Nome do teatro (não usado se processo_id for fornecido)
        processo_id: ID do processo no Supabase (opcional, vem da URL)
    """
    supabase = get_supabase_client()
    if not supabase:
        print("⚠️ Cliente Supabase não configurado")
        return ""
        
    try:
        print(f"🔍 Buscando link do Drive:")
        
        # Se tiver processo_id, busca diretamente
        if processo_id:
            print(f"   Processo ID: {processo_id}")
            try:
                response = supabase.table("processos").select("link_drive").eq("id", processo_id).execute()
                
                if response.data and len(response.data) > 0:
                    link = response.data[0].get("link_drive", "")
                    if link:
                        print(f"   ✅ Link encontrado: {link[:50]}...")
                        return link
                    else:
                        print("   ⚠️ Campo link_drive está vazio")
                        return ""
                else:
                    print(f"   ❌ Processo {processo_id} não encontrado")
                    return ""
            except Exception as e:
                print(f"   ❌ Erro ao buscar por ID: {e}")
                return ""
        
        # Fallback: busca por nome (menos confiável)
        print(f"   Espetáculo: {espetaculo}")
        print(f"   Teatro: {teatro}")
        print("   ⚠️ Buscando sem processo_id - resultado pode ser impreciso")
        
        # Nota: Esta parte pode não funcionar se os nomes das colunas forem diferentes
        # É melhor sempre passar o processo_id via URL
        return ""
            
    except Exception as e:
        print(f"❌ Erro ao buscar link do Drive: {e}")
        import traceback
        traceback.print_exc()
        return ""





