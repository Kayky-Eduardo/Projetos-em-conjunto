import sqlite3

conexao = sqlite3.connect("BD/projeto.db")
cursor = conexao.cursor()   
cursor.execute("SELECT * FROM venda")
todos = cursor.fetchall()
print(todos)
