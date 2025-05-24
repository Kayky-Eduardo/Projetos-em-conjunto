import sqlite3
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'cadastro_encomenda.kv'))


class Cadastro_Encomenda(Screen):
    cliente_cpf = ObjectProperty(None)
    produto_id = ObjectProperty(None)
    qntd_produto = ObjectProperty(None)
    data_pedido = ObjectProperty(None)
    data_entrega = ObjectProperty(None)
    enviar = ObjectProperty(None)

    def buscar_dados(self, produto_id, cliente_cpf):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT qntd_produto FROM estoque WHERE produto_id = ?
        """, (produto_id,))
        produto = cursor.fetchone()
        
        cursor.execute("SELECT 1 FROM cliente WHERE cliente_cpf = ?", (cliente_cpf,))
        if not cursor.fetchone():
            self.enviar.text = "Cliente não encontrado."
            cliente_cpf = cursor.fetchone()
            conexao.close()
            
        return produto, cliente_cpf
    
    def adicionar_banco(self):    
        if not self.produto_id.text.isdigit():
            self.enviar.text = 'Preencha o campo de produto id corretamente.'
            return
        
        elif not self.qntd_produto.text.isdigit():
            self.enviar.text = 'Preencha o campo de quantidade corretamente.'
            return
    
        elif not self.cliente_cpf.text:
            self.enviar.text = 'Preencha o campo cliente CPF de forma correta.'    
            return
        
        elif not self.data_pedido.text:
            self.enviar.text = 'Preencha o campo de data do pedido corretamente.'
            return
          
        cliente_cpf_validacao = self.cliente_cpf.text
        produto_id_validacao = int(self.produto_id.text)
        qntd_produto_validacao = int(self.qntd_produto.text)
        data_pedido_validacao = self.data_pedido.text
        data_entrega_validacao = self.data_entrega.text
        quantidade, cpf = self.buscar_dados(produto_id_validacao, cliente_cpf_validacao)

        try:
            if quantidade and cpf:
                if quantidade[0] >= int(qntd_produto_validacao):
                    conexao = sqlite3.connect('BD/projeto.db')
                    cursor = conexao.cursor()
                    cursor.execute('''
                        INSERT INTO encomenda (cliente_cpf, produto_id, qntd_produto, data_pedido, data_entrega)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (cliente_cpf_validacao, produto_id_validacao, qntd_produto_validacao, data_pedido_validacao, data_entrega_validacao))
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
                self.enviar.text = 'Produto ou CPF de cliente não encontrado.'

        except sqlite3.Error as e:
            self.enviar.text = f'Erro: {e}'
        
        except ValueError:
            self.enviar.text = f'Erro na quantidade.'

# class Cadastro_EncomendaApp(App):
#     def build(self):
#         return Cadastro_Encomenda()

# if __name__ == '__main__':
#     Cadastro_EncomendaApp().run()
