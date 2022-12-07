#Leia 10 números inteiros e armazene em um vetor. EM seguida escreva os elementos que são primos e suas respectivas
# posições no vetor
vetor = []

for n in range(10):
    num = int(input(f'Digite o {n+1}º número do vetor: '))
    vetor.append(num)
    if num > 1:
        for i in range(2, vetor[num]):
            print(i)

            '''
            if num % i == 0:
                print(f'O número {i} é primo.')
                break
'''

