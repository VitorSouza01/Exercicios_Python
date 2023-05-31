"""
04. Faça um programa que leia um número, e caso ele seja positivo, calcule e mostre:
    * O número digitado ao quadrado.
    *A raiz quadrada do número digitado.
"""

print('.Descubra o valor ao quadrado e a raiz quadrada de um número positivo.')
nmr = float(input('\nDigite o valor de um número:'))

if nmr > 0:
    print(f'\nO número ao quadrado de {nmr} é: [{nmr * nmr}]. ')
    print(f'A raiz quadrada de {nmr} é: [{(nmr ** 0.5)}].')
else:
    print('\nO número é invalido, ele é negativo!')
