#Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os múltiplos de um número inteiro x num vetor
# e mostre-os na tela

vetor = []
for n in range(10):
    num = int(input(f'Digite o {n+1}º valor: '))
    vetor.append(num)

multiplo = int(input('Digite um número: '))
for n in vetor:
    print(f'{multiplo} x {n} = {multiplo * n}')