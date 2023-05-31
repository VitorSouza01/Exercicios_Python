"""
11. Leia uma velocidade em M/s (metros por segundo) e apresente-a convertida em Km/h (quilometros por hora).
A fórmula de conversão é: K = M * 3.6, sendo K a velocidade em Km/h e M em M/s.
"""

print('[ Conversor de Velocidade em M/s (metros por segundo) para Km/h (quilometros por hora). ]\n')
m = float(input('Digite a o valor da velocidade em M/s (metros por segundo):'))

k = m * 3.6

print('\n[ Conversão da Velocidade ]')
print(f'O valor da velocidade de M/s {m} convertido para Km/h é {k}.')