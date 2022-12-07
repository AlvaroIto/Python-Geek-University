#Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar qual o número foi gerado, a
# cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. O programa acaba quando o
# usuário acertar o número gerado. O programa deve informar em quantas tentativas o número foi descoberto

from random import randint

print('Gerando um número de 1 a 1000...')
pc = randint(1, 1000)
cont = 0

while True:
    num = int(input('Tente acertar o número gerado: '))

    if num != pc:
        if num > pc:
            print(f'ERROU, o número {num} é MAIOR que o número gerado. Tente novamente')
            cont += 1
        elif num < pc:
            print(f'ERROU, o número {num} é MENOR que o número gerado. Tente novamente')
            cont += 1
    else:
        cont += 1
        print(f'ACERTOU!!!, Chute: {num}, Gerado: {pc}. Você acertou na {cont}ª tentativa')
        break
