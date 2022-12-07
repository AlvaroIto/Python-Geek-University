#Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa
vetor = []
for n in range(6):
    num = int(input(f'Digite o {n+1}º valor: '))
    vetor.append(num)

print(f'Valores digitados: {vetor}')
vetor.reverse()
print(f'Valores digitados na ordem inversa: {vetor}')
