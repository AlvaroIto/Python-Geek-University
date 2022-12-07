#Leia um valor de área em emtros quadrados m² e apresente-o convertido em hectares. A fórmula de conversão é:
#H = M * 0.0001, sendo M a área em metros quadraros e H a áres em hectares

m2 = float(input('Digite a área em metros quadrados: '))
hec = m2 * 0.0001
print(f'A área {m2}m² convertido em hectares é: {hec}hec')
