# Repositório de Banco de Dados de Vendas

Este repositório contém exemplos e atividades práticas desenvolvidas durante as aulas. O foco principal é o gerenciamento de um banco de dados de vendas utilizando um script em Python e SQLAlchemy.

## Conteúdo:

- **Script de Criação de Tabelas (`vendas.py`):** Um script em Python utilizando SQLAlchemy para definir e criar tabelas no banco de dados `vendas.db`.
- **Banco de Dados Relacional (`vendas.db`):** Um banco de dados SQLite que armazena informações sobre vendas, incluindo detalhes de produtos, clientes e transações.

## Estrutura do Banco de Dados:

- **Cliente:** Tabela `tbCliente` com informações detalhadas dos clientes.
- **Fornecedor:** Tabela `tbFornecedor` com dados dos fornecedores.
- **Produto:** Tabela `tbProduto` com detalhes dos produtos, incluindo uma chave estrangeira para fornecedores.
- **Vendedor:** Tabela `tbVendedor` com informações dos vendedores.
- **Vendas:** Tabela `tbVendas` para registrar transações de vendas, com chaves estrangeiras para clientes, produtos e vendedores.