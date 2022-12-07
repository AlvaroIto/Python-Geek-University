#Faça um algorítmo que leia um número positivo e imprima seus divisores

num = int(input('Digite um número: '))
div = list()
for n in range(1, num):
    if num % n == 0:
        div.append(n)
print(f'Os divisores do número {num} são {div}')