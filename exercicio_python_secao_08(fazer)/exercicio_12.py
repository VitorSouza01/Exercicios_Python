"""
12. Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de todos os seus
algorismos. ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que zero,
o programa terminará com a mensagem "Número inválido".
"""


def soma_algorismo(numero):
    soma = 0
    for digit in str(numero):
        soma += int(digit)
    return f"\nA soma de todos os algarismos é: {soma}."


while True:
    numero = int(input("\nDigite um número maior do que 0: "))
    if numero > 0:
        break

    else:
        print("Número Inválido!")

print(soma_algorismo(numero))
