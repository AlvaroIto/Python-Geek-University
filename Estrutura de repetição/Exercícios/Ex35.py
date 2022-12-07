#Faça um programa que some os números ímpares contidos em um intervalo definido pelo usuário. O usuário define o valor
# inicial do inteval e o valor final deste intevalo e o programa deve somar todos os números ímpares contidos neste
# intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior que o valor final) deve ser
# escrito uma mensagem de erro na tela, " intervalo de valores inválido" e o programa termina.

val_inicio = int(input('Digite o valor de inicio: '))
val_final = int(input('Digite o valor de fim: '))
soma = 0

if val_inicio > val_final:
    print('Intervalo de valores inválido')
else:
    for n in range(val_inicio, val_final+1):
        print(n)
        if n % 2 != 0:
            soma += n
    print(f'A soma dos números ímpares entre os números {val_inicio} e {val_final} é: {soma}')