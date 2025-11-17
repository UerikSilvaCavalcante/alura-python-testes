# Conecta ao banco de dados MongoDB utilizando as variáveis de ambiente

from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env

load_dotenv()

# Cria a conexão com o banco de dados MongoDB
mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    raise ValueError("MONGO_URI não configurado no arquivo .env")

try:
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    # Testa a conexão
    client.admin.command("ping")
    print("✓ Conectado ao MongoDB com sucesso!")
except Exception as e:
    print(f"✗ Erro na conexão com MongoDB: {e}")
    raise

# Seleciona o banco de dados
db = client["burguer_app_db"]


# função para retornar a instância do banco de dados
def get_db():
    return db
