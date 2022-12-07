#Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos

tempo = int(input('Digite o valor em segundos: '))
hora = tempo / 3600
minuto = tempo / 60
segundo = tempo

print(f'{tempo} = {hora:.2f} horas')
print(f'{tempo} = {minuto:.2f} minutos')
print(f'{tempo} = {segundo} segundos')
