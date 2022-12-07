#Faça um programa que leia o valor de um produto e imprima o valor com descconto, tendo em vista que o desconto foi de
# 12%

valor = float(input('Digite o valor do produto: R$'))
desconto = valor - (valor * 0.12)
print(f'Valor do produto: R${valor}')
print(f'Desconto de 12%: R${desconto}')
