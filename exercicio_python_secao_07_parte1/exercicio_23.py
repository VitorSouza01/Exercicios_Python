"""
23. Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles.
Os conjuntos tem 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto
escalar é dado por:
x1 * y1 + x2 * y2 + ... + xn * yn.
"""

vtr1 = []
vtr2 = []

for i in range(5):
    vlr1 = float(input(f"Informe o {i+1}º valor do Vetor 1: "))
    vtr1.append(vlr1)

print("\n")

for i in range(5):
    vlr2 = float(input(f"Informe o {i+1}º valor do Vetor 2: "))
    vtr2.append(vlr2)

vtr_scl = []

for i in range(5):
    mlt = vtr1[i] * vtr2[i]
    vtr_scl.append(mlt)

print(f"\nConjunto do Vetor 1: {vtr1}")
print(f"Conjunto do Vetor 2: {vtr2}")
print(f"Conjunto do Produto Escalar: {vtr_scl}")
