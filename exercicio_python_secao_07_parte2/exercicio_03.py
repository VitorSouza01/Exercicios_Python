"""
03. Faça um programa que preencha uma matriz 4x4 com o produto do valor da linha da coluna de cada elemento.
Em seguida, imprima na tela a matriz.
"""

matriz = [[0 for j in range(4)]
          for i in range(4)]

for i in range(4):
  for j in range(4):
    matriz[i][j] = (i+1) * (j+1)

print("Matriz do Produto do Valor da Linha da Coluna de Cada Elemento")
for linha in matriz:
  print(linha)
