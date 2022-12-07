#Leia a distância em KM e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo
# em km/l e escreva uma mensagem de acordo com a tabela abaixo:
'''
consumo       km/l         mensagem
menor que      8        Venda o carro!
entre        8 e 14       Econômico!
maior que     12        Super Econômico!
'''

distancia = float(input('Digite a distância em km: '))
consumo = float(input('Digite a quantidade de litros de gasolina consumido: '))

km_litro = distancia / consumo

if km_litro < 8:
    print(f'Consumo {km_litro} km/l. Venda o carro!')
elif 8 < km_litro < 14:
    print(f'Consumo {km_litro} km/l. Econômico!')
else:
    print(f'Consumo {km_litro} km/l. Super Econômico!')
