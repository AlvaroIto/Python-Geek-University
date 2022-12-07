#Leia um valor de área em hectares e apresente-o convertido em metros quadrados m². a fórmula de conversão é:
# M = H * 10000, sendo M a área em metros quadrados e H a área em hectares

hec = float(input('Digite a área em hectares: '))
m2 = hec * 10000
print(f'A área {hec}hec convertida em metros quadrados é: {m2}m²')
