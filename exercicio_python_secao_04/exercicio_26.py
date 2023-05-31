"""
26. Leia um valor de área em metros quadrados m2 e apresente-o
convertidos em hectares.
A fórmula de conversão é: H = M * 0.0001, sendo M a área em metro
quadrados e H a área em hectares.
"""

print('\n')
print(' [ CONVERSOR DE ÁREA EM METROS ] ')
print('--- Informe um valor de área em Metros Quadrado! ---')
m = float(input('Digite aqui:'))

h = m * 0.0001

print('\n--- Valor convertido da área em Metros Quadrados'
      'para Hectares é: ---')
print(f'[{h}]')

