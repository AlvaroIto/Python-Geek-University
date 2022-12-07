#Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro

num = int(input('Digite um número: '))
triplo = num * 3
dobro = num * 2
suc = triplo + 1
ant = dobro - 1
soma = triplo + dobro
print(soma)
