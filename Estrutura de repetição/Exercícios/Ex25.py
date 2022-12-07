#Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5
soma3 = 0
soma5 = 0

for n in range(1, 1001):
    soma3 += n * 3
    soma5 += n * 5
print(f'A soma dos números abaixo de 1000 multiplo de 3 é {soma3}')
print(f'A soma dos números abaixo de 1000 multiplo de 5 é {soma5}')