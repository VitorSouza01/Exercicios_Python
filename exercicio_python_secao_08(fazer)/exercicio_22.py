"""
22. Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas com pontos de exclamação,
conforme o exemplo abaixo (para n = 5):
!
!!
!!!
!!!!
!!!!!
"""


def saida(numero):
    for i in range(1, numero):
        print("!" * i)
    return "!" * numero


numero = int(input("Digite a quantidade de linhas usando a exclamação (!): "))
print()
print(saida(numero))
