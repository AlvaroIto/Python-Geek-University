#Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a
#posição que ele se encontra

vetor = []
for n in range(10):
    num = int(input(f'Digite o {n+1}º valor: '))
    vetor.append(num)
print(f'Valores digitados: {vetor}\n'
      f'Maior valor digitado: {max(vetor)}\n'
      f'Posição do maior valor digitado: {vetor.index(max(vetor))}')