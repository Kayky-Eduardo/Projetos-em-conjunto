import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Line

class Encostar(FloatLayout, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        print("Mouse Down", touch)

    def on_touch_move(self, touch):
        print("Mouse Move", touch)

    def on_touch_up(self, touch):
        print("Mouse UP", touch)

class MenuApp(App):
    def build(self):
        return Encostar()

if __name__ == '__main__':
    MenuApp().run()