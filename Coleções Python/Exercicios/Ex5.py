#Leia um vetor de 10 posições, Contar e escrever quantos valores pares ele possui
vetor = []
vetor_par = []
for n in range(10):
    num = int(input(f'Digite o {n+1}º valor: '))
    vetor.append(num)
    if num % 2 == 0:
        vetor_par.append(num)

print(f'Valores digitados do vetor: {vetor}\n'
      f'Valores pares digitados do vetor: {vetor_par}\n'
      f'{len(vetor_par)} valores pares digitados')