def decorator_imprimir(func):
    def wrapper(capital, taxa, tempo):
        juros = func(capital, taxa, tempo)
        print(f"Juros calculados: {juros}")
        return juros
    return wrapper

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    juros = (capital * taxa * tempo) / 100
    return juros

# Exemplo de uso
capital = 1000
taxa = 5
tempo = 3

resultado = juros_simples(capital, taxa, tempo)

# MELHORADO

def decorator_imprimir(func):

    # Um decorator que calcula e imprime os juros de uma função.

    # Args:
    #     func (callable): A função que recebe capital, taxa e tempo como argumentos.

    # Returns:
    #     callable: A função decorada.

    def wrapper(capital, taxa, tempo):
        juros = func(capital, taxa, tempo)
        print(f"Juros calculados: {juros:.2f}")
        return juros
    return wrapper

@decorator_imprimir
def calcular_juros_simples(capital, taxa, tempo):

    # Calcula juros simples com base no capital, taxa e tempo.

    # Args:
    #     capital (float): O valor do capital.
    #     taxa (float): A taxa de juros.
    #     tempo (float): O período de tempo.

    # Returns:
    #     float: O valor dos juros calculados.

    juros = (capital * taxa * tempo) / 100
    return juros

# Exemplo de uso
capital = 1000
taxa = 5
tempo = 3

resultado = calcular_juros_simples(capital, taxa, tempo)
