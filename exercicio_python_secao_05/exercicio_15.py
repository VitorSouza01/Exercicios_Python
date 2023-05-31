""""
15. Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima
o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira
se 2, e assim por diante.
"""

print(' - Descubra O Dia Da Semana! - ')
print('\n- Digite um valor correspondente ao dia da semana de 1 até 7;')
dia = int(input('Digite aqui:'))

if dia == 1:
    print(f'\n*O número {dia} representa o dia de: [Domingo].')
elif dia == 2:
    print(f'\n*O número {dia} representa o dia de: [Segunda-Feira].')
elif dia == 3:
    print(f'\n*O número {dia} representa o dia de: [Terça-Feira].')
elif dia == 4:
    print(f'\n*O número {dia} representa o dia de: [Quarta-Feira].')
elif dia == 5:
    print(f'\n*O número {dia} representa o dia de: [Quinta-Feira].')
elif dia == 6:
    print(f'\n*O número {dia} representa o dia de: [Sexta-Feira].')
elif dia == 7:
    print(f'\n*O número {dia} representa o dia de: [Sabado].')
else:
    print(f'\nO valor do número está inválido!')
