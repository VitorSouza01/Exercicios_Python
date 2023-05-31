"""
32. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""
print('- Saiba qual é a soma do sucessor de seu triplo com o antecessor de seu dobro!')
vlr_nmr = int(input('Escolha um número:'))

vlr_ant = (vlr_nmr * 2) - 1
vlr_scs = (vlr_nmr * 3) + 1
soma = vlr_ant + vlr_scs

print(f'\n* O Antecessor do Dobro de {vlr_nmr} é [{vlr_ant}].')
print(f'* O Sucessor do Triplo de {vlr_nmr} é [{vlr_scs}].')
print(f'A Soma do Sucessor de seu Triplo {vlr_scs} com o Antecessor do seu Dobro {vlr_ant} é [{soma}].')
