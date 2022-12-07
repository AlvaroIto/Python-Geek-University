# Faça uma função e um programa de teste para o cálculo do volume de uma esfera. Sendo que o raio é passado por
# parâmetro. V = 4/3 * pi * raio³

def volume():
    raio = float(input('Digite o raio da esfera: '))
    vol = 4/3 * 3.14 * (raio ** 2)
    print(f'Raio da esfera: {raio}\n'
          f'Volume da esfera: {vol:.2f}')
volume()