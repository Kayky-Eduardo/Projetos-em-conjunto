from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
import sqlite3
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'tela_cadastro_cargo.kv'))



class Tela_Cadastro_Cargo(Screen):  
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def buscar_dados(self):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM cargo
        """)

        dados = cursor.fetchall()
        conexao.close()
        return dados

    def atualizar_dados(self):
        container = self.ids.container
        container.clear_widgets()
        for cargo_id, nome_cargo, tipo_contrato, setor_id in self.buscar_dados():
            texto = f"ID: {cargo_id} | Cargo: {nome_cargo} | Tipo contrato: {str(tipo_contrato).upper()} | ID do Setor: {setor_id}"
            container.add_widget(Label(text=texto))