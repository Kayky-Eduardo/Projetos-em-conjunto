import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class MeuLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MeuApp(App):
    def build(self):
        return MeuLayout()

if __name__ == '__main__':
    MeuApp().run()