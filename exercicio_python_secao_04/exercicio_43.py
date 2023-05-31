""""
43. Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
    * O tatal a pagar com desconto de 10%.
    * O valor de cada parcela, no parcelamento de 3x sem juros.
    * A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
    * A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""

print(' [ TABELA DE PREÇO DE VENDAS ]')
valor_produto = float(input(' [] Digite o valor do produto:'))

vlr_desconto = valor_produto - ((valor_produto / 100) * 10)
vlr_parcela = valor_produto / 3
vlr_comisao_avista = (vlr_desconto / 100) * 5
vlr_comisao_parcela = (valor_produto / 100) * 5

print(f'\n [] O valor do produto com de desconto de 10% é: ({vlr_desconto}).')
print(f' [] O valor das parcelas do produto em 3x é: ({vlr_parcela}).')
print(f' [] A comisão do vendedor caso a venda seja a vista é: ({vlr_comisao_avista}).')
print(f' [] A comisão do vendedor caso a venda seja parcelada é: ({vlr_comisao_parcela}).')
