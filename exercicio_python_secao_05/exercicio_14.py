"""
14. A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e um
exame final. A média das três notas mencionadas anteriormente obedece aos pesos:
Trabalho de Labooratório: 2; Avaliação Semestral: 3; Exame Final: 5.
De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9),
de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

print('- DESCRUBRA SE VOCÊ FOI APROVADO!')

trabalho_de_laboratorio = float(input('\nDigite a sua nota referente ao trabalho de laboratório:'))
if trabalho_de_laboratorio > 10:
    print('*Nota Inválida!')
    exit()
avaliacao_semestral = float(input('Digite a sua nota referente a avaliação semestral:'))
if avaliacao_semestral > 10:
    print('*Nota Inválida!')
    exit()
exame_final = float(input('Digite a sua nota referente ao exame final:'))
if exame_final > 10:
    print('*Nota Inválida!')
    exit()

media = ((trabalho_de_laboratorio * 2) + (avaliacao_semestral * 3) + (exame_final * 5)) / (2+3+5)

if media < 2.9:
    print(f'\nVocê está de Reprovado!')
    print(f'Sua Média foi: [{media}].')
elif media < 4.9:
    print(f'\nVocê está de Recuperação!')
    print(f'Sua Média foi: [{media}].')
else:
    print(f'\nVocê está de Aprovado!')
    print(f'Sua Média foi: [{media}].')






