#Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores que 100. Escolha
# números aleatórios entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b, onde a e b são os número
# aleatórios. Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas,
# além de quantas vezes o aluno acertou

from random import randint
acerto = 0
pergunta_certa = list()
resposta_certa = list()

for n in range(5):
    a = randint(0, 100)
    b = randint(0, 100)
    pergunta = print(f'Qual a soma de {a} + {b}?')
    resposta = int(input(f'{a} + {b} = '))
    if resposta == a + b:
        acerto += 1
        pergunta_certa.append(f'{a} + {b} = {resposta}')

print(f'Das 5 perguntas o aluno acertou {acerto}:\n'
      f'{pergunta_certa}')