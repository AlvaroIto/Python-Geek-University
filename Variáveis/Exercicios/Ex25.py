#Leia um valor de área em acres e apresente-o convertido em metros quadrados m². A fórmula de conversão é:
# M = A * 4048.58, sendo M a área e metros quadrados e A a área em acres

ac = float(input('Digite a área em acres: '))
m2 = ac * 4048.58
print(f'A área em acres {ac}ac convertida para metros quadrados é: {m2:.2f}m²')
