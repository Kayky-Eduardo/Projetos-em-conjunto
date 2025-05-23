from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.button import Button
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
            produto.produto_id,
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
    
    def remover_cargo(self, id):
        conexao = sqlite3.connect('BD/projeto.db')
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produto WHERE produto_id = ?", (id,))
        cursor.execute("DELETE FROM estoque WHERE produto_id = ?", (id,))
        conexao.commit()
        conexao.close()
        self.atualizar_dados()

    def atualizar_dados(self):
        container = self.ids.container
        container.clear_widgets()
        for produto_id, nome, tipo, preco, qntd, validade in self.buscar_dados():
            texto = f"Produto ID: {produto_id} | Produto: {nome} | Categoria: {tipo} | Preço: R${preco:.2f} | Quantidade: {qntd} | Validade: {validade}"
            container.add_widget(Label(text=texto))
            butao = Button(text='Deletar')
            butao.bind(on_press=lambda instance, id=produto_id: self.remover_cargo(id))
            container.add_widget(butao)
