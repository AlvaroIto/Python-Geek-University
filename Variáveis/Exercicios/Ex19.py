#Leia um valor de volume em litros e apresente-o convertido em metro cúbicos m³. A fórmula de conversão é: M = L / 1000,
#sendo L o volume em litros e M o volume em metros cúbicos

l = int(input('Digite o volume em litros: '))
m3 = l / 1000
print(f'O volume {l}L convertido para metros cúbicos é: {m3}m³')
