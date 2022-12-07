#Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu
#para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio e imprima
#quanto cada um ganharia do prêmio com base no valor investido

premio = float(input('Digite o valor do prêmio: R$'))
valor1 = float(input('Digite o valor investido do primeiro jogador: R$'))
valor2 = float(input('Digite o valor investido do segundo jogador: R$'))
valor3 = float(input('Digite o valor investido do segundo jogador: R$'))

#ver % investida de cada jogador
inv_tot = valor1 + valor2 + valor3
porc1 = (valor1 / inv_tot)
porc2 = (valor2 / inv_tot)
porc3 = (valor3 / inv_tot)

#divisão do prêmio para cada jogador
premio1 = premio * porc1
premio2 = premio * porc2
premio3 = premio * porc3

print(f'O jogador 1 investiu {int(porc1 * 100)}% e irá receber: R${premio1:.2f}')
print(f'O jogador 2 investiu {int(porc2 * 100)}% e irá receber: R${premio2:.2f}')
print(f'O jogador 3 investiu {int(porc3 * 100)}% e irá receber: R${premio3:.2f}')