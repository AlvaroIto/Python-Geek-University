#Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha

num = int(input('Digite um número de 4 dígitos de 1000 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(unidade)
print(dezena)
print(centena)
print(milhar)