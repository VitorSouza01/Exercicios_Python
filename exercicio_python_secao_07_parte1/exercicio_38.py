"""
38. Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores, guardando-os
num vetor. Ordene o valor assim que ele for digitado. Mostre ao final na tela os valores em ordem.
"""

vtr = []

for i in range(10):
  nmr = float(input(f"Digite o {i+1}° valor: "))
  vtr.append(nmr)

nmr_odnd = sorted(vtr)

print(f"\nVetor Ordenados: {nmr_odnd}.")
