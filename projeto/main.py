from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from login.tela_login import TelaPrimeira
from menu.menu import TelaSecundaria

class MeuMainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaPrimeira(name='inicial'))
        sm.add_widget(TelaSecundaria(name='secundaria'))
        return sm


if __name__== '__main__':
    MeuMainApp().run()