#Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido

menor = 0
maior = 0

for n in range(1, 11):
    num = int(input(f'Digite o {n}º número: '))
    if n == 0:
        menor = n
        maior = n
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'O maior número digitado é {maior} e o menor é {menor}')