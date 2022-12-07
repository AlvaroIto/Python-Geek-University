#Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um
#triângulo escaleno, equilátero, ou isócele, considerando os seguintes conceitos:
# - O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados
# - Chama-se equilátero o triângulo que tem três lados iguais
# - Denominam-se isóceles o triângulo que tem  comprimento de dois lados iguais
# - Recebe o nome de escaleno o triângulo que tem os  três lados diferentes

l1 = float(input('Digite o primeiro ladp do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('Não é possível formar um triângulo!')
else:
    if l1 == l2 and l2 == l3 and l3 == l1:
        print('Triângulo Equilátero')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isóceles')

