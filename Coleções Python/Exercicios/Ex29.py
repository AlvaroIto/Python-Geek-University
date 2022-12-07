#Faça um programa que receba 6 núemros inteiros e mostre:
#- Os números pares digitados
#- A soma dos números pares digitados
#- Os números impares digitados
#- A quantidade de números ímpares digitados

vetor = []
vetor_par = []
soma_par = 0
vetor_impar = []

for n in range(6):
    num = int(input(f'Digite o {n+1}º valor: '))
    vetor.append(num)
    if num % 2 == 0:
        vetor_par.append(num)
        soma_par += num
    else:
        vetor_impar.append(num)

print(f'Números digitados: {vetor}')
print(f'Números pares digitados: {vetor_par}')
print(f'Soma dos números pares: {soma_par} ')
print(f'Números ímpares digitados: {vetor_impar}')
print(f'Foram digitados {len(vetor_impar)} números ímpares')