"""
15. Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de conversão é: G = R * 180/π, sendo G o ângulo em graus e R em radianos e π = 3,14.
"""

print('*** CONVERSÃO DE ÂNGULO EM RADIANOS PARA GRAUS ***')
r = float(input('Digite o valor do ângulo em radianos:'))

g = r * 180/3.14

print('\n*** CONVERSÃO... ***]')
print(f'O valor do ângulo em radianos {r}º, convertido em graus é {g}º.')
