"""
06. Escreva um programa que, dados dois números inteiros, mostre na tela o maior
deles, assim como a diferença existente entre ambos.
"""

print('* Descubra qual é o número maior *')

nmr1 = int(input('\nDigite o valor do 1º número:'))
nmr2 = int(input('Digite o valor do 2º número:'))

if nmr1 > nmr2:
    print(f'\n{nmr1} é maior que {nmr2}, a diferença entre eles é de: [{(nmr1-nmr2)}].')
else:
    print(f'\n{nmr2} é maior que {nmr1}, a diferença entre eles é de: [{(nmr2 - nmr1)}].')
