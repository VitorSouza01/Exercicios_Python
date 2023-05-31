"""
26. Faça um algoritmo que receba um número inteiro positivo N e calcule o somatório de 1 até N.
"""


def somatorio(numero):
    for i in range(1, numero+1):
        lista.append(i)
    return f"\nA soma de 1 até {numero} é: {sum(lista)}"


lista = []
numero = int(input("Digite um número inteiro positivo: "))
print(somatorio(numero))
