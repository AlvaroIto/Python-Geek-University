#Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice versa. Você deve criar um menu com as
# duas opções de conversão e com uma opção para finalizar o programa. O usuário poderá fazer quantas conversões desejar,
# sendo que o program só será finalziado quando a opção de finalizar for escolhida


while True:
    opcao = int(input('Digite a opção desejada:\n'
                      '1- Conversão km/h -> m/s \n'
                      '2- Conversão m/s -> km/h\n'
                      '3- Sair\n'
                      ''))
    if opcao >= 3:
        print('FIM')
        break
    else:
        velocidade = float(input('Digite a velocidade: '))
        if opcao == 1:
            conv = velocidade / 3.6
            print(f'A velocidade {velocidade}km/h convertida para m/s é: {conv:.2f}m/s')
            print()
        elif opcao == 2:
            conv = velocidade * 3.6
            print(f'A velocidade {velocidade}m/s convertida para km/h é: {conv:.2f}km/h')
            print()
