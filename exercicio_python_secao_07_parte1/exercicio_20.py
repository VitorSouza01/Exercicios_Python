"""
20. Escreva um programa que leia números inteiros no intervalo [0,50]
e os armazene em um vetor com 10 posições. Preencha um segundo vetor
apenas com os números ímpares do primeiro vetor. Imprima os dois
vetores, 2 elementos por linha.
"""

import numpy as np

vetor = list(np.random.choice(np.arange(1, 10, 0.5), size=10))
print(f"Valor original do vetor: {vetor}")

vetor_impar = []

for numero in vetor:
    if numero % 2 != 0:
        if numero % 1 == 0:
            vetor_impar.append(numero)

print(f"Valor ímpar do vetor: {vetor_impar}")
