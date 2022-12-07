#EScreva o menu de opções abaixo. Leia a opção do usuário e execute a operação esolhida. Escreva uma mensagem de erro se
# a opção for inválida
# Escolha a opção:
# 1- Soma de 2 números
# 2- Diferença entre 2 números (maior pelo menor)
# 3- Produto entre 2 números
# 4- Divisão entre 2 números (o denominador não pode ser zero)
# Opção

escolha = ('Soma', 'Subtração', 'Multiplicação', 'Divisão','')


print('=' * 60)
opcao = int(input('Escolha a opção\n'
      '1- Soma de 2 números\n'
      '2- Diferença entre 2 números (maior pelo menor)\n'
      '3- Produto entre 2 números\n'
      '4- Divisão entre 2 números (o denominador não pode ser zero)\n'
      'Opção: '))
print('=' * 60)


if opcao > 4:
    escolha == 5
    print(f'Opção {opcao} inválida')
    print('FIM')
else:
    print(f'Opção escolhida: {escolha[opcao - 1]}')
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} = {soma}')
    elif opcao == 2:
        if n1 > n2:
            subtracao = n1 - n2
            print(f'A subtração de {n1} - {n2} = {subtracao}')
        else:
            subtracao = n2 - n1
            print(f'A subtração de {n2} - {n1} = {subtracao}')
    elif opcao == 3:
        multiplicacao = n1 * n2
        print(f'A multiplicação de {n1} * {n2} = {multiplicacao}')
    elif opcao == 4:
        if n2 == 0:
            print(f'O Denominador não pode ser {n2} (Zero)')
        else:
            divisao = n1 / n2
            print(f'A divisão de {n1} / {n2} = {divisao}')