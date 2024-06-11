import os
os.system("cls || clear")

def cabecalho():
    os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
numeros = []

for i in range(QUANTIDADE_NUMEROS):
    cabecalho()
    numeros = int(input("Digite um número: "))
    if numero < 0:
        numero = 0

    numeros.append(numero)

for i, numero in enumerate(numeros):
    print(f"{i + 1}º número: {numero}")
