'''

open() -> abre arquivos
arquivo = open('texto.txt')
print(arquivo)

read() -> ler arquivo
print(arquivo.read())

#forma 'certa' de abrir arquivos:
with open('texto'.txt) as arquivo:
    print(arquivo.realines())

seek() -> serve para movimentar o cursor pelo arquivo
arquivo.seek(0)
print(arquivo.read())

readline() -> função que lê o arquivo linha por linha
print(arquivo.realine())

readlines() -> coloca todas as linhas do arquivo em uma lista. Cada linha sendo um item da lista
print(arquivo.realines())

closed() -> verificcar se o arquivo está aberto ou fechado. Retornando um valor booleano
print(arquivo.closed())

close() -> fechar arquivos

escrever em arquivos:
with open('novo_texto.txt', 'w') as arquivo:
    arquivo.write('Escrever dados rm arquivo é muito fácil.\n')
    arquivo.write('Podemos colcoar quantas linhas quisermos.\n')
    arquivo.write('Esta é a ultima linha.\n')

Modos de ABertura de Arquivos:

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera erro
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo




'''

import os
import sys

print(os.name)

print(sys.platform)
