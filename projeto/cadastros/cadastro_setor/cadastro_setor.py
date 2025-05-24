import sqlite3
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'cadastro_setor.kv'))

class Cadastro_Setor(Screen):
    nome_setor = ObjectProperty(None)
    nome_responsavel = ObjectProperty(None)
    enviar = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def adicionar_banco(self):
        nome_setor_validacao = self.nome_setor.text
        nome_responsavel_validacao = self.nome_responsavel.text
        
        if not nome_setor_validacao:
            self.enviar.text = 'Preencha o campo de setor.'
            return
        
        elif not nome_responsavel_validacao:
            self.enviar.text = 'Preencha o campo de nome do responsável.'
            return
        
        try:
            conexao = sqlite3.connect('BD/projeto.db')
            cursor = conexao.cursor()
            cursor.execute('''
            INSERT INTO setor (nome_setor, nome_responsavel)
            VALUES (?, ?)
        ''', (nome_setor_validacao, nome_responsavel_validacao))
            conexao.commit()
            conexao.close()
            self.enviar.text = 'Cadastro realizado'
            
        except sqlite3.Error:
            self.enviar.text = 'Erro: Verifique os dados e cheque se já não está cadastrado'