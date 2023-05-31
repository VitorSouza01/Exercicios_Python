"""
33. Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com valor zero.
Para isso, todos os elementos a frente do valor zero, devem ser movidos uma posição para trás no vetor.
"""

vtr = []

for i in range(15):
  nmr = int(input(f"Digite o {i+1}º número: "))
  vtr.append(nmr)

  if 0 in vtr:
    val_remove = 0
    vtr.remove(val_remove)

print(f"\nVetor com os zeros eliminados: : {vtr}.")
