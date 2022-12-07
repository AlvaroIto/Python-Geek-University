#Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre qual
#calssificação dessa pessoa
'''
altura                                  peso
                    Ate 60      Entre 60 e 60       Acima de 90
menor que 1,20        A             D                   G
de 1,20 a 1,70        B             E                   H
maior que 1,70        C             F                   I
'''

alt = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))

if alt < 1.20:
    if peso < 60:
        print('Categoria A')
    elif 60 <= peso <= 90:
        print('Categoria D')
    elif peso > 90:
        print('Categoria G')

if 1.20 <= alt <= 1.70:
    if peso < 60:
        print('Categoria B')
    elif 60 <= peso <= 90:
        print('Categoria E')
    elif peso > 90:
        print('Categoria H')

if alt > 1.70:
    if peso < 60:
        print('Categoria C')
    if 60 <= peso <= 90:
        print('Categoria F')
    if peso > 90:
        print('Categoria I')