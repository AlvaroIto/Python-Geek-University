#Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em ms/s (metros por segundo). A fórmula de
# conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s

km = float(input('Digite a velocidade em Km/h: '))
ms = km / 3.6
print(f'A velocidade {km} km/h convertida para m/s é: {ms:.2f} m/s')