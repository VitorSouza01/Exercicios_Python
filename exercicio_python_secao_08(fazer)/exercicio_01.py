"""
01. Crie uma função que recebe como parâmetro um número inteiro e devolve o seu dobro

"""


def numero_dobro(numero):
    dobro = numero * 2
    return f"O dobro de {numero} é: {dobro}."


numero = int(input("Digite um número: "))
print(numero_dobro(numero))
