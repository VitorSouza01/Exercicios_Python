"""
08. Leia uma matriz 3 x 3 elementos. Calcule a soma dos elementos que estão acima da diagonal principal
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

for n in range(1):
  del matriz[n][n]

  for o in range(2):
    del matriz[n+1][n]

  for p in range(3):
    del matriz[o+1][n]

for q in range(3):
  matriz_diag_prin.append(sum(matriz[q]))

print(f"\nSoma dos elementos que estão acima da diagonal principal; {sum(matriz_diag_prin)}")
