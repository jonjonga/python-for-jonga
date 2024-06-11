import os
from dataclasses import dataclass

os.system ("cls || clear")

QUANTADIDADE_LIVROS = 2

@dataclass
class Livro:
    def __init__(self,titulo,autor,numero_pag,preco):
        self.titulo = titulo
        self.autor = autor 
        self.numero_pag = numero_pag
        self.preco = preco

livros = []

for i in range(QUANTADIDADE_LIVROS):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    numero_pag = int(input("Digite o número de páginas: "))
    preco = int(input("Digite o preço do livro: "))

    livro = Livro(titulo = titulo, autor = autor, numero_pag = numero_pag, preco = preco)
    livros.append(livro)

for dados_livro in livros:
    print(f"Título: {dados_livro.titulo}")
    print(f"Autor: {dados_livro.autor}")
    print(f"Número de páginas: {dados_livro.numero_pag}")
    print(f"Preço: {dados_livro.preco}")