import sqlite3

conexao = sqlite3.connect("BD/projeto.db")
cursor = conexao.cursor()   
cursor.execute('''
    INSERT INTO funcionario (
        funcionario_cpf, cargo_id, nome_funcionario, salario, data_admissao, fim_contrato, senha
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
''', (
    '2',
    2,              
    'Administrador',
    0,
    '0000-00-00',
    None,
    '1'
))
conexao.commit()
conexao.close()