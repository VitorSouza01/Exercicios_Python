"""
08. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.
"""

print("-Digite 6 números inteiros")

lp = 0
lst = []

while lp < 6:
    lp += 1
    vlr = int(input(f"Digete o {lp}º número: "))
    lst.append(vlr)

print(f"\nLista: {lst}")
lst.reverse()
print(f"Lista Inversa: {lst}")
