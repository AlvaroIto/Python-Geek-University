#Faça um programa que leia um número inteiro positivo N e imprima todos os números natruais de N até 0 em ordem descrente

while True:
    num = int(input('Digite um número positivo: '))
    if num < 0:
        print('Número precisa ser positivo.')
    else:
        break

for n in range(num, 0, -1):
    print(n)
