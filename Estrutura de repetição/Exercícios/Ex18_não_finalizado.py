#Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi
# lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário
'''
maior = 0
cont = 0
lista = list()
quant = int(input('Informe a quantidade de números fornecedos: '))
for n in range(quant):
    num = int(input(f'Digite o {n+1}º número: '))
    if n == 0:
        maior = n
    else:
        if num > maior:
            maior = num
            lista.append()

print(lista)
print(f'Dos {quant} números digitados o número {maior} é o maior e foi digitado {cont} vezes')
'''

i = 1
lista_num = []

qtd_num = int(input('Entre com a quantidade de números a serem lidos: '))

while i <= qtd_num:
    num = int(input(f'Digite o {i}º número: '))
    i += 1
    lista_num.append(num)

maior = max(lista_num)
print(f'O maior valor é {maior} e ele ocorre {lista_num.count(maior)} vezes')