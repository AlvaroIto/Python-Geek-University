#Leia um valor de comprimento em centímetro e apresente-o convertido em polegadas. A fórmula de conversão é:
# P = C / 2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.

cm = float(input('Digite o comprimento em centímetros: '))
pol = cm / 2.54
print(f'O comprimento {cm} cm convertido para polegadas é: {pol:.2f}')
