import sqlalchemy as sa 

engine = sa.create_engine("sqlite:///BD//Vendas.db")

import sqlalchemy.orm as orm
base = orm.declarative_base()

#Tabela cliente
class cliente(base):
    __tablename__ = 'tbCliente'

    cpf = sa.Column(sa.CHAR(14), primary_key = True,index=True)
    nmCliente = sa.Column(sa.VARCHAR(100), nullable = False)
    email = sa.Column(sa.VARCHAR(50), nullable = False)
    faixa_salarial = sa.Column(sa.DECIMAL(10,2))
    dia_mes_aniversario = sa.Column(sa.CHAR(5))
    genero = sa.Column(sa.CHAR(1))
    bairro = sa.Column(sa.VARCHAR(50))
    cidade = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))

#Tabela fornecedor
class fornecedor(base):
    __tablename__ = 'tbFornecedor'

    registro = sa.Column(sa.INTEGER, primary_key = True, index=True)
    nome_fantasia = sa.Column(sa.VARCHAR(100), nullable = False)
    razao_social = sa.Column(sa.VARCHAR(100), nullable = False)
    cidade = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))

#Tabela produto
class produto(base):
    __tablename__ = 'tbProduto'

    codBarras = sa.Column(sa.INTEGER, primary_key = True, index=True)
    registro = sa.Column(sa.INTEGER, sa.ForeignKey('tbFornecedor.registro', ondelete='NO ACTION', onupdate='CASCADE'))
    dscProduto = sa.Column(sa.VARCHAR(100), nullable = False)
    genero = sa.Column(sa.CHAR(1))  

#Tabela Vendedor
class vendedor(base):
    __tablename__ = 'tbVendedor'

    registro_vendedor = sa.Column(sa.INTEGER, primary_key = True, index=True)
    cpf = sa.Column(sa.CHAR(14), nullable = False)
    nome = sa.Column(sa.VARCHAR(100), nullable = False)
    genero = sa.Column(sa.CHAR(1))  
    email = sa.Column(sa.VARCHAR(50))

#Tabela Vendas
class vendas(base):
    __tablename__ = 'tbVendas'

    idTransacao = sa.Column(sa.INTEGER, primary_key=True, index=True)
    cpf = sa.Column(sa.CHAR(14), sa.ForeignKey('tbCliente.cpf', ondelete='NO ACTION', onupdate='CASCADE'), index=True)
    codBarras = sa.Column(sa.INTEGER, sa.ForeignKey('tbProduto.codBarras', ondelete='NO ACTION', onupdate='CASCADE'), index=True)
    registro_vendedor = sa.Column(sa.INTEGER, sa.ForeignKey('tbVendedor.registro_vendedor', ondelete='NO ACTION', onupdate='CASCADE'), index=True)
    dia_hora_venda = sa.Column(sa.DATETIME, nullable = False)
    vlrVenda = sa.Column(sa.DECIMAL(10,2), nullable = False)


#Criar a tabelas
try:
    base.metadata.create_all(engine) #Criar a tabela
    print("Tabelas criadas!")
except ValueError:
    print("Tabelas não foram criadas")