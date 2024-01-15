import sqlite3 as lite

con = lite.connect('dados.db')

lista = [('Tenis','Nike', "12/19/2010", 20, 39,'veio em bom estado')]

# Inserir Informações

def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO controle (nome, fornecedor, dia_em, estoque, preco, descricao) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query,i)



def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM controle"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista


def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE controle SET nome=?, fornecedor=?, dia_em=?, estoque=?, preco=?, descricao=? WHERE id=?"     
        cur.execute(query, i)


def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM controle WHERE id=?"
        cur.execute(query,i)
