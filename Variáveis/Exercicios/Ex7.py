# Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A fórmula de conversão é:
#C = 5.0 * (F -32.0) / 9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit

f = float(input('Digite a temperatura em graus Fahrenheit: '))
c = 5 * (f - 32) / 9
print(f'A temperatura {f}º Fahrenheit em Celsius é: {c}º')