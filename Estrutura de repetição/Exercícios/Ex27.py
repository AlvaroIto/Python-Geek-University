#Em matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmônica:
# H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
#Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n)

num = int(input('Digite um número: '))
for n in range(1, num):
   har = 1 + 1/n
   print(1 / n)


print(f'H{num} = {har:.2f}')
