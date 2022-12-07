#Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas pelo usuário. Esse programa não
# pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0

base = float(input('Digite a base: '))
alt = float(input('Digite a altura: '))

if base <= 0 or alt <= 0:
    print('Dados inválidos!')
else:
    area = (base * alt) / 2
    print(f'A área do triângulo de base {base} e altura {alt} é: {area:.2f}')
