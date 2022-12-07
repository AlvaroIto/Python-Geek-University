#Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem
# crescente

while True:
    num = int(input('Digite um número positivo: '))
    if num < 0:
        print('Número precisa ser positivo.')
    else:
        break

for n in range(0, num+1):
    print(n)
