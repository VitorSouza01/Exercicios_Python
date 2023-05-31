"""
08. Sejam A e B os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = √A²+B². Faça uma função que receba os valores de
A e B e calcule o valor da hipotenusa através da equação.
"""


def hipotenusa(valor_a, valor_b):
    return ((valor_a * valor_a) + (valor_b * valor_b)) ** (1/2)


valor_a = int(input("Digite o cateto A do triângulo: "))
valor_b = int(input("Digite o cateto B do triângulo: "))
print(f"\nO Valor da Hipotenusa é: {round(hipotenusa(valor_a, valor_b), 2)}")
