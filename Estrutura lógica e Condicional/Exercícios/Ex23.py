#Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se for
#divisível por 4 e não for por 100.

ano = int(input('Digite o ano: '))
if ano % 400 == 0:
    print(f'Ano {ano} é bissexto')
elif ano % 4 == 0 and not ano % 100 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'Ano {ano} não é bissexto')