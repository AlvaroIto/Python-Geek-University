#Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais

num = 0
soma = 0
while num <= 0:
    num = int(input('Digite um número positivo: '))
    for n in range(0, num):
        soma += n

print(soma)



