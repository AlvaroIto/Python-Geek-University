# Leia uma temperatura em graus Kelvin e apresente-a converttida em graus Celsius. A fórmula de conversão é:
# C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

k = float(input('Digite a temperatura em graus Kelvin: '))
c = k - 273.15
print(f'A temperatura {k}º Kelvin convertida para Celsius é: {c:.2f}º')
