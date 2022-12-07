#Leia a nota e o número de faltas de um aluno e escreva seu conceito. De acordo com a tabela abaixo, quando o aluno tem
# mais de 20 faltas ocorre uma redução de conceito

'''
Nota            Conceito(até 20 faltas)     conceito(mais de 20 faltas)
9.0 até 10.0                A                           B
7.5 até 8.9                 B                           C
5.0 até 7.4                 C                           D
4.0 até 4.9                 D                           E
0.0 até 3.9                 E                           E
'''

nota = float(input('Digite a nota: '))
falta = int(input('Digite o número de faltas: '))

if falta > 20:
    if 9.0 <= nota <= 10.0:
        print('Conceito B')
    elif 7.5 <= nota <= 8.9:
        print('Conceito C')
    elif 5.0 <= nota <= 7.4:
        print('Conceito D')
    elif 4.0 <= nota <= 4.9:
        print('Conceito E')
    elif 0.0 <= nota <= 3.9:
        print('Conceito E')
elif falta <= 20:
    if 9.0 <= nota <= 10.0:
        print('Conceito A')
    elif 7.5 <= nota <= 8.9:
        print('Conceito B')
    elif 5.0 <= nota <= 7.4:
        print('Conceito C')
    elif 4.0 <= nota <= 4.9:
        print('Conceito D')
    elif 0.0 <= nota <= 3.9:
        print('Conceito E')
