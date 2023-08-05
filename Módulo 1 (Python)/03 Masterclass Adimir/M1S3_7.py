#Crie uma função que permita contar o número de vezes que aparece uma determinada letra em uma frase. A letra desejada e a frase a ser verificada serão passadas por parâmetro para a função, que retornará a quantidade da letra na frase.

'''- Utilize o comando input() para obter a letra desejada.'''
'''- Utilize o comando input() para obter a frase desejada.'''
'''- Implemente uma função que conte a quantidade de vezes que a letra aparece na frase e retorne este valor.'''
'''- Mostre na tela o resultado obtido, usando o comando print()'''

def conta_letras(letra, frase):
    contagem = 0
#Para (for) um valor (i) na frase
    for i in frase:
#Se (if ) o valor (i) for igual a letra
        if i == letra:
#Conte de 1 em 1
            contagem += 1
#Retorne (return) a contagem
    return contagem

letra = input("Digite a letra: ")
frase = input("Digite a frase: ")
saida = conta_letras(letra, frase)
print(saida)