#Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado
lista11 = list()
lista13 = list()
lista17 = list()
num = int(input('Digite um número: '))
for n in range(1, 11):
    lista11.append(n * 11)
    lista13.append(n * 13)
    lista17.append(n * 17)
print(f'Múltiplos de 11: {lista11}')
print(f'Múltiplos de 13: {lista13}')
print(f'Múltiplos de 17: {lista17}')
if num in lista11:
    print(f'Número {num} é mútiplo de 11')
elif num in lista13:
    print(f'Número {num} é mútiplo de 13')
elif num in lista17:
    print(f'Número {num} é mútiplo de 17')
else:
    print(f'Número {num} não é mútiplo de 11, 13 ou 17')
