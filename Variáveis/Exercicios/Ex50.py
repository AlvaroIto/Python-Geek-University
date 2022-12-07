#Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual
import datetime
idade = int(input('Digite sua idade: '))
atual = datetime.datetime.now().year
ano = atual - idade
print(f'Você nasceu no ano: {ano}')
