#Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produtor escalar entre eles. Os conjuntos
# tem 5 elementos cada. Imprimir os dois conjkuntos e o produto escalar, sendo que o produto escalar é dado por:
# x1 * y1 + x2 * y2 + ... + xn * yn

c1 = []
c2 = []
produto_tot = []

for n in range(5):
    c1.append(int(input(f'Digite o {n+1}º valor do primeiro conjunto: ')))
for n in range(5):
    c2.append(int(input(f'Digite o {n+1}º valor do segundo conjunto: ')))

produto = (c1[0] * c2[0]) + (c1[1] * c2[1]) + (c1[2] * c2[2]) + (c1[3] * c2[3]) + (c1[4] * c2[4])
print(produto)
