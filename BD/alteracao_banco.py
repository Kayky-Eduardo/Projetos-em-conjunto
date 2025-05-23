import sqlite3

conexao = sqlite3.connect("BD/projeto.db")
cursor = conexao.cursor()   
cursor.execute('''
    INSERT INTO funcionario (funcionario_cpf, cargo_id, nome_funcionario, salario, data_admissao, fim_contrato, senha)
    VALUES (1010, 1, 'ADM', 0, '2000-01-01', '9000-01-01', 1)
''',)
conexao.commit()
conexao.close()