"""
37. Faça um programa que leia o valor de um produto e imprima o valor com desconto,
tendo em vista que o desconto foi de 12%.
"""

print('( DESCUBRA O VALOR DO DESCONTO )')
print('O Desconto aplicado no valor do produto é de 12%!')

vlr_pdt = float(input('\nDigite o valor do produto:'))

dsct = (vlr_pdt / 100) * 12
vlr_dsct = vlr_pdt - dsct

print(f'\nO Valor do Desconto de 12% no valor de {vlr_pdt} é ({dsct}).')
print(f'O valor final do Produto com o Desconto aplicado é de [{vlr_dsct}].')

