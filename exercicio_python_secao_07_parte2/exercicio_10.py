"""
10. Leia uma matriz 3 x 3 elementos. Calcule a soma dos elementos que estão na diagonal principal
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

matriz_diag_prin = []

for n in range(3):
  matriz_diag_prin.append(matriz[n][n])

print(f"\nSoma dos elementos que estão na diagonal principal; {sum(matriz_diag_prin)}")
