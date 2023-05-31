"""
12. Ler um número inteiro. Se o número lido for negativo, escreva a mensagem
"Número inválido". Se o número for positivo, calcular o logaritmo deste número.
"""
print('- CALCULE O LOGARITMO DE UM NÚMERO POSITIVO!')
numero = float(input('-Digite um número positivo:'))

import math

if numero > 0:
    print(f'\nO logaritmo de {numero} é: [{math.log10(numero)}]')
else:
    print('\nNúmero Inválido!')
