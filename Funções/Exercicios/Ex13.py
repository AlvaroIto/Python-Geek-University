# Faça uma função que receba dois valores numéricos e um símbolo. Este símbolo representará a operação que se deseja
# efetuar com os números. Se o símbolo for + deverá ser realizada uma adição, se for - uma subtração, se for / uma
# divisão e se for * será efetuada uma multiplicação
'''
def operacao():
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print('Digite a operação desejada:\n'
          '+ Soma\n'
          '- Subtração\n'
          '/ Divisão\n'
          '* Multiplicação')
    op = input()

    if op == '+':
        soma = n1 + n2
        print(f'Operação escolhida: Soma\n'
              f'{n1} + {n2}= {soma}')
    elif op == '-':
        subtracao = n1 - n2
        print(f'Operação escolhida: Subtração\n'
              f'{n1} - {n2}= {subtracao}')
    elif op == '/':
        if n2 == 0:
            print(f'O divisor não pode ser {n2}')
        else:
            divisao = n1 / n2
            print(f'Operação escolhida: Divisão\n'
                  f'{n1} / {n2}= {divisao:.2f}')
    elif op == '*':
        multiplicacao = n1 * n2
        print(f'Operação escolhida: Multiplicação\n'
              f'{n1} * {n2}= {multiplicacao}')
    else:
        print('Operação inválida')


operacao()
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

print('Digite a operação desejada:\n'
          '+ Soma\n'
          '- Subtração\n'
          '/ Divisão\n'
          '* Multiplicação')
op = input()

def soma(n1, n2):
    return print(f'Operação escolhida: Soma\n'
                 f'{n1} + {n2} = {n1 + n2}')
def subtracao(n1, n2):
    return print(f'Operação escolhida: Subtração\n'
                 f'{n1} - {n2} = {n1 - n2}')
def divisao(n1, n2):
    if n2 == 0:
        return print(f'O divisor não pode ser {n2}')
    else:
        return print(f'Operação escolhida: Divisão\n'
                     f'{n1} / {n2} = {n1 / n2:.2f}')
def multiplicao(n1, n2):
    return print(f'Operação escolhida: Multiplicação\n'
                 f'{n1} * {n2} = {n1 * n2}')


if op == '+':
    soma(n1, n2)
elif op == '-':
    subtracao(n1, n2)
elif op == '/':
    divisao(n1, n2)
elif op == '*':
    multiplicao(n1, n2)
else:
    print(f'Operação {op} inválida')

