#Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 > ... > A11, ou seja está ordenado em ordem
# crescente ate o sexto elemento, e a partir desse elemento está ordenado em ordem decrescente. Dado o vetor da questão
# anterior proponha um algoritmo para ordenar os elementos
# A1 < A2 < A3 < A4 < A5 < A6 > A7 > A8 > A9 > A10 > A11
vetor = [6, 7, 8, 9, 10, 11, 5, 4, 3, 2, 1]

ordem = sorted(vetor)
print(vetor)
print(ordem)