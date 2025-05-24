import sqlite3
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'cadastro_cargo.kv'))

class Cadastro_Cargo(Screen):
    nome_cargo = ObjectProperty(None)
    setor_id = ObjectProperty(None)
    enviar = ObjectProperty(None)
        
    tipo_contrato = None

    def set_tipo_contrato(self, tipo, ativo):
        if ativo:
            self.tipo_contrato = tipo
            
    def adicionar_banco(self):
        if not self.setor_id.text.isdigit():
            self.enviar.text = 'Preencha o campo de setor id corretamente.'
            return
        
        nome_cargo_validacao = self.nome_cargo.text
        tipo_contrato_validacao = self.tipo_contrato
        setor_id_validacao = self.setor_id.text
        
        if not nome_cargo_validacao:
            self.enviar.text = 'Preencha o campo nome do cargo.'
            return
        
        elif not tipo_contrato_validacao:
            self.enviar.text = 'Escolha uma das opções(CNPJ ou CLT).'
            return
        
        try:
            conexao = sqlite3.connect('BD/projeto.db')
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO cargo (nome_cargo, tipo_contrato, setor_id)
                VALUES (?, ?, ?)
            ''', (nome_cargo_validacao, tipo_contrato_validacao, setor_id_validacao))
            conexao.commit()
            conexao.close()
            self.enviar.text = 'Cadastro realizado com sucesso!'
            
        except sqlite3.Error as e:
            self.enviar.text = f'Erro: {e}'