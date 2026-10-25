import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient

RAIZ = Path(__file__).resolve().parents[2]
load_dotenv(RAIZ / ".env", encoding="utf-8-sig")


def obter_colecao():
    uri = os.getenv("MONGO_URI")
    if not uri:
        raise RuntimeError("MONGO_URI não foi encontrada. Verifique o arquivo .env")
    cliente = MongoClient(uri)
    banco = cliente["analisador_logs"]
    return banco["logs"]