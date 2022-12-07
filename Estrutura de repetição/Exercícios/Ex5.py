#Faça um programa que peça ao usuário para difitar 10 valores e some-os

soma = 0
for n in range(1, 11):
    num = int(input(f'Digite o {n}º número: '))
    n += 1
    soma += num

print(f'Soma total dos números digitados: {soma}')