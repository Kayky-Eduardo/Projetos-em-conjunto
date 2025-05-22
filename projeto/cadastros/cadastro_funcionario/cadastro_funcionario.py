import sqlite3
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'cadastro_funcionario.kv'))

class Cadastro_Funcionario(Screen):
    cpf = ObjectProperty(None)
    cargo_id = ObjectProperty(None)
    nome = ObjectProperty(None)
    salario = ObjectProperty(None)
    senha = ObjectProperty(None)
    data_admissao = ObjectProperty(None)
    fim_contrato = ObjectProperty(None)
    confirmar_senha = ObjectProperty(None)
    enviar = ObjectProperty(None)

    def adicionar_banco(self):
        nome_validacao = self.nome.text
        cpf_validacao = self.cpf.text
        senha_validacao = self.senha.text
        confirmar_senha_validacao = self.confirmar_senha.text
        salario_validacao = self.salario.text
        cargo_id_validacao = self.cargo_id.text
        data_admissao_validacao = self.data_admissao.text
        fim_contrato_validacao = self.fim_contrato.text
        
        try:
            if senha_validacao == confirmar_senha_validacao:
                conexao = sqlite3.connect("BD/projeto.db")
                cursor = conexao.cursor()
                cursor.execute('''
                    INSERT INTO funcionario (funcionario_cpf, cargo_id, nome_funcionario, salario, data_admissao, fim_contrato, senha)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (cpf_validacao, cargo_id_validacao, nome_validacao, salario_validacao, data_admissao_validacao, fim_contrato_validacao, senha_validacao))
                conexao.commit()
                conexao.close()
                self.enviar.text = "Cadastro realizado com sucesso!"

            else:
                self.enviar.text = "A senha não é a mesma"
        except sqlite3.Error as e:
            self.enviar.text = f'Erro: {e}'
