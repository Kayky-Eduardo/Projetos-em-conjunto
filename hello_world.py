from kivy.app import App
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        self.botao = Button(
            text="Clique aqui",
            background_normal='',
            background_color=(1, 0.4, 0.7, 1)  # Rosa
        )
        self.botao.bind(on_press=self.mudar_cor)
        return self.botao

    def mudar_cor(self, instancia):
        # Muda para um tom diferente de rosa ao clicar
        instancia.background_color = (1, 0, 0.5, 1)
        instancia.text = "Mudou!"

MeuApp().run()
