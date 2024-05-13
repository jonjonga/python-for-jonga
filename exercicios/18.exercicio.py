import os
os.system("cls || clear")



soma: float = 0
for nota in range(1,3):
    while True:
        nota = float(input("Digite uma nota: "))


        if (nota < 0 or nota > 10):
            print("Valor inválido.")
        else:
            soma += nota
            break


media = soma / 2
print(f"Média: {media}")
