"""
17. Leia um valor do comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = (C/2,54), sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""

print('*** CONVERSÃO DE COMPRIMENTO EM CENTÍMETROS PARA POLEGADAS ***')
c = float(input('Digite um valor de comprimento em centímetros:'))

p = c / 2.54

print('\nCONVERSÃO...')
print(f'O valor do comprimento em Centímetros {c}, para Polegadas é: {p}')

