#Leia um número positivo do usuário, então, calcule e imprima a sequência de Fibonacci até o primeiro número superior ao
#número lido. Exempo: se o usuário informou o número 30, a sequência a ser impressa será 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

t1 = 0
t2 = 1
n = int(input('Digite um número: '))
print(f'{t1}, {t2}', end='')

while t2 <= n:
    t3 = t1 + t2
    print(f', {t3}', end='')
    t1 = t2
    t2 = t3


