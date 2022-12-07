#Faça um programa que mostre ao usuário um menu com 4 opções matemáticas (as basicas, por exemplo). O usuário escolhe
#uma das opoes e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo

print('=' * 30)
print('Escolha um Operação')
opcao = int(input('1- Soma\n'
                  '2- Subtração\n'
                  '3- Multiplicação\n'
                  '4- Divisão\n'
                  ''))

if opcao < 0 or opcao > 4:
    print('OPÇÃO INVÁLIDA!')
else:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))

    if opcao == 1:
        print(f'Opção escolhida: SOMA\n'
              f'{n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'Opção escolhida: SUBTRAÇÃO\n'
              f'{n1} - {n2} = {n1 - n2}')
    elif opcao == 3:
        print(f'Opção escolhida: MULTIPLICAÇÃO:\n'
              f'{n1} * {n2} = {n1 * n2}')
    elif opcao == 4:
        print(f'Opção escolhida: DIVISÃO:\n'
              f'{n1} / {n2} = {n1 / n2:.2f}')