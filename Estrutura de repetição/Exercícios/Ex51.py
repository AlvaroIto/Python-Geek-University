#Um funcionário recebe aumento anual. Em 1995 foi contradado por R$2000,00. Em 1996 recebeu aumento de 1.5%.
# A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. Faça programa que determine o salário
# atual do funcionário
ano = 1996
atual = int(input('Digite o ano atual: '))
qtd_ano = atual - ano

primeiro_aumento = 2000 * 0.015
aumento_correspondente = primeiro_aumento * 2
aumento_tot = qtd_ano + aumento_correspondente
salario_final = 2000 + aumento_tot
print(salario_final)
