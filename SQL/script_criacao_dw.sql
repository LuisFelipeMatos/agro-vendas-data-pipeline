-- ============================================
-- CRIAÇÃO DO DATA WAREHOUSE - DW_VENDAS
-- ============================================

-- 1. Criação do Schema (Organização)
CREATE SCHEMA IF NOT EXISTS dw;

-- 2. Limpeza para Testes (Opcional - CUIDADO: apaga os dados atuais)
DROP TABLE IF EXISTS dw.fato_vendas;
DROP TABLE IF EXISTS dw.dim_cliente;
DROP TABLE IF EXISTS dw.dim_produto;
DROP TABLE IF EXISTS dw.dim_data;

-- 3. Dimensão Cliente
CREATE TABLE dw.dim_cliente (
    sk_cliente SERIAL PRIMARY KEY,    -- Surrogate Key (Interna do DW)
    id_cliente INT NOT NULL,          -- ID de Negócio (Vem do CSV)
    nome_cliente VARCHAR(150),
    cidade VARCHAR(100),
    estado VARCHAR(2)
);

-- 4. Dimensão Produto
CREATE TABLE dw.dim_produto (
    sk_produto SERIAL PRIMARY KEY,    -- Surrogate Key
    id_produto INT NOT NULL,          -- ID de Negócio
    produto VARCHAR(150),
    categoria VARCHAR(100),
    preco_unitario NUMERIC(10,2)
);

-- 5. Dimensão Data
CREATE TABLE dw.dim_data (
    sk_data SERIAL PRIMARY KEY,       -- Surrogate Key
    data DATE UNIQUE NOT NULL,        -- A data em si (link com o merge do Python)
    ano INT,
    mes INT,
    dia INT
);

-- 6. Tabela Fato Vendas
CREATE TABLE dw.fato_vendas (
    sk_venda SERIAL PRIMARY KEY,
    sk_cliente INT NOT NULL,
    sk_produto INT NOT NULL,
    sk_data INT NOT NULL,
    quantidade INT,
    valor_total NUMERIC(12,2),

    -- Relacionamentos (Integridade Referencial)
    CONSTRAINT fk_cliente FOREIGN KEY (sk_cliente) REFERENCES dw.dim_cliente (sk_cliente),
    CONSTRAINT fk_produto FOREIGN KEY (sk_produto) REFERENCES dw.dim_produto (sk_produto),
    CONSTRAINT fk_data FOREIGN KEY (sk_data) REFERENCES dw.dim_data (sk_data)
);

-- 7. Índices para Performance em Ferramentas de BI (Power BI/Tableau)
CREATE INDEX idx_fato_cliente ON dw.fato_vendas (sk_cliente);
CREATE INDEX idx_fato_produto ON dw.fato_vendas (sk_produto);
CREATE INDEX idx_fato_data ON dw.fato_vendas (sk_data);