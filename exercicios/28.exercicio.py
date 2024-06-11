import os
os.system("cls || clear")

def cabecalho():
    os.system("cls || clear")
    print(" -------------------- ")
    print(" === SENAI | FIEB === ")
    print(" -------------------- ")

def somar(primeiroNumero, segundoNumero):
    resultado = primeiroNumero + segundoNumero
    return resultado


cabecalho()
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)

cabecalho()
print(f"Soma: {soma}")
