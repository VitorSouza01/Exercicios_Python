""""
48. Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""

print('- Transforme um valor inteiro de Segundos em Horas, Minutos e Segundos!')
entrada = int(input('Digite um valor inteiro em segundos:'))

horas = entrada // 3600
minutos = str(entrada // 60)
segundos = entrada % 60

print(f'\nO valor convertido é: [{horas}:{minutos[0:2]}:{segundos}].')
print(f'Horas [{horas}].')
print(f'Minutos [{minutos[0:2]}].')
print(f'Segundos [{segundos}].')



