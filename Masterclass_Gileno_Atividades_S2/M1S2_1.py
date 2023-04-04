#O caixa no bar do Sr. João está cheio de diversas moedas. O Sr. João precisa fechar o caixa, mas está com dificuldade de fazer os cálculos do tanto de dinheiro que ele possui em moedas. O caixa no bar do Sr. João está cheio de diversas moedas. O Sr. João precisa fechar o caixa, mas está com dificuldade de fazer os cálculos do tanto de dinheiro que ele possui em moedas. Enquanto estava organizando, ele conseguiu separar as moedas e contar a quantidade.

'''Moeda	Quantidade
5 centavos	35
10 centavos	50
25 centavos	30
50 centavos	15
1 real	19 '''

'''Crie uma aplicação que calcule o valor total que o Sr. João possui em moedas de real (R$) no caixa. '''
'''A aplicação deve imprimir o valor total em reais (R$) e pode-se utilizar ponto flutuante para representar o valor com duas casas decimais no momento que for imprimir o valor na tela.'''

#Umaidéia de código interativo para contar moedas.
moeda = float(input("Digite o valor da moeda: "))
quantidade = int(input("Digite a quantidade de moedas: "))

total_5_centavos = moeda * quantidade
total_10_centavos = moeda * quantidade
total_25_centavos = moeda * quantidade
total_50_centavos = moeda * quantidade
total_1_real = moeda * quantidade

print(total_5_centavos )

#Codigo simples e pronto

total_5_centavos = 35 * 0.05
total_10_centavos = 50 * 0.10
total_25_centavos = 30 * 0.25
total_50_centavos = 15 * 0.50
total_1_real = 19 * 1

total_caixa = (
    total_5_centavos + total_10_centavos + total_25_centavos + total_50_centavos + total_1_real
)

print(total_caixa)