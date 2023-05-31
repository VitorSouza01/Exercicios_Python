"""
17. Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem valores negativos.
"""

lp = 0
lst = []

while lp < 10:
    lp += 1
    vlr = int(input(f"Digite o {lp}º valor: "))
    lst.append(vlr)

for i, n in enumerate(lst):
  if n < 0 == 0:
    lst[i] = 0

print(lst)
