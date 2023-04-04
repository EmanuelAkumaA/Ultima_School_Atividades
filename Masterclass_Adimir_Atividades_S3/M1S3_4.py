#4. Crie um programa que seja capaz de obter e somar TODOS os números passados pelo usuário como entrada, permitindo somar qualquer quantidade de dados de entrada.
'''- Utilize uma estrutura de repetição para repetir a leitura de todos os números passados como entrada,até que encontre o valor '-1'.'''
'''- Ou seja, o número -1 será o critério de parada para a leitura dos dados de entrada.'''
'''- Utilize o comando int(input()) para obter todos os números inteiros de entrada.'''
'''- Calcule a soma de todos os números.'''
'''- Mostre na tela a soma calculada, usando o comando print().'''
'''- Extra: utilize Funções e *args (Opcional).'''

def soma_numeros(*args):
    return args 
#A soma começa com o valor (0), pois o usuário não digitou nenhum numero. Então não tem numero salvo na variavel (soma)
soma = 0
numero = int(input())
'''Enquanto (while) o numero digitado for diferente de -1 o coodigo continuara pedindo numero e somando
o primeiro numero digitado pelo proximo, e o resultado dos dois primeiros pelo proximo numero, e assim 
sucessivamente até o usuário digitar -1 (o numero for igual a -1), que não será somado aos outros numeros, porém é a condição para o
break do programa'''
while (numero > -5):
    soma += numero
    numero = int(input())
print(soma)