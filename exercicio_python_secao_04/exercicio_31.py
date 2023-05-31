"""
31. Leia um número inteiro e imprima o se antecessor e o seu sucessor.
"""

print('- Saiba qual é o número antecessor e o sucessor escolhido!')
vlr_nmr = int(input('Escolha um número:'))

vlr_ant = vlr_nmr - 1
vlr_scs = vlr_nmr + 1

print(f'\n* O valor Antecessor de {vlr_nmr} é [{vlr_ant}].')
print(f'* O valor Sucessor de {vlr_nmr} é [{vlr_scs}].')
