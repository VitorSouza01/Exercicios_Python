"""
06. Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá
ser impresso o maior e o menor elemento do vetor.
"""

print("-Digite 10 números")

lp = 0
lst = []

while lp < 10:
    lp += 1
    vlr = int(input(f"Digete o {lp}º número: "))
    lst.append(vlr)

print(f"\nMaior valor do vetor: {(max(lst))}")
print(f"Menor valor do vetor: {(min(lst))}")
