"""
45. Faça um programa para converter uma letra maiúscula em letra minúscula.
Use a tabela ASCII para resolver o problema.
"""
#32

print('¦ CONVERSOR DE LETRA MAIÚSCULA PARA LETRA MINÚSCULA ¦')
print('\n"Obs:Digite apenas letras em Maiúscula"')
letra_maiuscula = input('- Digite uma letra em Maiúscula:')

etapa1 = ord(letra_maiuscula) + 32
etapa2 = chr(etapa1)

print(f'\nLetra em minúscula [{etapa2}].')





