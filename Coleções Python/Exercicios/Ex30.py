#Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção entre os 2 vetores
# anteriores, ou seja, que contém apenas os números que estão em ambos os vetores. Não deve conter números repetitivos

from collections import Counter

vetor1 = []
vetor2 = []


for n in range(10):
    num = int(input(f'Digite o {n+1}º valor do primeiro vetor: '))
    vetor1.append(num)

for n in range(10):
    num = int(input(f'Digite o {n+1}º valor do primeiro vetor: '))
    vetor2.append(num)

interseccao = set(vetor1).intersection(set(vetor2))
print(f'Valores do primeiro vetor: {vetor1}\n'
      f'Valores do segundo vetor: {vetor2}\n'
      f'Intersecção do primeiro e segundo vetor tirando repetidos: {interseccao}')