#Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas.
#Uma nota válida deve ser, obrigatóriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido,
#este fato deve ser informado ao usuário e o programa termina


n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
if n1 in range(0, 11) and n2 in range(0, 11):
    media = (n1 + n2) / 2
    print(f'A média das notas {n1} e {n2} é: {media}')
else:
    print('Números inválidos!')