"""
29. Leia quatro notas, calcule a média aritmética e imprima o resultado.
"""
print('--- DESCUBRA A MÉDIA ARITMÉTICA! ---')
print('\nDigite Cada Nota dos 4º Bimestres.')

nt1 = float(input('*Nota do 1º Bimestre:'))
nt2 = float(input('*Nota do 2º Bimestre:'))
nt3 = float(input('*Nota do 3º Bimestre:'))
nt4 = float(input('*Nota do 4º Bimestre:'))

med_arit = (nt1 + nt2 + nt3 + nt4) / 4

print(f'\nA Média aritmética das suas notas é [{med_arit}].')