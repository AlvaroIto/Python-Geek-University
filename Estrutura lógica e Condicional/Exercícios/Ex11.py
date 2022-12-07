#Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus
#algarismos. Por exemplo, ao número 251 corresponderá o valor 8(2+5+1). Se o número lido não for maior que zer, o
#programa terminará com a mensagem "Número inválido"

numero = int(input("Informe um número inteiro: "))
soma = 0
while numero > 0:
   soma += numero % 10
   numero = numero // 10
print(soma)

