"""
23. Leia um valor de comprimento em metros e apresente-o convertido
em Jardas.
A fórmula de convevrsão é: J = M/0,91, sendo J o comprimento em Jardas
e o M o comprimento em Metros.
"""

print('CONVERSÃO DO VALOR DE COMPRIMENTO EM METROS PARA JARDAS')
m = float(input('Digite o valor de Comprimento em Metros:'))

j = m / 0.91

print('\nCONVERSÃO...')
print(f'O valor do comprimento em Metros de [{m}], convertido'
      f'em Jardas é [{j}]')
