#Leia 10 núemros inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2. Copie os valores ímpares de v para
# v1, e os valores pares de v para v2. Note que cada um dos vetores v1 e v2 tem no maximo 10 elementos, mas nem todos os
# elmentos são utilizados. No final escreva os elementos UTILIZADOS de v1 e v2

vetor = []
vetor1 = []
vetor2 = []
for n in range(10):
    num = int(input(f'Digite o {n+1}º valor: '))
    vetor.append(num)
    if num % 2 == 0:
        vetor2.append(num)
    else:
        vetor1.append(num)
print(f'Valores digitados: {vetor}')
print(f'Valores ímpares digitados: {vetor1}')
print(f'Valores pares digitados: {vetor2}')