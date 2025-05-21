import sqlite3

conexao = sqlite3.connect("BD/projeto.db")
cursor = conexao.cursor()   
cursor.execute("SELECT * FROM cliente")
todos = cursor.fetchall()
print(todos)
