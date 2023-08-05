'''Desenvolva um programa que recebe dados de clientes e armazene-os em uma lista.
A saída do seu programa será os dados formatados dos 5 clientes cadastrados.

Nome (String)
CPF (String)
Idade (Inteiro)
'''
#FORMA COM CLASSES
#Criar uma classe cliente
class Cliente:
#Definir a função __init__ que vai ser a primeira a rodar no programa
    def __init__(self):
        self.nome  = None
        self.cpf   = None
        self.idade = None
#Criando uma função dento da função para pegar os dados e adcionar na classe clientes
    def cadasto(self):
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu CPF com apenas 11 números: ')
        idade = int(input('Digite a sua idade: '))
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
#Criando uma lista para adcionar todos os clientes
clientes = []
#Para fazer o sistema de repetição
for i in range(2):
    cliente = Cliente()
    cliente.cadasto()
    clientes.append(cliente)
#Para mostrar na tela os clientes
for i in range(2):
    print(clientes[i].nome)
    print(clientes[i].cpf)
    print(clientes[i].idade)


#DICIONARIO
'''dicionario_cliente = {}
seq = 5

while seq >= 1:
    dicionario_cliente['nome'] = input()
    dicionario_cliente['cpf'] = input()
    dicionario_cliente['idade'] = int(input())
    print("Cliente:", dicionario_cliente['nome'], "CPF:", dicionario_cliente['cpf'], "Idade:", dicionario_cliente['idade'])
    seq -= 1'''


#SIMPLIFICADA
'''clientes = []
for i in range(5):
    nome = input()
    cpf  = input()
    idade = int(input())
    cliente = {"nome": nome, "cpf": cpf, "idade": idade}
    clientes.append(cliente)
for i in range(5):
    print(clientes[i]["nome"])
    print(clientes[i]["idade"])
    print(clientes[i]["cpf"])'''