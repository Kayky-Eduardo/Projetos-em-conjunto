from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import sqlite3

class Tela_Cadastro_Venda(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def buscar_dados(self):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM venda
        """)

        dados = cursor.fetchall()
        conexao.close()
        return dados

    def atualizar_dados(self):
        container = self.ids.container
        container.clear_widgets()
        for venda_id, funcionario_id, cliente_cpf, compra_id in self.buscar_dados():
            texto = f"ID: {venda_id} | ID do funcionário: {funcionario_id} | CPF do cliente: {cliente_cpf} | ID da compra: {compra_id}"
            container.add_widget(Label(text=texto))

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
         
class Gerenciador_Telas(App):
    def build(self):
        return Builder.load_file("Tela_Cadastro_Venda.kv")

if __name__ == '__main__':
    Gerenciador_Telas().run()
