# Faça uma função que receba a data atual (dia, mes e ano em inteiro) e exiba-a na tela no formato textual por extenso
# Exemplo: Data: 01/01/2000: 1 de janeiro de 2000

def ano():
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mes: '))
    ano = int(input('Digite o ano: '))

    mes_ext = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
               'novembro', 'dezembro']

    print(f'{dia} de {mes_ext[mes-1]} de {ano}')

ano()

