import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from login.tela_login import Tela_Login
from menu.menu import Menu

class MainApp(App):
    def build(self):
        Builder.load_file(os.path.join('login', 'tela_login.kv'))
        sm = ScreenManager()
        sm.add_widget(Tela_Login(name='tela_login'))
        sm.add_widget(Menu(name='menu'))
        return sm
    
if __name__ == '__main__':
    MainApp().run()