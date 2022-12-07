'''

Com Map fazemos mapeamento de valores para função
Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável

Exemplo:
import math

def area(r):
    return math.pi * (r ** 2)

raios = [2, 5, 7.1, 0.3, 10, 44]
#          (funcao, iteravel)
areas = map(area, raios)
print(list(areas))
'''
