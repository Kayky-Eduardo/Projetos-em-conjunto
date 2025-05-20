import sqlite3
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class Cadastro_Usuario(GridLayout):
    cpf = ObjectProperty(None)
    cargo_id = ObjectProperty(None)
    nome = ObjectProperty(None)
    salario = ObjectProperty(None)
    senha = ObjectProperty(None)
    data_admissao = ObjectProperty(None)
    fim_contrato = ObjectProperty(None)
    confirmar_senha = ObjectProperty(None)
    enviar = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
            
class CadastroApp(App):
    def build(self):
        return Cadastro_Usuario()

if __name__ == '__main__':
    CadastroApp().run()
