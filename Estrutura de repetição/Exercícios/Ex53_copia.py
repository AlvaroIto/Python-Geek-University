#Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas chamado triângulo de Floyd.
# Para n = 6 temos:
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15
#16 17 18 19 20 21

'''
num = int(input('Digite um número: '))
linha = list(range(num))

for l in linha:
    print(list(range(num)))
'''

linha = int(input('Digite o número de linhas: '))
m = 1
for c in range(1, linha + 1):
    for i in range(1, c + 1):
        print(f'{m:<4}', end='')
        m += 1
    print()