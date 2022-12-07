#Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário
#imprima: Empréstimo negado, caso contrário imprima: Empréstimo aprovado

salario = float(input('Digite o salário: R$'))
prestacao = float(input('Digite o valor da prestação do emprestimo: R$'))
limite = salario * 20 / 100
if prestacao > limite:
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado')