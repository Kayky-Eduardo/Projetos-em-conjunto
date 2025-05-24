from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.button import Button
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
            butao = Button(text='Deletar')
            butao.bind(on_press=lambda instance, id=compra_id: self.remover_compra(id))
            container.add_widget(butao)
    
    def remover_compra(self, id):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM compra WHERE compra_id = ?", (id,))
        conexao.commit()
        conexao.close()
        self.atualizar_dados()