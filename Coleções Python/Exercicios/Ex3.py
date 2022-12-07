#Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando
# o resultado em outro vetor. Os conjuntos tem 10 elementos cada. Imprimir todos os conjuntos
vetor_a = []
vetor_b = []

for n in range(10):
    num = float(input(f'Digite o {n+1}º valor: '))
    vetor_a.append(num)

for n in vetor_a:
    n = n ** 2
    vetor_b.append(n)

print(f'Os valores digitados são: {vetor_a}')
print(f'O quadrado dos valores digitados são: {vetor_b}')

