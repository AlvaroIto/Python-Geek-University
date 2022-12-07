#Faça um programa que receba dois número e mostre o maior. Se por acaso, os dois número forem iguais, imrpima a
#mensagem Numero iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print(f'O {n1} é maior que o {n2}')
elif n2 > n1:
    print(f'O {n2} é maior que o {n1}')
else:
    print(f'O {n1} e o {n2} são iguais!!')

