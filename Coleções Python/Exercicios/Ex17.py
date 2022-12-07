#Leia um vetor de 10 posições e atribua o valor 0 para todos os elementos que possuírem valores negativos
vetor = []
for n in range(10):
    num = int(input(f'Digite o {n+1}º valor: '))
    if num < 0:
        num = 0
        vetor.append(num)
    else:
        vetor.append(num)
print(vetor)
