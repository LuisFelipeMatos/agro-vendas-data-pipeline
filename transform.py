import pandas as pd

def transform(df):
    print(f"--- 2. TRANSFORMAÇÃO ---")
    # Converte data
    df['data'] = pd.to_datetime(df['data'])
    
    # O CSV tem preço unitário, a Fato pede Valor Total
    df['valor_total'] = df['quantidade'] * df['preco_unitario']
    
    return df

def dim_cliente(df):
    # Colunas exatas do CSV
    cols = ['id_cliente', 'nome_cliente', 'cidade', 'estado']
    return df[cols].drop_duplicates().reset_index(drop=True)

def dim_produto(df):
    # Colunas exatas do CSV
    cols = ['id_produto', 'produto', 'categoria', 'preco_unitario']
    return df[cols].drop_duplicates().reset_index(drop=True)

def dim_data(df):
    df_data = pd.DataFrame({'data': df['data'].unique()})
    df_data['ano'] = df_data['data'].dt.year
    df_data['mes'] = df_data['data'].dt.month
    df_data['dia'] = df_data['data'].dt.day
    return df_data