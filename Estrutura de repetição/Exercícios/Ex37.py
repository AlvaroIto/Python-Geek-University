#Escreva um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade seguinte: a soma
# dos dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem elevada ao quadrado é igual ao próprio
# número. Por exemplo para o inteiro 3025, temos que 30 + 25 = 55 55² = 3025

for n in range(1000, 10000):
    u = n // 1 % 10
    d = n // 10 % 10
    c = n // 100 % 10
    m = n // 1000 % 10

    baixa_ordem = (d * 10) + u
    alta_ordem = (m * 10) + c
    soma = baixa_ordem + alta_ordem
    ordem_elevada = soma ** 2

    if n == ordem_elevada:
        print(f'Número: {n}\n'
              f'Baixa Ordem: {baixa_ordem}\n'
              f'Alta Ordem: {alta_ordem}\n'
              f'Soma (baixa+alta): {soma}\n'
              f'Quadrado da soma: {ordem_elevada} = Número {n}\n'
              f'')


