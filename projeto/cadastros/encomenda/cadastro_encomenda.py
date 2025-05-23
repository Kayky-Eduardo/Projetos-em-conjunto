import sqlite3
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'cadastro_encomenda.kv'))


class Cadastro_Encomenda(Screen):
    produto_id = ObjectProperty(None)
    nome_produto = ObjectProperty(None)
    tipo_produto = ObjectProperty(None)
    preco_produto = ObjectProperty(None)
    quantidade = ObjectProperty(None)
    validade = ObjectProperty(None)
    enviar = ObjectProperty(None)

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
                    

# class Cadastro_EncomendaApp(App):
#     def build(self):
#         return Cadastro_Encomenda()

# if __name__ == '__main__':
#     Cadastro_EncomendaApp().run()
