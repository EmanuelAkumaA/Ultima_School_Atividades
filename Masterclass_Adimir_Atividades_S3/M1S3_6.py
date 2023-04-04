#Escreva uma função que, dado o valor da conta de um restaurante e um percentual de taxa de serviço, calcule e exiba a gorjeta do garçom, considerando o percentual do valor da conta.
'''- Utilize o comando float(input()) para obter o valor da conta.'''
'''- Utilize o comando int(input()) para obter o valor da taxa de serviço.'''
'''- Implemente uma função que calcule a gorjeta do garçon, baseado no percentual do valor da conta definido.'''
'''- Mostre na tela o resultado com duas casas decimais, usando o comando print(f"{resultado:.2f}").'''
'''- Lembrando que o cálculo de porcentagem é: valor*porcentagem/100.'''

def gorjeta(valor, porcentagem):
    return (valor * porcentagem/100)
valor_da_conta = float(input("Digite o valor da sua conta: "))
porcentagem = int(input("Digite a taxa: "))
resultado = gorjeta(valor_da_conta, porcentagem)
print(f"A gorjeta do garçom é R$!: {resultado:.2f}")