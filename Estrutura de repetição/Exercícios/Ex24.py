#Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele
#próprio. Ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 87

num = int(input('Digite um número: '))
div = list()
for n in range(1, num):
    if num % n == 0:
        div.append(n)
print(f'Os divisores do número {num} são {div}')
print(f'A soma dos seus divisores é {sum(div)}')