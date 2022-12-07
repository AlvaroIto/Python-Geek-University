# Escreva uma função para determianr a quantidade de números primos abaixo N.

def num_primo():
'''
    div = 0
    num = int(input('Digite um número: '))
    if num > 1:
        for n in range(2, num):
            if num % n == 0:
                div += 1
        if div == 0:
            print(f'O número {num} é primo')
        else:
            print(f'O número {num} não é primo')
    elif num == 2:
        print(f'O número {num} é primo')
    elif num == 1:
        print(f'O número {num} não é primo')
    elif num == 0:
        print(f'Você digitou o {num}')
    else:
        print(f'O número {num} é negativo')

'''
cont = 2
div = 0
num = int(input('Digite um número: '))

while cont <  num:
    if num > 1:
        if num % cont == 0:
            div += 1
        if div == 0:
            print(f'O número {num} é primo')
        else:
            print(f'O número {num} não é primo')




num_primo()