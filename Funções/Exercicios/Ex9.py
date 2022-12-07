#Faça uma função que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro. O volume de um
# cilindro circular é calculado por meio da seguinte fórmula: V = pi * raio² * altura, onde pi = 3.141592

def volume_cilindro():
    alt = float(input('Digite a altura do cilindro: '))
    raio = float(input('Digite o raio do cilindro: '))
    vol = 3.14 * (raio ** 2) * alt
    print(f'Dado os dados do cilindro: altura = {alt} e raio = {raio}. O volume do cilindro é: {vol:.2f}')

volume_cilindro()