"""
51. Escreva um programa que leia as coordenadas 'x' e 'y' de pontos no R2 e
calcule sua distâncio de origem (0,0).
"""

print (' - Descubra a distância das coordenadas A e B - ')
Xa = int(input('Digite o valor de x de A:'))
Ya = int(input('Digite o valor de y de A:'))
Xb = int(input('Digite o valor de x de B:'))
Yb = int(input('Digite o valor de y de B:'))

distancia = (((Xb - Xa)**2) + ((Yb - Ya)**2)) ** 0.5

print(f'\nA distâncio entre os pontos A({Xa},{Ya}) e B({Xb},{Yb}) é de; [{distancia}].')



