#Elabore um programa que faça a leitura de vários números inteiros, até que se digite um número negativo. O programa tem
# que retornar o maior e o menor número lido

maior = 0

while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    else:
        if num > maior:
            maior = num
print(f'O maior número digitado foi {maior}')