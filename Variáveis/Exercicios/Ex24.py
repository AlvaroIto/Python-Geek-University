#Leia um valor de área em emtros quadrados m² e apresente-o convertido em acres. A fórmula de conversão é:
#A = m * 0.00247, sendo M a área em emtros quadrados e A a área em acres

m2 = float(input('Digite a área em metros quadrados: '))
ac = m2 * 0.00247
print(f'A área em metros quadrados {m2}m² convertida para acres é: {ac:.2f}ac')

