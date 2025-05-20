import sqlite3

conexao = sqlite3.connect("BD/projeto.db")
cursor = conexao.cursor()   
<<<<<<< HEAD
cursor.execute("SELECT * FROM estoque")
=======
cursor.execute("SELECT * FROM funcionario")
>>>>>>> 833cb99344d2458a2d1d56308c51879810a3fcbe
todos = cursor.fetchall()
print(todos)
