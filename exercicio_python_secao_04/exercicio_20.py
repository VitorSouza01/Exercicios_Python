"""
20. Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é: L = K/0,45, sendo K a massa em quilogramas e L a
massa em libras.
"""

print('CONVERSÃO DE VALOR DE MASSA EM QUILOGRAMAS PARA LIBRAS')
k = float(input('Digite o valor de Massa em Quilogramas:'))

l = k / 0.45

print('\nCONVERSÃO...')
print(f'O valor de Massa em Quilogramas [{k}], convertido para Massa em Libras é [{l}]')
