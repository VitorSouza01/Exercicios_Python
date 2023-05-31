"""
25. Leia um valor de área em acres e apresente-o convertido em
metros quadrados m2.
A fórmula de conversão é: M = A * 4048,58, sendo M a área em metros
quadrados e A a área em acres.
"""

print('\n')
print('--- Informe um valor de área em Acres! ---')
a = float(input('*Digite aqui:'))

m = a * 4048.58

print('\n--- Valor convertido da área em Acres para'
      'Metros Quadrados; ---')
print(f'[{m}]')
