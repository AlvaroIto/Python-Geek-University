#Escreva um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade. O programa
# deve calcular o valor a ser pado por aquele lanche; Considere que a cada execução somente será calculado um pedido.
# O cardápio da lanchonete segue o padrão abaixo:
'''
Especificação       Código      Preço
Cachorro quente      100        1.20
Bauru Simples        101        1.30
Bauru com Ovo        102        1.50
Hamburguer           103        1.20
Cheeseburguer        104        1.70
Suco                 105        2.20
Refrigerante         106        1.00
'''

cardapio = [('Cachorro Quente', 100, 1.20),('Bauru Simples', 101, 1.30), ('Bauru com Ovo', 102, 1.50),
            ('Hamburguer', 103, 1.20), ('Cheesebruguer', 104, 1.70), ('Suco', 105, 2.20), ('Refrigerante', 106, 1.00)]

codigo = int(input('Digite o código do produto desejado: '))
quant = int(input('Digite a quantidade: '))
if codigo == 100:
    print(f'Opção escolhida: {cardapio[0][0]}\n'
          f'Quantidade {quant}\n'
          f'Valor total: R${quant * cardapio[0][2]:.2f}')
elif codigo == 101:
    print(f'Opção escolhida: {cardapio[1][0]}\n'
          f'Quantidade {quant}\n'
          f'Valor total: R${quant * cardapio[1][2]:.2f}')
elif codigo == 102:
    print(f'Opção escolhida: {cardapio[2][0]}\n'
          f'Quantidade {quant}\n'
          f'Valor total: R${quant * cardapio[2][2]:.2f}')
elif codigo == 103:
    print(f'Opção escolhida: {cardapio[3][0]}\n'
          f'Quantidade {quant}\n'
          f'Valor total: R${quant * cardapio[3][2]:.2f}')
elif codigo == 104:
    print(f'Opção escolhida: {cardapio[4][0]}\n'
          f'Quantidade {quant}\n'
          f'Valor total: R${quant * cardapio[4][2]:.2f}')
elif codigo == 105:
    print(f'Opção escolhida: {cardapio[5][0]}\n'
          f'Quantidade {quant}\n'
          f'Valor total: R${quant * cardapio[5][2]:.2f}')
elif codigo == 106:
    print(f'Opção escolhida: {cardapio[6][0]}\n'
          f'Quantidade {quant}\n'
          f'Valor total: R${quant * cardapio[6][2]:.2f}')

