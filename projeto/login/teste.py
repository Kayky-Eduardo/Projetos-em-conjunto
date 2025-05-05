from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

class MeuLayout(GridLayout):
    f_cpf = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class MeuApp(App):
    def build(self):
        return MeuLayout()
    
if __name__ == '__main__':
    MeuApp().run()