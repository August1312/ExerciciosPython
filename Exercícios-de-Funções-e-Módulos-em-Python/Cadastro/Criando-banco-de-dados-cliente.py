#criando o banco de dados:
import sqlite3
conexao = sqlite3.connect('clientes.db')

#criando o cursor:

c = conexao.cursor()

#criando a tabela:

c.execute("""create table clientes (
          nome text,
          sobrenome text,
          email tex,
          telefone text
)""")

#commit as mudancas:

conexao.commit()

#fecha o banco de dados:

conexao.close
