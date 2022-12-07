# Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida  pela equação: hip = raiz a² + b². Faça uma função
# que receba os valores de a e b e calcule o valor da hipotenusa através da equação
from math import sqrt

def hipotenusa():
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))
    hip = sqrt(((a ** 2) + (b ** 2)))
    print(f'Dados os catetos a:{a} e b:{b}, o valor da hipotenusa é: {hip:.2f}')

hipotenusa()