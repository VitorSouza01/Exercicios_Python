"""
34. Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20.
Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.
"""
from math import gcd

print("-Programa para calcular o menor número divisível por cada um dos números de 1 a 20;\n")

def mmc(numeros):
    m = 1
    for n in numeros:
        m = m * n // gcd(m, n)
    return m

print(mmc([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
