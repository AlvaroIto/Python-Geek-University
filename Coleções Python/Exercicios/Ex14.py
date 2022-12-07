#Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela
from collections import Counter

vetor = []

for n in range(10):
    num = int(input(f'Digite o {n+1}º valor: '))
    vetor.append(num)


contador = Counter(vetor)
print(contador)