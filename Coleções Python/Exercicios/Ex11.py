#Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a
# soma dos números positivos desse valor

vetor = []
negativos = []
positivo = []
soma = 0

for n in range(10):
    num = float(input(f'Digite o {n+1}º valor: '))
    vetor.append(num)
    if num < 0:
        negativos.append(num)
    else:
        positivo.append(num)
        soma += num
print(f'Números digitados: {vetor}\n'
      f'Foram digitados {len(negativos)} números negativos: {negativos}\n'
      f'A soma dos números positivos ({positivo}) é: {soma}')
