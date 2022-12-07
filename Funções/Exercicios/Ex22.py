# Cria uma função que receba como parâmetro um valor inteiro e gere como saída n linhas com pontos de exclamação,
# conforme o exemplo abaixo (para n = 5):
'''
!
!!
!!!
!!!!
!!!!!
'''


def exclamação():
    num = int(input('Digite um número: '))
    for n in range(num+1):
        print('!' * n)


exclamação()