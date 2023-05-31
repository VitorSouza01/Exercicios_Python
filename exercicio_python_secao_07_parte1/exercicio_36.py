"""
36. Leia um vetor com 10 números reai, ordene os elementos deste valor, e no final escreva os elementos do vetor
ordenado.
"""

vetor = []

for i in range(10):
  numero = int(input(f"Digite o {i+1}º número: "))
  vetor.append(numero)

vetor.sort()

print(f"\nVetor Ordenado: {vetor}")
