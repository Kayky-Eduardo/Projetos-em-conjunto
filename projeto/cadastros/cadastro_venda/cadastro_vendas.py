from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import sqlite3
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'cadastro_venda.kv'))

class Cadastro_Venda(Screen):
    venda_id = ObjectProperty(None)
    funcionario_id = ObjectProperty(None)
    cliente_cpf = ObjectProperty(None)
    compra_id = ObjectProperty(None)
    enviar = ObjectProperty(None)
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo_contrato = None
       
    def adicionar_banco(self):
        venda_id_validacao = self.venda_id.text
        funcionario_id_validacao = self.funcionario_id.text
        cliente_cpf_validacao = self.cliente_cpf.text
        compra_id_validacao = self.compra_id.text
        
        try:
            conexao = sqlite3.connect('BD/projeto.db')
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO venda (venda_id, funcionario_id, cliente_cpf, compra_id)
                VALUES (?, ?, ?, ?)
            ''', (venda_id_validacao, funcionario_id_validacao, cliente_cpf_validacao, compra_id_validacao))
            conexao.commit()
            conexao.close()
            self.enviar.text = 'Cadastro realizado com sucesso!'
            
        except sqlite3.Error as e:
            self.enviar.text = f'Erro: {e}'
                    

class Cadastro_VendaApp(App):
    def build(self):
        return Cadastro_Venda()

if __name__ == '__main__':
    Cadastro_VendaApp().run()
