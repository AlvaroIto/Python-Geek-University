#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para
# posentadoria são:
# - Ter pelo menos 65 anos
# - Ou ter trabalhadado pelo menos 30 anos
# - ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

idade = int(input('Digite a idade: '))
trabalho = int(input('Digite o tempo trabalhado em anos: '))

if idade > 65:
    print(f'Pode se aposentar. Idade: {idade} anos')
elif trabalho > 30:
    print(f'Pode se aposentar. Tempo de trabalho {trabalho} anos')
elif idade > 60 and trabalho > 25:
    print(f'Pode se aposentar. Idade {idade} anos e tempo de trabalho {trabalho} anos')
else:
    print('Não pode se aposentar!')
