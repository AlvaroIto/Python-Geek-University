#Faça um programa para ler as dimensoões de um terreno (comprimento c  e largura l) bem como o preço do metro da tela p
#Imprima o custo par cercar este mesmo terrno com tela

c = float(input('Digite o comprimento do terreno(mts): '))
l = float(input('Digite a largura do terreno(mts): '))
p = float(input('Digite o valor do metro da tela(mts): R$'))
area = c * l
print(f'Para preencher um área de {area}m² sernão necessários R${p * 2}')