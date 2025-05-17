from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

class Menu(Screen, FloatLayout):
    Builder.load_file(os.path.join('menu','menu.kv'))