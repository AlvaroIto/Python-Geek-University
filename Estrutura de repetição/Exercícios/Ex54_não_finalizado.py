#Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é primo ou não
num = int(input('Digite um número: '))
#for n in range(1, (num + 1)):
if num % num == 0:
    print(f'O número {num} é primo')
else:
    print(f'Não é primo')