"""
06. Leia duas matrizes 4x4 e escreva uma terceira com os maiores valores de cada posição das matrizes lidas.
"""

matriz_1 = [[0 for linha in range(4)]
          for coluna in range(4)]

for linha in range(4):
    for coluna in range(4):
        matriz_1[linha][coluna] = int(input(f"Digite um valor para a Matriz 1 [{linha},{coluna}]: "))

print()

matriz_2 = [[0 for linha in range(4)]
            for coluna in range(4)]

for linha in range(4):
    for coluna in range(4):
        matriz_2[linha][coluna] = int(input(f"Digite um valor para a Matriz 2 [{linha}, {coluna}]: "))

print("\nMatriz 1;")
for linha in matriz_1:
    print(linha)

print("\nMatriz 2;")
for linha in matriz_2:
    print(linha)

matriz_3 = []
matriz_3.append(max(matriz_1))
matriz_3.append(max(matriz_2))

print("\nMatriz 3 - Com os maiores valores de cada posição das matrizes lidas;")
for linha in matriz_3:
    print(linha)


