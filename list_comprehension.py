'''

Serve para gerar nova lista com dados processados a partir de outro iterável
sintaxe:
[dado for dado in iterável]

Exemplo:
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)

onde dividimos a leitura em:

1- for numero in numeros
2- numero * 10
      (-----2-----)(----------1---------)
res = [numero * 10 for numero in numeros]



Podemos adicionar estruturas condicionais lógicas

numeros = [1, 2, 3, 4, 5]

Exemplo 1:
pares = [numero for numero in numeros if  numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

Exemplo 2:
res = [numero * 2 if numero % 2  == 0 else numero / 2 for numero in numeros]

'''

