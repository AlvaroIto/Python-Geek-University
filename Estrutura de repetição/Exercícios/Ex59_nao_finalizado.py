#Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor do kwh, e para cada habitante
# entre com os seguitnes dados: consumo do mês e o código do consumidor (1- Residencial, 2- Comercial, 3- Industrial).
# No final imprima o maior, o menor e a média do consumo dos habitantes; e por fim o total do consumo de cada categoria
# de consumidor

habitantes_tot = int(input('Digite a quantidade total de habitantes da cidade: '))
consumo_habitante = []
codigo = []
lista_junta = []
maior = menor = cont = soma = 0

for n in range(habitantes_tot):
    consumo_mes = int(input(f'Digite o valor do consumo kwh/mes do {n+1}º habitante: '))
    consumo_habitante.append(consumo_mes)
    codigo_habitante = int(input(f'Digite o código do consumidor do {n+1}º habitante onde:\n'
                                 f'1 - Residencial\n'
                                 f'2 - Comercial\n'
                                 f'3 - Industrial\n'
                                 f' '))
    codigo.append(codigo_habitante)
    cont += 1

    if cont == 1:
        maior = menor = 1
    else:
        if consumo_mes > maior:
            maior = consumo_mes
        if consumo_mes < menor:
            menor = consumo_mes

    for v in consumo_habitante:
        for c in codigo_habitante:
            lista_junta = [c, v]



media = soma / habitantes_tot

print(f'O maior consumo de kwh foi de {maior}kwh')
print(f'O menor consumo de kwh foi de {menor}kwh')
print(f'A média de consumo foi de {media}kwh')
print(codigo)
print(lista_junta)

