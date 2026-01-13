import sys
import os

# Garante que o Python encontre a pasta config
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extract import extract
from transform import transform, dim_cliente, dim_produto, dim_data
from load import load_dim, load_fato
from config.db_config import get_engine

def main():
    try:
        engine = get_engine()
        
        # Execução do ETL
        df_raw = extract()
        df_clean = transform(df_raw)
        
        print(f"--- 3. CARGA ---")
        load_dim(dim_cliente(df_clean), "dim_cliente", engine)
        load_dim(dim_produto(df_clean), "dim_produto", engine)
        load_dim(dim_data(df_clean), "dim_data", engine)
        
        load_fato(df_clean, engine)
        
        print("\n🚀 PROCESSO FINALIZADO COM SUCESSO!")
        
    except Exception as e:
        print(f"\n❌ FALHA NO PIPELINE: {e}")

if __name__ == "__main__":
    main()