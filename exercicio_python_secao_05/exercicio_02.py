"""
02. Leia um número fornecido pelo úsuario. Se esse número for positivo, calcule a raiz
quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o
número é invalido.
"""

print(' - DESCUBRA A RAIZ QUADRADA DE UM NÚMERO! - ')
nmr = float(input('Digite um número >'))

if nmr > 0:
    print(f'\n- A raiz quadrada de ({nmr}) é: [{nmr ** (1/2)}]')
else:
    print(f'\n- O número digitado é invalido!')
