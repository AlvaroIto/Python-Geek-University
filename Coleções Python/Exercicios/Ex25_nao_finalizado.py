#Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que não são multiplos de 7 ou que
# terminam com 7
vetor = []
cont = 0

while True:
    if len(vetor) < 101:
        for n in range(100):
            if n % 7 != 0:
                if n // 1 % 10 != 7:
                    vetor.append(n)
                    cont += 1
    else:
        break
print(vetor)
print(len(vetor))
