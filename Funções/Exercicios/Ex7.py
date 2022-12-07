# Faça uma função que receba uma temperatura em graus Celsius e retorne-a convertida em graus Fahrenheit. A fórmula de
# conversão é: F = C * (9/5) + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

def fahrenheit():
    c = int(input('Digite a temperatura em graus Celsius: '))
    f = c * (9/5) + 32
    print(f'A temperatura {c}º Celsius convertidade em Fahrenheit é: {f:.2f}ºF')

fahrenheit()