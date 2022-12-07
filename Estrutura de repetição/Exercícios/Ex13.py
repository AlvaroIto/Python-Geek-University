#Façã um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
# crescente

num = int(input('Digite um número positivo par: '))
if num % 2 == 0:
    print(f'Os números pares de 0 até {num} são:')
    for n in range(num):
        if n % 2 == 0:
            print(n)

