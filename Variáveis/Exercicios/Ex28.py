#Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))

res = (n1 ** 2) + (n2 ** 2) + (n3 ** 2)
print(f'A soma dos quadrados dos 3 valores digitados é: {res}')