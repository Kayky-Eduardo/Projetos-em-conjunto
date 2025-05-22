from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import sqlite3
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'tela_cadastro_encomenda.kv'))

class Tela_Cadastro_encomenda(Screen):
    procurar = ObjectProperty(None)
    cliente_cpf = ObjectProperty(None)
    produto_id = ObjectProperty(None)
    qntd_produto = ObjectProperty(None)
    data_pedido = ObjectProperty(None)
    data_entrega = ObjectProperty(None)
    enviar = ObjectProperty(None)
        
    def buscar_dados(self):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT 
                encomenda.encomenda_id,
                encomenda.cliente_cpf,
                encomenda.produto_id,
                encomenda.qntd_produto,
                encomenda.data_pedido,
                encomenda.data_entrega
            FROM encomenda
            LEFT JOIN produto ON encomenda.produto_id = produto.produto_id;
        """)

        dados = cursor.fetchall()
        conexao.close()
        return dados

    def atualizar_dados(self):
        container = self.ids.container
        container.clear_widgets()
        for encomenda_id, cliente_cpf, produto_id, qntd_produto, data_pedido, data_entrega in self.buscar_dados():
            texto = f"ID: {encomenda_id} | CPF do cliente: {cliente_cpf} | ID do produto: {produto_id} | Quantidade: {qntd_produto} | Data pedido: {data_pedido} | Data entrega: {data_entrega}"
            container.add_widget(Label(text=texto))


  
# class Gerenciador_Telas(App):
#     def build(self):
#         return Builder.load_file("tela_cadastro_encomenda.kv")

# if __name__ == '__main__':
#     Gerenciador_Telas().run()
