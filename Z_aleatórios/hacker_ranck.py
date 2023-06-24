# O contrutor de car deve receber dois argumentos. o primeiro deles é sua veloidade máxima, e o segundo é uma string que denota as unidades em que a velocidade é dada: "km/h" ou "mph"

# a classe deve ser implementada para retornar uma string com base nos atrgumentos. por exemplo, se car é um objeto da classe Carro com velocidade máxima de 120 e a unidade é "km/h", imprimir carro imprime a seguinte string: "Carro com velocidade máxima de 120 km/h", sem citações. Se a velocidade máxima for 94 e a unidade for "mph", a impressão do carro será impressa na seguinte string: "Carro com velocidade máxima de 94 mph", sem aspas.

# codifique em Python o resultado deste problema para a minha aula da faculdade
class Carro:
    def __init__(self, vmax, unidade):
        self.vmax = vmax
        self.unidade = unidade

    def __str__(self):
        return f"Carro com velocidade máxima de {self.vmax} {self.unidade}"

c1 = Carro(120, "km/h")
c2 = Carro(94, "mph")
print(c1)
print(c2)


# O construtor de Boat deve receber um único argumento denotando sua velocidade máxima em nós.

# A Classe deve ser implementada para  retornar uma string baseada no arguento. Por exemplo: se barco for um objeto da classe Barco com velocidade máxima de 82, a impressão de barco imprime a seguinte string: "Barco com velocidade máxima de 82 nós" sem aspas.

class Barco:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima

    def __str__(self):
        return f"Barco com velocidade máxima de {self.velocidade_maxima} nós"
b1 = Barco(82)
b2 = Barco(94)
print(b1)
print(b2)


# Letras ausentes em ordem crescente 

def caracteres_ausentes(s):
    # Definimos um conjunto com todas as letras e dígitos em minúsculo
    abc = set("abcdefghijklmnopqrstuvwxyz0123456789")
    # Removemos todas as letras e dígitos presentes na string s
    abc -= set(s)
    # Ordenamos a lista de caracteres ausentes (primeiro os dígitos, depois as letras)
    ausentes = sorted(filter(str.isdigit, abc)) + sorted(filter(str.isalpha, abc))
    # Retornamos uma nova string com os caracteres ausentes
    return "".join(ausentes)
