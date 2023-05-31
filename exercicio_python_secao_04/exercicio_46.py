""""
46. Faça um programa que leia um número inteiro positivo de três dígitos ( de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido.
Exemplo:

[Número Lido:   123]
[Número Gerado: 321]
"""
print('- Escreva um número inteiro positivo de três dígitos (De 100 a 999)!')
numero = input('.Digite o número:')
numero_natural = int(numero)
numero_invertido = str(numero[::-1])


if numero_natural < 100:
    print('\nDigite um número válido entre 100 e 999.')
elif numero_natural <= 999:
    print(f'\nSeu número inteiro invertido é [{numero_invertido}].')
else:
    print('\nDigite um número válido entre 100 e 999.')




