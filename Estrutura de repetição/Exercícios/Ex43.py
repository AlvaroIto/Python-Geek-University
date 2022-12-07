#Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for informada a idade 0), e
#calcule a idade média desse grupo

soma = 0
cont = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade > 0:
        soma += idade
        cont += 1
    else:
        media = soma / cont
        print(f'A média de idade do grupo é {media:.2f}')
        break
