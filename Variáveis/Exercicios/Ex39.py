# A importância de R$780.000.00 será dividida entre três ganhadores de um concurso. Sendo que a quantida total:
# - O primeiro ganhador receberá 46%
# - O Segundo receberá 32%
# - O teceiro recerá o restante
#Calcule e mostre a quantida ganha por cada um dos ganhadores

valor = 100000
novo_valor = 0
primeiro = valor - (valor * 0.46)
print(f'valor 1 = R${primeiro:.2f}')
novo_valor = valor - primeiro
segundo = novo_valor - (novo_valor * 0.32)
print(f'valor 2 = R${segundo:.2f}')
novo_valor = novo_valor - segundo
print(f'valor 3 = R${novo_valor:.2f}')
soma = primeiro + segundo + novo_valor
print(f'Soma    = R${soma:.2f}')
