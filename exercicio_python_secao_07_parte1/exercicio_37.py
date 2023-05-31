"""
37. Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 > ... > A11, ou seja, está
ordenado em ordem crescente até o sexte elemento, e a partir desse elemento está ordenado em ordem decrescente.
Dado o vetor da questão anterior, proponha um algoritmo para ordenar os elementos.
"""

vetor_cres = []
vetor_decr = []

for i in range(7):
    numero_cres = int(input(f"Digite o valor do {i+1}° número: "))
    vetor_cres.append(numero_cres)

for i in range(4):
    numero_decr = int(input(f"Digite o valor do {i+8}° número: "))
    vetor_decr.append(numero_decr)


vetor_decr.reverse()
vetor_total = vetor_cres + vetor_decr
print(f"\nVetor Original: {vetor_total}.")

vetor_total.sort()
print(f"Vetor Ordenado: {vetor_total}.")
