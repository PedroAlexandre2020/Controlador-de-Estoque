import sqlite3 as lite

con = lite.connect('dados.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE controle(nome TEXT, fornecedor TEXT, dia_em DATE, estoque INT, preco FLOAT, descricao TEXT)")

