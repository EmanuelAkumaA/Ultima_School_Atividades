
#1. Crie uma função que, ao receber um número inteiro, retorna se um número é par ou ímpar.
'''- Utilize o comando int(input()) para obter o número inteiro de entrada.'''
'''- Passe o número para uma função por parâmetro.'''
'''#- Calcule e retorne o resultado.'''
'''#- Mostre na tela se o número é 'Par' ou 'Impar', usando o comando print()'''

#Essa é a que eu desenvolvi para saber se a soma de dois numeros é par ou impar
'''IDÉIA: colocar a opção onde dê para o usuário escolher qual operação aritimética ele quer realizar com
os dois numeros, antes de dizer se o resultado é par.'''

a = int(input("Digite um numero: "))
b = int(input("Digite outo numero: "))

def soma(n1, n2):  
    return a + b
saida = soma(a, b)
print("Resultado é: ",saida)
print("Então")
if saida % 2 == 0:
    print(f'O numero: {saida} é par!')
else:
    print(f'O numero: {saida} é impar!')



#Foi usada para a atividade 1 da plataforma. Funciona para saber se um unico numero é par ou impar.

'''numero = int(input())
def par_impar(numero):
    return numero
if par_impar(numero) % 2 == 0:
    print("Par")
else:
    print("Impar")'''