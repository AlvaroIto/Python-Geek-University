#Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer correspondente
#a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições
# X e Y

vetor = []
x = []
y = []
for n in range(8):
    num = int(input(f'Digite o {n+1}º valor: '))
    vetor.append(num)
while True:
    num = int(input('Digite a primeira posição: '))
    if num <= 0 or num > 8:
        print('Posição inválida, digite novamente')
    else:
        x.append(num)
        break

while True:
    num = int(input('Digite a segunda posição: '))
    if num <= 0 or num > 8:
        print('Posição inválida, digite novamente')
    else:
        y.append(num)
        break

soma = vetor[x[0]] + vetor[y[0]]
print(f'A soma dos números: {vetor[x[0]]} + {vetor[y[0]]} = {soma}')
