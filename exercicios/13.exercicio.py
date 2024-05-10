import os
os.system("cls || clear")

numeroPar = 0
numeroImpar = 0


for i in range (5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    if numero % 2 == 0:
         numeroPar += 1
    else:
        numeroImpar += 1

print(f"Números pares: {numeroPar}")
print(f"Números impares: {numeroImpar}")
