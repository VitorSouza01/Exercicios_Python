""""
39. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
sabendo que ele recebeu um aumento de 25%.
"""

print('- Aumento do Salário do Funcionário em 25%.')
salario = float(input('\nDigite o valor do salário do funcionário:'))

aumento = ((25/100) + 1) * salario

print(f'\nO valor do novo salário do funcionario com o aumento de 25% é [{aumento}].')

