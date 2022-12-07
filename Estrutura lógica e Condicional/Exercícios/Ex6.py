#Escreva um programa que, dados dois número inteiros, mostre na tela o amior deles, assim como a diferença existente
#entre ambos

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print(f'O {n1} é maior que o {n2} e a diferença entre eles é {n1 - n2}')
elif n2 > n1:
    print(f'O {n2} é maior que o {n1} e a diferença entre eles é {n2 - n1}')
else:
    print(f'O {n1} e o {n2} são iguais!! E a diferença entre eles é {n1 - n2}')

