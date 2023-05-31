"""
13. Leia uma distância em quilômetros e apresente-a convertida em milhas.
A fórmula de conversão é: M = (K/1,61), sendo K a distância em quilômetros e M em milhas.
"""

print('[ Conversor de Distância em Quilômetros para Milhas. ]\n')
k = float(input('Digite a o valor da distância em Quilômetros:'))

m = k / 1.61

print('\n[ Conversão da Distância... ]')
print(f'O valor da distância em Quilômetros [{k}] convertido para Milhas é [{m}].')

