"""
20. Faça um algoritmo que receba um número inteiro positivo N e calcule o seu fatorial, N!.
"""

import numpy


def fatorial(numero):

    for i in range(1, numero + 1):
        lista.append(i)

    resultado = numpy.prod(lista)
    return f"\nO Fatorial de {numero} é: {resultado}."


numero = int(input("Digete um número inteiro positivo: "))
lista = []

print(fatorial(numero))
