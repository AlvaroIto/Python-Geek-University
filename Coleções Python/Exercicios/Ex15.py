#Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetitivos
vetor = []
unicos = []

for n in range(20):
    num = int(input(f'Digite o {n+1}º número: '))
    vetor.append(num)

for n in vetor:
    if n not in unicos:
        unicos.append(n)

print(f'Vetor dos números digitados sem repetição: {unicos}')

