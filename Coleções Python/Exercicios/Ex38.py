#Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores, guardando-os num vetor.
# Ordene o valor assim que ele for digitado. Mostre ao final na tela os valores em ordem

vetor = []
for n in range(3):
    num = int(input(f'Digite o {n+1}º valor do vetor: '))
    vetor.append(num)

ordem = sorted(vetor)
print(vetor)
print(ordem)