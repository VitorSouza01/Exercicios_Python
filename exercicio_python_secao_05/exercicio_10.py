"""
10. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre
seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
*homens: (72.7 * h) - 58
*mulheres: (62.1 * h) - 44.7
"""

print('-Descubra o seu peso ideal!')

sexo = str(input('\nQual é o seu sexo?(Homem ou Mulher)'))
altura = float(input('Qual é a sua altura?'))

homem1  = str('Homem')
homem2 = str('homem')
mulher1 = str('Mulher')
mulher2 = str('mulher')

if sexo == homem1:
    print(f'\nO seu peso ideal é: [{(72.7 * altura) - 58}].')
elif sexo == homem2:
    print(f'\nO seu peso ideal é: [{(72.7 * altura) - 58}].')
elif sexo == mulher1:
    print(f'\nO seu peso ideal é: [{(62.1 * altura) - 44.7}].')
elif sexo == mulher2:
    print(f'\nO seu peso ideal é: [{(62.1 * altura) - 44.7}].')
else:
    print('\nSexo não Reconhecido!')


