import os
os.system("cls || clear")


numeroUm = int(input ("Digite o primeiro valor: "))
numeroDois = int(input("Digite o segundo valor: "))
operacao = str(input("Digite a operação desejada: "))

match(operacao):
    case '*':
       resultado = numeroUm * numeroDois
    case '+':
        resultado = numeroUm + numeroDois
    case '/':
        resultado = numeroUm / numeroDois
    case '-':
        resultado = numeroUm - numeroDois
    case _:
        resultado = 0

print(f"{numeroUm} {operacao} {numeroDois} = {resultado}")