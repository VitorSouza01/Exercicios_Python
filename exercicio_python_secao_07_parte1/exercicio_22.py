"""
22. Faça um programa que leia dois vetores de 10 posições e calcule
outro vetor contendo, nas posições pares os valores do primeiro e
nas posições impares os valores do segundo.
"""
""

vtr_a = []
vtr_b = []

for i in range(10):
    vlr_a = int(input(f"Digite o {i + 1}° valor do vetor A: "))
    vtr_a.append(vlr_a)
print("\n")

for i in range(10):
    vlr_b = int(input(f"Digite o {i + 1}° valor do vetor B: "))
    vtr_b.append(vlr_b)

vtr_c = []

for i in range(10):
    vtr_c.append(vtr_a[i])
    vtr_c.append(vtr_b[i])

print(f"\nVetor A: {vtr_a}")
print(f"Vetor B: {vtr_b}")
print(f"Vetor C: {vtr_c}")
