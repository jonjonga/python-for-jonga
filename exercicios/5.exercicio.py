import os
os.system("cls || clear")

numeroUm = int(input("Digite o primeiro número: "))
numeroDois = int(input("Digite o segundo número: "))

soma = numeroUm + numeroDois
media = soma / 2
produto = numeroUm * numeroDois

print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")

maior = max(numeroUm, numeroDois)
menor = min(numeroUm, numeroDois)

