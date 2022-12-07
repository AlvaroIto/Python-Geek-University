#Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula de conversão é: K = L * 0.45,
#sendo K a massam em quilogramas e L e massa e libras

lb = float(input('Digite a massa em libras: '))
kg = lb * 0.45
print(f'A massa {lb}lb convertido em quilograma é: {kg:.2f}kg')