#Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este
#número. Isto é, domingo se 1, segunda-feira se 2 e assim por diante

dia = int(input('Digite um número de 1 a 7: '))
semana = ('domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado')
print(semana[dia-1])

