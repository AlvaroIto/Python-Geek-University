#Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro. Se o código for zero,
# finalize o prgrama, se for 1 mostre o vetor na ordem direta. se for 2 mostre o vetor na ordem inversa. Caso o código
# for difrente de 1 e 2 escreva uma mensagem informando que o código é inválido

vetor = []

for n in range(5):
    num = int(input(f'Digite o {n+1}º valor: '))
    vetor.append(num)

while True:

    print('=' * 50)
    print('Escolha a opção:\n'
          '0 - Sair do Programa\n'
          '1 - Mostrar números digitados\n'
          '2 - Mostrar números digitados na ordem inversa')
    cod = int(input())
    if cod == 0:
        print(f'Opção escolhida: {cod} "Sair do Programa"')
        break
    else:
        if cod == 1:
            print(f'Opção escolhida - {cod} "Mostrar números digitados: {vetor}')
        elif cod == 2:
            print(f'Opção escolhida - {cod} "Mostrar números digitados na ordem inversa": {vetor[::-1]}')
        else:
            print(f'Opção escolhida - {cod} Código inválido!')
            break

