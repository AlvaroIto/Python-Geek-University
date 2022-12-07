#Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E, conforme a fórmula a seguir
# E = 1 + 1/1! + 1/2! + 1/3! + ... 1/N!
from math import factorial

num = int(input('Digite um número: '))

for n in range(num):
    e = 1 + (1/(factorial(n)))
    n += 1
print(e)