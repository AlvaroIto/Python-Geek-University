#Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo
# encanador e imprima a quantida líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda

valor_dia = 30
dia_trabalhado = int(input('Digite a quantidade de dias trabalhados: '))
tot_bruto = dia_trabalhado * valor_dia
tot_liq = tot_bruto - (tot_bruto * 0.08)
print(f'Dias trabalhados: {dia_trabalhado}')
print(f'Valor total bruto: R${tot_bruto}')
print(f'Valor total com desconto de 8%: R${tot_liq}')
