"""
23. Determine se um determinado ano lido é bissexto.
Sendo que um ano é bissextp se for divisível por 400 ou se for divisível por 4 e não for divisível por 100.
Pro exemplo;
1988, 1992, 1996.
"""

print('[ DESCUBRA SE O ANO É BISSEXTO ]')
ano = int(input('- Digite um ano:'))

if (ano % 400 == 0) or (ano % 4 == 0) is not (ano % 100 == 0):
    print(f'\n{ano} é um ano Bissexto!')
else:
    print(f'\n{ano} não é um ano Bissexto!')
