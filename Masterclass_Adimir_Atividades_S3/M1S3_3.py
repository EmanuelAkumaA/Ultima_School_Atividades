#3. Crie um programa com uma função que necessite de três parâmetros e então que retorne a sua soma.
'''- Utilize o comando int(input()) para obter os três números inteiros de entrada.'''
'''- Passe os três números para uma função por parâmetro.'''
'''- Calcule a soma e retorne o resultado.'''
'''- Mostre na tela a soma calculada, usando o comando print().'''
'''(ESCOLHI NÃO FAZER)- Extra: utilize *args (Opcional)'''
#Para fazer com (*args), só precisa trocar os parametros (a, b, c) por (*args).


def soma_tripla(a, b, c):
    return n1 + n2 + n3

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
resultado = soma_tripla(n1, n2, n3)
print(f'O resultado é: {resultado}')