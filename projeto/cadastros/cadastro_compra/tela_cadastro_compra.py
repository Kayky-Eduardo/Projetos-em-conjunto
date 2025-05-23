from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder
import sqlite3
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'tela_cadastro_compra.kv'))

class Tela_Cadastro_Compra(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def buscar_dados(self):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM compra
        """)
        dados = cursor.fetchall()
        conexao.close()
        return dados

    def atualizar_dados(self):
        container = self.ids.container
        container.clear_widgets()
        for compra_id, produto_id, qntd_produto in self.buscar_dados():
            texto = f"ID: {compra_id} | ID do Produto: {produto_id} | Quantidade: {qntd_produto}"
            container.add_widget(Label(text=texto))