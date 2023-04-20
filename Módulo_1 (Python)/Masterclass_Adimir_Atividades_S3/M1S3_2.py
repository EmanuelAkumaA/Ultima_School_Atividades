#2. Crie uma função que recebe um número inteiro por parâmetro e então imprime na tela do número recebido até o zero.
'''- Utilize o comando int(input()) para obter o número inteiro de entrada.'''
'''- Passe o número para uma função por parâmetro.'''
'''- Mostre na tela do número recebido até o zero, usando o comando print().'''
'''- Extra: crie uma versão recursiva deste programa (Opcional)'''

numero = int(input("Digite um numero: "))

def ate_zero(numero):
    return (numero)
for numero in range(ate_zero(numero), -1, -1):
    print(numero)

#Código serve para colocar um numero em ordem decrescente

'''for num in range(n, -1, -1):
    print(num)'''