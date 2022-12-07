#Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto
# sobre o produto (MG 7%, SP 12%, RJ 15%, MS 8%) Faça um programa em que o usuário entre com o valor e o estado destino
# do produto e o programa retorne o preço finaç do produto acrescido do imposto do estado em que ele será vendido
#Se o estado digitado não for válido, mostrar uma mensagem de erro


valor = float(input('Digite o valor do produto: R$'))
destino = str(input('Digite o estado de destino (MG, SP, RJ ou MS): ')).upper()
if destino not in 'MGSPRJMS':
    print('Estado inválido')
else:
    if destino == 'MG':
        print(f'Destino: {destino}\n'
              f'Valor do produto R${valor}\n'
              f'Valor com acréscimo de 7%: R${valor + (valor * 0.07)}')
    elif destino == 'SP':
        print(f'Destino: {destino}\n'
              f'Valor do produto R${valor}\n'
              f'Valor com acréscimo de 12%: R${valor + (valor * 0.12)}')
    elif destino == 'RJ':
        print(f'Destino: {destino}\n'
              f'Valor do produto R${valor}\n'
              f'Valor com acréscimo de 15%: R${valor + (valor * 0.15)}')
    elif destino == 'MS':
        print(f'Destino: {destino}\n'
              f'Valor do produto R${valor}\n'
              f'Valor com acréscimo de 8%: R${valor + (valor * 0.08)}')
