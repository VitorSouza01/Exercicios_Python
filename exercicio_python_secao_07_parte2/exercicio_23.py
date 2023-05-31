"""
23. Faça um programa que leia uma matriz A de tamanho 3 x 3 e calcule B = A²
"""
matriz_a, matriz_b, matriz_nova_parte_1, matriz_nova_parte_2, matriz_nova_parte_3 = [[], [], []], [[], [], []], \
                                                                                [[], [], []], [[], [], []], [[], [], []]
valor = 1


# Matriz A
print("Matriz A")
for a in range(3):
    for b in range(3):
        matriz_a[a].append(valor)
        valor += 1
[print(matriz_a[c]) for c in range(3)]
matriz_a_copia = matriz_a


# Matriz nova parte 1
for d in range(3):
    for e in range(3):
        matriz_nova_parte_1[d].append(matriz_a[d][e] * matriz_a_copia[e][0])
for f in range(3):
    matriz_nova_parte_1[f] = sum(matriz_nova_parte_1[f])


# Matriz nova parte 2
for g in range(3):
    for h in range(3):
        matriz_nova_parte_2[g].append(matriz_a[g][h] * matriz_a_copia[h][1])
for i in range(3):
    matriz_nova_parte_2[i] = sum(matriz_nova_parte_2[i])


# Matriz nova parte 3
for j in range(3):
    for k in range(3):
        matriz_nova_parte_3[j].append(matriz_a[j][k] * matriz_a_copia[k][2])
for l in range(3):
    matriz_nova_parte_3[l] = sum(matriz_nova_parte_3[l])


# Matriz B
for n in range(3):
    matriz_b[n].append(matriz_nova_parte_1[n])
    matriz_b[n].append(matriz_nova_parte_2[n])
    matriz_b[n].append(matriz_nova_parte_3[n])
print("\nMatriz B = A²")
[print(matriz_b[m]) for m in range(3)]
