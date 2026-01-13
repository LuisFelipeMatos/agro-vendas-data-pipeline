Pipeline ETL de Vendas Agrícolas - Python para PostgreSQL
Este projeto demonstra um pipeline de dados completo (ETL) que extrai dados de vendas brutos de um CSV, aplica transformações de negócio e carrega-os num Data Warehouse utilizando a arquitetura Star Schema no PostgreSQL.

Tecnologias Utilizadas
Linguagem: Python 3.x

Bibliotecas: Pandas, SQLAlchemy, Psycopg2, Dotenv

Base de Dados: PostgreSQL 18

Arquitetura: Star Schema (Tabela Fato e Dimensões)

Estrutura do Data Warehouse (Star Schema)
O projeto transforma dados planos num modelo relacional otimizado para BI:

dim_cliente: Cadastro único de clientes, cidades e estados.

dim_produto: Catálogo de produtos com categorias e preços unitários.

dim_data: Dimensão de tempo com ano, mês e dia para análise temporal.

fato_vendas: Tabela central com métricas de quantidade, valor total e chaves estrangeiras (Surrogate Keys).

Como Executar o Projeto
Clonar o Repositório:

Bash

git clone https://github.com/LuisFelipeMatos/agro-vendas-data-pipeline.git
cd teu-repositorio
Configurar o Ambiente: Crie um arquivo .env na raiz do projeto com as suas credenciais:

Plaintext

DB_USER=teu_usuario
DB_PASSWORD=tua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=dw_vendas
Instalar Dependências:

Bash

pip install -r requirements.txt
Criar a Base de Dados: Execute o script SQL contido na pasta /sql (ou no ficheiro de criação) no seu PostgreSQL para gerar o schema dw.

Rodar o ETL:
Bash
python main.py

Principais Diferenciais Implementados

Surrogate Keys: Uso de chaves artificiais (SK) para garantir integridade e performance no DW.

Segurança: Uso de variáveis de ambiente (.env) para proteção de credenciais.

Cálculo de Métricas: Geração automática do valor_total durante o processo de transformação.