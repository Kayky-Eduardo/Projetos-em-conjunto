from kivy.app import App
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        return Button(text="Clique aqui", on_press=self.mudar_texto)

    def mudar_texto(self, instancia):
        instancia.text = "Clicado!"

MeuApp().run()
