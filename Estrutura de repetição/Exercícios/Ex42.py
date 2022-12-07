#Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores
# lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero
from math import sqrt
while True:
    num = int(input('Digite um número: '))
    if num <= 0:
        print('FIM')
        break
    else:
        quadrado = num ** 2
        cubo = num ** 3
        print(f'Número digitado: {num}\n'
              f'{num}² = {quadrado}\n'
              f'{num}³ = {cubo}\n'
              f'Raiz quadrada de {num} = {sqrt(num):.2f}')

