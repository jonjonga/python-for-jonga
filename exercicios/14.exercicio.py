import os
os.system("cls || clear")

media = 0
soma = 0 

for i in range (4):
    nota = int(input(f"Digite a {i + 1}º nota: "))
    soma += nota

media = soma / 4

print(f"Média: {media}")
