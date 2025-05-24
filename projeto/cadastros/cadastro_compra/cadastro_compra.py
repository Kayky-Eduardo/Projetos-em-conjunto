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
       
    def buscar_dados(self, produto_id):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT qntd_produto FROM estoque WHERE produto_id = ?
        """, (produto_id,))
        dados = cursor.fetchone()
        conexao.close()
        return dados

    def adicionar_banco(self):
        if not self.produto_id.text.isdigit():
            self.enviar.text = 'Preencha o campo de produto id corretamente.'
            return
        
        elif not self.qntd_produto.text.isdigit():
            self.enviar.text = 'Preencha o campo de quantidade corretamente.'
            return
            
        produto_id_validacao = int(self.produto_id.text)
        qntd_produto_validacao = int(self.qntd_produto.text)
        quantidade = self.buscar_dados(produto_id_validacao)
        
        try:
            if quantidade:
                if quantidade[0] >= int(qntd_produto_validacao):
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

            else:
                self.enviar.text = 'Produto não encontrado no estoque'
                
        except sqlite3.Error as e:
            self.enviar.text = f'Erro: {e}'

        except ValueError:
            self.enviar.text = f'Erro na quantidade.'