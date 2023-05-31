"""
42. Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se
que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga
7% de imposto sobre o salário-base.
"""

print(' - Valor total Salarial! - ')
salario_base = float(input('Digite o seu salário-base:'))
print('*Obs: 5% de aumento de gratificação')
print('Obs: 7% de desconto de imposto.')

gratificacao = ((5/100) + 1) * salario_base
imposto = (gratificacao / 100) * 7
imposto_aplicado = gratificacao - imposto

print(f'\nO Salário á receber é [{imposto_aplicado}].')


