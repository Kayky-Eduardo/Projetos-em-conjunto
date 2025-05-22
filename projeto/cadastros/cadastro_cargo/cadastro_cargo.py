import sqlite3
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'cadastro_cargo.kv'))

class Cadastro_Cargo(Screen):
    cargo_id = ObjectProperty(None)
    nome_cargo = ObjectProperty(None)
    setor_id = ObjectProperty(None)
    enviar = ObjectProperty(None)
        
    tipo_contrato = None

    def set_tipo_contrato(self, tipo, ativo):
        if ativo:
            tipo_contrato = tipo
            
    def adicionar_banco(self):
        cargo_id_validacao = self.cargo_id.text
        nome_cargo_validacao = self.nome_cargo.text
        tipo_contrato_validacao = self.tipo_contrato
        setor_id_validacao = self.setor_id.text
        
        try:
            conexao = sqlite3.connect('BD/projeto.db')
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO cargo (cargo_id, nome_cargo, tipo_contrato, setor_id)
                VALUES (?, ?, ?, ?)
            ''', (cargo_id_validacao, nome_cargo_validacao, tipo_contrato_validacao, setor_id_validacao))
            conexao.commit()
            conexao.close()
            self.enviar.text = 'Cadastro realizado com sucesso!'
            
        except sqlite3.Error as e:
            self.enviar.text = f'Erro: {e}'