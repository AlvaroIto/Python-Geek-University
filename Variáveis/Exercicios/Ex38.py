#Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%

salario = float(input('Informe o salário: R$'))
aumento = salario + (salario * 0.25)
print(f'Salário antigo: R${salario}')
print(f'Salário com aumento de 25%: R${aumento}')