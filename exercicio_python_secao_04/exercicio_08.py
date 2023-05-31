"""
8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = K - 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
"""

print('[ Conversor de Temperatura entre Kelvin para Celsius. ]\n')
k = float(input('Digite a temperatura no valor em Kelvin (ºK):'))

c = k - 273.15

print('\n[ Conversão ]')
print(f'O valor da temperatura Kelvin de {k}ºK, convertido para Celsius é {c}ºC.')

