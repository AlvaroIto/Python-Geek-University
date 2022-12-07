#Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido" Se o número for positivo
# calcular o logaritmo deste número

from math import log
num = int(input('Digite um número: '))
if num > 0:
    print(log(num))
else:
    print('Número inválido!')