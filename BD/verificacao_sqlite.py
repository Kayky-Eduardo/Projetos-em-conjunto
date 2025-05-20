import sqlite3

conexao = sqlite3.connect("BD/projeto.db")
cursor = conexao.cursor()   
cursor.execute("SELECT * FROM produto")
todos = cursor.fetchall()
print(todos)
