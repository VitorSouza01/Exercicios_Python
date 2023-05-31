"""
19. Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m3.
A fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em
Metros Cúbicos.
"""

print('[ CONVERSÃO DE VALOR DE VOLUME EM LITROS PARA METROS CÚBICOS]')
l = float(input('Digite o valor de volume em Litros:'))

m = l / 1000

print('\nCONVERSÃO...')
print(f'O valor do volume em Litros [{l}], convertido para Metros Cúbicos é [{m}]')
