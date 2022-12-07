#Faça um programa que calcula a associção em paralelo de dois resistores R1 e R2 fornecidos pelo usuário via teclado.
#O programa fica pedindo estes valores e calculando até que o usuário entre com um valor para resistência igual a zero
#R = R1 * R2 / R1 + R2

while True:
    r1 = int(input('Digite o valor de R1: '))
    r2 = int(input('Digite o valor de R2: '))
    r = (r1 * r2) / (r1 + r2)
    print(f'R = {r:.2f}')
    if r1 <= 0 or r2 <= 0:
        print('FIM')
        break
