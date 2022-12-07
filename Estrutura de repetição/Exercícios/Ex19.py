#Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saida cada um dos algarismos que compõem o
# número

num = int(input('Digite um número entre 100 e 999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10

print(f'Unidade: {u}\n'
      f'Dezena: {d}\n'
      f'Centena: {c}')