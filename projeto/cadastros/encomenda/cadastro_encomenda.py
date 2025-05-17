import sqlite3
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty


class Cadastro_Encomenda(GridLayout):
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
        cargo_id_validacao = self.cargo_id.text
        nome_cargo_validacao = self.nome_cargo.text
        tipo_contrato_validacao = self.tipo_contrato
        setor_id_validacao = self.setor_id.text
        
        # try:
        #     # conexao = sqlite3.connect('BD/projeto.db')
        #     # cursor = conexao.cursor()
        #     # cursor.execute('''
        #     #     INSERT INTO cargo (cargo_id, nome_cargo, tipo_contrato, setor_id)
        #     #     VALUES (?, ?, ?, ?)
        #     # ''', (cargo_id_validacao, nome_cargo_validacao, tipo_contrato_validacao, setor_id_validacao))
        #     # conexao.commit()
        #     # conexao.close()
        #     # self.enviar.text = 'Cadastro realizado com sucesso!'
            
        # except sqlite3.Error as e:
        #     self.enviar.text = f'Erro: {e}'
                    

class Cadastro_EncomendaApp(App):
    def build(self):
        return Cadastro_Encomenda()

if __name__ == '__main__':
    Cadastro_EncomendaApp().run()
