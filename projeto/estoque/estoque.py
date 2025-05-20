import sqlite3
import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

# Carrega o arquivo KV
Builder.load_file(os.path.join(os.path.dirname(__file__), 'estoque.kv'))

class Estoque(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def exibir(self):
        # Buscanome_produto do banco
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute('''SELECT produto.nome_produto, estoque.qntd_estoque
                        FROM produto
                        JOIN estoque ON produto.id_produto = estoque.id_produto;''')
        produto = cursor.fetchall()
        print(produto)
        conexao.close()


# para rodar o código como se fosse o principal
class EstoqueApp(App):
    def build(self):
        return Estoque()

if __name__ == '__main__':
    EstoqueApp().run()