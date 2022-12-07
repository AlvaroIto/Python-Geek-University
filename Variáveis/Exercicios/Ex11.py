#Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilometros por hora). A fórmula
#de conversão é K = M * 3.6, sendo K a velocidade em km/h e M em m/s

ms = float(input('Digite a velocidade em metros por segundo (m/s): '))
km = ms * 3.6
print(f'A velocidade {ms} m/s corresponde a {km} km/h')