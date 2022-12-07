#Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo, nas posições pares os valores do
# primeiro e nas posições ímpares os valores do segundo

vetor_a = []
vetor_b = []
vetor_c = []

for n in range(10):
    vetor_a.append(int(input(f'Digite o {n+1}º valor: ')))
for n in range(10):
    vetor_b.append(int(input(f'Digite o {n+1}º valor: ')))
for n in range(1, 21):
    vetor_c.append(n)

for n in range(len(vetor_c)):
    if vetor_c[n] % 2 == 0:
        vetor_c[n] = vetor_a[n]
    else:
        if vetor_c[n] % 2 == 1:
            vetor_c[n] = vetor_b[n]

print(vetor_c)




