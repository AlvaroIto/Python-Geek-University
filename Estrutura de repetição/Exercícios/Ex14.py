#Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
# decrescente

num = int(input('Digite um número inteiro positivo par: '))
if num % 2 == 0:
    for n in range(num, 0, -1):
        if n % 2 == 0:
            print(n)
else:
    print('Número precisa ser par e positivo')



