# Faça uma função que receba 3 números inteiros com parâmetro, representando horas, minutos e segundos, e os converta
# em segundos.

def conversor():
    hora = int(input('Digite a hora: '))
    minuto = int(input('Digite o minuto: '))
    segundo = int(input('DIgite o segundo: '))

    hora_seg = hora * 3600
    minuto_seg = minuto * 60
    segundo_total = hora_seg + minuto_seg + segundo
    print(f"O tempo: {hora}:{minuto}:{segundo} em segundos é: {segundo_total}")

conversor()