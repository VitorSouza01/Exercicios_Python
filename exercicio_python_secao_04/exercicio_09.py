"""
9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
A fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
"""

print('[ Conversor de Temperatura entre Celsius para Kelvin. ]\n')
c = float(input('Digite a temperatura no valor em Celsius (ºC):'))

k = c + 273.15

print('\n[ Conversão ]')
print(f'O valor da temperatura Celsius de {c}ºC, convertido para Kelvin é {k}ºK.')

