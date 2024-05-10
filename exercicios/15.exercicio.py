import os
os.system("cls || clear")

soma = 0


for i in range (3):
    nota = int(input(f"Digite a nota da {i + 1}º unidade: "))
    soma += nota

media = soma / 3

if media >= 7:
    print("APROVADO")
elif media < 6.9 and media > 5:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")
