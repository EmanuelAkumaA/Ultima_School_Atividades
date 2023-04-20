#Crie uma função que receba duas palavras e retorne "True" caso a primeira palavra seja um prefixo da segunda, e "False" caso contrário.
#Exemplo: ’programa’ é prefixo de "programador", pois todas as letras de 'programa' correspondem às primeiras letras de "programador"

'''- Utilize o comando input() para obter a palavra1.'''
'''- Utilize o comando input() para obter a palavra2.'''
'''- Implemente uma função que identifique se a palavra1 é prefixo da palavra 2, e retorne o resultado obtido.'''
'''- Mostre na tela o resultado, usando o comando print().'''
'''- Extra: utilize slicing para indexar as strings. (Opcional).'''

def verifica_prefixo(palavra1, palavra2):
  tamanho = len(palavra1)
  for indice in range(tamanho):
    if palavra1[indice] != palavra2[indice]:
      return False
  return True

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
resultado = verifica_prefixo(palavra1, palavra2)
print(resultado)


#Variação 1 Para o resultado
'''def eh_prefixo(palavra1, palavra2):
    if palavra1 == palavra2[:len(palavra1)]:
        return True
    else:
        return False
'''

#Váriação 2

#A função "startswith() é usada para verificar se uma string começa com o prefixo especificado
'''def verifica_prefixo(palavra1, palavra2):
    if palavra2.startswith(palavra1):
        return True
    else:
        return False
palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite outra palavra: ")
resultado = verifica_prefixo(palavra1, palavra2)
print(resultado)'''