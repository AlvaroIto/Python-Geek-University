# Faça um algoritmo que receba um número inteiro positivo n e calcule o seu fatorial, n!

def fatorial():
    fat = 1
    num = int(input('Digite um número: '))

    while num > 0:
        fat *= num
        num -= 1
    print(fat)


fatorial()