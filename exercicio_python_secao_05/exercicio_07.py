""""
07. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem de 'Números iguais'
"""

print('* Descubra qual é o número maior *')

nmr1 = int(input('\nDigite o valor do 1º número:'))
nmr2 = int(input('Digite o valor do 2º número:'))

if nmr1 > nmr2:
    print(f'\n{nmr1} é maior que {nmr2}, a diferença entre eles é de: [{(nmr1-nmr2)}].')
elif nmr1 == nmr2:
    print(f'\n{nmr1} e {nmr2} são números iguais.')
else:
    print(f'\n{nmr2} é maior que {nmr1}, a diferença entre eles é de: [{(nmr2 - nmr1)}].')
