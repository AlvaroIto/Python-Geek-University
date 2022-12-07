#Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamento com o maior, o menor e a
# média dos valores
vetor = []
for n in range(5):
    num = int(input(f'Digite o {n+1}º valor: '))
    vetor.append(num)
print(f'Valores digitados: {vetor}\n'
      f'Maior valor digitado: {max(vetor)}\n'
      f'Menor valor digitado: {min(vetor)}')

