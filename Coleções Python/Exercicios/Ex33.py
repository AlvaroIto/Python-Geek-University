#Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com valor 0. para isso,
# todos os elementos a frente do valor zero, devem ser movidos uma posição apra trás no vetor

vetor = []

for n in range(15):
    num = int(input(f'Digite o {n+1}º valor do vetor: '))
    if num != 0:
        vetor.append(num)

print(vetor)
