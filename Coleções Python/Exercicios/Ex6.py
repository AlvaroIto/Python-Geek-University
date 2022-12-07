#Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior e o menor
# elemento do vetor
vetor = []
for n in range(10):
    num = [int(input(f'Digite o {n+1}º valor: '))]
    vetor.append(num)

print(f'Números digitados: {vetor}\n'
      f'Maior número digitado: {max(vetor)}\n'
      f'Menor número digitado: {min(vetor)}')
