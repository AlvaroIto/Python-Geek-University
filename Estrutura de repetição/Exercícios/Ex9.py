#Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares:
num = int(input('Digite um número: '))
print(f'Os primeiros {num} números ímpares são:')
for n in range(0, num):
    if n % 2 == 1:
        print(n)
