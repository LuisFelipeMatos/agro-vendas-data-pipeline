
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")
    
    # conexão com o banco de dados
    conn_str = f"postgresql://{user}:{password}@{host}:{port}/{db}?client_encoding=utf8"
    
    return create_engine(conn_str,client_encoding='utf8', connect_args={'client_encoding': 'utf8'})