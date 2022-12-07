#Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:
'''
IMC             Classificação
< 18,5          Abaixo do peso
18,6 - 24,9     Saudável
25,0 - 29,9     Peso em excesso
30,0 - 34,9     Obesidade Grau 1
35,0 - 39,9     Obesidade Grau 2 (severa)
>= 40,0         Obesidade Grau 3 (mórbida)
'''

peso = float(input('Digite se peso(kg): '))
alt = float(input('Digite a altura(mts): '))
imc = peso / (alt * alt)

if imc <= 18.5:
    print(f'IMC: {imc:.2f}kg/m². Abaixo do peso')
elif 18.6 < imc <= 24.9:
    print(f'IMC: {imc:.2f}kg/m². Saudável.')
elif 25 < imc <= 29.9:
    print(f'IMC: {imc:.2f}kg/m². Peso em excesso')
elif 30 < imc <= 34.9:
    print(f'IMC: {imc:.2f}kg/m². Obesidade Grau 1')
elif 35 < imc <= 39.9:
    print(f'IMC: {imc:.2f}kg/m². Obesidade Grau 2(severa)')
else:
    print(f'IMC: {imc:.2f}kg/m². Obesidade Grau 3(mórbida)')