#Leia um valor em real e a cotação do dólar. Em sequida, imprima o valor correspondente em dólares

real = float(input('Digite o valor em reais: R$'))
dolar = float(input('Informe a cotação do dólar $1.00 = R$'))
conversao = real / dolar
print(f'Valor em Reais: R${real:.2f}')
print(f'Cotação do dólar: $1.00 = R${dolar:.2f}')
print(f'Valor convertido para dólar: ${conversao:.2f}')