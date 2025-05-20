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

        # Busca produtos do banco
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT nome_produto FROM produto')
        produtos = cursor.fetchall()
        print(produtos[0])
        conexao.close()
        container = self.ids.lista_produtos

        for produto in produtos:
            nome = produto[0]
            linha = BoxLayout(size_hint_y=None, height=40)
            label = Label(text=nome)
            btn_remover = Button(text="Remover", size_hint_x=None, width=100)

            linha.add_widget(label)
            linha.add_widget(btn_remover)
            container.add_widget(linha)


# para rodar o código como se fosse o principal
class EstoqueApp(App):
    def build(self):
        return Estoque()

if __name__ == '__main__':
    EstoqueApp().run()