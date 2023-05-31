"""
25. Faça uma função que receba um inteiro N como parâmetro, calcule e retorne o resultado da seguinte série:
S = 2/4 + 5/5 + 10/6 + ... + (N² + 1)/(N + 3)
"""


def calcular_serie(numero):
    s = 0
    for i in range(2, numero+1):
        numerorador = (i ** 2) + 1
        denomidor = i + 3

        s += numerorador / denomidor
    return f"Valor da série: {s}"


numero = int(input("Digite o número que será o parâmetro: "))
print(calcular_serie(numero))
