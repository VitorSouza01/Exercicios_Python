"""
10. Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = k/3.6, sendo K a velocidade em
km/h e M em m/s.
"""

print('[ Conversor de Velocidade em Km/h (quilometros por hora) para M/s (metros por segundo). ]\n')
k = float(input('Digite a o valor da velocidade em Km/h (quilometros por hora):'))

m = k / 3.6

print('\n[ Conversão da Velocidade ]')
print(f'O valor da velocidade de Km/h {k} convertido para M/s é {m}.')
