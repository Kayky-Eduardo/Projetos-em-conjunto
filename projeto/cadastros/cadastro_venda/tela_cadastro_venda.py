from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import sqlite3
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'tela_cadastro_venda.kv'))

class Tela_Cadastro_Venda(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def buscar_dados(self):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM venda
        """)

        dados = cursor.fetchall()
        conexao.close()
        return dados

    def atualizar_dados(self):
        container = self.ids.container
        container.clear_widgets()
        for venda_id, funcionario_id, cliente_cpf, compra_id in self.buscar_dados():
            texto = f"ID: {venda_id} | ID do funcionário: {funcionario_id} | CPF do cliente: {cliente_cpf} | ID da compra: {compra_id}"
            container.add_widget(Label(text=texto))

# class Gerenciador_Telas(App):
#     def build(self):
#         return Builder.load_file("Tela_Cadastro_Venda.kv")

# if __name__ == '__main__':
#     Gerenciador_Telas().run()
