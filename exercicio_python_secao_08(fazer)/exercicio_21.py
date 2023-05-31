"""
21. Escreva uma função para determinar a quantidade de números primos abaixo N.
"""


def numeros_primos(numero):
    contagem = 0

    for n in range(2, numero):

        loop = True

        for i in range(2, n):
            if n % i == 0:
                loop = False
                break
        if loop:
            contagem += 1
            lista.append(n)

    return f"\nQuantidade de números primos: {contagem} = {lista} "


lista = []
numero = int(input("Digite um número positivo: "))

print(numeros_primos(numero))
