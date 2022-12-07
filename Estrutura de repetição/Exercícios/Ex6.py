#Faça um programa que leia 10 inteiros e imprima sua média

soma = 0

for n in range(1, 11):
    num = int(input(f'Digite o {n}º número: '))
    soma += num
media = soma / 10
print(f'Média dos números digitados: {media}')