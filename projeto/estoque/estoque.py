from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import sqlite3

class Tela_Estoque(BoxLayout):
    def buscar_dados(self):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("""
        SELECT 
            produto.nome_produto,
            produto.tipo_produto,
            produto.preco_produto,
            estoque.qntd_produto,
            estoque.validade
        FROM produto
        LEFT JOIN estoque ON produto.produto_id = estoque.produto_id;
        """)
        dados = cursor.fetchall()
        conexao.close()
        return dados

    def atualizar_dados(self):
        container = self.ids.container
        container.clear_widgets()
        for nome, tipo, preco, qntd, validade in self.buscar_dados():
            texto = f"Produto: {nome} | Categoria: {tipo} | Preço: R${preco:.2f} | Quantidade: {qntd} | Validade: {validade}"
            container.add_widget(Label(text=texto))

class EstoqueApp(App):
    def build(self):
        return Tela_Estoque()

if __name__ == '__main__':
    EstoqueApp().run()