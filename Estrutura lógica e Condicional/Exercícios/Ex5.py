#Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar

num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'O número {num} é Par')
else:
    print(f'O número {num} é Ímpar')