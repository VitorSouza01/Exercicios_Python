"""
12. Leia uma matriz 3 x 3 elementos. Calcule e imprima a sua transposta
"""
valor = 1
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(3):
  for j in range(3):
    matriz[i][j] = valor
    valor += 1

print("Matriz 3x3;")
print(matriz)

matriz_nova = [[], [], []]

for n in range(3):
    matriz_nova[0].append(matriz[n][0])

for m in range(3):
    matriz_nova[1].append(matriz[m][1])

for o in range(3):
    matriz_nova[2].append(matriz[o][2])

print("\nTransposta da Matriz 3x3;")
print(matriz_nova)
