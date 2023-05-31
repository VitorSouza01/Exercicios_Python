"""
01. Faça um programa que possua um vetor denominado A que armazena 6 números inteiros.
O programa deve executar os seguintes passos:

(a) Atribua  os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
(b) Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0],
A[1], e A[5] do vetor e mostre na tela esta soma.
(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
(d) Mostre na tela cada valor do vetor A, um em cada linha.
"""

vet_a = [1, 0, 5, -2, -5, 7]
print(f"Valores do vetor: {vet_a}")

soma = vet_a[0] + vet_a[1] + vet_a[5]
print(f"\nSoma dos valores das posições [0], [1] e [5]: {soma}")

vet_a[4] = 100
print(f"\nNovo valor do vetor da posição [4]: {vet_a[4]}")

print("\nValor de cada vetor em cada linha:")
for linha in vet_a:
    print(linha)



