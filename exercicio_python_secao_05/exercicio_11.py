"""
11. Escreva um programa que leia um número inteiro maior do que zero e devolva,
na tela a soma de todos os seus algarismos. Por exemplo, ao número 251
corresponderá o valor 8(2+5+1). Se o número lido não for maior do que zero,
o programa terminará com a mensagem "Número inválido".
"""

print('- Veja os algarismos de um número e a soma deles!')
numero = int(input('Digite um número inteiro maior do que zero:'))
soma = 0

operacao = [int(a) for a in str(numero)]

if numero > 0:
    while(numero > 0):
        soma += numero % 10
        numero = int(numero /10)
    print(f'\n*Os algarismos são: {operacao} e sua soma é: [{soma}].')
elif numero < 0:
    print('Número Inválido!')







