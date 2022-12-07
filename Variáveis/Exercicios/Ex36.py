#Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um cilindro cricular é
#calculado por meio da seguinte fórmula: V = pi * raio² * altura, onde pi = 3.141592

alt = float(input('Digite a altura do cilindro: '))
raio = float(input('Digite o raio do cilindro: '))
vol = 3.14 * (raio ** 2) * alt
print(f'O volume do cilindro é: {vol:.2f}')