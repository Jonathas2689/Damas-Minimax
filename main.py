from datetime import datetime
from src.db.conexao import obter_colecao

colecao = obter_colecao()

log = {
    "data_hora": datetime.now(),
    "nivel": "ERROR",
    "servico": "pagamentos",
    "mensagem": "Falha ao conectar no banco",
    "ip": "192.168.0.10",
}

colecao.insert_one(log)

for documento in colecao.find():
    print(documento)
    