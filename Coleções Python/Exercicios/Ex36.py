#Leia um vetor com 10 números reais, ordene os elementos deste vetor, e no final escreva os elementos do vetor ordenado
vetor = []

for n in range(10):
    num = int(input(f'Digite o {n+1}º valor do vetor: '))
    vetor.append(num)

ordem = sorted(vetor)

print(f'Números digitados do vetor: {vetor}')
print(f'Números do vetor em ordem crescente: {ordem}')