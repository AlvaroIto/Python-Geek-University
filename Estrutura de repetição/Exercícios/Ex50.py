#Chico tem 1.50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centímetros por ano.
# Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico
ano = 0
alt_chico = 1.50
alt_ze = 1.10

while alt_ze <= alt_chico:
    alt_ze += 0.03
    alt_chico += 0.02
    ano += 1

print(f'Serão necessários {ano} anos para a altura de Zé {alt_ze:.2f} passar a altura de Chico {alt_chico:.2f}')
