import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from login.tela_login import Tela_Login
from menu.menu import Menu
from cadastros.tela_cadastros.menu_cadastros import Menu_Cadastro
from cadastros.cadastro_cliente.tela_cadastro_cliente import Tela_Cadastro_Cliente
from cadastros.cadastro_cliente.cadastro_cliente import Cadastro_Cliente
from cadastros.cadastro_venda.cadastro_vendas import Cadastro_Venda
from cadastros.cadastro_venda.tela_cadastro_venda import Tela_Cadastro_Venda
from cadastros.cadastro_compra.cadastro_compra import Cadastro_Compra
from cadastros.cadastro_compra.tela_cadastro_compra import Tela_Cadastro_Compra
from cadastros.cadastro_funcionario.cadastro_funcionario import Cadastro_Funcionario
from cadastros.cadastro_funcionario.tela_cadastro_funcionario import Tela_Cadastro_Funcionario
from cadastros.cadastro_cargo.cadastro_cargo import Cadastro_Cargo
from cadastros.cadastro_cargo.tela_cadastro_cargo import Tela_Cadastro_Cargo
from cadastros.cadastro_setor.cadastro_setor import Cadastro_Setor
from cadastros.cadastro_setor.tela_cadastro_setor import Tela_Cadastro_Setor



# Builder.load_file(os.path.join(os.path.dirname(__file__), 'cadastro_cliente.kv'))

Builder.load_file(os.path.join('login', 'tela_login.kv'))

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Tela_Login(name='tela_login'))
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Menu_Cadastro(name='Menu_cadastros'))
        sm.add_widget(Tela_Cadastro_Cliente(name='telacadastro_cliente'))
        sm.add_widget(Cadastro_Cliente(name='cadastro_cliente'))
        sm.add_widget(Tela_Cadastro_Venda(name='telacadastro_venda'))
        sm.add_widget(Cadastro_Venda(name='cadastro_venda'))
        sm.add_widget(Tela_Cadastro_Compra(name='telacadastro_compra'))
        sm.add_widget(Cadastro_Compra(name='cadastro_compra'))
        sm.add_widget(Tela_Cadastro_Funcionario(name='telacadastro_funcionario'))
        sm.add_widget(Cadastro_Funcionario(name='cadastro_funcionario'))
        sm.add_widget(Tela_Cadastro_Cargo(name='telacadastro_cargo'))
        sm.add_widget(Cadastro_Cargo(name='cadastro_cargo'))
        sm.add_widget(Tela_Cadastro_Setor(name='telacadastro_setor'))
        sm.add_widget(Cadastro_Setor(name='cadastro_setor'))
        return sm
    
if __name__ == '__main__':
    MainApp().run()

        # Button:
        #     text: 'Voltar'
        #     size_hint_y: None
        #     height: "40dp"
        #     on_press: root.manager.current = "Menu_cadastros"