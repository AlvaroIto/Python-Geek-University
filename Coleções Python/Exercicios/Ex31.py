#Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a união entre os 2 vetores anterioes, ou
# seja, que contem os números dos dois vetores. Não deve conter números repetidos

vetor1 = []
vetor2 = []

for n in range(10):
    num = int(input(f'Digite o {n+1}º valor do primeiro vetor: '))
    vetor1.append(num)
for n in range(10):
    num = int(input(f'Digite o {n+1}º valor do segundo vetor: '))
    vetor2.append(num)

uniao = set(vetor1).union(set(vetor2))

print(f'Valores do vetor 1: {vetor1}\n'
      f'Valores do vetor 2: {vetor2}\n'
      f'União do vetor 1 e 2 sem repetição: {uniao}')