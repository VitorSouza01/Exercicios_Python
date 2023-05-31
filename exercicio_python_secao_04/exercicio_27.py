"""
27. Leia um valor de área em hectares e apresente-o convertido
em metros quadrados m2.
A fórmula de conversão é: M = H * 10000, sendo M a área em metros
quadrados e H e a área em hectares.
"""

print('\n')
print(' [ CONVERSOR DE ÁREA EM METROS ] ')
print('--- Informe um valor de área em Hectares! ---')
h = float(input('*Digite aqui:'))

m = h * 10000

print('\n--- Valor convertido da área em Hectares'
      'para Metros Quadrados é: ---')
print(f'[{m}]')
