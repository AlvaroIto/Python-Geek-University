#A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10,
#respectivamente, a um trabalhyo de laboratório, a avaliação semestral a um exame fina. A média das três notas
#mencionadas anteriormente obedece aos pesos: Trabalho de laboratório: 2. Avaliação semestral: 3. Exame final: 5. De
#acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9), de recuperação (entre 3 e 4.9)
#ou se foi aprovado. Faça todas as verificações necessárias

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / (2 + 3 + 5)

if media < 3:
    print(f'Média {media}. REPROVADO!')
elif media > 4.9:
    print(f'Média {media}. APROVADO!')
else:
    print(f'Média {media}. RECUPERAÇÃO!')