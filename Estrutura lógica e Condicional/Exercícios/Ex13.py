#Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm peso 1 e a
#terceira peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota de aprovação
# deve ser igual ou superior a 60 pontos

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = (n1 + n2 + (n3 * 2)) / (1 + 1 + 3)
print(f'A média do aluno foi {media:.2f}')
if media > 6:
    print('Aprovado')
else:
    print('Reprovado')