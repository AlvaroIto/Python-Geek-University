#Escreva um programa para calcular o valor da série, para 5 termos
# S = 0 + 1/2! + 2/4! + 3/6! + ...
from math import factorial
s = 0 + 1/factorial(2) + 2/factorial(4) + 3/factorial(6)

print(s)