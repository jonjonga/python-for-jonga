import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 10
numeros = []
quantidadeNegativos = 0
quantidadePositivos = 0

for i in range(QUANTIDADE_NUMEROS):
    numeros = int(input("Digite um número: "))
    numeros.append(numero)

    if numeros > 0:
        quantidadePositivos += 1
    else:
        quantidadeNegativos += 1

print(f"Quantidade de números negativos: {quantidadeNegativos}")

print(f"Soma dos números positivos: {quantidadePositivos}")
