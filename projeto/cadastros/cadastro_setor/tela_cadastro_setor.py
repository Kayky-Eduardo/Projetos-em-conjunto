from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.lang import Builder
import sqlite3
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'tela_cadastro_setor.kv'))

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
            butao = Button(text='Deletar')
            butao.bind(on_press=lambda instance, id=setor_id: self.remover_setor(id))
            container.add_widget(butao)
    
    def remover_setor(self, id):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM setor WHERE setor_id = ?", (id,))
        conexao.commit()
        conexao.close()
        self.atualizar_dados()