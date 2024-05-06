import os
os.system("cls || clear")

print("== Coletando dados do usuário ==")
idade = int(input("Digite a idade do usuário: "))

if idade >= 18 and idade <= 65:
    print("O usuário é obrigado a votar!")
else:
    print("O usuário não é obrigado a votar!")