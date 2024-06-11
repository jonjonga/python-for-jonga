import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 3
notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas) / QUANTIDADE_NOTAS

for i, nota in enumerate(notas): 
    print(f" {i + 1}º nota: {nota}")

print(f"Média: {notas}")

