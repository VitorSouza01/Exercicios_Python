"""
35. Sejam 'A' e 'B' os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
Hipotenusa = √a2 + b2. Faça um programa que receba os valores de 'A' e 'B' e calcule o
valor da hipotenusa através da equação. Imprima o resultado dessa operação.
"""

print('DESCUBRA O VALOR DA HÍPOTENUSA')
vlr_a = float(input('- Digite o Valor de A:'))
vlr_b = float(input('- Digite o Valor de B:'))

hptns = ((vlr_a ** 2) + (vlr_b ** 2)) ** 0.5

print(f'\nO Valor da Hípotenusa é [{hptns}]')


