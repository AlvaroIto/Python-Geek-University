#Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada. Crie um novo vetor denominado
# C calculando C =A - B, Mostre na tela os dados do vetor C

vetor_a = []
vetor_b = []
vetor_c = []

for n in range(10):
    num_a = int(input(f'Digite o {n+1}º valor do vetor A: '))
    vetor_a.append(num_a)
for n in range(10):
    num_b = int(input(f'Digite o {n+1}º valor do vetor B: '))
    vetor_b.append(num_b)

for n in range(10):
    vetor_c.append(vetor_a[n] - vetor_b[n])

print(f'{vetor_a} - {vetor_b} = {vetor_c}')
