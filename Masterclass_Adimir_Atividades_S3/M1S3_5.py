#5. Faça um programa com uma função que necessite de um parâmetro. A função deve retornar "Positivo",
#se seu o número for maior que zero, "Negativo" se o número for menor que zero, e "Zero" se o número for
#igual a zero.

'''- Utilize o comando int(input()) para obter o número inteiro de entrada.'''
'''- Implemente uma função que seja capaz de descobrir se um número é positivo, negativo ou zero, e retorne o resultado'''
'''- Mostre na tela o resultado, usando o comando print().'''


#Protótipo
'''def origem_num(numero):
    return numero
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
elif num == 0:
    print("Zero")'''


#Função definitiva

def origem_do_numero(numero):
  if numero == 0:
    return "Zero"
  elif numero > 0:
    return "Positivo"
  else:
    return "Negativo"

numero = int(input("Digite o numero: "))
print(origem_do_numero(numero))