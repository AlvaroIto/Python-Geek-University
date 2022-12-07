#Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão é: G = R * 180 / pi, sendo G o
#ângulo em graus e R em radianos e pi = 3.14

rad = int(input('Digite o ângulo em radiano: '))
graus = rad * 180 / 3.14
print(f'O ângulo radiano {rad} convertido para graus é: {graus}')
