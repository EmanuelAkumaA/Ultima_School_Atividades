# Para a atividade dessa semana, vamos trabalhar com a seguinte situação:

# Uma pessoa do seu time de desenvolvimento está escrevendo várias funções que calculam diferentes formas de gerar juros. 
# Veja abaixo o exemplo de uma das funções:

# Ela pediu para você escrever um decorator chamado decorator_imprimir, que será usado para a função chamada 
# imprima os parâmetros: capital, taxa e tempo, além do resultado da função.
# Ao executar a função juros_simples, teríamos o seguinte resultado:

# CAPITAL: 1000.0, TAXA: 6.0, TEMPO: 10.0, RESULTADO: 600.0


def decorator_imprimir(funcao):
    def mostrar_na_tela(*args, **kwargs):
        capital, taxa, tempo = args
        resultado = funcao(*args, **kwargs)
        return print(f'capital: {capital}, taxa: {taxa}, tempo: {tempo}, resultado: {resultado}')
    return mostrar_na_tela



@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

capital = 1000.0
taxa = 6.0
tempo = 10.0

juros_simples(capital, taxa, tempo)