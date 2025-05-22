from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder

import sqlite3

Builder.load_file("tela_cadastro_setor.kv")
class Tela_Cadastro_Setor(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def buscar_dados(self):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM setor
        """)

        dados = cursor.fetchall()
        conexao.close()
        return dados

    def atualizar_dados(self):
        container = self.ids.container
        container.clear_widgets()
        for setor_id, nome_setor, responsavel_setor in self.buscar_dados():
            texto = f"ID: {setor_id} | Nome setor: {nome_setor} | Responsável: {responsavel_setor}"
            container.add_widget(Label(text=texto))

class Gerenciador_Telas(App):
    def build(self):
        return Tela_Cadastro_Setor()

if __name__ == '__main__':
    Gerenciador_Telas().run()
