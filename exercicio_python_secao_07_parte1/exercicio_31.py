"""
31. Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a
 união entre os 2 vetores  anteriores, ou seja, que contém os números dos dois vetores.
  Não deve conter números repetidos.
"""

vetor1 = []
vetor2 = []

for i in range(10):
    numero1 = int(input(f"Digite o {i+1}º valor do Vetor 1: "))
    vetor1.append(numero1)

print("\n")

for i in range(10):
    numero2 = int(input(f"Digite o {i+1}º valor do Vetor 2: "))
    vetor2.append(numero2)

def union(vetor1, vetor2):
    vetor3 = list(set(vetor1) | set(vetor2))
    return vetor3

print(f"\nVetor 1: {vetor1}.")
print(f"Vetor 2: {vetor2}.")
print(f"União entre os Vetores (sem repetição): {union(vetor1, vetor2)}")
