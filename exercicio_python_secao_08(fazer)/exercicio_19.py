"""
19. Faça uma função que retorne o maior fator primo de um número.
"""


def maior_fator_primo(numero):

    fator = 2
    while fator * fator <= numero:
        if numero % fator == 0:
            numero/= fator
        else:
            fator += 1

    return f"\nO maior fator primo de {numero_inicial} é: {numero}."


numero = float(input("Digite um número: "))
numero_inicial = numero

print(maior_fator_primo(numero))
