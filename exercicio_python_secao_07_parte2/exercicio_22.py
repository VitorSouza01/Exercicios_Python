"""
22. Faça um programa que leia duas matrizes A e B de tamanho 3 x 3 e calcule C = A * B.
"""

matriz_a, matriz_b, valor = [[], [], []], [[], [], []], 1

# Matriz A
print("Matriz A")
for n in range(3):
    for i in range(3):
        matriz_a[n].append(valor)
        valor += 1
[print(matriz_a[n]) for n in range(3)]

# Matriz B
print("\nMatriz B")
for n in range(3):
    for i in range(3):
        matriz_b[n].append(valor)
        valor += 1
[print(matriz_b[n]) for n in range(3)]


# Matriz parte 1
matriz_nova_soma_1 = [[], [], []]
for o in range(3):
    for p in range(3):
        matriz_nova_soma_1[o].append(matriz_a[o][p] * matriz_b[p][0])
for q in range(3):
    matriz_nova_soma_1[q] = sum(matriz_nova_soma_1[q])


# Matriz parte 2
matriz_nova_soma_2 = [[], [], []]
for r in range(3):
    for s in range(3):
        matriz_nova_soma_2[r].append(matriz_a[r][s] * matriz_b[s][1])
for t in range(3):
    matriz_nova_soma_2[t] = sum(matriz_nova_soma_2[t])


# Matriz parte 3
matriz_nova_soma_3 = [[], [], []]
for u in range(3):
    for v in range(3):
        matriz_nova_soma_3[u].append(matriz_a[u][v] * matriz_b[v][2])
for w in range(3):
    matriz_nova_soma_3[w] = sum(matriz_nova_soma_3[w])


# Matriz C
matriz_c = [[], [], []]
for x in range(3):
    matriz_c[x].append(matriz_nova_soma_1[x])
    matriz_c[x].append(matriz_nova_soma_2[x])
    matriz_c[x].append(matriz_nova_soma_3[x])
print("\nMultiplicação Matriz A * Matriz B;")
print("\nMatriz C")
[print(matriz_c[x]) for x in range(3)]
