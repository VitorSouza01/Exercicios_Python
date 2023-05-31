"""
30. Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a
intersecção entre os 2 vetores anteriores, ou seja, que contém apenas os números
que estão em ambos os vetores. Não deve conter números repetidos.
"""

vtr1 = []
vtr2 = []

for i in range(10):
	nmr1= int(input(f"Digite o {i+1}° valor do Vetor 1: "))
	vtr1.append(nmr1)
print("\n")

for i in range(10):
	nmr2 = int(input(f"Digite o {i+1}° valor do Vetor 2: "))
	vtr2.append(nmr2)

vtr_itsc = set(vtr1) & set(vtr2)

print(f"\nVetor 1: {vtr1}.")
print(f"Vetor 2: {vtr2}.")
print(f"Vetor Intersecção: {vtr_itsc}.")
