'''

filter recebe 2 parametros, sendo uma função e um iterável. Serve para filtrrar dados de uma determinada coleção



'''

import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

media = statistics.mean(dados)

print(f'Média {media:.2f}')

res = filter(lambda valor: valor > media, dados)
print(list(res))