"""
52. Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente
ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada
apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base
no valor investido.
"""
print('DESCUBRA QUANTO GANHARIA - PRÊMIO DA LOTERIA!')
premio = float(input('\n- Digite o valor do prêmio:'))

aposta1 = float(input('*Digite o valor da aposta do 1º amigo:'))
aposta2 = float(input('*Digite o valor da aposta do 2º amigo:'))
aposta3 = float(input('*Digite o valor da aposta do 3º amigo:'))

apostatotal = aposta1 + aposta2 + aposta3

porcetagem1 = aposta1 / apostatotal
porcetagem2 = aposta2 / apostatotal
porcetagem3 = aposta3 / apostatotal

recebe1 = premio * porcetagem1
recebe2 = premio * porcetagem2
recebe3 = premio * porcetagem3

print(f'\nO 1º amigo vai receber R$[{recebe1}].')
print(f'O 2º amigo vai receber R$[{recebe2}].')
print(f'O 3º amigo vai receber R$[{recebe3}.]')

print(f'\nTotal:[{(recebe1 + recebe2 + recebe3)}].')
