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

if numeroUm > numeroDois :
    print(f"Maior número: {numeroUm}")
    print(f"Menor número: {numeroDois}")
else:
    print(f"Maior número: {numeroDois}")
    print(f"Menor número: {numeroUm}")