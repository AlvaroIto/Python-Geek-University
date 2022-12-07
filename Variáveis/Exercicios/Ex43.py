#Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# - O total a pagar com desconto de 10%
# - O valor de cada parcela, no parcelmaneot de 3x sem juros
# - A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
# - A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

valor = float(input('Digite o valor: R$'))
desconto10 = valor - (valor * 0.10)
parcela3 = valor / 3
comissao_vista = desconto10 * 0.05
comissao_parcela = valor * 0.05
print(f'Valor real: R${valor}')
print(f'Valor com 10% de desconto: R${desconto10}')
print(f'Comissão do vendedor a vista: R${comissao_vista}')
print(f'Comissão do vendedor parcelado: R${comissao_parcela}')

