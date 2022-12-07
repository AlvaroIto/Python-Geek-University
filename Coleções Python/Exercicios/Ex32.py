#Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuário não informa elementos repetidos) Calcule e mostre os vetores resultantes em cada caso abaixo:
#- Soma entre x e y: soma de cada elemento de x comm o elemento da mesma posição em y
#-  Produto entre x e y: multiplicação de cada elemento de x comm o elemento da mesma posiçãoi em y
#- Diferença entre x e y: todos os elementos de x que não existam em y
#- Interseção entre x e y: apenas os elementos que aparecem nos 2 vetores
#- União entre x e y: todos elementos que estão em x e y

x = []
y = []
vetor_soma = []
vetor_mult = []
i = 0

for n in range(5):
    num = int(input(f'Digite o {n+1}º valor do primeiro vetor: '))
    x.append(num)
for n in range(5):
    num = int(input(f'Digite o {n + 1}º valor do segundo vetor: '))
    y.append(num)

while i < len(x):
    soma = [y[i] + x[i]]
    vetor_soma.append(soma)
    mult = [y[i] * x[i]]
    vetor_mult.append(mult)
    i += 1

inter = set(x).intersection(set(y))
uniao = set(x).union(set(y))

print(f'vetor x: {x}\n'
      f'vetor y: {y}\n'
      f'Soma entre x e y: {vetor_soma}\n'
      f'Produto entre x e y: {vetor_mult}\n'
      f'Intersecção x e y: {inter}\n'
      f'União x e y: {uniao}')

