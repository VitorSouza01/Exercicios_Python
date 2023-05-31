"""
22. Leia um valor de comprimento em Jardas e apresente-o convertido
em Metros.
A fórmumla de conversão é: M = 0,91 * J, sendo J o comprimento em
Jardas e M o comprimento em metros.
"""

print('CONVERSÃO DO VALOR DE COMPRIMENTO EM JARDAS PARA METROS')
j = float(input('Digite o valor de Comprimento em Jardas:'))

m = 0.91 * j

print('\nCONVERSÃO...')
print(f'O valor do comprimento em Jardas de [{j}], convertido para'
      f'comprimento em Metros é [{m}].')
