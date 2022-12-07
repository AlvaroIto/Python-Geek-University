#Escreva um programa que recebe como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas
# de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas
# de 100, 50, 20, 10, 5, 2 e 1 real

valor = int(input('Digite o valor de saque: R$'))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            break

