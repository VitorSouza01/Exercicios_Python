"""
03. Faça um função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno será 1
se positivo, -1 se negativo e 0 se for igual a 0.
"""


def verificar_numero(numero):
    if numero > 0:
        numero = 1
        return f"O número é Positivo! O valor de retorno é: {numero}"

    elif numero < 0:
        numero = -1
        return f"O número é Negativo! O valor de retorno é: {numero}"

    else:
        numero = 0
        return f"O número é Indefinido! O valor de retorno é: {numero}"


numero = int(input("Digite um número inteiro: "))
print(verificar_numero(numero))
