"""
18. Faça um programa que mostre ao usuário um meno com 4 opções de operações
matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o
seu programa então pede dois valores númericos e realiza a operação,
mostrando o resultado e saindo.
"""

print('[ CALCULADORA BÁSICA ]')
print('[+ = soma][- = subtração][/ = divisão][* = multiplicação]')

numero1 = float(input('\n-Digite um valor do primeiro número:'))
operador = str(input('-Digite um operador:'))
numero2 = float(input('-Digite um valor do segundo número:'))

if operador == '+':
    print('\n[RESULTADO:]')
    print(f'[{numero1} {operador} {numero2} = {numero1+numero2}]')
elif operador == '-':
    print('\n[RESULTADO:]')
    print(f'[{numero1} {operador} {numero2} = {numero1-numero2}]')
elif operador == '/':
    print('\n[RESULTADO:]')
    print(f'[{numero1} {operador} {numero2} = {numero1/numero2}]')
elif operador == '*':
    print('\n[RESULTADO:]')
    print(f'[{numero1} {operador} {numero2} = {numero1*numero2}]')
else:
    print(f'\n* O operador está inválido!')
