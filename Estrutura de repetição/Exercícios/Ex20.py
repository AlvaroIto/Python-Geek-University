#Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de dados
# lidos e número de valores pares. O processo termina quando for digitado o número 1000
par = list()
num = 0
quant = int(input('Digite a quantidade de dados: '))
for n in range(quant):
    if num == 1000:
        print('Foi digitado o número 1000 para parar o processo')
        break
    else:
        num = int(input(f'Digite o {n+1}º número: '))
        n += 1
        if num % 2 == 0 and num != 1000:
            par.append(num)
print(f'Foi solicitado {quant} dados e os números pares são: {par}')



