import os
from supabase import create_client, Client
from typing import List, Dict, Any
from dotenv import load_dotenv

# Carrega variáveis locais se existirem
load_dotenv()

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
        # Mapeia o nome do teatro para o ID correto (UUIDs do Supabase)
        teatro_map = {
            "Teatro das Artes": "8b1a5b21-5847-46be-94c2-45fd7c761376",
            "Teatro dos Grandes Atores": "b11871eb-7621-4fdc-99ca-77177920f465",
            # Aliases e compatibilidade
            "DAS_ARTES": "8b1a5b21-5847-46be-94c2-45fd7c761376",
            "ARTES": "8b1a5b21-5847-46be-94c2-45fd7c761376",
            "GRANDES_ATORES": "b11871eb-7621-4fdc-99ca-77177920f465",
        }
        
        # Tenta pegar pelo nome exato, ou normaliza se precisar
        teatro_id = teatro_map.get(teatro)
        if not teatro_id:
             # Tenta algumas variações se não achou direto
             if "Artes" in teatro:
                 teatro_id = teatro_map["Teatro das Artes"]
             elif "Grandes Atores" in teatro:
                 teatro_id = teatro_map["Teatro dos Grandes Atores"]
             else:
                 teatro_id = teatro.lower() # Fallback arriscado
        
        print(f"🔍 Buscando link do Drive:")
        
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
        
        # Fallback: busca por nome da atração (menos confiável)
        print(f"   Atração: {espetaculo}")
        print(f"   Teatro: {teatro}")
        print("   ⚠️ Buscando sem processo_id - tentando encontrar por nome da atração")
        
        try:
            # Tenta buscar usando 'atracao' e 'teatro_id'
            # Usando ilike para ignorar maiúsculas/minúsculas
            response = supabase.table("processos").select("link_drive").ilike("atracao", f"%{espetaculo}%").eq("teatro_id", teatro_id).execute()
            
            if response.data and len(response.data) > 0:
                link = response.data[0].get("link_drive", "")
                if link:
                    print(f"   ✅ Link encontrado via busca por nome: {link[:50]}...")
                    return link
            
            print("   ❌ Nenhuma atração encontrada com esses critérios")
            return ""
            
        except Exception as search_err:
             print(f"   ❌ Erro na busca por nome: {search_err}")
             return ""

    except Exception as e:
        print(f"❌ Erro ao buscar link do Drive: {e}")
        import traceback
        traceback.print_exc()
        return ""





