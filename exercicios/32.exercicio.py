import os 
from dataclasses import dataclass

os.system ("cls || clear")

@dataclass
class Cliente:
    nome: str
    idade: int
    cpf: int
    endereco: str
    telefone: float

@dataclass
class Veiculo:
    placa: str
    cor: str
    numero_passageiros: int
    capacidade_tanque: int
    velocidade_max: int
    consumo_medio: float

clientes = []
veiculos = []

print(f"=== Cliente ===")
nome = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade do cliente: "))
cpf = int(input("Digite o CPf do cliente: "))
endereco = input("Digite o endereço do cliente: ")
telefone = int(input("Digite o telefone do cliente: "))

print(f"=== Carro ===")
placa = str(input("Digite a placa do veículo: "))
cor = input("Informe a cor do carro: ")
numero_passageiros = int(input("Informe a quantidade de passageiros: "))
capacidade_tanque = int(input("Informe a capacidaded do tanque de combustível: "))
velocidade_max = int(input("Informe a velocidade máxima: "))
consumo_medio = float(input("Informe o consumo médio de combustível: "))

cliente = Cliente(nome = nome, idade = idade, cpf = cpf, endereco = endereco, telefone = telefone)
veiculo = Veiculo(placa = placa, cor = cor, numero_passageiros = numero_passageiros, capacidade_tanque = capacidade_tanque, velocidade_max = velocidade_max, consumo_medio = consumo_medio)

clientes.append(cliente)
veiculos.append(veiculo)

for dados in cliente:
    print(f"Nome: {dados.nome}")
    print(f"Idade: {dados.idade}")
    print(f"CPF: {dados.cpf}")
    print(f"Endereço: {dados.endereco}")
    print(f"Telefone: {telefone}")

for dados in veiculo:
    print(f"Placa: {dados.placa}")
    print(f"Cor: {dados.cor}")
    print(f"Número de passageiros: {dados.numero_passageiros}")
    print(f"Capacidade do tanque: {dados.capacidade_tanque}")
    print(f"Consumo médio: {dados.consumo_medio}")