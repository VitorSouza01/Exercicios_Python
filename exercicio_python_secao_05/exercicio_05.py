"""
05. Faça um programa que receba um número inteiro e verifique se este número
é par ou ímpar.
"""

print('* Descubra se o número é Par ou Ímpar *')
numero = float(input('Digite um número:'))
valor_final = numero % 2

if valor_final == 0:
    print(f'\n[{numero}] é um número Par!')
else:
    print(f'\n[{numero}] é um número Ímpar!')
