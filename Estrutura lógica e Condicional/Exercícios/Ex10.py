#Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as
#seguintes fórmulas (onde h corresponde a altura)
# - homens (72.7 * h) - 58
# - mulher (62.7 * h) - 44.7

alt = float(input('Digite a altura: '))
sexo = str(input('Digite o sexo(M/F): ')).upper().strip()

if sexo == 'M':
    ideal = (72.7 * alt) - 58
else:
    ideal = (62.1 * alt) - 44.7

print(f'O pesoa ideal para {"Homem" if sexo == "M" else "Mulher"} com altura de {alt} é {ideal:.2f}kg')