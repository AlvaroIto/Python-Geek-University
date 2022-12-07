#Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes e tem como saída o número de dados e a
#relação entre eles (>,<,=) de cada lançamento

from random import randint

lista_d1 = list()
lista_d2 = list()
d1 = 0
d2 = 0
igual = 0

vezes = int(input('Digite a quantidade de vezes os dados serão jogados: '))

for n in range(vezes):
    d1 = randint(1, 6)
    lista_d1.append(d1)
    d2 = randint(1, 6)
    lista_d2.append(d2)

    if d1 == d2:
        igual += 1
    elif d1 > d2:
        d1 += 1
    elif d2 > d1:
        d2 += 1

print(lista_d1)
print(lista_d2)

print(f'Das {vezes} vezes que foram jogados os 2 dados:\n'
      f'O dado 1 teve {d1} vezes valor maior\n'
      f'O dado 2 teve {d2} vezes valor maior\n'
      f'O dado 1 e dado 2 tiveram os valores iguais {igual} vezes.')