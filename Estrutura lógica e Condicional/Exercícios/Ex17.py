#Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: A = ((base maior + base menor) * altura) / 2
#Lembre-se a base maior e a base menor devem ser números maiores que zero

bmaior = float(input('Digite o valor da base maior: '))
bmenor = float(input('Digite o valor da base menor: '))
alt = float(input('Digite o valor da altura: '))

if bmaior > 0 and bmenor > 0:
    area = ((bmaior + bmenor) * alt) / 2
    print(f'A área do trapézio é: {area}')
else:
    print('A base deve ser maior que 0')

