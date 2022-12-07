#Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou 5, mas não simultaneamente.

num = int(input('Digite um número: '))

if num % 3 == 0 and num % 5 == 0:
    print(f'Número {num} divisível por 3 e 5')
elif num % 3 == 0 and not num % 5 == 0:
    print(f'Número {num} divisível por 3')
elif num % 5 == 0 and not num % 3 == 0:
    print(f'Número {num} divisível por 5')
else:
    print(f'Número não é divisível por 3, 5 ou por ambos')