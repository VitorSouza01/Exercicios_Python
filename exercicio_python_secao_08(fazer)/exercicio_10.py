"""
10. Faça uma função que receba dois números e retorne qual deles é o maior.
"""


def numero_maior(numero_a, numero_b):
    if numero_a > numero_b:
        return f"\nO número A '{numero_a}' é o maior!"
    return f"\nO número B '{numero_b}' é o maior!"


numero_a = float(input("Digite o número A: "))
numero_b = float(input("Digite o número B: "))

print(numero_maior(numero_a, numero_b))
