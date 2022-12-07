#Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, Mês e Ano. Teste a validade
# desta data para saber se esta é uma data válida. Teste se o dia fornecido é um dia válido: Dia > 0, dia <=28 para o
#mes de fevereiro (29 se o ano for bissexto), dia <= 30 em abril, junho setembro e novembro, dia <= 31 nos outros meses
#Teste a validade do mes: mes > 0 e mes < 13. Teste a validade do ano: ano <= ano atual (use uma constante definida com
#o valor igual a 2022. Imprimir: 'data válida' ou 'data inválida' no final da execução do programa.

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))

if mes in (1, 3, 5, 7, 8, 10, 12):
    if dia > 31:
        print(f'Mês {mes} não tem mais do que 31 dias')
    else:
        print(f'Data:{dia}/{mes}/{ano}')
elif mes in (2, 4, 6, 9, 11):
    if mes == 2:
        if ano % 400 == 0 or ano % 4 == 0 and not ano % 100 == 0:
            if dia > 29:
                print('Fevereiro não tem mais do que 29 dias')
            else:
                print(f'Data:{dia}/{mes}/{ano}')
        else:
            if dia > 28:
                print('Fevereiro não tem mais do que 28 dias')
            else:
                print(f'Data:{dia}/{mes}/{ano}')
    else:
        if dia > 30:
            print(f'Mês {mes} não tem mais do que 30 dias')
        else:
            print(f'Data:{dia}/{mes}/{ano}')
else:
    print(f'Mês {mes} inexistente')