import os
os.system("cls || clear")

print("Solicitando dados")
nome = input("Digite o nome do aluno: ")
idade = input("Digite a idade do aluno: ")
notaUm = int(input("Digite a primeira nota: "))
notaDois = int(input("Digite a segunda nota: "))
notaTres = int(input("Digite a terceira nota: "))
soma = notaUm + notaDois
media = soma / 2

print("Exibindo dados")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {notaUm}")
print(f"Segunda nota: {notaDois}")
print(f"Segunda terceira: {notaTres}")
print(f"Média: {media}")

if media  >= 7:
    print("Aprovado.")
else:
    print("Reprovado")