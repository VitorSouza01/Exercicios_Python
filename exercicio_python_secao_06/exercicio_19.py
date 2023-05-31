""""
19. Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos que
compõem o número.
"""
while True:

    nmr = int(input("-Digite um número inteiro entre 100 e 999:"))

    if nmr > 100 and nmr < 999:
        break

    if nmr < 100 or nmr > 999:
        nmr = str(input("-O número informado está inválido! Tentar novamente?[sim/não]"))

    if nmr == "não":
        break

    elif nmr == "sim":
        print()

if nmr != "não":
    print()

    b = str(nmr)

    for i, v in enumerate(b):
        print(v)

elif nmr == "não":
    print()



