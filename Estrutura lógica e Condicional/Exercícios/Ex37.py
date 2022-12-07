#As tarifas de certo parque de estacionamento são as seguintes:
# - 1ª e 2ª hora - R$1,00 cada
# - 3ª e 4ª hora - R$1,40 cada
# - 5ª e seguintes - R$2,00 cada
#O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos
# pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido por 120 minutos. Os momentos de chegada
#ao parque e partida deste são apresentados na forma de pares de inteiros, representando horas e minutos. Por exemplo
#o par 12 50 representará "dez para uma da tarde". Pretendendo-se criar um programa que, lidos pelo teclado os
#momentos de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a
# partida se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior a da partida
# isso não é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada

chegada_hora = int(input('Digite a hora de chegada(01-24): '))
chegada_minuto = int(input('Digite o minuto de chegada(00-59): '))
saida_hora = int(input('Digite a hora de saída(01-24): '))
saida_minuto = int(input('Digite o minuto de saída(01-24): '))
#arredondar os valores
if chegada_minuto > 0:
    arredonda_hora_chegada = chegada_hora + 1
if saida_minuto > 0:
    arredonda_hora_saida = saida_hora + 1

if chegada_hora > saida_hora:
    tempo = chegada_hora - saida_hora
else:
    tempo = saida_hora - chegada_hora

print(f'Hora de chegada {chegada_hora}:{chegada_minuto}\n'
      f'Hora de saída {saida_hora}:{saida_minuto}\n'
      f'Tempo de permanência {tempo} hora(s)')
if tempo <= 2:
    valor = tempo
elif 2 < tempo <= 4:
    valor = tempo * 1.40
else:
    valor = tempo * 2
print(f'Valor: R${valor:.2f}')