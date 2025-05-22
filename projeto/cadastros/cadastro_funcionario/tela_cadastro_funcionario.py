from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder

import sqlite3

Builder.load_file("tela_cadastro_funcionario.kv")
class Tela_Cadastro_Funcionario(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def buscar_dados(self):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM funcionario
        """)
        dados = cursor.fetchall()
        conexao.close()
        return dados

    def atualizar_dados(self):
        container = self.ids.container
        container.clear_widgets()
        for funcionario_cpf, cargo_id, nome_funcionario, salario, data_admissao, fim_contrato, senha in self.buscar_dados():
            texto = f"Funcionario CPF: {funcionario_cpf} | Cargo: {cargo_id} | Nome: {nome_funcionario} | Salário: {salario}\nData Admissão: {data_admissao} | Fim do Contrato {fim_contrato}"
            container.add_widget(Label(text=texto))

class Gerenciador_Telas(App):
    def build(self):
        return Tela_Cadastro_Funcionario()

if __name__ == '__main__':
    Gerenciador_Telas().run()
