"""
21. Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação
escolhida. Escreva uma mensagem de erro se a opção for inválida.

Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 númertos.
4- Divisão entre 2 números (o denominador não pode ser zero).
Opção
"""

print('- MENU DE OPÇÕES!')
print('[1]SOMA (Entre 2 números)')
print('[2]DIFERENÇA (Entre 2 números, o maior pelo menor)')
print('[3]PRODUTO (Entre 2 números)')
print('[4]DIVISÃO (Entre 2 números, o denominador não pode ser zero)')

print('\n- Escolha dois números, e selecione a opção da operação mostrada a cima pelo seu número.')
numero1 = float(input('Digite o primeiro número:'))
operacao = float(input('Digite número da operação:'))
numero2 = float(input('Digite o segundo número:'))

if operacao == 1:
    print('\nVocê escolheu a Soma!')
    print(f'[ {numero1} + {numero2} = {(numero1+numero2)} ]')
elif operacao == 2:
    if numero1 > numero2:
        print('\nVocê escolheu a Diferença!')
        print(f'[ {numero1} - {numero2} = {(numero1-numero2)}]')
    elif numero2 > numero1:
        print('\nVocê escolheu a Diferença!')
        print(f'[ {numero2} - {numero1} = {(numero2-numero1)}]')
elif operacao == 3:
    print('\nVocê escolheu o Produto!')
    print(f'[ {numero1} * {numero2} = {(numero1*numero2)} ]')
elif operacao == 4:
    if numero2 > 0:
        print('\nVocê escolheu a Divisão!')
        print(f'[ {numero1} / {numero2} = {(numero1/numero2)} ]')
    else:
        print('\nVocê escolheu a Divisão!')
        print('Você digitou um número inválido, menor ou igual a zero!')
else:
    print('\n[ Erro! ]')
    print('[ Opção de Operação Inválida! ]')
