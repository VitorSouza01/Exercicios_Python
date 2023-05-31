"""
28. Faça a leitura de três valores e apresente como resultado a
soma dos quadrados dos três valores lidos.
"""

print('--- Digite Três Valores! ---')
vlr1 = float(input('Valor 1:'))
vlr2 = float(input('Valor 2:'))
vlr3 = float(input('Valor 3:'))

qdd_vlr1 = vlr1 * vlr1
qdd_vlr2 = vlr2 * vlr2
qdd_vlr3 = vlr3 * vlr3

sm_qdd = qdd_vlr1 + qdd_vlr2 + qdd_vlr3

print(f'\nO Quadrado dos seguintes valores são: Valor1 [{qdd_vlr1}], Valor2 [{qdd_vlr2}], Valor3 [{qdd_vlr3}]')
print(f'A Soma dos Quadrados dos três valores são [{sm_qdd}]')


