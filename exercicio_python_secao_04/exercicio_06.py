"""
6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A formula da conversão é: F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
"""

print('Conversor de Temperatura entre Celsius para Fahrenheit.\n')
c = float(input('Digite a temperatura em Celsius (ºC):'))

f = c * (9.0/5.0) + 32.0

print('\n[Conversão]')
print(f'O valor Celsius de {c}ºC convertido para Fahrenheit é {f}ºF.')
