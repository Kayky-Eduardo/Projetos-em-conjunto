import sqlite3
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty


class Cadastro_Setor(GridLayout):
    setor_id = ObjectProperty(None)
    nome_setor = ObjectProperty(None)
    nome_responsavel = ObjectProperty(None)
    enviar = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def adicionar_banco(self):
        setor_id_validacao = self.setor_id.text
        nome_setor_validacao = self.nome_setor.text
        nome_responsavel_validacao = self.nome_responsavel.text

        try:
            conexao = sqlite3.connect("BD/projeto.db")
            cursor = conexao.cursor()
            cursor.execute('''
            INSERT INTO setor (setor_id, nome_setor, nome_responsavel)
            VALUES (?, ?, ?)
        ''', (setor_id_validacao, nome_setor_validacao, nome_responsavel_validacao))
            conexao.commit()
            conexao.close()
            self.enviar.text = "Cadastro realizado"
            
        except sqlite3.Error:
            self.enviar.text = "Erro: Verifique os dados e cheque se já não está cadastrado"

class Cadastro_setorApp(App):
    def build(self):
        return Cadastro_Setor()

if __name__ == '__main__':
    Cadastro_setorApp().run()
