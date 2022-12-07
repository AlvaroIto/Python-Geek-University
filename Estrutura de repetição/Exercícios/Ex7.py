#Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
soma = 0
for n in range(1, 11):
    num = int(input('Digite um número positivo: '))
    if num < 0:
        num = 0
    else:
        soma += num
media = soma / 10
print(f'A média dos números digitados é: {media}')