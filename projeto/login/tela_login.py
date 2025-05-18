import sqlite3
import os
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

class ImageButton(ButtonBehavior, Image):
        pass

# Carrega o arquivo KV
class Tela_Login(Screen, FloatLayout):
    Builder.load_file(os.path.join('login', 'tela_login.kv'))
    cpf = ObjectProperty(None)
    senha = ObjectProperty(None)
    enviar = ObjectProperty(None)
    senha_visivel = ObjectProperty(False)

    def verificar(self):
        cpf = self.cpf.text
        senha = self.senha.text

        conexao = sqlite3.connect("BD/projeto.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM funcionario WHERE funcionario_cpf=? AND senha=?", (cpf, senha))
        resultado = cursor.fetchone()
        conexao.close()

        if resultado:
            self.enviar.text = "Login bem-sucedido!"
        else:
            self.enviar.text = "CPF ou senha inválidos."

    def alternar_visibilidade(self):
        self.senha_visivel = not self.senha_visivel