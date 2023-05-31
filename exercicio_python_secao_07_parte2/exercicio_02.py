"""
02. Declare uma matriz 5x5. Preencha com 1 a diagonal principal e com 0 os demais elementos.
Escreva ao final a matriz obtida.
"""

matriz = [[0 for j in range(5)] for i in range(5)]

for i in range(5):
  matriz[i][i] = 1

print("Matriz Final obtida;")
for i in range(5):
  print(matriz[i])
