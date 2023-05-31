"""
36. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
O volume de um cilindro circular é calculado por meio da seguinte fórmula:
V = 𝝿 * raio2 * altura, onde 𝝿 = 3.141592.
"""

print('( DESCUBRA O VOLUME DE UM CILINDRO CIRCULAR )')
altura = float(input('\nDigite o valor da Altura do cilindro:'))
raio = float(input('Digite o valor do Raio do cilindro'))

volume = 3.14 * ((raio ** 2) * altura)

print(f'\nO valor do Volume do cilindro circular é [{volume}]')

