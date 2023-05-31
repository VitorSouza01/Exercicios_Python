"""
30. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.
"""

print(' - CONVERSÃO DE MOEDA - ')
print('\n* Conversão do valor da moeda em real para dolar!')
vlr_rl = float(input('.Digite um valor em real:'))

vlr_dlr = vlr_rl * 4.90

print(f'\n= Valor em Real: [ R${vlr_rl} ]')
print(f'= Valor em Dólar: [ US${vlr_dlr} ]')
