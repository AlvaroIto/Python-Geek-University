#Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos
valores = []
for n in range(6):
    v = int(input(f'Digite o {n+1}º valor: '))
    valores.append(v)
print(f'Os valores digitados foram: {valores}')