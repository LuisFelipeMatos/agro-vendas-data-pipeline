import pandas as pd

def load_dim(df, tabela, engine):

    # if_exists='append' para não apagar a estrutura, apenas adicionar os dados
    df.to_sql(tabela, engine, schema='dw', if_exists='append', index=False)
    print(f"✅ Dimensão {tabela} carregada.")

def load_fato(df_vendas, engine):

    # 1. Recupera os SKs (Surrogate Keys) do banco
    with engine.connect() as conn:
        d_cliente = pd.read_sql("SELECT sk_cliente, id_cliente FROM dw.dim_cliente", conn)
        d_produto = pd.read_sql("SELECT sk_produto, id_produto FROM dw.dim_produto", conn)
        d_data    = pd.read_sql("SELECT sk_data, data FROM dw.dim_data", conn)

    # Garantir que a coluna de data está no formato correto para o merge
    d_data['data'] = pd.to_datetime(d_data['data'])
    df_vendas['data'] = pd.to_datetime(df_vendas['data'])
    
    # 2. Fazendo os Merges (Lookup) apenas pelos IDs numéricos
    # Isso evita o erro de 'coluna não encontrada' caso o nome varie
    df_fato = df_vendas.merge(d_cliente, on='id_cliente', how='left')
    df_fato = df_fato.merge(d_produto, on='id_produto', how='left')
    df_fato = df_fato.merge(d_data, on='data', how='left')

    # 3. Selecionar apenas as colunas que o banco espera
    colunas_finais = ['sk_cliente', 'sk_produto', 'sk_data', 'quantidade', 'valor_total']
    
    # Verifica se houve algum erro no merge (se algum SK ficou nulo)
    if df_fato[colunas_finais].isnull().values.any():
        print("⚠️ Aviso: Alguns registros não encontraram correspondência nas dimensões.")
        df_fato = df_fato.dropna(subset=colunas_finais)

    df_final = df_fato[colunas_finais]

    # 4. Enviar para o banco
    df_final.to_sql('fato_vendas', engine, schema='dw', if_exists='append', index=False)
    print("✅ Tabela Fato carregada com sucesso.")