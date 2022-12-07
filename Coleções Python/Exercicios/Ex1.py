#Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar os
# seguintes passos:
#a- Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7
#b- Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1] e A[5] do vetor e mostre
# na tela esta soma
#c- Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
#d- Mostre na tela cada valor do vetor A, um em cada linha

# A
vetor_a = [1, 0, 5, -2, -5, 7]

# B
soma =  vetor_a[0] + vetor_a[1] + vetor_a[5]
print(soma)

# C
vetor_a[4] = 100
print(vetor_a)

# D
for v in vetor_a:
    print(v)
