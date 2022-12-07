# Faça uma função que receba dois números e retorne qual deles é o maior.

def maior_num():

    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    if n1 > n2:
        print(f'O maior número é o {n1}')
    elif n1 < n2:
        print(f'O maior número é o {n2}')
    else:
        print(f'Os números {n1} e {n2} são iguais')

maior_num()
