#Faça um programa que receba dois números e mostre qual deles é o maior

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O {n1} é maior q o {n2}')
elif n1 < n2:
    print(f'O {n2} é maior que o {n1}')
else:
    print(f'O {n1} e {n2} são iguais!')