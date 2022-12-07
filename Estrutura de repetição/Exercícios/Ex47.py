#Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
#- adição
#- Subtração
#- Multiplicação
#- Divisão
#- Saída
#O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do rsultado e a volta ao menu de
# opções. O programa só termina quando for escolhida a opçao de saída
opcao = 0
while True:
    opcao = int(input('MENU DE OPÇÕES PARA CÁLCULO:\n'
          '1- Adição\n'
          '2- Subtração\n'
          '3- Multiplicação\n'
          '4- Divisão\n'
          '5- SAIR\n'
          'Digite a opção desejada: '))

    if opcao > 5:
        print('Opção inválida. FIM')
        break
    if opcao == 5:
        print(f'Opção escolhida: SAIR. Fim do programa')
        break
    else:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

        if opcao == 1:
            print('Opção escolhida: Soma')
            soma = n1 + n2
            print(f'{n1}+{n2}={soma}')
        elif opcao == 2:
            print('Opção escolhida: Subtração')
            if n1 > n2:
                subtracao = n1 - n2
                print(f'{n1}-{n2}={subtracao}')
            else:
                subtracao = n2 - n1
                print(f'{n2}-{n1}={subtracao}')
        elif opcao == 3:
            print('Opção escolhida: Multiplicação')
            multiplicacao = n1 * n2
            print(f'{n1}*{n2}={multiplicacao}')
        elif opcao == 4:
            print('Opção escolhida: Divisão')
            if n2 == 0:
                print('ERRO, Divisor não pode ser igual a ZERO!')
            else:
                divisao = n1 / n2
                print(f'{n1}/{n2}={divisao:.2f}')

