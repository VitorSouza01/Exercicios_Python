"""
01. Faça um programa que receba dois números e mostre qual deles é o maior.
"""

print('- Descubra qual número é o maior!')

nmr1 = float(input('\nDigite o valor do 1º número >'))
nmr2 = float(input('Digite o valor do 2º número >'))

if nmr1 > nmr2:
    print(f'\n[{nmr1}] é o número maior!')
else:
    print(f'\n[{nmr2}] é o número maior!')
