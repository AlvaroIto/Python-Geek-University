#Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = raiz a²  b². Faça um
#programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação. Imprima o resultado

from math import sqrt

a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
hip = sqrt((a ** 2) + (b ** 2))
print(f'A hipotenusa do triângulo é: {hip:.2f}')