import sqlite3
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'cadastro_compra.kv'))

class Cadastro_Compra(Screen):
    compra_id = ObjectProperty(None)
    produto_id = ObjectProperty(None)
    qntd_produto = ObjectProperty(None)
    enviar = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo_contrato = None
       
    def adicionar_banco(self):
        compra_id_validacao = self.compra_id.text
        produto_id_validacao = self.produto_id.text
        qntd_produto_validacao = self.qntd_produto.text
        
        try:
            conexao = sqlite3.connect('BD/projeto.db')
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO compra (compra_id, produto_id, qntd_produto)
                VALUES (?, ?, ?)
            ''', (compra_id_validacao, produto_id_validacao, qntd_produto_validacao,))
            conexao.commit()
            conexao.close()
            self.enviar.text = 'Cadastro realizado com sucesso!'
            
        except sqlite3.Error as e:
            self.enviar.text = f'Erro: {e}'