"""
26. Faça um programa que calcule o desvio padrão de um vetor V contendo N = 10 números, onde M é a média do vetor.
"""

import numpy as np

vtr = []

for i in range(10):
    nmr = int(input(f"Digite o {i+1}º número: "))
    vtr.append(nmr)

print(f"\nVetor: {vtr}.")
print(f"Desvio padrão do vetor: {np.std(vtr)}.")
