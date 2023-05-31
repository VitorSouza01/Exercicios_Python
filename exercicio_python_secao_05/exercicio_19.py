"""
19. Faça um programa para verificar se um determinado número inteiro e divisível
por 3 ou 5, mas não simultaneamente pelos dois.
"""

print('[ Descubra se um determinado número inteiro é divisível por 3 ou 5, mas não simultaneamente pelos dois. ]')
numero = int(input('-Digite um número inteiro:'))

if numero % 3 ==0:
    print(f'\nO número {numero} é divisível por 3!')
elif numero % 5 ==0:
    print(f'\nO número {numero} é divisível por 5!')
else:
    print(f'\nO número {numero} não é divisível tanto por 3 quanto 5!')

