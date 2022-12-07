# Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra for A, a função deverá
# calcular a média aritmética das notas do aluno. se for P, deverá calcular a média ponderada com pesos 5, 3 e 2

def media():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    print('Escolha a média desejada:\n'
          'A - Média aritmética\n'
          'P - Média ponderada')
    m = str(input()).upper()
    if m not in 'AaPp':
        print('Opção inválida!')
    else:
        if m == 'A':
            media_ari = (n1 + n2 + n3) / 3
            print(f'Opção escolhida: {m} - Média aritmética:\n'
                  f'Notas: {n1, n2, n3}\n'
                  f'Média aritmética: {media_ari:.2f}')
        else:
            media_pon = (((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10)
            print(f'Opção escolhida: {m} - Média ponderada:\n'
                  f'Notas: {n1, n2, n3}\n'
                  f'Média ponderada: {media_pon:.2f}')

media()