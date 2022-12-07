# Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de todos os seus algarismos. Por
# exemplo, ao número 251 corresponderá o valor 8 ( 2 + 5 + 1). Se o número lido não for maior do que zero, o programa
# terminará com a mensagem "Número inválido"

def soma_algarismo():
    num_lista = []
    soma = 0
    num = int(input('Digite um número: '))
    if num >= 0:
        #converter número em string para separar
        num_str = str(num)
        #separar algarismos do número digitado
        for n in num_str:
            #somar os algarimos do número digitado
            soma += int(n)
            #armazenar os algarismos para exibição
            num_lista.append(int(n))
        print(f'Número digitado: {num}\n'
              f'Soma dos algarismos: {num_lista} = {soma}')
    else:
        print(f'Número {num} inválido!')

soma_algarismo()