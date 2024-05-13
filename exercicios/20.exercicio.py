import os 
os.system("cls || clear")

soma = 0
quantidadeNotas = 0

while True:
    nota = float(input("Digite a primeira nota: "))

    resposta = input("Deseja inserir mais alguma nota: ")
    resposta = resposta.upper()

    soma += nota
    quantidadeNotas += 1

    if resposta == "N":
        break

media = soma / quantidadeNotas

print(f"Média: {media}")

if(media >= 7):
        print("APROVADO")
elif(media >= 5 and media <= 6.9):
    print("RECUPERAÇÂO")
else:
     print("REPROVADO")