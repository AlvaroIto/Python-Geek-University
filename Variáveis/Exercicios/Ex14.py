#Leia um ângulo em graus e apresente-o convertido em radianos. A fórmul de conversão é: R = G * pi / 180, sendo G o
#ângulo em graus e R em radianos e pi = 3.14

graus = int(input('Digite o valor do angulo em graus: '))
rad = graus * 3.14 / 180
print(f'O ângulo {graus} em graus convertido para radiano é: {rad}')
