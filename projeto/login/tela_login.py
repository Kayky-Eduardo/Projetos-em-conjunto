import sqlite3
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.lang import Builder

class ImageButton(ButtonBehavior, Image):
        pass

class Tela_Login(GridLayout):
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
            Builder.load_file('menu/meu.kv')
        else:
            self.enviar.text = "CPF ou senha inválidos."

    def alternar_visibilidade(self):
        self.senha_visivel = not self.senha_visivel

class LoginApp(App):
    def build(self):
        return Tela_Login()

if __name__ == '__main__':
    Tela_Login().run()
