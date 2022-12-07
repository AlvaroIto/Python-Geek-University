#Faça um programa para ler o horário (hora, minuto e segundo) de inicio e a duração, em segundos, de uma experiência
#biológica. O programa deve resultar com o novo horário (hora, minuto e segundos) do término da mesma
soma = 0

print('=' * 50)
print('Informe a hora de inicio do experimento')
hora = int(input('Digite a hora: '))
minuto = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))
print(f'INÍCIO: {hora}:{minuto}:{segundos}')
print('=' * 50)
duracao = int(input('Digite a duração do experimento em segundos: '))

tempo_seg = (hora * 3600) + (minuto * 60) + segundos
print(tempo_seg)
tempo_dur = tempo_seg + duracao
print(tempo_dur)

nova_hora == tempo_dur // 3600







'''
if duracao < 60:
    segundos += duracao
    print(segundos)
    if segundos >= 60:
        soma = segundos - 60
        minuto += soma
        print(minuto)
        print(segundos)
'''