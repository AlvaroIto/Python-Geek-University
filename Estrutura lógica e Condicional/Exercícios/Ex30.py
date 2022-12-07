#Faça um programa que receba três números e mostre-os em ordem crescente

ordem = list()
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

ordem.append(n1)
ordem.append(n2)
ordem.append(n3)
print(sorted(ordem))
