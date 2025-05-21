import sqlite3
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

class Cadastro_Encomenda(Screen, FloatLayout):
    cliente_cpf = ObjectProperty(None)
    produto_id = ObjectProperty(None)
    qntd_produto = ObjectProperty(None)
    data_pedido = ObjectProperty(None)
    data_entrega = ObjectProperty(None)
    enviar = ObjectProperty(None)
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo_contrato = None
       
    def adicionar_banco(self):
        cliente_cpf_validacao = self.cliente_cpf.text
        produto_id_validacao = self.produto_id.text
        qntd_produto_validacao = self.qntd_produto.text
        data_pedido_validacao = self.data_pedido.text
        data_entrega_validacao = self.data_entrega.text
        
        try:
            conexao = sqlite3.connect('BD/projeto.db')
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO encomenda (cliente_cpf, produto_id, qntd_produto, data_pedido, data_entrega)
                VALUES (?, ?, ?, ?, ?)
            ''', (cliente_cpf_validacao, produto_id_validacao, qntd_produto_validacao, data_pedido_validacao, data_entrega_validacao))
            conexao.commit()
            conexao.close()
            self.enviar.text = 'Cadastro realizado com sucesso!'
            
        except sqlite3.Error as e:
            self.enviar.text = f'Erro: {e}'              

class Cadastro_EncomendaApp(App):
    def build(self):
        return Cadastro_Encomenda()

if __name__ == '__main__':
    Cadastro_EncomendaApp().run()
