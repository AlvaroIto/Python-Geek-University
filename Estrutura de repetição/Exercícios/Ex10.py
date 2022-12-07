#Faça um programa que calcule e mostre a soma dos 50 primeiros números pares
soma = 0
for n in range(0, 51):
    if n % 2 == 0:
        print(n)
        soma += n
print(soma)