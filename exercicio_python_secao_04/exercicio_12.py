"""
12. Leia uma distância em milhas e apresente-a convertida em quilômetros.
A formula de conversão é: K = 1,61 * M, sendo K a distância em quilômetros e M em milhas.
"""

print('[ Conversor de Distância em Milhas para Quilômetros. ]\n')
m = float(input('Digite a o valor da distância em Milhas:'))

k = 1.61 * m

print('\n[ Conversão da Distância ]')
print(f'O valor da distância em Milhas [{m}] convertido para Quilômetros é [{k}].')

