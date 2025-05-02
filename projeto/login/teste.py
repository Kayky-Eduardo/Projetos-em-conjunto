from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MeuLayoutGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MeuLayoutGrid, self).__init__(**kwargs)
        self.cols = 5
        self.rows = 5
        self.add_widget(Label(text="Login: "))
        self.nome = TextInput(multiline=False)
        
class MeuApp(App):
    def build(self):
        self.botao = Button(
            text="testando",
        )
        return self.botao
    
if __name__ == '__main__':
    MeuApp().run()