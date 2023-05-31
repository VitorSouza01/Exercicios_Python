"""
32. Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saída o número
de cada dado e a relação entre eles (>,<,=) de cada lançamento.
"""
import random

print("[Lançamento de Dois Dados!]")
vzs = int(input("-Digite quantas vezes o dado vai ser lançado: "))
n = 0

while n < vzs:
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    n += 1
    print(f"[{n}° Lançamento!]")

    if d1 > d2:
        print(f"1° Dado seu valor é: {d1}.")
        print(f"2º Dado seu valor é: {d2}.")
        print(f"O valor do 1º Dado é Maior(>) do que o valor do 2° Dado.\n")
    elif d2 > d1:
        print(f"1° Dado seu valor é: {d1}.")
        print(f"2º Dado seu valor é: {d2}.")
        print(f"O valor do 1º Dado é Menor(<) do que o valor do 2° Dado.\n")
    elif d1 == d2:
        print(f"1° Dado seu valor é: {d1}.")
        print(f"2º Dado seu valor é: {d2}.")
        print(f"O valor do 1º Dado é Igual(=) ao valor do 2° Dado.\n")
