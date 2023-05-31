"""
17. Faça uma função que receba dois números inteiros positivos por parâmetro e retorne a soma dos N números inteiros
existentes entre eles.
"""


def soma_dos_numeros(numero_1, numero_2):
    for i in range(numero_1 + 1, numero_2):
        lista.append(i)
    return f"\nA dos números entre {numero_1} e {numero_2} é: {sum(lista)}."


numero_1 = int(input("Digite o valor inteiro positivo de Número 1 : "))
numero_2 = int(input("Digite o valor inteiro positivo de Número 2 : "))

lista = []

print(soma_dos_numeros(numero_1, numero_2))
