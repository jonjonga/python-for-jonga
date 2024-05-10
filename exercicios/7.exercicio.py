import os
os.system("cls || clear")

nomeProduto = input("Digite o nome do produto: ")
quantidadeProduto = int(input("Quantidadade do produto: "))
precoUnidade = float(input("Preço do produto: "))

total = quantidadeProduto * precoUnidade

if quantidadeProduto <= 5:
    desconto = total * 0.02

elif quantidadeProduto > 5 and quantidadeProduto <= 10:
    desconto = total * 0.03

else :
    desconto = total * 0.05

totalPagar = total - desconto

print(f"Total: {total}")
print(f"Desconto: {desconto}")
print(f"Total a pagar: {totalPagar}")