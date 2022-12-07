#Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos valores não ultrapassem quatro
# milhões

t1 = 0
t2 = 1
cont = 3
soma = 0
while True:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'número:{t3}')
    if t3 % 2 == 0:
        soma += t3
        if soma > 1000:
            print(f'soma:{soma}')
            break


