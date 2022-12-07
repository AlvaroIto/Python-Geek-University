#Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês
#Note que Fevereiro tem 29 dias em anos bissextos e 28 dias em anos não bissextos

dia = int(input('Digite o dia(1-31): '))
mes = int(input('Digite o mes(1-12): '))
ano = int(input('Digite o ano(xxxx): '))

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

