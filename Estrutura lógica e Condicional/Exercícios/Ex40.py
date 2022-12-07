#O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos.
#A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. LEia o custo de
#fábrica e escreva o custo ao consumidor.
'''
Custo de fábrica                   % do distribuidor           % dos impostos
até R$12.000,00                             5                       isento
entre R$12.000,00 a 25.000,00               10                      15
acima de R$25.000,00                        15                      20
'''
custo_fabrica = float(input('Digite o custo de fábrica do carro: R$'))
if custo_fabrica <= 12000:
    comissao = custo_fabrica * 0.05
    imposto = 0
elif 12000 < custo_fabrica <= 25000:
    comissao = custo_fabrica * 0.1
    imposto = custo_fabrica * 0.15
elif custo_fabrica > 25000:
    comissao = custo_fabrica * 0.15
    imposto = custo_fabrica * 0.20

print(f'Valor custo fábrica: R${custo_fabrica:.2f}\n'
      f'Comissão do distribuidor: R${comissao:.2f}\n'
      f'Imposto: R${imposto:.2f}\n'
      f'Valor total R${custo_fabrica + imposto:.2f}')

