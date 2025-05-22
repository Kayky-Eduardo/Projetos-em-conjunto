from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.lang import Builder
import sqlite3
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'tela_estoque.kv'))

# ----- TELA ESTOQUE -----
class Tela_Estoque(Screen):
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
