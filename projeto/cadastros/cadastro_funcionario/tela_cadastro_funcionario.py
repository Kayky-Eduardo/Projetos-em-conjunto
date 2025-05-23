from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.lang import Builder
import sqlite3
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'tela_cadastro_funcionario.kv'))

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
            butao = Button(text='Deletar')
            butao.bind(on_press=lambda instance, cpf=funcionario_cpf: self.remover_funcionario(cpf))
            container.add_widget(butao)
    
    def remover_funcionario(self, cpf):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM funcionario WHERE funcionario_cpf = ?", (cpf,))
        conexao.commit()
        conexao.close()
        self.atualizar_dados()