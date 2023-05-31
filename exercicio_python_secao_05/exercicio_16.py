"""
16. Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima
o mês correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.
"""

print(' [ DESCUBRA O MÊS ! ] ')
mes = int(input('Digite um número correspondente a um mês:'))

if mes == 1:
    print(f'\n* O número {mes} representa o mês de: [Janeiro].')
elif mes == 2:
    print(f'\n* O número {mes} representa o mês de: [Fevereiro].')
elif mes == 3:
    print(f'\n* O número {mes} representa o mês de: [Março].')
elif mes == 4:
    print(f'\n* O número {mes} representa o mês de: [Abril].')
elif mes == 5:
    print(f'\n* O número {mes} representa o mês de: [Maio].')
elif mes == 6:
    print(f'\n* O número {mes} representa o mês de: [Junho].')
elif mes == 7:
    print(f'\n* O número {mes} representa o mês de: [Julho].')
elif mes == 8:
    print(f'\n* O número {mes} representa o mês de: [Agosto].')
elif mes == 9:
    print(f'\n* O número {mes} representa o mês de: [Setembro].')
elif mes == 10:
    print(f'\n* O número {mes} representa o mês de: [Outubro].')
elif mes == 11:
    print(f'\n* O número {mes} representa o mês de: [Novembro].')
elif mes == 12:
    print(f'\n* O número {mes} representa o mês de: [Dezembro].')
else:
    print(f'\n* O valor do número está inválido!')
