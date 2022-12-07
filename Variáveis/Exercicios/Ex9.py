#Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A fórmula de conversão é:
#K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin

c = float(input('Digite a temperatura em graus Celsius: '))
k = c + 273.15
print(f'A temperatura {c}º Celsius convertida em graus Kelvin é {k}º')
