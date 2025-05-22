from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import sqlite3

class Tela_Cadastro_Compra(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def buscar_dados(self):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM compra
        """)

        dados = cursor.fetchall()
        conexao.close()
        return dados

    def atualizar_dados(self):
        container = self.ids.container
        container.clear_widgets()
        for compra_id, produto_id, qntd_produto in self.buscar_dados():
            texto = f"ID: {compra_id} | ID do Produto: {produto_id} | Quantidade: {qntd_produto}"
            container.add_widget(Label(text=texto))

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
 
class Gerenciador_Telas(App):
    def build(self):
        return Builder.load_file("Tela_Cadastro_Compra.kv")

if __name__ == '__main__':
    Gerenciador_Telas().run()
