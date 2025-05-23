import sqlite3
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'cadastro_compra.kv'))

class Cadastro_Compra(Screen):
    produto_id = ObjectProperty(None)
    qntd_produto = ObjectProperty(None)
    enviar = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo_contrato = None
       
    def buscar_dados(self):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT qntd_produto FROM estoque
        """)
        dados = cursor.fetchall()
        conexao.close()
        return dados

    def adicionar_banco(self):
        produto_id_validacao = self.produto_id.text
        qntd_produto_validacao = self.qntd_produto.text
        quantidade = self.buscar_dados()
        estoque = int(quantidade[0][0])
        try:
            if int(estoque) >= int(qntd_produto_validacao):
                conexao = sqlite3.connect('BD/projeto.db')
                cursor = conexao.cursor()
                cursor.execute('''
                    INSERT INTO compra (produto_id, qntd_produto)
                    VALUES (?, ?)
                ''', (produto_id_validacao, qntd_produto_validacao,))
                
                cursor.execute('''
                UPDATE estoque 
                SET qntd_produto = qntd_produto - ? 
                WHERE produto_id = ?
                ''', (qntd_produto_validacao, produto_id_validacao))
                conexao.commit()
                conexao.close()
                self.enviar.text = 'Cadastro realizado com sucesso!'
            else:
                self.enviar.text = 'Quantidade insuficiente no estoque'

        except sqlite3.Error as e:
            self.enviar.text = f'Erro: {e}'