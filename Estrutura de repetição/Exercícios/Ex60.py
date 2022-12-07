#Faça um programa que leia vários números, calcule o mostre:
#(a) A soma dos números digitados
#(b) A quantidade de números digitados
#(c) A média dos números digitados
#(d) O maior número digitado
#(e) O menor número digitado
#(f) A média dos números pares
#Finalize a entrada de dados caso o usuário informe o valor 0

numeros = list()
pares = list()
maior = menor = cont = soma = soma_par = 0
#loop para ler vários números
while True:
    num = int(input('Digite um número ou 0 para sair: '))
    cont += 1
    if num == 0:
        break
    else:
        soma += num
        numeros.append(num)
        media = soma / len(numeros)

        #verificar o maior e menor número digitado
        if cont == 1:
            maior = menor = 1
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num

        #números pares
        if num % 2 == 0:
            soma_par += num
            pares.append(num)
            media_pares = soma_par / len(pares)

print(f'A soma dos {len(numeros)} digitados é: {soma}')
print(f'Foram digitados {len(numeros)} números')
print(f'A média dos números digitados é: {media}')
print(f'O maior número digitado foi: {maior}')
print(f'O menor número digitado foi: {menor}')
print(f'A média dos números pares é: {media_pares}')
