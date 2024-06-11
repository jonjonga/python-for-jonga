import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 6
numeros = []
numeroPar: int = 0
numeroImpar: int = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

    if numero % 2 == 0:
        numeroPar += 1
        
    else :
        numeroImpar += 1

for i, numero in enumerate(numeros):
    print(f"{i + 1}º número: {numero}")

print(f"Números pares: {numeroPar}")
print(f"Números impares: {numeroImpar}")