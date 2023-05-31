"""
08. Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor
entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser
informado ao usuário e o programa termina.
"""

print('Verificação de Notas.')

nota1 = float(input('\nDigite o valor da 1º nota:'))
nota2 = float(input('Digite o valor da 2º nota:'))

media = (nota1 + nota2) / 2

if media > 5:
    print(f'\nSuas notas são válidas, sua média é: [{media}].')
else:
    print(f'\nSuas notas são inválidas, sua média é: [{media}]. ')
