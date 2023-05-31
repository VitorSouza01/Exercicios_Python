"""
24. Uma empresa vende o mesmo produto para quatro diferentes estados.
Cada estado possui uma taxa diferente de impostos sobre o produto
(MG 7%, SP 12%, RJ 15%, MS 8%).
Faça um programa em que o usuário entre com o valor e o estado destino do
produto e o programa retorne o preço final do produto acrescido do imposto
do estado em que ele será vendido.
Se o estado digitado não for válido, mostrar uma mensagem de erro.
"""

print('[ - DESCUBRA O VALOR DO PRODUTO COM O IMPOSTO DO ESTADO -]')
print('[ VALOR DO IMPOSTO APLICADO EM CADA ESTADO; ]')
print('[ MG: 7% ] [ SP: 12% ] [ RJ: 15% ] [ MS: 8% ]')

produto = str(input('\nInforme o produto vendido:'))
valor_produto = float(input('Informe o valor do produto vendido:'))
estado = str(input('Informe o estado que irá receber o produto:'))

if estado == 'MG' or estado == 'Mg' or estado == 'mg' or estado == 'MINAS GERIAS' or estado == 'Minas Gerais' or \
        estado == 'minas gerais':
    print(f'\n-O preço final da(o) [{produto}] para venda, acrescido ao imposto do estado de {estado} será:'
          f'[R${((7/100)+1) * valor_produto}].')

elif estado == 'SP' or estado == 'Sp' or estado == 'sp' or estado == 'SÃO PAULO' or estado == 'São Paulo' or \
        estado == 'são paulo':
    print(f'\n-O preço final da(o) [{produto}] para venda, acrescido ao imposto do estado de {estado} será:'
          f'[R${(((12/100)+1) * valor_produto)}].')

elif estado == 'RJ' or estado == 'Rj' or estado == 'rj' or estado == 'RIO DE JANEIRO' or estado == 'Rio de Janeiro' or \
        estado == 'rio de janeiro':
    print(f'\n-O preço final da(o) [{produto}] para venda, acrescido ao imposto do estado de {estado} será:'
          f'[R${((15/100)+1) * valor_produto}].')

elif estado == 'MS' or estado == 'Ms' or estado == 'ms' or estado == 'MATO GROSSO DO SUL' or \
        estado == 'Mato Grosso do Sul' or estado == 'mato grosso do sul':
    print(f'\n-O preço final da(o) [{produto}] para venda, acrescido ao imposto do estado de {estado} será:'
          f'[R${((8/100)+1) * valor_produto}].')

else:
    print(f'\n[Erro!] O Estado informado não é válido!')
