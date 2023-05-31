"""
03. Leia um número real. Se o número for positio imprima a raiz quadrada. Do contrário,
imprima o número ao quadrado.
"""

numero_real = float(input('* Digite um número real >'))

if numero_real > 0:
    print(f'\nO número {numero_real} é positivo, sua raiz quadrada é: [{(numero_real ** (1/2))}].')
else:
    print(f'\nO número {numero_real} é negativo, seu número ao quadrado é: [{numero_real * numero_real}].')

