import json
import os
from datetime import datetime
from typing import Dict, Any, List

HISTORY_FILE = "validation_history.json"

def get_supabase():
    try:
        from supabase_utils import get_supabase_client
        return get_supabase_client()
    except ImportError:
        return None

def load_all_history() -> Dict[str, Any]:
    # 1. Tenta carregar do Supabase (Persistência Real na Nuvem)
    sb = get_supabase()
    if sb:
        try:
            # Busca todos os registros
            response = sb.table("validation_history").select("*").execute()
            history_dict = {}
            for item in response.data:
                # Reconstrói formato de dicionário de manipulação local
                key = f"{item['espetaculo']} | {item['teatro']}"
                # data_json armazena os arrays (approved, rejected, missing)
                details = item.get('data_json', {})
                history_dict[key] = {
                    "espetaculo": item['espetaculo'],
                    "teatro": item['teatro'],
                    "last_update": item.get('updated_at', ''),
                    "approved": details.get('approved', []),
                    "rejected": details.get('rejected', []),
                    "missing": details.get('missing', []),
                    "status": item['status']
                }
            return history_dict
        except Exception as e:
            print(f"Erro Supabase Load (Fallback Local): {e}")

    # 2. Fallback: Arquivo Local JSON
    if not os.path.exists(HISTORY_FILE):
        return {}
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_validation_state(espetaculo: str, teatro: str, arquivos_aprovados: List[str], arquivos_reprovados: List[str], faltantes: List[str]):
    # Prepara dados
    status = "Concluído" if not faltantes and not arquivos_reprovados else "Pendente"
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    data_json = {
        "approved": arquivos_aprovados,
        "rejected": arquivos_reprovados,
        "missing": faltantes
    }

    # 1. Tenta salvar no Supabase
    sb = get_supabase()
    if sb:
        try:
            # Upsert logic based on espetaculo_teatro unique constraint (assumida)
            payload = {
                "espetaculo": espetaculo,
                "teatro": teatro,
                "status": status,
                "data_json": data_json,
                "updated_at": timestamp
            }
            # Tenta insert ou update. No supabase upsert geralmente requer uma constraint unique.
            # Aqui estamos assumindo que existe uma tabela 'validation_history'
            sb.table("validation_history").upsert(payload, on_conflict="espetaculo,teatro").execute()
            return # Sucesso, não precisa salvar local se nuvem funcionou (ou salva ambos por segurança)
        except Exception as e:
             print(f"Erro Supabase Save: {e}")

    # 2. Salva Localmente (Fallback)
    history = load_all_history()
    key = f"{espetaculo.strip()} | {teatro.strip()}"
    
    entry = {
        "espetaculo": espetaculo,
        "teatro": teatro,
        "last_update": timestamp,
        "approved": arquivos_aprovados,
        "rejected": arquivos_reprovados,
        "missing": faltantes,
        "status": status
    }
    
    history[key] = entry
    
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

def get_history_entry(espetaculo: str, teatro: str) -> Dict[str, Any]:
    history = load_all_history()
    key = f"{espetaculo.strip()} | {teatro.strip()}"
    return history.get(key, {})
