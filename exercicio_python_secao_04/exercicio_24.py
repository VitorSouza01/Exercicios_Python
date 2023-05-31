"""
24. Leia um valor de área em metros quadrados m2 e apresente-o
convertido em acres.
A fórmula de conversão é: A = M * 0,000247, sendo M a área em
metros quadrados e A a área em acres.
"""

print('\n')
print('--- Informe um valor de área em Metros Quadrado ---')
m = float(input('*Digite aqui:'))

a = m * 0.000247

print('\n--- Valor convertido da área em Metros Quadrado'
      'para Acres; ---')
print(f'[{a}]')
