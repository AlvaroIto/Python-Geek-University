#Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N em ordem
# crescente
num = int(input('Digite um número positivo ímpar: '))
if num % 2 == 1:
    print(f'Os números ímpares de 0 até {num} são:')
    for n in range(num):
        if n % 2 == 1:
            print(n)
