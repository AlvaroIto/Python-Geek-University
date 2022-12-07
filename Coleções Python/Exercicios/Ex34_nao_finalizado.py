#Faça um programa par ler 10 números DIFERENTES a serem armazenados em um vetor. Os dados deverão ser armazenados no
# vetor na ordem que forem sendo lidos, sendo que caso o usuário digite um número que já foi digitado anteriormente, o
# programa deverá pedir para ele digitar outro número. Note que cada valor digitado pelo usuário deve ser pesquisado no
# vetor, verificando se ele existe entre os número que já foram fornecidos. Exibir na tela o vetor final que foi digitado

vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
'''
for n in range(10):
    num = int(input(f'Digite o {n+1}º valor: '))
    if len(vetor) == 0:
        vetor.append(num)
    else:
        while i < len(vetor):
            if num == vetor[i]:
'''

while True:
    for n in range(10):
        num = int(input(f'Digite o {n+1}º valor: '))
        if vetor[0] == 0:
            vetor.append(num)
        else:
            while i < len(vetor):
                if num == vetor[i]:
                    print('Número já existente no vetor, digite outro número.')
                    #num = int(input(f'Digite o {n + 1}º valor: '))
                    i += 1
                else:
                    vetor.append(num)
            break
