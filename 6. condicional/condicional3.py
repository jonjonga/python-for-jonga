import os
os.system("cls || clear")
login = str(input("Digite o login: "))
senha = int(input("Digite a senha: "))

if login == "jonjonga" and senha == 12345:  
    print("Login aceito")
else: 
    print("Login negado")