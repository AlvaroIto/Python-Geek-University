#Faça um programa que leia dez conjuntos de dois alores, o primerio representando o número do aluno e o segundo
# representando a sua altura em metros. Encontre o aluno mais baixo e o mais alto Mostre o número do aluno mais baixo e
# do mais alto, juntamento com suas alturas

chave = []
valor = []
dados = {}
for n in range(5):
    chave.append(int(input(f'Digite o número do {n+1}º aluno: ')))
for n in range(5):
    valor.append(int(input(f'Digite a altura em metros do {n+1}º aluno: ')))

dados = dict(zip(chave, valor))
baixo_tam = min((dados.values()))
baixo_num = dados.get(min((dados.values())))
alto_tam = max((dados.values()))


print(dados)

for c, v in enumerate(dados):


'''
print(f'O aluno mais baixo é o aluno {baixo_num} com altura de {baixo_tam}\n'
      f'O aluno mais alto é o aluno {alto_tam} com altura de {alto_tam}')
'''