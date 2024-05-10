import os
os.system("cls || clear")

nome = str(input("Digite o seu nome: "))
sexo = str(input("Digite o sexo: "))
estadoCivil = str(input("Digite o estado civil: "))

if sexo == 'f' and estadoCivil == "casada":
   anosCasamento = int(input("Digite o tempo de casamento: "))


print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estadoCivil}")
print(f"Anos de casamento: {anosCasamento}")

