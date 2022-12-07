#Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# - O número digitado ao quadrado
# - A raiz quadrada do número digitado

from math import sqrt
while True:
    num = int(input('Digite um número positivo: '))
    if num >= 0:
        print(f'O quadrado de {num} é: {num ** 2}')
        print(f'A raiz quadrada de {num} é: {sqrt(num):.2f}')
        break
    else:
        print('Número inválido!!!!')