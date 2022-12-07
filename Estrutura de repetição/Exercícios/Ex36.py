#Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o quadrado da
# soma. Ex: A soma dos quadrados dos dez primeiros números naturais é, 1² + 2² + ... + 10² = 385. O quadrado da soma dos
# dez primeiros números naturais é, ( 1 + 2 + .... + 10)² = 55² = 3025. A diferença entre a soma dos quadrados dos dez
# primeiros números naturais e o quadrado da soma é 3025-385 = 2640

calc1 = 0
calc2 = 0
soma = 0

for n in range(1, 101):
    calc1 += n**2
    soma += n
    calc2 = soma ** 2

res = calc2 - calc1


print(f'Diferença entre a soma dos quadrados ({calc1}) e o quadrado da soma ({calc2}) dos 100 primeiros números naturais '
      f'é {res}')