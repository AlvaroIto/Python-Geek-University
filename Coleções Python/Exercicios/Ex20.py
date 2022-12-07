#Escreva um programa que leia números inteiros no intervalor [0,50] e os armazene em um vetor com 10 posições. Preencha
# um segundo vetor apenas com os números ímpares do primeiro vetor. Imprima os dois vetors, 2 elementos por linha
vetor = []
vetor_impar = []
linhas  = range(10)
for n in range(10):
    num = int(input('Digite um número de entre 0 e 50: '))
    vetor.append(num)
    if num % 2 == 1:
        vetor_impar.append(num)


print(vetor[0], vetor[1])
print(vetor[2], vetor[3])
print(vetor[4], vetor[5])
print(vetor[6], vetor[7])
print(vetor[8], vetor[9])
