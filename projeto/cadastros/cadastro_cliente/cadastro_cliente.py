import sqlite3
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'cadastro_cliente.kv'))

class Cadastro_Cliente(Screen):
    cliente_cpf = ObjectProperty(None)
    tel1 = ObjectProperty(None)
    tel2 = ObjectProperty(None)
    email = ObjectProperty(None)
    enviar = ObjectProperty(None)
     
    def validar_cpf(self, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        for i in [9, 10]:
            soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
            digito = (soma * 10 % 11) % 10
            if digito != int(cpf[i]):
                return False
        return True
    
    def validar_telefone(self, telefone):
        telefone = ''.join(c for c in telefone if c.isdigit())
        return len(telefone) in [10, 11]
    
    def adicionar_banco(self):
        cliente_cpf_validacao = self.cliente_cpf.text
        tel1_validacao = self.tel1.text
        tel2_validacao = self.tel2.text
        email_validacao = self.email.text

        if not self.validar_cpf(cliente_cpf_validacao):
            self.enviar.text = 'CPF inválido!'
            return
        
        if not self.validar_telefone(tel1_validacao):
            self.enviar.text = 'Telefone 1 inválido!'
            return
             
        try:
            conexao = sqlite3.connect('BD/projeto.db')
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO cliente (cliente_cpf, telefone1, telefone2, email)
                VALUES (?, ?, ?, ?)
            ''', (cliente_cpf_validacao, tel1_validacao, tel2_validacao, email_validacao))
            conexao.commit()
            conexao.close()
            self.enviar.text = 'Cadastro realizado com sucesso!'
            
        except sqlite3.Error as e:
            self.enviar.text = f'Erro: {e}'