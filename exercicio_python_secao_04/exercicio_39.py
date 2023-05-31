"""
39. A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantial total:
    * O primeiro ganhador receberá 46%.
    * O segundo receberá 32%.
    * O terceiro receberá o restante.
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

print(' - Um prêmio de R$ 780.000,00 vai será dividida entre três pessoas;')
print('*O Primeiro ganhador receberá 46%.')
print('*O Segundo ganhador receberá 32%.')
print('*O Terceiro ganhador receberá o restante.')

vlr1 = (46 * 780000) / 100
vlr2 = (36 * 780000) / 100
vlr3 = 780000 - (vlr1 + vlr2)

print('\n[]Cada ganhador irá receber;')
print(f'O Primeiro R$[{vlr1}].')
print(f'O Segundo R$[{vlr2}].')
print(f'O Terceiro R$[{vlr3}].')

