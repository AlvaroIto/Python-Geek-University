#Leia um valor de volume em metro cúbicos m³ e apresente-o convertido em litros. A fórmula de conversão é L = 1000 * M,
#sendo L o volume em litros em M o volume em metros cúbicos

m3 = float(input('Digite o volume em m³: '))
l = 1000 * m3
print(f'O volume {m3}m³ convertido para litros é: {l}L')
