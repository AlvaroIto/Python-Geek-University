#Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula de conversão é:  M = 0.91 * J
#sendo J o comprimento em Jardas e M o comprimento em metros

jd = float(input('Digite o comprimento em jardas: '))
mt = 0.91 * jd
print(f'O comprimento {jd}jd convertido em metros é: {mt}mts')
