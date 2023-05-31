"""
47. Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
"""

print('[ Digite um número inteiro de 4 dígitos (De 1000 a 9999)! ]')
print('"Obs: Será imprimido 1 dígito por linha."')

numero = input(f'\n- Digite um número válido:')
numero_natural = int(numero)
numero_cortado = str(numero)

if numero_natural < 1000:
    print('\n*Digite um número válido entre 1000 a 9999.')
elif numero_natural <= 9999:
    print(f'\n*1º Dígito por linha [{numero_cortado[0]}].')
    print(f'*2º Dígito por linha [{numero_cortado[1]}].')
    print(f'*3º Dígito por linha [{numero_cortado[2]}].')
    print(f'*4º Dígito por linha [{numero_cortado[3]}].')
else:
    print('\n*Digite um número válido entre 1000 a 9999.')




