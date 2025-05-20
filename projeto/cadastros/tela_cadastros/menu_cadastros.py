from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__),'menu_cadastros.kv'))
class Menu_Cadastro(Screen, FloatLayout):
    pass

