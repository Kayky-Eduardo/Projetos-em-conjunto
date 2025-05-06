import os
import sqlite3
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

class MeuLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MeuLayout, self).__init__(**kwargs)

        self.cols = 1

        self.dentro = GridLayout()
        self.dentro.cols = 2
        
        
        self.dentro.add_widget(Label(text="CPF: "))
        self.cpf = TextInput(multiline=False)
        self.dentro.add_widget(self.cpf)
        
        self.dentro.add_widget(Label(text="Senha: "))
        self.senha = TextInput(multiline=False)
        self.dentro.add_widget(self.senha)
        
        self.add_widget(self.dentro)

        self.enviar = Button(text="Enviar", font_size=20)
        self.enviar.bind(on_press=self.Verificar)
        self.add_widget(self.enviar)


    def Verificar(self, instancia):
        cpf = self.cpf.text
        senha = self.senha.text
        os.system('cls')
        print(f'CPF: {cpf}\nSenha: {senha}')
    
        conexao = sqlite3.connect("BD/projeto.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM funcionario WHERE funcionario_cpf=? AND senha=?", (cpf, senha))
        resultado = cursor.fetchone()
        conexao.close()

        if resultado:
            self.enviar.text = "Login bem-sucedido!"
        else:
            self.enviar.text = "CPF ou senha inválidos."


class MeuApp(App):
    def build(self):
        return MeuLayout()
    
if __name__ == '__main__':
    MeuApp().run()