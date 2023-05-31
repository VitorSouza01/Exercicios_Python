"""
21. Faça um programa que receba do usuário dois vetores, A e B, com
10 números inteiros cada. Crie um novo vetor denominado C calculando
C = A - B. Mostre na tela os dados do vetor C.
"""

vetor_a = []
vetor_b = []
vetor_c = []

for i in range(10):
	valor_a = int(input(f"Digite o {i+1}° número A: "))
	vetor_a.append(valor_a)
print("\n")

for i in range(10):
	valor_b = int(input(f"Digite o {i+1}° número B: "))
	vetor_b.append(valor_b)

valor_c = 0

for i in range(10):
	valor_c = vetor_a[i] - vetor_b[i]
	vetor_c.append(valor_c)

print(f"\nVetor A: {vetor_a}")
print(f"Vetor B: {vetor_b}")
print(f"Vetor C: {vetor_c}")

