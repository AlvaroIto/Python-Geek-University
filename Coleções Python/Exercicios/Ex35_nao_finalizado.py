#Faça um programa que leia dois números a e b. (positivos menores que 10000) e:
#- Crie um vetor onde cad posição é um algarismo do número. A primeira posição é o algarismo menos significativo
#- Crie um vetor que seja a soma de a e b, mas faça-o usando paenas os vetores construidos anterioemente
#Dica: some as posióes correspondente. Se a soma ultrapassar 10, subtraia 10 do resultado e some 1 a proxima posição

vetor_a = []
vetor_b = []
vetor_soma = []

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valore de B: '))
soma_d = soma_c = soma_m = soma_dm = 0

u_a = a // 1 % 10
d_a = a // 10 % 10
c_a = a // 100 % 10
m_a = a // 1000 % 10
dm_a = a // 10000 % 10
vetor_a.append(dm_a)
vetor_a.append(m_a)
vetor_a.append(c_a)
vetor_a.append(d_a)
vetor_a.append(u_a)


u_b = b // 1 % 10
d_b = b // 10 % 10
c_b = b // 100 % 10
m_b = b // 1000 % 10
dm_b = b // 10000 % 10
vetor_b.append(dm_b)
vetor_b.append(m_b)
vetor_b.append(c_b)
vetor_b.append(d_b)
vetor_b.append(u_b)



soma_u = u_a + u_b
if soma_u >= 10:
    soma_u = soma_u - 10
    soma_d = 1

soma_d += (d_a + d_b)
if soma_d >= 10:
    soma_d = soma_d - 10
    soma_c = 1

soma_c += (c_a + c_b)
if soma_c >= 10:
    soma_c = soma_c - 10
    soma_m = 1

soma_m += (m_a + m_b)
if soma_m >= 10:
    soma_m = soma_m - 10
    soma_dm = 1

soma_dm += (dm_a + dm_b)

vetor_soma.append(soma_dm)
vetor_soma.append(soma_m)
vetor_soma.append(soma_c)
vetor_soma.append(soma_d)
vetor_soma.append(soma_u)

print(f'Vetor A onde cada número é uma posição: {vetor_a}')
print(f'Vetor B onde cada número é uma posição: {vetor_b}')
print(f'Vetor Soma A+B: {vetor_soma}')


