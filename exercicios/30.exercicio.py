import os
from dataclasses import dataclass

os.system ("cls||clear")

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    def __init__(self,nome,idade,altura,peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    peso = float(input("Digite o peso do aluno em kg: "))
    altura = float(input("Digite a altura do aluno: "))

    aluno = Aluno(nome = nome, idade = idade, peso = peso, altura = altura)
    alunos.append(aluno)

for dados_aluno in alunos:
    print(f"Nome: {dados_aluno.nome}")
    print(f"Idade: {dados_aluno.idade}")
    print(f"Altura: {dados_aluno.altura}")
    print(f"Peso: {dados_aluno.peso}")
