#Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este número.
#Isto é janeiro se 1, fevereiro se 2, e assim por diante

num = int(input('Digite um número de 1 a 12: '))
mes = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
       'Dezembro')

print(mes[num-1])