#Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa
vetor = []
while True:
    num = int(input(f'Digite um número par: '))
    if num % 2 == 0:
        vetor.append(num)
        if len(vetor) == 6:
            break
    else:
        print('O valor precisa ser par')


print(f'Os valores pares digitados foram: {vetor}')
vetor.reverse()
print(f'Os valores pares digitados na ordem inversa é: {vetor}')