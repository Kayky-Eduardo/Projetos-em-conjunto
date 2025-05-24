from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import sqlite3
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'cadastro_venda.kv'))

class Cadastro_Venda(Screen):
    funcionario_cpf = ObjectProperty(None)
    cliente_cpf = ObjectProperty(None)
    compra_id = ObjectProperty(None)
    enviar = ObjectProperty(None)
                
    def buscar_dados(self, funcionario_cpf, cliente_cpf, compra_id):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT 1 FROM funcionario WHERE funcionario_cpf = ?", (funcionario_cpf,))
        
        if not cursor.fetchone():
            self.enviar.text = "Funcionário não encontrado."
            conexao.close()
            return False

        cursor.execute("SELECT 1 FROM cliente WHERE cliente_cpf = ?", (cliente_cpf,))
        if not cursor.fetchone():
            self.enviar.text = "Cliente não encontrado."
            conexao.close()
            return False

        cursor.execute("SELECT 1 FROM compra WHERE compra_id = ?", (compra_id,))
        if not cursor.fetchone():
            self.enviar.text = "Compra não encontrada."
            conexao.close()
            return False
        
        conexao.close()
        return True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo_contrato = None
    
    def adicionar_banco(self):      
        funcionario_cpf_validacao = self.funcionario_cpf.text
        cliente_cpf_validacao = self.cliente_cpf.text
        compra_id_validacao = self.compra_id.text
  
        if not funcionario_cpf_validacao or not cliente_cpf_validacao or not compra_id_validacao:
            self.enviar.text = "Preencha todos os campos obrigatórios."
            return
        
        if not self.buscar_dados(funcionario_cpf_validacao, cliente_cpf_validacao, compra_id_validacao):
            return
     
        try:    
            conexao = sqlite3.connect('BD/projeto.db')
            cursor = conexao.cursor()
            cursor.execute("SELECT 1 FROM venda WHERE compra_id = ?", (compra_id_validacao,))
            if cursor.fetchone():
                self.enviar.text = "Já existe uma venda cadastrada para esta compra."
                conexao.close()
                return
            
            cursor.execute('''
                INSERT INTO venda (funcionario_id, cliente_cpf, compra_id)
                VALUES (?, ?, ?)
            ''', (funcionario_cpf_validacao, cliente_cpf_validacao, compra_id_validacao))
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
