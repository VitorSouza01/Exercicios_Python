"""
09. Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
Se a prestação for maior que 20% do salário imprima: 'Empréstimo não concedido'
caso contrário imprima: 'Empréstimo concedido'.
"""

print(' LIBERAÇÃO DE EMPRÉSTIMO ')

salario = float(input('\nDigite o seu salário:'))
prestacao = float(input('Digite o valor da prestação do empréstimo:'))

operacao = ((prestacao - salario) / salario) * 100

if operacao > 20:
    print('\nEmpréstimo Não Concedido!')
else:
    print('\nEmpréstimo Concedido')
