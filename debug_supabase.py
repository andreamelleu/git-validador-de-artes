from supabase_utils import get_supabase_client
import json

def debug_db():
    supabase = get_supabase_client()
    if not supabase:
        print("Erro de conexão")
        return

    print("--- Buscando Processos (Estrutura) ---")
    try:
        # Busca 1 processo com TODAS as colunas
        res = supabase.table("processos").select("*").limit(1).execute()
        
        if res.data and len(res.data) > 0:
            print("✅ Colunas encontradas:")
            for key in res.data[0].keys():
                print(f"   - {key}")
        else:
            print("❌ Tabela 'processos' parece vazia ou inacessível")
            
    except Exception as e:
        print(f"Erro ao buscar estrutura: {e}")

    # Não tenta buscar específico ainda até sabermos as colunas


if __name__ == "__main__":
    debug_db()
