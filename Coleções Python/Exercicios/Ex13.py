#Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o menor valor
vetor = []
for n in range(5):
    num = int(input(f'Digite o {n+1}º valor: '))
    vetor.append(num)
print(f'Valores digitados: {vetor}\n'
      f'Maior valor digitado na posição: {vetor.index(max(vetor))}\n'
      f'Menor valor digitado na posição: {vetor.index(min(vetor))}')
print(f'O maior valor digitado é: {i}')