#Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada; Calcule e mostre
#quantos degraus o usuário deverá subir para atingir o objetivo

alt_degrau = int(input('Digite a altura do degrau(cm): '))
alt = int(input('Digite a altura que deseja alcançar(cm): '))
degrau = alt // alt_degrau
print(f'Cada degrau tem {alt_degrau}cm e para alcançar a altura de {alt}cm serão necessários {degrau} degraus')
