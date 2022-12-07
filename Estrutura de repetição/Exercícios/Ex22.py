#Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de notas
#válidas no intervalor de 10 a 20, e que mostre na tela, como resultado, a correspondente média aritmética. O número
#de notas com que o aluno pretende efetuar o cálculo não será fornecido ao programa, o qual terminará quando for
#introduzido um valor que não seja válido como nota de aprovação

media = 0
soma = 0
while True:
    nota = float(input('Digite uma nota válida no intervalor de 10 a 20: '))

    if nota < 0 or nota > 10:
        break
    else:
        media += 1
        soma += nota


media_tot = soma / media
print(f'Foram digitados {media} notas e a média é {media_tot:.1f}')
