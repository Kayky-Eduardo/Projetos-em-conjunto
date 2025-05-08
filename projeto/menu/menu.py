import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.uix.screenmanager import Screen

class TelaSecundaria(Screen):
    pass

class Menu(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MenuApp(App):
    def build(self):
        return Menu()

if __name__ == '__main__':
    MenuApp().run()