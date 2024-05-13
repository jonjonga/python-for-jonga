import os
os.system ("cls || clear")

notaUm: float = -1
notaDois: float = -1

while(notaUm < 0 or notaUm > 10):
    notaUm = float(input("Digite a primeira nota: "))

while(notaDois < 0 or notaDois > 10):
    notaDois = float(input("Digite a segunda nota: "))

media = (notaUm + notaDois) / 2

print(f"Primeira Nota: {notaUm}")
print(f"Segunda Nota: {notaDois}")
print(f"Média: {media}")


print("== fim ===")