#Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0

while True:
    num = int(input('Digite um número positivo: '))
    if num < 0:
        print('Número precisa ser positivo')
    else:
        break
print(f'Os cinco primeiros números mútiplos de 3 a partir do número {num} são:')
for n in range(0, 6):
    mult = num * 3
    print(f' {mult}')
    num = mult