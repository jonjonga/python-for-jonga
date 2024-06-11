import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
numeros = []
maiorNumero = float('-inf')
menorNumero = float('inf')

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

if numero > maiorNumero:
    maiorNumero = numero
if numero < menorNumero:
    menorNumero = numero

media = sum(numeros) /  QUANTIDADE_NUMEROS

for i, numero in enumerate(numeros):
    print(f" {i + 1}º número: {numero}")


print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")