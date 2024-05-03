import os
os.system("cls || clear")

print("Solicitando dados")
nome = input("Digite o nome do aluno: ")
idade = input("Digite a idade do aluno: ")
notaUm = int(input("Digite a primeira nota:  "))
notaDois = int(input("Digite a segunda nota: "))
soma = notaUm + notaDois
media = soma / 2

print("jonExibindo dados")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {notaUm}")
print(f"Segunda nota: {notaDois}")
print(f"Média: {media}")