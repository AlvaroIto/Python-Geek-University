#O funcionário chamado Carlos tem um colega chamado joão que recebe um salário que equivale a um terço do seu salário.
# Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente no fundo de renda
# fixa, que está rendendendo 5% ao mês. Construa um programa qu deverá calcular e mostrar a quantindade de meses
# necessários para que o valor pertecente a João iguale ou ultrapasse o valor pertecente a Carlos.
# Teste com outros valores para as taxas;
sal_carlos = float(input('Digite o salário de Carlos: R$'))
sal_joao = sal_carlos * 0.333
renda = sal_joao + (sal_joao * 0.05)
meses = 0
renda_tot = 0
while renda_tot <= sal_carlos:
    renda_tot += renda
    meses += 1

print(f'Salário Carlos: R${sal_carlos:.2f}\n'
      f'Salário João: R${sal_joao:.2f}\n'
      f'Renda de 5% baseado no valor de R${sal_joao:.2f}: R${renda:.2f}\n'
      f'Renda Total: {renda_tot:.2f}\n'
      f'Quantidaes de meses para igualar ou ultrapassar o salário de Carlos: {meses}')

