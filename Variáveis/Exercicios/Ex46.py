#Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos
#dígitos invertidos do número lido EX.: lido=123 gerado=321

num = int(input('Digite um número entre 100 e 999: '))
num = str(num)
print(num[::-1])