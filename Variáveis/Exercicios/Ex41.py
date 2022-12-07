#Faça um programa que leia o valor da hora de trabalho (em reais) e o número de horas trabalhadas no mês. Imprima o
#valor a ser pago ao funcionário, adicionanado 10% sobre o valor calculado

valor_hora = float(input('Informe o valor da hora de trabaho em reais: R$'))
hora_mes = int(input('Informe o número de horas trabalhadas no mês: '))
valor = valor_hora * hora_mes
aumento = valor + (valor * 0.10)
print(f'Valor bruto: R${valor}')
print(f'Valor com 10%: R${aumento}')