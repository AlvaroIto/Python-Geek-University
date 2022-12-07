#Faça um programa que receba dois números. Calcule e mostre:
# - a soma dos números pares desse intervalor de números, incluindo os números digitados;
# - A multiplicação dos números ímpares desse intervalor, incluindo os digitados;

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = 0
mult = 1

if n1 > n2:
    for n in range(n2, n1+1):
        print(n)
        soma += n
        mult *=n

elif n1 < n2:
    for n in range(n1, n2+1):
        print(n)
        soma += n
        mult *= n

else:
    print('Os 2 números são iguais')

print(f'A soma entre os números digitados é: {soma}')
print(f'A multiplicação entre os números digitados é: {mult}')