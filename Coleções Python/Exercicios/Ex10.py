#Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral
notas = []
for n in range(15):
    nota = float(input(f'Digite a {n + 1}º nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f'As notas dos alunos foram: {notas}\n'
      f'E a média geral é: {sum(notas)} / {len(notas)} = {media}')