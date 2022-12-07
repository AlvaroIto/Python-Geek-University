#Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for
#negativo, mostre uma mensagem dizendo que o número é inválido

from math import sqrt

while True:
    num = int(input('Digite um número positivo: '))
    if num >= 0:
        print(f'A raiz quadrada do número {num} é {sqrt(num):.2f}')
        break
    else:
        print(f'Número inválido!')