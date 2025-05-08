import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.graphics import Color

class Encostar(FloatLayout, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, .5, mode='rgba')
            self.rect = Rectangle(pos=(0,0), size=(50,50))

    def on_touch_down(self, touch):
        print("Mouse Down", touch)

    def on_touch_move(self, touch):
        print("Mouse Move", touch)

    def on_touch_up(self, touch):
        print("Mouse UP", touch)

class MeuApp(App):
    def build(self):
        return Encostar()

if __name__ == '__main__':
    MeuApp().run()