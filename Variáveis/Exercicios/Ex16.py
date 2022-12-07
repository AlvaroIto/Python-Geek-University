#Leia um valor de comprimento em polegadas e apresente-o convertido em centímetro. A fórmula de conversão é:
#C = P * 2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.

pol = float(input('Digite o comprimento em polegadas: '))
cm = pol * 2.54
print(f'O comprimento {pol} polegadas convertido em centímetros é: {cm:.2f}')