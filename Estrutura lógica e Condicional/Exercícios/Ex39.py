#Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o salário atual e o
# tempo de serviço de cada funcinário. Os funcionários com menor salário terão um aumento proporcionalmente maior do
# que os funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um
# bônus adicional de salário. Faça um program que leia:
# - O valor do salário atual do funcionário;
# - O tempo de serviço desse funinário na empresa (número de anos de trabalho na empresa)
#Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final
# reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.
'''
Salário Atual       Reajuste(%)     Tempo de serviço        Bônus
Até 500,00          25%             Abaixo de 1 ano         Sem bônus
Até 1000,00         20%             De 1 a 3 anos           100,00
Até 1500,00         15%             De 4 a 6 anos           200,00
Até 2000,00         10%             De 7 a 10 anos          300,00
Acima de 2000,00    Sem reajuste    Mais de 10 anos         500,00
'''

salario = float(input('Digite o salário: R$'))
tempo = int(input('Digite o tempo de serviço(anos): '))

if salario <= 500:
    novo_salario = salario + (salario * 0.25)
elif 500 < salario <= 1000:
    novo_salario = salario + (salario * 0.2)
elif 1000 < salario <= 1500:
    novo_salario = salario + (salario * 0.15)
elif 1500 < salario <= 2000:
    novo_salario = salario + (salario * 0.1)
else:
    print(f'Salário de R${salario}. Acima de R$2000,00 Sem reajuste')
    novo_salario = salario

if tempo < 1:
    bonus = 0
    print(f'Tempo de serviço {tempo}. Menos de 1 ano. Sem bônus')
    salario_final = novo_salario
elif 1 <= tempo <= 3:
    bonus = 100
    salario_final = novo_salario +bonus
elif 4 <= tempo <= 6:
    bonus = 200
    salario_final = novo_salario +bonus
elif 7 <= tempo <= 10:
    bonus = 300
    salario_final = novo_salario +bonus
else:
    bonus = 500
    salario_final = novo_salario +bonus

print(f'Salário antigo: R${salario:.2f}\n'
      f'Reajuste: R${novo_salario:.2f}\n'
      f'Bônus: R${bonus}.\n'
      f'Salário final: R${salario_final:.2f}')
