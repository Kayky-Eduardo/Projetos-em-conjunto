import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from login.tela_login import Tela_Login
from menu.menu import Menu
<<<<<<< Updated upstream

=======
from cadastros.tela_cadastros.menu_cadastros import Menu_Cadastro
from cadastros.cadastrar_produto.cadastro_produto import TelaCadastro
from cadastros.cadastro_cliente.cadastro_cliente import TelaCadastro_Cliente
>>>>>>> Stashed changes
class MainApp(App):
    def build(self):
        Builder.load_file(os.path.join('login', 'tela_login.kv'))
        sm = ScreenManager()
        sm.add_widget(Tela_Login(name='tela_login'))
        sm.add_widget(Menu(name='menu'))
<<<<<<< Updated upstream
=======
        sm.add_widget(Menu_Cadastro(name='Menu_cadastros'))
        sm.add_widget(TelaCadastro(name='telacadastro'))
        sm.add_widget(TelaCadastro_Cliente(name='telacadastro_cliente'))
>>>>>>> Stashed changes
        return sm
    
if __name__ == '__main__':
    MainApp().run()