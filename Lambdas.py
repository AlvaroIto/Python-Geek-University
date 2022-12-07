'''
Lambdas são funções sem nome, ou seja, funções anônimas.
calc = lambda x: 3 * x + 1
print(calc(4))

#podemos ter expressões lambdas com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('Alvaro', 'Ito'))

'''



