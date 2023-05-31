""""
7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0 * (F - 32.0)/9.0, sendo C a temperatura em Celsius e
F a temperatura em Fahrenheit.
"""

print('Conversor de Temperatura entre Fahrenheit para Celsius.\n')
f = float(input('Digite a temperatura em Fahrenheit (ºF):'))

c = (5.0 * (f - 32.0) / 9.0)

print('\n[Conversão]')
print(f'O valor Fahrenheit de {f}ºF convertido para Celsius é {c}ºC.')
