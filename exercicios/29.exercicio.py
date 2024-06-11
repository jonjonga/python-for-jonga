import os
os.system("cls || clear")

def cabecalho():
    os.system("cls || clear")
    print("---------------------")
    print(" === SENAI | FIEB ===")
    print("---------------------")

def somar(n1, n2):
    resultado = n1 + n2
    return resultado
def multiplicar(n1, n2):
    resultado = n1 * n2
    return resultado
def dividir(n1, n2):
    resultado = n1 / n2
    return resultado
def subtrair(n1, n2):
    resultado = n1 - n2
    return resultado

cabecalho()
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = somar (primeiroNumero, segundoNumero)
divisao = dividir (primeiroNumero, segundoNumero)
multiplicacao = multiplicar (primeiroNumero, segundoNumero)
subtracao = subtrair (primeiroNumero, segundoNumero)

cabecalho()
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")