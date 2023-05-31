"""
44. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo as escadas. Calcule e mostre quantos degraus o usuário deverá subir para
atingir seu objetivo.
"""

print('+ CALCULE A QUANTIDADE DE DEGRAU PARA SUBIR + ')
altura_degrau = float(input('Qual é a altura do degrau da escada(Cm)?'))
altura_alcancar = float(input('Qual é a altura que você deseja alcançar(Cm)?'))

quantidade_degrau = altura_alcancar / altura_degrau

print(f'\n Você precisará subir [{quantidade_degrau}] degraus para alcançar seu objetivo.')

