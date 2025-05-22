import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from login.tela_login import Tela_Login
from menu.menu import Menu
from cadastros.tela_cadastros.menu_cadastros import Menu_Cadastro
from cadastros.cadastro_cliente.tela_cadastro_cliente import Tela_Cadastro_Cliente
from cadastros.cadastro_cliente.cadastro_cliente import Cadastro_Cliente

Builder.load_file(os.path.join('login', 'tela_login.kv'))

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Tela_Login(name='tela_login'))
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Menu_Cadastro(name='Menu_cadastros'))
        sm.add_widget(Tela_Cadastro_Cliente(name='telacadastro_cliente'))
        sm.add_widget(Cadastro_Cliente(name='cadastro_cliente'))
        return sm
    
if __name__ == '__main__':
    MainApp().run()