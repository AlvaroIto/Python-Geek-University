# Crie um programa que receba três valores (obrigatoriamente maiores que zero), representando as medidas dos três lados
# de um triângulo. Elabores funções para:
# a- Determinar se esses lados formam um triângulo. sabendo que:
# - O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados
# b- Determianr e mostrar o tipo de triângulo, caso as medidas formem um triângulo. Sendo que:
# - Chama-se equiçátero o triângulo que tem três lados iguais
# - Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais
# - Recebe o nome de escaleno o triângulo que tem os três lados diferentes


l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))

if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print('Triângulo')
    if l1 == l2 and l2 == l3:
        print('O triângulo é equilátero!')
    elif l1 != l2 != l3 != l1:
        print('O triângulo é escaleno!')
    else:
        print('O triângulo é isósceles')
else:
    print('Não pode se formar um triângulo')

