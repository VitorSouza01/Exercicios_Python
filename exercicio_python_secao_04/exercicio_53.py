"""
53. Faça um programa para ler as dimensões de um terreno (comprimento 'c' e largura 'l'),
bem como o preço do metro da tela 'p'. Imprima o custo para cercar este mesmo terreno com
tela.
"""

print('Descubra o custo para cercar um terreno com tela!')

c = float(input('\nDigite o comprimento do terreno:'))
l = float(input('Digite a largura do terreno:'))
a = float(input('Digite o preço do metro do arame R$:'))

p = c*l*a

print(f'\nO custo para cercar o terreno é de R${p}.')
