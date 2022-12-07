#Receba o salário-base de um funcionário; Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma
#gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base

salario = float(input('Informe o salário base: R$'))
grat = salario + (salario * 0.05)
imp = salario * 0.07
salario_real = grat - imp
print(f'Salário base: R${salario}')
print(f'Gratificação de 5%: R${grat}')
print(f'Salário real (R${grat} - R${imp}) = R${salario_real}')