#Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. A área do cículo é pi * raio²,
#considere pi = 3.141592

raio = float(input('Digite o raio do círculo: '))
area = 3.141592 * (raio ** 2)
print(f'A área do círculo é:{area:.2f}')