from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kv = Builder.load_file("meu.kv")

class JanelaPrincipal(Screen):
    pass

class JanelaSecundaria(Screen):
    pass

class ControleJanelas(ScreenManager):
    pass

class MeuMainApp(App):
    def build(self):
        return kv
    

if __name__== '__main__':
    MeuMainApp().run()