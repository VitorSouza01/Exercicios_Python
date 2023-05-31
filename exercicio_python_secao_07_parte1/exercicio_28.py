"""
28. Leia 10 números inteiros e armazene em um vetor V. Crie dois novos vetores V1 e V2.
Copie os valores ímpares de V para V1, e os valores pares de V para V2. Note que cada
um dos vetores V1 e  V2 tem no máximo 10 elementos, mas nem todos os elementos são
utilizados. No final escreva os elementos UTILIZADOS de V1 e V2.
"""

vtr0 = []
vtr1 = []
vtr2 = []

for i in range(10):
	nmr = int(input(f"Digite o {i+1} número inteiro: "))
	vtr0.append(nmr)

	if nmr % 2 == 0:
		vtr2.append(nmr)

	else:
		vtr1.append(nmr)

print(f"\nVetor V: {vtr0}")
print(f"Vetor V1(Ímpar): {vtr1}")
print(f"Vetor V2(Par): {vtr2}")
