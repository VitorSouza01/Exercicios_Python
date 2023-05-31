"""
17. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = ((basemaior)+(basemenor)*altura)/2
Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""
print('* DESCUBRA A ÁREA DE UM TRAPÉZIO.')

basemaior = float(input('\nDigite o valor da base maior:'))
basemenor = float(input('Digite o valor da base menor:'))
altura = float(input('Digite o valor da altura:'))

if basemaior >0 and basemenor > 0:
    area = ((basemaior+basemenor)*altura)/2
    print(f'\nA área do trapézio é: [{area}]cm.')
else:
    print('\nO valor da base maior e base menor, tem que ser números maiores que zero!')
