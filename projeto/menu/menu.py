import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Meulayout(GridLayout):
    pass


class MeuApp(App):
    def build(self):
        return MeuLayout()
