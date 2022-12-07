# Faça uma função que receba a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um
# percurso, calcule o consumo em Km/l e escreva uma linha mensagem de acordo com a tabela abaixo:
'''
Consumo     (Km/l)          Mensagem
menor que     8             Venda o carro!
entre       8 e 14          Econômico!
maior que     12            Super Econômico!

'''

def conversor():
    km = float(input('Digite a distância em KM: '))
    litros = float(input('Digite o consumo de gasolina do carro na distância percorrida: '))
    consumo = km / litros

    if consumo < 8:
        print(f'Consumo de {consumo:.2f}Km/l. Venda o carro!')
    elif consumo > 12:
        print(f'Consumo de {consumo:.2f}km/l. Super Econômico!')
    else:
        print(f'Consumo de {consumo:.2f}km/l. Econômico!')

conversor()
