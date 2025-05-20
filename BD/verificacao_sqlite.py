import sqlite3

conexao = sqlite3.connect("BD/projeto.db")
cursor = conexao.cursor()   

cursor.execute('''SELECT produto.nome_produto, estoque.qntd_produto FROM produto JOIN estoque ON produto  produto.produto_id = estoque.produto_id;''')
produto = cursor.fetchall()
print(produto)