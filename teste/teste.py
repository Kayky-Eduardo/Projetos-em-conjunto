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

    def mudar_cor(self, instance):
        # Aqui você pode mudar a cor do botão, por exemplo
        self.botao.background_color = (0.4, 0.7, 1, 1)  # Azul

MeuApp().run()
