import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

print("Pasta atual:", Path.cwd())
print(".env encontrado em:", find_dotenv())

load_dotenv()
valor = os.getenv("MONGO_URI")
print("Variável lida:", "SIM" if valor else "NÃO (None)")
if valor:
    print("Começa com:", valor[:20])