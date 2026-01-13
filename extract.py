import pandas as pd
import os

def extract():
    # caminho do arquico csv
    file_path = os.path.join("data", "raw", "vendas.csv")
    print(f"\n--- 1. EXTRAÇÃO ---")
    
    try:
        
        df = pd.read_csv(file_path, sep=',', encoding='utf8', engine='python')
        print(f"✅ Sucesso: {len(df)} linhas extraídas.")

        # remove espaços em branco que podem vir nas pontas das palavras
        df['nome_cliente'] = df['nome_cliente'].str.strip()
        df['cidade'] = df['cidade'].str.strip()
        df['produto'] = df['produto'].str.strip()
     
        
        return df
    except Exception as e:
        print(f"❌ Erro na extração: {e}")
        raise