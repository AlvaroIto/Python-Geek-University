#Faça um programa para calcular as seguintes sequencias:
#1 + 2 + 3 + 4 + 5 + ... + n
#1 - 2 + 3 + 4 + 5 + ... + (2n - 1)
#1 + 3 + 5 + 7 + ... + (2n - 1)

lista1 = list()
lista3 = list()

num = int(input('Digite um número: '))

for n in range(1, num+1):
    print(n)
    lista1.append(n)
    seq1 = sum(lista1)


print(lista1)
print(seq1)

for n in range(1, num+1):
    if n % 2 != 0:
        lista3.append(n)
        seq3 = sum(lista3)

print(lista3)
print(seq3)

