# Você está desenvolvendo uma aplicação para um restaurante que precisa calcular o valor final de uma conta com base no
#  valor dos pratos e uma taxa de serviço. Você tem uma função chamada calcula_conta que recebe dois parâmetros: 
# valor_pratos (uma lista com os preços de cada prato) e taxa_servico. Essa função retorna o valor final da conta, 
# incluindo a taxa de serviço.

# Sua tarefa é criar um decorador chamado decorator_resumo, que será usado com a função calcula_conta.
# O decorador deve imprimir os parâmetros: valor_pratos, taxa_servico e o resultado da função.

# Por exemplo, ao chamar a função calcula_conta com uma lista de valores [10.0, 20.0, 15.0] e uma taxa de 
# serviço de 0.1 (10%), o resultado deve ser algo como:

# VALOR PRATOS: [10.0, 20.0, 15.0], TAXA DE SERVIÇO: 0.1, TOTAL: 48.5
# Nesse caso, 48.5 é o valor total da conta, somando todos os pratos e aplicando a taxa de serviço de 10%.




# def decoator_resumo(funcao):
#     def wrapper(*args, **kwargs):
#         print(f"VALOR PRATOS: {args[0]}, TAXA DE SERVIÇO: {args[1]}, TOTAL: {funcao(*args, **kwargs)}")

def decorator_resumo(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print("VALOR PRATOS: {}, TAXA DE SERVIÇO: {}, TOTAL: {}".format(valor_pratos, taxa_servico, resultado))
        return resultado
    return wrapper


@decorator_resumo
def calcula_conta(valor_pratos, taxa_servico):
    total = sum(valor_pratos)
    total += total * taxa_servico
    return total

valor_pratos = []
taxa_servico = 0.1
pratos = int(input('quantidade de pratos requisitados: '))
while pratos > 0:
    valor_prato = float(input('valor do prato: '))
    valor_pratos.append(valor_prato)
    pratos -= 1

calcula_conta(valor_pratos, taxa_servico)