"""
07. Escreva um programa que leia 10 números inteiros e os armazena em um vetor. Imprima o vetor,
o maior elemento e a posição que ele se encontra.
"""

print("-Digite 10 números inteiros")

lp = 0
lst = []

while lp < 10:
    lp += 1
    vlr = int(input(f"Digete o {lp}º número: "))
    lst.append(vlr)
    mr_vtr = (max(lst))

print(f"\nValor do vetor: {lst}")
print(f"Maior valor do vetor: {mr_vtr}")

print(f"Posição do maior vetor: {lst.index(mr_vtr)}")
