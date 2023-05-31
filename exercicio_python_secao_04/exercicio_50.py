"""
50. Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de
sua idade e do ano atual.
"""

print('- Descubra o Ano de Nascimento!')

idade = int(input('\n*Digite a idade que você quer descobrir o ano de nascimento:'))
ano = int(input('*Digite o ano atual:'))

nascimento = ano - idade

print(f'\n- O ano de nascimento de quem tem {idade} anos em {ano} é [{nascimento}].')
