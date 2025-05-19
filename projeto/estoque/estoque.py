import sqlite3
import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Estoque(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Carrega o arquivo KV
        Builder.load_file(os.path.join(os.path.dirname(__file__), 'estoque.kv'))

        # Busca produtos do banco
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT produto.produto_id, produto.nome_produto, estoque.qntd_produto FROM produto JOIN estoque ON produto.produto_id = estoque.produto_id')
        cursor.row_factory = sqlite3.Row # para acessar colunas pelo nome (ex: produto['nome_produto'])
        produtos = cursor.fetchall()
        conexao.close()

        for produto in produtos:
            linha = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
            nome_label = Label(text=produto['nome_produto'])
            quantidade_label = Label(text=str(produto['qntd_produto']))
            linha.add_widget(nome_label)
            linha.add_widget(quantidade_label)

# para rodar o código como se fosse o principal
class EstoqueApp(App):
    def build(self):
        return Estoque()

if __name__ == '__main__':
    EstoqueApp().run()