#Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário imprima o número ao quadrado

from math import sqrt
num = int(input('Digite um número: '))
if num >= 0:
    print(f'A raiz quadrada de {num} é {sqrt(num):.2f}')
else:
    print(f'O quadrado de {num} è: {num ** 2}')