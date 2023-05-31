"""
41. Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado.
"""
print(' - Valor a receber de trabalho no mês!')

valor = float(input('\nQual valor cobrado por hora de trabalho:'))
hora = int(input('Quantas horas de trabalho por dia:'))

valor_diario = valor * hora
horas_mensal = hora * 20
valor_mensal = ((10/100) + 1) * (valor_diario * 20)

print(f'\nVocê trabalhou por {horas_mensal} horas nesse mês, e está recebendo o valor de R$[{valor_mensal}].')
print('*Um aumento de 10% foi aplicado sobre o recebimento.')





