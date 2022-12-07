#Faça um programa que calcule e escreva o valor de S
#S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50

impar = list()
num = list()
res = 0
s = {}
for n in range(1, 101):
    if n % 2 != 0:
        impar.append(n)

for n in range(1, 51):
    num.append(n)
print(len(impar))
print(len(num))
print(impar)
print(num)

for n in impar:
    for item in num:
        s[n] = item

for c, v in s:
    res += c / v
print(res)
